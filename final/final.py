from audio2numpy import open_audio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

## 2 Flauti

# Read file
song = "flauti.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 2 Oboi

# Read file
song = "oboi.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 2 Clarinetti

# Read file
song = "clarinetti.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 2 Fagotti

# Read file
song = "fagotti.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 1 Corni

# Read file
song = "corni.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 2 Trombe

# Read file
song = "trombe.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 2 Tromboni

# Read file
song = "tromboni.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 1 Tuba

# Read file
song = "tuba.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 1 Timpani

# Read file
song = "timpani.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 1 Arpa

# Read file
song = "arpa.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 4 Violine I

# Read file
song = "violine.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 4 Violine II

# Read file
song = "violine2.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 2 Viola

# Read file
song = "viola.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 2 Violoncelle

# Read file
song = "violoncelle.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)

## 2 Contrabasse

# Read file
song = "contrabasse.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

my_array = my_array/max(my_array)