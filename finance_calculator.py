import math

simple = ""
compound = ""
deposit = ""
interest_rate = ""
interest = ""
interest_bond = ""
year = ""
month = ""

# In case the user enters upper or lower case letters or camel letters, it is necessary to add '.lower()'
calculator = str(input("Choose either 'investment' or 'bond' from the menu below to proceed: \n"
                       "investment \t - \t to calculate the amount of interest you'll earn on your investment \n"
                       "bond \t \t - \t to calculate the amount of you'll have to pay on a home loan \n" 
                       "Please enter your answer here: ")).lower()
# user have to enter investment or bond
while True:
    if calculator == "investment":
        deposit = float(input("Please enter the amount of money you want to deposit: "))
        interest_rate = float(input("What percent interest rate do you want to use?: % "))
        year = int(input("Please enter the number of years you plan on investing: "))
        interest_bond = str(input("Which interest would you like to use? 'simple' or 'compound': ")).lower()

        # user have to enter simple or compound
        if interest_bond == "simple":
            total_amount = deposit * (1 + (interest_rate * 0.01) * year)
            print(f"Total amount is : {total_amount}")
            break
        if interest_bond == "compound":
            total_amount = deposit * math.pow((1 + (interest_rate * 0.01)), year)
            print(f"Total amount is : {total_amount}")
            break
        else:
            print("This data is not valid! Please restart and enter the correct value")
            break

    if calculator == "bond":
        house = float(input("Please enter the present value of the house: "))
        interest_rate = float(input("What percent interest rate do you want to use?: % "))
        month = int(input("Please enter the number of you plan to take repay the bond: "))

        """ we have to convert the interest rate that user entered to percentile by dividing 100
        and divide by 12 as well to calculate the monthly payment """

        repayment = float(house * (interest_rate * 0.01 / 12) / (1 - (1 + interest_rate * 0.01 / 12) ** (-month)))
        print(f"You have to repay each month {repayment}")
        break
    else:
        print("This data is not valid! Please restart and enter the correct value")
        break
