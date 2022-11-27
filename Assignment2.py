#caricare file audio wav e trasformare audio in array dati, la funzione qui sotto dovrebbe funzionare
from scipy.io import wavfile
samplerate, data = wavfile.read('"C:\Users\alepf\OneDrive\Documenti\Python Scripts\source_squabb.wav"')
# Ci sono due array in data
data = data[:,1]
#------------------FIRST TASK----------------------------------------------------------------
import pandas as pd
import numpy as np


mean_data = np.mean(data) #data è array del segnale
mean_diff = np.mean(data - mean_data)
threshold = mean_data + mean_diff
#avendo impostato una soglia, si possono identificare i click in sto modo

#clicks_position = np.where(data > threshold)
clicks_position = np.where(abs(data) > abs(threshold))

from tqdm import tqdm
import statistics
#k stand for how many steps i wanna do to the right and to the left, so choosing k=1 means that from where i am i will see 
#the valeu on the left and the one on the right, which accounts for a blocksize of 3
k = 1
int_ex = len(data)
#defining the blocksize in this way I also make sure that my blocksize is not going to be an even number
block_size = 2*k + 1 
#creating an array that will come in handy in the for loop
sequence = []
#initializing the final result with an array of zeros
output_list = np.zeros(int_ex)

#copying the first and the last element of the data list into the outpust list
output_list[0] = data[0]

output_list[-1] = data[-1]

for start in tqdm(range(k, len(data)-k)):
    # repeating the seed function so the values are the same as shown before
    np.random.seed(1)
    #copying a sequence of 2*k + 1 elements in sequence
    sequence = np.copy(data[(start - k) : (start + k + 1)])
    #sorting the sequence so i can get the median value
    sequence.sort()
    #now i will substitute the median value in the position 2*N -1 should be the middle of the window
    output_list[start] = sequence[2*k -1] 
    # Unit-test per vedere se il metodo calcola correttamente la mediana
    assert statistics.median(sequence) == sequence[2*k-1]


# Calcolo errore solo sui click
output_list[clicks_position] = data[clicks_position]

from sklearn.metrics import mean_squared_error as mse

print('Error')
print(mse(output_list,data))
#STAMPARE DONE QUANDO IL CODICE HA TERMINATO Di FARE LE SUE ROBE

print("DONE TASK 1")