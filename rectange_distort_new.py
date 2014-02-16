# -*- coding: utf-9 -*-
"""Created on Tue Feb 10 7:07
@author : voladoddi
"""

import numpy as np
from matplotlib import pyplot

#creating a normal rectangle centered about the origin.
def makerectangle(width, height, vec_points_per_side = 25):
    #allocate an array of points
    xnormal = np.zeros(4*vec_points_per_side)
    ynormal = np.zeros(4*vec_points_per_side)

    #define sides of rectangle, counter - clockwise
    #left side

#main part of the code ---
def main():
    #generate a rectangle
    rect_normal = makerectangle(5,10)

    #generate points for warped version
    k1 = 0.005
    k2 = 0.001
    k3 = 0.001
    rect_distort = radial_distort(rect_normal, k1, k2, k3)

    #define plot and display
    r_fig, r_axes = pyplot.subplots() #pyplot with just one subplot. useful for multiple plots on the same figure.
    r_normal  = pyplot.plot(rect_normal[0,:], rect_normal[1,:], 'b*-',label = 'normal')
    r_distort = pyplot.plot(rect_distort[0,:], rect_distort[1,:], 'r*', label = 'distorted')
    pyplot.legend()
    pyplot.title('Distorting a rectangle')
    pyplot.show()

#starting of the process. calling the main() function
if __name__ == '__main__':
    main()
