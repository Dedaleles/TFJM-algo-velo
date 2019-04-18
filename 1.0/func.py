import sys, pygame, math
from const import *
from param import *
pygame.font.init()
Arial = pygame.font.SysFont("Arial", 20)

def drawAxis(screen):
    pygame.draw.line(screen, grey, origin, ordTop, 3)
    pygame.draw.line(screen, grey, origin, absTop, 3)
    pygame.draw.line(screen, grey, (absTopX, absTopY+6), (absTopX, absTopY-6), 2)
    pygame.draw.line(screen, grey, (originX + sizeTmin, absTopY+6), (originX + sizeTmin, absTopY-6), 2)
    draw_dashed_line(screen, grey, coordTminabs, (coordTminabs[0], coordTminabs[1]-sizeOrd), dash_length=5)
    zero = Arial.render("0", True, grey)
    un = Arial.render("1", True, grey)
    Tmintext = Arial.render("Tmin", True, grey)
    screen.blit(zero, (originX - 10, originY))
    screen.blit(un, (absTopX, absTopY+2))
    screen.blit(Tmintext, coordTminabs)
    i=0
    while i < nbPersonne:
        i += 1
        pygame.draw.line(screen, grey, (originX+6, originY - sizePart*i ), (originX - 6, originY - sizePart*i), 2)
        nb = Arial.render(str(i)+"/" + str(nbPersonne), True, grey)
        screen.blit(nb, (originX - 30, originY - sizePart*i))



#pour tracer la figure
def drawFig(screen):
    mypos = []
    mypos.append(drawSegPied(screen, origin, nbPersonne-nbVelo))
    mypos.append(drawSegVelo(screen, origin, nbVelo))
    drawSegVelo(screen, mypos[0],nbVelo)
    drawSegPied(screen, mypos[1],nbPersonne-nbVelo)
    i=0
    while i < nbVelo-1:
        i+=1
        point = drawSegPied(screen, (origin[0] + (1/vVelo)*sizePart*i, origin[1] - sizePart*i), nbPersonne-nbVelo)
    j=0
    while j < nbPersonne-nbVelo-1:
        j+=1
        point = drawSegVelo(screen, (origin[0] + sizePart*j, origin[1] - sizePart*j), nbVelo)
    traceLigneEntreDeux(screen)

def traceLigneEntreDeux(screen):
        pointsGauche = []
        pointsDroite = []
        i=0
        pos = origin
        j=0
        while i<nbPersonne:
            if j < nbVelo:
                pos=(pos[0]+(1/vVelo)*sizePart, pos[1] - sizePart)
                pointsGauche.append(pos)
            else:
                pos=(pos[0]+ sizePart, pos[1] - sizePart)
                pointsGauche.append(pos)
            j+=1
            i+=1
        i=0
        pos = origin
        j=0
        while i<nbPersonne:
            if j < nbPersonne-nbVelo:
                pos= (pos[0]+sizePart, pos[1] - sizePart)
                pointsDroite.append(pos)
            else:
                pos= (pos[0]+ (1/vVelo)*sizePart, pos[1] - sizePart)
                pointsDroite.append(pos)
            j+=1
            i+=1
        i=0
        while i < len(pointsDroite):
            draw_dashed_line(screen, black,(int(pointsGauche[i][0]), int(pointsGauche[i][1])), (int(pointsDroite[i][0]), int(pointsDroite[i][1])), dash_length=5)
            i+=1


def drawSegPied(screen,firstPos, nbSeg):
    i=0
    endPos = (firstPos[0] + sizePart, firstPos[1] - sizePart)
    while i < nbSeg:
        i+=1
        pygame.draw.line(screen, black, firstPos, endPos, 2 )
        firstPos = endPos
        endPos = (endPos[0] + sizePart, endPos[1] - sizePart)
    return (endPos[0] - sizePart, endPos[1] + sizePart)

def drawSegVelo(screen, firstPos, nbSeg):
    i=0
    endPos = (firstPos[0] + (1/vVelo)*sizePart, firstPos[1] - sizePart)
    while i < nbSeg:
        i+=1
        pygame.draw.line(screen, black, firstPos, endPos, 2 )
        firstPos = endPos
        endPos = (endPos[0] + (1/vVelo)*sizePart, endPos[1] - sizePart)
    return (endPos[0] - (1/vVelo)*sizePart, endPos[1] + sizePart)




def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)
