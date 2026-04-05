"""
The extractor extracts information of a video -> YoutubeDL.extract_info()
The options passed to the YoutubeDL object are the information the extractor extracts 
We put them into a dictionairy with the parameter name (refer to docs) and pass it to the YoutubeDL object
"""

import yt_dlp,json
from download_test import URL

opts = {
    'noplaylist' : True
}
downloader = yt_dlp.YoutubeDL(opts)
info = downloader.extract_info(URL, download=False)
print(json.dumps(info, indent=3))
