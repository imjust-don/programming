from pytube import YouTube
import requests

def Download(link):
    youtubeObject = YouTube(link)
    download = youtubeObject.streams.get_highest_resolution()
    video_id = link.split("=")[-1]
    watch_page_url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(watch_page_url)
    cookies = response.cookies
    yt = YouTube(link, cookies=cookies)
    title = yt.title
    channel = yt.author
    stream = download.stream.first()
    try:
        stream.download()
    except:
        print("An error has occurred")
    print(f"Succesfully Downloaded: ---> {title.upper()} by the channel {channel.upper()}")


link = input("Enter the YouTube video URL: ")
Download(link)