import cdmath
import FiniteVolumes2DWithCDMATH
import matplotlib.pyplot as plt
from math import log10

##### 2D FV triangle mesh
nbMeshes=5
error_tab=[0]*nbMeshes
mesh_size_tab=[0]*nbMeshes
mesh_path='../validation/2DTriangles/'
mesh_name='meshSquareTrianglesFV'
i=0
for filename in ['triangleMeshSquare_1','triangleMeshSquare_2','triangleMeshSquare_3','triangleMeshSquare_4','triangleMeshSquare_5']:
    error_tab[i], mesh_size_tab[i] =FiniteVolumes2DWithCDMATH.solve_file(mesh_path+filename)
    error_tab[i]=log10(error_tab[i])
    mesh_size_tab[i] = log10(mesh_size_tab[i])
    i=i+1
    
plt.plot(mesh_size_tab, error_tab)
plt.xlabel('log(number of nodes)')
plt.ylabel('log(error)')
plt.title('Convergence of finite volumes for Laplace operator on a 2D triangular mesh')
plt.savefig(mesh_name+".png")
plt.close()

### 2D FV rectangular mesh
nbMeshes=4
error_tab=[0]*nbMeshes
mesh_size_tab=[0]*nbMeshes
mesh_name='meshSquareRectanglesFV'
i=0
for nx in [11,51,151,201]:
    my_mesh=cdmath.Mesh(0,1,nx,0,1,nx)
    error_tab[i], mesh_size_tab[i] =FiniteVolumes2DWithCDMATH.solve(my_mesh,str(nx)+'x'+str(nx))
    error_tab[i]=log10(error_tab[i])
    mesh_size_tab[i] = log10(mesh_size_tab[i])
    i=i+1
    
plt.plot(mesh_size_tab, error_tab)
plt.xlabel('log(number of nodes)')
plt.ylabel('log(error)')
plt.title('Convergence of finite volumes for Laplace operator on a 2D rectangular mesh')
plt.savefig(mesh_name+".png")

