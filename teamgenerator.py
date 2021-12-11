import random

students = ['Student 1', 'Student 2','Student 3', 'Student 4', 'Student 5', 'Student 6',
'Student 7', 'Student 8', 'Student 9', 'Student 10', 'Student 11', 'Student 12', 'Student 13',
'Student 14', 'Student 15', 'Student 16', 'Student 17', 'Student 18', 'Student 19',
'Student 20', 'Student 21', 'Student 22', 'Student 23', 'Student 24', 'Student 25', 'Student 26'
'Student 27']
    
def main() :
    
    groupNum = int(input('How many groups do you want to make?:'))

    def make_random_groups(students, number_of_groups):
    
        #Shuffle list of students
        random.shuffle(students)
    
        #Create groups
        all_groups = []
        for index in range(number_of_groups):
            group = students[index::number_of_groups]
        all_groups.append(group)
    
        #Format and display groups
        for index, group in enumerate(all_groups):
            print(f"Group {index+1}: {' / '.join(group)}\n")
    
    groupNum = int(input('How many groups do you want to make?:'))
    make_random_groups(students, groupNum)

# end of main()

main()

answer = input("Are you happy with these results? [y/n]:")
if answer == "y" :
    print("Good!")
    print("Exiting program")
    quit()
elif answer == "n" :
    main()
else :
    print("That input is not recognized, next time answer with y or n.")
if answer == "cake" :
    print("The cake is a lie!")
