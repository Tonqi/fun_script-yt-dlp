"""
Plan: we extract the URL information, seperate all formats and let the user pick from the list of formats.
We save the user choice into opts['format'] and feed it to the downloader
"""
import yt_dlp
from download_test import URL
# Command to download audio only (the best audio)
opts = {'outtmpl': '%(title)s_%(height)sp.%(ext)s'}
opts['format'] = 'ba' # Best video and audio = bestvideo+bestaudio/best
opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]

test = yt_dlp.YoutubeDL(opts)
test.download(URL)

print("DONE 1")

# Command to download a specific height (e.g 720 -> 720p)
opts2 = {'outtmpl': '%(title)s_%(height)sp.%(ext)s'}
h = 720
opts2['format'] = f'bv*[height<={h}]+ba/b'

test2 = yt_dlp.YoutubeDL(opts2)
test2.download(URL)

print("DONE 2")

# Example for user choosing a specific quality
opts3 = {'outtmpl': '%(title)s_%(height)sp.%(ext)s'}
test3 = yt_dlp.YoutubeDL(opts3)
info = test3.extract_info(URL,download=False)

seen_heights = set()
height_list = []
for f in info.get('formats'):
    vcodec = f.get('vcodec') # none means no video...
    h = f.get('height')
    if vcodec == 'none' or not h or h in seen_heights or h < 144:
        continue # Skip the iteration
    seen_heights.add(h) # Add height to set
    height_list.append(h)
height_list.sort(reverse=True)

video_formats = [f'{h}p' for h in height_list]
all_video_options = ", ".join(video_formats)
print("Choose one of the following qualities: " + all_video_options)

final_choice = ""
while(True):
    choice = input("Your choice: ")
    if(choice not in video_formats):
        print("Please enter a valid choice")
    elif(choice in video_formats):
        print("Downloading video in quality: " + choice)
        final_choice = choice.replace("p", "")
        break

opts4 = {'outtmpl': '%(title)s_%(height)sp.%(ext)s'}
opts4['format'] = f'bv*[height<={final_choice}]+ba/b'
test4 = yt_dlp.YoutubeDL(opts4)
test4.download(URL)

print("DONE 3")


# You can also do a unique id 
# 'outtmpl': '%(id)s_%(height)sp.%(ext)s'
# id = str(uuid.uuid64())
