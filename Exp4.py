import cv2
from google.colab import files
import matplotlib.pyplot as plt

# Upload image
uploaded = files.upload()
path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(path)

# Convert to grayscale (required)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Display images
plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original Image")

plt.subplot(1,2,2)
plt.imshow(equalized, cmap='gray')
plt.title("Equalized Image")

plt.show()
