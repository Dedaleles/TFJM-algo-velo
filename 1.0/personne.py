from func import *
from const import *
from param import *
import sys, pygame

class groupe:
    def __init__(self,screen, nbPers):
        self.screen = screen
        self.Arial = pygame.font.SysFont("Arial", 15)
        self.pos = origin
        self.velo = False
        i=0
        self.nbPers = nbPers
        self.imglink = 'pers.png'
        self.rawimage = pygame.image.load(self.imglink)
        self.image = pygame.transform.scale(self.rawimage, (int(self.rawimage.get_width()/20), int(self.rawimage.get_height()/20)))

    def getNb(self):
        return self.nbPers

    def setNb(self):
        i=0

    def add(self, nbPersonne):
        self.nbPers += nbPersonne

    def remove(self, nbPers):
        self.nbPers -= nbPers

    def setPos(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    def refresh(self):
        self.txt = self.Arial.render(str(self.nbPers), True, black)
        self.screen.blit(self.image, self.pos)
        self.screen.blit(self.txt, (self.pos[0]+self.image.get_width(),self.pos[1]))
        pygame.display.flip()

class totalPers:
    def __init__(self,screen):
        self.screen = screen
        self.nbPers = nbPersonne
        self.grps = [groupe(self.screen, self.nbPers)]
        self.refresh()
        self.time = 0
        self.timeDepasse = 1

    def split(self):
        self.time +=1
        if self.time == 1:
            self.grps = [groupe(self.screen, nbVelo), groupe(self.screen,self.nbPers-nbVelo)]
            self.grps[0].setPos((origin[0]+(1/vVelo)*sizePart, origin[1] - sizePart))
            self.grps[1].setPos((origin[0]+sizePart, origin[1] - sizePart))
            self.refresh()
        elif self.time<nbPersonne:
            #gere l'axe de gauche
            grpProv = self.grps
            if self.time < nbVelo+1:
                first = grpProv[0].getNb() - 1
            else:
                first =  grpProv[0].getNb() + 1
            self.grps = [groupe(self.screen, first)]
            if self.time< nbVelo+1 and self.time < nbPersonne-nbVelo+1:
                i=0
                while i < self.time-1:
                    self.grps.append(groupe(self.screen, 2))
                    i+=1
            elif self.time >= nbVelo and self.time <= nbPersonne-nbVelo:
                i=0
                while i < nbVelo-1:
                    self.grps.append(groupe(self.screen, 2))
                    i+=1
            elif self.time <= nbVelo and self.time >= nbPersonne-nbVelo:
                i=0
                while i < nbVelo-1:
                    self.grps.append(groupe(self.screen, 2))
                    i+=1
            elif self.time > nbVelo and self.time > nbPersonne-nbVelo:
                i=0
                self.timeDepasse+=1
                while i < nbVelo-self.timeDepasse:
                    self.grps.append(groupe(self.screen, 2))
                    i+=1

            #gere l'axe de droite
            if self.time < nbPersonne-nbVelo+1:
                last = grpProv[len(grpProv)-1].getNb() - 1
            else:
                last =  grpProv[len(grpProv)-1].getNb() + 1
            self.grps.append(groupe(self.screen, last))
            #definir les positions
            if self.time < nbVelo+1:
                posGauche = self.grps[0].getPos()
                self.grps[0].setPos((origin[0]+self.time*(1/vVelo)*sizePart, origin[1] - self.time*sizePart))
                posGauche = self.grps[0].getPos()
            else:
                posGauche = self.grps[0].getPos()
                self.grps[0].setPos((origin[0]+(self.time-nbVelo)*sizePart+(1/vVelo)*sizePart*nbVelo, origin[1] - self.time*sizePart))
                posGauche = self.grps[0].getPos()

            i=1
            print(posGauche)
            while i < len(self.grps):
                self.grps[i].setPos((posGauche[0]+i*dist2PtAdj, posGauche[1]))
                i+=1
        elif self.time == nbPersonne:
            print(self.time)
            self.grps = [groupe(self.screen, self.time)]
            self.grps[0].setPos((origin[0]+(self.time-nbVelo)*sizePart+(1/vVelo)*sizePart*nbVelo, origin[1] - self.time*sizePart))

        self.refresh()

    def refresh(self):
        for grp in self.grps:
            grp.refresh()
