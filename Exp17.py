# 17. Watermarking Technique using OpenCV

# Import libraries
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload image
uploaded = files.upload()

# Get image path
image_path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(image_path)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Copy image
watermarked = img.copy()

# Watermark text
text = "WATERMARK"

# Get image dimensions
h, w, _ = watermarked.shape

# Text position
position = (w//4, h//2)

# Add watermark
cv2.putText(
    watermarked,
    text,
    position,
    cv2.FONT_HERSHEY_SIMPLEX,
    2,                 # Font size
    (255, 255, 255),  # White color
    4,                 # Thickness
    cv2.LINE_AA
)

# Convert output to RGB
watermarked_rgb = cv2.cvtColor(watermarked, cv2.COLOR_BGR2RGB)

# Display output
plt.figure(figsize=(12,6))

# Original image
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Watermarked image
plt.subplot(1,2,2)
plt.imshow(watermarked_rgb)
plt.title("Watermarked Image")
plt.axis('off')

plt.show()
