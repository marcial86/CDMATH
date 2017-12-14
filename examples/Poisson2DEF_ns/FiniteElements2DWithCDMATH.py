# -*-coding:utf-8 -*
#===============================================================================================================================
# Name        : Résolution EF de l'équation de Poisson 2D -\triangle u = f avec conditions aux limites de Dirichlet u=0
# Author      : Michaël Ndjinga
# Copyright   : CEA Saclay 2016
# Description : Utilisation de la méthode des éléménts finis P1 avec champs u et f discrétisés aux noeuds d'un maillage triangulaire
#		Création et sauvegarde du champ résultant ainsi que du champ second membre en utilisant la librairie CDMATH
#================================================================================================================================

import cdmath
from math import sin, pi

#Préprocessing optionnel: création du fichier my_mesh.med contenant la géométrie et le maillage du domaine de calcul à partir de commandes python (import salome)

#Chargement du maillage triangulaire du domaine carré [0,1]x[0,1], définition des bords
#=======================================================================================
my_mesh = cdmath.Mesh("../../tests/ressources/MeshTri2600Cells.med")
if(!my_mesh.isTriangular()) :
	raise ValueError("Wrong cell types : mesh is not made of triangles")
eps=1e-6
my_mesh.setGroupAtPlan(0.,0,eps,"DirichletBorder")#Bord GAUCHE
my_mesh.setGroupAtPlan(1.,0,eps,"DirichletBorder")#Bord DROIT
my_mesh.setGroupAtPlan(0.,1,eps,"DirichletBorder")#Bord BAS
my_mesh.setGroupAtPlan(1.,1,eps,"DirichletBorder")#Bord HAUT

nbNodes = my_mesh.getNumberOfNodes()
nbCells = my_mesh.getNumberOfCells()

print("Mesh building done")
print("nb of nodes=", nbNodes)
print("nb of cells=", nbCells)

#Discrétisation du second membre et détermination des noeuds intérieurs
#======================================================================
my_RHSfield = cdmath.Field("RHS field", cdmath.NODES, my_mesh, 1)
nbInteriorNodes = 0
nbBoundaryNodes=0
maxNbNeighbours=0#This is to determine the number of non zero coefficients in the sparse finite element rigidity matrix
interiorNodes=[]
boundaryNodes=[]

#parcours des noeuds pour discrétisation du second membre et extraction 1) des noeuds intérieur 2) des noeuds frontière 3) du nb max voisins d'un noeud
for i in range(nbNodes):
	Ni=my_mesh.getNode(i)
	x = Ni.x()
	y = Ni.y()

	my_RHSfield[i]=2*pi*pi*sin(pi*x)*sin(pi*y)#mettre la fonction definie au second membre de l'edp
	if my_mesh.isBorderNode(i): # Détection des noeuds frontière
		boundaryNodes.append(i)
		nbBoundaryNodes=nbBoundaryNodes+1
	else: # Détection des noeuds intérieurs
		interiorNodes.append(i)
		nbInteriorNodes=nbInteriorNodes+1
		maxNbNeighbours= max(1+Ni.getNumberOfCells(),maxNbNeighbours) #true only in 2D, need a function Ni.getNumberOfNeighbourNodes()

# sauvegarde sur le disque dur du second membre discrétisé dans un fichier paraview
my_RHSfield.writeVTK("FiniteElementsRHSField") 

print("Right hand sde discretidation done")
print("nb of interior nodes=", nbInteriorNodes)
print("nb of boundary nodes=", nbBoundaryNodes)
print("Max nb of neighbours=", maxNbNeighbours)

# Construction de la matrice de rigidité et du vecteur second membre du système linéaire
#=======================================================================================
Rigidite=cdmath.SparseMatrix(nbInteriorNodes,nbInteriorNodes,nbInteriorNodes*maxNbNeighbours)
RHS=cdmath.Vector(nbInteriorNodes)

# Vecteurs gradient de la fonction de forme associée à chaque noeud d'un triangle (hypothèse 2D)
GradShapeFunc0=cdmath.Vector(2)
GradShapeFunc1=cdmath.Vector(2)
GradShapeFunc2=cdmath.Vector(2)

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

	#Formule des gradients voir EF P1 -> calcul déterminants
	GradShapeFunc0[0]= (N1.y()-N2.y())/2
	GradShapeFunc0[1]=-(N1.x()-N2.x())/2
	GradShapeFunc1[0]=-(N0.y()-N2.y())/2
	GradShapeFunc1[1]= (N0.x()-N2.x())/2
	GradShapeFunc2[0]= (N0.y()-N1.y())/2
	GradShapeFunc2[1]=-(N0.x()-N1.x())/2

	#Création d'un tableau (numéro du noeud, gradient de la fonction de forme
	GradShapeFuncs={nodeId0 : GradShapeFunc0}
	GradShapeFuncs[nodeId1]=GradShapeFunc1
	GradShapeFuncs[nodeId2]=GradShapeFunc2


	# Remplissage de  la matrice de rigidité et du second membre
	for j in [nodeId0,nodeId1,nodeId2] :
		if boundaryNodes.count(j)==0 : #seuls les noeuds intérieurs contribuent au système linéaire (matrice de rigidité et second membre)
			j_int=interiorNodes.index(j)#indice du noeud j en tant que noeud intérieur
			#Ajout de la contribution de la cellule triangulaire i au second membre du noeud j 
			RHS[j_int]=Ci.getMeasure()/3*my_RHSfield[j]+RHS[j_int] # intégrale dans le triangle du produit f x fonction de base
			#Contribution de la cellule triangulaire i à la ligne j_int du système linéaire
 			for k in [nodeId0,nodeId1,nodeId2] : 
				if boundaryNodes.count(k)==0 : #seuls les noeuds intérieurs contribuent à la matrice du système linéaire
					k_int=interiorNodes.index(k)#indice du noeud k en tant que noeud intérieur
					coeff = Rigidite(j_int,k_int)+GradShapeFuncs[j]*GradShapeFuncs[k]/Ci.getMeasure()
					Rigidite.setValue(j_int,k_int,coeff)
				#else: si condition limite non nulle au bord, ajouter la contribution du bord au second membre de la cellule j

print("Linear system matrix building done")

# Résolution du système linéaire
#=================================
LS=cdmath.LinearSolver(Rigidite,RHS,100,1.E-6,"CG","ILU")#Remplacer CG par CHOLESKY pour solveur direct
SolSyst=LS.solve()

print("Fin de la résolution du système linéaire")

# Création du champ résultat
#===========================
my_ResultField = cdmath.Field("Result field", cdmath.NODES, my_mesh, 1)
for j in range(nbInteriorNodes):
    my_ResultField[interiorNodes[j]]=SolSyst[j];#remplissage des valeurs pour les noeuds intérieurs
for j in range(nbBoundaryNodes):
    my_ResultField[boundaryNodes[j]]=0;#remplissage des valeurs pour les noeuds frontière (condition limite)
#sauvegarde sur le disque dur du résultat dans un fichier paraview
my_ResultField.writeVTK("FiniteElementsResultField")

print("Numerical solution of 2D poisson equation using finite elements done")

#Calcul de l'erreur commise par rapport à la solution exacte
#===========================================================
max_sol_exacte=(my_RHSfield.getNormEuclidean()).max()/(2*pi*pi)
erreur_max=(my_RHSfield/(2*pi*pi) - my_ResultField).getNormEuclidean().max()
print("max(| numerical solution - exact solution |)/max(| exact solution |) = ",erreur_max/max_sol_exacte)

#Postprocessing optionnel: ouverture du fichier FiniteElementsResultField.pvd contenant le résultat numérique à partir de commandes python (import paraview)

