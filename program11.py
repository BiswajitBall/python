#sum of a four dimensional numpy array along different axis 
import numpy as np

seed_value = 1
np.random.seed(seed_value)

#random_matrix = np.random.rand(3,2,2,2)
random_matrix = np.random.randint(1, 10, size=(3,2,2,2))
#random_matrix = np.random.normal(loc=10, scale=3, size=(3,2,2,2))

print(random_matrix)

#sum all
sum_all = np.sum(random_matrix)
print(sum_all)

#sum along axis=0
sum_axis_0 = np.sum(random_matrix, axis=0)
print(sum_axis_0)

#sum along axis=1
sum_axis_1 = np.sum(random_matrix, axis=1)
print(sum_axis_1)

#sum along axis=2
sum_axis_2 = np.sum(random_matrix, axis=2)
print(sum_axis_2)

#sum along axis=3
sum_axis_3 = np.sum(random_matrix, axis=3)
print(sum_axis_3)

#sum along axis=(1,2)
sum_axis_12 = np.sum(random_matrix, axis=(1,2))
print(sum_axis_12)
