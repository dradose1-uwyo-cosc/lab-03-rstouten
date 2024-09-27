# Reuben Stoutenburg
# UWYO COSC 1010
# 9/26/2024
# Lab 03 
# Lab Section: 
# Sources

#Create a list that contains the elements:  Wyoming, Colorado, Montana in that order 

states = ["Wyoming", "Colorado", "Montana"]

#print the list

print(states)

#print the first element in the list

print(states[0])

#print last element

print(states[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided

print(f"{states[1].upper()} is south of {states[0].upper()}")

print("Part Two-------------------------------------------------------------------------")

#Append the following states to your list: Washington, Oregon, California and print your list

states.append("Washington")
states.append("Oregon")
states.append("California")

print(states)

#override the second to last element to be Maine and print

states[-2] = "Maine"
print(states)

#Insert the state Texas to be the third element in the list, again printing your list

states.insert(2,"Texas")
print(states)

#Using the `del` statement remove the fourth item from the list, print your list 

del states[3]
print(states)

#Remove Texas using its value, print the list

states.remove("Texas")

print("Part Three----------------------------------------------------------------------")

#Temporarily sort your list, print it both sorted and unsorted 

print(sorted(states))
print(states)

#Permanently sort your list in reverse order, printing it out

states.sort(reverse=True)

#Using the reverse method reverse the list and print it

states.reverse()
print(states)

