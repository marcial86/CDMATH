# -*-coding:utf-8 -*
#===============================================================================================================================
# Name        : Résolution EF de l'équation de Laplace-Beltrami -\triangle u = f sur une sphere
# Author      : Michael Ndjinga
# Copyright   : CEA Saclay 2017
# Description : Utilisation de la méthode des éléménts finis P1 avec champs u et f discrétisés aux noeuds d'un maillage triangulaire
#				Création et sauvegarde du champ résultant ainsi que du champ second membre en utilisant la librairie CDMATH
#================================================================================================================================

import cdmath
import time
from math import pow
import numpy as np
import PV_routines
import VTK_routines

def solve(filename,resolution):
    start = time.time()
    #Préprocessing optionnel: création du fichier my_mesh.med contenant la géométrie et le maillage du domaine de calcul à partir de commandes python (import salome)
    
    #Chargement du maillage triangulaire de la sphère
    #=======================================================================================
    my_mesh = cdmath.Mesh(filename+".med")
    if(not my_mesh.isTriangular()) :
        raise ValueError("Wrong cell types : mesh is not made of triangles")
    if(my_mesh.getMeshDimension()!=2) :
        raise ValueError("Wrong mesh dimension : expected a surface of dimension 2")
    if(my_mesh.getSpaceDimension()!=3) :
        raise ValueError("Wrong space dimension : expected a space of dimension 3")
    
    nbNodes = my_mesh.getNumberOfNodes()
    nbCells = my_mesh.getNumberOfCells()
    
    print("Mesh building/loading done")
    print("nb of nodes=", nbNodes)
    print("nb of cells=", nbCells)
    
    #Discrétisation du second membre et détermination des noeuds intérieurs
    #======================================================================
    my_RHSfield = cdmath.Field("RHS field", cdmath.NODES, my_mesh, 1)
    maxNbNeighbours = 0#This is to determine the number of non zero coefficients in the sparse finite element rigidity matrix
    
    #parcours des noeuds pour discrétisation du second membre et extraction du nb max voisins d'un noeud
    for i in range(nbNodes):
        Ni=my_mesh.getNode(i)
        x = Ni.x()
        y = Ni.y()
        z = Ni.z()
    
        my_RHSfield[i]=12*y*(3*x*x-y*y)/pow(x*x+y*y+z*z,3/2)#vecteur propre du laplacien sur la sphère
        if my_mesh.isBorderNode(i): # Détection des noeuds frontière
            raise ValueError("Mesh should not contain borders")
        else:
            maxNbNeighbours = max(1+Ni.getNumberOfCells(),maxNbNeighbours)
    
    # sauvegarde sur le disque dur du second membre discrétisé dans un fichier paraview
    my_RHSfield.writeVTK("FiniteElementsOnSphereRHSField"+str(nbNodes)) 
    
    print("Right hand side discretisation done")
    print("Max nb of neighbours=", maxNbNeighbours)
    print("Integral of the RHS", my_RHSfield.integral(0))
    
    # Construction de la matrice de rigidité et du vecteur second membre du système linéaire
    #=======================================================================================
    Rigidite=cdmath.SparseMatrixPetsc(nbNodes,nbNodes,maxNbNeighbours)# warning : third argument is number of non zero coefficients per line
    RHS=cdmath.Vector(nbNodes)
    
    # Vecteurs gradient de la fonction de forme associée à chaque noeud d'un triangle
    GradShapeFunc0=cdmath.Vector(3)
    GradShapeFunc1=cdmath.Vector(3)
    GradShapeFunc2=cdmath.Vector(3)
    
    normalFace0=cdmath.Vector(3)
    normalFace1=cdmath.Vector(3)
    
    #On parcourt les triangles du domaine
    for i in range(nbCells):
    
        Ci=my_mesh.getCell(i)
    
        #Contribution à la matrice de rigidité
        nodeId0=Ci.getNodeId(0)
        nodeId1=Ci.getNodeId(1)
        nodeId2=Ci.getNodeId(2)
        N0=my_mesh.getNode(nodeId0)
        N1=my_mesh.getNode(nodeId1)
        N2=my_mesh.getNode(nodeId2)
    
        #Build normal to cell Ci
        normalFace0[0]=Ci.getNormalVector(0,0)
        normalFace0[1]=Ci.getNormalVector(0,1)
        normalFace0[2]=Ci.getNormalVector(0,2)
        normalFace1[0]=Ci.getNormalVector(1,0)
        normalFace1[1]=Ci.getNormalVector(1,1)
        normalFace1[2]=Ci.getNormalVector(1,2)
    
        normalCell = normalFace0.crossProduct(normalFace1)
        test = normalFace0.tensProduct(normalFace1)
        normalCell = normalCell/normalCell.norm()
    
        cellMat=cdmath.Matrix(4)
        cellMat[0,0]=N0.x()
        cellMat[0,1]=N0.y()
        cellMat[0,2]=N0.z()
        cellMat[1,0]=N1.x()
        cellMat[1,1]=N1.y()
        cellMat[1,2]=N1.z()
        cellMat[2,0]=N2.x()
        cellMat[2,1]=N2.y()
        cellMat[2,2]=N2.z()
        cellMat[3,0]=normalCell[0]
        cellMat[3,1]=normalCell[1]
        cellMat[3,2]=normalCell[2]
        cellMat[0,3]=1
        cellMat[1,3]=1
        cellMat[2,3]=1
        cellMat[3,3]=0
    
        #Formule des gradients voir EF P1 -> calcul déterminants
        GradShapeFunc0[0]= cellMat.partMatrix(0,0).determinant()/2
        GradShapeFunc0[1]=-cellMat.partMatrix(0,1).determinant()/2
        GradShapeFunc0[2]= cellMat.partMatrix(0,2).determinant()/2
        GradShapeFunc1[0]=-cellMat.partMatrix(1,0).determinant()/2
        GradShapeFunc1[1]= cellMat.partMatrix(1,1).determinant()/2
        GradShapeFunc1[2]=-cellMat.partMatrix(1,2).determinant()/2
        GradShapeFunc2[0]= cellMat.partMatrix(2,0).determinant()/2
        GradShapeFunc2[1]=-cellMat.partMatrix(2,1).determinant()/2
        GradShapeFunc2[2]= cellMat.partMatrix(2,2).determinant()/2
    
        #Création d'un tableau (numéro du noeud, gradient de la fonction de forme
        GradShapeFuncs={nodeId0 : GradShapeFunc0}
        GradShapeFuncs[nodeId1]=GradShapeFunc1
        GradShapeFuncs[nodeId2]=GradShapeFunc2
    
        # Remplissage de  la matrice de rigidité et du second membre
        for j in [nodeId0,nodeId1,nodeId2] : 
            #Ajout de la contribution de la cellule triangulaire i au second membre du noeud j 
            RHS[j]=Ci.getMeasure()/3*my_RHSfield[j]+RHS[j] # intégrale dans le triangle du produit f x fonction de base
            #Contribution de la cellule triangulaire i à la ligne j du système linéaire
            for k in [nodeId0,nodeId1,nodeId2] : 
                Rigidite.addValue(j,k,GradShapeFuncs[j]*GradShapeFuncs[k]/Ci.getMeasure())
    
    print("Linear system matrix building done")
    
    # Résolution du système linéaire
    #=================================
    LS=cdmath.LinearSolver(Rigidite,RHS,100,1.E-3,"CG","ILU")#Remplacer CG par CHOLESKY pour solveur direct
    LS.isSingular()#En raison de l'absence de bord
    SolSyst=LS.solve()
    print "Preconditioner used : ", LS.getNameOfPc()
    print "Number of iterations used : ", LS.getNumberOfIter()
    print "Final residual : ", LS.getResidu()
    print("Linear system solved")
    
    # Création du champ résultat
    #===========================
    my_ResultField = cdmath.Field("ResultField", cdmath.NODES, my_mesh, 1)
    for j in range(nbNodes):
        my_ResultField[j]=SolSyst[j];#remplissage des valeurs pour les noeuds intérieurs
    #sauvegarde sur le disque dur du résultat dans un fichier paraview
    my_ResultField.writeVTK("FiniteElementsOnSphereResultField"+str(nbNodes))
    
    #Postprocessing : save 3D picture
    PV_routines.Save_PV_data_to_picture_file("FiniteElementsOnSphereResultField"+'_0.vtu',"ResultField",'NODES',"FiniteElementsOnSphereResultField")
    VTK_routines.Clip_VTK_data_to_VTK("FiniteElementsOnSphereResultField"+'_0.vtu',"Clip_VTK_data_to_VTK_"+ "FiniteElementsOnSphereResultField"+'_0.vtu',[0.25,0.25,0.25], [-0.5,-0.5,-0.5],resolution )
    PV_routines.Save_PV_data_to_picture_file("Clip_VTK_data_to_VTK_"+"FiniteElementsOnSphereResultField"+'_0.vtu',"ResultField",'NODES',"Clip_VTK_data_to_VTK_"+"FiniteElementsOnSphereResultField")
    
    print("Integral of the numerical solution", my_ResultField.integral(0))
    print("Numerical solution of poisson equation on a sphere using finite elements done")
    
    #Calcul de l'erreur commise par rapport à la solution exacte
    #===========================================================
    #The following formulas use the fact that the exact solution is equal the right hand side divided by 12
    max_abs_sol_exacte=0
    erreur_abs=0
    max_sol_num=0
    min_sol_num=0
    for i in range(nbNodes) :
        if max_abs_sol_exacte < abs(my_RHSfield[i]) :
            max_abs_sol_exacte = abs(my_RHSfield[i])
        if erreur_abs < abs(my_RHSfield[i]/12 - my_ResultField[i]) :
            erreur_abs = abs(my_RHSfield[i]/12 - my_ResultField[i])
        if max_sol_num < my_ResultField[i] :
            max_sol_num = my_ResultField[i]
        if min_sol_num > my_ResultField[i] :
            min_sol_num = my_ResultField[i]
    max_abs_sol_exacte = max_abs_sol_exacte/12
    
    print("Absolute error = max(| exact solution - numerical solution |) = ",erreur_abs )
    print("Relative error = max(| exact solution - numerical solution |)/max(| exact solution |) = ",erreur_abs/max_abs_sol_exacte)
    print ("Maximum numerical solution = ", max_sol_num, " Minimum numerical solution = ", min_sol_num)

    end = time.time()
    return erreur_abs/max_abs_sol_exacte, my_mesh.getNumberOfNodes(), min_sol_num, max_sol_num, end - start
    
if __name__ == """__main__""":
    solve("meshSphere",100)
