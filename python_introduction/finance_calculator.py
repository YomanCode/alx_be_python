income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
interest = 0.05

saving = income - expenses
projected = saving * 12 + (saving * 12 * interest)
print("Your monthly savings are", saving)
print("Projected saving after one year, with interest, is: ", projected)
