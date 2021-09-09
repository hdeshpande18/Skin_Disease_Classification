import tensorflow as tf
model = tf.keras.models.load_model('my_model.hdf5')

import streamlit as st
st.write("""
         # Skin Disease Classification
         """
         )
st.write("This is a simple image classification web app to predict disease class")
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):
    
        size = (150,150)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(28, 28),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img_resize[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) == 0:
        st.write("Melanocytic Nevi")
    elif np.argmax(prediction) == 1:
        st.write("Melanoma")
    elif np.argmax(prediction) == 2:
        st.write("Benign keratosis-like lesions")
    elif np.argmax(prediction) == 3:
        st.write("Basal cell carcinoma")
    elif np.argmax(prediction) == 4:
        st.write("Actinic keratoses")
    elif np.argmax(prediction) == 5:
        st.write("Vascular lesions")
    else:
        st.write("Dermatofibroma")
    
    #st.text("Probability (0: Melanocytic Nevi, 1:Melanoma , 2: Benign keratosis-like lesions, 3:Basal cell carcinoma,4:Actinic keratoses,5:Vascular lesions,6:Dermatofibroma ")
    #st.write(prediction)