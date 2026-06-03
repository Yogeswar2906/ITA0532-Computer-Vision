# 38. Count Number of Faces using OpenCV

# Import libraries
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload image
uploaded = files.upload()

# Get uploaded image name
image_path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(image_path)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(60, 60)
)

# Create output image
output = img_rgb.copy()

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(
        output,
        (x, y),
        (x+w, y+h),
        (0, 255, 0),
        3
    )

# Display images
plt.figure(figsize=(12,6))

# Original Image
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Face Count Output
plt.subplot(1,2,2)
plt.imshow(output)
plt.title("Detected Faces")
plt.axis('off')

plt.show()

# Print total faces
print("Number of Faces Detected:", len(faces))
