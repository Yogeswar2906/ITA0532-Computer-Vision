# 33. Create White Image and Draw Rectangle using OpenCV

# Import libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Get image size from user
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Define rectangle coordinates
start_point = (width//4, height//4)
end_point = (3*width//4, 3*height//4)

# Rectangle color (Blue in BGR)
color = (255, 0, 0)

# Thickness of rectangle border
thickness = 4

# Draw rectangle
cv2.rectangle(image, start_point, end_point, color, thickness)

# Convert BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display image
plt.figure(figsize=(8,8))
plt.imshow(image_rgb)
plt.title("Rectangle Shape")
plt.axis('off')

plt.show()
