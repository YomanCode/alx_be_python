Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower
time_bound = input("Is it time-bound? (yes/no): ").lower

match Priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: {Task} is a high-priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Reminder: {Task} is a high-priority task, but it is not time-bound.")
        else:
            print("Invalid time-bound value.")
            
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: {Task} is a medium-priority task. Consider doing it after higher-priority tasks today.")
        elif time_bound == 'no':
            print(f"Reminder: {Task} is a medium-priority task. You can do it later, not time-bound.")
        else:
            print("Invalid time-bound value.")
            
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: {Task} is a low-priority task, but it is time-bound.")
        elif time_bound == 'no':
            print(f"Reminder: {Task} is a low-priority task. Consider completing it when you have free time.")
        else:
            print("Invalid time-bound value.")
            

    case _:
        print("Invalid priority entered.")