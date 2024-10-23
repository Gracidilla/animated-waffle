# Grace Maurer
# Program 9 - Tracker
# COP 2500 0V06
# April 11th 2024


def load_goals(goals):
    
    # adds 3 goals to the dictionary
        # loops 3 times
        # takes in category and value as input
        # goals[category] = value
        
    for i in range(3):
        category = str(input("Enter a category for your goal:"))
        print("Enter your target for",category,":")
        target = int(input(""))
#        Target = int(input("Enter your target for",category,": "))
        goals[category]= target

    return goals

        
def load_data():
    
    # create a dictionary
    given_targets = {}

    
    print("Enter your data with the category and measurement.\n")
    print("Type 'done' when done for today'\n")
    
    category = str(input("Enter Category:\n"))

    
    # while category isnt done
        # take in input for category and value
        
    while (category != "done"):
        value = int(input("Enter value:"))

        # if category is in dictionary

        if category in given_targets:
            print ("You have a value for", + category, ".")
            # ask if they want to add or replace
            choice = input(int("Do you want to (1) Add to Steps, or (2) Replace Steps?"))
                # if add
                    # add the values
            if choice==1:
                given_targets[category] += value
                    # replace
                        # replace the values
            elif choice==2:
                given_targets[category] = value
                            # else
                # add it to the dictionary
        else:
            given_targets[category] = value

        category = str(input("Enter Category:\n"))
        
    # return dictionary
        return given_targets
    
    
def compare_data(goals, target_value):
    count = 0
        # loop through the goals
        # if the goal category is in day
            # compare their values
                # add to a counter variable
                
    for key in goals:
        if key in given_targets:
            # if goal is met, returns 1 and adds 1 to the goal-met count.
            if given_targets[key] >= goals[key]:
                count += 1
                return 1
            # if goal is not met, returns 0.
            else:
                return 0



def main():
    goals = {}
    goals = load_goals(goals)
    hit = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week = []
    
    for i in range(7):
        
        if (i == 4):
             print("It's", days[i], "- Happy Friday!\n")
        else:
            print("It's", days[i], ".")
        day=load_data()
        current = compare_data(goals, day)
        hit += current 

    print("You hit your goal", hit, "times")

    

main()
