import cv2
import numpy as np
import sys
import random

def random_color():
    """Generate a random color."""
    return tuple(random.randint(0, 255) for _ in range(3))

def polygonization(input_image_path, output_image_path):
    # Load the contour image
    image = cv2.imread(input_image_path)
    if image is None:
        print(f"Error: Could not load image {input_image_path}")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Find contours
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create an overlay image for polygons
    overlay = image.copy()
    
    # Draw the contours in black or white (based on original image)
    cv2.drawContours(image, contours, -1, (255, 255, 255), 1)
    
    for contour in contours:
        # Approximate each contour to a polygon
        epsilon = 0.01 * cv2.arcLength(contour, True)
        polygon = cv2.approxPolyDP(contour, epsilon, True)
        
        # Draw the polygon on the overlay with a random color
        polygon_color = random_color()
        cv2.polylines(overlay, [polygon], isClosed=True, color=polygon_color, thickness=2)
        
        # Mark the vertices with small circles (distinct color)
        vertex_color = (0, 255, 255)  # Yellow color for vertices
        for point in polygon:
            cv2.circle(overlay, tuple(point[0]), radius=5, color=vertex_color, thickness=-1)

    # Blend the overlay with the original image to ensure contours remain visible
    alpha = 0.5  # Transparency factor
    cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

    # Save the polygonized image
    cv2.imwrite(output_image_path, image)

if __name__ == "__main__":
    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    polygonization(input_image_path, output_image_path)
