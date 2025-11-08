import numpy as np

scores_array = np.array([10,0,30,40,50,60,70,80,0,100])
print(scores_array)
sliced_array=scores_array[2:5]
print(sliced_array)
print(scores_array[:4])
print(scores_array[5:])
print(scores_array[:1])
print(scores_array[::2])
print(scores_array[::3])
print(scores_array[-3:])