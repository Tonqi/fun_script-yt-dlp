import yt_dlp

URL = "https://x.com/terrenoviral/status/2040869857978122574"

output_template = "downloads/%(title)s_%(height)sp.%(ext)s"

def info_extraction(url: str) -> list[str]:
    # List out every available format
    opts = {}
    test = yt_dlp.YoutubeDL(opts)
    info = test.extract_info(url,download=False)

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

    audio_only = 'audio'
    video_formats = [f'{h}p' for h in height_list]
    video_formats.append(audio_only)
    all_video_options = ", ".join(video_formats)
    
    return all_video_options

def run_download(url: str):
    all_video_options = info_extraction(url)
    print("Choose: " + all_video_options)
    final_choice = ""
    while(True):
        choice = input("Your choice: ")
        if(choice not in all_video_options):
            print("Please enter a valid choice")
        elif(choice == 'audio'):
            print("Downloading audio...")
            final_choice = 'audio'
            break
        elif(choice in all_video_options and choice != 'audio'):
            print("Downloading video in quality: " + choice)
            final_choice = choice.replace("p", "")
            break
    
    opts = {'outtmpl': output_template, 'noplaylist': True, 'no_warnings': True, 'quiet': True}
    if(final_choice == 'audio'):
        opts['format'] = 'ba' # Best video and audio = bestvideo+bestaudio/best
        opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
    else:
        opts['format'] = f'bv*[height<={final_choice}]+ba/b'
    try:
        downloader = yt_dlp.YoutubeDL(opts)
        downloader.download(url)
        print("Download done, file should be here in /downloads.")
    except yt_dlp.utils.DownloadError as e:
        print(f"Error: The URL '{url}' is invalid or could not be processed.")
        print(f"System message: {e}")
    except Exception as e:
        print(f"An unexpected error has occured: {e}")


