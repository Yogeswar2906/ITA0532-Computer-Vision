# 36. Background Subtraction based on Color Levels using OpenCV

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

# Convert image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define color range for background removal
# (Example: removing green background)

lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])

# Create mask
mask = cv2.inRange(hsv, lower_green, upper_green)

# Invert mask
mask_inv = cv2.bitwise_not(mask)

# Remove background
result = cv2.bitwise_and(img_rgb, img_rgb, mask=mask_inv)

# Display outputs
plt.figure(figsize=(15,5))

# Original Image
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Mask Image
plt.subplot(1,3,2)
plt.imshow(mask, cmap='gray')
plt.title("Background Mask")
plt.axis('off')

# Background Removed Output
plt.subplot(1,3,3)
plt.imshow(result)
plt.title("Background Subtracted Image")
plt.axis('off')

plt.show()

print("Background Subtraction Completed!")
