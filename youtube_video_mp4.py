from pytube import YouTube

# Replace 'YOUTUBE_VIDEO_URL' with the actual URL of the video
youtube_url = 'https://www.youtube.com/watch?v=48kyJDur3m'

yt = YouTube(youtube_url)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream.download()
