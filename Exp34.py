# 34. Create White Image and Draw Circle using OpenCV

# Import libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Get image size from user
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Define circle center
center = (width//2, height//2)

# Define radius
radius = min(height, width) // 4

# Circle color (Red in BGR)
color = (0, 0, 255)

# Thickness
thickness = 4

# Draw circle
cv2.circle(image, center, radius, color, thickness)

# Convert BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display image
plt.figure(figsize=(8,8))
plt.imshow(image_rgb)
plt.title("Circle Shape")
plt.axis('off')

plt.show()
