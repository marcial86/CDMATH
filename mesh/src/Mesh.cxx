/*
 * mesh.cxx
 *
 *  Created on: 22 janv. 2012
 *      Authors: CDMATH
 */

#include "Mesh.hxx"
#include "Node.hxx"
#include "Cell.hxx"
#include "Face.hxx"
#include "IntTab.hxx"

#include "MEDFileMesh.hxx"
#include "MEDLoader.hxx"
#include "MEDCouplingUMesh.hxx"
#include "MEDCouplingIMesh.hxx"
#include "MEDCouplingFieldDouble.hxx"

#include "CdmathException.hxx"

#include <iostream>
#include <iterator>
#include <algorithm> 

using namespace MEDCoupling;
using namespace std;

//----------------------------------------------------------------------
Mesh::Mesh( void )
//----------------------------------------------------------------------
{
	_mesh=NULL;
	_cells=NULL;
	_nodes=NULL;
	_faces=NULL;
	_spaceDim = 0 ;
	_meshDim  = 0 ;
	_numberOfNodes = 0;
	_numberOfFaces = 0;
	_numberOfCells = 0;
    _isStructured=false;
	_xMin=0.;
	_xSup=0.;
	_yMin=0.;
	_ySup=0.;
	_zMin=0.;
	_zSup=0.;
    _nxyz.resize(0);
    _dxyz.resize(0.);
	_groupNames.resize(0);
	_groups.resize(0);
}

//----------------------------------------------------------------------
Mesh::~Mesh( void )
//----------------------------------------------------------------------
{
	delete [] _cells;
	delete [] _nodes;
	delete [] _faces;
	//for(int i=0; i< _groups.size(); i++)
	//	_groups[i]->decrRef();
}

Mesh::Mesh( const MEDCoupling::MEDCouplingIMesh* mesh )
{
	_spaceDim=mesh->getSpaceDimension();
	_meshDim=mesh->getMeshDimension();
    _isStructured=true;
	_dxyz=mesh->getDXYZ();
	_nxyz=mesh->getCellGridStructure();
	double* Box0=new double[2*_spaceDim];
	mesh->getBoundingBox(Box0);

	_xMin=Box0[0];
	_xSup=Box0[1];
	if (_spaceDim>=2)
	{
		_yMin=Box0[2];
		_ySup=Box0[3];
	}
	if (_spaceDim>=3)
	{
		_zMin=Box0[4];
		_zSup=Box0[5];
	}

	double *originPtr = new double[_spaceDim];
	double *dxyzPtr = new double[_spaceDim];
	int *nodeStrctPtr = new int[_spaceDim];

	for(int i=0;i<_spaceDim;i++)
	{
		originPtr[i]=Box0[2*i];
		nodeStrctPtr[i]=_nxyz[i]+1;
		dxyzPtr[i]=_dxyz[i];
	}
	_mesh=MEDCouplingIMesh::New("MESH",
			_spaceDim,
			nodeStrctPtr,
			nodeStrctPtr+_spaceDim,
			originPtr,
			originPtr+_spaceDim,
			dxyzPtr,
			dxyzPtr+_spaceDim);
	delete [] originPtr;
	delete [] dxyzPtr;
	delete [] nodeStrctPtr;
	delete [] Box0 ;
	setMesh();
}

//----------------------------------------------------------------------
Mesh::Mesh( const Mesh& m )
//----------------------------------------------------------------------
{
	_spaceDim = m.getSpaceDimension() ;
	_meshDim = m.getMeshDimension() ;
    _isStructured=m.isStructured();
    if(_isStructured)
    {
        _nxyz = m.getCellGridStructure() ;
        _dxyz=m.getDXYZ();
        _xMin=m.getXMin();
        _xSup=m.getXSup();
        _yMin=m.getYMin();
        _ySup=m.getYSup();
        _zMin=m.getZMin();
        _zSup=m.getZSup();
    }
	_numberOfNodes = m.getNumberOfNodes();
	_numberOfFaces = m.getNumberOfFaces();
	_numberOfCells = m.getNumberOfCells();
	_groupNames = m.getNamesOfGroups() ;
	_groups = m.getGroups() ;
	_nodes   = new Node[_numberOfNodes] ;
	_faces   = new Face[_numberOfFaces] ;
	_cells   = new Cell[_numberOfCells] ;

	for (int i=0;i<_numberOfNodes;i++)
		_nodes[i]=m.getNode(i);

	for (int i=0;i<_numberOfFaces;i++)
		_faces[i]=m.getFace(i);

	for (int i=0;i<_numberOfCells;i++)
		_cells[i]=m.getCell(i);

	MCAuto<MEDCouplingMesh> m1=m.getMEDCouplingMesh()->deepCopy();
	_mesh=m1;
}

//----------------------------------------------------------------------
Mesh::Mesh( const std::string filename, int meshLevel )
//----------------------------------------------------------------------
{
	readMeshMed(filename, meshLevel);
}

//----------------------------------------------------------------------
void
Mesh::readMeshMed( const std::string filename, const int meshLevel)
//----------------------------------------------------------------------
{
	MEDFileUMesh *m=MEDFileUMesh::New(filename.c_str());//reads the first mesh encountered in the file, otherwise call New (const char *fileName, const char *mName, int dt=-1, int it=-1)
	_mesh=m->getMeshAtLevel(meshLevel);
	_mesh->setName(_mesh->getName());
	_meshDim=_mesh->getMeshDimension();
	_spaceDim=_mesh->getSpaceDimension();
    MEDCoupling::MEDCouplingIMesh* structuredMesh = dynamic_cast<MEDCoupling::MEDCouplingIMesh*> (_mesh.retn());
    if(structuredMesh)
    {
        _isStructured=true;
        _dxyz=structuredMesh->getDXYZ();
        _nxyz=structuredMesh->getCellGridStructure();
        double* Box0=new double[2*_spaceDim];
        structuredMesh->getBoundingBox(Box0);
    
        _xMin=Box0[0];
        _xSup=Box0[1];
        if (_spaceDim>=2)
        {
            _yMin=Box0[2];
            _ySup=Box0[3];
        }
        if (_spaceDim>=3)
        {
            _zMin=Box0[4];
            _zSup=Box0[5];
        }
    }
    else
        _isStructured=true;
    
	MEDCouplingUMesh*  mu = setMesh();
	setGroups(m, mu);
	cout<<endl<< "Loaded file "<< filename<<", mesh name= "<<m->getName()<<", _meshDim="<< _meshDim<< ", _spaceDim="<< _spaceDim<<endl;

	m->decrRef();
	mu->decrRef();
}

void
Mesh::setGroupAtFaceByCoords(double x, double y, double z, double eps, std::string groupName)
{
	int nbFace=getNumberOfFaces();
	bool flag=false;
	for (int iface=0;iface<nbFace;iface++)
	{
		double FX=_faces[iface].x();
		double FY=_faces[iface].y();
		double FZ=_faces[iface].z();
		if (abs(FX-x)<eps && abs(FY-y)<eps && abs(FZ-z)<eps)
		{
			_faces[iface].setGroupName(groupName);
			IntTab nodesID= _faces[iface].getNodesId();
			int nbNodes = _faces[iface].getNumberOfNodes();
			for(int inode=0 ; inode<nbNodes ; inode++)
				_nodes[nodesID[inode]].setGroupName(groupName);

			flag=true;
		}
	}
	if (flag)
		_groupNames.push_back(groupName);
	//To do : update _groups
}

void
Mesh::setGroupAtPlan(double value, int direction, double eps, std::string groupName)
{
	int nbFace=getNumberOfFaces();
	bool flag=false;
	for (int iface=0;iface<nbFace;iface++)
	{
		double cord=_faces[iface].getBarryCenter()[direction];
		if (abs(cord-value)<eps)
		{
			_faces[iface].setGroupName(groupName);
			IntTab nodesID= _faces[iface].getNodesId();
			int nbNodes = _faces[iface].getNumberOfNodes();
			for(int inode=0 ; inode<nbNodes ; inode++)
				_nodes[nodesID[inode]].setGroupName(groupName);

			flag=true;
		}
	}
	if (flag)
		_groupNames.push_back(groupName);
	//To do : update _groups
}

IntTab
Mesh::getIndexFacePeriodic( void ) const
{
	int nbFace=getNumberOfFaces();
	IntTab indexesFacesPerio(nbFace);
	for (int iface=0;iface<nbFace;iface++)
		indexesFacesPerio(iface)=getIndexFacePeriodic(iface);
	return indexesFacesPerio;
}

int
Mesh::getIndexFacePeriodic(int indexFace) const
{
	if (!_faces[indexFace].isBorder())
		return -1;
	double minmax[4];
	_mesh->buildUnstructured()->getCoords()->getMinMaxPerComponent(minmax);
	double xmin=minmax[0];
	double xmax=minmax[1];
	double ymin=minmax[2];
	double ymax=minmax[3];
	int nbFace=getNumberOfFaces();
	double x=_faces[indexFace].x();
	double y=_faces[indexFace].y();
	double eps=1.E-10;
	// pos=0 : bottom
	// pos=1 : right
	// pos=2 : top
	// pos=3 : left
	int pos=-1;
	if (abs(y-ymin)<1.E-10)
		pos=0;
	if (abs(x-xmax)<1.E-10)
		pos=1;
	if (abs(y-ymax)<1.E-10)
		pos=2;
	if (abs(x-xmin)<1.E-10)
		pos=3;
	if (pos==-1)
		cerr << "periodic face not found " << endl;

	int ifaceOk=-1;
	for (int iface=0;iface<nbFace;iface++)
	{
		double xi=_faces[iface].x();
		double yi=_faces[iface].y();
		if (abs(y-yi)<eps && pos==1 && abs(xi-xmin)<eps)
		{
			ifaceOk=iface;
			break;
		}
		if (abs(y-yi)<eps && pos==3 && abs(xi-xmax)<eps)
		{
			ifaceOk=iface;
			break;
		}
		if (abs(x-xi)<eps && pos==0 && abs(yi-ymax)<eps)
		{
			ifaceOk=iface;
			break;
		}
		if (abs(x-xi)<eps && pos==2 && abs(yi-ymin)<eps)
		{
			ifaceOk=iface;
			break;
		}
	}
	return ifaceOk;
}

bool
Mesh::isBorderNode(int nodeid) const
{
	return getNode(nodeid).isBorder();
}

bool
Mesh::isBorderFace(int faceid) const
{
	return getFace(faceid).isBorder();
}

bool
Mesh::isTriangular() const
{
	return _eltsTypes.size()==1 && _eltsTypes[0]==INTERP_KERNEL::NORM_TRI3;
}
bool
Mesh::isTetrahedral() const
{
	return _eltsTypes.size()==1 && _eltsTypes[0]==INTERP_KERNEL::NORM_TETRA4;
}
bool
Mesh::isQuadrangular() const
{
	return _eltsTypes.size()==1 && _eltsTypes[0]==INTERP_KERNEL::NORM_QUAD4;
}
bool
Mesh::isHexahedral() const
{
	return _eltsTypes.size()==1 && _eltsTypes[0]==INTERP_KERNEL::NORM_HEXA8;
}
bool
Mesh::isStructured() const
{
	return _isStructured;
}

void
Mesh::setGroups( const MEDFileUMesh* medmesh, MEDCouplingUMesh*  mu)
{
	//Searching for face groups
	vector<string> faceGroups=medmesh->getGroupsNames() ;

	for (unsigned int i=0;i<faceGroups.size();i++ )
	{
		string groupName=faceGroups[i];
		vector<int> nonEmptyGrp(medmesh->getGrpNonEmptyLevels(groupName));
		//We check if the group has a relative dimension equal to -1 
		//before call to the function getGroup(-1,groupName.c_str())
		vector<int>::iterator it = find(nonEmptyGrp.begin(), nonEmptyGrp.end(), -1);
		if (it != nonEmptyGrp.end())
		{
			cout<<"Boundary face group named "<< groupName << " found"<<endl;
			MEDCouplingUMesh *m=medmesh->getGroup(-1,groupName.c_str());
			_groups.push_back(m);
			_groupNames.push_back(groupName);
			DataArrayDouble *baryCell = m->computeCellCenterOfMass() ;
			const double *coorBary=baryCell->getConstPointer();

			int nbCellsSubMesh=m->getNumberOfCells();
			for (int ic(0), k(0); ic<nbCellsSubMesh; ic++, k+=_spaceDim)
			{
				vector<double> coorBaryXyz(3,0);
				for (int d=0; d<_spaceDim; d++)
					coorBaryXyz[d] = coorBary[k+d];
				Point p1(coorBaryXyz[0],coorBaryXyz[1],coorBaryXyz[2]) ;

				int flag=0;
				for (int iface=0;iface<_numberOfFaces;iface++ )
				{
					Point p2=_faces[iface].getBarryCenter();
					if(p1.distance(p2)<1.E-10)
					{
						_faces[iface].setGroupName(groupName);
						flag=1;
						break;
					}
				}
				if (flag==0)
					throw CdmathException("No face belonging to group " + groupName + " found");
			}
			baryCell->decrRef();
			//m->decrRef();
		}
	}

	//Searching for node groups
	vector<string> nodeGroups=medmesh->getGroupsOnSpecifiedLev(1) ;

	for (unsigned int i=0;i<nodeGroups.size();i++ )
	{
		string groupName=faceGroups[i];
		DataArrayInt * nodeGroup=medmesh->getNodeGroupArr( groupName );
		const int *nodeids=nodeGroup->getConstPointer();

		if(nodeids!=NULL)
		{
			cout<<"Boundary node group named "<< groupName << " found"<<endl;

			int nbNodesSubMesh=nodeGroup->getNumberOfTuples();//nodeGroup->getNbOfElems();

			DataArrayDouble *coo = mu->getCoords() ;
			const double *cood=coo->getConstPointer();

			for (int ic(0); ic<nbNodesSubMesh; ic++)
			{
				vector<double> coorP(3,0);
				for (int d=0; d<_spaceDim; d++)
					coorP[d] = cood[nodeids[ic]*_spaceDim+d];
				Point p1(coorP[0],coorP[1],coorP[2]) ;

				int flag=0;
				for (int inode=0;inode<_numberOfNodes;inode++ )
				{
					Point p2=_nodes[inode].getPoint();
					if(p1.distance(p2)<1.E-10)
					{
						_nodes[inode].setGroupName(groupName);
						flag=1;
						break;
					}
				}
				if (flag==0)
					throw CdmathException("No node belonging to group " + groupName + " found");
			}
		}
	}
}

//----------------------------------------------------------------------
MEDCouplingUMesh* 
Mesh::setMesh( void )
//----------------------------------------------------------------------
{
	DataArrayInt *desc=DataArrayInt::New();
	DataArrayInt *descI=DataArrayInt::New();
	DataArrayInt *revDesc=DataArrayInt::New();
	DataArrayInt *revDescI=DataArrayInt::New();
	MEDCouplingUMesh* mu=_mesh->buildUnstructured();
	mu->unPolyze();
	MEDCouplingUMesh* m2=mu->buildDescendingConnectivity(desc,descI,revDesc,revDescI);//mesh of dimension N-1 containing the cell interfaces
	m2->setName(mu->getName());

	//Test du type d'éléments contenus dans le maillage afin d'éviter les éléments contenant des points de gauss
	_eltsTypes=mu->getAllGeoTypesSorted();
	for(int i=0; i<_eltsTypes.size();i++)
	{
		if(
				_eltsTypes[i]!= INTERP_KERNEL::NORM_POINT1 && _eltsTypes[i]!= INTERP_KERNEL::NORM_SEG2
				&& _eltsTypes[i]!= INTERP_KERNEL::NORM_TRI3   && _eltsTypes[i]!= INTERP_KERNEL::NORM_QUAD4
				&& _eltsTypes[i]!= INTERP_KERNEL::NORM_TETRA4 && _eltsTypes[i]!= INTERP_KERNEL::NORM_PYRA5
				&& _eltsTypes[i]!= INTERP_KERNEL::NORM_PENTA6 && _eltsTypes[i]!= INTERP_KERNEL::NORM_HEXA8
				&& _eltsTypes[i]!= INTERP_KERNEL::NORM_POLYGON&& _eltsTypes[i]!= INTERP_KERNEL::NORM_POLYHED
		)
		{
			cout<< "Mesh " + mu->getName() + " contains an element of type " <<endl;
			cout<< _eltsTypes[i]<<endl;
			throw CdmathException("Mesh::setMesh : in order to avoid gauss points, mesh should contain elements of type NORM_POINT1, NORM_SEG2, NORM_TRI3, NORM_QUAD4, NORM_TETRA4, NORM_PYRA5, NORM_PENTA6, NORM_HEXA8, NORM_POLYGON");
		}
	}

	const int *tmp=desc->getConstPointer();
	const int *tmpI=descI->getConstPointer();

	DataArrayDouble *baryCell = mu->computeCellCenterOfMass() ;
	const double *coorBary=baryCell->getConstPointer();

	MEDCouplingFieldDouble* fields=mu->getMeasureField(true);
	DataArrayDouble *surface = fields->getArray();
	const double *surf=surface->getConstPointer();

	DataArrayDouble *coo = mu->getCoords() ;
	const double *cood=coo->getConstPointer();

	DataArrayInt *revNode=DataArrayInt::New();
	DataArrayInt *revNodeI=DataArrayInt::New();
	mu->getReverseNodalConnectivity(revNode,revNodeI) ;
	const int *tmpN=revNode->getConstPointer();
	const int *tmpNI=revNodeI->getConstPointer();

	DataArrayInt *revCell=DataArrayInt::New();
	DataArrayInt *revCellI=DataArrayInt::New();
	m2->getReverseNodalConnectivity(revCell,revCellI) ;
	const int *tmpC=revCell->getConstPointer();
	const int *tmpCI=revCellI->getConstPointer();

	const DataArrayInt *nodal = m2->getNodalConnectivity() ;
	const DataArrayInt *nodalI = m2->getNodalConnectivityIndex() ;
	const int *tmpNE=nodal->getConstPointer();
	const int *tmpNEI=nodalI->getConstPointer();

	const int *tmpA=revDesc->getConstPointer();
	const int *tmpAI=revDescI->getConstPointer();

	_numberOfCells = mu->getNumberOfCells() ;
	_cells    = new Cell[_numberOfCells] ;

	_numberOfNodes = mu->getNumberOfNodes() ;
	_nodes    = new Node[_numberOfNodes] ;

	_numberOfFaces = m2->getNumberOfCells();
	_faces    = new Face[_numberOfFaces] ;

	// _cells, _nodes and _faces initialization:
	if (_spaceDim == 1)
	{
		for( int id=0;id<_numberOfCells;id++ )
		{
			int nbFaces=tmpI[id+1]-tmpI[id];
			int nbVertices=mu->getNumberOfNodesInCell(id) ;
			const int *work=tmp+tmpI[id];

			Cell ci( nbVertices, nbFaces, surf[id], Point(coorBary[id], 0.0, 0.0) ) ;

			std::vector<int> nodeIdsOfCell ;
			mu->getNodeIdsOfCell(id,nodeIdsOfCell) ;
			for( int el=0;el<nbVertices;el++ )
				ci.addNodeId(el,nodeIdsOfCell[el]) ;

			double xn = (cood[nodeIdsOfCell[nbVertices-1]] - cood[nodeIdsOfCell[0]] > 0.0) ? -1.0 : 1.0;

			for( int el=0;el<nbFaces;el++ )
			{
				ci.addNormalVector(el,xn,0.0,0.0) ;
				ci.addFaceId(el,work[el]) ;
				xn = - xn;
			}
			_cells[id] = ci ;
		}

		for( int id(0), k(0); id<_numberOfNodes; id++, k+=_spaceDim)
		{
			Point p(cood[k], 0.0, 0.0) ;
			const int *workc=tmpN+tmpNI[id];
			int nbCells=tmpNI[id+1]-tmpNI[id];
			const int *workf=tmpC+tmpCI[id];
			int nbFaces=tmpCI[id+1]-tmpCI[id];
			Node vi( nbCells, nbFaces, p ) ;

			for( int el=0;el<nbCells;el++ )
				vi.addCellId(el,workc[el]) ;
			for( int el=0;el<nbFaces;el++ )
				vi.addFaceId(el,workf[el]) ;
			_nodes[id] = vi ;
		}

		for(int id(0), k(0); id<_numberOfFaces; id++, k+=_spaceDim)
		{
			Point p(cood[k], 0.0, 0.0) ;
			const int *workc=tmpA+tmpAI[id];
			int nbCells=tmpAI[id+1]-tmpAI[id];

			const int *workv=tmpNE+tmpNEI[id]+1;
			Face fi( 1, nbCells, 1.0, p, 1.0, 0.0, 0.0) ;
			fi.addNodeId(0,workv[0]) ;

			for(int idCell=0; idCell<nbCells; idCell++)
				fi.addCellId(idCell,workc[idCell]) ;

			_faces[id] = fi ;
		}
	}
	else if(_spaceDim==2  || _spaceDim==3)
	{
		DataArrayInt *desc2=DataArrayInt::New();
		DataArrayInt *descI2=DataArrayInt::New();
		DataArrayInt *revDesc2=DataArrayInt::New();
		DataArrayInt *revDescI2=DataArrayInt::New();
		MEDCouplingUMesh *m3=mu->buildDescendingConnectivity2(desc2,descI2,revDesc2,revDescI2);
		m3->setName(mu->getName());

		const int *tmp2=desc2->getConstPointer();
		const int *tmpI2=descI2->getConstPointer();

		DataArrayDouble *barySeg = m2->computeCellCenterOfMass() ;
		const double *coorBarySeg=barySeg->getConstPointer();

		MEDCouplingFieldDouble* fieldn;
		DataArrayDouble *normal;
		const double *tmpNormal;

		if(_spaceDim==_meshDim)
			fieldn = m2->buildOrthogonalField();//Compute the normal to each cell interface
		else
		{
			//compute the 3D normal vector to the 2D cell
			fieldn = mu->buildOrthogonalField();
		}
		normal = fieldn->getArray();
		tmpNormal = normal->getConstPointer();

		/*Building mesh cells */
		for(int id(0), k(0); id<_numberOfCells; id++, k+=_spaceDim)
		{
			const int *work=tmp+tmpI[id];
			const int *work2=tmp2+tmpI2[id];

			int nbFaces=tmpI[id+1]-tmpI[id];
			int nbVertices=mu->getNumberOfNodesInCell(id) ;

			vector<double> coorBaryXyz(3,0);
			for (int d=0; d<_spaceDim; d++)
				coorBaryXyz[d] = coorBary[k+d];

			Point p(coorBaryXyz[0],coorBaryXyz[1],coorBaryXyz[2]) ;
			Cell ci( nbVertices, nbFaces, surf[id], p ) ;

			/* Filling cell nodes */
			std::vector<int> nodeIdsOfCell ;
			mu->getNodeIdsOfCell(id,nodeIdsOfCell) ;
			for( int el=0;el<nbVertices;el++ )
				ci.addNodeId(el,nodeIdsOfCell[el]) ;

			/* Filling cell faces */
			if(_spaceDim==_meshDim)//use the normal field generated by buildOrthogonalField()
				for( int el=0;el<nbFaces;el++ )
				{
					vector<double> xyzn(3);
					for (int d=0; d<3; d++)
						xyzn[d] = 0.;
					if (work2[el]<0)
						for (int d=0; d<_spaceDim; d++)
							xyzn[d] = -tmpNormal[_spaceDim*work[el]+d];
					else
						for (int d=0; d<_spaceDim; d++)
							xyzn[d] = +tmpNormal[_spaceDim*work[el]+d];
					ci.addNormalVector(el,xyzn[0],xyzn[1],xyzn[2]) ;
					ci.addFaceId(el,work[el]) ;
				}
			else//build normals associated to the couple (cell id, face el)
			{
				if(_meshDim==1)//we know in this case there are only two faces around the cell id, each face is composed of a single node
				{//work[0]= first face global number, work[1]= second face global number
					int idNodeA=(tmpNE+tmpNEI[work[0]]+1)[0];//global number of the first face node
					int idNodeB=(tmpNE+tmpNEI[work[1]]+1)[0];//global number of the second face node
					Vector vecAB(3);
					for(int i=0;i<_spaceDim;i++)
						vecAB[i]=coo->getIJ(idNodeB,i) - coo->getIJ(idNodeA,i);
					vecAB/=vecAB.norm();
					ci.addNormalVector(0,-vecAB[0],-vecAB[1],-vecAB[2]) ;
					ci.addNormalVector(1,vecAB[0],vecAB[1],vecAB[2]) ;				
					ci.addFaceId(0,work[0]) ;
					ci.addFaceId(1,work[1]) ;	
				}
				else//_meshDim==2, number of faces around the cell id is variable, each face is composed of two nodes
				{
					Vector xyzn(3);//Normal to the cell
					for (int d=0; d<_spaceDim; d++)
						xyzn[d] = tmpNormal[_spaceDim*id+d];
					for( int el=0;el<nbFaces;el++ )
					{
						const int *workv=tmpNE+tmpNEI[work[el]]+1;
						int nbNodes= tmpNEI[work[el]+1]-tmpNEI[work[el]]-1;
						if(nbNodes!=2)//We want to compute the normal to a straight line, not a curved interface composed of more thant 2 points
						{
							cout<<"Mesh name "<< mu->getName()<< " space dim= "<< _spaceDim <<" mesh dim= "<< _meshDim <<endl;
							cout<<"For cell id "<<id<<" and local face number "<<el<<", the number of nodes is "<< nbNodes<< ", total number of faces is "<< nbFaces <<endl;
							throw CdmathException("Mesh::setMesh number of nodes around a face should be 2");
						}

						int idNodeA=workv[0];
						int idNodeB=workv[1];
						vector<double> nodeA(_spaceDim), nodeB(_spaceDim);
						for(int i=0;i<_spaceDim;i++)
						{
							nodeA[i]=coo->getIJ(idNodeA,i);
							nodeB[i]=coo->getIJ(idNodeB,i);
						}
						//Let P be the barycenter of the cell id
						//Let M be the barycenter of the face AB
						Vector vecAB(3), vecPM(3);
						for(int i=0;i<_spaceDim;i++)
						{
							vecAB[i]=coo->getIJ(idNodeB,i)       - coo->getIJ(idNodeA,i);
							vecPM[i]=coorBarySeg[_spaceDim*el+i] - coorBary[_spaceDim*id+i];
						}

						Vector normale = xyzn % vecAB;//Normal to the edge
						normale/=normale.norm();

						if(normale*vecPM<0)
							ci.addNormalVector(el,normale[0],normale[1],normale[2]) ;	
						else
							ci.addNormalVector(el,-normale[0],-normale[1],-normale[2]) ;	
						ci.addFaceId(el,work[el]) ;
					}
				}
			}
			_cells[id] = ci ;
		}

		/*Building mesh nodes */
		for(int id(0), k(0); id<_numberOfNodes; id++, k+=_spaceDim)
		{
			vector<double> coorP(3,0);
			for (int d=0; d<_spaceDim; d++)
				coorP[d] = cood[k+d];
			Point p(coorP[0],coorP[1],coorP[2]) ;

			const int *workc=tmpN+tmpNI[id];
			int nbCells=tmpNI[id+1]-tmpNI[id];
			const int *workf=tmpC+tmpCI[id];
			int nbFaces=tmpCI[id+1]-tmpCI[id];
			Node vi( nbCells, nbFaces, p ) ;

			for( int el=0;el<nbCells;el++ )
				vi.addCellId(el,workc[el]) ;
			for( int el=0;el<nbFaces;el++ )
				vi.addFaceId(el,workf[el]) ;
			_nodes[id] = vi ;
		}

		MEDCouplingFieldDouble* fieldl=m2->getMeasureField(true);
		DataArrayDouble *longueur = fieldl->getArray();
		const double *lon=longueur->getConstPointer();

		const double *normalFaces2;
		MEDCouplingFieldDouble * orthoField;
		if(_spaceDim==_meshDim)
		{
			orthoField = m2->buildOrthogonalField();
			const DataArrayDouble *normalFaces1 = orthoField->getArray() ;
			normalFaces2=normalFaces1->getConstPointer();
		}
		else
		{
			/* Since spaceDim!=meshDim, don't build normal to faces */
			orthoField=NULL;
			normalFaces2=NULL;
		}

		/*Building mesh faces */
		for(int id(0), k(0); id<_numberOfFaces; id++, k+=_spaceDim)
		{
			vector<double> coorBarySegXyz(3,0);
			for (int d=0; d<_spaceDim; d++)
				coorBarySegXyz[d] = coorBarySeg[k+d];
			Point p(coorBarySegXyz[0],coorBarySegXyz[1],coorBarySegXyz[2]) ;
			const int *workc=tmpA+tmpAI[id];
			int nbCells=tmpAI[id+1]-tmpAI[id];

			const int *workv=tmpNE+tmpNEI[id]+1;
			int nbNodes= tmpNEI[id+1]-tmpNEI[id]-1;

			Face fi;
			if(_spaceDim==_meshDim)//Euclidean flat mesh geometry
				fi=Face( nbNodes, nbCells, lon[id], p, normalFaces2[k], normalFaces2[k+1], 0.0) ;
			else//Curved mesh geometry
				fi=Face( nbNodes, nbCells, lon[id], p, 0.0, 0.0, 0.0) ;//Since spaceDim!=meshDim, normal to faces is not defined

			for(int node_id=0; node_id<nbNodes;node_id++)
				fi.addNodeId(node_id,workv[node_id]) ;

			fi.addCellId(0,workc[0]) ;
			if (nbCells==2)
				fi.addCellId(1,workc[1]) ;

			_faces[id] = fi ;
		}
		desc2->decrRef();
		descI2->decrRef();
		revDesc2->decrRef();
		revDescI2->decrRef();
		m3->decrRef();
		if(_spaceDim==_meshDim)
		{
			fieldn->decrRef();
			orthoField->decrRef();
		}
		fieldl->decrRef();
		barySeg->decrRef();
	}
	else
		throw CdmathException("Mesh::setMesh space dimension should be 1, 2 or 3");

	desc->decrRef();
	descI->decrRef();
	revDesc->decrRef();
	revDescI->decrRef();
	m2->decrRef();
	baryCell->decrRef();
	fields->decrRef();
	revNode->decrRef();
	revNodeI->decrRef();
	revCell->decrRef();
	revCellI->decrRef();

	return mu;
}

//----------------------------------------------------------------------
Mesh::Mesh( double xinf, double xsup, int nx, std::string meshName )
//----------------------------------------------------------------------
{
	if(nx<=0)
		throw CdmathException("Mesh::Mesh( double xinf, double xsup, int nx) : nx <= 0");
	if(xinf>=xsup)
		throw CdmathException("Mesh::Mesh( double xinf, double xsup, int nx) : xinf >= xsup");

	double dx = (xsup - xinf)/nx ;

	_spaceDim = 1 ;
	_meshDim  = 1 ;
    _isStructured = true;
	_xMin=xinf;
	_xSup=xsup;
	_yMin=0.;
	_ySup=0.;
	_zMin=0.;
	_zSup=0.;

	_dxyz.resize(_spaceDim);
	_dxyz[0]=dx;
	_nxyz.resize(_spaceDim);
	_nxyz[0]=nx;

	double *originPtr = new double[_spaceDim];
	double *dxyzPtr = new double[_spaceDim];
	int *nodeStrctPtr = new int[_spaceDim];

	originPtr[0]=xinf;
	nodeStrctPtr[0]=nx+1;
	dxyzPtr[0]=dx;


	_mesh=MEDCouplingIMesh::New(meshName,
			_spaceDim,
			nodeStrctPtr,
			nodeStrctPtr+_spaceDim,
			originPtr,
			originPtr+_spaceDim,
			dxyzPtr,
			dxyzPtr+_spaceDim);
	delete [] originPtr;
	delete [] dxyzPtr;
	delete [] nodeStrctPtr;

	DataArrayInt *desc=DataArrayInt::New();
	DataArrayInt *descI=DataArrayInt::New();
	DataArrayInt *revDesc=DataArrayInt::New();
	DataArrayInt *revDescI=DataArrayInt::New();
	MEDCouplingUMesh* mu=_mesh->buildUnstructured();
	MEDCouplingUMesh *m2=mu->buildDescendingConnectivity(desc,descI,revDesc,revDescI);
	m2->setName(mu->getName());

	DataArrayDouble *baryCell = mu->computeCellCenterOfMass() ;
	const double *coorBary=baryCell->getConstPointer();

	_numberOfCells = _mesh->getNumberOfCells() ;
	_cells    = new Cell[_numberOfCells] ;

	MEDCouplingFieldDouble* fieldl=mu->getMeasureField(true);
	DataArrayDouble *longueur = fieldl->getArray();
	const double *lon=longueur->getConstPointer();

	int comp=0;
	for( int id=0;id<_numberOfCells;id++ )
	{
		int nbVertices=mu->getNumberOfNodesInCell(id) ;
		Point p(coorBary[id],0.0,0.0) ;
		Cell ci( nbVertices, nbVertices, lon[id], p ) ;

		std::vector<int> nodeIdsOfCell ;
		mu->getNodeIdsOfCell(id,nodeIdsOfCell) ;
		for( int el=0;el<nbVertices;el++ )
		{
			ci.addNodeId(el,nodeIdsOfCell[el]) ;
			ci.addFaceId(el,nodeIdsOfCell[el]) ;
		}
		_cells[id] = ci ;
		comp=comp+2;
	}


	DataArrayInt *revNode=DataArrayInt::New();
	DataArrayInt *revNodeI=DataArrayInt::New();
	mu->getReverseNodalConnectivity(revNode,revNodeI) ;
	const int *tmpN=revNode->getConstPointer();
	const int *tmpNI=revNodeI->getConstPointer();

	_numberOfNodes = mu->getNumberOfNodes() ;
	_nodes    = new Node[_numberOfNodes] ;
	_numberOfFaces = _numberOfNodes;
	_faces    = new Face[_numberOfFaces] ;

	for( int id=0;id<_numberOfNodes;id++ )
	{
		std::vector<double> coo ;
		mu->getCoordinatesOfNode(id,coo);
		Point p(coo[0],0.0,0.0) ;
		const int *workc=tmpN+tmpNI[id];
		int nbCells=tmpNI[id+1]-tmpNI[id];
		int nbFaces=1;
		Node vi( nbCells, nbFaces, p ) ;
		int nbVertices=1;
		/* provisoire !!!!!!!!!!!!*/
		//        Point pf(0.0,0.0,0.0) ;
		Face fi( nbVertices, nbCells, 0.0, p, 0., 0., 0. ) ;

		for( int el=0;el<nbCells;el++ )
			vi.addCellId(el,workc[el]) ;
		for( int el=0;el<nbFaces;el++ )
			vi.addFaceId(el,id) ;
		_nodes[id] = vi ;

		for( int el=0;el<nbVertices;el++ )
			fi.addNodeId(el,id) ;

		for( int el=0;el<nbCells;el++ )
			fi.addCellId(el,workc[el]) ;
		_faces[id] = fi ;
	}
	fieldl->decrRef();
	baryCell->decrRef();
	desc->decrRef();
	descI->decrRef();
	revDesc->decrRef();
	revDescI->decrRef();
	revNode->decrRef();
	revNodeI->decrRef();
	m2->decrRef();
	mu->decrRef();
}

//----------------------------------------------------------------------
Mesh::Mesh( std::vector<double> points, std::string meshName )
//----------------------------------------------------------------------
{
    int nx=points.size();
    
	if(nx<2)
		throw CdmathException("Mesh::Mesh( vector<double> points, string meshName) : nx < 2, vector should contain at least two values");
    int i=0;
    while( i<nx-1 && points[i+1]>points[i] )
        i++;
	if( i!=nx-1 )
    {
        //cout<< points << endl;
		throw CdmathException("Mesh::Mesh( vector<double> points, string meshName) : vector values should be sorted");
    }
    
	_spaceDim = 1 ;
	_meshDim  = 1 ;
	_xMin=points[0];
	_xSup=points[nx-1];
	_yMin=0.;
	_ySup=0.;
	_zMin=0.;
	_zSup=0.;

    _isStructured = false;
    //Not relevant
	/*_dxyz.resize(_spaceDim);
	_dxyz[0]=dx;
	_nxyz.resize(_spaceDim);
	_nxyz[0]=nx;
    */
    
    MEDCouplingUMesh * mesh1d = MEDCouplingUMesh::New(meshName, 1);
    mesh1d->allocateCells(nx - 1);
    double * coords = new double[nx];
    int * nodal_con = new int[2];
    coords[0]=points[0];
    for(int i=0; i<nx- 1 ; i++)
    {
        nodal_con[0]=i;
        nodal_con[1]=i+1;
        mesh1d->insertNextCell(INTERP_KERNEL::NORM_SEG2, 2, nodal_con);
        coords[i+1]=points[i + 1];
    }
    mesh1d->finishInsertingCells();

    DataArrayDouble * coords_arr = DataArrayDouble::New();
    coords_arr->alloc(nx,1);
    std::copy(coords,coords+nx,coords_arr->getPointer());
    mesh1d->setCoords(coords_arr);

    delete [] coords, nodal_con;
    coords_arr->decrRef();

    _mesh=mesh1d;
    
	DataArrayInt *desc=DataArrayInt::New();
	DataArrayInt *descI=DataArrayInt::New();
	DataArrayInt *revDesc=DataArrayInt::New();
	DataArrayInt *revDescI=DataArrayInt::New();
    MEDCouplingUMesh* mu=_mesh->buildUnstructured();
	MEDCouplingUMesh *m2=mu->buildDescendingConnectivity(desc,descI,revDesc,revDescI);
	m2->setName(mu->getName());

	DataArrayDouble *baryCell = mu->computeCellCenterOfMass() ;
	const double *coorBary=baryCell->getConstPointer();

	_numberOfCells = _mesh->getNumberOfCells() ;
	_cells    = new Cell[_numberOfCells] ;

	MEDCouplingFieldDouble* fieldl=mu->getMeasureField(true);
	DataArrayDouble *longueur = fieldl->getArray();
	const double *lon=longueur->getConstPointer();

	int comp=0;
	for( int id=0;id<_numberOfCells;id++ )
	{
		int nbVertices=mu->getNumberOfNodesInCell(id) ;
		Point p(coorBary[id],0.0,0.0) ;
		Cell ci( nbVertices, nbVertices, lon[id], p ) ;

		std::vector<int> nodeIdsOfCell ;
		mu->getNodeIdsOfCell(id,nodeIdsOfCell) ;
		for( int el=0;el<nbVertices;el++ )
		{
			ci.addNodeId(el,nodeIdsOfCell[el]) ;
			ci.addFaceId(el,nodeIdsOfCell[el]) ;
		}
		_cells[id] = ci ;
		comp=comp+2;
	}


	DataArrayInt *revNode=DataArrayInt::New();
	DataArrayInt *revNodeI=DataArrayInt::New();
	mu->getReverseNodalConnectivity(revNode,revNodeI) ;
	const int *tmpN=revNode->getConstPointer();
	const int *tmpNI=revNodeI->getConstPointer();

	_numberOfNodes = mu->getNumberOfNodes() ;
	_nodes    = new Node[_numberOfNodes] ;
	_numberOfFaces = _numberOfNodes;
	_faces    = new Face[_numberOfFaces] ;

	for( int id=0;id<_numberOfNodes;id++ )
	{
		std::vector<double> coo ;
		mu->getCoordinatesOfNode(id,coo);
		Point p(coo[0],0.0,0.0) ;
		const int *workc=tmpN+tmpNI[id];
		int nbCells=tmpNI[id+1]-tmpNI[id];
		int nbFaces=1;
		Node vi( nbCells, nbFaces, p ) ;
		int nbVertices=1;
		/* provisoire !!!!!!!!!!!!*/
		//        Point pf(0.0,0.0,0.0) ;
		Face fi( nbVertices, nbCells, 0.0, p, 0., 0., 0. ) ;

		for( int el=0;el<nbCells;el++ )
			vi.addCellId(el,workc[el]) ;
		for( int el=0;el<nbFaces;el++ )
			vi.addFaceId(el,id) ;
		_nodes[id] = vi ;

		for( int el=0;el<nbVertices;el++ )
			fi.addNodeId(el,id) ;

		for( int el=0;el<nbCells;el++ )
			fi.addCellId(el,workc[el]) ;
		_faces[id] = fi ;
	}

	fieldl->decrRef();
	baryCell->decrRef();
	desc->decrRef();
	descI->decrRef();
	revDesc->decrRef();
	revDescI->decrRef();
	revNode->decrRef();
	revNodeI->decrRef();
	m2->decrRef();
	mu->decrRef();
}
//----------------------------------------------------------------------
Mesh::Mesh( double xinf, double xsup, int nx, double yinf, double ysup, int ny, std::string meshName)
//----------------------------------------------------------------------
{
	if(nx<=0 || ny<=0)
		throw CdmathException("Mesh::Mesh( double xinf, double xsup, int nx, double yinf, double ysup, int ny) : nx <= 0 or ny <= 0");
	if(xinf>=xsup)
		throw CdmathException("Mesh::Mesh( double xinf, double xsup, int nx, double yinf, double ysup, int ny) : xinf >= xsup");
	if(yinf>=ysup)
		throw CdmathException("Mesh::Mesh( double xinf, double xsup, int nx, double yinf, double ysup, int ny) : yinf >= ysup");
	_xMin=xinf;
	_xSup=xsup;
	_yMin=yinf;
	_ySup=ysup;
	_zMin=0.;
	_zSup=0.;


	double dx = (xsup - xinf)/nx ;
	double dy = (ysup - yinf)/ny ;

	_spaceDim = 2 ;
	_meshDim  = 2 ;
    _isStructured = true;
	_nxyz.resize(_spaceDim);
	_nxyz[0]=nx;
	_nxyz[1]=ny;

	_dxyz.resize(_spaceDim);
	_dxyz[0]=dx;
	_dxyz[1]=dy;

	double *originPtr = new double[_spaceDim];
	double *dxyzPtr = new double[_spaceDim];
	int *nodeStrctPtr = new int[_spaceDim];

	originPtr[0]=xinf;
	originPtr[1]=yinf;
	nodeStrctPtr[0]=nx+1;
	nodeStrctPtr[1]=ny+1;
	dxyzPtr[0]=dx;
	dxyzPtr[1]=dy;


	_mesh=MEDCouplingIMesh::New(meshName,
			_spaceDim,
			nodeStrctPtr,
			nodeStrctPtr+_spaceDim,
			originPtr,
			originPtr+_spaceDim,
			dxyzPtr,
			dxyzPtr+_spaceDim);
	delete [] originPtr;
	delete [] dxyzPtr;
	delete [] nodeStrctPtr;
	setMesh();
}

//----------------------------------------------------------------------
Mesh::Mesh( double xinf, double xsup, int nx, double yinf, double ysup, int ny, double zinf, double zsup, int nz, std::string meshName)
//----------------------------------------------------------------------
{
	if(nx<=0 || ny<=0 || nz<=0)
		throw CdmathException("Mesh::Mesh( double xinf, double xsup, int nx, double yinf, double ysup, int ny, double zinf, double zsup, int nz) : nx <= 0 or ny <= 0 or nz <= 0");
	if(xinf>=xsup)
		throw CdmathException("Mesh::Mesh( double xinf, double xsup, int nx, double yinf, double ysup, int ny, double zinf, double zsup, int nz) : xinf >= xsup");
	if(yinf>=ysup)
		throw CdmathException("Mesh::Mesh( double xinf, double xsup, int nx, double yinf, double ysup, int ny, double zinf, double zsup, int nz) : yinf >= ysup");
	if(zinf>=zsup)
		throw CdmathException("Mesh::Mesh( double xinf, double xsup, int nx, double yinf, double ysup, int ny, double zinf, double zsup, int nz) : zinf >= zsup");

	_spaceDim = 3;
	_meshDim  = 3;
	_xMin=xinf;
	_xSup=xsup;
	_yMin=yinf;
	_ySup=ysup;
	_zMin=zinf;
	_zSup=zsup;

	double dx = (xsup - xinf)/nx ;
	double dy = (ysup - yinf)/ny ;
	double dz = (zsup - zinf)/nz ;

    _isStructured = true;
	_dxyz.resize(_spaceDim);
	_dxyz[0]=dx;
	_dxyz[1]=dy;
	_dxyz[2]=dz;

	_nxyz.resize(_spaceDim);
	_nxyz[0]=nx;
	_nxyz[1]=ny;
	_nxyz[2]=nz;

	double *originPtr = new double[_spaceDim];
	double *dxyzPtr = new double[_spaceDim];
	int *nodeStrctPtr = new int[_spaceDim];

	originPtr[0]=xinf;
	originPtr[1]=yinf;
	originPtr[2]=zinf;
	nodeStrctPtr[0]=nx+1;
	nodeStrctPtr[1]=ny+1;
	nodeStrctPtr[2]=nz+1;
	dxyzPtr[0]=dx;
	dxyzPtr[1]=dy;
	dxyzPtr[2]=dz;


	_mesh=MEDCouplingIMesh::New(meshName,
			_spaceDim,
			nodeStrctPtr,
			nodeStrctPtr+_spaceDim,
			originPtr,
			originPtr+_spaceDim,
			dxyzPtr,
			dxyzPtr+_spaceDim);
	delete [] originPtr;
	delete [] dxyzPtr;
	delete [] nodeStrctPtr;
	setMesh();
}

//----------------------------------------------------------------------
int
Mesh::getSpaceDimension( void )  const
//----------------------------------------------------------------------
{
	return _spaceDim ;
}

//----------------------------------------------------------------------
int
Mesh::getMeshDimension( void )  const
//----------------------------------------------------------------------
{
	return _meshDim ;
}

std::vector<double>
Mesh::getDXYZ() const
{
    if(!_isStructured)
		throw CdmathException("std::vector<double> Mesh::getDXYZ() : dx,dy and dz are defined only for structured meshes !");

	return _dxyz;
}

std::vector<int>
Mesh::getCellGridStructure() const
{
    if(!_isStructured)
		throw CdmathException("std::vector<int> Mesh::getCellGridStructure() : nx, ny and nz are defined only for structured meshes !");

	return _nxyz;
}

//----------------------------------------------------------------------
int
Mesh::getNx( void )  const
//----------------------------------------------------------------------
{
    if(!_isStructured)
		throw CdmathException("int Mesh::getNx( void ) : Nx is defined only for structured meshes !");

	return _nxyz[0];
}

//----------------------------------------------------------------------
int
Mesh::getNy( void )  const
//----------------------------------------------------------------------
{
    if(!_isStructured)
		throw CdmathException("int Mesh::getNy( void ) : Ny is defined only for structured meshes !");
	if(_spaceDim < 2)
		throw CdmathException("int double& Field::operator[ielem] : Ny is not defined in dimension < 2!");

	return _nxyz[1];
}

//----------------------------------------------------------------------
int
Mesh::getNz( void )  const
//----------------------------------------------------------------------
{
    if(!_isStructured)
		throw CdmathException("int Mesh::getNz( void ) : Nz is defined only for structured meshes !");
	if(_spaceDim < 3)
		throw CdmathException("int Mesh::getNz( void ) : Nz is not defined in dimension < 3!");

	return _nxyz[2];
}

//----------------------------------------------------------------------
double
Mesh::getXMin( void )  const
//----------------------------------------------------------------------
{
    if(!_isStructured)
		throw CdmathException("double Mesh::getXmin( void ) : xMin is defined only for structured meshes !");
        
	return _xMin ;
}

//----------------------------------------------------------------------
double
Mesh::getXSup( void )  const
//----------------------------------------------------------------------
{
    if(!_isStructured)
		throw CdmathException("double Mesh::getXsup( void ) : xSup is defined only for structured meshes !");
        
	return _xSup ;
}

//----------------------------------------------------------------------
double
Mesh::getYMin( void )  const
//----------------------------------------------------------------------
{
    if(!_isStructured)
		throw CdmathException("double Mesh::getYmin( void ) : yMin is defined only for structured meshes !");
        
	return _yMin ;
}

//----------------------------------------------------------------------
double
Mesh::getYSup( void )  const
//----------------------------------------------------------------------
{
    if(!_isStructured)
		throw CdmathException("double Mesh::getYSup( void ) : ySup is defined only for structured meshes !");
        
	return _ySup ;
}

//----------------------------------------------------------------------
double
Mesh::getZMin( void )  const
//----------------------------------------------------------------------
{
    if(!_isStructured)
		throw CdmathException("double Mesh::getZmin( void ) : zMin is defined only for structured meshes !");

	return _zMin ;
}

//----------------------------------------------------------------------
double
Mesh::getZSup( void )  const
//----------------------------------------------------------------------
{
    if(!_isStructured)
		throw CdmathException("double Mesh::getZSup( void ) : zSup is defined only for structured meshes !");

	return _zSup ;
}

//----------------------------------------------------------------------
MCAuto<MEDCouplingMesh>
Mesh::getMEDCouplingMesh( void )  const
//----------------------------------------------------------------------
{
	return _mesh ;
}

//----------------------------------------------------------------------
int
Mesh::getNumberOfNodes ( void ) const
//----------------------------------------------------------------------
{
	return _numberOfNodes ;
}

//----------------------------------------------------------------------
int
Mesh::getNumberOfCells ( void ) const
//----------------------------------------------------------------------
{
	return _numberOfCells ;
}

//----------------------------------------------------------------------
int
Mesh::getNumberOfFaces ( void ) const
//----------------------------------------------------------------------
{
	return _numberOfFaces ;
}

//----------------------------------------------------------------------
Face*
Mesh::getFaces ( void )  const
//----------------------------------------------------------------------
{
	return _faces ;
}

//----------------------------------------------------------------------
Cell*
Mesh::getCells ( void ) const
//----------------------------------------------------------------------
{
	return _cells ;
}

//----------------------------------------------------------------------
Cell&
Mesh::getCell ( int i ) const
//----------------------------------------------------------------------
{
	return _cells[i] ;
}

//----------------------------------------------------------------------
Face&
Mesh::getFace ( int i ) const
//----------------------------------------------------------------------
{
	return _faces[i] ;
}

//----------------------------------------------------------------------
Node&
Mesh::getNode ( int i ) const
//----------------------------------------------------------------------
{
	return _nodes[i] ;
}

//----------------------------------------------------------------------
Node*
Mesh::getNodes ( void )  const
//----------------------------------------------------------------------
{
	return _nodes ;
}

vector<string>
Mesh::getNamesOfGroups( void )  const
{
	return _groupNames;
}

vector<MEDCoupling::MEDCouplingUMesh *>
Mesh::getGroups( void )  const
{
	return _groups;
}

//----------------------------------------------------------------------
const Mesh&
Mesh::operator= ( const Mesh& mesh )
//----------------------------------------------------------------------
{
	_spaceDim = mesh.getSpaceDimension() ;
	_meshDim  = mesh.getMeshDimension() ;
	_numberOfNodes = mesh.getNumberOfNodes();
	_numberOfFaces = mesh.getNumberOfFaces();
	_numberOfCells = mesh.getNumberOfCells();
    _isStructured = mesh.isStructured();
    if(_isStructured)
    {
        _nxyz = mesh.getCellGridStructure() ;
        _dxyz=mesh.getDXYZ();
        _xMin=mesh.getXMin();
        _xSup=mesh.getXSup();
        _yMin=mesh.getYMin();
        _ySup=mesh.getYSup();
        _zMin=mesh.getZMin();
        _zSup=mesh.getZSup();
    }
	_groupNames = mesh.getNamesOfGroups() ;
	_groups = mesh.getGroups() ;
	if (_nodes)
	{
		delete [] _nodes ;
		_nodes=NULL;
	}
	if (_faces)
	{
		delete [] _faces ;
		_faces=NULL;
	}
	if (_cells)
	{
		delete [] _cells ;
		_cells=NULL;
	}

	_nodes   = new Node[_numberOfNodes] ;
	_faces   = new Face[_numberOfFaces] ;
	_cells   = new Cell[_numberOfCells] ;

	for (int i=0;i<_numberOfNodes;i++)
		_nodes[i]=mesh.getNode(i);

	for (int i=0;i<_numberOfFaces;i++)
		_faces[i]=mesh.getFace(i);

	for (int i=0;i<_numberOfCells;i++)
		_cells[i]=mesh.getCell(i);

	MCAuto<MEDCouplingMesh> m1=mesh.getMEDCouplingMesh()->deepCopy();
	_mesh=m1;
	return *this;
}

//----------------------------------------------------------------------
void
Mesh::writeVTK ( const std::string fileName ) const
//----------------------------------------------------------------------
{
	string fname=fileName+".vtu";
	_mesh->writeVTK(fname.c_str()) ;
}

//----------------------------------------------------------------------
void
Mesh::writeMED ( const std::string fileName ) const
//----------------------------------------------------------------------
{
	string fname=fileName+".med";
	MEDCouplingUMesh* mu=_mesh->buildUnstructured();
	MEDCoupling::WriteUMesh(fname.c_str(),mu,true);

	//MEDFileUMesh meshMEDFile;
	//meshMEDFile.setMeshAtLevel(0,mu);
	//for(int i=0; i< _groups.size(); i++)
	//meshMEDFile.setMeshAtLevel(-1,_groups[i]);
	//if (fromScratch)
	//MEDCoupling::meshMEDFile.write(fname.c_str(),2)	;
	//else
	//MEDCoupling::meshMEDFile.write(fname.c_str(),1)	;


	mu->decrRef();
}
