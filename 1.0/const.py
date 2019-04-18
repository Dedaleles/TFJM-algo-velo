from param import *
vPied = 1

size = width, height = 700, 700
speed = [2, 2]
black = 0, 0, 0
grey = 100, 100, 100
white = 255, 255, 255
originX = 40
originY = 660
origin = (originX, originY)
ordTopX = 40
ordTopY = 40
ordTop = (ordTopX, ordTopY)
absTopX = 660
absTopY = 660
absTop = (absTopX, absTopY)
sizeOrd = originY - ordTopY
sizeAbs = absTopX - originX
sizePart = sizeOrd / nbPersonne
Tmin = (nbVelo+vVelo*(nbPersonne-nbVelo))/(nbPersonne*vVelo)
sizeTmin = sizeAbs*Tmin
coordTminabs= (originX + sizeTmin, absTopY)
dist2PtAdj = ((1/nbPersonne)-(1/(nbPersonne*vVelo)))*sizeAbs
