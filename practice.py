#UWYO COSC1010
#Example code from lab TA

#First show the creation of empty array

fruits = []

#Then add elements with the append function

fruits.append("apple")
fruits.append("bannana")
fruits.insert(1,"star fruit")
print(fruits)


#Access elements by index position

print(fruits[0])

#Loop through a list
for fruit in fruits:
    print(fruit)

#Loop with range function

for i in range(0, len(fruits)):
    print(fruits[i])

