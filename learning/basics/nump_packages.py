import numpy as np

height = np.array([1.65, 1.6, 2.1, 1.4, 3.2])
weight = np.array([133, 163, 132, 84, 97])
bmi = weight / height ** 2
print(bmi)

over_weight = bmi[bmi > 22]
print(over_weight)