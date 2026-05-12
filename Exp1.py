# Import required libraries
import cv2
from google.colab import files
from matplotlib import pyplot as plt
import numpy as np

# Step 1: Upload image
uploaded = files.upload()

# Step 2: Read the uploaded image
image_path = list(uploaded.keys())[0]
img = cv2.imread(image_path)

# Convert BGR (OpenCV) to RGB for correct display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 3: Convert to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4: Display images
plt.figure(figsize=(10,5))

# Original Image
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Grayscale Image
plt.subplot(1,2,2)
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

plt.show()
