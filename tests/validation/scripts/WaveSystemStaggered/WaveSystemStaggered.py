#!/usr/bin/env python
# -*-coding:utf-8 -*

from math import sin, cos, pi
import time, json
import cdmath
import PV_routines
import VTK_routines

test_desc={}

rho0=1000.#reference density
c0=1500.#reference sound speed
p0=rho0*c0*c0#reference pressure
precision=1e-5

def initial_conditions_wave_system_staggered(my_mesh):
    test_desc["Initial_data"]="Constant pressure, divergence free velocity"
    
    dim     = my_mesh.getMeshDimension()
    nbCells = my_mesh.getNumberOfCells()
    nbFaces = my_mesh.getNumberOfFaces()

    pressure_field = cdmath.Field("Pressure",            cdmath.CELLS, my_mesh, 1)
    velocity_field = cdmath.Field("Velocity",            cdmath.FACES, my_mesh, 1)

    for i in range(nbCells):
        Ci=my_mesh.getCell(i)
        x = Ci.x()
        y = Ci.y()

        pressure_field[i] = p0
        
    for i in range(nbFaces):
        Fi=my_mesh.getFace(i)
        x = Fi.x()
        y = Fi.y()
        #We take only the normal component of the velocity on a cartesian grid
        #Warning : boundary values should be the same for left and right as well as top and down (front and back in 3D) boundaries
        if(dim==2):
            if abs(abs(Fi.xN) -1) < eps :
                velocity_field[i] =  sin(pi*x)*cos(pi*y) 
            elif abs(abs(Fi.yN) -1) < eps :
                velocity_field[i] = -sin(pi*y)*cos(pi*x)
            else :
                raise ValueError("initial_conditions_wave_system_staggered: the 2D mesh should be structured");
        if(dim==3):
            z = my_mesh.getCell(i).z()
            if abs(abs(Fi.xN) -1) < eps :
                velocity_field[i] =    sin(pi*x)*cos(pi*y)*cos(pi*z)
            elif abs(abs(Fi.yN) -1) < eps :
                velocity_field[i] =    sin(pi*y)*cos(pi*x)*cos(pi*z)
            elif abs(abs(Fi.zN) -1) < eps :
                velocity_field[i] = -2*sin(pi*z)*cos(pi*x)*cos(pi*y)
            else :
                raise ValueError("initial_conditions_wave_system_staggered: the 3D mesh should be structured");
        
    return pressure_field, velocity_field
    
def computeDivergenceMatrix(my_mesh,nbVoisinsMax,dt,scaling):
    nbCells = my_mesh.getNumberOfCells()
    dim=my_mesh.getMeshDimension()
    nbComp=dim+1

    if(!my_mesh.isStructured()):
        raise ValueError("WaveSystemStaggered: the mesh should be structured");

    NxNyNz=my_mesh.getCellGridStructure()
    DxDyDz=my_mesh.getDXYZ()
    
    implMat=cdmath.SparseMatrixPetsc(nbCells*nbComp,nbCells*nbComp,(nbVoisinsMax+1)*nbComp)

    idMoinsJacCL=cdmath.Matrix(nbComp)
    
    if( dim == 1) :    
        nx=NxNyNz[0]
        dx=DxDyDz[0]
            
        if( scaling==0 ):
            for k in range(nbCells):
                implMat.insertValue(k,1*nbCells +  k      , -c0*c0/dx)
                implMat.insertValue(k,1*nbCells + (k+1)%nx,  c0*c0/dx)
    
                implMat.insertValue(  1*nbCells +  k      ,k,  1/dx)
                implMat.insertValue(  1*nbCells + (k+1)%nx,k, -1/dx)
        else : # scaling >0    
            for k in range(nbCells):
                implMat.insertValue(k,1*nbCells +  k      , -c0/dx)
                implMat.insertValue(k,1*nbCells + (k+1)%nx,  c0/dx)
    
                implMat.insertValue(  1*nbCells +  k      ,k,  c0/dx)
                implMat.insertValue(  1*nbCells + (k+1)%nx,k, -c0/dx)
    
    elif( dim == 2) :# k = j*nx+i
        nx=NxNyNz[0]
        ny=NxNyNz[1]
        dx=DxDyDz[0]
        dy=DxDyDz[1]
                
        if( scaling==0 ):
            for k in range(nbCells):
                i = k % nx
                j = k //nx
    
                implMat.insertValue(k,1*nbCells + j*nx +  i      ,   -c0*c0/dx)
                implMat.insertValue(k,1*nbCells + j*nx + (i+1)%nx,    c0*c0/dx)
    
                implMat.insertValue(k,2*nbCells +   j       *nx + i, -c0*c0/dy)
                implMat.insertValue(k,2*nbCells + ((j+1)%ny)*nx + i,  c0*c0/dy)
    
                implMat.insertValue(  1*nbCells + j*nx +  i      ,  k,  1/dx)
                implMat.insertValue(  1*nbCells + j*nx + (i+1)%nx,  k, -1/dx)
    
                implMat.insertValue(  2*nbCells +   j       *nx + i,k,  1/dy)
                implMat.insertValue(  2*nbCells + ((j+1)%ny)*nx + i,k, -1/dy)
    
        else :# scaling >0
            for k in range(nbCells):
                i = k % nx
                j = k //nx
    
                implMat.insertValue(k,1*nbCells + j*nx +  i      ,   -c0/dx)
                implMat.insertValue(k,1*nbCells + j*nx + (i+1)%nx,    c0/dx)
    
                implMat.insertValue(k,2*nbCells +   j       *nx + i, -c0/dy)
                implMat.insertValue(k,2*nbCells + ((j+1)%ny)*nx + i,  c0/dy)
    
                implMat.insertValue(  1*nbCells + j*nx +  i      ,  k,  c0/dx)
                implMat.insertValue(  1*nbCells + j*nx + (i+1)%nx,  k, -c0/dx)
    
                implMat.insertValue(  2*nbCells +   j       *nx + i,k,  c0/dy)
                implMat.insertValue(  2*nbCells + ((j+1)%ny)*nx + i,k, -c0/dy)
    
    elif( dim == 3) :# k = l*nx*ny+j*nx+i
        nx=NxNyNz[0]
        ny=NxNyNz[1]
        nz=NxNyNz[2]
        dx=DxDyDz[0]
        dy=DxDyDz[1]
        dz=DxDyDz[2]
                
        if( scaling==0 ):
            for k in range(nbCells):
                i =  k % nx
                j = (k //nx)%ny 
                l =  k //(nx*ny)
                
                implMat.insertValue(k,1*nbCells + l*nx*ny + j*nx +  i      ,  -c0*c0/dx)
                implMat.insertValue(k,1*nbCells + l*nx*ny + j*nx + (i+1)%nx,   c0*c0/dx)
    
                implMat.insertValue(k,2*nbCells + l*nx*ny +   j       *nx + i, -c0*c0/dy)
                implMat.insertValue(k,2*nbCells + l*nx*ny + ((j+1)%ny)*nx + i,  c0*c0/dy)
    
                implMat.insertValue(k,3*nbCells +   l*nx*ny        + j*nx + i, -c0*c0/dz)
                implMat.insertValue(k,3*nbCells + ((l+1)%nz)*nx*ny + j*nx + i,  c0*c0/dz)
    
                implMat.insertValue(  1*nbCells + l*nx*ny + j*nx +  i      ,  k,  1/dx)
                implMat.insertValue(  1*nbCells + l*nx*ny + j*nx + (i+1)%nx,  k, -1/dx)
    
                implMat.insertValue(  2*nbCells + l*nx*ny +   j       *nx + i,k,  1/dy)
                implMat.insertValue(  2*nbCells + l*nx*ny + ((j+1)%ny)*nx + i,k, -1/dy)
    
                implMat.insertValue(  3*nbCells +   l*nx*ny        + j*nx + i,k,  1/dz)
                implMat.insertValue(  3*nbCells + ((l+1)%nz)*nx*ny + j*nx + i,k, -1/dz)

        else:# scaling >0
            for k in range(nbCells):
                i =  k % nx
                j = (k //nx)%ny 
                l =  k //(nx*ny)
                
                implMat.insertValue(k,1*nbCells + l*nx*ny + j*nx +  i      ,  -c0/dx)
                implMat.insertValue(k,1*nbCells + l*nx*ny + j*nx + (i+1)%nx,   c0/dx)
    
                implMat.insertValue(k,2*nbCells + l*nx*ny +   j       *nx + i, -c0/dy)
                implMat.insertValue(k,2*nbCells + l*nx*ny + ((j+1)%ny)*nx + i,  c0/dy)
    
                implMat.insertValue(k,3*nbCells +   l*nx*ny        + j*nx + i, -c0/dz)
                implMat.insertValue(k,3*nbCells + ((l+1)%nz)*nx*ny + j*nx + i,  c0/dz)
    
                implMat.insertValue(  1*nbCells + l*nx*ny + j*nx +  i      ,  k,  c0/dx)
                implMat.insertValue(  1*nbCells + l*nx*ny + j*nx + (i+1)%nx,  k, -c0/dx)
    
                implMat.insertValue(  2*nbCells + l*nx*ny +   j       *nx + i,k,  c0/dy)
                implMat.insertValue(  2*nbCells + l*nx*ny + ((j+1)%ny)*nx + i,k, -c0/dy)
    
                implMat.insertValue(  3*nbCells +   l*nx*ny        + j*nx + i,k,  c0/dz)
                implMat.insertValue(  3*nbCells + ((l+1)%nz)*nx*ny + j*nx + i,k, -c0/dz)

    return dt*implMat

def WaveSystemStaggered(ntmax, tmax, cfl, my_mesh, output_freq, meshName, resolution,scaling):
    dim=my_mesh.getMeshDimension()
    nbCells = my_mesh.getNumberOfCells()
    
    dt = 0.
    time = 0.
    it=0;
    isStationary=False;
    
    nbVoisinsMax=my_mesh.getMaxNbNeighbours(CELLS)
    iterGMRESMax=50
    
    #iteration vectors
    Un =cdmath.Vector(nbCells*(dim+1))
    dUn=cdmath.Vector(nbCells*(dim+1))
    
    # Initial conditions #
    print("Construction of the initial data …")
    pressure_field, velocity_field = initial_conditions_wave_system_staggered(my_mesh)
    initial_pressure, initial_velocity = initial_conditions_wave_system_staggered(my_mesh)

    for k in range(nbCells):
        Un[k + 0*nbCells] =      initial_pressure[k]
        Un[k + 1*nbCells] = rho0*initial_velocity[k,0]
        Un[k + 2*nbCells] = rho0*initial_velocity[k,1]
        if(dim==3):
            Un[k + 3*nbCells] = rho0*initial_velocity[k,2]
    if( scaling>0):
        Vn = Un.deepCopy()
        for k in range(nbCells):
            Vn[k] = Vn[k]/c0
            
    #sauvegarde de la donnée initiale
    pressure_field.setTime(time,it);
    pressure_field.writeVTK("WaveSystem"+str(dim)+"DStaggered"+meshName+"_pressure");
    velocity_field.setTime(time,it);
    velocity_field.writeVTK("WaveSystem"+str(dim)+"DStaggered"+meshName+"_velocity");
    #Postprocessing : save 2D picture
    PV_routines.Save_PV_data_to_picture_file("WaveSystem"+str(dim)+"DStaggered"+meshName+"_pressure"+'_0.vtu',"Pressure",'CELLS',"WaveSystem"+str(dim)+"DStaggered"+meshName+"_pressure_initial")
    PV_routines.Save_PV_data_to_picture_file("WaveSystem"+str(dim)+"DStaggered"+meshName+"_velocity"+'_0.vtu',"Velocity",'CELLS',"WaveSystem"+str(dim)+"DStaggered"+meshName+"_velocity_initial")

    total_pressure_initial=pressure_field.integral()#For conservation test later
    total_velocity_initial=velocity_field.integral()#For conservation test later
    
    dx_min=my_mesh.minRatioVolSurf()

    dt = cfl * dx_min / c0
    divMat=computeDivergenceMatrix(my_mesh,nbVoisinsMax,dt,scaling)

    #Add the identity matrix on the diagonal
    divMat.diagonalShift(1)#only after  filling all coefficients

    if( scaling==0):
        LS=cdmath.LinearSolver(divMat,Un,iterGMRESMax, precision, "GMRES","ILU")
    else:
        LS=cdmath.LinearSolver(divMat,Vn,iterGMRESMax, precision, "GMRES","ILU")
    LS.setComputeConditionNumber()

    test_desc["Linear_solver_algorithm"]=LS.getNameOfMethod()
    test_desc["Linear_solver_preconditioner"]=LS.getNameOfPc()
    test_desc["Linear_solver_precision"]=LS.getTolerance()
    test_desc["Linear_solver_maximum_iterations"]=LS.getNumberMaxOfIter()
    test_desc["Numerical_parameter_space_step"]=dx_min
    test_desc["Numerical_parameter_time_step"]=dt
    test_desc["Linear_solver_with_scaling"]=scaling

    test_desc['Linear_system_max_actual_iterations_number']=0
    test_desc["Linear_system_max_actual_error"]=0
    test_desc["Linear_system_max_actual_condition number"]=0

    print("Starting computation of the linear wave system with a pseudo staggered scheme …")
    
    # Starting time loop
    while (it<ntmax and time <= tmax and not isStationary):
        dUn=Un.deepCopy()
        if( scaling==0):
            LS.setSndMember(Un)
            Un=LS.solve()
        else:#( scaling > 0)
            LS.setSndMember(Vn)
            Vn=LS.solve()
            Un = Vn.deepCopy()
            for k in range(nbCells):
                Un[k] = c0*Vn[k]
            
        if(not LS.getStatus()):
            print "Linear system did not converge ", iterGMRES, " GMRES iterations"
            raise ValueError("Pas de convergence du système linéaire");
        dUn-=Un
        
        test_desc["Linear_system_max_actual_iterations_number"]=max(LS.getNumberOfIter(),test_desc["Linear_system_max_actual_iterations_number"])
        test_desc["Linear_system_max_actual_error"]=max(LS.getResidu(),test_desc["Linear_system_max_actual_error"])
        test_desc["Linear_system_max_actual_condition number"]=max(LS.getConditionNumber(),test_desc["Linear_system_max_actual_condition number"])

        maxVector=dUn.maxVector(dim+1)
        isStationary= maxVector[0]/p0<precision and maxVector[1]/rho0<precision and maxVector[2]/rho0<precision;
        if(dim==3):
            isStationary=isStationary and maxVector[3]/rho0<precision
        time=time+dt;
        it=it+1;
    
        #Sauvegardes
        if(it%output_freq==0 or it>=ntmax or isStationary or time >=tmax):
            print"-- Iter: " + str(it) + ", Time: " + str(time) + ", dt: " + str(dt)
            print "Variation temporelle relative : pressure ", maxVector[0]/p0 ,", velocity x", maxVector[1]/rho0 ,", velocity y", maxVector[2]/rho0
            print "Linear system converged in ", LS.getNumberOfIter(), " GMRES iterations"

            delta_press=0
            delta_v=cdmath.Vector(dim)
            for k in range(nbCells):
                pressure_field[k]=Un[k*(dim+1)+0]
                velocity_field[k,0]=Un[k*(dim+1)+1]/rho0
                if(dim>1):
                    velocity_field[k,1]=Un[k*(dim+1)+2]/rho0
                    if(dim>2):
                        velocity_field[k,2]=Un[k*(dim+1)+3]/rho0
                if (abs(initial_pressure[k]-pressure_field[k])>delta_press):
                    delta_press=abs(initial_pressure[k]-pressure_field[k])
                if (abs(initial_velocity[k,0]-velocity_field[k,0])>delta_v[0]):
                    delta_v[0]=abs(initial_velocity[k,0]-velocity_field[k,0])
                if (abs(initial_velocity[k,1]-velocity_field[k,1])>delta_v[1]):
                    delta_v[1]=abs(initial_velocity[k,1]-velocity_field[k,1])
                if(dim==3):
                    if (abs(initial_velocity[k,2]-velocity_field[k,2])>delta_v[2]):
                        delta_v[2]=abs(initial_velocity[k,2]-velocity_field[k,2])
                
            pressure_field.setTime(time,it);
            pressure_field.writeVTK("WaveSystem"+str(dim)+"DStaggered"+meshName+"_pressure",False);
            velocity_field.setTime(time,it);
            velocity_field.writeVTK("WaveSystem"+str(dim)+"DStaggered"+meshName+"_velocity",False);

            print "Ecart au stationnaire exact : error_p= ",delta_press/p0," error_||u||= ",delta_v.maxVector()[0]
            print
    print"-- Iter: " + str(it) + ", Time: " + str(time) + ", dt: " + str(dt)
    print "Variation temporelle relative : pressure ", maxVector[0]/p0 ,", velocity x", maxVector[1]/rho0 ,", velocity y", maxVector[2]/rho0
    print

    if(it>=ntmax):
        print "Nombre de pas de temps maximum ntmax= ", ntmax, " atteint"
        raise ValueError("Maximum number of time steps reached : Stationary state not found !!!!!!!")
    elif(isStationary):
        print "Régime stationnaire atteint au pas de temps ", it, ", t= ", time
        assert (total_pressure_initial-pressure_field.integral()).norm()/p0<precision
        #print (total_velocity_initial-velocity_field.integral()).norm()/velocity_field.normL1().norm(), precision
        assert (total_velocity_initial-velocity_field.integral()).norm()/velocity_field.normL1().norm()<precision
        print "------------------------------------------------------------------------------------"

        pressure_field.setTime(time,0);
        pressure_field.writeVTK("WaveSystem"+str(dim)+"DStaggered"+meshName+"_pressure_Stat");
        velocity_field.setTime(time,0);
        velocity_field.writeVTK("WaveSystem"+str(dim)+"DStaggered"+meshName+"_velocity_Stat");

        #Postprocessing : Extraction of the diagonal data
        if(dim==2):
            diag_data_press=VTK_routines.Extract_field_data_over_line_to_numpyArray(pressure_field,[0,1,0],[1,0,0], resolution)    
            diag_data_vel  =VTK_routines.Extract_field_data_over_line_to_numpyArray(velocity_field,[0,1,0],[1,0,0], resolution)    
        elif(dim==3):
            diag_data_press=VTK_routines.Extract_field_data_over_line_to_numpyArray(pressure_field,[0,0,0],[1,1,1], resolution)    
            diag_data_vel  =VTK_routines.Extract_field_data_over_line_to_numpyArray(velocity_field,[0,0,0],[1,1,1], resolution)    
        #Postprocessing : save 2D picture
        PV_routines.Save_PV_data_to_picture_file("WaveSystem"+str(dim)+"DStaggered"+meshName+"_pressure_Stat"+'_0.vtu',"Pressure",'CELLS',"WaveSystem"+str(dim)+"DStaggered"+meshName+"_pressure_Stat")
        PV_routines.Save_PV_data_to_picture_file("WaveSystem"+str(dim)+"DStaggered"+meshName+"_velocity_Stat"+'_0.vtu',"Velocity",'CELLS',"WaveSystem"+str(dim)+"DStaggered"+meshName+"_velocity_Stat")
        
        return delta_press/p0, delta_v.maxVector()[0], nbCells, time, it, velocity_field.getNormEuclidean().max(), diag_data_press, diag_data_vel,test_desc["Linear_system_max_actual_condition number"]
    else:
        print "Temps maximum Tmax= ", tmax, " atteint"
        raise ValueError("Maximum time reached : Stationary state not found !!!!!!!")


def solve(my_mesh,meshName,resolution,scaling, meshType, testColor,cfl):
    start = time.time()
    test_desc["Mesh_type"]=meshType
    test_desc["Test_color"]=testColor
    test_name="Resolution of the Wave system in dimension " +str( my_mesh.getMeshDimension())+" on "+str(my_mesh.getNumberOfCells())+ " cells"
    test_name_comment="New scheme for low Mach flows"
    test_model="Wave system"
    if(scaling==0):
        test_method="Staggered without scaling"
    else:    
        test_method="Staggered with scaling"
    test_initial_data="Constant pressure, divergence free velocity"
    test_bc="Periodic"
    print test_name
    print "Numerical method : ", test_method
    print "Initial data : ", test_initial_data
    print "Boundary conditions : ",test_bc
    print "Mesh name : ",meshName , ", ", my_mesh.getNumberOfCells(), " cells"
    if( scaling>0):
        print "Use of scaling strategy for a better preconditioning"

    # Problem data
    tmax = 1000.
    ntmax = 10000
    output_freq = 1000

    error_p, error_u, nbCells, t_final, ndt_final, max_vel, diag_data_press, diag_data_vel, cond_number = WaveSystemStaggered(ntmax, tmax, cfl, my_mesh, output_freq, meshName, resolution,scaling)
    end = time.time()

    test_desc["Global_name"]=test_name
    test_desc["Global_comment"]=test_name_comment
    test_desc["PDE_model"]=test_model
    test_desc["PDE_is_stationary"]=False
    test_desc["PDE_search_for_stationary_solution"]=True
    test_desc["Numerical_method_name"]=test_method
    test_desc["Numerical_method_space_discretization"]="Finite volumes"
    test_desc["Numerical_method_time_discretization"]="Implicit"
    test_desc["Space_dimension"]=my_mesh.getSpaceDimension()
    test_desc["Mesh_dimension"]=my_mesh.getMeshDimension()
    test_desc["Mesh_is_unstructured"]=True
    test_desc["Mesh_cell_type"]=my_mesh.getElementTypes()
    test_desc["Mesh_number_of_elements"]=my_mesh.getNumberOfCells()
    test_desc["Mesh_max_number_of_neighbours"]=10
    test_desc["Geometry"]="Square"
    test_desc["Boundary_conditions"]=test_bc
    test_desc["Initial_data"]=test_initial_data
    test_desc["Part_of_mesh_convergence_analysis"]=True
    test_desc["Numerical_parameter_cfl"]=cfl
    test_desc["Simulation_parameter_maximum_time_step"]=ntmax
    test_desc["Simulation_parameter_maximum_time"]=tmax
    test_desc["Simulation_output_frequency"]=output_freq
    test_desc["Simulation_final_time_after_run"]=t_final
    test_desc["Simulation_final_number_of_time_steps_after_run"]=ndt_final
    test_desc["Computational_time_taken_by_run"]=end-start
    test_desc["Absolute_error"]=max(error_p*p0,error_u)
    test_desc["Relative_error"]=max(error_p,error_u)

    with open('test_WaveSystem'+str(my_mesh.getMeshDimension())+'DStaggered_'+meshName+ "Cells.json", 'w') as outfile:  
        json.dump(test_desc, outfile)
    
    return error_p, error_u, nbCells, t_final, ndt_final, max_vel, diag_data_press, diag_data_vel, end - start, cond_number

def solve_file( filename,meshName, resolution,scaling, meshType, testColor,cfl):
    my_mesh = cdmath.Mesh(filename+".med")

    return solve(my_mesh, meshName+str(my_mesh.getNumberOfCells()),resolution,scaling, meshType, testColor,cfl)
    

if __name__ == """__main__""":
    M1=cdmath.Mesh(0,1,20,0,1,20)
    cfl=0.5
    solve(M1,"SquareWithSquares",100,2,"Regular squares","Green",cfl)
