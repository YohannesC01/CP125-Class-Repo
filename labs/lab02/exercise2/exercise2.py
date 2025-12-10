# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    tent_cost = math.ceil(participants / tent_capacity) * tent_price
    food_cost = participants * meal_price

    total_cost = tent_cost + food_cost
    
    return total_cost
# Test your code here

