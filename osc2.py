#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:22:47 2018

@author: andre
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import qutip as qt

N=20
n=5
a=qt.destroy(N)
x=qt.position(N)
p=qt.momentum(N)
H=a.dag()*a
psi0=qt.coherent(N,n**0.5)
#psi0=qt.fock(N,n)
time=np.linspace(0,100,1000)
sol=qt.mesolve(H,psi0,time,[],[])

fig,ax=plt.subplots(2,1)
xvec=np.linspace(-10,10,100)
#ax.plot(qt.expect(x,sol.states),qt.expect(p,sol.states))
line,=ax[1].plot([0],[qt.expect(H,psi0)])
im=ax[0].imshow(qt.wigner(psi0,xvec,xvec))

def updatefig(i):
    psi=sol.states[i]
    data=qt.wigner(psi,xvec,xvec)
    im.set_array(data)
    X=list(range(i))
    Y=qt.expect(x,sol.states[:i])
    line.set_data(X,Y)
    ax[1].set_xlim((0,i))
    ax[1].set_ylim((0,N))
#    ax.plot(qt.expect(x,sol.states),qt.expect(p,sol.states))
    return im,line

ani = animation.FuncAnimation(fig, updatefig,  interval=100, blit=False)
plt.show()
