import numpy as np

# Boolean Indexing
names = np.array(['Seong Hoon', 'Han Eun', 'Hyun Soo'])
info = np.array(['height', 'weight', 'gender', 'address', 'age'])

data = np.random.randn(5,3)

print(data)
print((names == 'Han Eun') | (names == 'Hyun Soo'))
print(info == 'weight')
print(data[info=='height', names=='Seong Hoon'])

arr = np.arange(32).reshape(8, 4)
arr_slice = arr[[1,2,3]][:, [1,2,3]]
print(arr)
print(arr_slice)
