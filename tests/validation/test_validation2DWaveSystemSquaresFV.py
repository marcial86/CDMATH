import cdmath
import WaveSystem2DFV
import matplotlib.pyplot as plt
import numpy as np
from math import log10, sqrt

    
def test_validation2DWaveSystemSquaresFV():
    #### 2D square mesh
    meshList=[11,51,151,201]
    nbMeshes=len(meshList)
    error_p_tab=[0]*nbMeshes
    error_u_tab=[0]*nbMeshes
    mesh_size_tab=[0]*nbMeshes
    mesh_name='meshSquareWithSquaresFV'
    diag_data_press=[0]*nbMeshes
    diag_data_vel=[0]*nbMeshes
    time_tab=[0]*nbMeshes
    resolution=100
    curv_abs=np.linspace(0,sqrt(2),resolution+1)
    plt.close('all')
    i=0
    # Storing of numerical errors, mesh sizes and diagonal values
    for nx in meshList:
        my_mesh=cdmath.Mesh(0,1,nx,0,1,nx)
        error_p_tab[i], error_u_tab[i], mesh_size_tab[i], diag_data_press[i], diag_data_vel[i], time_tab[i] =WaveSystem2DFV.solve(my_mesh,str(nx)+'x'+str(nx), resolution)
        plt.figure('pressure')
        plt.plot(curv_abs, diag_data_press[i], label= str(mesh_size_tab[i]) + ' cells')
        plt.figure('velocity')
        plt.plot(curv_abs, diag_data_vel[i],   label= str(mesh_size_tab[i]) + ' cells')
        time_tab[i]=log10(time_tab[i])
        i=i+1
    
    # Plot over diagonal line
    plt.figure('pressure')
    plt.legend()
    plt.xlabel('Position on diagonal line')
    plt.ylabel('Pressure on diagonal line')
    plt.title('Plot over diagonal line for stationary wave system \n on 2D square meshes')
    plt.savefig(mesh_name+'_Pressure_2DWaveSystemSquares_'+"PlotOverDiagonalLine.png")

    plt.close('pressure')

    plt.figure('velocity')
    plt.legend()
    plt.xlabel('Position on diagonal line')
    plt.ylabel('Velocity on diagonal line')
    plt.title('Plot over diagonal line for the stationary wave system \n on 2D square meshes')
    plt.savefig(mesh_name+"_Velocity_2DWaveSystemSquares_"+"PlotOverDiagonalLine.png")
    
    plt.close('velocity')

    # Plot of convergence curves
    plt.close()
    plt.plot(mesh_size_tab, error_p_tab, label='|error on stationary pressure|')
    plt.legend()
    plt.xlabel('number of cells')
    plt.ylabel('|error|')
    plt.title('Convergence of finite volumes \n for the stationary Wave System on 2D square meshes')
    plt.savefig(mesh_name+"_Pressure_2DWaveSystemSquares_"+"ConvergenceCurve.png")
    
    plt.close()
    plt.plot(mesh_size_tab, error_u_tab, label='log(|error on stationary velocity|)')
    plt.legend()
    plt.xlabel('number of cells')
    plt.ylabel('|error|')
    plt.title('Convergence of finite volumes \n for the stationary Wave System on 2D square meshes')
    plt.savefig(mesh_name+"_Velocity_2DWaveSystemSquares_"+"ConvergenceCurve.png")
    
    for i in range(nbMeshes):
        mesh_size_tab[i]=log10(mesh_size_tab[i])
        
    # Plot of computational time
    plt.close()
    plt.plot(mesh_size_tab, time_tab, label='log(cpu time)')
    plt.legend()
    plt.xlabel('log(number of cells)')
    plt.ylabel('log(cpu time)')
    plt.title('Computational time of finite volumes \n for the stationary Wave System on 2D square meshes')
    plt.savefig(mesh_name+"2DWaveSystemSquares_ComputationalTimeSquares.png")
    
if __name__ == """__main__""":
    test_validation2DWaveSystemSquaresFV()