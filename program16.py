#flatten a list of list (nested list)

list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]

#method:1
def flatten(nested_list):
    flatten_list = []
    for sublist in nested_list:
        for item in sublist:
            flatten_list.append(item)
    return flatten_list

flatten(list_of_lists)

#method:2 
flatten_list = [item for sublist in list_of_lists for item in sublist]
print(flatten_list)
