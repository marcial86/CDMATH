#!/usr/bin/env python
# -*-coding:utf-8 -*

#===============================================================================================================================
# Name        : Résolution VF de l'équation du transport 1D \partial_t u + c \partial_x u = 0 avec conditions aux limites périodiques
# Author      : Michaël Ndjinga, Katia Ait Ameur
# Copyright   : CEA Saclay 2018
# Description : Utilisation de la méthode des volumes P0 avec champs u discrétisé aux cellules d'un maillage 1D régulier
#		        Création et sauvegarde du champ résultant et des figures
#================================================================================================================================


from math import sin, pi, ceil
import numpy as np
import matplotlib.pyplot as plt

import time, sys

precision=1e-5

def solve(nx,cfl,a,b, isSmooth):
    start = time.time()
    print "Transport equation, explicit scheme, nx= ", nx, " cfl= ", cfl
    ##################### Simulation parameters
    dx = (b - a) / nx #space step

    c = 0.25 # advection velocity
    tmax = (b-a)/c # runs the simulation for 0 <= t <= tMax
    dt = cfl * dx / c
    ntmax = ceil(tmax/dt)

    x=[a+0.5*dx + i*dx for i in range(nx)]   # array of cell center (1D mesh)
    
    ########################## Initial data
    if(isSmooth):
        print "Smooth initial data"
        u_initial = [ 0.5*(1+sin(4*pi*xi-pi*.5))  for xi in x];# to be used with a=0, b=1
        u = [ 0.5*(1+sin(4*pi*xi-pi*.5))  for xi in x];# to be used with a=0, b=1
    else:
        print "Stiff initial data"
        u_initial = [ int(1./3<xi)*int(xi<2./3)  for xi in x];# to be used with a=0, b=1
        u = [ int(1./3<xi)*int(xi<2./3)  for xi in x];# to be used with a=0, b=1
        
    max_initial=max(u_initial)
    min_initial=min(u_initial)
    total_var_initial = np.sum([abs(u_initial[i] - u_initial[(i-1)%nx]) for i in range(nx)])

    Time = 0.
    it = 0
    output_freq = 50

    ########################### Postprocessing initialisation
    # Picture frame
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('u')
    plt.xlim(a,b)
    plt.ylim( min_initial - 0.1*(max_initial-min_initial), max_initial +  0.1*(max_initial-min_initial) )
    plt.title('Upwind scheme for transport equation')
    line1, = plt.plot(x, u, label='u') #new picture for video # Returns a tuple of line objects, thus the comma

    plt.savefig("TransportEquation_UpwindScheme_"+str(nx)+"Cells_Smoothness"+str(isSmooth)+"ResultField_"+str(it)+".png")

    print("Saving initial data at T=0")
    np.savetxt("TransportEquation_UpwindScheme_"+str(nx)+"Cells_Smoothness"+str(isSmooth)+"ResultField_0.txt", u, delimiter="\n")

    ############################# Time loop
    while (it < ntmax and Time <= tmax):
        for i in reversed(range(nx)):
            u[i] = u[i] - c * dt / dx * (u[i] - u[(i-1)%nx])

        Time += dt
        it += 1

        # Postprocessing
        line1.set_ydata(u)
        if (it % output_freq == 0):
            print("-- Iter: " + str(it) + ", Time: " + str(Time) + ", dt: " + str(dt))
            np.savetxt( "TransportEquation_UpwindScheme_"+str(nx)+"Cells_Smoothness"+str(isSmooth)+"ResultField_"+str(it)+".txt", u, delimiter="\n")
            plt.savefig("TransportEquation_UpwindScheme_"+str(nx)+"Cells_Smoothness"+str(isSmooth)+"ResultField_"+str(it)+".png")
            #plt.show()
            pass
        pass

    if cfl<1 :
        assert max(u) <= max_initial+precision
        assert min(u) >= min_initial-precision
        assert np.sum([abs(u[i] - u[(i-1)%nx]) for i in range(nx)]) <= total_var_initial+precision

    print("Simulation of transport equation with upwind scheme done.")
    
    end = time.time()

    #return min, max, sol, total variation, l1 error and elapsed time
    return min(u), max(u), u, np.sum([abs(u[i] - u[(i-1)%nx]) for i in range(nx)]), dx*np.sum([abs(u[i] - u_initial[i]) for i in range(nx)]), end-start


if __name__ == """__main__""":
    if len(sys.argv) >3 :
        nx = int(sys.argv[1])
        cfl = float(sys.argv[2])
        isSmooth=bool(sys.argv[3])
        solve(nx,cfl,0,1,isSmooth)
    else :
        nx = 50 # number of cells
        cfl = 0.99 # c*dt/dx <= CFL
        isSmooth=True
        solve(nx,cfl,0,1,isSmooth)