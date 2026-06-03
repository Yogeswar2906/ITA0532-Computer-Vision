# 31. Image Segmentation using Thresholding in OpenCV

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

# Apply threshold segmentation
# Threshold value = 127
# Pixel > 127 -> White
# Pixel <= 127 -> Black

_, segmented = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

# Display outputs
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

# Segmented Image
plt.subplot(1,3,3)
plt.imshow(segmented, cmap='gray')
plt.title("Segmented Image")
plt.axis('off')

plt.show()

print("Image Segmentation Completed!")
