#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GetMarkFromSection.py
#  
#  Copyright 2018 User <User@DESKTOP-17Q7VC8>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import numpy as np
import cv2
import matplotlib.pyplot as plt
from imutils.perspective import four_point_transform
from imutils import contours
import math
import imutils
import time
from pandas import DataFrame
import errno
import os
from datetime import datetime

def divideSection(bubbleregion,path):

	# [GET] region of every questions section
	height,width = bubbleregion.shape[:2]
	print("height", height)
	print("width", width)

	Y = height
	WidthStart = 0
	sect = list()
	qSect = list()
	for i in range(2):
		WidthEnd = int(width * (i+1)/2)
		print(i)
		if i == 0:
			WidthStart = WidthStart + 10
			
		if i == 1:
			WidthStart = WidthStart - 5
			WidthEnd   = WidthEnd 
			
		
		sect.insert(i,(bubbleregion[120:Y-30 , WidthStart+30:WidthEnd]))
		
		if i == 0:
			y,x = sect[i].shape[:2]
			leftbound = 0
			rightbound = x - 30
			topbound = 0
			
			heightRange = int((y-5)/15)
			print("heightRange",heightRange)
			bottombound = heightRange

			for l in range(15):
				print("topbound",topbound)
				
				print("bottombound",bottombound)
				qSect.insert(l,(sect[i][topbound:bottombound, leftbound:rightbound]))
				
				topbound = bottombound - 25 
				bottombound = bottombound + heightRange + 2
				cv2.imwrite(os.path.join(path , str(l)+"_section1.jpg"),qSect[l])
				
				
		WidthStart = WidthEnd
		
		
	return sect,qSect

def divideSmaller(img):
	height,width = img.shape[:2]
	boxheight = int(height/15)
	print(boxheight)
	return boxheight
def resizeSmaller(img):
	height,width = img.shape[:2]
	height = int((height/2) * 1)
	width = int((width/2) * 1)
	resized_img = cv2.resize(img,(width,height))
	return resized_img

def viewPixel(img): 
		
	height,width = img.shape[:2]
	print("height", height)
	print("width", width)
	return

def save_qSect():
	mydir = os.path.join(os.getcwd(),datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	try:
		os.makedirs(mydir)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise  # This was not a "directory exist" error..
	print(mydir)
	return mydir


  
image = cv2.imread("b.jpg")
image = resizeSmaller(image)
path = save_qSect()
sect,qSect = divideSection(image,path)
cv2.waitKey(0)
