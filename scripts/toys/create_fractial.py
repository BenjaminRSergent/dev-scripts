#!/usr/bin/python
# Just for fun...

from PIL import Image, ImageDraw, ImageFilter

def lerp(start, end, percent):
    minuspercent = 1 - percent
    retcolor = [0,0,0]

    for index in range(0,3):
        retcolor[index] = int(start[index] * minuspercent + end[index] * percent)

    return (retcolor[0], retcolor[1], retcolor[2])

def drawrect(drawer, center, size, startcolor, endcolor, childscale, depth, maxdepth):
    upperleft = (center[0] - size[0]/2,center[1] - size[1]/2)
    lowerright = (center[0] + size[0]/2,center[1] + size[1]/2)
    bounds = [upperleft[0], upperleft[1], lowerright[0], lowerright[1]]
    colortouse = lerp(startcolor, endcolor, depth/float(maxdepth))

    drawer.rectangle(bounds, fill=colortouse)

    if(depth >= maxdepth):
        return

    childsize = (size[0] * childscale, size[1] * childscale)

    leftcenter = (center[0] - size[0] + childsize[0], center[1])
    drawrect(drawer, leftcenter, childsize, startcolor, endcolor, childscale, depth+1, maxdepth)

    rightcenter = (center[0] + size[0] - childsize[0], center[1])
    drawrect(drawer, rightcenter, childsize, startcolor, endcolor, childscale, depth+1, maxdepth)

    upcenter = (center[0], center[1] + size[1] - childsize[1])
    drawrect(drawer, upcenter, childsize, startcolor, endcolor, childscale, depth+1, maxdepth)



imgsize = (1024,1024)

img = Image.new('RGB', imgsize)
drawer = ImageDraw.Draw(img)

coresize = (imgsize[0]/2, imgsize[1]/2)

center = (imgsize[0]/2, imgsize[1]/2 - coresize[1]/2)
size = (imgsize[0]/2, imgsize[1]/2)

drawrect(drawer, center, size, (0,0,255), (255,0,255), 0.25,0, 4)

del drawer

img.save("./Test",'PNG')