# 25. General Object Recognition (Watch Detection) using OpenCV

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

# Create copy for output
output = img_rgb.copy()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Apply Hough Circle Transform to detect watch dial
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=100,
    param1=50,
    param2=30,
    minRadius=30,
    maxRadius=150
)

# Draw detected watch
if circles is not None:
    circles = circles[0].astype(int)

    for (x, y, r) in circles:
        # Draw outer circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)

        # Put label
        cv2.putText(
            output,
            "Watch Detected",
            (x - 40, y - r - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

# Display results
plt.figure(figsize=(12,6))

# Original Image
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Watch Detection Output
plt.subplot(1,2,2)
plt.imshow(output)
plt.title("Watch Recognition Output")
plt.axis('off')

plt.show()
