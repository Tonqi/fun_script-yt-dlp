from downloader.download import run_download
import sys

if __name__ == "__main__":
    # Check if a URL was actually provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        run_download(url)