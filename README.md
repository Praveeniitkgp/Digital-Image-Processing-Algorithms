######NOTES  ->>>> I have created a shell file can be use drun all file sequentiallly in one go. 



#Step 1: Chamfer Labeling

#Process each image file to label the connected components:

python3 chamfer_label.py curve.256.bmp output_curve_labelled.png
python3 chamfer_label.py setsqr.256.bmp output_setsqr_labelled.png
python3 chamfer_label.py spaner.256.bmp output_spaner_labelled.png


#Step 2: Contour Following
python3 contour_follow.py output_curve_labelled.png output_curve_contour.png
python3 contour_follow.py output_setsqr_labelled.png output_setsqr_contour.png
python3 contour_follow.py output_spaner_labelled.png output_spaner_contour.png


#Step 3: Polygonization (ADSS Approach)

python3 polygonization.py output_curve_contour.png output_curve_polygonized.png
python3 polygonization.py output_setsqr_contour.png output_setsqr_polygonized.png
python3 polygonization.py output_spaner_contour.png output_spaner_polygonized.png




#This README.md file consolidates all the commands needed to run each part of this image processing #assignment.
