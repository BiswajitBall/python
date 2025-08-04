#Dictionaries in python

my_dict = {'apple': 3, 'orange': 1, 'banana': 2}
my_dict['grapes']=9   #add item to dictionary 
my_dict['mango']=20  
#my_dict.pop('apple')  
del my_dict['apple']  #remove item from dictionary

for key, value in my_dict.items():   #looping through a dictionary
    print(key,':', value)

my_dict_sorted_by_key=dict(sorted(my_dict.items(), key=lambda item: item[0]))  #sort the dictionary by key 
my_dict_sorted_by_value=dict(sorted(my_dict.items(), key=lambda item: item[1]))  #sort the dictionary by value 

print(my_dict_sorted_by_value)

my_dict_filtered = {key:value for key, value in my_dict.items() if my_dict['mango'] == 20}

print(my_dict_filtered)
