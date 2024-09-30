Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
TimeBound = input("Is it time-bound? (yes/no): ")

match Priority:
    case 'high':
        if TimeBound == 'yes':
            print(f"Note: {Task} is a high-priority task that requires immediate attention today!")
        elif TimeBound == 'no':
            print(f"Note: {Task} is a high-priority task, but it is not time-bound.")
        else:
            print("Invalid time-bound value.")
            
    case 'medium':
        if TimeBound == 'yes':
            print(f"Note: {Task} is a medium-priority task. Consider doing it after higher-priority tasks today.")
        elif TimeBound == 'no':
            print(f"Note: {Task} is a medium-priority task. You can do it later, not time-bound.")
        else:
            print("Invalid time-bound value.")
            
    case 'low':
        if TimeBound == 'yes':
            print(f"Note: {Task} is a low-priority task, but it is time-bound.")
        elif TimeBound == 'no':
            print(f"Note: {Task} is a low-priority task. Consider completing it when you have free time.")
        else:
            print("Invalid time-bound value.")
            
    case _:
        print("Invalid priority entered.")