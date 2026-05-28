# 18. Image Cropping, Copying and Pasting using OpenCV

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

# Create copy of image
output = img_rgb.copy()

# -----------------------------
# Select ROI (Region of Interest)
# Format: [y1:y2 , x1:x2]
# -----------------------------
roi = output[100:300, 100:300]

# Crop ROI
cropped_roi = roi.copy()

# Paste ROI to another location
output[320:520, 350:550] = cropped_roi

# -----------------------------
# Display Results
# -----------------------------
plt.figure(figsize=(15,5))

# Original Image
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Cropped ROI
plt.subplot(1,3,2)
plt.imshow(cropped_roi)
plt.title("Cropped ROI")
plt.axis('off')

# Pasted Output
plt.subplot(1,3,3)
plt.imshow(output)
plt.title("Copied and Pasted ROI")
plt.axis('off')

plt.show()
