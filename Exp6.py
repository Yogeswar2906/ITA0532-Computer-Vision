# Install OpenCV (if not installed)
!pip install opencv-python

# Import libraries
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Upload image
from google.colab import files
uploaded = files.upload()

# Read the image
image = cv2.imread(list(uploaded.keys())[0])

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create kernel (structuring element)
kernel = np.ones((5,5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(gray, kernel, iterations=1)

# Show original image
print("Original Image:")
cv2_imshow(image)

# Show eroded image
print("Eroded Image:")
cv2_imshow(eroded_image)
