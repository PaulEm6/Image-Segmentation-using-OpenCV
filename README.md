# Image Segmentation using OpenCV

#### Objective:
This project implements a segmentation algorithm to identify individual grains within images and extract their average color.

#### Algorithm Implementation:
The algorithm preprocesses images, applies segmentation, and saves the average color of the minerals in a dataframe.

#### Dependencies:
- **opencv-python**: Main OpenCV library for image processing and computer vision tasks.
- **opencv-contrib-python**: Additional modules providing advanced functionality, such as `ximgproc` for superpixel segmentation like SLIC.
- **numpy**: Library for numerical data handling.
- **pandas**: Library for data manipulation and analysis.

#### Usage:
Run the `run.py` script with the image folder path as an argument:
```
python run.py Images
```

#### Applications:
Useful in material science, agriculture, and image analysis for tasks like grain size measurement and color analysis.

#### Future Improvements:
Potential enhancements include algorithm optimization, integration of machine learning techniques, and improving the user interface.