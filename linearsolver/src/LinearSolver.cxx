/**
 * LinearSolver.cxx
 *
 *  Created on: 15 avr. 2013
 *      Author: mekkas
 */

#include <cmath>
#include <string>

#include <petscksp.h>
#include <petscmat.h>
#include <petscvec.h>

#include "CdmathException.hxx"
#include "LinearSolver.hxx"
#include "SparseMatrix.hxx"
#include "SparseMatrixPetsc.hxx"

using namespace std;


LinearSolver::LinearSolver ( void )
{
    _tol=1.E-15;
    _numberMaxOfIter=0;
    _residu=1.E30;
    _convergence=false;
    _numberOfIter=0;
    _isSingular=false;
    _nameOfPc="";
    _nameOfMethod="";
    _mat=NULL;
    _smb=NULL;
    _ksp=NULL;
    _prec=NULL;
    _isSparseMatrix=false;
    _displayConditionNumber=false;
}

void
LinearSolver::kspDuplicate(const KSP source, const Mat mat, KSP* destination) const
{
    KSPCreate(PETSC_COMM_WORLD,&(*destination));
    #ifdef PETSC_VERSION_GREATER_3_5
        KSPSetOperators(*destination,mat,mat);
    #else
        KSPSetOperators(*destination,mat,mat,SAME_NONZERO_PATTERN);
    #endif
    KSPType type;
    KSPGetType(source,&type);
    KSPSetType(*destination,type);
	/*
    PetscReal tol1,tol2,tol3;
    PetscInt maxIter;
    KSPGetTolerances(source,&tol1,&tol2,&tol3,&maxIter);
    KSPSetTolerances(*destination,tol1,tol2,tol3,maxIter);
	// */
}

void
LinearSolver::precDuplicate(const PC source, const KSP ksp, PC* destination)  const
{
	KSPGetPC(ksp,destination);
    PCType type;
    PCGetType(source,&type);
    PCSetType(*destination,type);
}

LinearSolver::~LinearSolver ( void )
{
	//if(&_mat != NULL)
	//	MatDestroy(&_mat);
	if(&_smb != NULL)
		VecDestroy(&_smb);
    KSPDestroy(&_ksp);
    //PetscFinalize();
}

void
LinearSolver::setTolerance(double tol)
{
    _tol=tol;
    KSPSetTolerances(_ksp,tol,PETSC_DEFAULT,PETSC_DEFAULT,getNumberMaxOfIter());
}

void
LinearSolver::setNumberMaxOfIter(int numberMaxOfIter)
{
    _numberMaxOfIter=numberMaxOfIter;
    KSPSetTolerances(_ksp,getTolerance(),PETSC_DEFAULT,PETSC_DEFAULT,numberMaxOfIter);
}

void
LinearSolver::setDisplayConditionNumber(bool display)
{
    _displayConditionNumber=display;
}

LinearSolver::LinearSolver( const GenericMatrix& matrix,
		const Vector& secondMember,
		int numberMaxOfIter,
		double tol,
		string nameOfMethod,
		string nameOfPc )
{
    _tol = tol;
    _numberMaxOfIter = numberMaxOfIter;
    _residu = 1.E30;
    _convergence = false;
    _numberOfIter = 0;
    _isSingular = false;
    _isSparseMatrix = matrix.isSparseMatrix();
    _displayConditionNumber=false;    
    _nameOfPc = nameOfPc;
    _nameOfMethod = nameOfMethod;
    _secondMember = secondMember;
	_mat = NULL;
	_smb = NULL;
	_prec = NULL;
	_ksp = NULL;

	//setTolerance(tol);
	//setNumberMaxOfIter(numberMaxOfIter);
    setPreconditioner(nameOfPc);
    setMethod(nameOfMethod);
    setLinearSolver(matrix, secondMember);
}


void
LinearSolver::setPreconditioner(string pc)
{
    if((pc.compare("ICC") != 0) && (pc.compare("ILU") != 0) && (pc.compare("LU") != 0) && (pc.compare("") != 0))
    {
        string msg="LinearSolver::LinearSolver: preconditioner "+pc+" does not exist.\n";
        throw CdmathException(msg);
    }
    if ((pc.compare("ICC")==0 || pc.compare("ILU")==0) && _isSparseMatrix==false)
    {
        string msg="LinearSolver::LinearSolver: preconditioner "+pc+" is not compatible with dense matrix.\n";
        throw CdmathException(msg);
    }

    if ((pc.compare("ICC")==0 || pc.compare("ILU")==0) && (_nameOfMethod.compare("LU")==0 || _nameOfMethod.compare("CHOLESKY")==0 ))
    {
        string msg="LinearSolver::LinearSolver: preconditioner "+pc+" is not compatible with "+_nameOfMethod+".\n";
        throw CdmathException(msg);
    }
    _nameOfPc=pc;
}


void
LinearSolver::setMethod(string nameOfMethod)
{
    _nameOfMethod = nameOfMethod;

    if ((_nameOfPc.compare("ICC")==0 || _nameOfPc.compare("ILU")==0) && (_nameOfMethod.compare("LU")==0 || _nameOfMethod.compare("CHOLESKY")==0) )
    {
        string msg="LinearSolver::LinearSolver: preconditioner "+_nameOfPc+" is not compatible with "+_nameOfMethod+".\n";
        throw CdmathException(msg);
    }
}


void
LinearSolver::setLinearSolver(const GenericMatrix& matrix, const Vector& secondMember)
{
    if ((_nameOfPc.compare("ICC")==0 || _nameOfPc.compare("ILU")==0) && _isSparseMatrix==false)
    {
        string msg="LinearSolver::LinearSolver: preconditioner "+_nameOfPc+" is not compatible with dense matrix.\n";
        throw CdmathException(msg);
    }

    PetscInitialize(0, (char ***)"", PETSC_NULL, PETSC_NULL);
    setMatrix(matrix);
    setSndMember(secondMember);
}


bool
LinearSolver::isSparseMatrix( void ) const
{
    return (_isSparseMatrix);
}

bool
LinearSolver::isSingular( void ) const
{
    return (_isSingular);
}

int
LinearSolver::getNumberOfIter( void ) const
{
    return (_numberOfIter);
}

bool
LinearSolver::getStatus( void ) const
{
    return (_convergence);
}

double
LinearSolver::getResidu( void ) const
{
    return (_residu);
}

double
LinearSolver::getTolerance(void) const
{
    return (_tol);
}

int
LinearSolver::getNumberMaxOfIter(void) const
{
    return (_numberMaxOfIter);
}

void
LinearSolver::setMatrix(const GenericMatrix& matrix)
{
    /* matrix to mat */
    int numberOfRows=matrix.getNumberOfRows();
    int numberOfColumns=matrix.getNumberOfColumns();

    if (matrix.isSparseMatrix())
    {
		if(matrix.containsPetscMatrix())
		{
         const SparseMatrixPetsc& Smat = dynamic_cast<const SparseMatrixPetsc&>(matrix);
		_mat=Smat.getPetscMatrix();
		}
		else
		{
        const SparseMatrix& Smat = dynamic_cast<const SparseMatrix&>(matrix);
        PetscInt nnz[numberOfRows];
        IntTab iRows=Smat.getIndexRows();
        IntTab iColumns=Smat.getIndexColumns();
        for (int i=0;i<numberOfRows;i++)
            nnz[i]=iRows[i+1]-iRows[i];
        MatCreateSeqAIJ(MPI_COMM_SELF,numberOfRows,numberOfColumns,PETSC_DEFAULT,nnz,&_mat);
        DoubleTab values=Smat.getValues();
        for (int i=0;i<numberOfRows;i++)
        {
            PetscInt    cols[nnz[i]];
            PetscScalar    vals[nnz[i]];
           for (int j=0;j<nnz[i];j++)
            {
                cols[j]=iColumns[iRows[i]+j]-1;
                vals[j]=values[iRows[i]+j];
            }
            MatSetValues(_mat,1,
                        &i,
                        nnz[i],
                        cols,
                        vals,INSERT_VALUES);
        }
		}
    } 
    else
    {
        MatCreate(PETSC_COMM_WORLD, &_mat);
        MatSetSizes(_mat, PETSC_DECIDE, PETSC_DECIDE, numberOfRows, numberOfColumns);
        MatSetType(_mat,MATSEQDENSE);

        PetscScalar *a;
        PetscMalloc(numberOfRows*numberOfColumns*sizeof(PetscScalar),&a);
        for (int i=0;i<numberOfRows;i++)
            for (int j=0;j<numberOfColumns;j++)
                a[i+j*numberOfRows]=matrix(i,j);

        MatSeqDenseSetPreallocation(_mat,a);
    }
    //Assemblage final
    MatAssemblyBegin(_mat, MAT_FINAL_ASSEMBLY);
    MatAssemblyEnd(_mat, MAT_FINAL_ASSEMBLY);

    KSPCreate(PETSC_COMM_WORLD, &_ksp);
    #ifdef PETSC_VERSION_GREATER_3_5
        KSPSetOperators(_ksp,_mat,_mat);
    #else
        KSPSetOperators(_ksp,_mat,_mat,SAME_NONZERO_PATTERN);
    #endif

    KSPGetPC(_ksp,&_prec);
}

void
LinearSolver::setSndMember(const Vector& secondMember)
{
    _secondMember=secondMember;
    if(&_smb!=NULL)
		VecDestroy(&_smb);
    _smb=vectorToVec(secondMember);

}

void
LinearSolver::setSingularity(bool sing)
{
    _isSingular=sing;
}

Vector
LinearSolver::getSndMember(void) const
{
    return (_secondMember);
}

string
LinearSolver::getNameOfMethod(void) const
{
    return (_nameOfMethod);
}

string
LinearSolver::getNameOfPc(void) const
{
    return (_nameOfPc);
}

LinearSolver::LinearSolver ( const LinearSolver& LS )
{
    _tol=LS.getTolerance();
    _nameOfMethod=LS.getNameOfMethod();
    _numberMaxOfIter=LS.getNumberMaxOfIter();
    _secondMember=LS.getSndMember();
    _residu=LS.getResidu();
    _convergence=LS.getStatus();
    _numberOfIter=LS.getNumberOfIter();
    _isSingular=LS.isSingular();
    _nameOfPc=LS.getNameOfPc();
    _mat=NULL;
    MatDuplicate(LS.getPetscMatrix(),MAT_COPY_VALUES,&_mat);
    _smb=NULL;
    VecDuplicate(LS.getPetscVector(),&_smb);    				;
    _ksp=NULL;
    kspDuplicate(LS.getPetscKsp(),_mat,&_ksp);
    _prec=NULL;
    precDuplicate(LS.getPetscPc(),_ksp,&_prec);
//    _ksp=LS.getPetscKsp();
//    _prec=LS.getPetscPc();
    _isSparseMatrix=LS.isSparseMatrix();
}

KSP
LinearSolver::getPetscKsp() const
{
    return (_ksp);
}

Mat
LinearSolver::getPetscMatrix() const
{
    return (_mat);
}

Vec
LinearSolver::getPetscVector() const
{
    return (_smb);
}

void
LinearSolver::viewPetscMatrix() const 
{
	MatView(_mat,PETSC_VIEWER_STDOUT_SELF);
}
void
LinearSolver::viewPetscRHS() const 
{
	VecView(_smb,PETSC_VIEWER_STDOUT_SELF);
}
double
LinearSolver::getPetscMatValue(int i, int j) const 
{
	double res;
	int idxm=i,idxn=j;
	MatGetValues(_mat,1,&idxm,1, &idxn,&res);
	return res;
}
double
LinearSolver::getPetscRHSValue(int i) const 
{
	double res;
	int idxm=i;
	VecGetValues(_smb,1,&idxm,&res);
	return res;
}
PC
LinearSolver::getPetscPc() const
{
    return (_prec);
}

Vector
LinearSolver::solve( void )
{

    PetscInitialize(0,(char ***)"", PETSC_NULL, PETSC_NULL);

    if (_nameOfMethod.compare("GMRES")==0)
       KSPSetType(_ksp,KSPGMRES);
    else if (_nameOfMethod.compare("LGMRES")==0)
        KSPSetType(_ksp,KSPLGMRES);
    else if (_nameOfMethod.compare("CG")==0)
        KSPSetType(_ksp,KSPCG);
    else if (_nameOfMethod.compare("BCG")==0)
        KSPSetType(_ksp,KSPBCGS);
    else if (_nameOfMethod.compare("CR")==0)
        KSPSetType(_ksp,KSPCR);
    else if (_nameOfMethod.compare("CGS")==0)
        KSPSetType(_ksp,KSPCGS);
    else if (_nameOfMethod.compare("BICG")==0)
        KSPSetType(_ksp,KSPBICG);
    else if (_nameOfMethod.compare("GCR")==0)
        KSPSetType(_ksp,KSPGCR);
    else if (_nameOfMethod.compare("LSQR")==0)
        KSPSetType(_ksp,KSPLSQR);
    else if (_nameOfMethod.compare("CHOLESKY")==0)
		{
        KSPSetType(_ksp,KSPGMRES);			
        PCSetType(_prec,PCCHOLESKY);
		}
    else if (_nameOfMethod.compare("LU")==0)
		{
        KSPSetType(_ksp,KSPGMRES);			
        PCSetType(_prec,PCLU);
		}
    else
    {
        string msg="Vector LinearSolver::solve( void ) : The method "+_nameOfMethod+" is not yet implemented.\n";
        msg+="The methods implemented are : GMRES, BICG, CG, CHOLESKY, LU, BCG, LGMRES, LSQR, CR, CGS and GCR.\n";
        throw CdmathException(msg);
    }

   if (_nameOfPc.compare("ILU")==0) 
		PCSetType(_prec,PCILU);
   else if (_nameOfPc.compare("LU")==0) 
		PCSetType(_prec,PCLU);
   else if (_nameOfPc.compare("ICC")==0) 
		PCSetType(_prec,PCICC);
   else if (_nameOfPc.compare("CHOLESKY")==0) 
		PCSetType(_prec,PCCHOLESKY);
   else if (_nameOfPc.compare("")==0) 
		PCSetType(_prec,PCNONE);
    else
    {
        string msg="Vector LinearSolver::solve( void ) : The preconditioner "+_nameOfPc+" is not yet available.\n";
        msg+="The preconditioners available are : ICC, ILU, CHOLESKY and LU.\n";
        throw CdmathException(msg);
    }
	    
    KSPSetTolerances(_ksp,_tol,_tol,PETSC_DEFAULT,_numberMaxOfIter);
    
    PetscInt its;
    PetscReal rtol,abstol,dtol;
    PetscInt maxits;

    Vec X;
    VecDuplicate(_smb,&X);

    if (isSingular())
    {
        MatNullSpace nullsp;
        MatNullSpaceCreate(PETSC_COMM_WORLD, PETSC_TRUE, 0, PETSC_NULL, &nullsp);
        MatSetNullSpace(_mat, nullsp);
        MatNullSpaceDestroy(&nullsp);
    }

    if(_displayConditionNumber)
        KSPSetComputeEigenvalues(_ksp,PETSC_TRUE);

    KSPSolve(_ksp,_smb,X);

    KSPGetResidualNorm(_ksp,&rtol);
    _residu=(double)rtol;

    KSPGetIterationNumber(_ksp,&its);
    _numberOfIter=(int)its;

    KSPConvergedReason reason;
    KSPGetConvergedReason(_ksp,&reason);

    if (reason>=0 )
          _convergence=true;
	else{
          _convergence=false;
        cout<<"Linear system algorithm did not converge"<<endl;
        cout<<"Final number of iterationx= "<<_numberOfIter<<". Maximum allowed was " << _numberMaxOfIter<<endl;
        cout<<"Final residual "<< _residu<< ". Objective was "<< _tol<<endl;
        string msg="Linear system algorithm did not converge";
        throw CdmathException(msg);
		}
	
	if(_displayConditionNumber)
	    {
		PetscReal sv_max, sv_min;
		KSPComputeExtremeSingularValues(_ksp, &sv_max, &sv_min);
		cout<<" Maximal singular value = " << sv_max <<", Minimal singular value = " << sv_min <<", Condition number = " << sv_max/sv_min <<endl;
		}

    Vector X1=vecToVector(X);

    return (X1);
}

Vec
LinearSolver::vectorToVec(const Vector& myVector) const
{
    int numberOfRows=myVector.getNumberOfRows();
    Vec X;

    VecCreate(PETSC_COMM_WORLD,&X);
    VecSetSizes(X,PETSC_DECIDE,numberOfRows);
    VecSetFromOptions(X);
    for (PetscInt i=0; i<numberOfRows; i++)
    {
        double value = myVector(i);
        VecSetValues(X,1,&i,&value,INSERT_VALUES);
    }

    VecAssemblyBegin(X);
    VecAssemblyEnd(X);

    return (X);
}

Vector
LinearSolver::vecToVector(const Vec& vec) const
{
    PetscInt numberOfRows;

    VecGetSize(vec,&numberOfRows);

    Vector X(numberOfRows);
    double value;

    for (PetscInt i=0; i<numberOfRows; i++)
    {
        VecGetValues(vec,1,&i,&value);
        X(i)=value;
    }

    return (X);
}

//----------------------------------------------------------------------
const LinearSolver&
LinearSolver::operator= ( const LinearSolver& linearSolver )
//----------------------------------------------------------------------
{
    _tol=linearSolver.getTolerance();
    _numberMaxOfIter=linearSolver.getNumberMaxOfIter();
    _nameOfMethod=linearSolver.getNameOfMethod();
    _residu=linearSolver.getResidu();
    _convergence=linearSolver.getStatus();
    _numberOfIter=linearSolver.getNumberOfIter();
    _isSingular=linearSolver.isSingular();
    _secondMember=linearSolver.getSndMember();
    _isSparseMatrix=linearSolver.isSparseMatrix();
    _nameOfPc="";
    setPreconditioner(linearSolver.getNameOfPc());
    _mat=NULL;
    MatDuplicate(linearSolver.getPetscMatrix(),MAT_COPY_VALUES,&_mat);
    _smb=NULL;
    VecDuplicate(linearSolver.getPetscVector(),&_smb);    				;
    _ksp=NULL;
    kspDuplicate(linearSolver.getPetscKsp(),_mat,&_ksp);
    _prec=NULL;
    precDuplicate(linearSolver.getPetscPc(),_ksp,&_prec);
    return (*this);
}
