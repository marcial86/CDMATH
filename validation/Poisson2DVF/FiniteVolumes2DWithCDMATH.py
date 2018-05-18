# -*-coding:utf-8 -*
#===============================================================================================================================
# Name        : Résolution VF de l'équation de Poisson -\triangle u = f avec conditions aux limites de Dirichlet u=0
# Author      : Michaël Ndjinga
# Copyright   : CEA Saclay 2016
# Description : Utilisation de la méthode des volumes finis avec champs u et f discrétisés aux cellules d'un maillage quelconque
#				Création et sauvegarde du champ résultant ainsi que du champ second membre en utilisant CDMATH
#================================================================================================================================

import cdmath
from math import sin, pi

def solve(my_mesh,filename):
    # Création d'un maillage cartésien du domaine carré [0,1]x[0,1], définition des bords
    #====================================================================================
    xmin=0
    xmax=1
    ymin=0
    ymax=1
    #zmin=0 si calcul 3D
    #zmax=1 si calcul 3D
    
    eps=1e-6
    my_mesh.setGroupAtPlan(0,0,eps,"DirichletBorder")#Bord GAUCHE
    my_mesh.setGroupAtPlan(1,0,eps,"DirichletBorder")#Bord DROIT
    my_mesh.setGroupAtPlan(0,1,eps,"DirichletBorder")#Bord BAS
    my_mesh.setGroupAtPlan(1,1,eps,"DirichletBorder")#Bord HAUT
    #my_mesh.setGroupAtPlan(0,2,eps,"DirichletBorder")#Bord AVANT si calcul 3D
    #my_mesh.setGroupAtPlan(1,2,eps,"DirichletBorder")#Bord ARRIERE si calcul 3D
    
    nbCells = my_mesh.getNumberOfCells()
    
    print("Mesh groups done")
    print("nb of cells  = ", nbCells)
    
    #Discrétisation du second membre et extraction du nb max de voisins d'une cellule
    #================================================================================
    my_RHSfield = cdmath.Field("RHS field", cdmath.CELLS, my_mesh, 1)
    maxNbNeighbours=0#This is to determine the number of non zero coefficients in the sparse finite element rigidity matrix
    #parcours des cellules pour discrétisation du second membre et extraction du nb max de voisins d'une cellule
    for i in range(nbCells): 
        Ci = my_mesh.getCell(i)
        x = Ci.x()
        y = Ci.y()
        # z=Ci.z() si calcul 3D
        my_RHSfield[i]=2*pi*pi*sin(pi*x)*sin(pi*y)#mettre la fonction definie au second membre de l edp
        # compute maximum number of neighbours
        maxNbNeighbours= max(1+Ci.getNumberOfFaces(),maxNbNeighbours)
    
    # sauvegarde sur le disque dur du second membre discrétisé dans un fichier paraview
    my_RHSfield.writeVTK("FiniteVolumes2DRHSField"+filename)
    
    print("Right hand side discretisation done")
    print("Max nb of neighbours=", maxNbNeighbours)
    
    # Construction de la matrice et du vecteur second membre du système linéaire
    #===========================================================================
    Rigidite=cdmath.SparseMatrix(nbCells,nbCells,nbCells*maxNbNeighbours)# warning : third argument is total number of non zero coefficients in the matrix
    RHS=cdmath.Vector(nbCells)
    #Parcours des cellules du domaine
    for i in range(nbCells):
        RHS[i]=my_RHSfield[i] #la valeur moyenne du second membre f dans la cellule i
        Ci=my_mesh.getCell(i)
        for j in range(Ci.getNumberOfFaces()):# parcours des faces voisinnes
            Fj=my_mesh.getFace(Ci.getFaceId(j))
            if not Fj.isBorder():
                k=Fj.getCellId(0)
                if k==i :
                    k=Fj.getCellId(1)
                Ck=my_mesh.getCell(k)
                distance=Ci.getBarryCenter().distance(Ck.getBarryCenter())
                coeff=Fj.getMeasure()/Ci.getMeasure()/distance
                Rigidite.setValue(i,k,-coeff) # terme extradiagonal
            else:
                coeff=Fj.getMeasure()/Ci.getMeasure()/Ci.getBarryCenter().distance(Fj.getBarryCenter())
            Rigidite.addValue(i,i,coeff) # terme diagonal
    
    print("Linear system matrix building done")
    
    # Résolution du système linéaire
    #=================================
    LS=cdmath.LinearSolver(Rigidite,RHS,500,1.E-6,"CG","LU")
    SolSyst=LS.solve()
    
    print "Preconditioner used : ", LS.getNameOfPc()
    print "Number of iterations used : ", LS.getNumberOfIter()
    print("Linear system solved")
    
    # Création du champ résultat
    #===========================
    my_ResultField = cdmath.Field("Result field", cdmath.CELLS, my_mesh, 1)
    for i in range(nbCells):
        my_ResultField[i]=SolSyst[i];
    #sauvegarde sur le disque dur du résultat dans un fichier paraview
    my_ResultField.writeVTK("FiniteVolumes2DResultField"+filename)
    
    print("Numerical solution of 2D poisson equation using finite elements done")
    
    #Calcul de l'erreur commise par rapport à la solution exacte
    #===========================================================
    #The following formulas use the fact that the exact solution is equal the right hand side divided by 2*pi*pi
    max_abs_sol_exacte=max(my_RHSfield.max(),-my_RHSfield.min())/(2*pi*pi)
    max_sol_num=my_ResultField.max()
    min_sol_num=my_ResultField.min()
    erreur_abs=0
    for i in range(nbCells) :
        if erreur_abs < abs(my_RHSfield[i]/(2*pi*pi) - my_ResultField[i]) :
            erreur_abs = abs(my_RHSfield[i]/(2*pi*pi) - my_ResultField[i])
    
    print("Relative error = max(| exact solution - numerical solution |)/max(| exact solution |) = ",erreur_abs/max_abs_sol_exacte)
    print ("Maximum numerical solution = ", max_sol_num, " Minimum numerical solution = ", min_sol_num)

    return erreur_abs/max_abs_sol_exacte, my_mesh.getNumberOfCells()

#Postprocessing optionnel: ouverture du fichier FiniteElementsResultField.pvd contenant le résultat numérique à partir de commandes python (import paraview)

def solve_file( filename):
    my_mesh = cdmath.Mesh(filename+".med")
    return solve(my_mesh, filename)
    
if __name__ == """__main__""":
        mesh51 = cdmath.Mesh(0,1,51,0,1,51)
        solve(mesh51,'51')
