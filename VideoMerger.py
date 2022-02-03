from moviepy.editor import VideoFileClip, concatenate_videoclips


class VideoMerger:
    def __init__(self):
        self.videos = []

    def merge_videos(self, counter):
        for i in range(counter):
            self.videos.append(VideoFileClip(f"{i+1}.mp4"))
        final_video = concatenate_videoclips(self.videos)
        final_video.write_videofile("final_video.mp4")
        self.videos = []


if __name__ == "__main__":
    v_g = VideoMerger()
    v_g.merge_videos(4)
