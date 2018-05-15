#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:16:47 2018

@author: andre
"""

import numpy as np
import matplotlib.pyplot as plt
import qutip as qt
import matplotlib.animation as animation

N=2
ket0=qt.fock(N,0)
ket1=qt.fock(N,1)

time=np.linspace(0,100,1000)
sol=qt.mcsolve(H,psi0,time,[a*0.25,a.dag()*0.1],[H,qt.position(N),qt.momentum(N)],1)
