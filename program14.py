#use of max/min for two dimensional matrix along different axis  
import numpy as np

seed_value = 1
np.random.seed(seed_value)


random_matrix = np.random.randint(1, 10, size=(3,3))


print(random_matrix)

#max all
max_all = np.max(random_matrix)
print(max_all)

#max along axis=0
max_axis_0 = np.max(random_matrix, axis=0)
print(max_axis_0)

#max along axis=1
max_axis_1 = np.max(random_matrix, axis=1)
print(max_axis_1)
