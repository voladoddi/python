# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:27:26 2014

@author: voladoddi
"""

import numpy as np
import matplotlib.pyplot as pp

x1=np.ones(50)
x1[0:25] = 5
x1[25:50] = np.linspace(1,5,25)

x2=np.ones(50)
x2[0:25] = np.linspace(1,5,25)
x2[25:50] = 1

y1=np.ones(50)
y1[0:25]= np.linspace(1,5,25)
y1[25:50]=5

y2=np.ones(50)
y2[0:25]=1
y2[25:50]=np.linspace(1,5,25)


# radius of distortion
# we have plotted the rectangle in two parts (x1,y1) and (x2,y2). Hence,
#I thought r = sqrt ([x1 x2]^2 + [y1 y2]^2) where [x1 x2] indicates concatenation
x=np.ones(50)
x = np.concatenate([x1,x2])
y= np.concatenate([y1,y2])

r = np.sqrt(pow(x,2) + pow(y,2)) #this needs to be a single scalar but I'm getting a vector. Would appreciate pointers on this.
                                 #r cannot be calculated separately (?)
                                 
                                 
# co-efficients for x_corrected and y_corrected
k1 = 0.005;            #noted from Eric's demo run.
k2 = 0.001;
k3 = 0.001;

#calculating x_xorrected and y_corrected


xc1 = np.multiply(x1,( 1 + k1*r**2 + k2*r**4 + k3*r**6)) 		#changed to r**2
yc1 = np.multiply(y1,( 1 + k1*r**2 + k2*r**4 + k3*r**6))

xc2 = np.multiply(x2,( 1 + k1*r**2 + k2*r**4 + k3*r**6))
yc2 = np.multiply(y2,( 1 + k1*r**2 + k2*r**4 + k3*r**6))


# plotting the rectangle and the distortion
p = pp.plot(x,y,'r',x2,y2,'r',xc1,yc1,'g',xc2,yc2,'g');
p.set_autoscale_on        
pp.show(p)

