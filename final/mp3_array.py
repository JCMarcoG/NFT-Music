from audio2numpy import open_audio
import numpy as np
import matplotlib.pyplot as plt

# Read file
song = "tromboni.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

print(sampling_rate)
print(len(samples))
print(len(my_array))
print(max(my_array))

plt.plot(my_array)
plt.show()