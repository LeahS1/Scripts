# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:01:41 2020
Building a Convolutional Neural Network to distinguish Cats & Dogs

"""

import os
import os.path
import zipfile
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import Model

local_zip = '.../Downloads/catsanddogsfiltered.zip'
path = '.../Downloads/catsanddogsfiltered/'


isdir = os.path.isdir(path)
#Extract the files from zipfile
if isdir == True:
    print ("Folder exists")
else: 
    zip_ref = zipfile.ZipFile(local_zip, "r")
    zip_ref.extractall('C:/Users/ilear/Downloads')
    zip_ref.close()

#Defining paths and directories
base_dir = '.../Downloads/catsanddogsfiltered'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join (base_dir, 'validation')

# Directory with training Cat images
train_cats_dir = os.path.join(train_dir, 'cats')

#Directory with training Dog images
train_dogs_dir = os.path.join (train_dir, 'dogs')

#Directory with the validation Cat images
validation_cats_dir = os.path.join(validation_dir, 'cats')

#Directory with validation Dog images
validation_dogs_dir = os.path.join(validation_dir, 'dogs')

#Determine file names
train_cat_fnames = os.listdir(train_cats_dir)
train_dog_fnames = os.listdir(train_dogs_dir)
#Sort dog filenames in ascending order
sorted(train_dog_fnames)

#Print first 10 instances in Cat directory
print (train_cat_fnames[:10])
print (train_dog_fnames[:10])

#determine total number of instances
print ('total training cat images: ', len(os.listdir(train_cats_dir)))
print ('total training dog images: ', len(os.listdir(train_dogs_dir)))
print ('total validation cat images: ', len(os.listdir(validation_cats_dir)))
print ('total validation dog images: ', len(os.listdir(validation_dogs_dir)))


#output images as 4x4 feature input maps
nrows = 4
ncols = 4
pic_index = 0

#Display a 4x4 grid of 8 cat and dog images
fig = plt.gcf()
fig.set_size_inches(ncols*4, nrows*4)

pic_index +=8
next_cat_pix = [os.path.join(train_cats_dir, fname)
    for fname in train_cat_fnames[pic_index-8:pic_index]]
next_dog_pix = [os.path.join(train_dogs_dir, fname)
    for fname in train_dog_fnames[pic_index-8:pic_index]]

for i, img_path in enumerate(next_cat_pix+next_dog_pix):
    sp = plt.subplot(nrows,ncols, i+1)
    sp.axis('Off')
    
    img = mpimg.imread(img_path)
    plt.imshow(img)

plt.show()

#Build the convnet

#Define convolution parameters
img_input = layers.Input(shape= (150,150,3))
#First convolution-Extract 16 filters that are 3x3 and follow with maxpooling algorithm of 2x2
x = layers.Conv2D (16,3,activation='relu')(img_input)
x = layers.MaxPooling2D(2)(x)

#2nd convolution
x = layers.Conv2D(32,3,activation='relu')(x)
x = layers.MaxPooling2D(2)(x)

#3rd convolution
x = layers.Conv2D(64, 3, activation='relu')(x)
x = layers.MaxPooling2D(2)(x)

#Flatten feature map
x = layers.Flatten()(x)
#Create a fully connected layer
x = layers.Dense(512,activation='relu')(x)

#create output layer w/ single node & sigmoid activation
output = layers.Dense(1, activation='sigmoid')(x)

#create convolutional neural network model
# input= input feature map
# output = input feature map + stacked conv/maxpooling layers + fully
#connected layer + sigmoid output layer

model = Model(img_input,output)
model.summary()

from tensorflow.keras.optimizers import RMSprop
model.compile (loss='binary_crossentropy',
               optimizer= RMSprop (lr=0.001),
               metrics=['acc'])
