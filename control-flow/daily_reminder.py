# Personal Daily Reminder

# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

#Prompt for a Single Task:

task = input("Enter your task :")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match time_bound:
    case "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!" )

    case "no":
     print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time." )



