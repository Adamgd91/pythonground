import numpy as np

height = np.array([1.65,3,5,7,9])
weight = np.array([33, 43, 32, 34, 67])
bmi = weight / height ** 2
print(bmi)