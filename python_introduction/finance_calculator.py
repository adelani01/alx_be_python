# User Input for Financial Details:

# prompting user for monthly income
monthly_income = int(input("Enter your monthly income: "))

# Ask for their total monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings:
monthly_savings = monthly_income - monthly_expenses

print(f"Your monthly savings are ${monthly_savings}")

# Project Annual Savings:
Projected_Savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))

# projected annual savings result:
print(f"Projected savings after one year, with interest, is: ${int(Projected_Savings)}")


