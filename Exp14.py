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

# Define 4 points in original image
pts1 = np.float32([[50,50], [cols-50,50], [50,rows-50], [cols-50,rows-50]])

# Define corresponding points after transformation
pts2 = np.float32([[0,0], [cols,0], [100,rows], [cols-100,rows]])

# Get perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
perspective = cv2.warpPerspective(image_rgb, matrix, (cols, rows))

# Display side-by-side
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Perspective Transformed Image")
plt.imshow(perspective)
plt.axis("off")

plt.show()
