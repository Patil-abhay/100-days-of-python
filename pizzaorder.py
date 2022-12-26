print("Welcome to python pizza deliveries!! ")
size = input("What size of pizza do you want? S, M, L\n")
add_pepperoni = input("Do you want pepperoni?\n")
extra_cheese = input("Do you want extra chesse?\n")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else :
    bill += 25

if add_pepperoni == "Y":
    if size == "S":  
        bill += 2
    else:
        bill += 3
    
if extra_cheese == "Y":
    bill += 1


print(f"Yor final bill is ${bill}")


  
