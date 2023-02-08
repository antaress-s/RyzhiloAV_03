my_list = ["leaf", "cherry", "fish"]
my_list1 = ["D", "C", "B", "A"]
my_list2 = [1, 2, 3, 4, 5]
my_list3 = ["Never", "gonna", "let", "you", "down"]

my_list.sort()  # ['cherry', 'fish', 'leaf']
my_list1.sort()  # ['A', 'B', 'C', 'D']
print(sorted(my_list2, reverse=True))  # [5, 4, 3, 2, 1]
print(sorted(my_list3))  # ['Never', 'down', 'gonna', 'let', 'you']
