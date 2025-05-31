# Personal Daily Reminder

# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

#Prompt for a Single Task:

Task = input("Enter your task:")
Priority = input("Priority (high/medium/low):")
Time_Bound = input("Is it time-bound? (yes/no):")

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!" )
        
        else:
             print(f"Note: '{Task}' is a {Priority} priority task. Consider completing it when you have free time." )


    case "medium":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!" )

        else:
             print(f"Note: '{Task}' is a {Priority} priority task. Consider completing it when you have free time." )

    case "low":
        if Time_Bound == "yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!" )

        else:
             print(f"Note: '{Task}' is a {Priority} priority task. Consider completing it when you have free time." )

    



