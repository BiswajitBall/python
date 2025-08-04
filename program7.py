#nested dictionaries in python

person1_data = {"name": "Alice", "age": 30, "city": "New York"}
person2_data = {"name": "Pravat", "age": 20, "city": "Purulia"}
person3_data = {"name": "Nayan", "age": 25, "city": "Kolkata"}
person4_data = {"name": "Amal", "age": 40, "city": "Varanasi"}
person5_data = {"name": "Mayur", "age": 22, "city": "Chennai"}

my_dict={'person1': person1_data, 'person2': person2_data, 'person3': person3_data, 'person4': person4_data, 'person5': person5_data}

print(my_dict)

for key, value in my_dict.items():
    print(f'{key}:{value}')

my_dict_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]['age'])) #sort my_dict by age
print(my_dict_sorted)

my_dict_filtered = {key:value for key, value in my_dict.items() if (value['age'] > 20)} #filter by person age

print(my_dict_filtered)
