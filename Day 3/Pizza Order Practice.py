# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
add_pepperoni_small = 2
add_pepperoni_medium = 3
extra_keju = 1
if size == "S":
    bill += small_pizza
    if add_pepperoni == "Y":
        bill += add_pepperoni_small    
        if extra_cheese == "Y":
            bill += extra_keju
            print(f"Your final bill is: ${bill}.")
        else :
            print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "Y":
        bill += extra_keju
        print(f"Your final bill is: ${bill}.")
    else :
        print(f"Your final bill is: ${bill}.")        
if size == "M":
    bill += medium_pizza
    if add_pepperoni == "Y":
        bill += add_pepperoni_medium    
        if extra_cheese == "Y":
            bill += extra_keju
            print(f"Your final bill is: ${bill}.")
        else :
            print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "Y":
        bill += extra_keju
        print(f"Your final bill is: ${bill}.")
    else :
        print(f"Your final bill is: ${bill}.")        
if size == "L":
    bill += large_pizza
    if add_pepperoni == "Y":
        bill += add_pepperoni_large    
        if extra_cheese == "Y":
            bill += extra_keju
            print(f"Your final bill is: ${bill}.")
        else :
            print(f"Your final bill is: ${bill}.")
    elif extra_cheese == "Y":
        bill += extra_keju
        print(f"Your final bill is: ${bill}.")
    else :
        print(f"Your final bill is: ${bill}.")        