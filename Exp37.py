# 37. Foreground Subtraction based on Color Levels using OpenCV

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

# Define color range for foreground removal
# (Example: removing red foreground object)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Create masks
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Combine masks
mask = mask1 + mask2

# Invert mask
mask_inv = cv2.bitwise_not(mask)

# Remove foreground
result = cv2.bitwise_and(img_rgb, img_rgb, mask=mask_inv)

# Display outputs
plt.figure(figsize=(15,5))

# Original Image
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Foreground Mask
plt.subplot(1,3,2)
plt.imshow(mask, cmap='gray')
plt.title("Foreground Mask")
plt.axis('off')

# Foreground Removed Output
plt.subplot(1,3,3)
plt.imshow(result)
plt.title("Foreground Subtracted Image")
plt.axis('off')

plt.show()

print("Foreground Subtraction Completed!")
