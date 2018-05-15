#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 01:11:02 2018

@author: andre
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import qutip as qt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig,azim=-40,elev=30)
sphere = qt.Bloch(axes=ax)


psi0=qt.basis(2,1)
H=qt.sigmax()
time=np.linspace(0,10,100)
sol=qt.mesolve(H,psi0,time,[qt.sigmay()*0.1],[])


def animate(i):
    sphere.clear()
    sphere.add_states(sol.states[i])
    sphere.make_sphere()
    return ax,

def init():
    sphere.vector_color = ['r']
    return ax,

ani = animation.FuncAnimation(fig, animate,init_func=init, blit=False, repeat=False)
