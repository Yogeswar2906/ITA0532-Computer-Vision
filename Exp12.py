# Install OpenCV
!pip install opencv-python

import cv2
from google.colab import files
import matplotlib.pyplot as plt

# Upload image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# Read image
image = cv2.imread(image_path)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Rotate 270° clockwise (same as 90° anticlockwise)
rotated = cv2.rotate(image_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display side-by-side
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Rotated Image (270° CW)")
plt.imshow(rotated)
plt.axis("off")

plt.show()
