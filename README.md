# Extraction of façade details from street-view panoramic images
This is a modified implementation of Mask R-CNN on Python 3, Keras, and TensorFlow. The model generates bounding boxes and segmentation masks for each instance of an object in the image. It's based on Feature Pyramid Network (FPN) and a ResNet101 backbone.
Instance segmenting more than 2 classes in an image,where image dataset is from publicly available data, for annotation we are using VGG annotator latest version

Here we defined 5 classes :
 - Window
 - Wall
 - Basement_window
 - Door
 - Balcony
 
The repository includes:
- Source code for download panorama images
- Source code for Rectilinear projection
- Source code for Identifying building based on longitude, latitude and heading
- Jupyter notebooks to visualize image extracting pipeline process
- Modified code of Mask R-CNN for custom data set
- Jupyter notebooks to visualize the detection pipeline at every step
- Evaluation metrics 
