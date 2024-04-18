import random

from flask import jsonify
import flask
#import DinningHallData



food_items = [
    {"name": "Chicken Breast", "calories": 230, "protein": 30, "carbohydrates": 0, "fats": 5},
    {"name": "Salmon", "calories": 300, "protein": 25, "carbohydrates": 0, "fats": 20},
    {"name": "Brown Rice", "calories": 200, "protein": 5, "carbohydrates": 45, "fats": 2},
    {"name": "Broccoli", "calories": 50, "protein": 5, "carbohydrates": 10, "fats": 0.5},
    {"name": "Quinoa", "calories": 220, "protein": 8, "carbohydrates": 40, "fats": 3},
    {"name": "Spinach", "calories": 10, "protein": 1, "carbohydrates": 2, "fats": 0},
    {"name": "Sweet Potato", "calories": 180, "protein": 3, "carbohydrates": 40, "fats": 0.5},
    {"name": "Eggs", "calories": 70, "protein": 6, "carbohydrates": 1, "fats": 5},
    # Sample can be replaced with data from API 
]

input_protein = int(input("Please enter your protein")) 
input_carbs = int(input("Please enter your carbs"))
input_fats = int(input("Please enter your fats")) 

fats_upper_bound = input_fats + 10 
fats_lower_bound = input_fats - 10

carbs_upper_bound = input_carbs + 10
carbs_lower_bound = input_carbs - 10

def generate_meal_plan(food_items, input_fats):
    """Generate a meal plan with random selection of food items."""
    fats = 0
    carbs = 0
    protein = 0
    meal_plan = []

    # Continue selecting food items until the total fats content is within the specified limit
    
    while fats <= fats_upper_bound or carbs <= carbs_upper_bound:  # Assuming a buffer of 5g of fats
        selected_item = random.choice(food_items)
        
        # Check if adding the selected item would exceed the fats limit
        if fats + selected_item["fats"] < input_fats and carbs + selected_item["carbohydrates"] < input_carbs and protein + selected_item["protein"]:
            meal_plan.append(selected_item)
            fats += selected_item["fats"]
            carbs += selected_item["carbohydrates"]
            protein += selected_item["protein"]

        elif (fats + selected_item["fats"] < input_fats + 10 or fats + selected_item["fats"] > input_fats - 10) and (
            carbs + selected_item["carbohydrates"] < input_carbs + 10 or carbs + selected_item["carbohydrates"] > input_carbs - 10) and (
            protein + selected_item["carbohydrates"] < input_protein + 10 or protein + selected_item["carbohydrates"] > input_protein - 10):
            meal_plan.append(selected_item)
            print("hi")
            fats += selected_item["fats"]
            carbs += selected_item["carbohydrates"]
            protein += selected_item["protein"]

            break


          # Exit the loop if adding the item would exceed the fats limit
    

    return meal_plan #flask.jsonify({"plan": meal_plan})   
    

#Displaying the generated meal plan -->  
def display_meal_plan(meal_plan):
    """Display the meal plan with nutritional information."""
    total_calories = sum(item["calories"] for item in meal_plan)
    total_protein = sum(item["protein"] for item in meal_plan)
    total_carbohydrates = sum(item["carbohydrates"] for item in meal_plan)
    total_fats = sum(item["fats"] for item in meal_plan)

    print("Meal Plan:")
    print("-----------")
    for item in meal_plan:
        print(f"{item['name']}: {item['calories']} calories, {item['protein']}g protein, {item['carbohydrates']}g carbohydrates, {item['fats']}g fats")
    print("-----------")
    print(f"Total: {total_calories} calories, {total_protein}g protein, {total_carbohydrates}g carbohydrates, {total_fats}g fats")
    print()

# Number of meal plans to generate
num_meal_plans = 3

# Generate and display multiple meal plans
for i in range(num_meal_plans):
    print(f"Meal Plan {i+1}:")
    meal_plan = generate_meal_plan(food_items, input_fats)
    display_meal_plan(meal_plan)

#flask.jsonify(meal_plan)