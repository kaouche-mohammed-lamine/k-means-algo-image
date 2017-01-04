#!/usr/bin/env python

from __future__ import division
from PIL import Image
import numpy as np
import random
import math



#begining the stage one
global image
image1 = Image.open("salt221.png")# it is accept all type of image like jpg,png, ...... 
image = image1.convert("RGB")  #just for convert the image to RGB without alfa to using it in the program
#image.save("salt21.png") #if you need to save the image 
global size #using global size this image to use it in all this program
size = width, height = image.size
def moyen(x,y,z):
    if x+y+z != 0:
        if (x/(x+y+z) > y/(x+y+z) and x/(x+y+z) > z/(x+y+z) ):
            return x
def moyen_g(x,y,z):
    if x+y+z != 0:
        if (y/(x+y+z) > x/(x+y+z) and y/(x+y+z) > z/(x+y+z) ):
            return y
def moyen_b(x,y,z):
    if x+y+z != 0:
        if (z/(x+y+z) > y/(x+y+z) and z/(x+y+z) > x/(x+y+z) ):
            return z

def center_r(g):
    som=len(g)
    x_som=0
    for item in g:
        x,y,z=item
        x_som+=x
    return (x_som/som)

def center_g(g):
    som=len(g)
    y_som=0
    for item in g:
        x,y,z=item
        y_som+=y
    return (y_som/som)
def center_b(g):
    som=len(g)
    z_som=0
    for item in g:
        x,y,z=item
        z_som+=z
    return (z_som/som)


def distance(pixel_cen,pixel):
    x_c,y_c,z_c=pixel_cen
    x,y,z=pixel

    dis_x = (x-x_c)*(x-x_c)
    dis_y = (y-y_c)*(y-y_c)
    dis_z = (z-z_c)*(z-z_c)
    diss=dis_x+dis_y+dis_z
    dis = math.sqrt(diss)

    return dis





def main():
	group_red=[] #this is list for add the pixel have the red color the big one 
	group_rred=[] #this is list for add the position the pixel 
	group_green=[]#this is list for add the pixel have the red color the big one 
	group_ggreen=[]#this is list for add the position the pixel 
	group_blue=[]#this is list for add the pixel have the red color the big one 
	group_bblue=[]#this is list for add the position the pixel 
	group_black=[]#this is list for add the pixel have the red color the big one 


	while True:
		r_xi = random.randint(1,width)  #this is here for get the pixel have a red the big one using the moyen function 
		r_yi = random.randint(1,height)
		cordonate = r_xi,r_yi
		pixel1 = image.getpixel(cordonate)
		x,y,z=pixel1
		if x== moyen(x,y,z):
			break
		else:
			pass

	while True:
		g_xi = random.randint(1,width)  #this is here for get the pixel have a red the big one using the moyen function 
		g_yi = random.randint(1,height)
		cordonate = g_xi,g_yi
		pixel2 = image.getpixel(cordonate)
		x,y,z=pixel2
		if y== moyen_g(x,y,z):
			break
		else:
			pass
	while True:
		b_xi = random.randint(1,width) #this is here for get the pixel have a red the big one using the moyen function 
		b_yi = random.randint(1,height)
		cordonate = b_xi,b_yi
		pixel3 = image.getpixel(cordonate)
		x,y,z=pixel3
		if z== moyen_b(x,y,z):
			break
		else:
			pass

	center1=0,0,0 #set three center 
	center2=0,0,0
	center3=0,0,0
	true=True


	while true:
		jj=range(1,width)
		ii=range(1,height)

		for j in jj:
			for i in ii :
				cordon = j,i
				pixel = image.getpixel(cordon)
				d_x=distance(pixel1,pixel)
				d_y=distance(pixel2,pixel)
				d_z=distance(pixel3,pixel)
				if(d_z == d_x) and (d_z == d_y):
					group_black.append(pixel)
				if d_x < d_y and d_x < d_z:
					group_red.append(pixel)
					group_rred.append(cordon)
				if d_y < d_x and d_y < d_z:
					group_green.append(pixel)
					group_ggreen.append(cordon)
				if d_z < d_x and d_z < d_y:
					group_blue.append(pixel)
					group_bblue.append(cordon)


#Begining the stage three
		if pixel1 == center1 and pixel2 == center2 and pixel3 == center3 :
			for j in jj:
				for i in ii :
					cordon = j,i
					for item in group_rred:
						if(cordon == item):
							print "red"
							print image.getpixel((cordon))
							image.putpixel((cordon),(255,0,0))
							#print image.getpixel((cordoni))
							break	
			for j in jj:
				for i in ii :
					cordon = j,i
					for item in group_ggreen:
						if(cordon == item):
							print "green"
							print image.getpixel((cordon))
							image.putpixel(cordon,(0,255,0))
							#print image.getpixel((cordonis))
							break
			for j in jj:
				for i in ii :
					cordon = j,i
					for item in group_bblue:
						if(cordon == item):
							print "blue"
							print image.getpixel((cordon))
							image.putpixel(cordon,(0,0,255))
							#print image.getpixel((cordoniz))
							break

			true = False
		else :
			center1 = pixel1
			pixel1 = center_r(group_red),center_g(group_red),center_b(group_red)
			center2 = pixel2
			pixel2 = center_r(group_green),center_g(group_green),center_b(group_green)
			center3 = pixel3
			pixel3 = center_r(group_blue),center_g(group_blue),center_b(group_blue)
			group_green=[]
			group_blue=[]
			group_red=[]
			group_rred=[]
			group_bblue=[]
			group_ggreen=[]
      
	image.show()
if __name__ == "__main__":
	main()

#show the result or classification


del image # for remove the object of Image 




