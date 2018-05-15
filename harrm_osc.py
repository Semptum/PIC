#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:11:24 2018

@author: andre
"""

import numpy as np
import matplotlib.pyplot as plt
import qutip as qt
import matplotlib.animation as animation

N=30
m=1
w=1
a=qt.destroy(N)
H=a.dag()*a
psi0=(qt.fock(N,0)+qt.fock(N,1))/np.sqrt(2)
psi0=qt.coherent(N,3)-qt.coherent(N,-3)
time=np.linspace(0,30,1000)
sol=qt.mesolve(H,psi0,time,[],[])

fig,ax=plt.subplots()
xvec=np.linspace(-5,5,100)
data=np.sum(qt.wigner(psi0,xvec,xvec),axis=0)
data/=np.sum(data)
line,=ax.plot(xvec,data)
ax.set_ylim((0,0.1))

def updatefig(i):
    psi=sol.states[i]
    data=qt.wigner(psi,xvec,xvec)
    data=np.sum(data,axis=0)
    data/=np.sum(data)
    line.set_ydata(data)
    return line,

ani = animation.FuncAnimation(fig, updatefig,  interval=1, blit=False)
plt.show()
