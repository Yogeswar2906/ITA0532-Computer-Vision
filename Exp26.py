# 26. Reverse Video using OpenCV

# Import libraries
import cv2
import imageio
from google.colab import files
from IPython.display import HTML
from base64 import b64encode

# Upload video
uploaded = files.upload()

# Get video name
video_path = list(uploaded.keys())[0]

# Read video
cap = cv2.VideoCapture(video_path)

frames = []

# Read all frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frames.append(frame)

cap.release()

# Reverse frames
frames = frames[::-1]

# Save reversed video
output_path = "reverse_video.mp4"

imageio.mimsave(output_path, frames, fps=20)

print("Reverse video created successfully!")

# Display video properly in Colab
mp4 = open(output_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()

HTML(f"""
<video width=600 controls>
      <source src="{data_url}" type="video/mp4">
</video>
""")
