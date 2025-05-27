# User Input for Financial Details:

# prompting user for thier monthly income
Monthly_income = int(input("Enter your monthly income: "))

# Ask for their total monthly expenses
Monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings:
Monthly_savings = Monthly_income - Monthly_expenses

print(f"Your monthly savings are ${Monthly_savings}")

# Project Annual Savings:
Projected_Savings = (Monthly_savings * 12 + (Monthly_savings * 12 * 0.05))

# projected annual savings result:
print(f"Projected savings after one year, with interest, is: ${int(Projected_Savings)}")


