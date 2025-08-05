#use of np.cumsum along different axis  
import numpy as np

seed_value = 1
np.random.seed(seed_value)


random_matrix = np.random.randint(1, 10, size=(3,3))


print(random_matrix)

#sum all
sum_all = np.cumsum(random_matrix)
print(sum_all)

#sum along axis=0
sum_axis_0 = np.cumsum(random_matrix, axis=0)
print(sum_axis_0)

#sum along axis=1
sum_axis_1 = np.cumsum(random_matrix, axis=1)
print(sum_axis_1)
