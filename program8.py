#lambda function in python

#lambda arguments: expression

add = lambda x, y: x+y
print(add(4, 5))

sq = lambda x: x**2
print(sq(11))

list_of_tuples = [(4, 'nis'), (2, 'tap'), (32, 'mow')]
sorted_list_of_tuples = sorted(list_of_tuples, key=lambda item: item[0])
print(sorted_list_of_tuples)

list_of_numbers = [1, 2, 3, 4]
operated_list = list(map(lambda x: x**2, list_of_numbers))
filtered_list = list(filter(lambda x: x%2 == 0, list_of_numbers))

print(operated_list)
print(filtered_list)

