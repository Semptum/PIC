#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 09:41:58 2018

@author: andre
"""

from qutip import *
import matplotlib.pyplot as plt
import numpy as np


N=20

TIME=np.linspace(0,5,1000)

omega=3

a=destroy(N)
H_os=omega * (a.dag()*a)

psi0=(fock(N,5)+fock(N,4))/np.sqrt(2)

x=position(N)
p=momentum(N)

psi0=(coherent(N,2.236)+coherent(N,-2.236))/np.sqrt(2)
#psi0=coherent(N,2.236)
#psi0=fock(N,5)
#
sol=mesolve(H_os,psi0,TIME,[a,0.5*a.dag()],[])

#fig,ax=plt.subplots()
#
#fig.set_size_inches(4,3)
#
#ax.plot(sol.times,sol.expect[0],label="Position")
#ax.plot(sol.times,sol.expect[1],label="Moment")
#
#ax.set_xlabel("Temps")
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles, labels)
#fig.tight_layout()
#fig.savefig("Sum_coherent.png")

#psi0=coherent(N,2.236)
fig,ax=plt.subplots()

fig.set_size_inches(4,3)
S=[entropy.entropy_vn(i) for i in sol.states]
ax.plot(sol.times,S)
ax.set_xlabel("Temps")
ax.set_ylabel("Entropie de Von Neumann")
fig.tight_layout()
fig.savefig("Entropy.png")




#sx=sigmax()
#sy=sigmay()
#sz=sigmaz()
#
#H_q=-omega*sz
#
#
#g=fock(2,0)
#e=fock(2,1)
#
#L1=(1j*sy+sx+sz+1)/2
#L2=sz
#
#psi0=(g+e)/np.sqrt(2)
#
#sol=mcsolve(H_q,psi0,TIME,[L2],[sx,sy,sz],100)
#
#fig,ax=plt.subplots()
#fig.set_size_inches(4,3)
#
#
#plt.plot(sol.times,sol.expect[0],label="Axe x")
#plt.plot(sol.times,sol.expect[1],label="Axe y")
#plt.plot(sol.times,sol.expect[2],label="Axe z")
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles, labels)
#ax.set_xlabel("Temps")
#fig.tight_layout()
#fig.savefig("U_Qubit_deco2_100.png")

