# 29. Eye Detection using OpenCV

# Import libraries
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload image
uploaded = files.upload()

# Get image name
image_path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(image_path)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load face cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Load eye cascade
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

# Create output copy
output = img_rgb.copy()

# Detect eyes inside faces
for (x, y, w, h) in faces:

    # Draw face rectangle
    cv2.rectangle(output, (x, y), (x+w, y+h), (0,255,0), 2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = output[y:y+h, x:x+w]

    # Detect eyes
    eyes = eye_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=10
    )

    # Draw eye rectangles
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(
            roi_color,
            (ex, ey),
            (ex+ew, ey+eh),
            (255,0,0),
            2
        )

# Display images
plt.figure(figsize=(12,6))

# Original image
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Eye detection output
plt.subplot(1,2,2)
plt.imshow(output)
plt.title("Eye Detection Output")
plt.axis('off')

plt.show()
