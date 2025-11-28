def hotel_costs(nights):
    return nights * 140
def plane_ride_costs(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_costs(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost
def holiday_costs(city, days, spending_money):
    return hotel_costs(days) + plane_ride_costs(city) + rental_car_costs(days) + spending_money
print(holiday_costs("Los Angeles", 5, 600))