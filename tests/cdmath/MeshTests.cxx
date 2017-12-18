/*
 * meshtests.cxx
 *
 *  Created on: 24 janv. 2012
 *      Authors: CDMATH
 */

#include "MeshTests.hxx"
#include "MEDLoader.hxx"
#include "Face.hxx"
#include "Cell.hxx"
#include "Node.hxx"

#include <string>
#include <cmath>

using namespace MEDCoupling;
using namespace std;

//----------------------------------------------------------------------
void
MeshTests::testClassMesh( void )
//----------------------------------------------------------------------
{
	double eps=1.E-10;

	// Testing Mesh(xinf, xsup, nx)
	Mesh M1(0.0,4.0,4);
	CPPUNIT_ASSERT_EQUAL( 1, M1.getSpaceDimension() );
	CPPUNIT_ASSERT_EQUAL( 5, M1.getNumberOfNodes() );
	CPPUNIT_ASSERT_EQUAL( 4, M1.getNumberOfCells() );
	CPPUNIT_ASSERT_EQUAL( 5, M1.getNumberOfFaces() );
	CPPUNIT_ASSERT_EQUAL( 0., M1.getFace(0).x() );
	CPPUNIT_ASSERT_EQUAL( 0., M1.getNode(0).x() );
	CPPUNIT_ASSERT_EQUAL( 1., M1.getFace(1).x() );
	CPPUNIT_ASSERT_EQUAL( 1., M1.getNode(1).x() );
	CPPUNIT_ASSERT_EQUAL( 2., M1.getFace(2).x() );
	CPPUNIT_ASSERT_EQUAL( 2., M1.getNode(2).x() );
	CPPUNIT_ASSERT_EQUAL( 3., M1.getFace(3).x() );
	CPPUNIT_ASSERT_EQUAL( 3., M1.getNode(3).x() );
	CPPUNIT_ASSERT_EQUAL( 4., M1.getFace(4).x() );
	CPPUNIT_ASSERT_EQUAL( 4., M1.getNode(4).x() );
	double x11=M1.getCells()[1].x();
	double y11=M1.getCells()[1].y();
	CPPUNIT_ASSERT_EQUAL( x11, 1.5 );
	CPPUNIT_ASSERT_EQUAL( y11, 0.0 );
	M1.setGroupAtFaceByCoords(0.,0.,0.,1.E-14,"LeftEdge") ;
	M1.setGroupAtFaceByCoords(4.,0.,0.,1.E-14,"RightEdge") ;
	CPPUNIT_ASSERT(M1.getFace(0).isBorder()==true);
	CPPUNIT_ASSERT(M1.getFace(1).isBorder()==false);
	CPPUNIT_ASSERT(M1.getFace(2).isBorder()==false);
	CPPUNIT_ASSERT(M1.getFace(3).isBorder()==false);
	CPPUNIT_ASSERT(M1.getFace(4).isBorder()==true);
	CPPUNIT_ASSERT(M1.getNamesOfGroups()[0].compare("LeftEdge")==0);
	CPPUNIT_ASSERT(M1.getNamesOfGroups()[1].compare("RightEdge")==0);


	// Testing Mesh(xinf, xsup, nx, yinf, ysup, ny)
	double xinf=0.0;
	double xsup=4.0;
	double yinf=0.0;
	double ysup=4.0;
	Mesh M2(xinf,xsup,4,yinf,ysup,4);
	CPPUNIT_ASSERT_EQUAL( 4, M2.getNx() );
	CPPUNIT_ASSERT_EQUAL( 4, M2.getNy() );
	CPPUNIT_ASSERT_EQUAL( 2, M2.getSpaceDimension() );
	CPPUNIT_ASSERT_EQUAL( 25, M2.getNumberOfNodes() );
	CPPUNIT_ASSERT_EQUAL( 16, M2.getNumberOfCells() );
	CPPUNIT_ASSERT_EQUAL( 40, M2.getNumberOfFaces() );
	CPPUNIT_ASSERT(M2.isQuadrangular());
	int nbCellsM2 = M2.getNumberOfCells();
	double areaM2=0;
	for(int i=0; i<nbCellsM2; i++)
		areaM2+=M2.getCell(i).getMeasure();
	CPPUNIT_ASSERT_DOUBLES_EQUAL( 16., areaM2, eps );
	double x1=M2.getCells()[4].x();
	double y1=M2.getCells()[4].y();
	CPPUNIT_ASSERT_EQUAL( x1, 0.5 );
	CPPUNIT_ASSERT_EQUAL( y1, 1.5 );

	double x2=M2.getNodes()[24].x();
	double y2=M2.getNodes()[24].y();
	CPPUNIT_ASSERT_EQUAL( x2, 4. );
	CPPUNIT_ASSERT_EQUAL( y2, 4. );

	M2.setGroupAtPlan(xsup,0,eps,"RightEdge");
	M2.setGroupAtPlan(xinf,0,eps,"LeftEdge");
	M2.setGroupAtPlan(yinf,1,eps,"BottomEdge");
	M2.setGroupAtPlan(ysup,1,eps,"TopEdge");
	CPPUNIT_ASSERT_EQUAL( 4, int(M2.getNamesOfGroups().size()) );
	CPPUNIT_ASSERT(M2.getNamesOfGroups()[2].compare("BottomEdge")==0);
	int nbFaces=M2.getNumberOfFaces();
	IntTab indexFaces=M2.getIndexFacePeriodic();
	for (int i=0;i<nbFaces;i++)
	{
		double x=M2.getFaces()[i].x();
		double y=M2.getFaces()[i].y();
		if (y==0. && x==0.5)
		{
			int indexFace=M2.getIndexFacePeriodic(i);
			double xi=M2.getFace(indexFace).x();
			double yi=M2.getFace(indexFace).y();
			CPPUNIT_ASSERT_EQUAL( xi, x );
			CPPUNIT_ASSERT_EQUAL( yi, ysup );
			CPPUNIT_ASSERT_EQUAL( true, M2.getFace(indexFace).isBorder() );
			CPPUNIT_ASSERT_EQUAL( indexFace, indexFaces(i) );
		}

		if (y==0.5 && x==1.)
			CPPUNIT_ASSERT_EQUAL( -1, M2.getIndexFacePeriodic(i) );
	}


	// Testing Mesh(xinf, xsup, nx, yinf, ysup, ny, zinf, zsup, nz) (hexaèdres)
    		Mesh M3(0.0,1.0,4,0.0,1.0,4,0.0,1.0,4);
    		CPPUNIT_ASSERT_EQUAL( 3, M3.getSpaceDimension() );
    		CPPUNIT_ASSERT(M3.isHexahedral());
    		int nbCellsM3 = M3.getNumberOfCells();
    		double volM3=0;
    		for(int i=0; i<nbCellsM3; i++)
    			volM3+=M3.getCell(i).getMeasure();
    		CPPUNIT_ASSERT_DOUBLES_EQUAL( 1., volM3, eps );

    		// Testing copies
    		Mesh Mcopy1(M1);
    		CPPUNIT_ASSERT_EQUAL( 1, Mcopy1.getSpaceDimension() );
    		CPPUNIT_ASSERT_EQUAL( 5, Mcopy1.getNumberOfNodes() );
    		CPPUNIT_ASSERT_EQUAL( 4, Mcopy1.getNumberOfCells() );
    		CPPUNIT_ASSERT_EQUAL( 5, Mcopy1.getNumberOfFaces() );

    		Mcopy1=M2;
    		CPPUNIT_ASSERT_EQUAL( 2, Mcopy1.getSpaceDimension() );
    		CPPUNIT_ASSERT_EQUAL( 25, Mcopy1.getNumberOfNodes() );
    		CPPUNIT_ASSERT_EQUAL( 16, Mcopy1.getNumberOfCells() );
    		CPPUNIT_ASSERT_EQUAL( 40, Mcopy1.getNumberOfFaces() );

    		Mesh Mcopy2;
    		Mcopy2=Mcopy1;
    		CPPUNIT_ASSERT_EQUAL( 2, Mcopy2.getSpaceDimension() );
    		CPPUNIT_ASSERT_EQUAL( 25, Mcopy2.getNumberOfNodes() );
    		CPPUNIT_ASSERT_EQUAL( 16, Mcopy2.getNumberOfCells() );
    		CPPUNIT_ASSERT_EQUAL( 40, Mcopy2.getNumberOfFaces() );


    		// Connection with MED
    		string fileNameVTK="TestMesh";
    		string fileNameMED="TestMesh";

    		M2.writeMED(fileNameMED);
    		Mesh M22(fileNameMED + ".med");
    		CPPUNIT_ASSERT_EQUAL( 2, M22.getSpaceDimension() );
    		CPPUNIT_ASSERT_EQUAL( 25, M22.getNumberOfNodes() );
    		CPPUNIT_ASSERT_EQUAL( 16, M22.getNumberOfCells() );
    		CPPUNIT_ASSERT_EQUAL( 40, M22.getNumberOfFaces() );

    		//Testing a 2D unstructured mesh (triangles)
    		Mesh M23("mesh.med");
    		CPPUNIT_ASSERT(M23.getNamesOfGroups()[0].compare("BORD1")==0);
    		CPPUNIT_ASSERT(M23.getNamesOfGroups()[1].compare("BORD2")==0);
    		CPPUNIT_ASSERT(M23.getNamesOfGroups()[2].compare("BORD3")==0);
    		CPPUNIT_ASSERT(M23.getNamesOfGroups()[3].compare("BORD4")==0);
    		CPPUNIT_ASSERT(M23.isTriangular());
    		int nbCellsM23 = M23.getNumberOfCells();
    		double areaM23=0;
    		for(int i=0; i<nbCellsM23; i++)
    			areaM23+=M23.getCell(i).getMeasure();
    		CPPUNIT_ASSERT_DOUBLES_EQUAL( 1., areaM23 , eps);

    		Mcopy2.writeVTK(fileNameVTK);
    		Mcopy2.writeMED(fileNameMED);
    		Mesh M6(fileNameMED + ".med");
    		CPPUNIT_ASSERT_EQUAL( 2, M6.getSpaceDimension() );
    		CPPUNIT_ASSERT_EQUAL( 25, M6.getNumberOfNodes() );
    		CPPUNIT_ASSERT_EQUAL( 16, M6.getNumberOfCells() );
    		CPPUNIT_ASSERT_EQUAL( 40, M6.getNumberOfFaces() );

    		/*
    		const MEDCouplingMesh* M1MEDMesh = M2.getMEDCouplingMesh();
    		 */

    		//Test of a mesh with spaceDim=3 different from meshDim=2 (triangles)
    		Mesh M4("Sphere106Cells.med");
    		CPPUNIT_ASSERT(M4.isTriangular());
    		int nbCellsM4 = M4.getNumberOfCells();
    		double areaM4=0;
    		for(int i=0; i<nbCellsM4; i++)
    			areaM4+=M4.getCell(i).getMeasure();
    		CPPUNIT_ASSERT_DOUBLES_EQUAL( 120000., areaM4, 2000 );//

    		//Testing a 3D unstructured mesh (tétraèdres)
    		Mesh M5("Mesh_3D_5000.med");
    		CPPUNIT_ASSERT(M5.isTetrahedral());
    		int nbCellsM5 = M5.getNumberOfCells();
    		double volM5=0;
    		for(int i=0; i<nbCellsM5; i++)
    			volM5+=M5.getCell(i).getMeasure();
    		CPPUNIT_ASSERT_DOUBLES_EQUAL( 1., volM5, eps );
}
