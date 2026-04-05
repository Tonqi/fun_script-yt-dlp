"""
Information about the yt-dlp downloader
1.The YoutubeDL is responsible for downloading a video, in order to do that it needs a extractor that extracts
all necessary information about a video. If an extractor is used it will extract information and the YoutubeDL object
can start the download 

Extractor (sends it to) -> YoutubeDL object -> downloads the actual video -> save it on users disk if wanted
Finally: The YoutubeDL handles the URL when passed and passes it to the right extractor
"""
import yt_dlp
URL = "https://x.com/terrenoviral/status/2040869857978122574"

# list of possible parameters are found here: https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L183

opts = {
    'noplaylist': True,
    'outtmpl': f"%(title).80s.%(ext)s",
}
downloader = yt_dlp.YoutubeDL(opts)
# downloader.download(URL) Uncomment to test