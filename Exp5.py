import cv2
from google.colab import files
import matplotlib.pyplot as plt

# Upload image
uploaded = files.upload()
path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(path)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Function to plot histogram
def plot_histogram(image):
    colors = ('r', 'g', 'b')
    for i, col in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0,256])
        plt.plot(hist, color=col)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()

# Display image
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()

# Call function
plot_histogram(img_rgb)
