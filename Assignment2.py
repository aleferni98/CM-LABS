
from scipy.io import wavfile

#loading the audio file
samplerate, data_original = wavfile.read('./clean_piano.wav.wav')

#saving the audio track as an array with all the amplitudes area
data_original = data_original[:, 0]

#listen the original audio track
import IPython.display as ipd 

ipd.Audio(data_original, rate = samplerate)

#I'll take only the first 10 secs
data_original = data_original[: 10 * samplerate]
#listen the 10 secs
ipd.Audio(data_original, rate = samplerate)

import matplotlib.pyplot as plt

#plotting the original signal
plt.plot(data_original)
plt.title('Original Signal')
plt.show()


import numpy as np

'''creating an array full of zeros and ones, the indexes where the value is 1 will be considered as clicks,
we will set the value of the clicks as 1.5 times the maximum value of the original signal
p = 0.0001 means that the probability to find a click in a specific site is 0.0001'''

clicks_position = np.random.binomial(n = 1, p = 0.0001, size = [len(data_original)])

data = data_original.copy()

data[np.where(clicks_position==1)] = max(data_original)*1.5

#plotting the original signal along with the clicks
plt.plot(data_original, label = 'Signal')
plt.plot(clicks_position*max(data_original)*2, label = 'Clicks')
plt.title('Original Signal')
plt.legend()
plt.show()

#------------------FIRST TASK----------------------------------------------------------------
'''we will try to restore the degraded signal using a median filter'''
#all the libraries needed
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from tqdm import tqdm
import statistics
from sklearn.metrics import mean_squared_error as mse

#initialising an array where we will put all the MSE values for different block sizes
result_mse = []
#saving the number of elements in the array data
int_ex = len(data)
'''k stand for how many steps i wanna do to the right and to the left, so choosing k=1 means that from where i am i will see 
the valeu on the left and the one on the right, which accounts for a blocksize of 3'''
lista_k = [1,2,3,4,5]

for k in lista_k:   
#defining the blocksize in this way I also make sure that my blocksize is not going to be an even number
    block_size = 2*k + 1 
#creating an array that will come in handy in the for loop
    sequence = []
#initializing the final result with an array of zeros
    output_list = np.zeros(int_ex)

#copying the first and the last element of the data list into the outpust list
    output_list[0] = data[0]

    output_list[-1] = data[-1]
    #the next loop is for showing on the terminal how long it is taking to the code to do its jobe
    for start in tqdm(range(k, len(data)-k)):

    #copying a sequence of 2*k + 1 elements in sequence
        sequence = np.copy(data[(start - k) : (start + k + 1)])

    #sorting the sequence so i can get the median value
        sequence.sort()

    #now i will substitute the median value in the position 2*N -1 should be the middle of the window
        output_list[start] = sequence[k] 

    # Unit-test to check if my code is correct
        assert statistics.median(sequence) == sequence[k]
    
    #saving the new data order in the list for each block size
    output_list[np.where(clicks_position == 0)] = data[np.where(clicks_position == 0)]
    
    #saving the audio track for each block size
    write('./median_prediction_k='+str(k)+'.wav', samplerate, output_list)
    
    #plotting the restored signal for each block size
    plt.plot(output_list)
    plt.title('Restored Signal through Median Filtering with k='+str(k))
    plt.show()
    
    #computing the MSE for each block size and showing the value on the terminal
    result_mse.append(mse(output_list,data_original))
    print('Error for k='+str(k)+' is equal to '+str(mse(output_list,data_original)))

import matplotlib.pyplot as plt

#plotting the mse for each block_size
plt.plot([2*k+1 for k in lista_k],result_mse, marker = 'o')
plt.ylabel('MSE values for different window size')
plt.show()

#task 1 is now over
print("DONE TASK 1")

#-----------------------SECOND TASK----------------------------------
'''Same goal of task 1, this time we will use a cubic spline interpolation'''

x = np.where(clicks_position==0)

x = x[0]

from patsy import dmatrix
# Generating cubic spline with 3 knots at 10, 100, 10000
transformed_x = dmatrix(
            "bs(train, knots=(10,1000,10000), degree=3, include_intercept=False)", 
                {"train": x},return_type='dataframe')

import statsmodels.api as sm

# Fitting generalised linear model on transformed dataset
cs = sm.GLM(data[x], transformed_x).fit()

# Test data
pred = cs.predict(dmatrix("bs(test, knots=(10,1000,10000), include_intercept=False)", {"test": range(len(data))}, return_type='dataframe'))

pred[x] = data[x]

print('Error for Spline is equal to '+str(mse(pred,data_original)))
plt.plot(pred)
plt.title('Restored Signal through Spline Filtering')
plt.show()

#task 2 is over
print("DONE TASK 2")

#write('./median_prediction.wav', samplerate, output_list)
write('./spline_prediction.wav', samplerate, pred)
write('./data_degraded.wav', samplerate, data)

import IPython.display as ipd 

#listening the degraded audio
samplerate, data = wavfile.read('./data_degraded.wav')

ipd.Audio(data, rate=samplerate)

#listening the audio after median filtering
samplerate, median_pred = wavfile.read('./median_prediction_k=1.wav')

ipd.Audio(median_pred, rate=samplerate)

#listening the audio after cubic spline 
samplerate, spline_pred = wavfile.read('./spline_prediction.wav')

ipd.Audio(spline_pred, rate=samplerate)
