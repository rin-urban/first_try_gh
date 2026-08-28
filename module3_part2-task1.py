#part2 - task1

my_list = [1.5,7, True, 'Hi', 'Bye', 'Hi', 7.5, True, 'Bye', 'Bye']
my_set = set(my_list)
list_of_repeats = []

for i in my_set:
    if my_list.count(i)>1:
        list_of_repeats.append(i)

print(list_of_repeats)