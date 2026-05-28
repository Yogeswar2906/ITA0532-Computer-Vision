import cv2
from google.colab import files
import matplotlib.pyplot as plt

# Upload image
uploaded = files.upload()
path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(path)

# Convert to grayscale (needed for Canny)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Display images
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(edges, cmap='gray')
plt.title("Canny Edges")

plt.show()
