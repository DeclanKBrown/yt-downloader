from pytube import YouTube

url = ''
video = YouTube(url)

print(video.streams.filter(file_extension='mp4'))

stream = video.streams.get_by_itag()
# stream.download('/Users/macbook/Downloads/')