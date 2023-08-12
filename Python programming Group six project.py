#GROUP SIX(6) PROJECT WORK

"""
MEMBERS WHO PARTICIPATED IN THE PROJECT(Everyone Participated)

    Name                       Training ID
1. Ransford Addai                32524
2. Chidozie Egbu                 31562
3. Alhazzan Adeyemi              31342
4. Nasilu Fred                   31633
5. Chioma Edward                 32208
6. Maryam Baba                   32378
7. Chukwumuanya Nwanko           32633
8. Alice Egonu                   32724
9. Oluwabukola Alade             32359
10.Allan Shikomere               31530

"""




                    #QUESTION ONE(LISTS)

# Task 1: Create a Python list containing the names of five different fruits. Print the list.
fruits_list = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
print("Original fruits list:", fruits_list)

# Task 2: Append two more fruits to the list and print the updated list.
fruits_list.append("Strawberry")
fruits_list.append("Watermelon")
print("Updated fruits list:", fruits_list)

# Task 3: Remove the third fruit from the list and print the list again.
del fruits_list[2]
print("Fruits list after removing the third fruit:", fruits_list)

# Task 4: Create two more lists, merge them into a single list and sort it in ascending order.
list1 = [10, 5, 20, 15]
list2 = [8, 12, 6, 18]
merged_list = list1 + list2
sorted_list = sorted(merged_list)
print("Sorted merged list:", sorted_list)

# Task 5: Write a code to count the occurrences of a specific fruit in the list.
specific_fruit = "Banana"
fruit_count = fruits_list.count(specific_fruit)
print(f"The number of occurrences of {specific_fruit} in the fruits list is:", fruit_count)






                    #QUESTION TWO(SETS)

# Task 1: Create two sets: one containing the names of five colors and another with five different shapes.
colors_set = {"Red", "Green", "Blue", "Yellow", "Orange"}
shapes_set = {"Circle", "Triangle", "Square", "Rectangle", "Pentagon"}

# Task 2: Find and print the intersection of the two sets.
intersection_set = colors_set.intersection(shapes_set)
print("Intersection of colors and shapes sets:", intersection_set)

# Task 3: Add two more colors to the first set and remove one shape from the second set.
colors_set.add("Purple")
colors_set.add("Pink")
shapes_set.remove("Pentagon")

# Task 4: Check if the intersection between the updated sets is empty.
updated_intersection_set = colors_set.intersection(shapes_set)
is_intersection_empty = len(updated_intersection_set) == 0
print("Is the intersection between updated sets empty?", is_intersection_empty)

# Task 5: Write a code to remove duplicates from a given list using sets.
def remove_duplicates_from_list(input_list):
    unique_list = list(set(input_list))
    return unique_list

given_list = [1, 2, 2, 3, 4, 5, 5, 6]
unique_list = remove_duplicates_from_list(given_list)
print("List with duplicates removed:", unique_list)






                    #QUESTION THREE(DICTIONARIES)

# Task 1: Create a dictionary representing the personal details of three friends (name, age, city).
friends_dict = {
    "Friend1": {"name": "Alice", "age": 25, "city": "New York"},
    "Friend2": {"name": "Bob", "age": 30, "city": "San Francisco"},
    "Friend3": {"name": "Charlie", "age": 28, "city": "Los Angeles"}
}

# Task 2: Add one more friend to the dictionary and print the updated dictionary.
friends_dict["Friend4"] = {"name": "David", "age": 27, "city": "Chicago"}
print("Updated dictionary with a new friend:", friends_dict)

# Task 3: Access and print the age of one of the friends from the dictionary.
selected_friend = "Friend2"
age_of_selected_friend = friends_dict[selected_friend]["age"]
print(f"The age of {selected_friend} is:", age_of_selected_friend)

# Task 4: Remove one friend from the dictionary and print the final version.
removed_friend = "Friend3"
if removed_friend in friends_dict:
    del friends_dict[removed_friend]
print("Final dictionary after removing a friend:", friends_dict)

# Task 5: Write a code to find the friend with the highest age in the dictionary.
def friend_with_highest_age(dictionary):
    max_age = 0
    friend_with_max_age = None

    for friend, details in dictionary.items():
        if details["age"] > max_age:
            max_age = details["age"]
            friend_with_max_age = friend

    return friend_with_max_age

friend_with_highest_age = friend_with_highest_age(friends_dict)
print(f"The friend with the highest age is: {friend_with_highest_age}")