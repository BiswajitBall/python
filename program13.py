#use of np.diff for two dimensional matrix along different axis  
import numpy as np

seed_value = 1
np.random.seed(seed_value)


random_matrix = np.random.randint(1, 10, size=(3,3))


print(random_matrix)

#diff all
diff_all = np.diff(random_matrix)
print(diff_all)

#diff along axis=0
diff_axis_0 = np.diff(random_matrix, axis=0)
print(diff_axis_0)

#diff along axis=1
diff_axis_1 = np.diff(random_matrix, axis=1)
print(diff_axis_1)
