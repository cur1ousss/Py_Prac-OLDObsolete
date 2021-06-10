# Lists & Tuples for Sequential Data
# Sets unordered data with unique no duplicates

list_Courses=["Computer Science","Maths","Physics","Biology","Chemisty"]

print(list_Courses) # Output in form of square same list >> ["Computer Science","Maths","Physics","Biology","Chemisty"]
print(len(list_Courses)) # len(ListName) prints len of list

print(list_Courses[0]) # indexing start 0 -> n-1
# Output Simple string >> Computer Science
# List Index out of Range Erorr

print(list_Courses[-1]) # -1 for the Last Element of List {for cases where size may increase and need to know only last element}

# Printing Range of Data from Lists
# Output of Range Data in Form >> ["Computer Science","Maths"]
print(list_Courses[0:3])    # listName[X:Y] last part not included (upto)

print(list_Courses[:2]) # listName[:X]  by default assumes from starting if nothing given in start

print(list_Courses[1:]) # listName[2:] by default assumes upto last if nothing given in last

# &&& Slicing Video Continue here later >> https://www.youtube.com/watch?v=ajrtAuDg3yw

# *****************************************************************************

			# Modifying List

list_Courses.append("Economics") # appends at last of list
# list_Courses.append("Psychology","Astronomy") # ERROR   >> List.append() takes only 1 argument

print(list_Courses)

list_Courses.insert(0,"Psychology") # list.insert(Position_Number,"Value") inserts at that position and shifts other automatically Not Overwrite

print(list_Courses)

list_Courses=["Computer Science","Maths","Physics","Biology","Chemisty"]

list_Courses2=["Pyschology","Economics"]

list_Courses.insert(0,list_Courses2) # can insert list within list But Outputs as Sublist >> [['Pyschology', 'Economics'], 'Computer Science', 'Maths', 'Physics', 'Biology', 'Chemisty']
print(list_Courses)



