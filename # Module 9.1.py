# Module 9.1
# Cara Riley
# CIS 245

principal = int (input("Enter the initial investment amount: "))
interest = eval(input("Enter the annual interest as decimal number (i.e 0.5 for 50% ) : "))
balance = principal
year = 0
while balance < 2 * principal:
    balance = balance + balance * ((float(interest) / 100))
year += 1
print("the time it will take for your investment to double in value at that interest rate is ", year ,"years.")