# Troy Jeffrey Amegashie
# Exam2
# 04/10/2020

import random
from Search_Methods import bubble_sort
from Search_Methods import selection_sort
from Search_Methods import insertion_sort
from Search_Methods import merge_sort
from Search_Methods import quick_sort


user_list = []
method = 0

while method != 6:
    print("\n>Sort your list using  any of the sort methods below. What sort method would you like to use?""")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Exit Program")
    method = int(input("\n>"))

    print("\nHow many numbers do you want in your list?")
    number = int(input(">"))

    for i in range(0, number):
        n = random.randint(1, 100000)
        user_list.append(n)
    print(f"\nHere's you original list : {user_list}")

    if method == 1:
        bubble_sort(user_list)
        print(f"\nHere's your sorted list {user_list}")

    elif method == 2:
        selection_sort(user_list)
        print(f"\nHere's your sorted list {user_list}")

    elif method == 3:
        insertion_sort(user_list)
        print(f"\nHere's your sorted list {user_list}")

    elif method == 4:
        merge_sort(user_list)
        print(f"\nHere's your sorted list {user_list}")

    elif method == 5:
        quick_sort(user_list)
        print(f"\nHere's your sorted list {user_list}")
