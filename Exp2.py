# Install OpenCV (run once)
!pip install opencv-python

import cv2
from google.colab import files
from matplotlib import pyplot as plt

# Step 1: Upload image
uploaded = files.upload()

# Step 2: Get file name
image_path = next(iter(uploaded))

# Step 3: Read image
img = cv2.imread(image_path)

# Convert BGR to RGB (for correct display)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 4: Apply Gaussian Blur
# (5,5) is kernel size, 0 means auto sigma
blur_img = cv2.GaussianBlur(img_rgb, (5,5), 0)

# Step 5: Display images
plt.figure(figsize=(10,5))

# Original Image
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Blurred Image
plt.subplot(1,2,2)
plt.imshow(blur_img)
plt.title("Gaussian Blurred Image")
plt.axis('off')

plt.show()
