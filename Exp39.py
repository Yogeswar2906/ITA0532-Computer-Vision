# 39. Reverse Video in Slow Motion using OpenCV

# Import libraries
import cv2
import imageio
from google.colab import files
from IPython.display import HTML
from base64 import b64encode

# Upload video
uploaded = files.upload()

# Get uploaded video name
video_path = list(uploaded.keys())[0]

# Read video
cap = cv2.VideoCapture(video_path)

frames = []

# Read all frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    frame = cv2.resize(frame, (640, 360))

    # Convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frames.append(frame)

cap.release()

# Reverse frames
frames = frames[::-1]

# Create slow motion effect
# Duplicate each frame 2 times
slow_frames = []

for frame in frames:
    slow_frames.append(frame)
    slow_frames.append(frame)

# Save output video
output_path = "reverse_slow_motion.mp4"

# Lower fps for slow motion
imageio.mimsave(output_path, slow_frames, fps=10)

print("Reverse Slow Motion Video Created Successfully!")

# Display video
mp4 = open(output_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()

HTML(f"""
<video width=700 controls>
      <source src="{data_url}" type="video/mp4">
</video>
""")
