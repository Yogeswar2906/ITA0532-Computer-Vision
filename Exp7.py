from google.colab import files
import cv2
from google.colab.patches import cv2_imshow
import time

# Upload video
uploaded = files.upload()
video_path = list(uploaded.keys())[0]

def play_video(video_path, speed=1.0):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 30

    delay = 1 / (fps * speed)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2_imshow(frame)
        time.sleep(delay)

    cap.release()

# Normal speed
print("Normal Video")
play_video(video_path, speed=1.0)

# Slow motion
print("Slow Motion Video")
play_video(video_path, speed=0.5)

# Fast motion
print("Fast Motion Video")
play_video(video_path, speed=2.0)
