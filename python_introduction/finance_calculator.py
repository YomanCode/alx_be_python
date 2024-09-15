income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
interest = 0.05

monthly_saving = income - monthly_expenses
projected = int(monthly_saving * 12 + (monthly_saving * 12 * interest))
print("Your monthly savings are", monthly_saving)
print("Projected saving after one year, with interest, is: ", projected)
