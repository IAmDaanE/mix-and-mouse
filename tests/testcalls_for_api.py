import requests

base_url = "https://cocktail-game-leaderboard-api.onrender.com"

def add_data_test():
    name = input("Enter username: ")
    customers_served = int(input("Enter customers served: "))
    best_cocktail_value = int(input("Enter best cocktail value: "))
    response = requests.post(f"{base_url}/initial_post", json={"name": name, "customers_served": customers_served, "best_cocktail_value": best_cocktail_value})
    print(response)

def update_data_test():
    name = input("Enter username: ")
    customers_served = int(input("Enter customers served: "))
    best_cocktail_value = int(input("Enter best cocktail value: "))
    response = requests.post(f"{base_url}/update_post", json={"name": name, "customers_served": customers_served, "best_cocktail_value": best_cocktail_value})
    print(response)

def best_recipe_test():
    response = requests.get(f"{base_url}/best_recipe")
    data = response.json()
    print(f"{data[0][0]:<20}{data[0][1]}")

def wakeup_test():
    response = requests.get(f"{base_url}/wakeup")
    print(response)

def sql_injection_test():
    name = "DELETE FROM scores;"
    customers_served = 50
    best_cocktail_value = 60
    response = requests.post(f"{base_url}/post", json={"name": name, "customers_served": customers_served, "best_cocktail_value": best_cocktail_value})
    print(response)

update_data_test()
#sql_injection_test()
#add_data_test()