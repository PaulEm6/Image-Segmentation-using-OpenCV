# pylint: skip-file

import cv2

import numpy as np
import os, sys
import pandas as pd

##############
#LOAD IMAGE
##############

if len(sys.argv) != 2:
    print("Usage: python script.py /path/to/file")
else:
    file_path = sys.argv[1]
    if os.path.exists(file_path) == False:
        print("Image file does not exist.")

# Load an image
image = cv2.imread(file_path)

##############
#PREPROCESSING
##############

# Step 2: Convert the image to LAB color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Apply contrast stretching
min_intensity = 0
max_intensity = 255
min_value = np.min(lab_image)
max_value = np.max(lab_image)
contrast_stretched = np.uint8((lab_image - min_value) / (max_value - min_value) * (max_intensity - min_intensity) + min_intensity)

##########
#ALGORITHM
##########

# Step 3: Apply SLIC superpixel segmentation
num_segments = 75  # You can adjust this value
compactness = 30 # You can adjust this value
slic = cv2.ximgproc.createSuperpixelSLIC(lab_image, cv2.ximgproc.SLICO, num_segments, compactness)
slic.iterate(20)

# Step 4: Get the superpixel labels
superpixel_labels = slic.getLabels()

# Step 5: Calculate the average color of each superpixel
superpixel_average_colors = {}
dataframe_list = []
for label in np.unique(superpixel_labels):
    mask = (superpixel_labels == label)
    superpixel = image.copy()
    superpixel[~mask] = 0  # Zero out pixels that don't belong to the superpixel
    average_color = np.mean(superpixel[mask], axis=0)
    superpixel_average_colors[label] = average_color

# Step 6: Filter out superpixels with average color values below a minimum threshold
min_color_value = 50  # Adjust this value as needed
number_rocks = 0
filtered_superpixels = {}
for label, average_color in superpixel_average_colors.items():
    if np.all(average_color > min_color_value):
        filtered_superpixels[label] = average_color
        dataframe_list.append(average_color)

# Step 7: Display the filtered superpixels
result_image = image.copy()
for label, average_color in filtered_superpixels.items():
    mask = (superpixel_labels == label)
    result_image[mask] = average_color

###############################
#SAVE DATAFRAME AND FINAL IMAGE
###############################

df = pd.DataFrame(dataframe_list, columns=['Moyenne de B', 'Moyenne de G', 'Moyenne de R'])

#print("Shape of Dataframe SLIC" + str(df.shape))

#cleprint(df)

base_name = os.path.splitext(file_path)[0]

# Now, 'image_with_contours' contains the original image with drawn contours.
cv2.imwrite(str(base_name) + "z_with_SLIC.png", result_image)

folder = os.path.dirname(file_path)

csv_path = os.path.join(folder, "image.csv")

df.to_csv(csv_path, mode='a', header=False, index=False)

