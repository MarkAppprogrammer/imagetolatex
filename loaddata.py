#imports
import tarfile
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from itertools import islice

#vars

#methods
def readlst(filename):
    with open(filename, 'r') as file:
        data = [line.rstrip('\n').split(" ") for line in file]
    image_names = [row[1] + ".png" for row in data]
    render_types = [row[2] for row in data]
    formula_numbers = [row[0] for row in data]
    return image_names, render_types, formula_numbers

def readformulas(filename):
    with open(filename, 'r') as file:
        data = [line.rstrip('\n') for line in file]
    return data

def unpacktar(filename, extract_path):
    with tarfile.open(filename, 'r:gz') as tar:
        tar.extractall(path=extract_path)

def resize_image(image, target_height):
    height, width = image.shape[:2]
    aspect_ratio = width / height
    new_width = int(target_height * aspect_ratio)
    resized_image = tf.image.resize(image, [target_height, new_width])
    return resized_image

def load_images(foldername, filenames):
    images = []

    image_files = [f for f in os.listdir(foldername) if os.path.isfile(os.path.join(foldername, f))]
    filtered_files = [f for f in image_files if f in filenames]

    print("[*] Collected image files")
    for i, image_file in enumerate(filtered_files):
        #add exception here
        read_image = tf.io.read_file(foldername + image_file)

        image = tf.image.decode_png(read_image, channels=1)

        #resize image to resoable before converting
        #image = resize_image(image, 250)
        image = tf.image.resize(image, (250, 500), method=tf.image.ResizeMethod.BICUBIC)     

        #preprocess 
        image = tf.image.adjust_contrast(image, contrast_factor=1.5)
        image = tf.image.adjust_brightness(image, delta=0.1)

        #convert
        image = tf.image.convert_image_dtype(image, tf.float32)
        
        if ( (i + 1) % 1000 == 0):
            print("Loaded " + str(i + 1) + " images")
        images.append(image)
    
    return images

def arrange_formulas(formulafile, linenumbers):
    arranged_formulas = []

    file = open(formulafile)
    content = file.readlines()
    
    for linenumber in linenumbers:
        arranged_formulas.append(content[int(linenumber) - 1].rstrip('\n'))
   
    return arranged_formulas
#test
#need to try only loading images that are part of the dataset we want not all for time usage
""" image_names, render_types, formula_numbers = readlst(filename='data/im2latex_test.lst')
images = load_images(foldername='data/fixed_formula_images/', filenames=image_names) """
#unpacktar(filename='data/formula_images.tar.gz', extract_path='data')


