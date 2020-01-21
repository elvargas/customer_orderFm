# File: customer_orderFm.py
# Assignment 4.1
# Eric Vargas
# DESC: Program define the calc_total_cost function which will calculate the total cost of a fiber optic cable installation.
# You will prompt the user for the number of fiber optic cable they need installed. Using the default value of $0.87 calculate the total expense.
# If the user purchases more than 100 feet they are charged $0.80 per foot. If the user purchases more than 250 feet they will be charged $0.70 per foot.
# If they purchase more than 500 feet, they will be charged $0.50 per foot. Program will display company name, fiber optic cable needed, and total cost.

def calc_total_cost(cable_length):
    # check for feet entered is valid or not
    if cable_length > 0:
        # length greater than 100 and less than 250
        if 100 < cable_length < 250:
            total_cost = cable_length * 0.80
        # Length greater than 250 and less than 500
        elif 250 < cable_length < 500:
            total_cost = cable_length * 0.70
        # Length greater than 500
        elif cable_length > 500:
            total_cost = cable_length * 0.50
        # Length = less than 100
        else:
            total_cost = cable_length * 0.87
        return total_cost
    elif cable_length < 0:
        return 0


if __name__ == '__main__':
    print("*** ORDER FORM ***")
    # ask for company name as input from user
    cmpName = input("Please enter your company name:  ")
    # ask the number of feet of fiber cable as input
    ftCable = int(input("Length of Fiber Optic Cable needed for Installation (Ft) "))

    # Calculate total installation cost
    total_cost = calc_total_cost(ftCable)
    # Print company name, number of feet and Total cost
    print("*** RECEIPT *** ")
    print("Company name: ", cmpName)
    print("Fiber Optic Cable Needed (Ft) :", ftCable)
    print("Total cost: $", total_cost)
