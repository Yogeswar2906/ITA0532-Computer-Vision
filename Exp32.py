# 32. Create White Image with 4 Colored Corner Boxes

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Get image size from user
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create white image
# 255 = white color
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Box size = 1/10th of image size
box_h = height // 10
box_w = width // 10

# Top-left corner → Black
img[0:box_h, 0:box_w] = [0, 0, 0]

# Top-right corner → Blue
img[0:box_h, width-box_w:width] = [0, 0, 255]

# Bottom-left corner → Green
img[height-box_h:height, 0:box_w] = [0, 255, 0]

# Bottom-right corner → Red
img[height-box_h:height, width-box_w:width] = [255, 0, 0]

# Display image
plt.figure(figsize=(8,8))
plt.imshow(img)
plt.title("White Image with 4 Colored Boxes")
plt.axis('off')

plt.show()
