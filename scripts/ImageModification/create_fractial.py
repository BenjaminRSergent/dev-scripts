#!/usr/bin/python
# Just for fun...

from PIL import Image, ImageDraw, ImageFilter


def drawrect(drawer, center, size, color, depth, maxdepth):
    upperleft = (center[0] - size[0]/2,center[1] - size[1]/2)
    lowerright = (center[0] + size[0]/2,center[1] + size[1]/2)
    bounds = [upperleft[0], upperleft[1], lowerright[0], lowerright[1]]
    drawer.rectangle(bounds, fill=color)

    if(depth >= maxdepth):
        return

    childsize = (size[0]/2, size[1]/2)

    leftcenter = (center[0] - size[0], center[1] - childsize[1])
    drawrect(drawer, leftcenter, childsize, color, depth+1, maxdepth)

    rightcenter = (center[0] + size[0], center[1] - childsize[1])
    drawrect(drawer, rightcenter, childsize, color, depth+1, maxdepth)

    upcenter = (center[0], center[1] + size[1]/2)
    drawrect(drawer, upcenter, childsize, color, depth+1, maxdepth)



imgsize = (1024,1024)

img = Image.new('RGB', imgsize)
drawer = ImageDraw.Draw(img)

coresize = (imgsize[0]/2, imgsize[1]/2)

center = (imgsize[0]/2, imgsize[1]/2)
size = (imgsize[0]/2, imgsize[1]/2)

drawrect(drawer, center, size, 'red', 0, 4)

del drawer

img.save("./Test",'PNG')