#######################################
############QUES 1 ####################
#######################################
my_roll_no = 1024160001
L = []
while(my_roll_no>0):
    roll = my_roll_no%10
    L.append(roll*10)
    my_roll_no = my_roll_no//10
print(L)

#ques1 ii
L.append(0)
print(L)
L.insert(2,5)
print(L)

#ques1 iii
L.pop()
print(L)
L.remove(0)
print(L)

#ques1 iv
L.sort()
print(L)
L.sort(reverse=True)
print(L)

#ques1 v
print(L[0:3])
print(L[-3:])

#ques1 vi
avg = sum(L)/len(L)
A = []
print(avg)
for i in L:
    if i>avg:
        A.append(i)
print(A)

#######################################
############QUES 2 ####################
#######################################

scores = (60, 40, 20, 10, 10, 10, 5, 0)

#ques2 i
max_val = max(scores)
idx = scores.index(max_val)
print(max_val)
print(idx)

min_val = min(scores)
print(min_val)
n = scores.count(min_val)
print(n)


#ques2 ii
rev_scores = tuple(reversed(scores))
print(rev_scores)

#ques2 iii
user = int(input("enter a number:"))
if user in scores:
    print("yes")
else:
    print("no")

# #ques2 iv
# scores[0] = 1
# # 'tuple' object does not support item assignment

#ques2 v
first , second , *rest = scores
print(first)
print(second)
print(rest)

#######################################
############QUES 3 ####################
#######################################

import random
random.seed(1024160001)

#ques3 i
my_list = []
for i in range(100):
    my_list.append((random.randint(100,900)))

print(my_list)


#ques3 ii
odd_numbers = [x for x in my_list if x % 2 != 0]
print("Odd numbers:", odd_numbers)
print("Count of odd numbers:", len(odd_numbers))

#ques3 iii
even_numbers = [x for x in my_list if x % 2 == 0]
print("Even numbers:", even_numbers)
print("Count of even numbers:", len(even_numbers))

#ques3 iv
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

prime_numbers = [x for x in my_list if is_prime(x)]

print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", len(prime_numbers))

#ques3 v
most_frequent = max(set(my_list), key=my_list.count)
frequency = my_list.count(most_frequent)

print("Most frequent number:", most_frequent)
print("Frequency:", frequency)

#######################################
############QUES 4 ####################
#######################################

digits = [1,0,2,4,1,6,0,0,0,1]

#ques4 Create sets A and B
A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("Set A:", A)
print("Set B:", B)

#ques4 vi. Union of A and B
uni = A.union(B)
print("Union of A and B:", uni)

#ques4 vii Intersection of A and B
intersection = A.intersection(B)
print("Intersection of A and B:", intersection)

# viii. Difference
A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print("A - B:", A_minus_B)
print("B - A:", B_minus_A)

#quqes4 ix. Symmetric difference
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference:", symmetric_diff)

#ques4 x. Subset and superset
print("Is A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))

#ques4 xi
X = int(input("Enter a value X: "))

A.discard(X)

print("Set A after discarding X:", A)

#######################################
############QUES 5 ####################
#######################################

# Original dictionary
my_dict = {
    "name": "Aditya",
    "roll_no": 124,
    "branch": "CSE",
    "age": 20,
    "city": "Chandigarh"
}

#ques5 i & ii. Rename "city" to "location" using pop()
my_dict["location"] = my_dict.pop("city")

# Add CGPA
my_dict["cgpa"] = 9.0

# iii. Increase age by 1
my_dict["age"] += 1

print("Updated dictionary:", my_dict)


# iv. Delete "branch" using pop() in one copy
dict_pop = my_dict.copy()

removed_branch = dict_pop.pop("branch")

print("\nUsing pop():")
print("Removed value:", removed_branch)
print("Dictionary:", dict_pop)


# Delete "branch" using del in another copy
dict_del = my_dict.copy()

del dict_del["branch"]

print("\nUsing del:")
print("Dictionary:", dict_del)


# v. Iterate using .items()
print("\nKey-value pairs:")

for key, value in my_dict.items():
    print(f"{key} → {value}")


# vi. Check whether "email" exists
print("\nChecking for email:")

if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email not found.")


# vii. Friend's dictionary
friend_dict = {
    "name": "Ak",
    "roll_no": "123",
    "branch": "CSE",
    "age": 20,
    "city": "Delhi"
}

# Merge dictionaries
merged_dict = {**my_dict, **friend_dict}

print("\nMerged dictionary:", merged_dict)



# viii. Dictionary comprehension
string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nDictionary containing only string values:")
print(string_values)