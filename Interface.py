#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

File to input patient's information and output the optimal lens design

Created on Wed Mar 15 14:26:10 2023

@author: williamnguyen
"""
import optimisation 
import scipy.optimize as op 
import convergence 
import warnings
import matplotlib.pyplot as plt
import numpy as np

def caculate(n,shape,In2=1.5618):
  patient_power = n # dipotre
  In2=In2

  focal_length = 1/patient_power * 1000 # in mm 


  #Optimisation procedure 


  warnings.filterwarnings("ignore") 


#  c0 = 0.02 # initial guess for the first curvature 
#  c1 = -0.02 # initial guess for second curvature 


  focus_point = 198 #distance between retina and lens is roughly 2 mm  


  #setting up bound for optimisation

  rmin = 5 #has to be at least 5 cm in radius for 10 mm beam 


  #can define rmax to impose max limit on lens size if desired. 
  if shape==1:
      c0 = 0.02 # initial guess for the first curvature 
      c1 = -0.02 # initial guess for second curvature 
      bound = ((0,1./(rmin)),(-1./(rmin),0)) #one convex side, one concave side
  else:
      c0 = -0.02 # initial guess for the first curvature 
      c1 = 0.02 # initial guess for second curvature 
      bound = ((-1./(rmin),0),(0,1./(rmin)))

#   bound = ((0,1./(rmin)),(-1./(rmin),0)) #one convex side, one concave side

  def focal_length_constraint(C,shape_0=shape):
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
    if shape_0==0:
      return 1/c0+1/c1+1/focal_length
    else:
      return 1/c0+1/c1-1/focal_length


  constraints = {'type': 'eq', 'fun': focal_length_constraint}

  # ros_sim = convergence.Simulator(optimisation.system_rms)

  optimum = op.minimize(optimisation.system_rms, [c0, c1], args = (100, 106,
                                      focus_point, 10,1 ,In2), bounds=bound, constraints=constraints)

  optimum_curvature = optimum.x
  min_rms = optimum.fun

  # print('The optimum curvature combination is:', optimum_curvature, 'mm^-1')
  # print('The minimised RMS is:', min_rms, 'mm')
  return(optimum_curvature)

def weight_of_glasses(ind,dens):
    index=ind
    density=dens
    list_curvature1=[]
    list_curvature2=[]
    list_curvature3=[]
    list_curvature4=[]
    list_degree=[]
    list_degree2=[]
    weight1=[]
    weight2=[]
    for i in range(10): 
          list_curvature1.append(caculate((-i-1),0,In2=index)[0])
          list_curvature2.append(caculate((-i-1),0,In2=index)[1])
          list_curvature3.append(caculate(i+1,1,In2=index)[0])
          list_curvature4.append(caculate(i+1,1,In2=index)[1])
          list_degree.append(-i-1)
          list_degree2.append(i+1)

    #print(list_curvature)
    area=np.multiply(np.abs(list_curvature1)+np.abs(list_curvature2),np.pi)
    area2=np.multiply(np.abs(list_curvature3)+np.abs(list_curvature4),np.pi)
    weight1=np.multiply(area,density)
    weight2=np.multiply(area2,density)
    return(weight1,weight2)

W1=weight_of_glasses(1.5618,2.5) #weight of glass
W2=weight_of_glasses(1.52,1.32) #weight of CR-39
W3=weight_of_glasses(1.597,1.34) #weight of 1.60MR-6
'''
plt.plot(list_curvature1)
plt.xlabel("patient's power")
print(list_curvature1)
plt.show()
plt.plot(list_curvature2)
print(list_curvature2)
plt.show()
plt.plot(list_curvature3)
print(list_curvature3)
plt.show()
plt.plot(list_curvature4)
print(list_curvature4)
plt.show()
'''
list_degree=np.arange(1,11).tolist()
list_degree2=np.arange(1,11).tolist()
fig,ax1=plt.subplots()
p1,=ax1.plot(list_degree,W1[1],color='g',label='weight of glass')
ax2=ax1.twinx()
p2,=ax2.plot(list_degree,W2[1],color='b',label='weight of CR-39')
ax3=ax1.twinx()
p3,=ax3.plot(list_degree,W3[1],color='r',label='weight of 1.60MR-6')
ax3.spines['right'].set_position(('outward',40))
ax1.legend(['weight of glass','weight of CR-39','weight of 1.60MR-6'])
plt.xlabel("degree of myopia")
plt.ylabel("weight of the glasses")
plt.grid()
ax1.legend(handles=[p1,p2,p3])
plt.show()
fig,ax1=plt.subplots()
p1,=ax1.plot(list_degree2,W1[0],color='g',label='weight of glass')
ax2=ax1.twinx()
p2,=ax2.plot(list_degree2,W2[0],color='b',label='weight of CR-39')
ax3=ax1.twinx()
p3,=ax3.plot(list_degree2,W3[0],color='r',label='weight of 1.60MR-6')
ax3.spines['right'].set_position(('outward',40))
plt.xlabel("degree of hyperopia")
plt.ylabel("weight of the glasses")
plt.grid()
ax1.legend(handles=[p1,p2,p3])
plt.show()
plt.plot(list_degree2,W1[0],label='weight of glass')
plt.plot(list_degree2,W2[0],label='weight of CR-39')
plt.plot(list_degree2,W3[0],label='weight of 1.60MR-6')
plt.xlabel("degree of myopia")
plt.ylabel("weight of the glasses")
plt.grid()
plt.legend()
plt.show()
plt.plot(list_degree2,W1[0],label='weight of glass')
plt.plot(list_degree2,W2[0],label='weight of CR-39')
plt.plot(list_degree2,W3[0],label='weight of 1.60MR-6')
plt.xlabel("degree of hyperopia")
plt.ylabel("weight of the glasses")
plt.grid()
plt.legend()
plt.show()