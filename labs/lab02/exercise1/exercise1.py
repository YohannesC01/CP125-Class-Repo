# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget
    fuel_used = (one_way_km * 2) / km_per_liter
    fuel_price = fuel_used * price_per_liter 
    
    if fuel_price <= budget:
        return True
    else:
        return False
        

# Test your code here
result = is_budget_sufficient(100,10,2.00,39)
print(result)