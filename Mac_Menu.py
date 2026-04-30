Drinks = ["Coca-Cola", "Sprite", "Fanta", "McCafé"]
meals = [
    "Big Mac",
    "McChicken",
    "Spicy McChicken",
    "Filet-O-Fish",
    "Quarter Pounder with Cheese",
    "Double Quarter Pounder with Cheese",
    "McDouble",
    "Double Cheeseburger",
    "Cheeseburger",
    "Hamburger",
    "6-piece Chicken McNuggets",
    "10-piece Chicken McNuggets",
    "20-piece Chicken McNuggets",
    "40-piece Chicken McNuggets",
    "Crispy Chicken Sandwich",
    "Deluxe Crispy Chicken Sandwich",
    "Spicy Crispy Chicken Sandwich",
    "Deluxe Spicy Crispy Chicken Sandwich",
    "Egg McMuffin",
    "Sausage McMuffin with Egg",
    "Bacon, Egg & Cheese Biscuit",
    "Sausage Biscuit with Egg",
    "Hotcakes with Sausage",
    "Sausage Burrito"
]

sauces = ["Ketchup", "Mayo", "BBQ", "Sweet & Sour"]
sizes = ["Small", "Medium", "Large", "Extra Large"]
fries = ["No Fries", "With Fries"]

#print(len(meals))
print(len(sizes))

value = int (input("Please enter the hex number: "), 16)


bin_str_value = bin(value)[2:]
bin_str_value_16 = bin_str_value[-16:].zfill(16)

'''
if bin_str_value_16[0] == 0:
    pickup = 'In-Store'
else:
    pickup = 'Drive-thru'
'''

print(bin_str_value_16)

# Shortcut if
pickup = 'In-Store' if bin_str_value_16[3] == '0' else 'Drive-thru'

payment = 'Cash' if bin_str_value_16[4] == '0' else 'Card'

sauce = sauces[int ((bin_str_value_16[5:7]),2)]

f = fries[int (bin_str_value_16[7])]

print(int ((bin_str_value_16[8:10]),2))
size = sizes[int ((bin_str_value_16[8:10]),2)]

Drink = Drinks[int ((bin_str_value_16[10:12]),2)]

meal = meals[int ((bin_str_value_16[12:17]),2)]

print("Meal Details:\nMeal:", meal + "\nDrink:", Drink + "\nSize:",
      size + "\nWith/Without fries:", f + "\nSauce type:", sauce + "\nPayment Method:",
      payment + "\nPickup: " + pickup)

print("Enjoy!")
'''
match bin_str_value_16[5:7]:
    case '00'
'''
'''
print(pickup)
print(bin(value))
print(bin_str_value)
print(bin_str_value_16)
'''



