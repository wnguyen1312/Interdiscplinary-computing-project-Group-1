import raytracer as rt
import numpy as np 
import matplotlib.pyplot as plt
import optimisation
import scipy.optimize as op 


def curvature(focus_lens,shape):
    # class finding_curvature(focal_point):


    # sets focus to the paraxial focus of the planoconvex lens to compare rms.
    focus_point = 198


    #setting up bound for optimisation

    rmin = 5 #has to be at least 5 cm in radius for 10 mm beam 


    #can define rmax to impose max limit on lens size if desired. 
    constraints=op.NonlinearConstraint()
    if shape=1:
        c0 = -0.02 # initial guess for the first curvature 
        c1 = 0.02 # initial guess for second curvature 
        bound = ((0,1./(rmin)),(-1./(rmin),0)) #one convex side, one concave side
    else:
        c0 = 0.02 # initial guess for the first curvature 
        c1 = -0.02 # initial guess for second curvature 
        bound = ((-1./(rmin),0),(0,1./(rmin)))


    optimum = op.minimize(optimisation.system_rms, [c0, c1], args = (100, 105,
                                        focus_point, 10 ), bounds=bound)

    optimum_curvature = optimum.x
    min_rms = optimum.fun

    # print('The optimum curvature combination is:', optimum_curvature, 'mm^-1')
    # print('The minimised RMS is:', min_rms, 'mm')
    return(optimum_curvature)        
    #Performance is better than planoconvex for 10 mm bundle 

list_curvature=[]
for i in range(10):
    if i-5<0:  
      list_curvature.append(curvature(((i)-5),0))
    else:
      list_curvature.append(curvature(((i+1)-5),1))
      
print(list_curvature)
