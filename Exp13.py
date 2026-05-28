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

# Get image size
rows, cols = image_rgb.shape[:2]

# Define 3 points in original image
pts1 = np.float32([[50,50], [200,50], [50,200]])

# Define corresponding points after transformation
pts2 = np.float32([[10,100], [200,50], [100,250]])

# Create affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
affine = cv2.warpAffine(image_rgb, matrix, (cols, rows))

# Display side-by-side
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Affine Transformed Image")
plt.imshow(affine)
plt.axis("off")

plt.show()
