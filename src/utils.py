import pygame
import os
import shutil
import json
import time
import math
import requests
from main import username_txt_file, invalid_dir_chars, save_files_location, selected_continue_save_name, screen, save_detail_font_date, save_detail_font_nums, save_details, continue_screen_cords, calculate_recipe_pages, calculate_cocktail_pages, calculate_stock_pages, update_post, leaderboard_columns_font, leaderboard_items_font, leaderboard_row_cords, stock_pages, cocktail_pages, recipe_book_pages

def convert_asset(png_name, scale):
    return pygame.transform.scale_by(pygame.image.load(png_name).convert_alpha(), scale)

def slice_tilesheet(path, tile_width, tile_height):
    sheet = pygame.image.load(path).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()
    tiles = []
    for y in range(0, sheet_height, tile_height):
        for x in range(0, sheet_width, tile_width):
            rect = pygame.Rect(x, y, tile_width, tile_height)
            tile = sheet.subsurface(rect)
            tiles.append(tile)
    return tiles

def wrap_text_colored(segments, font, max_width):
    lines = []
    current_line = []
    current_width = 0

    for text, color in segments:
        words = text.split(" ")

        for i, word in enumerate(words):
            word_text = word + (" " if i < len(words) - 1 else "")
            word_width = font.size(word_text)[0]

            if current_width + word_width <= max_width:
                current_line.append((word_text, color))
                current_width += word_width
            else:
                lines.append(current_line)
                current_line = [(word_text, color)]
                current_width = word_width

    if current_line:
        lines.append(current_line)

    return lines

def draw_text_centered(surface, segments, font, rect):
    lines = wrap_text_colored(segments, font, rect.width)

    y_offset = rect.top
    returned_y_offset = 0

    for line in lines:
        total_width = sum(font.size(text)[0] for text, _ in line)
        x_offset = rect.centerx - total_width // 2

        for text, color in line:
            text_surf = font.render(text, True, color)
            surface.blit(text_surf, (x_offset, y_offset))
            x_offset += font.size(text)[0]

        y_offset += font.get_linesize()
        returned_y_offset += font.get_linesize()

    return returned_y_offset
    
def get_text_block_height(segments, font, max_width):
    lines = wrap_text_colored(segments, font, max_width)
    return len(lines) * font.get_linesize()

def write_username_file(username):
        with open(username_txt_file, "w") as f:
            f.write(username)

def check_valid_dir_input():
    global playthrough_name_text
    if playthrough_name_text == "":
        return False
    elif any(char in playthrough_name_text for char in invalid_dir_chars):
        return False
    elif os.path.isdir(f"save_files/{playthrough_name_text}"):
        return False
    else:
        return True

def delete_save(save_num):
    folder_counter = 0
    for folder in os.listdir(save_files_location):
        if save_num == folder_counter:
            shutil.rmtree(f"{save_files_location}/{folder}")
            break
        folder_counter += 1

def new_save():
    global username
    if playthrough_name_text != "data.json":
        os.mkdir(f"{save_files_location}/{playthrough_name_text}")
        basic_data = {"balance": balance, "customers_served": customers_served, "last_save": time.strftime("%m/%d/%Y"), "legit_playthrough": legit_playthrough, "best_cocktail_value": best_cocktail_value, "tier_recipes_available": tier_recipes_available}
        guest_data = {"guests": guests, "guest_available_spots": guest_available_spots, "first_save_done": first_save_done}
        unlocked_ingredients_data = unlocked_ingredients
        settings_data = settings
        unlocks_data = unlocks
        save_data = {
            **basic_data,
            **guest_data,
            "settings": settings_data,
            "ingredients": unlocked_ingredients_data,
            "unlocks": unlocks_data
            }
        with open(f"{save_files_location}/{playthrough_name_text}/data.json", "w") as f:
            json.dump(save_data, f)
        with open(username_txt_file, "r") as f:
            username = f.read()

def load_save():
    global balance, customers_served, unlocked_ingredients, settings, guests, guest_available_spots, first_save_done, unlocks, username, personal_recipes, drink_pic_lib, unlocked_drinks, stashed_cocktails, cocktail_available_spots, cur_menu, legit_playthrough, best_cocktail_value, tier_recipes_available
    with open(f"{save_files_location}/{selected_continue_save_name}/data.json", "r") as f:
        raw_unloaded_data = json.load(f)
        balance = raw_unloaded_data["balance"]
        customers_served = raw_unloaded_data["customers_served"]
        settings = raw_unloaded_data["settings"]
        unlocked_ingredients = raw_unloaded_data["ingredients"]
        unlocks = raw_unloaded_data["unlocks"]
        guests = raw_unloaded_data["guests"]
        guest_available_spots = raw_unloaded_data["guest_available_spots"]
        first_save_done = raw_unloaded_data["first_save_done"]
        personal_recipes = raw_unloaded_data["recipes"]
        drink_pic_lib = raw_unloaded_data["recipe_icons"]
        unlocked_drinks = raw_unloaded_data["unlocked_drinks"]
        stashed_cocktails = raw_unloaded_data["stashed_cocktails"]
        cocktail_available_spots = raw_unloaded_data["cocktail_available_spots"]
        cur_menu = raw_unloaded_data["cur_menu"]
        legit_playthrough = raw_unloaded_data["legit_playthrough"]
        best_cocktail_value = raw_unloaded_data["best_cocktail_value"]
        tier_recipes_available = raw_unloaded_data["tier_recipes_available"]

    with open(username_txt_file, "r") as f:
        username = f.read()
    calculate_recipe_pages()
    calculate_cocktail_pages()
    calculate_stock_pages()

def display_save_details():
    save_counter = 0
    for save in save_details:
        last_save_text = save_detail_font_date.render(str(save["last_save"]), True, (0,0,0))
        balance_text = save_detail_font_nums.render(f"${int(save['balance'])}", True, (0,0,0))
        customers_served_text = save_detail_font_nums.render(f"guests: {save['customers_served']}", True, (0,0,0))
        screen.blit(last_save_text, (410, continue_screen_cords[save_counter] + 70))
        screen.blit(balance_text, (870 - balance_text.get_width(), continue_screen_cords[save_counter] + 12))
        screen.blit(customers_served_text, (870 - customers_served_text.get_width(), continue_screen_cords[save_counter] + 65))
        save_counter += 1

def regular_save():
    basic_data = {"balance": balance, "customers_served": customers_served, "last_save": time.strftime("%m/%d/%Y"), "legit_playthrough": legit_playthrough, "best_cocktail_value": best_cocktail_value, "tier_recipes_available": tier_recipes_available}
    guest_data = {"guests": guests, "guest_available_spots": guest_available_spots, "first_save_done": first_save_done}
    unlocked_ingredients_data = unlocked_ingredients
    settings_data = settings
    unlocks_data = unlocks
    save_data = {
        **basic_data,
        **guest_data,
        "unlocks": unlocks_data,
        "ingredients": unlocked_ingredients_data,
        "settings": settings_data,
        "recipes": personal_recipes,
        "recipe_icons": drink_pic_lib,
        "unlocked_drinks": unlocked_drinks,
        "stashed_cocktails": stashed_cocktails,
        "cocktail_available_spots": cocktail_available_spots,
        "cur_menu": cur_menu
        }
    
    with open(f"{save_files_location}/{selected_continue_save_name}/data.json", "w") as f:
        json.dump(save_data, f)
    update_post()

def rond_af_5(n):
        return int(math.ceil(n / 5) * 5)
    
def rond_af_12(n):
    return int(math.ceil(n / 12) * 12)

def rond_af_4(n):
    return int(math.ceil(n / 4) * 4)

base_api_url = "https://cocktail-game-leaderboard-api.onrender.com"

def initial_post():
    try:
        name = username
        customers_served = 0
        best_cocktail_value = 0
        response = requests.post(f"{base_api_url}/initial_post", json={"name": name, "customers_served": customers_served, "best_cocktail_value": best_cocktail_value})
    except requests.exceptions.RequestException:
        return None
    
def update_post():
    if legit_playthrough:
        try:
            response = requests.post(f"{base_api_url}/update_post", json={"name": username, "customers_served": customers_served, "best_cocktail_value": best_cocktail_value})
        except requests.exceptions.RequestException:
            return None
    
def check_username_conflict(username):
    response = requests.post(f"{base_api_url}/check_conflict", json={"name": username})
    if response.json()["exists"]:
        return True
    else:
        return False

def get_leaderboard():
    global leaderboard_data
    try:
        response = requests.get(f"{base_api_url}/top3").json()
        leaderboard_data = []
        for row in response:
            name = row["name"]
            customers_served = row["customers_served"]
            best_cocktail_value = row["best_cocktail_value"]
            leaderboard_data.append({"name": name, "customers_served": customers_served, "best_cocktail_value": best_cocktail_value})
    except requests.exceptions.RequestException:
        return None

def display_leaderboard():
    if len(leaderboard_data) > 0:
        name_column_text = leaderboard_columns_font.render("name", True, (0,0,0))
        customers_served_column_text = leaderboard_columns_font.render("customers served", True, (0,0,0))
        best_cocktail_column_text = leaderboard_columns_font.render("best cocktail", True, (0,0,0))
        screen.blit(name_column_text, (493, 483))
        screen.blit(customers_served_column_text, (645, 483))
        screen.blit(best_cocktail_column_text, (843, 483))        
        row_counter = 0
        for row in leaderboard_data:
            name_text = leaderboard_items_font.render(str(row["name"]), True, (0,0,0))
            customers_served_text = leaderboard_items_font.render(str(row["customers_served"]), True, (0,0,0))
            best_cocktail_text = leaderboard_items_font.render(f"{row['best_cocktail_value']} $", True, (0,0,0))
            screen.blit(name_text, (470, leaderboard_row_cords[row_counter]))
            screen.blit(customers_served_text, (692, leaderboard_row_cords[row_counter]))
            screen.blit(best_cocktail_text, (867, leaderboard_row_cords[row_counter]))
            row_counter += 1
        pygame.draw.line(screen, (0, 0, 0), (468, 516), (935, 516), 2)
    else:
        error_text = leaderboard_columns_font.render("leaderboard unavailable", True, (0,0,0))
        screen.blit(error_text, (620, 500))

def calculate_stock_pages():
    stock_pages.clear()
    num_of_pages = rond_af_5(len(unlocked_ingredients)) // 5
    ingredients_left = len(unlocked_ingredients)
    ingredient_counter = 0
    for i in range(num_of_pages):
        stock_pages.append([])
    for page in stock_pages:
                if ingredients_left >= 5:
                    ingredients_left -= 5
                    for i in range(5):
                        page.append(unlocked_ingredients[ingredient_counter])
                        ingredient_counter += 1
                else:
                    for i in range(ingredients_left):
                        page.append(unlocked_ingredients[ingredient_counter])
                        ingredient_counter += 1

def calculate_cocktail_pages():
    cocktail_pages.clear()
    num_of_pages = rond_af_12(len(unlocked_ingredients)) // 12
    ingredients_left = len(unlocked_ingredients)
    ingredient_counter = 0
    for i in range(num_of_pages):
        cocktail_pages.append([])
    for page in cocktail_pages:
                if ingredients_left >= 12:
                    ingredients_left -= 12
                    for i in range(12):
                        page.append(unlocked_ingredients[ingredient_counter])
                        ingredient_counter += 1
                else:
                    for i in range(ingredients_left):
                        page.append(unlocked_ingredients[ingredient_counter])
                        ingredient_counter += 1

def calculate_recipe_pages():
    recipe_book_pages.clear()
    num_of_pages = rond_af_4(len(personal_recipes)) // 4
    recipes_left = len(personal_recipes)
    recipe_counter = 0
    for i in range(num_of_pages):
        recipe_book_pages.append([])
    for page in recipe_book_pages:
                if recipes_left >= 4:
                    recipes_left -= 4
                    for i in range(4):
                        page.append(personal_recipes[recipe_counter])
                        recipe_counter += 1
                else:
                    for i in range(recipes_left):
                        page.append(personal_recipes[recipe_counter])
                        recipe_counter += 1

def check_unlocks():
    if not unlocks["group1"] and customers_served == 5:
        unlocked_ingredients.append({"name": "tequila", "price": 6, "owned": 0})
        unlocked_ingredients.append({"name": "ginger beer", "price": 5, "owned": 0})
        unlocked_ingredients.append({"name": "grenadine", "price": 5, "owned": 0})
        unlocked_ingredients.append({"name": "lemon juice", "price": 2, "owned": 0})
        unlocked_ingredients.append({"name": "lime", "price": 2, "owned": 0})
        unlocked_ingredients.append({"name": "apple juice", "price": 2, "owned": 0})
    if not unlocks["group2"] and customers_served == 15:
        unlocked_ingredients.append({"name": "triple sec", "price": 8, "owned": 0})
        unlocked_ingredients.append({"name": "cranberry juice", "price": 2, "owned": 0})
        unlocked_ingredients.append({"name": "pineapple juice", "price": 2, "owned": 0})
        unlocked_ingredients.append({"name": "dark rum", "price": 7, "owned": 0})
        unlocked_ingredients.append({"name": "mango juice", "price": 2, "owned": 0})
    if not unlocks["group3"] and customers_served == 30:
        unlocked_ingredients.append({"name": "whiskey", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "amaretto", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "coconut cream", "price": 2, "owned": 0})
        unlocked_ingredients.append({"name": "egg white", "price": 2, "owned": 0})
        unlocked_ingredients.append({"name": "champagne", "price": 11, "owned": 0})
        unlocked_ingredients.append({"name": "passionfruit juice", "price": 2, "owned": 0})
    if not unlocks["group4"] and customers_served == 50:
        unlocked_ingredients.append({"name": "kahlúa", "price": 12, "owned": 0})
        unlocked_ingredients.append({"name": "cream", "price": 2, "owned": 0})
        unlocked_ingredients.append({"name": "baileys", "price": 13, "owned": 0})
        unlocked_ingredients.append({"name": "grapefruit juice", "price": 3, "owned": 0})
        unlocked_ingredients.append({"name": "bitters", "price": 3, "owned": 0})
    if not unlocks["group5"] and customers_served == 75:
        unlocked_ingredients.append({"name": "prosecco", "price": 14, "owned": 0})
        unlocked_ingredients.append({"name": "peach schnapps", "price": 15, "owned": 0})
        unlocked_ingredients.append({"name": "peach juice", "price": 3, "owned": 0})
        unlocked_ingredients.append({"name": "elderflower liqueur", "price": 14, "owned": 0})
    if not unlocks["group6"] and customers_served == 110:
        unlocked_ingredients.append({"name": "blue curaçao", "price": 17, "owned": 0})
        unlocked_ingredients.append({"name": "midori", "price": 18, "owned": 0})
    if not unlocks["group7"] and customers_served == 150:
        unlocked_ingredients.append({"name": "campari", "price": 20, "owned": 0})
        unlocked_ingredients.append({"name": "dry vermouth", "price": 19, "owned": 0})
        unlocked_ingredients.append({"name": "sweet vermouth", "price": 19, "owned": 0})
    if not unlocks["group8"] and customers_served == 200:
        unlocked_ingredients.append({"name": "absinthe", "price": 25, "owned": 0})

def cheat_unlocks():
    global unlocked_ingredients, customers_served
    customers_served = 400
    unlocked_ingredients.clear()
    # start ingredients
    unlocked_ingredients.append({"name": "vodka", "price": 5, "owned": 300})
    unlocked_ingredients.append({"name": "gin", "price": 5, "owned": 300})
    unlocked_ingredients.append({"name": "orange juice", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "white rum", "price": 5, "owned": 300})
    unlocked_ingredients.append({"name": "cola", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "tonic water", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "soda water", "price": 1, "owned": 300})
    unlocked_ingredients.append({"name": "lime juice", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "mint", "price": 1, "owned": 300})
    unlocked_ingredients.append({"name": "sugar syrup", "price": 1, "owned": 300})
    unlocked_ingredients.append({"name": "ice", "price": 1, "owned": 300})
    # group 1
    unlocked_ingredients.append({"name": "tequila", "price": 6, "owned": 300})
    unlocked_ingredients.append({"name": "ginger beer", "price": 5, "owned": 300})
    unlocked_ingredients.append({"name": "grenadine", "price": 5, "owned": 300})
    unlocked_ingredients.append({"name": "lemon juice", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "lime", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "apple juice", "price": 2, "owned": 300})
    # group 2
    unlocked_ingredients.append({"name": "triple sec", "price": 8, "owned": 300})
    unlocked_ingredients.append({"name": "cranberry juice", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "pineapple juice", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "dark rum", "price": 7, "owned": 300})
    unlocked_ingredients.append({"name": "mango juice", "price": 2, "owned": 300})
    # group 3
    unlocked_ingredients.append({"name": "whiskey", "price": 10, "owned": 300})
    unlocked_ingredients.append({"name": "amaretto", "price": 10, "owned": 300})
    unlocked_ingredients.append({"name": "coconut cream", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "egg white", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "champagne", "price": 11, "owned": 300})
    unlocked_ingredients.append({"name": "passionfruit juice", "price": 2, "owned": 300})
    # group 4
    unlocked_ingredients.append({"name": "kahlúa", "price": 12, "owned": 300})
    unlocked_ingredients.append({"name": "cream", "price": 2, "owned": 300})
    unlocked_ingredients.append({"name": "baileys", "price": 13, "owned": 300})
    unlocked_ingredients.append({"name": "grapefruit juice", "price": 3, "owned": 300})
    unlocked_ingredients.append({"name": "bitters", "price": 3, "owned": 300})
    # group 5
    unlocked_ingredients.append({"name": "prosecco", "price": 14, "owned": 300})
    unlocked_ingredients.append({"name": "peach schnapps", "price": 15, "owned": 300})
    unlocked_ingredients.append({"name": "peach juice", "price": 3, "owned": 300})
    unlocked_ingredients.append({"name": "elderflower liqueur", "price": 14, "owned": 300})
    # group 6
    unlocked_ingredients.append({"name": "blue curaçao", "price": 17, "owned": 300})
    unlocked_ingredients.append({"name": "midori", "price": 18, "owned": 300})
    # group 7
    unlocked_ingredients.append({"name": "campari", "price": 20, "owned": 300})
    unlocked_ingredients.append({"name": "dry vermouth", "price": 19, "owned": 300})
    unlocked_ingredients.append({"name": "sweet vermouth", "price": 19, "owned": 300})
    # group 8
    unlocked_ingredients.append({"name": "absinthe", "price": 25, "owned": 300})