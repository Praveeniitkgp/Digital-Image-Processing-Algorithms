import cv2
import numpy as np
import sys

def contour_follow(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)
    if image is None:
        print(f"Error reading image {input_image_path}")
        return
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        print(f"No contours found in {input_image_path}")
        return
    
    output_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    for contour in contours:
        cv2.drawContours(output_image, [contour], -1, (0, 255, 0), 1)  # Green color for contours
    
    cv2.imwrite(output_image_path, output_image)

if __name__ == "__main__":
    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    contour_follow(input_image_path, output_image_path)
