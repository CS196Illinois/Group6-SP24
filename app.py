from flask import Flask, jsonify, request, render_template

from flask_cors import CORS, cross_origin
from Meal_Plan_Generator import generate_meal_plan

app = Flask(__name__)
cors = CORS(app)

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

@app.route("/home", methods = ['GET'])
def home():
    return jsonify({'text':"Hi"})


@app.route("/home/<data>", methods = ['GET'])
def home2(data):
    return jsonify({'text':data})

@app.route("/getPlan", methods = ['GET'])
def get_meal(): 
    input_protein = request.json['protein']
    input_fats = request.json['fat']
    input_carbs = request.json['carbs']
    dinning_hall = request.json['hall']
    meal = request.json['meal']
    date = request.json['date']
    output = generate_meal_plan(food_items, input_fats, input_carbs, input_protein)
    return jsonify({"plan": output})