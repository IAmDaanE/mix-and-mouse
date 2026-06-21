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
    import requests
    from recipes import all_recipes_in_game

    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("cocktail game")
    clock = pygame.time.Clock()

#------loading in assets--------

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

if True:
    continue_button_img = convert_asset("assets/continue_button.png", 1) 
    continue_button2_img = convert_asset("assets/continue_button.png", 2)
    new_button_img = convert_asset("assets/new_button.png", 1)
    settings_button_img = convert_asset("assets/settings_button.png", 1)
    exit_button_img = convert_asset("assets/exit_button.png", 1)
    back_button_img = convert_asset("assets/back_button.png", 1)
    plus_button_img = convert_asset("assets/plus_button.png", 1)
    min_button_img = convert_asset("assets/min_button.png", 1)
    buy_button_img = convert_asset("assets/buy_button.png", 1)
    create_button_img = convert_asset("assets/create_button.png", 1)
    save_button_img = convert_asset("assets/save_button.png", 1)
    save_exit_button_img = convert_asset("assets/save_exit_button.png", 1)
    make_button_img = convert_asset("assets/make_button_bar.png", 2)
    add_button_img = convert_asset("assets/add_button.png", 1)
    enable_anyway_button_img = convert_asset("assets/enable_anyway_button.png", 1)
    cancel_button_img = convert_asset("assets/cancel_button.png", 1)

    continue_button_clicked_img = convert_asset("assets/continue_button_clicked.png", 1)
    continue_button2_clicked_img = convert_asset("assets/continue_button_clicked.png", 2)
    new_button_clicked_img = convert_asset("assets/new_button_clicked.png", 1)
    settings_button_clicked_img = convert_asset("assets/settings_button_clicked.png", 1)
    exit_button_clicked_img = convert_asset("assets/exit_button_clicked.png", 1)
    back_button_clicked_img = convert_asset("assets/back_button_clicked.png", 1)
    plus_button_clicked_img = convert_asset("assets/plus_button_clicked.png", 1)
    min_button_clicked_img = convert_asset("assets/min_button_clicked.png", 1)
    buy_button_clicked_img = convert_asset("assets/buy_button_clicked.png", 1)
    create_button_clicked_img = convert_asset("assets/create_button_clicked.png", 1)
    save_button_clicked_img = convert_asset("assets/save_button_clicked.png", 1)
    save_exit_button_clicked_img = convert_asset("assets/save_exit_button_clicked.png", 1)
    make_button_clicked_img = convert_asset("assets/make_button_clicked_bar.png", 2)
    add_button_clicked_img = convert_asset("assets/add_button_clicked.png", 1)
    enable_anyway_button_clicked_img = convert_asset("assets/enable_anyway_button_clicked.png", 1)
    cancel_button_clicked_img = convert_asset("assets/cancel_button_clicked.png", 1)

    startscreen_background_img = convert_asset("assets/startscreen_background.png", 1)
    settings_screen_background_img = convert_asset("assets/settings_screen_background.png", 1)
    guest_screen_background_img = convert_asset("assets/guest_screen_background.png", 1)
    stock_screen_background_img = convert_asset("assets/stock_screen_background.png", 1)
    progress_screen_background_img = convert_asset("assets/progress_screen_background.png", 1)
    cocktailmaker_background_img = convert_asset("assets/cocktailmaker_background.png", 1)
    homescreen_background_img = convert_asset("assets/homescreen_background.png", 1)
    menu_screen_background_img = convert_asset("assets/menu_screen_background.png", 1)
    cocktail_made_background_img = convert_asset("assets/cocktail_made_background.png", 1)
    coktail_exterior_customizer_background_img = convert_asset("assets/cocktail_design_maker_bar.png",1)

    checkmark_img = convert_asset("assets/checkmark.png", 1)
    right_arrow_img = convert_asset("assets/right_arrow.png", 1)
    left_arrow_img = convert_asset("assets/left_arrow.png", 1)
    stock_screen_row_img = convert_asset("assets/stock_screen_row.png", 1)
    cocktail_shaker_img = convert_asset("assets/cocktail_shaker.png", 2)
    cocktail_glass_img = convert_asset("assets/cocktail_glass.png", 1)
    ice_layer_small_img = convert_asset("assets/ice_layer_small.png", 1)
    ice_layer_big_img = convert_asset("assets/ice_layer_big.png", 1)
    star_img = convert_asset("assets/star.png", 1)
    smudge_img = convert_asset("assets/smudge.png", 1)

    guest1_img = convert_asset("assets/guest_1.png", 1)
    guest2_img = convert_asset("assets/guest_2.png", 1)
    guest3_img = convert_asset("assets/guest_3.png", 1)
    guest4_img = convert_asset("assets/guest_4.png", 1)
    guest5_img = convert_asset("assets/guest_5.png", 1)
    guest6_img = convert_asset("assets/guest_6.png", 1)
    guest7_img = convert_asset("assets/guest_7.png", 1)
    guest8_img = convert_asset("assets/guest_8.png", 1)

    default_font = pygame.font.SysFont('Calibri', 25)
    pixel_font_numbers = pygame.font.Font("assets/micro_5.ttf", 60)
    pixel_font_letters = pygame.font.Font("assets/Jersey10.ttf", 50)
    playthrough_name_font = pygame.font.Font("assets/Jersey10.ttf", 60)
    playthrough_text_font = pygame.font.Font("assets/Jersey10.ttf", 70)
    save_detail_font_date = pygame.font.Font("assets/Jersey10.ttf", 30)
    save_detail_font_nums = pygame.font.Font("assets/Jersey10.ttf", 40)
    leaderboard_columns_font = pygame.font.Font("assets/Jersey10.ttf", 20)
    leaderboard_items_font = pygame.font.Font("assets/Jersey10.ttf", 25)
    recipe_steps_font = pygame.font.Font("assets/Jersey10.ttf", 32)

    ingredient_icons_list = slice_tilesheet("assets/ingredients_tilesheet.png", 66, 66)
    glass_tags_list = slice_tilesheet("assets/tags_tilesheet.png", 66, 66)
    glasses_list = slice_tilesheet("assets/glasses_tilesheet.png", 66, 66)

#----------assigning image names---------

if True: 
    drink_bar_library = {
                            "vodka": ingredient_icons_list[0],
                            "gin": ingredient_icons_list[40],
                            "orange juice": ingredient_icons_list[20],
                            "white rum": ingredient_icons_list[1],
                            "cola": ingredient_icons_list[3],
                            "tonic water": ingredient_icons_list[33],
                            "soda water": ingredient_icons_list[34],
                            "lime juice": ingredient_icons_list[23],
                            "mint": ingredient_icons_list[38],
                            "sugar syrup": ingredient_icons_list[30],
                            "ice": ingredient_icons_list[37],
                            "dark rum": ingredient_icons_list[2],
                            "tequila": ingredient_icons_list[5],
                            "whiskey": ingredient_icons_list[41],
                            "triple sec": ingredient_icons_list[6],
                            "amaretto": ingredient_icons_list[7],
                            "kahlúa": ingredient_icons_list[8],
                            "baileys": ingredient_icons_list[10],
                            "champagne": ingredient_icons_list[4],
                            "prosecco": ingredient_icons_list[11],
                            "peach schnapps": ingredient_icons_list[12],
                            "blue curaçao": ingredient_icons_list[13],
                            "midori": ingredient_icons_list[14],
                            "absinthe": ingredient_icons_list[15],
                            "dry vermouth": ingredient_icons_list[17],
                            "sweet vermouth": ingredient_icons_list[16],
                            "campari": ingredient_icons_list[18],
                            "elderflower liqueur": ingredient_icons_list[9],
                            "pineapple juice": ingredient_icons_list[21],
                            "cranberry juice": ingredient_icons_list[22],
                            "lemon juice": ingredient_icons_list[24],
                            "grapefruit juice": ingredient_icons_list[25],
                            "apple juice": ingredient_icons_list[26],
                            "mango juice": ingredient_icons_list[28],
                            "passionfruit juice": ingredient_icons_list[19],
                            "peach juice": ingredient_icons_list[27],
                            "grenadine": ingredient_icons_list[31],
                            "coconut cream": ingredient_icons_list[32],
                            "ginger beer": ingredient_icons_list[36],
                            "egg white": ingredient_icons_list[35],
                            "cream": ingredient_icons_list[42],
                            "lime": ingredient_icons_list[29],
                            "bitters": ingredient_icons_list[39]
                        }
    glass_tags_bar_library = {
                            1: glass_tags_list[0],
                            2: glass_tags_list[1],
                            3: glass_tags_list[2],
                            4: glass_tags_list[3],
                            5: glass_tags_list[4],
                            6: glass_tags_list[5],
                            7: glass_tags_list[6],
                            8: glass_tags_list[7],
                            9: glass_tags_list[8],
                            10: glass_tags_list[9],
                            11: glass_tags_list[10],
                            12: glass_tags_list[11],
                            13: glass_tags_list[12],
                            14: glass_tags_list[13],
                            15: glass_tags_list[14],
                            16: glass_tags_list[15],
                            17: glass_tags_list[16],
                            18: glass_tags_list[17],
                            19: glass_tags_list[18],
                            20: glass_tags_list[19],
                            21: glass_tags_list[20],
                            22: glass_tags_list[21],
                            23: glass_tags_list[22],
                            24: glass_tags_list[23],
                            25: glass_tags_list[24],
                            26: glass_tags_list[25],
                            27: glass_tags_list[26],
                            28: glass_tags_list[27],
                            29: glass_tags_list[28],
                            30: glass_tags_list[29],
                            31: glass_tags_list[30],
                            32: glass_tags_list[31],
                            33: glass_tags_list[32],
                            34: glass_tags_list[33],
                            35: glass_tags_list[34],
                            36: glass_tags_list[35],
                        }
    glasses_bar_library = {
                            "1.1": glasses_list[0],
                            "1.2": glasses_list[1],
                            "1.3": glasses_list[2],
                            "2.1": glasses_list[3],
                            "2.2": glasses_list[4],
                            "2.3": glasses_list[5],
                            "3.1": glasses_list[6],
                            "3.2": glasses_list[7],
                            "3.3": glasses_list[8],
                            "4.1": glasses_list[9],
                            "4.2": glasses_list[10],
                            "4.3": glasses_list[11],
                            "5.1": glasses_list[12],
                            "5.2": glasses_list[13],
                            "5.3": glasses_list[14],
                            "6.1": glasses_list[15],
                            "6.2": glasses_list[16],
                            "6.3": glasses_list[17],
                            "7.1": glasses_list[18],
                            "7.2": glasses_list[19],
                            "7.3": glasses_list[20],
                            "8.1": glasses_list[21],
                            "8.2": glasses_list[22],
                            "8.3": glasses_list[23],
                            "9.1": glasses_list[24],
                            "9.2": glasses_list[25],
                            "9.3": glasses_list[26],
                            "10.1": glasses_list[27],
                            "10.2": glasses_list[28],
                            "10.3": glasses_list[29],
                            "11.1": glasses_list[30],
                            "11.2": glasses_list[31],
                            "11.3": glasses_list[32],
                            "12.1": glasses_list[33],
                            "12.2": glasses_list[34],
                            "12.3": glasses_list[35],
                            "13.1": glasses_list[36],
                            "13.2": glasses_list[37],
                            "13.3": glasses_list[38],
                            "14.1": glasses_list[39],
                            "14.2": glasses_list[40],
                            "14.3": glasses_list[41],
                            "15.1": glasses_list[42],
                            "15.2": glasses_list[43],
                            "15.3": glasses_list[44],
                            "16.1": glasses_list[45],
                            "16.2": glasses_list[46],
                            "16.3": glasses_list[47],
                            "17.1": glasses_list[48],
                            "17.2": glasses_list[49],
                            "17.3": glasses_list[50],
                            "18.1": glasses_list[51],
                            "18.2": glasses_list[52],
                            "18.3": glasses_list[53],
                            "19.1": glasses_list[54],
                            "19.2": glasses_list[55],
                            "19.3": glasses_list[56],
                            "20.1": glasses_list[57],
                            "20.2": glasses_list[58],
                            "20.3": glasses_list[59],
                            "21.1": glasses_list[60],
                            "21.2": glasses_list[61],
                            "21.3": glasses_list[62],
                            "22.1": glasses_list[63],
                            "22.2": glasses_list[64],
                            "22.3": glasses_list[65],
                            "23.1": glasses_list[66],
                            "23.2": glasses_list[67],
                            "23.3": glasses_list[68],
                            "24.1": glasses_list[69],
                            "24.2": glasses_list[70],
                            "24.3": glasses_list[71],
                            "25.1": glasses_list[72],
                            "25.2": glasses_list[73],
                            "25.3": glasses_list[74],
                            "26.1": glasses_list[75],
                            "26.2": glasses_list[76],
                            "26.3": glasses_list[77],
                            "27.1": glasses_list[78],
                            "27.2": glasses_list[79],
                            "27.3": glasses_list[80]
                        }
    
#-----------button variables-----------

if True:
    continue_button_rect = continue_button_img.get_rect(topleft=(50, 20))
    continue_button2_rect = continue_button2_img.get_rect(topleft=(WINDOW_WIDTH / 2 - continue_button2_img.get_width() / 2, 637))
    new_button_rect = new_button_img.get_rect(topleft=(continue_button_rect.right + 20, 20))
    exit_button_rect = exit_button_img.get_rect(topleft=(new_button_rect.right + 20, 20))
    back_button_rect = back_button_img.get_rect(topleft=(20, 20))
    back_button2_rect = back_button_img.get_rect(topleft=(10, 208 + 10))
    stock_screen_button_rect = pygame.Rect(68, 143, 221, 364)
    progress_screen_button_rect = pygame.Rect(900, 400, 180, 80) #PLACEHOLDER
    cocktailmaker_button_rect = pygame.Rect(547, 336, 143, 107)
    guest_screen_button_rect = pygame.Rect(777, 123, 182, 272)
    menu_screen_button_rect = pygame.Rect(1025, 475, 137, 209)
    plus_button_rect = plus_button_img.get_rect(topleft=(754, 544))
    min_button_rect = min_button_img.get_rect(topleft=(461, 544))
    stock_right_arrow_rect = right_arrow_img.get_rect(topleft=(1187, WINDOW_HEIGHT / 2 - left_arrow_img.get_height() / 2))
    stock_left_arrow_rect = left_arrow_img.get_rect(topleft=(58, WINDOW_HEIGHT / 2 - left_arrow_img.get_height() / 2))
    cocktail_right_arrow_rect = right_arrow_img.get_rect(topleft=(1142 + 25*2, 56))
    cocktail_left_arrow_rect = left_arrow_img.get_rect(topleft=(24 + 27, 56))
    enable_anyway_button_rect = enable_anyway_button_img.get_rect(topleft=(300, 300))
    cancel_button_rect = cancel_button_img.get_rect(topleft=(500, 300))

    color_right_arrow_rect = right_arrow_img.get_rect(topleft=(743, 106))
    color_left_arrow_rect = left_arrow_img.get_rect(topleft=(1094, 106))

    glass_right_arrow_rect = right_arrow_img.get_rect(topleft=(743, 325))
    glass_left_arrow_rect = left_arrow_img.get_rect(topleft=(1094, 325))

    tags_right_arrow_rect = right_arrow_img.get_rect(topleft=(743, 544))
    tags_left_arrow_rect = left_arrow_img.get_rect(topleft=(1094, 544))

    buy_button_rect = buy_button_img.get_rect(topleft=(840, 544))
    create_button_rect = create_button_img.get_rect(topleft=(WINDOW_WIDTH / 2 - create_button_img.get_width() / 2, 500))
    save_button_rect = save_button_img.get_rect(topleft=(20, 20))
    save_exit_button_rect = save_exit_button_img.get_rect(topleft=(save_button_rect.right + 20, 20))
    settings_button_rect = settings_button_img.get_rect(topleft=(save_exit_button_rect.right + 20, 20))
    add_ingredient_button_rect = pygame.Rect(510, 355, 223, 314)
    cocktail_shaker_og_rect = cocktail_shaker_img.get_rect(topleft=(621 - cocktail_shaker_img.get_width() / 2, WINDOW_HEIGHT - 51 - cocktail_shaker_img.get_height()))
    cocktail_shaker_rect = cocktail_shaker_og_rect.copy()
    recipes_left_arrow_rect = left_arrow_img.get_rect(topleft=(516, 636))
    recipes_right_arrow_rect = left_arrow_img.get_rect(topleft=(720, 636))
    make_button_rect = make_button_img.get_rect(topleft=(322, 636))

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
    make_button_clicked = False
    enable_anyway_button_clicked = False
    cancel_button_clicked = False

    make_button_clicktime = 0
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
    enable_anyway_button_clicktime = 0
    cancel_button_clicktime = 0

    settings_sandbox_checkmark_rect = checkmark_img.get_rect(topleft=(146, 97))
    settings_soundon_checkmark_rect = checkmark_img.get_rect(topleft=(146, 133))
    settings_showleaderboard_checkmark_rect = checkmark_img.get_rect(topleft=(146, 168))

#-----------other variables------------

if True:
    click_duration = 80
    screen_switch_duration = 85
    running = True
    pos = (0,0)
    settings = {"sandbox": False, "sound_on": True, "show_leaderboard": True}
    guests = []
    guest_available_spots = []
    unlocked_ingredients = []
    locked_ingredients = []
    stock_page_displayed = 0
    cocktail_page_displayed = 0
    recipe_page_displayed = 0
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
    cocktail_layer_height = 16
    cocktail_glass_middle = 621
    shaking = False
    displaying_recipe_book = False
    newly_made_cocktail = []
    shaking_complete = False
    dragging = False
    unlocks = {}
    normal_guest_timer_range = [3, 23]
    sped_up_guest_timer_range = [1, 2]
    current_username_string = """"""
    username_error_message = ""
    total_dif = 0
    leaderboard_data = []
    max_total_difference = 10000
    shake_progress_rect_increaser = 292 / max_total_difference
    personal_recipes = []
    recipe_book_pages = []
    successfully_made_drink = False
    unlocked_drinks = []
    cur_photo = "1.1"
    color_pointer = 1
    glass_pointer = 1
    cur_tag = 1
    drink_pic_lib = {"screwdriver": {"glass_color": str(1.1), "tag": 1}}
    drink_tag = 1
    drink_glass_color = "1.1"
    stashed_cocktails = []
    cocktail_available_spots = [0,1,2,3,4,5,6,7]
    current_dragging_cocktail = -1
    dragging_cocktail = False
    item_added_to_menu = ""
    balance = 160
    star_price_ratio_lib = {1: "0.2", 2: "0.4", 3: "0.6", 4: "0.8", 5: "1.0", 6: "1.5", 7: "2", 8: "3", 9: "4", 10: "10"}
    earnings_text_duration = 100
    legit_playthrough = True
    best_cocktail_value = 0

#--------random rects and lists--------

if True:
    stock_screen_row1_rect = stock_screen_row_img.get_rect(topleft=(189, 109))
    stock_screen_row2_rect = stock_screen_row_img.get_rect(topleft=(189, 196))
    stock_screen_row3_rect = stock_screen_row_img.get_rect(topleft=(189, 284))
    stock_screen_row4_rect = stock_screen_row_img.get_rect(topleft=(189, 371))
    stock_screen_row5_rect = stock_screen_row_img.get_rect(topleft=(189, 458))

    cocktail_made_window_rect = cocktail_made_background_img.get_rect(topleft=(213, 120))

    cocktailmaker_ing_spacing = 24

    cocktailmaker_ing_rects = []
    for i in range(12):
        x = 27 + cocktailmaker_ing_spacing * 2 + 35 + i * (66 + cocktailmaker_ing_spacing)
        cocktailmaker_ing_rects.append(pygame.Rect(x, 56, 66, 66))

    og_stashed_cocktail_rects = []
    stashed_cocktail_spacing = 62
    stashed_cocktail_rect_width = 66
    for i in range(8):
        x = 141 + stashed_cocktail_spacing + i * (stashed_cocktail_rect_width + stashed_cocktail_spacing)
        og_stashed_cocktail_rects.append(pygame.Rect(x, 557, 66, 66))
    stashed_cocktail_rects = deepcopy(og_stashed_cocktail_rects)

    earnings_texts = []
    earnings_texts_timings = []
    for i in range(6):
        earnings_texts.append("")
        earnings_texts_timings.append(0)

    add_button_rects = [
        make_button_img.get_rect(topleft=(76,246)),
        make_button_img.get_rect(topleft=(706,246)),
        make_button_img.get_rect(topleft=(76,552)),
        make_button_img.get_rect(topleft=(706,552)),
    ]

    add_button_clicked_list = [False, False, False, False]

    add_button_clicktimes = [0, 0, 0, 0]

    delete_from_menu_rects = [
        pygame.Rect(20, 20, 610, 330),
        pygame.Rect(650, 20, 610, 330),
        pygame.Rect(20, 370, 610, 330),
        pygame.Rect(650, 370, 610, 330)
    ]

    for i in range(9):
        unlocks[f"group{i}"] = False
    
    personal_recipes = [{'name': 'screwdriver', 'stars': 7, 'price': 64, 'preparation': {'vodka': 9, 'orange juice': 9, 'ice': 2}, 'image_num': 74}]
                                                            
    stock_indicator_rect = pygame.Rect(stock_screen_row1_rect.x - stock_indicator_gap, stock_screen_row1_rect.y - stock_indicator_gap, stock_screen_row_img.get_width() + stock_indicator_gap * 2, stock_screen_row_img.get_height() + stock_indicator_gap * 2)
    cocktail_indicator_rect = pygame.Rect(cocktailmaker_ing_rects[0].x - cocktail_indicator_gap, cocktailmaker_ing_rects[0].y - cocktail_indicator_gap, cocktailmaker_ing_rects[0].width + 2 * cocktail_indicator_gap, cocktailmaker_ing_rects[0].height + 2 * cocktail_indicator_gap)

    new_playthrough_rect_big = pygame.Rect((WINDOW_WIDTH - 600) / 2, 220, 600, 400)
    new_playthrough_rect_small = pygame.Rect((WINDOW_WIDTH - 400) / 2, 400, 400, 70)

    stock_screen_row_cords = [109, 196, 284, 371, 458]
    continue_screen_cords = [100, 235, 370, 505]
    leaderboard_row_cords = [520, 580, 640]
    recipe_book_rects = [(18, 37, 612, 268), (18 + 612 + 18, 37, 612, 268), (18, 37 + 268 + 37, 612, 268), (18 + 612 + 18, 37 + 268 + 37, 612, 268)]
    recipe_book_cords = [[18, 37], [18 + 612 + 18, 37], [18, 37 + 268 + 37], [18 + 612 + 18, 37 + 268+ 37]]
    menu_cords = [[20, 20], [650, 20], [20, 369], [650, 369]]

    unlocked_ingredients = [
        {"name": "vodka", "price": 5, "owned": 0},
        {"name": "gin", "price": 5, "owned": 0},
        {"name": "orange juice", "price": 2, "owned": 0},
        {"name": "white rum", "price": 5, "owned": 0},
        {"name": "cola", "price": 2, "owned": 0},
        {"name": "tonic water", "price": 2, "owned": 0},
        {"name": "soda water", "price": 1, "owned": 0},
        {"name": "lime juice", "price": 2, "owned": 0},
        {"name": "mint", "price": 1, "owned": 0},
        {"name": "sugar syrup", "price": 1, "owned": 0},
        {"name": "ice", "price": 1, "owned": 0}]
    
    guest_rect_y = 319

    guest1_rect = guest1_img.get_rect(topleft=(100,guest_rect_y))
    guest2_rect = guest1_img.get_rect(topleft=(guest1_rect.right + 70, guest_rect_y))
    guest3_rect = guest1_img.get_rect(topleft=(guest2_rect.right + 70, guest_rect_y))
    guest4_rect = guest1_img.get_rect(topleft=(guest3_rect.right + 70, guest_rect_y))
    guest5_rect = guest1_img.get_rect(topleft=(guest4_rect.right + 70, guest_rect_y))
    guest6_rect = guest1_img.get_rect(topleft=(guest5_rect.right + 70, guest_rect_y))

    guest_order1_rect = pygame.Rect(guest1_rect.x - 20, guest_rect_y - 28, 150, 100)
    guest_order2_rect = pygame.Rect(guest2_rect.x - 20, guest_rect_y - 28, 150, 100)
    guest_order3_rect = pygame.Rect(guest3_rect.x - 20, guest_rect_y - 28, 150, 100)
    guest_order4_rect = pygame.Rect(guest4_rect.x - 20, guest_rect_y - 28, 150, 100)
    guest_order5_rect = pygame.Rect(guest5_rect.x - 20, guest_rect_y - 28, 150, 100)
    guest_order6_rect = pygame.Rect(guest6_rect.x - 20, guest_rect_y - 28, 150, 100)
    
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
        "passionfruit juice":  (232, 175, 16),
        "peach juice":          (230, 130, 50),

        # syrups & sweet
        "sugar syrup":          (180, 210, 140),
        "grenadine":            (190,  10,  40),
        "coconut cream":        (242, 230, 196),

        # sodas
        "cola":                 (45,   20,   5),
        "tonic water":          (224, 242, 220),
        "ginger beer":          (195, 160,  60),
        "soda water":           (225, 247, 242),

        # other
        "egg white":            (200, 210, 160),
        "cream":                (210, 185, 100),
        "lime":                 (80,  165, 30),
        "mint":                 (30,  140, 40),
        "bitters":              (110, 40,  15),
        "ice":                  (0,    0,   0) #PLACEHOLDER
    }

#-----------text formatting------------

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

#-------------guest logic-------------

if True:
    pos_sentences = ["give me a ", "i want a ", "i need a ", "can i get a ", "could you give me a ", "would you do your job and give me a ", "immediately give me a ", "make a ", "i desire a ", "i would love a ", "i want to get drunk so give me a ",
                    "stop being a jackass and give me a ", "i will die if you dont give me a ", "just give me a ", "bring me a ", "i don't have a lot of time, i just want a ", "i just got circumsised give me a "]

    cur_menu = ["screwdriver"]

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
    x = -1

    def client_request_completed(client_name, drink_served_name, star_multiplier):
        global guests, balance, customers_served, best_cocktail_value

        customers_served += 1

        for guest in guests:
            i = guest["rect_num"]
            if guest["name"] == client_name:
                if guest["order_item"] == drink_served_name:
                    earnings = guest["price"] * float(star_price_ratio_lib[star_multiplier])
                    if earnings > best_cocktail_value:
                        best_cocktail_value = earnings
                    balance += earnings
                    earnings_texts[i - 1] = str(earnings)
                    earnings_texts_timings[i - 1] = earnings_text_duration
                    guest_available_spots.append(i)
                    guests.remove(guest)
                    break
                else:
                    earnings = 2 * star_multiplier
                    if earnings == 0:
                        earnings = 8.0
                    balance += earnings
                    earnings_texts[i - 1] = str(earnings)
                    earnings_texts_timings[i - 1] = earnings_text_duration
                    guest_available_spots.append(i)
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
    def add_to_menu(drink):
        cur_menu.append(drink)

    def calculate_stars(calc_list):
        if calc_list == []:
            return 999999
        else:
            return sum(calc_list)

    def drink_check(used_ing):
        stars_temp = 0
        temp_drink_info = {}
        building_score = []
        temp_succes = False
        for recipe in all_recipes_in_game:
            recipe_ingredients = [ing["name"] for ing in recipe["makingprocess"].values()]
            
            if set(recipe_ingredients) == set(used_ing.keys()):
                temp_drink_info['successful'] = True
                temp_succes = True

                temp_drink_info["drink made"] = recipe["name"]

                temp_drink_info['new drink'] = False
                if not recipe["name"] in unlocked_drinks:
                    temp_drink_info['new drink'] = True
                    unlocked_drinks.append(recipe["name"])

                for ing in recipe["makingprocess"].values():
                    name = ing["name"]
                    required = ing["amount"]
                    used = used_ing[name]

                    building_score.append(abs(used - required))

        total_dif = calculate_stars(building_score)
        
        match total_dif:
                case 0:
                    stars_temp = 10
                case 1 | 2 | 3:
                    stars_temp = 9
                case 4 | 5:
                    stars_temp = 8
                case 6 | 7:
                    stars_temp = 7
                case 8 | 9 | 10:
                    stars_temp = 6
                case 11 | 12 | 13:
                    stars_temp = 5
                case 14 | 15 | 16 | 17:
                    stars_temp = 4
                case 18 | 19 | 20:
                    stars_temp = 3
                case 21 | 22 | 23:
                    stars_temp = 2
                case 24 | 25 | 26:
                    stars_temp = 1
                case 999999:
                    stars_temp = -1
                case _:
                    stars_temp = 0

        if temp_succes == True:
            temp_drink_info["stars"] = stars_temp

        temp_drink_info["preparation"] = used_ing
        
        temp_succes = False
        return temp_drink_info

#-------------file saving-------------

if True:
    def rond_af_5(n):
        return int(math.ceil(n / 5) * 5)
    
    def rond_af_12(n):
        return int(math.ceil(n / 12) * 12)

    def rond_af_4(n):
        return int(math.ceil(n / 4) * 4)

    save_files_location = f"{user_data_dir('cocktail_game', 'DTstudios')}/save_files"
    username_txt_file = f"{user_data_dir('cocktail_game', 'DTstudios')}/username.txt"

    os.makedirs(save_files_location, exist_ok=True)
                
    if not os.path.exists(username_txt_file):
        open(username_txt_file, "w").close()
        screen_displayed_now = "username"
    else:
        screen_displayed_now = "startscreen"

    saves_amount = 0
    for item in os.listdir(save_files_location):
        if os.path.isdir(os.path.join(save_files_location, item)):
            collision_rects_saves.append(pygame.Rect(WINDOW_WIDTH / 2 - 500 / 2, continue_screen_cords[saves_amount], 500, 120))
            saves_amount += 1
        

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
            basic_data = {"balance": balance, "customers_served": customers_served, "last_save": time.strftime("%m/%d/%Y"), "legit_playthrough": legit_playthrough, "best_cocktail_value": best_cocktail_value}
            guest_data = {"key": "value"}
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
        global balance, customers_served, unlocked_ingredients, settings, guests, guest_available_spots, first_save_done, unlocks, username, personal_recipes, drink_pic_lib, unlocked_drinks, stashed_cocktails, cocktail_available_spots, cur_menu, legit_playthrough, best_cocktail_value
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

        with open(username_txt_file, "r") as f:
            username = f.read()
        calculate_recipe_pages()
        calculate_cocktail_pages()
        calculate_stock_pages()
    
    def display_save_details():
        save_counter = 0
        for save in save_details:
            last_save_text = save_detail_font_date.render(str(save["last_save"]), True, (0,0,0))
            balance_text = save_detail_font_nums.render(f"${save['balance']}", True, (0,0,0))
            customers_served_text = save_detail_font_nums.render(f"guests: {save['customers_served']}", True, (0,0,0))
            screen.blit(last_save_text, (410, continue_screen_cords[save_counter] + 70))
            screen.blit(balance_text, (730, continue_screen_cords[save_counter] + 12))
            screen.blit(customers_served_text, (700, continue_screen_cords[save_counter] + 65))
            save_counter += 1

    def regular_save():
        basic_data = {"balance": balance, "customers_served": customers_served, "last_save": time.strftime("%m/%d/%Y"), "legit_playthrough": legit_playthrough, "best_cocktail_value": best_cocktail_value}
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
    
#----------leaderboard logic----------

if True:
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

    get_leaderboard()

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

#-------recipe book page calculations------

if True:
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
    calculate_recipe_pages()

#----------progression system---------

if True:
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

#---------recipe book system---------

def update_recipe_book():
    new_recipe = True
    for recipe in personal_recipes:
        if currently_preparing_drink["drink made"] == recipe["name"]:
            if currently_preparing_drink["stars"] > recipe["stars"]:
                recipe["preparation"] = currently_preparing_drink["preparation"]
                recipe["stars"] = currently_preparing_drink["stars"]
                for correct_recipe in all_recipes_in_game:
                    if currently_preparing_drink["drink made"] == correct_recipe["name"]:
                        price = correct_recipe["price"] * float(star_price_ratio_lib[currently_preparing_drink["stars"]])
                        break
                recipe["price"] = price
            new_recipe = False
            break
    if new_recipe:
        price = 0
        for correct_recipe in all_recipes_in_game:
            if currently_preparing_drink["drink made"] == correct_recipe["name"]:
                price = correct_recipe["price"] * float(star_price_ratio_lib[currently_preparing_drink["stars"]])
                break
        personal_recipes.append({"name": currently_preparing_drink["drink made"], "stars": currently_preparing_drink["stars"], "price": price, "preparation": currently_preparing_drink["preparation"], "image_num": random.randint(0, 80)})
    calculate_recipe_pages()

#------stashed cocktail system-------

if True:
    def stash_cocktail():
        pos_num = random.choice(cocktail_available_spots)
        stashed_cocktails.append({"name": currently_preparing_drink["drink made"], "num": pos_num, "stars": currently_preparing_drink["stars"]})
        cocktail_available_spots.remove(pos_num)

    def stash_smudge():
        pos_num = random.choice(cocktail_available_spots)
        stashed_cocktails.append({"name": "smudge", "num": pos_num, "stars": 0})
        cocktail_available_spots.remove(pos_num)

#---------display functions----------

if True:

    def display_startscreen():
        global continue_button_clicked, continue_button_clicktime, pos, settings_button_clicked, exit_button_clicked, settings_button_clicktime, exit_button_clicktime, screen_displayed_now, running, new_button_clicked, new_button_clicktime, save_details, playthrough_name_text
        #---------button logic----------
        
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
            continue_button_clicktime = 0
            for item in os.listdir(save_files_location):
                if os.path.isdir(os.path.join(save_files_location, item)):
                    with open(f"{save_files_location}/{item}/data.json", "r") as f:
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
            playthrough_name_text = ""

        #----------displaying-----------
        
        screen.blit(startscreen_background_img, (0,0))
        screen.blit(continue_button_clicked_img if continue_button_clicked else continue_button_img, continue_button_rect)
        screen.blit(exit_button_clicked_img if exit_button_clicked else exit_button_img, exit_button_rect)
        screen.blit(new_button_clicked_img if new_button_clicked else new_button_img, new_button_rect)

    def display_settings_screen():
        global back_button_clicktime, back_button_clicked, screen_displayed_now, settings
        #---------button logic----------

        if left_mouse_clicked and back_button_rect.collidepoint(pos):
            back_button_clicked = True
            back_button_clicktime = now
        
        if left_mouse_clicked and settings_sandbox_checkmark_rect.collidepoint(pos):
            if legit_playthrough:
                screen_displayed_now = "legit_playthrough_warning"
            else:
                settings["sandbox"] = not settings["sandbox"]

        if left_mouse_clicked and settings_soundon_checkmark_rect.collidepoint(pos):
            settings["sound_on"] = not settings["sound_on"]
        if left_mouse_clicked and settings_showleaderboard_checkmark_rect.collidepoint(pos):
            settings["show_leaderboard"] = not settings["show_leaderboard"]
        
        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "homescreen"
            back_button_clicktime = 0


        #----------displaying-----------

        screen.blit(settings_screen_background_img, (0,0))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        if settings["sandbox"]:
            screen.blit(checkmark_img, settings_sandbox_checkmark_rect)
        if settings["sound_on"]:
            screen.blit(checkmark_img, settings_soundon_checkmark_rect)
        if settings["show_leaderboard"]:
            screen.blit(checkmark_img, settings_showleaderboard_checkmark_rect)

    def display_new_playthrough():
        global back_button_clicked, back_button_clicktime, screen_displayed_now, create_button_clicked, create_button_clicktime, playthrough_name_text, playthrough_name_rendered_text, selected_continue_save_name
        #----------button logic--------

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
        
        if create_button_clicktime != 0 and create_button_clicktime <= now - screen_switch_duration:
            create_button_clicktime = 0
            if check_valid_dir_input():
                with os.scandir(save_files_location) as entries:
                    folder_count = sum(1 for entry in entries if entry.is_dir())
                if folder_count == 4:
                    screen_displayed_now = "overwrite_screen"
                    for item in os.listdir(save_files_location):
                        if os.path.isdir(os.path.join(save_files_location, item)):
                            with open(f"{save_files_location}/{item}/data.json", "r") as f:
                                raw_unloaded_data = json.load(f)
                            save_details.append({"last_save": raw_unloaded_data["last_save"], "balance": raw_unloaded_data["balance"], "customers_served": raw_unloaded_data["customers_served"]})
                else:
                    screen_displayed_now = "homescreen"
                    selected_continue_save_name = playthrough_name_text
                    new_save()
                    playthrough_name_text = ""

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
        global back_button_clicked, back_button_clicktime, screen_displayed_now, continue_button2_clicktime, continue_button2_clicked, selected_continue_save, selected_continue_save_name, new_ingredient_unlocked
        
        #----------button logic--------

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
        for item in os.listdir(save_files_location):
            if os.path.isdir(os.path.join(save_files_location, item)):
                continue_folder_rect = pygame.Rect(WINDOW_WIDTH / 2 - 500 / 2, continue_screen_cords[row_counter], 500, 120)
                pygame.draw.rect(screen, (255,255,255), continue_folder_rect, 1, border_radius=4)
                name_text = playthrough_name_font.render(item, True, (0,0,0))
                screen.blit(name_text, (continue_folder_rect.x + 20, continue_screen_cords[row_counter] + 4))
                row_counter += 1
        continue_indicator_rect = pygame.Rect(continue_folder_rect.x - save_indicator_gap, continue_screen_cords[selected_continue_save] - save_indicator_gap, 500 + 2 * save_indicator_gap, 120 + 2 * save_indicator_gap)
        pygame.draw.rect(screen, (0,0,0), continue_indicator_rect, 3, border_radius=4)
        display_save_details()

    def display_overwrite_playthrough():
        global back_button_clicked, back_button_clicktime, screen_displayed_now, continue_button2_clicked, continue_button2_clicktime, overwrite_indicator_rect, selected_overwrite_save, selected_continue_save_name
        #----------button logic--------

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
            selected_continue_save_name = playthrough_name_text
            new_save()
            screen_displayed_now = "homescreen"

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "startscreen"
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
        for item in os.listdir(save_files_location):
            if os.path.isdir(os.path.join(save_files_location, item)):
                continue_folder_rect = pygame.Rect(WINDOW_WIDTH / 2 - 500 / 2, continue_screen_cords[row_counter], 500, 120)
                pygame.draw.rect(screen, (255,255,255), continue_folder_rect, 1, border_radius=4)
                name_text = playthrough_name_font.render(item, True, (0,0,0))
                screen.blit(name_text, (continue_folder_rect.x + 20, continue_screen_cords[row_counter] + 4))
                row_counter += 1
        overwrite_indicator_rect = pygame.Rect(WINDOW_WIDTH / 2 - 500 / 2 - save_indicator_gap, continue_screen_cords[selected_overwrite_save] - save_indicator_gap, 500 + save_indicator_gap * 2, 120 + save_indicator_gap * 2)
        pygame.draw.rect(screen, (0,0,0), overwrite_indicator_rect, 3, border_radius=4)
        display_save_details()

    def display_homescreen():
        global screen_displayed_now, progress_rect, selected_cocktail_ingredient, selected_cocktail_ingredient_page, backup_ingredients, running, settings_button_clicked, settings_button_clicktime, save_button_clicked, save_button_clicktime, save_exit_button_clicked, save_exit_button_clicktime, progress_screen_button_rect
        #--------button logic--------

        if left_mouse_clicked and stock_screen_button_rect.collidepoint(pos):
            screen_displayed_now = "stock_screen"
            calculate_stock_pages()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if left_mouse_clicked and progress_screen_button_rect.collidepoint(pos):
            progress_rect = pygame.Rect(54, 514, min(1172, max(5, math.ceil(customers_served * 5.87))), 28)
            screen_displayed_now = "progress_screen"
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if left_mouse_clicked and cocktailmaker_button_rect.collidepoint(pos):
            if len(stashed_cocktails) < 8:
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
            settings_button_clicktime = 0

        #----------displaying----------

        screen.blit(homescreen_background_img, (0,0))
        screen.blit(save_button_clicked_img if save_button_clicked else save_button_img, save_button_rect)
        screen.blit(save_exit_button_clicked_img if save_exit_button_clicked else save_exit_button_img, save_exit_button_rect)
        screen.blit(settings_button_clicked_img if settings_button_clicked else settings_button_img, settings_button_rect)
        username_text = save_detail_font_nums.render(username, True, (255,255,255))
        progress_screen_button_rect = username_text.get_rect(topleft=(WINDOW_WIDTH - 10 - username_text.get_width(), 10))
        screen.blit(username_text, (WINDOW_WIDTH - 10 - username_text.get_width(), 10))
        balance_text = save_detail_font_nums.render(f"$ {balance}", True, (255,255,255))
        screen.blit(balance_text, ((WINDOW_WIDTH - 10 - balance_text.get_width(), 349)))
        if settings["show_leaderboard"]:
            display_leaderboard()

    def display_menu_screen():
        global back_button_clicktime, back_button_clicked, screen_displayed_now
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
            back_button_clicktime = 0

        #----------displaying-----------

        screen.blit(menu_screen_background_img, (0,0))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        for i, recipe in enumerate(cur_menu):
            name_text = save_detail_font_nums.render(recipe, True, (255,255,255))
            screen.blit(name_text, (menu_cords[i][0] + (610 / 2 - name_text.get_width() / 2), menu_cords[i][1] + 10))
            drink_tag = drink_pic_lib[recipe]["tag"]
            drink_glass_color = drink_pic_lib[recipe]["glass_color"]
            screen.blit(pygame.transform.scale_by(glasses_bar_library[drink_glass_color], 4.5), (menu_cords[i][0] - 34, menu_cords[i][1] - 30))
            screen.blit(pygame.transform.scale_by(glass_tags_bar_library[int(drink_tag)], 4.5), (menu_cords[i][0] - 34, menu_cords[i][1] - 30))
            for my_recipe in personal_recipes:
                if recipe == my_recipe["name"]:
                    stars_text = playthrough_name_font.render(str(int(my_recipe["stars"] / 2) if my_recipe["stars"] / 2 == int(my_recipe["stars"] / 2) else my_recipe["stars"] / 2), True, (0,0,0))
                    price_text = playthrough_name_font.render(f"{my_recipe['price']}$", True, (0,0,0))
                    break
            screen.blit(pygame.transform.scale_by(star_img, 2), (menu_cords[i][0] + 250, menu_cords[i][1] + 100))
            screen.blit(stars_text, (menu_cords[i][0] + 300, menu_cords[i][1] + 90))
            screen.blit(price_text, (menu_cords[i][0] + 250, menu_cords[i][1] + 190))

    def display_stock_screen():
        global back_button_clicked, back_button_clicktime, screen_displayed_now, plus_button_clicked, plus_button_clicktime, min_button_clicked, min_button_clicktime, stock_screen_row_counter, stock_page_displayed, selected_stock_ingredient, selected_stock_ingredient_page, buy_button_clicked, buy_button_clicktime, stock_amount_selected, balance
        
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
        if left_mouse_clicked and stock_screen_row2_rect.collidepoint(pos) and len(stock_pages[stock_page_displayed]) > 1:
            selected_stock_ingredient = stock_pages[stock_page_displayed][1]
            selected_stock_ingredient_page = stock_page_displayed
            stock_indicator_rect.y = stock_screen_row2_rect.y - stock_indicator_gap
        if left_mouse_clicked and stock_screen_row3_rect.collidepoint(pos) and len(stock_pages[stock_page_displayed]) > 2:
            selected_stock_ingredient = stock_pages[stock_page_displayed][2]
            selected_stock_ingredient_page = stock_page_displayed
            stock_indicator_rect.y = stock_screen_row3_rect.y - stock_indicator_gap
        if left_mouse_clicked and stock_screen_row4_rect.collidepoint(pos) and len(stock_pages[stock_page_displayed]) > 3:
            selected_stock_ingredient = stock_pages[stock_page_displayed][3]
            selected_stock_ingredient_page = stock_page_displayed
            stock_indicator_rect.y = stock_screen_row4_rect.y - stock_indicator_gap
        if left_mouse_clicked and stock_screen_row5_rect.collidepoint(pos) and len(stock_pages[stock_page_displayed]) > 4:
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
            screen.blit(drink_bar_library[dict["name"]], (189, stock_screen_row_cords[stock_screen_row_counter]))
            name_text = pixel_font_letters.render(dict["name"], True, (0,0,0))
            screen.blit(name_text, (320, stock_screen_row_cords[stock_screen_row_counter] + 5))
            price_text = pixel_font_numbers.render(f"${dict['price']}", True, (0,0,0))
            screen.blit(price_text, (702, stock_screen_row_cords[stock_screen_row_counter] + 3))
            owned_text = pixel_font_numbers.render(str(dict["owned"]), True, (0,0,0))
            screen.blit(owned_text, (935, stock_screen_row_cords[stock_screen_row_counter] + 3))
            stock_screen_row_counter += 1
        stock_screen_row_counter = 0

    def display_cocktailmaker():
        global newly_made_cocktail, shaking_complete, back_button_clicktime, back_button_clicked, screen_displayed_now, settings, cocktail_page_displayed, selected_cocktail_ingredient_page, selected_cocktail_ingredient, current_made_cocktail, unlocked_ingredients, current_cocktail_rects, shaking, cocktail_shaker_rect, total_dif, current_shaker_cords, temppos, currently_preparing_drink
        #-------button logic---------

        if left_mouse_clicked and back_button2_rect.collidepoint(pos):
            back_button_clicked = True
            back_button_clicktime = now

        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "homescreen"
            back_button_clicktime = 0
            current_made_cocktail = {}
            current_cocktail_rects = []
            unlocked_ingredients = list(deepcopy(backup_ingredients))
            backup_ingredients.clear()
            shaking = False
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
        if shaking:
            if cocktail_shaker_rect.collidepoint(pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if not shaking:
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
                        if ingredient_name != "ice":
                            current_cocktail_rects.append({
                                "name": ingredient_name,
                                "rect": pygame.Rect(cocktail_glass_middle - cocktail_glass_width / 2 + 2, cocktail_glass_bottom - cocktail_layer_height, cocktail_glass_width, cocktail_layer_height),
                                "color": ingredient_color_library[ingredient_name]
                            })
                    else:
                        if ingredient_name != "ice":
                            if current_cocktail_rects[-1]["name"] == ingredient_name:
                                current_cocktail_rects[-1]["rect"].height += cocktail_layer_height
                                current_cocktail_rects[-1]["rect"].y -= cocktail_layer_height
                            else:
                                current_cocktail_rects.append({
                                    "name": ingredient_name,
                                    "rect": pygame.Rect(cocktail_glass_middle - cocktail_glass_width / 2 + 2, current_cocktail_rects[-1]["rect"].y - cocktail_layer_height, cocktail_glass_width, cocktail_layer_height),
                                    "color": ingredient_color_library[ingredient_name]
                                })
        
        if len(current_made_cocktail) > 0:
            total_amount = 0
            for ingredient in current_made_cocktail:
                total_amount += current_made_cocktail[str(ingredient)]
            if total_amount == 20:
                shaking = True
                total_amount = 0

        #---------displaying---------

        screen.blit(cocktailmaker_background_img, (0,0))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button2_rect)
        rect_counter = 0
        for ingredient in cocktail_pages[cocktail_page_displayed]:
            screen.blit(drink_bar_library[ingredient["name"]], cocktailmaker_ing_rects[rect_counter])
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
        if not shaking:
            screen.blit(cocktail_glass_img, (512, 356))
            for rect in current_cocktail_rects:
                pygame.draw.rect(screen, rect["color"], rect["rect"])
            if "ice" in current_made_cocktail:
                if current_made_cocktail["ice"] == 1:
                    if len(current_cocktail_rects) > 0:
                        screen.blit(ice_layer_small_img, (cocktail_glass_middle - ice_layer_small_img.get_width() / 2 + 2, current_cocktail_rects[-1]["rect"].y - ice_layer_small_img.get_height()))
                    else:
                        screen.blit(ice_layer_small_img, (cocktail_glass_middle - ice_layer_small_img.get_width() / 2 + 2, cocktail_glass_bottom - ice_layer_small_img.get_height()))
                else:
                    if len(current_cocktail_rects) > 0:
                        screen.blit(ice_layer_big_img, (cocktail_glass_middle - ice_layer_big_img.get_width() / 2 + 2, current_cocktail_rects[-1]["rect"].y - ice_layer_big_img.get_height()))
                    else:
                        screen.blit(ice_layer_big_img, (cocktail_glass_middle - ice_layer_big_img.get_width() / 2 + 2, cocktail_glass_bottom - ice_layer_big_img.get_height()))
        if shaking:
            gap = 4
            total_width = 300
            total_height = 30
            text = pixel_font_letters.render("Shake!", True, (0,0,0))
            screen.blit(text, (WINDOW_WIDTH / 2 - text.get_width() / 2, 220))
            pygame.draw.rect(screen, (91, 91, 91), (cocktail_glass_middle - total_width / 2, WINDOW_HEIGHT - 40, total_width, total_height))
            pygame.draw.rect(screen, (151, 151, 151), (cocktail_glass_middle - total_width / 2 + gap, WINDOW_HEIGHT - 40 + gap, total_width - gap * 2, total_height - gap * 2))
            if total_dif != 0:
                pygame.draw.rect(screen, (144, 0, 0), (cocktail_glass_middle - total_width / 2 + gap, WINDOW_HEIGHT - 40 + gap, min(round(total_dif * shake_progress_rect_increaser), total_width - gap * 2), total_height - gap * 2))
            screen.blit(cocktail_shaker_img, cocktail_shaker_rect)
            if shaking_complete:
                temppos = (0,0)
                currently_preparing_drink = drink_check(current_made_cocktail)
                current_made_cocktail = {}
                current_cocktail_rects = []
                successfully_made_drink = currently_preparing_drink.get("successful", False)
                shaking_complete = False
                total_dif = 0
                shaking = False
                backup_ingredients.clear()
                cocktail_shaker_rect = cocktail_shaker_og_rect.copy()
                if successfully_made_drink == True:
                    update_recipe_book()
                    stash_cocktail()
                    successfully_made_drink = False
                else:
                    stash_smudge()
                if currently_preparing_drink.get("new drink", False) == False:
                    screen_displayed_now = "cocktail_made_screen"
                else:
                    screen_displayed_now = "cocktail_exterior_maker"

    def display_progress_screen():
        global back_button_clicked, back_button_clicktime, screen_displayed_now, customers_served, progress_rect
        #----------button logic---------

        if left_mouse_clicked and back_button_rect.collidepoint(pos):
            back_button_clicked = True
            back_button_clicktime = now

        if back_button_clicktime != 0 and back_button_clicktime <= now - click_duration:
            back_button_clicked = False

        if back_button_clicktime != 0 and back_button_clicktime <= now - screen_switch_duration:
            back_button_clicktime = 0
            screen_displayed_now = "homescreen"

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        #----------displaying----------
        
        screen.blit(progress_screen_background_img, (0,0))
        screen.blit(back_button_clicked_img if back_button_clicked else back_button_img, back_button_rect)
        pygame.draw.rect(screen, (137,0,0), progress_rect)

    def display_recipe_book():
        global recipe_page_displayed, screen_displayed_now, item_added_to_menu, displaying_recipe_book
        #---------button logic----------

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if left_mouse_clicked and recipes_left_arrow_rect.collidepoint(pos):
            if recipe_page_displayed != 0:
                recipe_page_displayed -= 1

        if left_mouse_clicked and recipes_right_arrow_rect.collidepoint(pos):
            if recipe_page_displayed != len(recipe_book_pages) - 1:
                recipe_page_displayed += 1

        if left_mouse_clicked:
            for i, rect in enumerate(add_button_rects):
             if rect.collidepoint(pos):
                 add_button_clicked_list[i] = True
                 add_button_clicktimes[i] = now
        
        for i, clicktime in enumerate(add_button_clicktimes):
            if clicktime != 0 and clicktime <= now - click_duration:
                add_button_clicked_list[i] = False
            if clicktime != 0 and clicktime <= now - screen_switch_duration:
                add_button_clicktimes[i] = 0
                if recipe_book_pages[recipe_page_displayed][i]["name"] not in cur_menu:
                    if len(cur_menu) < 4:
                        cur_menu.append(recipe_book_pages[recipe_page_displayed][i]["name"])
                        screen_displayed_now = "menu_screen"
                        displaying_recipe_book = False
                    else:
                        screen_displayed_now = "delete_from_menu"
                        item_added_to_menu = recipe_book_pages[recipe_page_displayed][i]["name"]
                        displaying_recipe_book = False

        #----------displaying-----------
        screen.fill((62, 39, 35))
        recipe_counter = 0
        
        for recipe in recipe_book_pages[recipe_page_displayed]:
            #recipe name
            name_text = save_detail_font_nums.render(recipe["name"], True, (0,0,0))
            screen.blit(name_text, (recipe_book_cords[recipe_counter][0] + (recipe_book_rects[0][2] / 2 - name_text.get_width() / 2), recipe_book_cords[recipe_counter][1] + 5))
            #recipe stars
            screen.blit(star_img, (recipe_book_cords[recipe_counter][0] + 25, recipe_book_cords[recipe_counter][1] + 15))
            stars_text = save_detail_font_nums.render(f'{int(recipe["stars"] / 2) if recipe["stars"] / 2 == int(recipe["stars"] / 2) else recipe["stars"] / 2}', True, (0,0,0))
            screen.blit(stars_text, (recipe_book_cords[recipe_counter][0] + 50, recipe_book_cords[recipe_counter][1] + 4))
            #recip price
            price_text = save_detail_font_nums.render(f"{round(recipe['price'])}$", True, (0,0,0))
            screen.blit(price_text, (recipe_book_cords[recipe_counter][0] + recipe_book_rects[0][2] - 25 - price_text.get_width(), recipe_book_cords[recipe_counter][1] + 4))
            #recipe ingredients
            step_y = recipe_book_cords[recipe_counter][1] + 46
            for ingredient, amount in recipe["preparation"].items():
                step_text_name = recipe_steps_font.render(f"{ingredient}", True, (255,255,255))
                screen.blit(step_text_name, (recipe_book_cords[recipe_counter][0] + 200, step_y))
                step_text_amount = recipe_steps_font.render(f"{amount}", True, (255,255,255))
                screen.blit(step_text_amount, (recipe_book_cords[recipe_counter][0] + 550, step_y))
                step_y += 28
            #recipe image
            drink_tag = drink_pic_lib[str(recipe["name"])]["tag"]
            drink_glass_color = drink_pic_lib[str(recipe["name"])]["glass_color"]
            screen.blit(pygame.transform.scale_by(glasses_bar_library[drink_glass_color], 3), (recipe_book_cords[recipe_counter][0] - 1, recipe_book_cords[recipe_counter][1] - 4))
            screen.blit(pygame.transform.scale_by(glass_tags_bar_library[int(drink_tag)], 3), (recipe_book_cords[recipe_counter][0] - 1, recipe_book_cords[recipe_counter][1] - 4))
            #counter
            recipe_counter += 1

        for i, rect in enumerate(add_button_rects):
            if len(recipe_book_pages[recipe_page_displayed]) >= i + 1:
                screen.blit(add_button_clicked_img if add_button_clicked_list[i] else add_button_img, rect)

        for i in range(len(recipe_book_pages[recipe_page_displayed])):
            pygame.draw.rect(screen, (0,0,0), recipe_book_rects[i], 2, border_radius=5)
        if recipe_page_displayed != 0:
            screen.blit(left_arrow_img, recipes_left_arrow_rect)
        if recipe_page_displayed != len(recipe_book_pages) - 1:
            screen.blit(right_arrow_img, recipes_right_arrow_rect)
        page_text = playthrough_name_font.render(f"{recipe_page_displayed + 1}/{len(recipe_book_pages)}", True, (255,255,255))
        screen.blit(page_text, (WINDOW_WIDTH / 2 - page_text.get_width() / 2, WINDOW_HEIGHT - page_text.get_height() - 20))

    def display_guest_screen():
        global screen_displayed_now, settings, guests, temp_guest_spawn_wait, temp_guest_timer, back_button_clicked, back_button_clicktime, balance, dragging_cocktail
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
            back_button_clicktime = 0

        #--------guest timer-------------

        if settings["sandbox"]:
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

        if settings["sandbox"]:
            for guest in guests:
                if right_mouse_clicked and guest_rects_library[guest["rect_num"]].collidepoint(pos):
                    check_unlocks()
                    client_request_completed(guest["name"], "test", 1)

        #----------displaying-----------

        screen.blit(guest_screen_background_img,  (0,0))
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
                    leaderboard_items_font,
                    custom_order_rect
                )
            screen.blit(guest_images_library[guest["image_num"]], guest_rects_library[guest["rect_num"]])
        for cocktail in stashed_cocktails:
            if cocktail["name"] == "smudge":
                screen.blit(pygame.transform.scale_by(smudge_img, 2), (stashed_cocktail_rects[cocktail["num"]].x - 33, stashed_cocktail_rects[cocktail["num"]].y - 33))
            else:
                img = drink_pic_lib[cocktail["name"]]["glass_color"]
                tag = drink_pic_lib[cocktail["name"]]["tag"]
                screen.blit(pygame.transform.scale_by(glasses_bar_library[img], 2), (stashed_cocktail_rects[cocktail["num"]].x - 33, stashed_cocktail_rects[cocktail["num"]].y - 33))
                screen.blit(pygame.transform.scale_by(glass_tags_bar_library[int(tag)], 2), (stashed_cocktail_rects[cocktail["num"]].x - 33, stashed_cocktail_rects[cocktail["num"]].y - 33))
        if dragging_cocktail:
            for cocktail in stashed_cocktails:
                if cocktail["num"] == current_dragging_cocktail:
                    name_text = save_detail_font_nums.render(cocktail["name"], True, (0,0,0))
                    stars_text = save_detail_font_nums.render(str(int(cocktail["stars"] / 2) if cocktail["stars"] / 2 == int(cocktail["stars"] / 2) else cocktail["stars"] / 2), True, (0,0,0))
                    break
            screen.blit(name_text, (10, WINDOW_HEIGHT - 45))
            screen.blit(star_img, (name_text.get_width() + 30, WINDOW_HEIGHT - 33))
            screen.blit(stars_text, (name_text.get_width() + 56, WINDOW_HEIGHT - 45))
        for i, num in enumerate(earnings_texts_timings):
            if num > 0:
                earnings_texts_timings[i] -= 1
                text = save_detail_font_nums.render(f"+{earnings_texts[i]}$", True, (50, 180, 50))
                screen.blit(text, ((guest_rects_library[i + 1].x + guest_rects_library[i + 1].width / 2) - text.get_width() / 2, 250))
        if settings["sandbox"]:
            rect_offset = 15
            money_cheat_text = leaderboard_items_font.render("money cheat - sandbox only", True, (0,0,0))
            money_cheat_rect = pygame.Rect(WINDOW_WIDTH - money_cheat_text.get_width() - rect_offset * 3, rect_offset, money_cheat_text.get_width() + 2 * rect_offset, money_cheat_text.get_height() + 2 * rect_offset)
            pygame.draw.rect(screen, (68, 137, 20), money_cheat_rect, border_radius=5)
            screen.blit(money_cheat_text, (money_cheat_rect.x + rect_offset, money_cheat_rect.y + rect_offset))
            if left_mouse_clicked and money_cheat_rect.collidepoint(pos):
                balance += 10000
                cheat_unlocks()

    def display_create_username():
        global continue_button2_clicktime, continue_button2_clicked, username, current_username_string, screen_displayed_now, username_error_message
        #----------button logic--------

        if left_mouse_clicked and continue_button2_rect.collidepoint(pos):
            continue_button2_clicked = True
            continue_button2_clicktime = now

        if continue_button2_clicktime != 0 and continue_button2_clicktime <= now - click_duration:
            continue_button2_clicked = False
        
        if continue_button2_clicktime != 0 and continue_button2_clicktime <= now - screen_switch_duration:
            continue_button2_clicktime = 0
            if len(current_username_string) == 0:
                username_error_message = "enter something"
            elif check_username_conflict(current_username_string):
                username_error_message = "username already exists"
            else:
                username = current_username_string
                initial_post()
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
        error_text = pixel_font_letters.render(username_error_message, True, (255, 0, 0))
        screen.blit(error_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def display_cocktail_made_screen():
        global screen_displayed_now, cocktail_made_window_rect, shaking, drink_tag, drink_glass_color, backup_ingredients
        screen.blit(cocktail_made_background_img, cocktail_made_window_rect)
        
        successfully_made_drink = currently_preparing_drink.get("successful", False)
        stars_text = pixel_font_letters.render(str(int(currently_preparing_drink.get('stars', 0) / 2) if currently_preparing_drink.get('stars', 0) / 2 == int(currently_preparing_drink.get('stars', 0) / 2) else currently_preparing_drink.get('stars', 0) / 2) + "/5", True, (255, 255, 255))

        if successfully_made_drink:
            name_text = pixel_font_letters.render(str(currently_preparing_drink.get('drink made', '')),True,(255, 255, 255))
            drink_tag = drink_pic_lib[str(currently_preparing_drink.get('drink made', ''))]["tag"]
            drink_glass_color = drink_pic_lib[str(currently_preparing_drink.get('drink made', ''))]["glass_color"]
        else:
            name_text = pixel_font_letters.render("smudge",True,(255, 255, 255))

        if left_mouse_clicked and not cocktail_made_window_rect.collidepoint(pos):
            if len(stashed_cocktails) < 8:
                screen_displayed_now = "cocktailmaker"
                backup_ingredients = list(deepcopy(unlocked_ingredients))
            else:
                screen_displayed_now = "homescreen"
        
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        screen.blit(name_text, (WINDOW_WIDTH / 2 - name_text.get_width() / 2, 430))

        if successfully_made_drink:
            screen.blit(stars_text, (600, 520))
            screen.blit(pygame.transform.scale_by(glasses_bar_library[drink_glass_color], 6), (442, 20))
            screen.blit(pygame.transform.scale_by(glass_tags_bar_library[int(drink_tag)], 6), (442, 20))
        else:
            screen.blit(pygame.transform.scale_by(smudge_img, 6), (442, 20))
    
    def display_cocktail_exterior_maker():
        global make_button_clicked, make_button_rect, make_button_clicktime, screen_displayed_now, shaking_complete, make_button_clicked_img, make_button_img, tags_left_arrow_clicked, tags_left_arrow_clicktime, tags_left_arrow_rect, tags_right_arrow_clicked, tags_right_arrow_clicktime, tags_right_arrow_rect, glass_left_arrow_clicked, glass_left_arrow_clicktime, glass_left_arrow_rect, glass_right_arrow_clicked, glass_right_arrow_clicktime, glass_right_arrow_rect, color_left_arrow_clicked, color_left_arrow_clicktime, color_left_arrow_rect, color_right_arrow_clicked, color_right_arrow_clicktime, color_right_arrow_rect, color_pointer, glass_pointer, cur_tag, currently_preparing_drink, cur_photo

        cur_photo = str(color_pointer) + "." + str(glass_pointer)

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # ----------------glass_right--------------------
        if left_mouse_clicked and glass_left_arrow_rect.collidepoint(pos):
            if glass_pointer >= 3:
                glass_pointer = 1
            else:
                glass_pointer += 1

        # ----------------glass_left--------------------
        if left_mouse_clicked and glass_right_arrow_rect.collidepoint(pos):
            if glass_pointer <= 1:
                glass_pointer = 3
            else:
                glass_pointer -= 1

        # ----------------color_right--------------------
        if left_mouse_clicked and color_left_arrow_rect.collidepoint(pos):
            if color_pointer >= 27:
                color_pointer = 1
            else:
                color_pointer += 1

        # ----------------color_left--------------------
        if left_mouse_clicked and color_right_arrow_rect.collidepoint(pos):
            if color_pointer <= 1:
                color_pointer = 27
            else:
                color_pointer -= 1

        # ----------------tags_right--------------------
        if left_mouse_clicked and tags_left_arrow_rect.collidepoint(pos):
            if cur_tag >= 36:
                cur_tag = 1
            cur_tag += 1

        # ----------------tags_left--------------------
        if left_mouse_clicked and tags_right_arrow_rect.collidepoint(pos):
            if cur_tag <= 1:
                cur_tag = 36
            cur_tag -= 1

        # ----------------make--------------------
        if left_mouse_clicked and make_button_rect.collidepoint(pos):
            make_button_clicked = True
            make_button_clicktime = now

        if make_button_clicktime != 0 and make_button_clicktime <= now - click_duration:
            make_button_clicked = False

        if make_button_clicktime != 0 and make_button_clicktime <= now - screen_switch_duration:
            make_button_clicktime = 0
            screen_displayed_now = "cocktail_made_screen"
            make_button_clicktime = 0
            shaking_complete = True
            drink_pic_lib.update({str(currently_preparing_drink.get('drink made', '')): {"glass_color": str(cur_photo), "tag": cur_tag}})
        
        name2_text = pixel_font_letters.render(str(currently_preparing_drink.get('drink made', '')),True,(255, 255, 255))
        
        screen.blit(coktail_exterior_customizer_background_img, (0,0))
        screen.blit(name2_text, (300, 100))
        screen.blit(make_button_clicked_img if make_button_clicked else make_button_img, make_button_rect)

        screen.blit(right_arrow_img, glass_left_arrow_rect)
        screen.blit(right_arrow_img, tags_left_arrow_rect)
        screen.blit(right_arrow_img, color_left_arrow_rect)

        screen.blit(left_arrow_img, glass_right_arrow_rect)
        screen.blit(left_arrow_img, tags_right_arrow_rect)
        screen.blit(left_arrow_img, color_right_arrow_rect)

        screen.blit(pygame.transform.scale_by(glasses_bar_library[cur_photo], 6), (200, 125))
        screen.blit(pygame.transform.scale_by(glass_tags_bar_library[cur_tag], 6), (200, 125))

    def display_delete_from_menu():
        global screen_displayed_now, item_added_to_menu
        #---------button logic----------

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        #----------displaying-----------

        screen.blit(menu_screen_background_img, (0,0))
        for i, recipe in enumerate(cur_menu):
            name_text = save_detail_font_nums.render(recipe, True, (255,255,255))
            screen.blit(name_text, (menu_cords[i][0] + (610 / 2 - name_text.get_width() / 2), menu_cords[i][1] + 10))
            drink_tag = drink_pic_lib[recipe]["tag"]
            drink_glass_color = drink_pic_lib[recipe]["glass_color"]
            screen.blit(pygame.transform.scale_by(glasses_bar_library[drink_glass_color], 5), (menu_cords[i][0] - 40, menu_cords[i][1] - 50))
            screen.blit(pygame.transform.scale_by(glass_tags_bar_library[int(drink_tag)], 5), (menu_cords[i][0] - 40, menu_cords[i][1] - 50))
        for i, rect in enumerate(delete_from_menu_rects):
            if left_mouse_clicked and rect.collidepoint(pos):
                cur_menu.pop(i)
                cur_menu.insert(i, item_added_to_menu)
                item_added_to_menu = ""
                screen_displayed_now = "menu_screen"

    def display_sandbox_warning():
        global screen_displayed_now, enable_anyway_button_clicked, enable_anyway_button_clicktime, cancel_button_clicked, cancel_button_clicktime, legit_playthrough
        #---------button logic-----------
        if left_mouse_clicked and cancel_button_rect.collidepoint(pos):
            cancel_button_clicked = True
            cancel_button_clicktime = now

        if left_mouse_clicked and enable_anyway_button_rect.collidepoint(pos):
            enable_anyway_button_clicked = True
            enable_anyway_button_clicktime = now
        
        if cancel_button_clicktime != 0 and cancel_button_clicktime <= now - click_duration:
            cancel_button_clicked = False

        if enable_anyway_button_clicktime != 0 and enable_anyway_button_clicktime <= now - click_duration:
            enable_anyway_button_clicked = False

        if cancel_button_clicktime != 0 and cancel_button_clicktime <= now - screen_switch_duration:
            cancel_button_clicktime = 0
            screen_displayed_now = "settings"
            cancel_button_clicktime = 0

        if enable_anyway_button_clicktime != 0 and enable_anyway_button_clicktime <= now - screen_switch_duration:
            enable_anyway_button_clicktime = 0
            screen_displayed_now = "settings"
            enable_anyway_button_clicktime = 0
            settings["sandbox"] = True
            legit_playthrough = False

        #--------displaying---------

        screen.blit(cocktail_made_background_img, cocktail_made_window_rect)
        screen.blit(cancel_button_clicked_img if cancel_button_clicked else cancel_button_img, cancel_button_rect)
        screen.blit(enable_anyway_button_clicked_img if enable_anyway_button_clicked else enable_anyway_button_img, enable_anyway_button_rect)

#-------------main loop-----------

while running:
    
    #---------event loop---------

    if True:
        new_ingredient_unlocked = False
        left_mouse_clicked = False
        right_mouse_clicked = False
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if screen_displayed_now != "startscreen" and screen_displayed_now != "continue_screen" and screen_displayed_now != "new_screen" and screen_displayed_now != "overwrite_screen" and screen_displayed_now != "username":
                    regular_save()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                left_mouse_clicked = True
                if cocktail_shaker_rect.collidepoint(pos):
                    dragging = True
                    temppos = pos
                    cocktail_shaker_x_offset = cocktail_shaker_rect.x - event.pos[0]
                    cocktail_shaker_y_offset = cocktail_shaker_rect.y - event.pos[1]
                for i, rect in enumerate(stashed_cocktail_rects):
                    if i not in cocktail_available_spots:
                        if rect.collidepoint(pos):
                            current_dragging_cocktail = i
                            dragging_cocktail = True
                            dragging_cocktail_x_offset = stashed_cocktail_rects[current_dragging_cocktail].x - event.pos[0]
                            dragging_cocktail_y_offset = stashed_cocktail_rects[current_dragging_cocktail].y - event.pos[1]

            if event.type == pygame.MOUSEMOTION:
                if dragging and shaking:
                    if total_dif >= max_total_difference:
                        shaking_complete = True
                    else:
                        difference_shaker_x = abs(temppos[0] - pos[0])
                        difference_shaker_y = abs(temppos[1] - pos[1])
                        total_dif += difference_shaker_y
                        total_dif += difference_shaker_x
                        temppos = pos
                        cocktail_shaker_rect.x = event.pos[0] + cocktail_shaker_x_offset
                        cocktail_shaker_rect.y = event.pos[1] + cocktail_shaker_y_offset
                if dragging_cocktail:
                    stashed_cocktail_rects[current_dragging_cocktail].x = event.pos[0] + dragging_cocktail_x_offset
                    stashed_cocktail_rects[current_dragging_cocktail].y = event.pos[1] + dragging_cocktail_y_offset

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False
                if dragging_cocktail:
                    sold = False
                    for guest in guests:
                        if guest_rects_library[guest["rect_num"]].collidepoint(pos):
                            sold = True
                            cocktail_available_spots.append(current_dragging_cocktail)
                            stashed_cocktail_rects = deepcopy(og_stashed_cocktail_rects)
                            for lib in stashed_cocktails:
                                if current_dragging_cocktail == lib["num"]:
                                    client_request_completed(guest["name"], lib['name'], lib["stars"])
                                    check_unlocks()
                                    dragging_cocktail = False
                                    stashed_cocktails.remove(lib)
                    if not sold:
                        dragging_cocktail = False
                        stashed_cocktail_rects = deepcopy(og_stashed_cocktail_rects)

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
                if event.key == pygame.K_TAB and screen_displayed_now != "username" and screen_displayed_now != "continue_screen" and screen_displayed_now != "overwrite_screen" and screen_displayed_now != "new_screen" and screen_displayed_now != "startscreen" and screen_displayed_now != "cocktail_made_screen":
                    displaying_recipe_book = not displaying_recipe_book

    #-----------updates--------------

    now = pygame.time.get_ticks()

    #-----------debugging----------

    
    
    #--------screen selection--------

    if screen_displayed_now == "username":
            display_create_username()

    elif screen_displayed_now == "continue_screen":
            display_continue_playthrough()

    elif screen_displayed_now == "overwrite_screen":
        display_overwrite_playthrough()

    elif screen_displayed_now == "new_screen":
        display_new_playthrough()

    elif screen_displayed_now == "startscreen":
        display_startscreen()

    elif screen_displayed_now == "delete_from_menu":
        display_delete_from_menu()

    elif screen_displayed_now == "legit_playthrough_warning":
        display_sandbox_warning()

    else:
        if displaying_recipe_book:
            display_recipe_book()
        else:
            if screen_displayed_now == "homescreen":
                display_homescreen()

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

            elif screen_displayed_now == "cocktail_made_screen":
                display_cocktail_made_screen()

            elif screen_displayed_now == "cocktail_exterior_maker":
                display_cocktail_exterior_maker()

    #----------------------------------

    pygame.display.update()
    clock.tick(60)

#-------------BUG_FIXES:-----------