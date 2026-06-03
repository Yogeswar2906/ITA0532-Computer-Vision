# 30. Smile Detection using OpenCV

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

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load face cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Load smile cascade
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(80, 80)
)

# Create output copy
output = img_rgb.copy()

# Detect smile inside face
for (x, y, w, h) in faces:

    # Draw face rectangle
    cv2.rectangle(output, (x, y), (x+w, y+h), (0,255,0), 2)

    # ROI for smile detection
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = output[y:y+h, x:x+w]

    # Detect smile
    smiles = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(25, 25)
    )

    # Draw smile rectangles
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(
            roi_color,
            (sx, sy),
            (sx+sw, sy+sh),
            (255,0,0),
            2
        )

# Display results
plt.figure(figsize=(12,6))

# Original Image
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Smile Detection Output
plt.subplot(1,2,2)
plt.imshow(output)
plt.title("Smile Detection Output")
plt.axis('off')

plt.show()

print("Smile Detection Completed!")
