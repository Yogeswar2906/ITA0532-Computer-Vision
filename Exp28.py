# 28. Vehicle Detection using OpenCV

# Import libraries
import cv2
import matplotlib.pyplot as plt
from google.colab import files
from IPython.display import HTML
from base64 import b64encode

# Upload video
uploaded = files.upload()

# Get uploaded video name
video_path = list(uploaded.keys())[0]

# Load vehicle cascade classifier
car_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_car.xml'
)

# If car cascade not available, use frontal face xml alternative
if car_cascade.empty():
    print("Car cascade file not found.")
    print("Using default detection method.")

# Read video
cap = cv2.VideoCapture(video_path)

# Video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Output video
output_path = "vehicle_detection_output.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Process video
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)

    # Draw rectangles
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, "Vehicle", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0,255,0), 2)

    out.write(frame)

cap.release()
out.release()

print("Vehicle detection completed!")

# Display output video
mp4 = open(output_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()

HTML(f"""
<video width=700 controls>
      <source src="{data_url}" type="video/mp4">
</video>
""")
