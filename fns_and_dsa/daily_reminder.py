task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time == 'yes':
            print(f"Note: {task} is a high-priority task that requires immediate attention today!")
        elif time == 'no':
            print(f"Note: {task} is a high-priority task, but not time-bound.")
        else:
            print("Invalid time-bound value.")
            
    case 'medium':
        if time == 'yes':
            print(f"Note: {task} is a medium-priority task. Consider doing it after higher-priority tasks today.")
        elif time == 'no':
            print(f"Note: {task} is a medium-priority task. You can do it later, not time-bound.")
        else:
            print("Invalid time-bound value.")
            
    case 'low':
        if time == 'yes':
            print(f"Note: {task} is a low-priority task, but it is time-bound.")
        elif time == 'no':
            print(f"Note: {task} is a low-priority task. Consider completing it when you have free time.")
        else:
            print("Invalid time-bound value.")
            
    case _:
        print("Invalid priority entered.")