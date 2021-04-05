import numpy as np 

narray1 = np.arange(1,10) # 1-dim vector
narray2 = np.arange(11,20) # 1-dim vector

narray3 = np.array([narray1, narray2]) # 2-dim vector = matrix
narray4 = np.array([narray3, narray3]) # 3-dim vector = tensor

print(narray4[1][0][4]) # 1st matrix, 0th row, 4th column
print(narray4[1,0,4]) # Same but less verbose

# Elementwise Calculation
narr1 = narray1 + narray2
print(narr1)
narr1 = narray1 - narray2
print(narr1)
narr1 = narray1 * narray2
print(narr1)
narr1 = narray1 / narray2
print(narr1)
