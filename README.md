# Skin-Disease-Classification
![Project Demo](Demo.gif)

# Sample snaps from each category
![Photos](category_samples.png)

Classification of 7 types of skin Lesions namely:

<li>Melanocytic nevi</li>
<li>Melanoma</li>
<li>Benign keratosis-like lesions</li>
<li>Basal cell carcinoma</li>
<li>Actinic keratoses</li>
<li>Vascular lesions</li>
<li>Dermatofibroma</li>

# About Dataset
Ham10000 is a collection dermatoscopic images from different populations, acquired and stored by different modalities. The final dataset consists of 10015 dermatoscopic images. The data set was obtained from here : https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000 From the HAM10000 data set we will be using only HAM10000_metadata.csv and HAM10000_images_part1 and HAM10000_images_part2 which have to be unzipped for accessing the images in the folders through the os module.

# Model
This is a simple Lenet model with 3 conv layers and 3 maxpool layers. Here the validation set was the same as the test set The model gave an accuracy of around 72% in the test set, 20 epochs was taken with anything more the more was seen to overfitting.

# Youtube Link 
https://www.youtube.com/watch?v=k4piRU17IpQ&feature=youtu.be

# Requirements
<li>Tensorflow 2.3.0</li>
<li>Streamlit 0.74.1</li>
<li>Numpy 1.18.5</li>
<li>Pillow 8.0.1</li>


