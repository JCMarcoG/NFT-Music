import moviepy.editor as mp

# Adding audio
video =  mp.VideoFileClip("animation.mp4")
video_with_new_audio = video.set_audio(mp.AudioFileClip("swan_lake.mp3")) 
video_with_new_audio.write_videofile("output.mp4",  codec="mpeg4")