# 1. Create an empty list called my_list
from operator import index, indexOf

my_list = []
print("Step 1: Empty list created:", my_list)

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Step 2: Elements appended to my_list:", my_list)

# 3. Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print("Step 3: Value 15 inserted at the second position in my_list:", my_list)

# 4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print("Step 4: my_list extended with [50, 60, 70]:", my_list)

# 5. Remove the last element from my_list.
my_list.pop()
print("Step 5: Last element removed from my_list:", my_list)

# 5. Sort my_list in ascending order.
my_list.sort()
print("Step 6: my_list sorted in ascending order:", my_list)

# 6. Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print("Step 7: Index of 30 in my_list:", index_of_30)