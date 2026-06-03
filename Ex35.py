  # 35. Display User Entered Text on Image using OpenCV

# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Get image size from user
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Get text from user
text = input("Enter text to display on image: ")

# Create white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Define text position
position = (50, height // 2)

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
color = (255, 0, 0)   # Blue color in BGR
thickness = 3

# Put text on image
cv2.putText(
    image,
    text,
    position,
    font,
    font_scale,
    color,
    thickness,
    cv2.LINE_AA
)

# Convert BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display image
plt.figure(figsize=(10,6))
plt.imshow(image_rgb)
plt.title("Image with User Text")
plt.axis('off')

plt.show()
