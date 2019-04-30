#! /usr/bin/env python
# Author: Mart Gil
# Date: February 11. 2019
# Description: simple script to extract aspect ratio of an image

width = input('Enter Image width: ')
height = input('Enter image height: ')

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

d = gcd(width,height)

aspect_width = width / d
aspect_height = height / d

print 'Your image aspect ratio is ' + str(aspect_width) + ':' + str(aspect_height)
print 'Crop your image at http://croppola.com/'
# credits to croppola

