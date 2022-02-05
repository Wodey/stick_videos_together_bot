from VideoMerger import VideoMerger
from VideoUploader import VideoUploader
from VideoDownloader import VideoDownloader

video_downloader = VideoDownloader()

uri = input("Send link on playlist or video: ")

if "playlist" in uri:
    video_downloader.download_playlist(uri)
else:
    video_downloader.download_video(uri)

video_merger = VideoMerger()

video_merger.merge_videos(video_downloader.counter)



