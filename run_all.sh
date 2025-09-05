#!/bin/bash

# Array of input image files
images=("curve.256.bmp" "setsqr.256.bmp" "spaner.256.bmp")

for image in "${images[@]}"; do
    # Get the base name without extension
    base_name=$(basename "$image" .256.bmp)
    
    # Step 1: Chamfer Labeling
    python3 chamfer_label.py "$image" "output_${base_name}_labelled.png"

    # Step 2: Contour Following
    python3 contour_follow.py "output_${base_name}_labelled.png" "output_${base_name}_contour.png"

    # Step 3: Polygonization
    python3 polygonization.py "output_${base_name}_contour.png" "output_${base_name}_polygonized.png"
done
