#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plotting script to investigate convergence of optimisation 
Created on Wed Mar 15 17:52:31 2023

@author: williamnguyen
"""
import numpy as np 
import matplotlib.pyplot as plt 

c1, c2, objective = np.loadtxt('/Users/williamnguyen/Desktop/University/Y2/optical ray tracer/convergence_1.txt',
                                  unpack=True)


c1_2, c2_2, objective_2 = np.loadtxt('/Users/williamnguyen/Desktop/University/Y2/optical ray tracer/convergence_2.txt',
                                  unpack=True)

c1_3, c2_3, objective_3 = np.loadtxt('/Users/williamnguyen/Desktop/University/Y2/optical ray tracer/convergence_3.txt',
                                  unpack=True)

residue_1 = np.abs(objective - objective[-1])
residue_2 = np.abs(objective_2 - objective_2[-1])
residue_3 = np.abs(objective_3 - objective_3[-1])


plt.plot(residue_1, label = 'L-BFGS-B. # iteration = 11' )
plt.plot(residue_2, label = 'Nelder-Mead. # iteration = 24' )
plt.plot(residue_3, label = 'TNC. # iteration = 11' )
plt.legend()
plt.xlabel('Number of iterations')
plt.ylabel('Residue (objective - optimised value)')
plt.savefig('convergence_compare.png', dpi=500)

