import cdmath
import FiniteElements3DSphereWithCDMATH
import matplotlib.pyplot as plt
import numpy as np
from math import log10, sqrt

def test_validation3DSphereEF():
    #### 3D sphere FE triangle mesh
    meshList=['meshSphere_1','meshSphere_2','meshSphere_3','meshSphere_4','meshSphere_5']
    nbMeshes=len(meshList)
    error_tab=[0]*nbMeshes
    mesh_size_tab=[0]*nbMeshes
    time_tab=[0]*nbMeshes
    mesh_path='../../ressources/3DSphere/'
    mesh_name='meshSphereWithTrianglesFE'
    diag_data=[0]*nbMeshes
    resolution=100
    plt.close('all')
    i=0
    # Storing of numerical errors and mesh sizes
    for filename in meshList:
        error_tab[i], mesh_size_tab[i], min_sol_num, max_sol_num, time_tab[i] =FiniteElements3DSphereWithCDMATH.solve(mesh_path+filename, resolution)
        assert min_sol_num>-1.1 
        assert max_sol_num<1.1
        error_tab[i]=log10(error_tab[i])
        time_tab[i]=log10(time_tab[i])
        with open('./FiniteElementsOnSphere_PlotOnSortedLines'+str(mesh_size_tab[i])+'0.csv') as f:
            lines = f.readlines()
            x = [line.split(",")[0] for line in lines[1:]]
            y = [line.split(",")[1] for line in lines[1:]]

        plt.plot(y, x, label= str(mesh_size_tab[i]) + ' cells')
        mesh_size_tab[i] = log10(mesh_size_tab[i])
        i=i+1

    # Plot over diagonal line
    plt.legend()
    plt.xlabel('Position on slice circle')
    plt.ylabel('Value on slice circle')
    plt.title('Plot over slice circle for finite elements \n for Laplace operator on 3D sphere meshes')
    plt.savefig(mesh_name+"_3DSpherePoissonFE_Slice.png")
    
    # Least square linear regression
    # Find the best a,b such that f(x)=ax+b best approximates the convergence curve
    # The vector X=(a,b) solves a symmetric linear system AX=B with A=(a1,a2\\a2,a3), B=(b1,b2)
    a1=np.dot(mesh_size_tab,mesh_size_tab)
    a2=np.sum(mesh_size_tab)
    a3=nbMeshes
    b1=np.dot(error_tab,mesh_size_tab)   
    b2=np.sum(error_tab)
    
    det=a1*a3-a2*a2
    assert det!=0, 'test_validation3DSphereEF() : Make sure you use distinct meshes and at least two meshes'
    a=( a3*b1-a2*b2)/det
    b=(-a2*b1+a1*b2)/det
    
    print "FE on 3D sphere triangle mesh : scheme order is ", -a
    assert abs(a+0.5)<0.1

    # Plot of convergence curves
    plt.close()
    plt.plot(mesh_size_tab, error_tab, label='log(|numerical-exact|)')
    plt.plot(mesh_size_tab, a*np.array(mesh_size_tab)+b,label='least square slope : '+'%.3f' % a)
    plt.legend()
    plt.xlabel('log(number of nodes)')
    plt.ylabel('log(error)')
    plt.title('Convergence of finite elements for \n Laplace operator on 3D sphere triangular meshes')
    plt.savefig(mesh_name+"_3DSpherePoissonFE_ConvergenceCurve.png")
    
    # Plot of computational time
    plt.close()
    plt.plot(mesh_size_tab, time_tab, label='log(cpu time)')
    plt.legend()
    plt.xlabel('log(number of nodes)')
    plt.ylabel('log(cpu time)')
    plt.title('Computational time of finite elements \n for Laplace operator on 3D sphere triangular meshes')
    plt.savefig(mesh_name+"_3DSpherePoissonFE_ComputationalTime.png")
    
    plt.close('all')

if __name__ == """__main__""":
    test_validation3DSphereEF()
