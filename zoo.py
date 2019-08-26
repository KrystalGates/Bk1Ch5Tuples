# 1. Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("bear", "beaver", "lion", "penguin", "giraffe", "rhino", "monkey", "anteater", "tiger", "flamingo")

# 2. Find one of your animals using the tuple.index(value) syntax on the tuple.
# Example
# flowers = ("daisy", "rose")
# flower.index("rose") # Output is 1

index_of_animal = zoo.index("penguin")
print(index_of_animal)

# 3. Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "kangaroo"
if animal_to_find in zoo:
    # Print that the animal was found
    print("The animal was found")

# 4. You can reverse engineer a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
()

# 5. Create a variable for the first three animals in your zoo tuple, and print them to the console.
first_three_animals = zoo[slice(3)]
print(first_three_animals)

# 6. Convert your tuple into a list.
zoo_list = list(zoo)
print(zoo_list)

# 7. Use extend() to add three more animals to your zoo.
zoo_list.extend(["kangaroo", "shark", "platypus"])
print(zoo_list)

# Convert the list back into a tuple.
zoo = tuple(zoo_list)
print("back to tuple", zoo)