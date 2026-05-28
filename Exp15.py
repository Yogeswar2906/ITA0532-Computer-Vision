# Install OpenCV
!pip install opencv-python

import cv2
import numpy as np
from google.colab import files
import matplotlib.pyplot as plt

# Upload image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# Read image
image = cv2.imread(image_path)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to float32 (required for Harris)
gray = np.float32(gray)

# Apply Harris Corner Detection
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate result for marking corners
dst = cv2.dilate(dst, None)

# Mark corners in red
image_rgb[dst > 0.01 * dst.max()] = [255, 0, 0]

# Display side-by-side
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Harris Corners Detected")
plt.imshow(image_rgb)
plt.axis("off")

plt.show()
