#---------initiations---------

if True:
    import pygame
    import time
    import random
    import math
    import os
    import json
    from platformdirs import user_data_dir
    from copy import deepcopy
    import shutil

    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("cocktail game")
    clock = pygame.time.Clock()

#------loading in assets--------

if True:
    continue_button_img = pygame.transform.scale_by(pygame.image.load("assets/continue_button.png").convert_alpha(), 1)
    continue_button2_img = pygame.transform.scale_by(pygame.image.load("assets/continue_button.png").convert_alpha(), 2)
    new_button_img = pygame.transform.scale_by(pygame.image.load("assets/new_button.png").convert_alpha(), 1)
    settings_button_img = pygame.transform.scale_by(pygame.image.load("assets/settings_button.png").convert_alpha(), 1)
    exit_button_img = pygame.transform.scale_by(pygame.image.load("assets/exit_button.png").convert_alpha(), 1)
    back_button_img = pygame.transform.scale_by(pygame.image.load("assets/back_button.png").convert_alpha(), 1)
    plus_button_img = pygame.transform.scale_by(pygame.image.load("assets/plus_button.png").convert_alpha(), 1)
    min_button_img = pygame.transform.scale_by(pygame.image.load("assets/min_button.png").convert_alpha(), 1)
    buy_button_img = pygame.transform.scale_by(pygame.image.load("assets/buy_button.png").convert_alpha(), 1)
    create_button_img = pygame.transform.scale_by(pygame.image.load("assets/create_button.png").convert_alpha(), 1)
    save_button_img = pygame.transform.scale_by(pygame.image.load("assets/save_button.png").convert_alpha(), 1)
    save_exit_button_img = pygame.transform.scale_by(pygame.image.load("assets/save_exit_button.png").convert_alpha(), 1)

    continue_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/continue_button_clicked.png").convert_alpha(), 1)
    continue_button2_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/continue_button_clicked.png").convert_alpha(), 2)
    new_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/new_button_clicked.png").convert_alpha(), 1)
    settings_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/settings_button_clicked.png").convert_alpha(), 1)
    exit_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/exit_button_clicked.png").convert_alpha(), 1)
    back_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/back_button_clicked.png").convert_alpha(), 1)
    plus_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/plus_button_clicked.png").convert_alpha(), 1)
    min_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/min_button_clicked.png").convert_alpha(), 1)
    buy_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/buy_button_clicked.png").convert_alpha(), 1)
    create_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/create_button_clicked.png").convert_alpha(), 1)
    save_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/save_button_clicked.png").convert_alpha(), 1)
    save_exit_button_clicked_img = pygame.transform.scale_by(pygame.image.load("assets/save_exit_button_clicked.png").convert_alpha(), 1)

    startscreen_background_img = pygame.transform.scale_by(pygame.image.load("assets/startscreen_background.png").convert_alpha(), 1)
    settings_screen_background_img = pygame.transform.scale_by(pygame.image.load("assets/settings_screen_background.png").convert_alpha(), 1)
    guest_screen_background_img = pygame.transform.scale_by(pygame.image.load("assets/guest_screen_background.png").convert_alpha(), 1)
    stock_screen_background_img = pygame.transform.scale_by(pygame.image.load("assets/stock_screen_background.png").convert_alpha(), 1)
    progress_screen_background_img = pygame.transform.scale_by(pygame.image.load("assets/progress_screen_background.png").convert_alpha(), 1)
    cocktailmaker_background_img = pygame.transform.scale_by(pygame.image.load("assets/cocktailmaker_background.png").convert_alpha(), 1)
    homescreen_background_img = pygame.transform.scale_by(pygame.image.load("assets/homescreen_background.png").convert_alpha(), 1)

    checkmark_img = pygame.transform.scale_by(pygame.image.load("assets/checkmark.png").convert_alpha(), 1)
    right_arrow_img = pygame.transform.scale_by(pygame.image.load("assets/right_arrow.png").convert_alpha(), 1)
    left_arrow_img = pygame.transform.scale_by(pygame.image.load("assets/left_arrow.png").convert_alpha(), 1)

    default_font = pygame.font.SysFont('Calibri', 25)
    pixel_font_numbers = pygame.font.Font("assets/micro_5.ttf", 60)
    pixel_font_letters = pygame.font.Font("assets/Jersey10.ttf", 50)
    playthrough_name_font = pygame.font.Font("assets/Jersey10.ttf", 60)
    playthrough_text_font = pygame.font.Font("assets/Jersey10.ttf", 70)
    save_detail_font_date = pygame.font.Font("assets/Jersey10.ttf", 30)
    save_detail_font_nums = pygame.font.Font("assets/Jersey10.ttf", 40)

    vodka_icon_img = pygame.transform.scale_by(pygame.image.load("assets/vodka_icon.png").convert_alpha(), 1)
    orange_juice_icon_img = pygame.transform.scale_by(pygame.image.load("assets/orange_juice_icon.png").convert_alpha(), 1)
    champagne_icon_img = pygame.transform.scale_by(pygame.image.load("assets/champagne_icon.png").convert_alpha(), 1)
    water_icon_img = pygame.transform.scale_by(pygame.image.load("assets/water_icon.png").convert_alpha(), 1)
    whiskey_icon_img = pygame.transform.scale_by(pygame.image.load("assets/whiskey_icon.png").convert_alpha(), 1)
    gin_icon_img = pygame.transform.scale_by(pygame.image.load("assets/gin_icon.png").convert_alpha(), 1)

    guest1_img = pygame.transform.scale_by(pygame.image.load("assets/guest_1.png").convert_alpha(), 1)
    guest2_img = pygame.transform.scale_by(pygame.image.load("assets/guest_2.png").convert_alpha(), 1)
    guest3_img = pygame.transform.scale_by(pygame.image.load("assets/guest_3.png").convert_alpha(), 1)
    guest4_img = pygame.transform.scale_by(pygame.image.load("assets/guest_4.png").convert_alpha(), 1)
    guest5_img = pygame.transform.scale_by(pygame.image.load("assets/guest_5.png").convert_alpha(), 1)
    guest6_img = pygame.transform.scale_by(pygame.image.load("assets/guest_6.png").convert_alpha(), 1)
    guest7_img = pygame.transform.scale_by(pygame.image.load("assets/guest_7.png").convert_alpha(), 1)
    guest8_img = pygame.transform.scale_by(pygame.image.load("assets/guest_8.png").convert_alpha(), 1)
    
    stock_screen_row_img = pygame.transform.scale_by(pygame.image.load("assets/stock_screen_row.png").convert_alpha(), 1)

    cocktail_shaker_img = pygame.transform.scale_by(pygame.image.load("assets/cocktail_shaker.png").convert_alpha(), 2)
    cocktail_glass_img = pygame.transform.scale_by(pygame.image.load("assets/cocktail_glass.png").convert_alpha(), 1)

#-----------recipes-------------

if True:
    all_recipes_in_game = [
        {"name": "mojito",
        "price": 8,
        "makingprocess": {
            "ing1": {"name": "white rum", "amount": 6},
            "ing2": {"name": "lime juice", "amount": 4},
            "ing3": {"name": "sugar syrup", "amount": 2},
            "ing4": {"name": "soda water", "amount": 6},
            "ing5": {"name": "mint", "amount": 2},
            "ing6": {"name": "ice", "amount": 2}
        }},

        {"name": "cosmopolitan",
        "price": 11,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 8},
            "ing2": {"name": "triple sec", "amount": 4},
            "ing3": {"name": "cranberry juice", "amount": 6},
            "ing4": {"name": "lime juice", "amount": 2}
        }},

        {"name": "margarita",
        "price": 10,
        "makingprocess": {
            "ing1": {"name": "tequila", "amount": 10},
            "ing2": {"name": "triple sec", "amount": 4},
            "ing3": {"name": "lime juice", "amount": 6},
            "ing4": {"name": "ice", "amount": 1}
        }},

        {"name": "piña colada",
        "price": 12,
        "makingprocess": {
            "ing1": {"name": "white rum", "amount": 6},
            "ing2": {"name": "pineapple juice", "amount": 8},
            "ing3": {"name": "coconut cream", "amount": 6},
            "ing4": {"name": "ice", "amount": 2}
        }},

        {"name": "whiskey sour",
        "price": 9,
        "makingprocess": {
            "ing1": {"name": "whiskey", "amount": 9},
            "ing2": {"name": "lemon juice", "amount": 6},
            "ing3": {"name": "sugar syrup", "amount": 3},
            "ing4": {"name": "egg white", "amount": 2},
            "ing5": {"name": "ice", "amount": 1}
        }},

        {"name": "daiquiri",
        "price": 8,
        "makingprocess": {
            "ing1": {"name": "white rum", "amount": 10},
            "ing2": {"name": "lime juice", "amount": 6},
            "ing3": {"name": "sugar syrup", "amount": 4}
        }},

        {"name": "long island iced tea",
        "price": 14,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 2},
            "ing2": {"name": "gin", "amount": 2},
            "ing3": {"name": "white rum", "amount": 2},
            "ing4": {"name": "tequila", "amount": 2},
            "ing5": {"name": "triple sec", "amount": 2},
            "ing6": {"name": "lemon juice", "amount": 4},
            "ing7": {"name": "cola", "amount": 6},
            "ing8": {"name": "ice", "amount": 2}
        }},

        {"name": "tequila sunrise",
        "price": 9,
        "makingprocess": {
            "ing1": {"name": "tequila", "amount": 6},
            "ing2": {"name": "orange juice", "amount": 12},
            "ing3": {"name": "grenadine", "amount": 2},
            "ing4": {"name": "ice", "amount": 2}
        }},

        {"name": "screwdriver",
        "price": 7,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 6},
            "ing2": {"name": "orange juice", "amount": 14},
            "ing3": {"name": "ice", "amount": 2}
        }},

        {"name": "moscow mule",
        "price": 10,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 6},
            "ing2": {"name": "ginger beer", "amount": 12},
            "ing3": {"name": "lime juice", "amount": 2},
            "ing4": {"name": "ice", "amount": 2}
        }},

        {"name": "dark & stormy",
        "price": 11,
        "makingprocess": {
            "ing1": {"name": "dark rum", "amount": 8},
            "ing2": {"name": "ginger beer", "amount": 10},
            "ing3": {"name": "lime juice", "amount": 2},
            "ing4": {"name": "ice", "amount": 2}
        }},

        {"name": "amaretto sour",
        "price": 9,
        "makingprocess": {
            "ing1": {"name": "amaretto", "amount": 9},
            "ing2": {"name": "lemon juice", "amount": 6},
            "ing3": {"name": "sugar syrup", "amount": 3},
            "ing4": {"name": "egg white", "amount": 2},
            "ing5": {"name": "ice", "amount": 1}
        }},

        {"name": "sex on the beach",
        "price": 10,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 6},
            "ing2": {"name": "cranberry juice", "amount": 6},
            "ing3": {"name": "orange juice", "amount": 6},
            "ing4": {"name": "grenadine", "amount": 2},
            "ing5": {"name": "ice", "amount": 2}
        }},

        {"name": "gimlet",
        "price": 8,
        "makingprocess": {
            "ing1": {"name": "gin", "amount": 12},
            "ing2": {"name": "lime juice", "amount": 6},
            "ing3": {"name": "sugar syrup", "amount": 2}
        }},

        {"name": "espresso martini",
        "price": 13,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 8},
            "ing2": {"name": "kahlúa", "amount": 8},
            "ing3": {"name": "cream", "amount": 4}
        }},

        {"name": "white russian",
        "price": 12,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 8},
            "ing2": {"name": "kahlúa", "amount": 6},
            "ing3": {"name": "cream", "amount": 6},
            "ing4": {"name": "ice", "amount": 2}
        }},

        {"name": "porn star martini",
        "price": 15,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 7},
            "ing2": {"name": "amaretto", "amount": 3},
            "ing3": {"name": "pineapple juice", "amount": 5},
            "ing4": {"name": "lime juice", "amount": 2},
            "ing5": {"name": "champagne", "amount": 3}
        }},

        {"name": "gin & tonic",
        "price": 7,
        "makingprocess": {
            "ing1": {"name": "gin", "amount": 6},
            "ing2": {"name": "tonic water", "amount": 12},
            "ing3": {"name": "lime", "amount": 2},
            "ing4": {"name": "ice", "amount": 2}
        }},

        {"name": "cuba libre",
        "price": 8,
        "makingprocess": {
            "ing1": {"name": "white rum", "amount": 6},
            "ing2": {"name": "cola", "amount": 12},
            "ing3": {"name": "lime juice", "amount": 2},
            "ing4": {"name": "ice", "amount": 2}
        }},

        {"name": "french 75",
        "price": 13,
        "makingprocess": {
            "ing1": {"name": "gin", "amount": 6},
            "ing2": {"name": "lemon juice", "amount": 4},
            "ing3": {"name": "sugar syrup", "amount": 2},
            "ing4": {"name": "champagne", "amount": 8}
        }},

        {"name": "bellini prosecco",
        "price": 12,
        "makingprocess": {
            "ing1": {"name": "prosecco", "amount": 14},
            "ing2": {"name": "peach juice", "amount": 6}
        }},

        {"name": "peach fizz",
        "price": 9,
        "makingprocess": {
            "ing1": {"name": "peach schnapps", "amount": 6},
            "ing2": {"name": "orange juice", "amount": 8},
            "ing3": {"name": "soda water", "amount": 6},
            "ing4": {"name": "ice", "amount": 1}
        }},

        {"name": "blue lagoon",
        "price": 11,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 6},
            "ing2": {"name": "blue curaçao", "amount": 4},
            "ing3": {"name": "lemon juice", "amount": 2},
            "ing4": {"name": "soda water", "amount": 8},
            "ing5": {"name": "ice", "amount": 2}
        }},

        {"name": "blue margarita",
        "price": 12,
        "makingprocess": {
            "ing1": {"name": "tequila", "amount": 10},
            "ing2": {"name": "blue curaçao", "amount": 4},
            "ing3": {"name": "lime juice", "amount": 6},
            "ing4": {"name": "ice", "amount": 1}
        }},

        {"name": "midori sour",
        "price": 10,
        "makingprocess": {
            "ing1": {"name": "midori", "amount": 9},
            "ing2": {"name": "lemon juice", "amount": 6},
            "ing3": {"name": "sugar syrup", "amount": 3},
            "ing4": {"name": "egg white", "amount": 2},
            "ing5": {"name": "ice", "amount": 1}
        }},

        {"name": "japanese slipper",
        "price": 10,
        "makingprocess": {
            "ing1": {"name": "midori", "amount": 8},
            "ing2": {"name": "triple sec", "amount": 8},
            "ing3": {"name": "lemon juice", "amount": 4}
        }},

        {"name": "death in the afternoon",
        "price": 15,
        "makingprocess": {
            "ing1": {"name": "absinthe", "amount": 4},
            "ing2": {"name": "champagne", "amount": 16}
        }},

        {"name": "corpse reviver",
        "price": 13,
        "makingprocess": {
            "ing1": {"name": "gin", "amount": 7},
            "ing2": {"name": "triple sec", "amount": 5},
            "ing3": {"name": "absinthe", "amount": 1},
            "ing4": {"name": "lemon juice", "amount": 7}
        }},

        {"name": "negroni",
        "price": 12,
        "makingprocess": {
            "ing1": {"name": "gin", "amount": 7},
            "ing2": {"name": "campari", "amount": 7},
            "ing3": {"name": "sweet vermouth", "amount": 6},
            "ing4": {"name": "ice", "amount": 1}
        }},

        {"name": "americano",
        "price": 11,
        "makingprocess": {
            "ing1": {"name": "campari", "amount": 7},
            "ing2": {"name": "sweet vermouth", "amount": 7},
            "ing3": {"name": "soda water", "amount": 6},
            "ing4": {"name": "ice", "amount": 1}
        }},

        {"name": "dry martini",
        "price": 14,
        "makingprocess": {
            "ing1": {"name": "gin", "amount": 16},
            "ing2": {"name": "dry vermouth", "amount": 4}
        }},

        {"name": "manhattan",
        "price": 13,
        "makingprocess": {
            "ing1": {"name": "whiskey", "amount": 12},
            "ing2": {"name": "sweet vermouth", "amount": 6},
            "ing3": {"name": "bitters", "amount": 2}
        }},

        {"name": "hugo spritz",
        "price": 10,
        "makingprocess": {
            "ing1": {"name": "elderflower liqueur", "amount": 4},
            "ing2": {"name": "prosecco", "amount": 10},
            "ing3": {"name": "soda water", "amount": 4},
            "ing4": {"name": "mint", "amount": 2},
            "ing5": {"name": "ice", "amount": 1}
        }},

        {"name": "elderflower collins",
        "price": 9,
        "makingprocess": {
            "ing1": {"name": "gin", "amount": 6},
            "ing2": {"name": "elderflower liqueur", "amount": 4},
            "ing3": {"name": "lemon juice", "amount": 4},
            "ing4": {"name": "soda water", "amount": 6},
            "ing5": {"name": "ice", "amount": 2}
        }},

        {"name": "mango daiquiri",
        "price": 11,
        "makingprocess": {
            "ing1": {"name": "white rum", "amount": 8},
            "ing2": {"name": "mango juice", "amount": 6},
            "ing3": {"name": "lime juice", "amount": 4},
            "ing4": {"name": "sugar syrup", "amount": 2}
        }},

        {"name": "passion fruit mojito",
        "price": 10,
        "makingprocess": {
            "ing1": {"name": "white rum", "amount": 5},
            "ing2": {"name": "passion fruit juice", "amount": 4},
            "ing3": {"name": "lime juice", "amount": 3},
            "ing4": {"name": "sugar syrup", "amount": 2},
            "ing5": {"name": "soda water", "amount": 4},
            "ing6": {"name": "mint", "amount": 2},
            "ing7": {"name": "ice", "amount": 2}
        }},

        {"name": "peach bellini royale",
        "price": 12,
        "makingprocess": {
            "ing1": {"name": "peach schnapps", "amount": 4},
            "ing2": {"name": "peach juice", "amount": 6},
            "ing3": {"name": "prosecco", "amount": 10}
        }},

        {"name": "apple mule",
        "price": 10,
        "makingprocess": {
            "ing1": {"name": "vodka", "amount": 6},
            "ing2": {"name": "apple juice", "amount": 6},
            "ing3": {"name": "ginger beer", "amount": 6},
            "ing4": {"name": "lime juice", "amount": 2},
            "ing5": {"name": "ice", "amount": 2}
        }},

        {"name": "tropical sunrise",
        "price": 11,
        "makingprocess": {
            "ing1": {"name": "tequila", "amount": 6},
            "ing2": {"name": "mango juice", "amount": 7},
            "ing3": {"name": "passion fruit juice", "amount": 5},
            "ing4": {"name": "grenadine", "amount": 2},
            "ing5": {"name": "ice", "amount": 2}
        }},

        {"name": "green demon",
        "price": 12,
        "makingprocess": {
            "ing1": {"name": "midori", "amount": 5},
            "ing2": {"name": "vodka", "amount": 5},
            "ing3": {"name": "pineapple juice", "amount": 8},
            "ing4": {"name": "blue curaçao", "amount": 2},
            "ing5": {"name": "ice", "amount": 2}
        }}
    ]

#------button variables---------

if True:
    continue_button_rect = continue_button_img.get_rect(topleft=(50, 20))
    continue_button2_rect = continue_button2_img.get_rect(topleft=(WINDOW_WIDTH / 2 - continue_button2_img.get_width() / 2, 637))
    new_button_rect = new_button_img.get_rect(topleft=(continue_button_rect.right + 20, 20))
    exit_button_rect = exit_button_img.get_rect(topleft=(new_button_rect.right + 20, 20))
    back_button_rect = back_button_img.get_rect(topleft=(20, 20))
    back_button2_rect = back_button_img.get_rect(topleft=(10, 208 + 10))
    stock_screen_button_rect = pygame.Rect(68, 143, 221, 364)
    progress_screen_button_rect = pygame.Rect(WINDOW_WIDTH - 100 - 5, WINDOW_HEIGHT - 80, 50, 50) #PLACEHOLDER
    cocktailmaker_button_rect = pygame.Rect(547, 336, 143, 107)
    guest_screen_button_rect = pygame.Rect(777, 123, 182, 272)
    menu_screen_button_rect = pygame.Rect(1025, 475, 137, 209)
    plus_button_rect = plus_button_img.get_rect(topleft=(754, 544))
    min_button_rect = min_button_img.get_rect(topleft=(461, 544))
    stock_right_arrow_rect = right_arrow_img.get_rect(topleft=(1187, WINDOW_HEIGHT / 2 - left_arrow_img.get_height() / 2))
    stock_left_arrow_rect = left_arrow_img.get_rect(topleft=(58, WINDOW_HEIGHT / 2 - left_arrow_img.get_height() / 2))
    cocktail_right_arrow_rect = right_arrow_img.get_rect(topleft=(1142 + 25*2, 56))
    cocktail_left_arrow_rect = left_arrow_img.get_rect(topleft=(24 + 27, 56))
    buy_button_rect = buy_button_img.get_rect(topleft=(840, 544))
    create_button_rect = create_button_img.get_rect(topleft=(WINDOW_WIDTH / 2 - create_button_img.get_width() / 2, 500))
    save_button_rect = save_button_img.get_rect(topleft=(20, 20))
    save_exit_button_rect = save_exit_button_img.get_rect(topleft=(save_button_rect.right + 20, 20))
    settings_button_rect = settings_button_img.get_rect(topleft=(save_exit_button_rect.right + 20, 20))
    add_ingredient_button_rect = pygame.Rect(510, 355, 223, 314)
    cocktail_shaker_og_rect = cocktail_shaker_img.get_rect(topleft=(621 - cocktail_shaker_img.get_width() / 2, WINDOW_HEIGHT - 51 - cocktail_shaker_img.get_height()))
    cocktail_shaker_rect = cocktail_shaker_og_rect.copy()

    continue_button_clicked = False
    continue_button2_clicked = False
    new_button_clicked = False
    settings_button_clicked = False
    exit_button_clicked = False
    back_button_clicked = False
    plus_button_clicked = False
    min_button_clicked = False
    stock_button_clicked = False
    buy_button_clicked = False
    create_button_clicked = False
    save_button_clicked = False
    save_exit_button_clicked = False

    continue_button_clicktime = 0
    continue_button2_clicktime = 0
    new_button_clicktime = 0
    settings_button_clicktime = 0
    exit_button_clicktime = 0
    back_button_clicktime = 0
    plus_button_clicktime = 0
    min_button_clicktime = 0
    buy_button_clicktime = 0
    create_button_clicktime = 0
    save_button_clicktime = 0
    save_exit_button_clicktime = 0

    settings_devmode_checkmark_rect = checkmark_img.get_rect(topleft=(147, 97))
    settings_soundon_checkmark_rect = checkmark_img.get_rect(topleft=(147, 133))

#--------other variables--------

if True:
    click_duration = 80
    screen_switch_duration = 85
    running = True
    pos = (0,0)
    settings = {"dev_mode": True, "sound_on": True}
    guests = []
    guest_available_spots = []
    unlocked_ingredients = []
    locked_ingredients = []
    stock_page_displayed = 0
    cocktail_page_displayed = 0
    stock_screen_row_counter = 0
    customers_served = 0
    new_ingredient_unlocked = False
    stock_pages = []
    cocktail_pages = []
    stock_indicator_gap = 12
    cocktail_indicator_gap = 5
    save_indicator_gap = -6
    stock_amount_selected = 0
    playthrough_name_text = ""
    selected_continue_save = 0
    selected_overwrite_save = 0
    saves_amount = 0
    collision_rects_saves = []
    selected_continue_save_name = ""
    save_details = []
    invalid_dir_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', '.']
    custom_order_rect = 0
    first_save_done = False
    current_made_cocktail = {}
    backup_ingredients = {}
    current_cocktail_rects = []
    cocktail_glass_bottom = WINDOW_HEIGHT - 64
    cocktail_glass_width = 198
    cocktail_layer_height = 15
    cocktail_glass_middle = 621
    cocktail_done = False
    starting_shaker_cords = [500, 500]
    current_shaker_cords = starting_shaker_cords.copy()
    dragging = False
    unlocks = {}
    normal_guest_timer_range = [3, 23]
    sped_up_guest_timer_range = [1, 2]
    current_username_string = """"""

#--------random rects and lists--------

if True:
    stock_screen_row1_rect = stock_screen_row_img.get_rect(topleft=(189, 109))
    stock_screen_row2_rect = stock_screen_row_img.get_rect(topleft=(189, 196))
    stock_screen_row3_rect = stock_screen_row_img.get_rect(topleft=(189, 284))
    stock_screen_row4_rect = stock_screen_row_img.get_rect(topleft=(189, 371))
    stock_screen_row5_rect = stock_screen_row_img.get_rect(topleft=(189, 458))

    cocktailmaker_ing_spacing = 24

    cocktailmaker_ing_rects = []
    for i in range(12):
        x = 27 + cocktailmaker_ing_spacing * 2 + 35 + i * (66 + cocktailmaker_ing_spacing)
        cocktailmaker_ing_rects.append(pygame.Rect(x, 56, 66, 66))

    for i in range(9):
        unlocks[f"group{i}"] = False
                                                            
    stock_indicator_rect = pygame.Rect(stock_screen_row1_rect.x - stock_indicator_gap, stock_screen_row1_rect.y - stock_indicator_gap, stock_screen_row_img.get_width() + stock_indicator_gap * 2, stock_screen_row_img.get_height() + stock_indicator_gap * 2)
    cocktail_indicator_rect = pygame.Rect(cocktailmaker_ing_rects[0].x - cocktail_indicator_gap, cocktailmaker_ing_rects[0].y - cocktail_indicator_gap, cocktailmaker_ing_rects[0].width + 2 * cocktail_indicator_gap, cocktailmaker_ing_rects[0].height + 2 * cocktail_indicator_gap)

    new_playthrough_rect_big = pygame.Rect((WINDOW_WIDTH - 600) / 2, 220, 600, 400)
    new_playthrough_rect_small = pygame.Rect((WINDOW_WIDTH - 400) / 2, 400, 400, 70)

    stock_screen_row_cords = [109, 196, 284, 371, 458]
    continue_screen_cords = [100, 235, 370, 505]

    unlocked_ingredients = (
        {"name": "vodka", "price": 10, "owned": 0},
        {"name": "gin", "price": 15, "owned": 0},
        {"name": "orange juice", "price": 4, "owned": 0},
        {"name": "white rum", "price": 6, "owned": 0},
        {"name": "cola", "price": 3, "owned": 0},
        {"name": "tonic water", "price": 7, "owned": 0},
        {"name": "soda water", "price": 4, "owned": 0},
        {"name": "lime juice", "price": 2, "owned": 0},
        {"name": "mint", "price": 4, "owned": 0},
        {"name": "sugar syrup", "price": 9, "owned": 0},
        {"name": "ice", "price": 1, "owned": 0})

    guest1_rect = guest1_img.get_rect(topleft=(100,360))
    guest2_rect = guest1_img.get_rect(topleft=(guest1_rect.right + 70, 360))
    guest3_rect = guest1_img.get_rect(topleft=(guest2_rect.right + 70, 360))
    guest4_rect = guest1_img.get_rect(topleft=(guest3_rect.right + 70, 360))
    guest5_rect = guest1_img.get_rect(topleft=(guest4_rect.right + 70, 360))
    guest6_rect = guest1_img.get_rect(topleft=(guest5_rect.right + 70, 360))

    guest_order1_rect = pygame.Rect(guest1_rect.x - 20, 332, 150, 100)
    guest_order2_rect = pygame.Rect(guest2_rect.x - 20, 332, 150, 100)
    guest_order3_rect = pygame.Rect(guest3_rect.x - 20, 332, 150, 100)
    guest_order4_rect = pygame.Rect(guest4_rect.x - 20, 332, 150, 100)
    guest_order5_rect = pygame.Rect(guest5_rect.x - 20, 332, 150, 100)
    guest_order6_rect = pygame.Rect(guest6_rect.x - 20, 332, 150, 100)
    
    drink_icon_library = {  
                            "vodka": vodka_icon_img,
                            "gin": gin_icon_img,
                            "orange juice": orange_juice_icon_img,
                            "white rum": whiskey_icon_img,
                            "cola": vodka_icon_img,
                            "tonic water": water_icon_img,
                            "soda water": water_icon_img,
                            "lime juice": vodka_icon_img,
                            "mint": vodka_icon_img,
                            "sugar syrup": vodka_icon_img,
                            "ice": water_icon_img,
                            "dark rum": vodka_icon_img,
                            "tequila": vodka_icon_img,
                            "whiskey": vodka_icon_img,
                            "triple sec": vodka_icon_img,
                            "amaretto": vodka_icon_img,
                            "kahlúa": vodka_icon_img,
                            "baileys": vodka_icon_img,
                            "champagne": vodka_icon_img,
                            "prosecco": vodka_icon_img,
                            "peach schnapps": vodka_icon_img,
                            "blue curaçao": vodka_icon_img,
                            "midori": vodka_icon_img,
                            "absinthe": vodka_icon_img,
                            "dry vermouth": vodka_icon_img,
                            "sweet vermouth": vodka_icon_img,
                            "campari": vodka_icon_img,
                            "elderflower liqueur": vodka_icon_img,
                            "pineapple juice": vodka_icon_img,
                            "cranberry juice": vodka_icon_img,
                            "lemon juice": vodka_icon_img,
                            "grapefruit juice": vodka_icon_img,
                            "apple juice": vodka_icon_img,
                            "mango juice": vodka_icon_img,
                            "passion fruit juice": vodka_icon_img,
                            "peach juice": vodka_icon_img,
                            "grenadine": vodka_icon_img,
                            "coconut cream": vodka_icon_img,
                            "ginger beer": vodka_icon_img,
                            "egg white": vodka_icon_img,
                            "cream": vodka_icon_img,
                            "lime": vodka_icon_img,
                            "mint": vodka_icon_img,
                            "bitters": vodka_icon_img
                            }
    
    guest_rects_library = { 1: guest1_rect,
                            2: guest2_rect,
                            3: guest3_rect,
                            4: guest4_rect,
                            5: guest5_rect,
                            6: guest6_rect}
    
    guest_order_rects_library = {1: guest_order1_rect,
                                 2: guest_order2_rect,
                                 3: guest_order3_rect,
                                 4: guest_order4_rect,
                                 5: guest_order5_rect,
                                 6: guest_order6_rect}

    guest_images_library = { 1: guest1_img,
                             2: guest2_img,
                             3: guest3_img,
                             4: guest4_img,
                             5: guest5_img,
                             6: guest6_img,
                             7: guest7_img,
                             8: guest8_img}

    ingredient_color_library = {
        # spirits
        "white rum":            (195, 230, 220),
        "dark rum":             (101, 55,  20),
        "gin":                  (180, 220, 235),
        "vodka":                (160, 200, 230),
        "tequila":              (195, 210, 130),
        "whiskey":              (180, 100, 30),
        "triple sec":           (255, 200, 50),
        "amaretto":             (160, 60,  10),
        "kahlúa":               (45,  20,  5),
        "baileys":              (210, 165, 90),
        "champagne":            (220, 195, 60),
        "prosecco":             (210, 185, 55),
        "peach schnapps":       (255, 160, 60),
        "blue curaçao":         (0,   120, 210),
        "midori":               (40,  200, 60),
        "absinthe":             (60,  150, 40),
        "dry vermouth":         (190, 195, 80),
        "sweet vermouth":       (160, 45,  20),
        "campari":              (200, 30,  20),
        "elderflower liqueur":  (190, 210, 80),

        # juices
        "orange juice":         (240, 130, 20),
        "pineapple juice":      (225, 195, 20),
        "cranberry juice":      (170, 10,  40),
        "lime juice":           (100, 185, 30),
        "lemon juice":          (220, 200, 20),
        "grapefruit juice":     (230, 100, 50),
        "apple juice":          (150, 190, 40),
        "mango juice":          (245, 140, 10),
        "passion fruit juice":  (210, 100, 10),
        "peach juice":          (230, 130, 50),

        # syrups & sweet
        "sugar syrup":          (180, 210, 140),
        "grenadine":            (190, 10,  40),
        "coconut cream":        (160, 210, 185),

        # sodas
        "cola":                 (45,  20,  5),
        "tonic water":          (140, 190, 220),
        "ginger beer":          (195, 160, 60),
        "soda water":           (130, 175, 210),

        # other
        "egg white":            (200, 210, 160),
        "cream":                (210, 185, 100),
        "lime":                 (80,  165, 30),
        "mint":                 (30,  140, 40),
        "bitters":              (110, 40,  15),
        "ice":                  (0,   0,   0)
    }

#---------text formatting----------

if True:
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

#---------guest logic----------

if True:
    pos_sentences = ["give me a ", "i want a ", "i need a ", "can i get a ", "could you give me a ", "would you do your job and give me a ", "immediately give me a ", "make a ", "i desire a ", "i would love a ", "i want to get drunk so give me a ",
                    "stop being a jackass and give me a ", "i will die if you dont give me a ", "just give me a ", "bring me a ", "i don't have a lot of time, i just want a "]

    cur_menu = ["mojito", "margarita", "cosmopolitan"]

    positions = [
        1, 
        2, 
        3, 
        4, 
        5, 
        6,
    ]

    guest_available_spots = [1, 2, 3, 4, 5, 6]
    guests = []
    guest_images_list = [1, 2, 3, 4, 5, 6, 7, 8]
    temp_guest_spawn_wait = 0
    temp_guest_timer = 0
    balance = 0
    x = -1

    def client_request_completed(client_name, star_multiplier):
        global guests, balance, customers_served

        customers_served += 1

        for guest in guests:
            if guest["name"] == client_name:
                balance += guest["price"] * star_multiplier
                guest_available_spots.append(guest["rect_num"])
                guests.remove(guest)
                break

    temp_price = 0

    def refresh(added_guest_number):
        global x, custom_order_rect

        x = random.randint(1, 999999999999999999999)

        want = random.choice(cur_menu)
        temp_price = 0
        
        for recipe in all_recipes_in_game:
            if recipe["name"] == want:
                temp_price = recipe["price"]
                break

        spoken_sentence = random.choice(pos_sentences)
        
        for position_num in positions:
            if position_num == added_guest_number:
                segments = [(spoken_sentence, (0, 0, 0)), (want, (0, 136, 209))]
                custom_order_rect = guest_order_rects_library[position_num].copy()
                height = get_text_block_height(segments, default_font, guest_order_rects_library[position_num].width)
                order_rect_y = guest_order_rects_library[position_num].y
                order_rect_y -= height
                guests.append({
                    "name": f"guest{x}",
                    "image_num": random.randint(1,8),
                    "rect_num": position_num,
                    "order_rect_y": order_rect_y,
                    "clicked": False,
                    "order_text": spoken_sentence,
                    "order_item": want,
                    "price": temp_price
                })
                guest_available_spots.remove(position_num)
                break

    if first_save_done == False:
        for position_num in positions:
            x += 1
            want2 = random.choice(cur_menu)
            temp_price2 = 0
            
            for recipe in all_recipes_in_game:
                if recipe["name"] == want2:
                    temp_price2 = recipe["price"]
                    break

            spoken_sentence2 = random.choice(pos_sentences)
            segments = [(spoken_sentence2, (0, 0, 0)), (want2, (0, 136, 209))]
            height = get_text_block_height(segments,default_font,150)
            order_rect_y = guest_order_rects_library[position_num].y
            order_rect_y -= height
            guests.append({
                "name": f"guest{x}",
                "image_num": random.randint(1,8),
                "rect_num": position_num,
                "order_rect_y": order_rect_y,
                "clicked": False,
                "order_text": spoken_sentence2,
                "order_item": want2,
                "price": temp_price2
            })
            guest_available_spots.remove(position_num)

#----------rating + recognition logic----------

if True:
    unlocked_recipes = []
    
    def add_to_menu(drink):
        cur_menu.append(drink)

    def calculate_stars(calc_list):
        if calc_list == []:
            return 999999
        else:
            return sum(calc_list)

    def drink_check(used_ing,):
        building_score = []
        for recipe in all_recipes_in_game:
            recipe_ingredients = [ing["name"] for ing in recipe["makingprocess"].values()]
            
            if set(recipe_ingredients) == set(used_ing.keys()):
                print("you succesfully made a " + recipe["name"])

                if (recipe["name"]) not in unlocked_recipes:
                    unlocked_recipes.append(recipe["name"])
                    print("new recipe unlocked")
                
                for ing in recipe["makingprocess"].values():
                    name = ing["name"]
                    required = ing["amount"]
                    used = used_ing[name]

                    building_score.append(abs(used - required))

        total_dif = calculate_stars(building_score)
        print("your total difference is " + str(total_dif))
        
        match total_dif:
                case 0:
                    return 10
                case 1 | 2 | 3:
                    return 9
                case 4 | 5:
                    return 8
                case 6 | 7:
                    return 7
                case 8 | 9 | 10:
                    return 6
                case 11 | 12 | 13:
                    return 5
                case 14 | 15 | 16 | 17:
                    return 4
                case 18 | 19 | 20:
                    return 3
                case 21 | 22 | 23:
                    return 2
                case 24 | 25 | 26:
                    return 1
                case 999999:
                    return -1
                case _:
                    return 0

#----------file saving----------

if True:
    def rond_af_5(n):
        return int(math.ceil(n / 5) * 5)
    
    def rond_af_12(n):
        return int(math.ceil(n / 12) * 12)

    save_files_location = f"{user_data_dir('cocktail_game', 'DTstudios')}/save_files"
    username_txt_file = f"{user_data_dir('cocktail_game', 'DTstudios')}/username.txt"

    os.makedirs(save_files_location, exist_ok=True)
                
    if not os.path.exists(username_txt_file):
        open(username_txt_file, "w").close()
        screen_displayed_now = "username"
    else:
        screen_displayed_now = "startscreen"

    saves_amount = 0
    for folder in os.listdir(save_files_location):
        collision_rects_saves.append(pygame.Rect(WINDOW_WIDTH / 2 - 500 / 2, continue_screen_cords[saves_amount], 500, 120))
        saves_amount += 1

    def  write_username_file(username):
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
        os.mkdir(f"{save_files_location}/{playthrough_name_text}")
        basic_data = {"balance": balance, "customers_served": customers_served, "dev_mode": str(settings["dev_mode"]), "sound_on": str(settings["sound_on"]), "last_save": time.strftime("%m/%d/%Y")}
        guest_data = {"key": "value"} #TWAN
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
        global balance, customers_served, unlocked_ingredients, settings, guests, guest_available_spots, first_save_done, unlocks, username
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
        calculate_stock_pages()
        with open(username_txt_file, "r") as f:
            username = f.read()
    
    def display_save_details():
        save_counter = 0
        for save in save_details:
            last_save_text = save_detail_font_date.render(str(save["last_save"]), True, (0,0,0))
            balance_text = save_detail_font_nums.render(f"${save['balance']}", True, (0,0,0))
            customers_served_text = save_detail_font_nums.render(f"guests: {save['customers_served']}", True, (0,0,0))
            screen.blit(last_save_text, (410, continue_screen_cords[save_counter] + 70))
            screen.blit(balance_text, (700, continue_screen_cords[save_counter] + 12))
            screen.blit(customers_served_text, (700, continue_screen_cords[save_counter] + 65))
            save_counter += 1

    def regular_save():
        basic_data = {"balance": balance, "customers_served": customers_served, "last_save": time.strftime("%m/%d/%Y")}
        guest_data = {"guests": guests, "guest_available_spots": guest_available_spots, "first_save_done": first_save_done}
        unlocked_ingredients_data = unlocked_ingredients
        settings_data = settings
        unlocks_data = unlocks
        save_data = {
            **basic_data,
            **guest_data,
            "unlocks": unlocks_data,
            "ingredients": unlocked_ingredients_data,
            "settings": settings_data
            }
        with open(f"{save_files_location}/{selected_continue_save_name}/data.json", "w") as f:
            json.dump(save_data, f)
    
#-------stock screen page calculations-------

if True:
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
    calculate_stock_pages()
    selected_stock_ingredient = stock_pages[0][0]
    selected_stock_ingredient_page = 0

#------cocktailmaker page calculations------

if True:
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
        calculate_cocktail_pages()
        selected_cocktail_ingredient = cocktail_pages[0][0]
        selected_cocktail_ingredient_page = 0

#----------progression system---------

def check_unlocks():
    if not unlocks["group1"] and customers_served == 5:
        unlocked_ingredients.append({"name": "tequila", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "ginger beer", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "grenadine", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "lemon juice", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "lime", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "apple juice", "price": 10, "owned": 0})
    if not unlocks["group2"] and customers_served == 15:
        unlocked_ingredients.append({"name": "triple sec", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "cranberry juice", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "pineapple juice", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "dark rum", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "mango juice", "price": 10, "owned": 0})
    if not unlocks["group3"] and customers_served == 30:
        unlocked_ingredients.append({"name": "whiskey", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "amaretto", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "coconut cream", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "egg white", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "champagne", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "passion fruit juice", "price": 10, "owned": 0})
    if not unlocks["group4"] and customers_served == 50:
        unlocked_ingredients.append({"name": "kahlúa", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "cream", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "baileys", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "grapefruit juice", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "bitters", "price": 10, "owned": 0})
    if not unlocks["group5"] and customers_served == 75:
        unlocked_ingredients.append({"name": "prosecco", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "peach schnapps", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "peach juice", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "elderflower liqueur", "price": 10, "owned": 0})
    if not unlocks["group6"] and customers_served == 110:
        unlocked_ingredients.append({"name": "blue curaçao", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "midori", "price": 10, "owned": 0})
    if not unlocks["group7"] and customers_served == 150:
        unlocked_ingredients.append({"name": "campari", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "dry vermouth", "price": 10, "owned": 0})
        unlocked_ingredients.append({"name": "sweet vermouth", "price": 10, "owned": 0})
    if not unlocks["group8"] and customers_served == 200:
        unlocked_ingredients.append({"name": "absinthe", "price": 10, "owned": 0})

#---------display functions----------

if True:

    def display_startscreen():
        global continue_button_clicked, continue_button_clicktime, pos, settings_button_clicked, exit_button_clicked, settings_button_clicktime, exit_button_clicktime, screen_displayed_now, running, transition_this_frame, new_button_clicked, new_button_clicktime, save_details, playthrough_name_text
        #---------button logic----------
        
        if not transition_this_frame:
            if left_mouse_clicked and continue_button_rect.collidepoint(pos):
                continue_button_clicked = True
                continue_button_clicktime = now
            if left_mouse_clicked and exit_button_rect.collidepoint(pos):
                exit_button_clicked = True
                exit_button_clicktime = now
            if left_mouse_clicked and new_button_rect.collidepoint(pos):
                new_button_clicked = True
                new_button_clicktime = now
            
        if continue_button_clicktime != 0 and continue_button_clicktime <= now - click_duration:
            continue_button_clicked = False
        if exit_button_clicktime != 0 and exit_button_clicktime <= now - click_duration:
            exit_button_clicked = False
        if new_button_clicktime != 0 and new_button_clicktime <= now - click_duration:
            new_button_clicked = False

        if continue_button_clicktime != 0 and continue_button_clicktime <= now - screen_switch_duration:
            continue_button_clicktime = 0
            transition_this_frame = True
            continue_button_clicktime = 0
            for folder in os.listdir(save_files_location):
                    with open(f"{save_files_location}/{folder}/data.json", "r") as f:
                        raw_unloaded_data = json.load(f)
                    save_details.append({"last_save": raw_unloaded_data["last_save"], "balance": raw_unloaded_data["balance"], "customers_served": raw_unloaded_data["customers_served"]})
            if len(save_details) > 0:
                screen_displayed_now = "continue_screen"
        if exit_button_clicktime != 0 and exit_button_clicktime <= now - screen_switch_duration:
            exit_button_clicktime = 0
            running = False
            exit_button_clicktime = 0
        if new_button_clicktime != 0 and new_button_clicktime <= now - screen_switch_duration:
            new_button_clicktime = 0
            screen_displayed_now = "new_screen"
            transition_this_frame = True
            playthrough_name_text = ""

        #----------displaying-----------
        
        screen.blit(startscreen_background_img, (0,0))
        screen.blit(continue_button_clicked_img if continue_button_clicked else continue_button_img, continue_button_rect)
        screen.blit(exit_button_clicked_img if exit_button_clicked else exit_button_img, exit_button_rect)
        screen.blit(new_button_clicked_img if new_button_clicked else new_button_img, new_button_rect)

    def display_settings_screen():
        global back_button_clicktime, back_button_clicked, screen_displayed_now, settings, transition_this_frame
        #---------button logic----------

        if not transition_this_frame:
            if left_mouse_clicked and back_button_rect.collidepoint(pos):
                back_button_clicked = True
                back_button_clicktime = now
            
            if left_mouse_clicked and settings_devmode_checkmark_rect.collidepoint(pos):
                settings["dev_mode"] = not settings["dev_mode"]
            if left_mouse_clicked and settings_soundon_checkmark_rect.collidepoint(pos):
                settings["sound_on"] = not settings["sound_on"]
        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "homescreen"
            transition_this_frame = True
            back_button_clicktime = 0


        #----------displaying-----------

        screen.blit(settings_screen_background_img, (0,0))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        if settings["dev_mode"]:
            screen.blit(checkmark_img, settings_devmode_checkmark_rect)
        if settings["sound_on"]:
            screen.blit(checkmark_img, settings_soundon_checkmark_rect)

    def display_new_playthrough():
        global back_button_clicked, back_button_clicktime, screen_displayed_now, transition_this_frame, create_button_clicked, create_button_clicktime, playthrough_name_text, playthrough_name_rendered_text, selected_continue_save_name
        #----------button logic--------

        if not transition_this_frame:
            if left_mouse_clicked and back_button_rect.collidepoint(pos):
                back_button_clicked = True
                back_button_clicktime = now

        if left_mouse_clicked and create_button_rect.collidepoint(pos):
            create_button_clicked = True
            create_button_clicktime = now

        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False
        if create_button_clicktime != 0 and create_button_clicktime <= now - click_duration:
            create_button_clicked = False

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "startscreen"
            transition_this_frame = True
        
        if create_button_clicktime != 0 and create_button_clicktime <= now - screen_switch_duration:
            create_button_clicktime = 0
            if check_valid_dir_input():
                transition_this_frame = True
                with os.scandir(save_files_location) as entries:
                    folder_count = sum(1 for entry in entries if entry.is_dir())
                print(folder_count)
                if folder_count == 4:
                    screen_displayed_now = "overwrite_screen"
                    for folder in os.listdir(save_files_location):
                        with open(f"{save_files_location}/{folder}/data.json", "r") as f:
                            raw_unloaded_data = json.load(f)
                        save_details.append({"last_save": raw_unloaded_data["last_save"], "balance": raw_unloaded_data["balance"], "customers_served": raw_unloaded_data["customers_served"]})
                else:
                    screen_displayed_now = "homescreen"
                    selected_continue_save_name = playthrough_name_text
                    new_save()
                    playthrough_name_text = ""
                print(folder_count)

        #----------displaying----------
        
        screen.fill((0, 89, 76))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        screen.blit(create_button_clicked_img if create_button_clicked else create_button_img, create_button_rect)
        playthrough_name_rendered_text = playthrough_name_font.render(playthrough_name_text, True, (0,0,0))
        screen.blit(playthrough_name_rendered_text, (448, 401))
        playthrough_text1 = playthrough_text_font.render("new save file", True, (0,0,0))
        playthrough_text2 = playthrough_text_font.render("save name:", True, (0,0,0))
        screen.blit(playthrough_text1, (476, 230))
        screen.blit(playthrough_text2, (504, 300))
        pygame.draw.rect(screen, (255,255,255), new_playthrough_rect_big, 1, border_radius=10)
        pygame.draw.rect(screen, (255,255,255), new_playthrough_rect_small, 1, border_radius=10)

    def display_continue_playthrough():
        global back_button_clicked, back_button_clicktime, screen_displayed_now, transition_this_frame, continue_button2_clicktime, continue_button2_clicked, selected_continue_save, selected_continue_save_name, new_ingredient_unlocked
        
        #----------button logic--------

        if not transition_this_frame:
            if left_mouse_clicked and back_button_rect.collidepoint(pos):
                back_button_clicked = True
                back_button_clicktime = now

        if left_mouse_clicked and continue_button2_rect.collidepoint(pos):
            continue_button2_clicked = True
            continue_button2_clicktime = now

        rect_counter = 0
        if left_mouse_clicked:
            for rect in collision_rects_saves:
                if rect.collidepoint(pos):
                    selected_continue_save = rect_counter
                rect_counter += 1

        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False
        if continue_button2_clicktime != 0 and continue_button2_clicktime <= now - click_duration:
            continue_button2_clicked = False

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "startscreen"
            transition_this_frame = True
            back_button_clicktime = 0
        if continue_button2_clicktime != 0 and continue_button2_clicktime <= now - screen_switch_duration:
            continue_button2_clicktime = 0
            folder_count = 0
            for folder in os.listdir(save_files_location):
                if folder_count == selected_continue_save:
                    selected_continue_save_name = folder
                folder_count += 1
            screen_displayed_now = "homescreen"
            new_ingredient_unlocked = True
            load_save()


        #----------save logic------------
        
        #----------displaying----------

        screen.fill((0, 89, 76))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        screen.blit(continue_button2_clicked_img if continue_button2_clicked else continue_button2_img, continue_button2_rect)
        row_counter = 0
        text = playthrough_text_font.render("choose a save:", True, (0,0,0))
        screen.blit(text, (450, 15))
        for folder in os.listdir(save_files_location):
            continue_folder_rect = pygame.Rect(WINDOW_WIDTH / 2 - 500 / 2, continue_screen_cords[row_counter], 500, 120)
            pygame.draw.rect(screen, (255,255,255), continue_folder_rect, 1, border_radius=4)
            name_text = playthrough_name_font.render(folder, True, (0,0,0))
            screen.blit(name_text, (continue_folder_rect.x + 20, continue_screen_cords[row_counter] + 4))
            row_counter += 1
        continue_indicator_rect = pygame.Rect(continue_folder_rect.x - save_indicator_gap, continue_screen_cords[selected_continue_save] - save_indicator_gap, 500 + 2 * save_indicator_gap, 120 + 2 * save_indicator_gap)
        pygame.draw.rect(screen, (0,0,0), continue_indicator_rect, 3, border_radius=4)
        display_save_details()

    def display_overwrite_playthrough():
        global back_button_clicked, back_button_clicktime, screen_displayed_now, transition_this_frame, continue_button2_clicked, continue_button2_clicktime, overwrite_indicator_rect, selected_overwrite_save
        #----------button logic--------

        if not transition_this_frame:
            if left_mouse_clicked and back_button_rect.collidepoint(pos):
                back_button_clicked = True
                back_button_clicktime = now

        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False

        if left_mouse_clicked and continue_button2_rect.collidepoint(pos):
            continue_button2_clicked = True
            continue_button2_clicktime = now

        if continue_button2_clicktime != 0 and continue_button2_clicktime <= now - click_duration:
            continue_button2_clicked = False

        if continue_button2_clicktime != 0 and continue_button2_clicktime <= now - screen_switch_duration:
            continue_button2_clicktime = 0
            delete_save(selected_overwrite_save)
            new_save()
            screen_displayed_now = "homescreen"

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "startscreen"
            transition_this_frame = True
            back_button_clicktime = 0

        rect_counter = 0
        for rect in collision_rects_saves:
            if left_mouse_clicked and rect.collidepoint(pos):
                selected_overwrite_save = rect_counter
            rect_counter += 1

        #----------displaying----------

        screen.fill((0, 89, 76))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        screen.blit(continue_button2_clicked_img if continue_button2_clicked else continue_button2_img, continue_button2_rect)
        row_counter = 0
        text = playthrough_text_font.render("overwrite a save:", True, (0,0,0))
        screen.blit(text, (450, 15))
        for folder in os.listdir(save_files_location):
            continue_folder_rect = pygame.Rect(WINDOW_WIDTH / 2 - 500 / 2, continue_screen_cords[row_counter], 500, 120)
            pygame.draw.rect(screen, (255,255,255), continue_folder_rect, 1, border_radius=4)
            name_text = playthrough_name_font.render(folder, True, (0,0,0))
            screen.blit(name_text, (continue_folder_rect.x + 20, continue_screen_cords[row_counter] + 4))
            row_counter += 1
        overwrite_indicator_rect = pygame.Rect(WINDOW_WIDTH / 2 - 500 / 2 - save_indicator_gap, continue_screen_cords[selected_overwrite_save] - save_indicator_gap, 500 + save_indicator_gap * 2, 120 + save_indicator_gap * 2)
        pygame.draw.rect(screen, (0,0,0), overwrite_indicator_rect, 3, border_radius=4)
        display_save_details()

    def display_homescreen():
        global screen_displayed_now, progress_rect, selected_cocktail_ingredient, selected_cocktail_ingredient_page, backup_ingredients, transition_this_frame, running, settings_button_clicked, settings_button_clicktime, save_button_clicked, save_button_clicktime, save_exit_button_clicked, save_exit_button_clicktime
        #--------button variables--------

        if left_mouse_clicked and stock_screen_button_rect.collidepoint(pos):
            screen_displayed_now = "stock_screen"
            calculate_stock_pages()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if left_mouse_clicked and progress_screen_button_rect.collidepoint(pos):
            progress_rect = pygame.Rect(54, 514, min(1172, max(5, math.ceil(customers_served * 5.87))), 28)
            screen_displayed_now = "progress_screen"
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if left_mouse_clicked and cocktailmaker_button_rect.collidepoint(pos):
            screen_displayed_now = "cocktailmaker"
            calculate_cocktail_pages()
            selected_cocktail_ingredient = cocktail_pages[0][0]
            selected_cocktail_ingredient_page = 0
            cocktail_indicator_rect.x = cocktailmaker_ing_rects[0].x - cocktail_indicator_gap
            backup_ingredients = list(deepcopy(unlocked_ingredients))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if left_mouse_clicked and guest_screen_button_rect.collidepoint(pos):
            screen_displayed_now = "guest_screen"
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if left_mouse_clicked and menu_screen_button_rect.collidepoint(pos):
            screen_displayed_now = "menu_screen"
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if stock_screen_button_rect.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif guest_screen_button_rect.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif cocktailmaker_button_rect.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif menu_screen_button_rect.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif progress_screen_button_rect.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        if left_mouse_clicked and save_button_rect.collidepoint(pos):
            save_button_clicked = True
            save_button_clicktime = now
        if left_mouse_clicked and save_exit_button_rect.collidepoint(pos):
            save_exit_button_clicked = True
            save_exit_button_clicktime = now
        if left_mouse_clicked and settings_button_rect.collidepoint(pos):
            settings_button_clicked = True
            settings_button_clicktime = now

        if save_button_clicktime != 0 and save_button_clicktime <= now - click_duration:
            save_button_clicked = False
            regular_save()
        if settings_button_clicktime != 0 and settings_button_clicktime <= now - click_duration:
            settings_button_clicked = False
        if save_exit_button_clicktime != 0 and save_exit_button_clicktime <= now - click_duration:
            save_exit_button_clicked = False

        if save_exit_button_clicktime != 0 and save_exit_button_clicktime <= now - screen_switch_duration:
            save_exit_button_clicktime = 0
            regular_save()
            running = False
        if settings_button_clicktime != 0 and settings_button_clicktime <= now - screen_switch_duration:
            settings_button_clicktime = 0
            screen_displayed_now = "settings"
            transition_this_frame = True
            settings_button_clicktime = 0

        #----------displaying----------

        screen.blit(homescreen_background_img, (0,0))
        screen.blit(save_button_clicked_img if save_button_clicked else save_button_img, save_button_rect)
        screen.blit(save_exit_button_clicked_img if save_exit_button_clicked else save_exit_button_img, save_exit_button_rect)
        screen.blit(settings_button_clicked_img if settings_button_clicked else settings_button_img, settings_button_rect)
        username_text = save_detail_font_nums.render(username, True, (255,255,255))
        screen.blit(username_text, (WINDOW_WIDTH - 10 - username_text.get_width(), 10))
        pygame.draw.rect(screen, (100, 0, 0), progress_screen_button_rect, 1)

    def display_menu_screen():
        screen.fill((255,0,0))

    def display_stock_screen(): 
        global back_button_clicked, back_button_clicktime, screen_displayed_now, transition_this_frame, plus_button_clicked, plus_button_clicktime, min_button_clicked, min_button_clicktime, stock_screen_row_counter, stock_page_displayed, selected_stock_ingredient, selected_stock_ingredient_page, buy_button_clicked, buy_button_clicktime, stock_amount_selected, balance
        
        #---------button logic---------
        
        if left_mouse_clicked and back_button_rect.collidepoint(pos):
            back_button_clicked = True
            back_button_clicktime = now
        if left_mouse_clicked and plus_button_rect.collidepoint(pos):
            plus_button_clicked = True
            plus_button_clicktime = now
            stock_amount_selected += 1
        if left_mouse_clicked and min_button_rect.collidepoint(pos):
            min_button_clicked = True
            min_button_clicktime = now
            if stock_amount_selected > 0:
                stock_amount_selected -= 1
        if left_mouse_clicked and stock_right_arrow_rect.collidepoint(pos) and stock_page_displayed + 1 < len(stock_pages):
            stock_page_displayed += 1
        if left_mouse_clicked and stock_left_arrow_rect.collidepoint(pos) and stock_page_displayed - 1 > -1:
            stock_page_displayed -= 1
        if left_mouse_clicked and buy_button_rect.collidepoint(pos):
            buy_button_clicked = True
            buy_button_clicktime = now
            if balance - selected_stock_ingredient["price"] * stock_amount_selected >= 0:
                balance -= selected_stock_ingredient["price"] * stock_amount_selected
                for ingredient in unlocked_ingredients:
                    if ingredient["name"] == selected_stock_ingredient["name"]:
                        ingredient["owned"] += stock_amount_selected
                        break

        if left_mouse_clicked and stock_screen_row1_rect.collidepoint(pos):
            selected_stock_ingredient = stock_pages[stock_page_displayed][0]
            selected_stock_ingredient_page = stock_page_displayed
            stock_indicator_rect.y = stock_screen_row1_rect.y - stock_indicator_gap
        if left_mouse_clicked and stock_screen_row2_rect.collidepoint(pos):
            selected_stock_ingredient = stock_pages[stock_page_displayed][1]
            selected_stock_ingredient_page = stock_page_displayed
            stock_indicator_rect.y = stock_screen_row2_rect.y - stock_indicator_gap
        if left_mouse_clicked and stock_screen_row3_rect.collidepoint(pos):
            selected_stock_ingredient = stock_pages[stock_page_displayed][2]
            selected_stock_ingredient_page = stock_page_displayed
            stock_indicator_rect.y = stock_screen_row3_rect.y - stock_indicator_gap
        if left_mouse_clicked and stock_screen_row4_rect.collidepoint(pos):
            selected_stock_ingredient = stock_pages[stock_page_displayed][3]
            selected_stock_ingredient_page = stock_page_displayed
            stock_indicator_rect.y = stock_screen_row4_rect.y - stock_indicator_gap
        if left_mouse_clicked and stock_screen_row5_rect.collidepoint(pos):
            selected_stock_ingredient = stock_pages[stock_page_displayed][4]
            selected_stock_ingredient_page = stock_page_displayed
            stock_indicator_rect.y = stock_screen_row5_rect.y - stock_indicator_gap
        
        stock_page_displayed = max(0, stock_page_displayed)
        stock_page_displayed = min(stock_page_displayed, rond_af_5(len(unlocked_ingredients)) / 5)

        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False
        if plus_button_clicktime != 0 and plus_button_clicktime <= now - click_duration:
            plus_button_clicked = False
        if min_button_clicktime != 0 and min_button_clicktime <= now - click_duration:
            min_button_clicked = False
        if buy_button_clicktime != 0 and buy_button_clicktime <= now - click_duration:
            buy_button_clicked = False
        
        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            screen_displayed_now = "homescreen"
            transition_this_frame = True
            back_button_clicktime = 0

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        #----------displaying---------

        screen.blit(stock_screen_background_img, (0,0))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        screen.blit(plus_button_clicked_img if plus_button_clicked else plus_button_img, plus_button_rect)
        screen.blit(min_button_clicked_img if min_button_clicked else min_button_img, min_button_rect)
        screen.blit(buy_button_clicked_img if buy_button_clicked else buy_button_img, buy_button_rect)
        if stock_page_displayed + 1 < len(stock_pages):
            screen.blit(right_arrow_img, stock_right_arrow_rect)
        if stock_page_displayed - 1 > -1:
            screen.blit(left_arrow_img, stock_left_arrow_rect)
        if stock_page_displayed == selected_stock_ingredient_page:
            pygame.draw.rect(screen, (255,255,255), stock_indicator_rect, 1)
        balance_text = pixel_font_numbers.render(f"${balance}", True, (0,0,0))
        screen.blit(balance_text, (198, 547))
        stock_amount_selected_text = pixel_font_numbers.render(str(stock_amount_selected), True, (0,0,0))
        screen.blit(stock_amount_selected_text, (570, 547))
        for dict in stock_pages[stock_page_displayed]:
            screen.blit(stock_screen_row_img, (189, stock_screen_row_cords[stock_screen_row_counter]))
            screen.blit(drink_icon_library[dict["name"]], (189, stock_screen_row_cords[stock_screen_row_counter]))
            name_text = pixel_font_letters.render(dict["name"], True, (0,0,0))
            screen.blit(name_text, (320, stock_screen_row_cords[stock_screen_row_counter] + 5))
            price_text = pixel_font_numbers.render(f"${dict['price']}", True, (0,0,0))
            screen.blit(price_text, (702, stock_screen_row_cords[stock_screen_row_counter] + 3))
            owned_text = pixel_font_numbers.render(str(dict["owned"]), True, (0,0,0))
            screen.blit(owned_text, (935, stock_screen_row_cords[stock_screen_row_counter] + 3))
            stock_screen_row_counter += 1
        stock_screen_row_counter = 0

    def display_cocktailmaker():
        global back_button_clicktime, back_button_clicked, screen_displayed_now, settings, transition_this_frame, cocktail_page_displayed, selected_cocktail_ingredient_page, selected_cocktail_ingredient, current_made_cocktail, unlocked_ingredients, current_cocktail_rects, cocktail_done, cocktail_shaker_rect
        #-------button logic---------

        if not transition_this_frame:
            if left_mouse_clicked and back_button2_rect.collidepoint(pos):
                back_button_clicked = True
                back_button_clicktime = now

        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "homescreen"
            transition_this_frame = True
            back_button_clicktime = 0
            current_made_cocktail = {}
            current_cocktail_rects = []
            unlocked_ingredients = list(deepcopy(backup_ingredients))
            backup_ingredients.clear()
            cocktail_done = False
            cocktail_shaker_rect = cocktail_shaker_og_rect.copy()

        if cocktail_page_displayed != 0:
            if left_mouse_clicked and cocktail_left_arrow_rect.collidepoint(pos):
                cocktail_page_displayed -= 1

        if cocktail_page_displayed != len(cocktail_pages) - 1:
            if left_mouse_clicked and cocktail_right_arrow_rect.collidepoint(pos):
                cocktail_page_displayed += 1

        col_check_rect_count = 0
        for rect in cocktailmaker_ing_rects:
            if left_mouse_clicked and rect.collidepoint(pos) and len(cocktail_pages[cocktail_page_displayed]) - 1 >= col_check_rect_count:
                selected_cocktail_ingredient = cocktail_pages[cocktail_page_displayed][col_check_rect_count]
                cocktail_indicator_rect.x = cocktailmaker_ing_rects[col_check_rect_count].x - cocktail_indicator_gap
                selected_cocktail_ingredient_page = cocktail_page_displayed
            col_check_rect_count += 1

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if cocktail_done:
            if cocktail_shaker_rect.collidepoint(pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if not cocktail_done:
            if left_mouse_clicked and add_ingredient_button_rect.collidepoint(pos) and selected_cocktail_ingredient["owned"] > 0:
                ingredient_name = selected_cocktail_ingredient["name"]
                do_add = False
                if ingredient_name not in current_made_cocktail:
                    current_made_cocktail[ingredient_name] = 1
                    selected_cocktail_ingredient["owned"] -= 1
                    do_add = True
                else:
                    if ingredient_name == "ice" and current_made_cocktail["ice"] >= 2:
                        pass
                    else:
                        current_made_cocktail[ingredient_name] += 1
                        selected_cocktail_ingredient["owned"] -= 1
                        do_add = True
                if do_add:
                    if len(current_cocktail_rects) == 0:
                        current_cocktail_rects.append({
                            "name": ingredient_name,
                            "rect": pygame.Rect(cocktail_glass_middle - cocktail_glass_width / 2 + 1, cocktail_glass_bottom - cocktail_layer_height, cocktail_glass_width, cocktail_layer_height),
                            "color": ingredient_color_library[ingredient_name]
                        })
                    else:
                        if current_cocktail_rects[-1]["name"] == ingredient_name:
                            current_cocktail_rects[-1]["rect"].height += cocktail_layer_height
                            current_cocktail_rects[-1]["rect"].y -= cocktail_layer_height
                        else:
                            current_cocktail_rects.append({
                                "name": ingredient_name,
                                "rect": pygame.Rect(cocktail_glass_middle - cocktail_glass_width / 2 + 1, current_cocktail_rects[-1]["rect"].y - cocktail_layer_height, cocktail_glass_width, cocktail_layer_height),
                                "color": ingredient_color_library[ingredient_name]
                            })
        
        if len(current_made_cocktail) > 0:
            total_amount = 0
            for ingredient in current_made_cocktail:
                total_amount += current_made_cocktail[str(ingredient)]
            if total_amount == 20:
                cocktail_done = True

        #---------displaying---------

        screen.blit(cocktailmaker_background_img, (0,0))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button2_rect)
        rect_counter = 0
        for ingredient in cocktail_pages[cocktail_page_displayed]:
            screen.blit(drink_icon_library[ingredient["name"]], cocktailmaker_ing_rects[rect_counter])
            owned_text_x = cocktailmaker_ing_rects[rect_counter].x + cocktailmaker_ing_rects[rect_counter].width / 2
            amount_owned_text = save_detail_font_date.render(str(ingredient["owned"]), True, (0,0,0))
            owned_text_x -= amount_owned_text.get_width() / 2
            screen.blit(amount_owned_text, (owned_text_x, 151))
            rect_counter += 1
        ingredient_name_text = pixel_font_letters.render(selected_cocktail_ingredient["name"], True, (0,0,0))
        screen.blit(ingredient_name_text, (50, WINDOW_HEIGHT - 54))
        if selected_cocktail_ingredient["name"] in current_made_cocktail:
            text = pixel_font_letters.render(str(current_made_cocktail[selected_cocktail_ingredient["name"]]), True, (0,0,0))
            screen.blit(text, (ingredient_name_text.get_width() + 100, WINDOW_HEIGHT - 54))
        if cocktail_page_displayed != 0:
            screen.blit(left_arrow_img, cocktail_left_arrow_rect)
        if cocktail_page_displayed != len(cocktail_pages) - 1:
            screen.blit(right_arrow_img, cocktail_right_arrow_rect)
        if selected_cocktail_ingredient_page == cocktail_page_displayed:
            pygame.draw.rect(screen, (0,0,0), cocktail_indicator_rect, 1)
        if not cocktail_done:
            screen.blit(cocktail_glass_img, (512, 356))
            for rect in current_cocktail_rects:
                pygame.draw.rect(screen, rect["color"], rect["rect"])
        if cocktail_done:
            gap = 4
            total_width = 300
            total_height = 30
            text = pixel_font_letters.render("Shake!", True, (0,0,0))
            screen.blit(text, (WINDOW_WIDTH / 2 - text.get_width() / 2, 220))
            pygame.draw.rect(screen, (91, 91, 91), (cocktail_glass_middle - total_width / 2, WINDOW_HEIGHT - 40, total_width, total_height))
            pygame.draw.rect(screen, (151, 151, 151), (cocktail_glass_middle - total_width / 2 + gap, WINDOW_HEIGHT - 40 + gap, total_width - gap * 2, total_height - gap * 2))
            screen.blit(cocktail_shaker_img, cocktail_shaker_rect)

    def display_progress_screen():
        global back_button_clicked, back_button_clicktime, screen_displayed_now, transition_this_frame, customers_served, progress_rect
        #----------button logic---------

        if not transition_this_frame:
            if left_mouse_clicked and back_button_rect.collidepoint(pos):
                back_button_clicked = True
                back_button_clicktime = now

        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "homescreen"
            transition_this_frame = True

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        #----------displaying----------
        
        screen.blit(progress_screen_background_img, (0,0))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        pygame.draw.rect(screen, (137,0,0), progress_rect)

    def display_recipe_book():
        screen.fill((255,0,0))

    def display_guest_screen():
        global screen_displayed_now, settings, transition_this_frame, guests, temp_guest_spawn_wait, temp_guest_timer, back_button_clicked, back_button_clicktime, balance
        #---------button logic----------

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if left_mouse_clicked and back_button_rect.collidepoint(pos):
            back_button_clicked = True
            back_button_clicktime = now

        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "homescreen"
            transition_this_frame = True
            back_button_clicktime = 0

        money_cheat_rect = pygame.Rect(500, 200, 50, 50)

        if settings["dev_mode"] and right_mouse_clicked and money_cheat_rect.collidepoint(pos):
            balance += 100

        #--------guest timer-------------

        if settings["dev_mode"]:
            timer_range = sped_up_guest_timer_range.copy()
        else:
            timer_range = normal_guest_timer_range.copy()

        if temp_guest_spawn_wait == 0:
            temp_guest_spawn_wait = random.randint(timer_range[0], timer_range[1])
            temp_guest_timer = time.time()
            
        if time.time() - temp_guest_timer >= temp_guest_spawn_wait:
            if (guest_available_spots):
                refresh(random.choice(guest_available_spots))
            temp_guest_spawn_wait = 0
                
        #--------guest interaction-------
        
        for guest in guests:
            if left_mouse_clicked and guest_rects_library[guest["rect_num"]].collidepoint(pos):
                if guest["clicked"]:
                    for dict in guests:
                        dict["clicked"] = False
                else:
                    for dict in guests:
                        dict["clicked"] = False
                    guest["clicked"] = True
        if settings["dev_mode"]:
            for guest in guests:
                if right_mouse_clicked and guest_rects_library[guest["rect_num"]].collidepoint(pos):
                    check_unlocks()
                    client_request_completed(guest["name"], 1)

        #----------displaying-----------

        screen.blit(guest_screen_background_img, (0,0))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        for guest in guests:
            if guest["clicked"]:
                segments = [
                    (guest["order_text"], (0,0,0)),
                    (guest["order_item"], (0,136,209))
                ]
            
                custom_order_rect = guest_order_rects_library[guest["rect_num"]].copy()
                custom_order_rect.y = guest["order_rect_y"]
                draw_text_centered(
                    screen,
                    segments,
                    default_font,
                    custom_order_rect
                )
            screen.blit(guest_images_library[guest["image_num"]], guest_rects_library[guest["rect_num"]])
        pygame.draw.rect(screen, (255, 0, 0), money_cheat_rect, 1)

    def display_create_username():
        global continue_button2_clicktime, continue_button2_clicked, username, current_username_string, screen_displayed_now
        #----------button logic--------

        if left_mouse_clicked and continue_button2_rect.collidepoint(pos):
            continue_button2_clicked = True
            continue_button2_clicktime = now

        if continue_button2_clicktime != 0 and continue_button2_clicktime <= now - click_duration:
            continue_button2_clicked = False
        
        if continue_button2_clicktime != 0 and continue_button2_clicktime <= now - screen_switch_duration:
            continue_button2_clicktime = 0
            username = current_username_string
            write_username_file(username)
            screen_displayed_now = "startscreen"
            current_username_string = """"""

        #----------displaying----------

        screen.fill((0, 89, 76))
        screen.blit(continue_button2_clicked_img if continue_button2_clicked else continue_button2_img, continue_button2_rect)
        username_name_rendered_text = playthrough_name_font.render(playthrough_name_text, True, (0,0,0))
        screen.blit(username_name_rendered_text, (448, 401))
        username_text1 = playthrough_text_font.render("enter a username:", True, (0,0,0))
        username_text2 = playthrough_text_font.render("used on global leaderboard!", True, (0,0,0))
        screen.blit(username_text1, (476, 230))
        screen.blit(username_text2, (504, 300))
        pygame.draw.rect(screen, (255,255,255), new_playthrough_rect_big, 1, border_radius=10)
        pygame.draw.rect(screen, (255,255,255), new_playthrough_rect_small, 1, border_radius=10)

#-----------main loop-----------

while running:
    
    #---------event loop---------

    if True:
        new_ingredient_unlocked = False
        left_mouse_clicked = False
        right_mouse_clicked = False
        transition_this_frame = False
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                left_mouse_clicked = True
                if cocktail_shaker_rect.collidepoint(pos):
                    dragging = True
                    cocktail_shaker_x_offset = cocktail_shaker_rect.x - event.pos[0]
                    cocktail_shaker_y_offset = cocktail_shaker_rect.y - event.pos[1]
            if event.type == pygame.MOUSEMOTION:
                if dragging and cocktail_done:
                    cocktail_shaker_rect.x = event.pos[0] + cocktail_shaker_x_offset
                    cocktail_shaker_rect.y = event.pos[1] + cocktail_shaker_y_offset
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = event.pos
                right_mouse_clicked = True
            if event.type == pygame.TEXTINPUT and len(playthrough_name_text) <= 15 and len(current_username_string) <= 15:
                playthrough_name_text += event.text
                current_username_string += event.text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    playthrough_name_text = playthrough_name_text[:-1]
                    current_username_string = current_username_string[:-1]
    
    #-----------updates--------------

    now = pygame.time.get_ticks()

    #-----------debugging----------

    #print(cocktailmaker_ing_rects[11].right)

    #--------screen selection--------

    if screen_displayed_now == "homescreen":
        display_homescreen()

    elif screen_displayed_now == "continue_screen":
        display_continue_playthrough()

    elif screen_displayed_now == "overwrite_screen":
        display_overwrite_playthrough()

    elif screen_displayed_now == "new_screen":
        display_new_playthrough()

    elif screen_displayed_now == "startscreen":
        display_startscreen()

    elif screen_displayed_now == "settings":
        display_settings_screen()
        
    elif screen_displayed_now == "menu_screen":
        display_menu_screen()

    elif screen_displayed_now == "stock_screen":
        display_stock_screen()
    
    elif screen_displayed_now == "cocktailmaker":
        display_cocktailmaker()

    elif screen_displayed_now == "progress_screen":
        display_progress_screen()
    
    elif screen_displayed_now == "recipe_book":
        display_recipe_book()
    
    elif screen_displayed_now == "guest_screen":
        display_guest_screen()
    elif screen_displayed_now == "username":
        display_create_username()

    #----------------------------------

    pygame.display.update()
    clock.tick(60)

#--------BUG_FIXES:--------