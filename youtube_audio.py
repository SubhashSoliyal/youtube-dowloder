from pytube import YouTube

# Replace 'YOUTUBE_VIDEO_URL' with the actual URL of the video
youtube_url = 'YOUTUBE_VIDEO_URL'

yt = YouTube(youtube_url)
stream = yt.streams.filter(only_audio=True).order_by('bitrate').desc().first()
stream.download()
