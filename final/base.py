from audio2numpy import open_audio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Read file
song = "swan_lake.mp3" 

#Song to numpy
signal, sampling_rate = open_audio(song)

#Convert stereo to mono
samples = signal.sum(axis=1) / 2

#Get as many samples as frames
my_array = np.take(samples, [i for i in range(len(samples)) if i%1470 == 0])


# Create matrix of data
data = np.tile(np.absolute(my_array), (50, 1))
X = np.linspace(-1, 1, 150)
G = 1.5 * np.exp(-4 * X ** 2)

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
    line, = ax.plot(xscale * X, i + G * data[i][0:150], color="w", lw=lw)
    lines.append(line)

# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 60)

# No ticks
ax.set_xticks([])
ax.set_yticks([])

# 2 part titles to get different font weights
ax.text(0.5, 1, "TCHAIKOVSKY ", transform=ax.transAxes,
        ha="center", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=32)
ax.text(0.5, 0.9, "Swan Lake Op. 20 Act II No 10", transform=ax.transAxes,
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
        lines[i].set_ydata(i + G * data[i][y:y + 150] * 7)

    y += 1

    # Return modified artists
    return lines

# Construct the animation, using the update function as the animation director.
anim = animation.FuncAnimation(fig, update, frames=2491, interval=1)
# plt.show()

# Save the animation
Writer = animation.writers["ffmpeg"]
writer = Writer(fps = 30, metadata={"autor": "JC_Marco"}, bitrate=1000)
anim.save("animation4.mp4", writer)