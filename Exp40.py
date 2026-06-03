# 40. Extract Text from Video using OpenCV and OCR

# Install Tesseract OCR
!apt-get install tesseract-ocr -y > /dev/null
!pip install pytesseract > /dev/null

# Import libraries
import cv2
import pytesseract
import matplotlib.pyplot as plt
from google.colab import files

# Upload video
uploaded = files.upload()

# Get uploaded video name
video_path = list(uploaded.keys())[0]

# Read video
cap = cv2.VideoCapture(video_path)

frame_count = 0
all_text = ""

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

    # Process every 30th frame
    if frame_count % 30 == 0:

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Extract text using OCR
        text = pytesseract.image_to_string(gray)

        # Store extracted text
        all_text += text + "\n"

        # Display sample frame
        plt.figure(figsize=(8,4))
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.title(f"Frame {frame_count}")
        plt.axis('off')
        plt.show()

cap.release()

# Print extracted text
print("Extracted Text from Video:\n")
print(all_text)
