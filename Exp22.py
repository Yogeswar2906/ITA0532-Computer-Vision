# 22. Implement Closing Morphological Operation using OpenCV

# Import libraries
import cv2
import numpy as np
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

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply Closing operation
# Closing = Dilation followed by Erosion
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Display results
plt.figure(figsize=(15,5))

# Original Image
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Grayscale Image
plt.subplot(1,3,2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

# Closing Output
plt.subplot(1,3,3)
plt.imshow(closing, cmap='gray')
plt.title("Closing Operation")
plt.axis('off')

plt.show()
