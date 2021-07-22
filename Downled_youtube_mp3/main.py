from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format':'bestaudio'})

youtube_list = [
    "https://www.youtube.com/watch?v=IdpKqrGUGaM&t=8s"]

for each_link in youtube_list:
    audio_downloader.extract_info(each_link)


    