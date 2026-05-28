# Install OpenCV
!pip install opencv-python

# Import libraries
import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload image
uploaded = files.upload()

# Read image
image_path = list(uploaded.keys())[0]
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create kernel (structuring element)
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(gray, kernel, iterations=1)

# Show original image
print("Original Image:")
cv2_imshow(image)

# Show dilated image
print("Dilated Image:")
cv2_imshow(dilated_image)
