from pytube import YouTube


video_id = '6APYhpbjKXY'   #'VIDEO_ID'
youtube_url = f'https://www.youtube.com/watch?v={video_id}'
video = YouTube(youtube_url)
video.streams.get_highest_resolution().download()
