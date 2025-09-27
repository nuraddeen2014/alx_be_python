task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
          print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!") if time_bound == "yes" else print(f"Reminder: '{task}' is a high priority task that doen't require immediate attention today!")

    case "medium":
          print(f"Reminder: '{task}' is a medium priority task that requires immediate attention after high priority tasks.") if time_bound == "high" else print(f"Reminder: '{task}' is a medium priority task that does not require immediate attention after high priority tasks.")

    case "low":
          print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
          
  