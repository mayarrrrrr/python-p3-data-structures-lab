spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    
    # names = []
    # for food in spicy_foods:
    #     names.append(food["name"])
    # return names

    names = [food["name"] for food in spicy_foods]
    return names
print(get_names(spicy_foods))
    

def get_spiciest_foods(spicy_foods):
    # heat_food = []
    # for food in spicy_foods:
    #     heat_level = food["heat_level"]
    #     if (heat_level > 5):
    #        heat_food.append(food)
    # return heat_food 
    heat_food = [food for food in spicy_foods if food["heat_level"]>5]
    return heat_food
    pass  
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
print(print_spicy_foods(spicy_foods))        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
get_spicy_food_by_cuisine(spicy_foods, "American")

def print_spiciest_foods(spicy_foods):
    
    
    return print_spicy_foods(get_spiciest_foods(spicy_foods))
        
print(print_spiciest_foods(spicy_foods))


def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)
    if num_spicy_foods == 0:
        return 0  # Avoid division by zero error
    return total_heat_level // num_spicy_foods
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()  # Create a copy of the original list
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
create_spicy_food(spicy_foods,spicy_food={ "name": "Kimchi",
    "cuisine": "Korean",
    "heat_level": 7,})
