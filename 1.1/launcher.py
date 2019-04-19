from tkinter import *
from functools import partial
import os

def sendValue(nbpers, nbvelo, vvelo):
    print('sending')
    f = open('param.py','w')
    f.writelines("vVelo ="+str(vvelo.get())+" \nnbVelo ="+str(nbvelo.get())+" \nnbPersonne ="+str(nbpers.get()))
    f.close()
    openWindow()

def openWindow():
    print('open')
    print(os.popen("python3 main.py"))


root = Tk()
vitesseVeloLab = Label(root, text='vitesse vélo:' )
nbpersLab = Label(root, text='nombre de personne:')
nbveloLab = Label(root, text='nombre de vélo:')
nbpers = StringVar(root)
nbvelo = StringVar(root)
vVelo = StringVar(root)
nbpers.set(6)
nbvelo.set(3)
vVelo.set(2)
entry_nbpers = Entry(root, textvariable=nbpers)
entry_nbVelo = Entry(root, textvariable=nbvelo)
entry_vVelo = Entry(root, textvariable=vVelo)
vitesseVeloLab.grid(column=0, row=0)
entry_vVelo.grid(column=1, row=0)
nbpersLab.grid(column=0, row=1)
entry_nbpers.grid(column=1, row=1)
nbveloLab.grid(column=0, row=2)
entry_nbVelo.grid(column=1, row=2)
boutonConfirmer = Button(root, text='Confirmer', command=partial(sendValue,nbpers,nbvelo,vVelo))
boutonConfirmer.grid(column=0, row=3)
root.mainloop()
