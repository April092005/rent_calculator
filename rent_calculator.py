##Total food ordered for snacking
#Electricity units spend
#Charge per unit
#Person living in room/ flat

##Output
#Total amount you have to pay is


rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount amount of food ordered = "))
electricity_spend = int(input("Enter the total amount of electricity spend = "))
charges_per_unit = int(input("Enter the number of persons living in room / falt = "))
persons = int(input("Enter the number of persons living = "))


total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output) 
