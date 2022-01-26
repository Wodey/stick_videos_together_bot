from pytube import YouTube, Playlist


class Video_Downloader:
    def __init__(self):
        self.counter = 0

    def download_playlist(self, url):
        pl = Playlist(url)
        for url in pl.video_urls:
            self.download_video(url)

    def download_video(self, url):
        yt = YouTube(url)
        self.counter += 1
        print("Have started video downloading...")
        print(f"It is a video №{self.counter}")
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
            filename=f"{self.counter}.mp4")
        print("Finished video downloading.")


if __name__ == "__main__":
    v_c = Video_Downloader()
    v_c.download_playlist("https://www.youtube.com/playlist?list=PLN2WeTFVM_p5x79B6n2-09BQYNPP4WdZq")
