#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

File to input patient's information and output the optimal lens design

Created on Wed Mar 15 14:26:10 2023

@author: williamnguyen
"""

patient_power = int(input("Please enter the patients refractive power in dioptre"))


focal_length = 1/patient_power * 1000 #in mm 

#Optimisation procedure 


import optimisation 
import scipy.optimize as op 
import convergence 
import warnings

warnings.filterwarnings("ignore") 


c0 = 0.02 # initial guess for the first curvature 
c1 = -0.02 # initial guess for second curvature 


focus_point = 198 #distance between retina and lens is roughly 2 mm  


#setting up bound for optimisation

rmin = 5 #has to be at least 5 cm in radius for 10 mm beam 


#can define rmax to impose max limit on lens size if desired. 


bound = ((0,1./(rmin)),(-1./(rmin),0)) #one convex side, one concave side

def focal_length_constraint(C):
  """ 
  FUNCTION THAT CONSTRAINTS THE CURVATURE OF THE LENS TO MATCH THE 
  PATIENT'S POWER 
  
  Input
  -----
  
   
  Output
  ------
  
  1/c0 + 1/c1 - 1/focal_length: if zero then constraint is met 
  """    
  c0, c1 = C
  return 1/c0 + 1/c1 - 1/focal_length 


constraints = {'type': 'eq', 'fun': focal_length_constraint}

ros_sim = convergence.Simulator(optimisation.system_rms)

optimum = op.minimize(ros_sim.simulate, [c0, c1], args = (100, 106,
                                     focus_point, 10 ), bounds=bound, 
                      constraints = constraints,
                      callback=ros_sim.callback,
                      method = 'TNC')

optimum_curvature = optimum.x
min_rms = optimum.fun

print('The optimum curvature combination is:', optimum_curvature
      , 'mm^-1')
print('The minimised RMS is:', min_rms, 'mm')

        
