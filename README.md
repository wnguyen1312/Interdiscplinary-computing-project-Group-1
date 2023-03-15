# Interdiscplinary-computing-project-Group-1
This file is mainly used to describe the work done by group 1
## Introduction
This project is mainly focused on finding the optimal lens in different conditions (myopia or hyperopia) based on optimisation.

## Contribution
Writing and testing the code: William Nguyen and Jingheng Peng.
Research and poster presentation: Shreya Sridharan and Oliver Lam.

## Assumption
1. Constant refractive indicies in the material (no dispersion).
2. Geometrical ray tracing holds (investigated length >> diffraction limit) 


## Background

Hyperopia (far-sightedness) and myopia (near-sightedness) are two of the most common vision problems. They affect approximately 30% and 25% of people worldwide. They are both caused by refractive errors that affect the eye’s ability to correctly focus light at the retina, causing blurriness [1]. 
In myopia, the eye is too long or the cornea is too steep, which causes light to focus in front of the retina instead of directly on it. This results in distant objects appearing blurry while close-up objects appear clear. See figure 1 (a)
In hyperopia, the opposite occurs, where the eye is too short or the cornea is too flat, causing light to focus behind the retina instead of directly on it. This results in close-up objects appearing blurry while distant objects appear clear. (See figure 1 b)

Figure 1a: Light rays converging and being focussed in front of the retina [2]

<img width="201" alt="image" src="https://user-images.githubusercontent.com/124576025/224732571-17949069-9340-4fe8-9e60-039f44c63863.png">

Figure 1b:Light converging and being focused behind the retina [2]

<img width="202" alt="image" src="https://user-images.githubusercontent.com/124576025/224732044-551e80df-1fa1-4161-bc7a-ce438433c88e.png">


Risk factors for both include age, genetics, and other underlying health conditions. Both can be treated using refractive surgery or orthokeratology; however, the most common method is using corrective lens in the form of glasses or contact lens. The lenses work by changing the way that light is refracted as it enters the eye, allowing it to focus directly on the retina. See Figure 2 and 3

Figure 2: How hyperopia is corrected using a converging lens [2]

 <img width="251" alt="image" src="https://user-images.githubusercontent.com/124576025/224732127-ebd3fc2a-5814-4ab2-95bb-eda8056f6b09.png">

Figure 3: How myopia is corrected using a diverging lens [2]

<img width="249" alt="image" src="https://user-images.githubusercontent.com/124576025/224732185-53668852-ffb2-4165-be48-e9af74688d53.png">

The different parameters important for the lens are curvature, thickness and refractive index. 

Spherical lens can suffer from spherical aberrations if the rays are not paraxial. Aberrations mean that highly deviated rays (i.e not paraxial) do not focus at the expected focal points. One way to counter this is through the use of adaptive optics, which involves essentially deforming the original spherical shapes. In terms of optimisation, we would measure the level of aberrations with the RMS spot size. The smaller the RMS spot size, the more focus your image is. The RMS spot size is found by tracing multiple rays through the system and working out the associated RMS value. Then, we will use some optimising routine from Scipy to obtain the deformation parameters to obtain the minimum RMS spot size. For a large number of parameters (I.e multiple lens / imaging system), we want to use the Nelder-Mead method, which is more robust as it is not gradient based. 



## Overview of the code

Date: 15/03/2023

By: William Nguyen, Oliver Lam, Shreya Sridharan, Jingheng Peng


Written and tested in Python 3.7

----- GETTING STARTED -----

- import the classes and functions from the raytracer.py and optimisation.py

- set up an optical system, which can consist of SphericalRefraction, AsphericRefraction and OutputPlane objects 

- use propagate_ray method to trace rays or a collimated beam

- visualise the results with MatplotLib 

- For more detailed instruction, see example.py file 


----- MODULES -----

- raytracer.py contains the classes and functions required to model ray tracing

- optimisation.py contains the methods to calculate RMS of different optical systems  


----- SCRIPTS ------

- example.py contains the example script on how to get started with the optical ray tracer

- unit_test.py contains the script to check the operations of classes and functions

- aspheric_surface_testing contains the unit tests for aspheric surface. 

- ray_tracing_investigation.py contains the script to perform Task 12 - 15 of the project.

- biconvex_lens_optimisation.py contains the script to perform the lens optimisation task. 

- aspheric_surface_optimisation contains the script to optimise plano-convex and bi-convex lens with adaptive optics. 

----- Sample outputs ------

![image](https://user-images.githubusercontent.com/108578700/219814286-fde14aa4-b052-422d-815a-0b13db0174c9.png)
![image](https://user-images.githubusercontent.com/108578700/219814376-fd9c6e48-d803-4039-8b86-1ca779cd57b5.png)
![image](https://user-images.githubusercontent.com/108578700/219814409-d29f64f4-7025-4257-bdd6-0b04eeb177af.png)



## References

[1]: "Facts About Refractive Errors". NEI. October 2010. Archived from the original on 28 July 2016. Retrieved 30 July 2016 

[2] https://courses.lumenlearning.com/suny-physics/chapter/26-2-vision-correction/ [accessed on 27th February 2023] 
