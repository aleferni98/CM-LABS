import numpy as np

from scipy.ndimage import median_filter
# generate some integers
int_ex = 15
#initializing an array
data_list = []

np.random.seed(1)
#creating a random list of integers of 15 units with values from 0 to 15
data_list = np.random.randint(int_ex, size=int_ex)

print("data_list")

print(data_list)

#k stand for how many steps i wanna do to the right and to the left, so choosing k=1 means that from where i am i will see 
#the valeu on the left and the one on the right, which accounts for a blocksize of 3
k = 1

#defining the blocksize in this way I also make sure that my blocksize is not going to be an even number
block_size = 2*k + 1 
#creating an array that will come in handy in the for loop
sequence = []
#initializing the final result with an array of zeros
output_list = np.zeros(int_ex)

#copying the first and the last element of the data list into the outpust list
output_list[0] = data_list[0]

output_list[-1] = data_list[-1]

for start in range(k, len(data_list)-k):
    # repeating the seed function so the values are the same as shown before
    np.random.seed(1)
    #copying a sequence of 2*k + 1 elements in sequence
    sequence = np.copy(data_list[(start - k) : (start + k + 1)])
    #sorting the sequence so i can get the median value
    sequence.sort()
    #now i will substitute the median value in the position 2*N -1 should be the middle of the window
    output_list[start] = sequence[2*k -1] 

print('Final median filter')

print(output_list)

#now I will check my results using a premade function for computing the median filter
check_list = []

check_list = median_filter(data_list, size=3, cval=0, mode='constant')

print("check_list")

print(check_list)

print("if outpust_list is matching check_list then the code should return True, otherwise False")

print("Final result:") 

print(np.array_equal(output_list,check_list))




