import random

def generate_meal(food_items, protein_range, carbs_range, fats_range):
    """
    Generate a meal plan with random selection of food items
    ensuring total protein, carbs, and fats intake falls within the specified range.
    """
    meal_plan = []
    total_protein = 0
    total_carbs = 0
    total_fats = 0
    
    while total_protein < protein_range[0] or total_protein > protein_range[1] \
            or total_carbs < carbs_range[0] or total_carbs > carbs_range[1] \
            or total_fats < fats_range[0] or total_fats > fats_range[1]:
        
        # Randomly shuffle the food items
        random.shuffle(food_items)
        
        # Add items to the meal plan until the ranges are met
        for item in food_items:
            if total_protein + item["protein"] <= protein_range[1] \
                    and total_carbs + item["carbs"] <= carbs_range[1] \
                    and total_fats + item["fats"] <= fats_range[1]:
                
                meal_plan.append(item)
                total_protein += item["protein"]
                total_carbs += item["carbs"]
                total_fats += item["fats"]
                if total_protein >= protein_range[0] \
                        and total_protein <= protein_range[1] \
                        and total_carbs >= carbs_range[0] \
                        and total_carbs <= carbs_range[1] \
                        and total_fats >= fats_range[0] \
                        and total_fats <= fats_range[1]:
                    break
    
    return meal_plan

# Example usage:
food_items = [
    {"name": "Chicken Breast", "protein": 30, "carbs": 0, "fats": 5},
    {"name": "Salmon", "protein": 25, "carbs": 0, "fats": 20},
    {"name": "Brown Rice", "protein": 5, "carbs": 45, "fats": 2},
    {"name": "Broccoli", "protein": 5, "carbs": 10, "fats": 0.5},
    {"name": "Quinoa", "protein": 8, "carbs": 40, "fats": 3},
    {"name": "Spinach", "protein": 1, "carbs": 2, "fats": 0},
    {"name": "Sweet Potato", "protein": 3, "carbs": 40, "fats": 0.5},
    {"name": "Eggs", "protein": 6, "carbs": 1, "fats": 5},
    # Add more food items as needed
]

# Define the protein, carbs, and fats range for a person
protein_range = (80, 100)  # Example protein range (in grams)
carbs_range = (200, 300)   # Example carbs range (in grams)
fats_range = (50, 70)      # Example fats range (in grams)

# Generate a meal plan
meal_plan = generate_meal(food_items, protein_range, carbs_range, fats_range)

# Print the generated meal plan
print("Generated Meal Plan:")
for item in meal_plan:
    print(f"{item['name']}: Protein - {item['protein']}g, Carbs - {item['carbs']}g, Fats - {item['fats']}g")
