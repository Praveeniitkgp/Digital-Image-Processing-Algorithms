import cv2
import numpy as np
import sys

def chamfer_label(input_image_path, output_image_path):
    # Load the input image
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    
    # Threshold the image to binary (0 and 255)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Invert the binary image so that foreground is 1 and background is 0
    binary = 255 - binary

    # Find connected components
    num_labels, labels = cv2.connectedComponents(binary, connectivity=8)
    
    # Generate random colors for each component
    output_image = np.zeros((labels.shape[0], labels.shape[1], 3), dtype=np.uint8)
    colors = np.random.randint(0, 255, size=(num_labels, 3))

    for i in range(1, num_labels):
        output_image[labels == i] = colors[i]

    # Save the labeled image
    cv2.imwrite(output_image_path, output_image)

if __name__ == "__main__":
    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    chamfer_label(input_image_path, output_image_path)
