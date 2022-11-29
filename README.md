# Click removal in degraded audio through cubic spline

## Description of the project
The goal of this project is to reconstruct a degraded audio signal through two different interpolation methods on Python. The methods we will take into consideration will be:
- median filtering
- cubic splines

---

## Installation and Execution

Below, the libraries used during the procedure are listed with their corresponding versions together with the version Python:
```sh                                 
ipython==8.7.0
matplotlib==3.6.2
numpy==1.23.5
pandas==1.5.2
patsy==0.5.3
scikit_learn==1.1.3
scipy==1.9.3
statsmodels==0.13.5
tqdm==4.64.1
```



Afer installing all required packages you can run the demo file simply by typing:
```sh
python Assignment2.py
```
---

## Methodology and Results

First of all, let's take into consideration a clean audio track and add clicks manually, through a random function that will establish in which position of the signal to place the clicks. The samples where the clicks are located will take on double the value of the maximum amplitude value recorded in the original signal.
The difference between the original and degraded signal is that in the latter one should perceive a background noise not present in the original.
In the following image you can see the original signal with the position of the clicks superimposed:


<img src="new_clicks.png" width=350>

Once the degraded signal has been obtained, we can go and test our two interpolation methods to see if they are able to reconstruct the signal as faithfully as possible to the original.




**Results**

1. For the median filter, different block size lengths were explored to test the effectiveness of the restoration, with values ranging from a few units up to thousands. Then we calculated the mean squared error for each of the block sizes. As shown in the figure below, it can be seen that the value of the MSE, for small values of block size, is around 4. By increasing the size of the blocks up to 100, the error grows dramatically compared to before, assuming values around 800. However, continuing to increase the block size, the error would seem to converge around 1000.

<img src="comparisons.png" width="350">

The restored waveform <median_prediction_k=1.wav> with the optimal filter length is given below:

<img src="filterk=1.png" widht="350">


2. Using the cubic splines, we observe that the MSE is much higher compared to the median filter, it assumes a value of about 929.

The restored waveform <spline_prediction.wav> using the cubic spline method is given below:

<img src="new_spline.png" widht=350>


3. Comparing the two different interpolation methods, we note that, focusing on the MSE values, the median filter would seem to perform better than the cubic spline. 


 The runtime of the median filter method is is about 2 seconds up to block sizes of no more than 100, while for values greater than 1000 it takes even more than a minute.
 As for the spline, it takes roughly 2 seconds to get the results. Ergo we could conclude by saying that the cubic spline method is on average faster than the median filter.



Contrary to what might be expected from the results shown above, both methods result in an audio track that is not faithful to the original signal before being degraded. While expectations were already low for the cubic spline due to the high MSE value, the median filter also disappoints as a result. Both methods output an audio signal that is very electronic and still very dirty. Although listening is very unpleasant, you can still distinguish the tones of the original audio.


---
## Credits

This code was developed for purely academic purposes by Alessandro Ferni (github profile: aleferni98) as part of the module "Computational Methods" at Trinity College Dublin.







