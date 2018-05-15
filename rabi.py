#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 01:37:02 2018

@author: andre
"""

import numpy as np
import matplotlib.pyplot as plt
import qutip as qt
import matplotlib.animation as animation

N=2
delta=0.1
epsilon=1

sx=qt.sigmax()
sy=qt.sigmay()
sz=qt.sigmaz()
sm=qt.sigmam()
sp=qt.sigmap()

H=1/2*(delta*sx+epsilon*sz)

TIME=np.linspace(0,100,1000)

g=qt.basis(N,0)
e=qt.basis(N,1)

psi0=(g+e)/np.sqrt(2)

sol=qt.mesolve(H,psi0,TIME,[sx*0.2],[sx,sy,sz])