import imageio
from moviepy.editor import VideoFileClip
import os

video_dir = 'videos'
thumbnail_dir = 'images/video_thumbnails'

for v_name in os.listdir(video_dir):
    if not v_name.endswith('mp4'):
        print('error', v_name)
        continue
    clip = VideoFileClip(os.path.join(video_dir, v_name))
    frame = clip.get_frame(0)
    imageio.imwrite(os.path.join(thumbnail_dir, v_name.replace('mp4', 'jpg')), frame)