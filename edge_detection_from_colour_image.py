# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 01:37:47 2014

@author: voladoddi
"""
#   creating a python script to read a colour image, convert it to a grayscale
#   image and display it, and then perform edge detection on it.

from scipy import misc,signal
import matplotlib.pyplot as plt
import numpy as np

'''numpy or matplotlib - either doesn't have an inbuilt function to convert
   a colour image to a grayscale image hence defining this function to do that
   
   This is an essential step to perform all sorts of binary processing on the 
   image. Including edge detection'''
   
def rgb2gray(rgb):
   r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
   gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
   return gray

#edge detection using 'scipy' 's 'convolve'
def edge_detect(input_image):
   #  lx, ly = input_image.shape
    mask_sobel_row= [[1,0,-1],[2,0,-2],[1,0,-1]]
    mask_sobel_col= [[1,2,1],[0,0,0],[-1,-2,-1]]
    
    row = signal.convolve2d(input_image,mask_sobel_row,mode='same')
    column = signal.convolve2d(input_image,mask_sobel_col,mode='same')  
    
    mag_map = np.sqrt((row**2) + (column**2))

    plt.figure(2)
    plt.imshow(mag_map,cmap = plt.get_cmap('gray'))
    plt.show()

#main function
def main():
    l = misc.imread('C:/Users/voladoddi/desktop/IMG_1630.jpg') #read image
    misc.imsave('C:/Users/voladoddi/desktop/IMG_1631.jpg',l) #saving a copy
    img = misc.imread('C:/Users/voladoddi/desktop/IMG_1631.jpg')#reading the copy
    img.shape #to check the dimensions of the image. [1280,960,3]
              #indicates that the image is of 1280x960 and a colour image(3D/3channels)
    
    img_gray = rgb2gray(img)
    plt.figure(1)    
    plt.imshow(img_gray,cmap = plt.get_cmap('gray'))
    plt.show()
    
    edge_detect(img_gray)
 
# call main - start the code   
if __name__=="__main__":
    main()
#end 
    

    