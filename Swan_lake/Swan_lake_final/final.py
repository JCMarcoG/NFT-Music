from audio2numpy import open_audio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import moviepy.editor as mp

def instrument2numpy(song, n):

    #Song to numpy
    signal, sampling_rate = open_audio(song)

    #Convert stereo to mono
    samples = signal.sum(axis=1) / 2

    #Get as many samples as frames
    my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])

    my_array = my_array/max(my_array)

    print(song + " completed")

    my_arrays = np.tile(my_array, (n, 1))

    return my_arrays

instruments = [("violine.mp3", 4), ("arpa.mp3", 1), ("viola.mp3", 3), ("contrabasse.mp3", 2), ("oboi.mp3", 2), 
               ("timpani.mp3", 1), ("tuba.mp3", 1), ("tromboni.mp3", 2), ("flauti.mp3", 2),
               ("clarinetti.mp3", 2),("fagotti.mp3", 2), ("corni.mp3", 1), ("violoncelle.mp3", 3),
               ("violine2.mp3", 4)]

# invert order of instrument (left side of a orchestra will be on top)
instruments = instruments[::-1]

# Blank vector
data = np.array([]).reshape(0, 2491)

for instrument in instruments:
    data = np.append(data, instrument2numpy(*instrument), axis = 0)

# Include this so the part playing will be centered
zer_left = np.zeros((30, 85))
zer_right = np.zeros((30, 73))
data = np.append(zer_left, data, axis = 1)
data = np.append(data, zer_right, axis = 1)

X = np.linspace(-1, 1, 150)
G = 1.5 * np.exp(-10 * X ** 2)

# Create new Figure with black background
fig = plt.figure(figsize=(9, 16), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)

# Generate line plots
lines = []
for i in range(len(data)):
    # Small reduction of the X extents to get a cheap perspective effect
    xscale = 1 - i / 200.
    # Same for linewidth (thicker strokes on bottom)
    lw = 1.5 - i / 100.0
    line, = ax.plot(xscale * X, (i+7) + G * data[i][0:150], color="w", lw=lw)
    lines.append(line)

# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 60)

# No ticks
ax.set_xticks([])
ax.set_yticks([])

# 2 part titles to get different font weights
ax.text(0.5, 0.95, "TCHAIKOVSKY", transform=ax.transAxes,
        ha="center", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=32)
ax.text(0.5, 0.85, "Swan Lake Op. 20 Act II No 10", transform=ax.transAxes,
        ha="center", va="bottom", color="w",
        family="sans-serif", fontweight="bold", fontsize=26)

def update(*args):
    try:
        y
    except:
        y = 0

    global data

    # Shift all data to the left
    data = np.roll(data, -1, 1)

    # Update data
    for i in range(len(data)):
        lines[i].set_ydata((i+7) + G * data[i][y:y + 150] * 4)

    y += 1

    # Return modified artists
    return lines

# Construct the animation, using the update function as the animation director.
anim = animation.FuncAnimation(fig, update, frames=2491, interval=1)
# plt.show()

# Save the animation
Writer = animation.writers["ffmpeg"]
writer = Writer(fps = 30, metadata={"autor": "JC_Marco"}, bitrate=1000)
anim.save("animation.mp4", writer)

# Adding audio
video =  mp.VideoFileClip("animation.mp4")
video_with_new_audio = video.set_audio(mp.AudioFileClip("swan_lake.mp3")) 
video_with_new_audio.write_videofile("TCHAIKOVSKY-swan_lake.mp4",  codec="mpeg4")