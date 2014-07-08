# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_medprofile', [dirname(__file__)])
        except ImportError:
            import _medprofile
            return _medprofile
        if fp is not None:
            try:
                _mod = imp.load_module('_medprofile', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _medprofile = swig_import_helper()
    del swig_import_helper
else:
    import _medprofile
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator_medprofile_module(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator_medprofile_module, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator_medprofile_module, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _medprofile.delete_SwigPyIterator_medprofile_module
    __del__ = lambda self : None;
    def value(self): return _medprofile.SwigPyIterator_medprofile_module_value(self)
    def incr(self, n=1): return _medprofile.SwigPyIterator_medprofile_module_incr(self, n)
    def decr(self, n=1): return _medprofile.SwigPyIterator_medprofile_module_decr(self, n)
    def distance(self, *args): return _medprofile.SwigPyIterator_medprofile_module_distance(self, *args)
    def equal(self, *args): return _medprofile.SwigPyIterator_medprofile_module_equal(self, *args)
    def copy(self): return _medprofile.SwigPyIterator_medprofile_module_copy(self)
    def next(self): return _medprofile.SwigPyIterator_medprofile_module_next(self)
    def __next__(self): return _medprofile.SwigPyIterator_medprofile_module___next__(self)
    def previous(self): return _medprofile.SwigPyIterator_medprofile_module_previous(self)
    def advance(self, *args): return _medprofile.SwigPyIterator_medprofile_module_advance(self, *args)
    def __eq__(self, *args): return _medprofile.SwigPyIterator_medprofile_module___eq__(self, *args)
    def __ne__(self, *args): return _medprofile.SwigPyIterator_medprofile_module___ne__(self, *args)
    def __iadd__(self, *args): return _medprofile.SwigPyIterator_medprofile_module___iadd__(self, *args)
    def __isub__(self, *args): return _medprofile.SwigPyIterator_medprofile_module___isub__(self, *args)
    def __add__(self, *args): return _medprofile.SwigPyIterator_medprofile_module___add__(self, *args)
    def __sub__(self, *args): return _medprofile.SwigPyIterator_medprofile_module___sub__(self, *args)
    def __iter__(self): return self
    def __iter__(self): return self
SwigPyIterator_medprofile_module_swigregister = _medprofile.SwigPyIterator_medprofile_module_swigregister
SwigPyIterator_medprofile_module_swigregister(SwigPyIterator_medprofile_module)

ABSOLUTE_H5IPUBLIC_H = _medprofile.ABSOLUTE_H5IPUBLIC_H
ABSOLUTE_H5PUBLIC_H = _medprofile.ABSOLUTE_H5PUBLIC_H
HAVE_CC_C99 = _medprofile.HAVE_CC_C99
HAVE_CUSERID = _medprofile.HAVE_CUSERID
HAVE_DLFCN_H = _medprofile.HAVE_DLFCN_H
HAVE_FTIME = _medprofile.HAVE_FTIME
HAVE_GETEUID = _medprofile.HAVE_GETEUID
HAVE_GETPWUID = _medprofile.HAVE_GETPWUID
HAVE_GETTIMEOFDAY = _medprofile.HAVE_GETTIMEOFDAY
HAVE_H5IPUBLIC_H = _medprofile.HAVE_H5IPUBLIC_H
HAVE_H5PUBLIC_H = _medprofile.HAVE_H5PUBLIC_H
HAVE_INTTYPES_H = _medprofile.HAVE_INTTYPES_H
HAVE_LIBHDF5 = _medprofile.HAVE_LIBHDF5
HAVE_MALLOC_H = _medprofile.HAVE_MALLOC_H
HAVE_MEMORY_H = _medprofile.HAVE_MEMORY_H
HAVE_PWD_H = _medprofile.HAVE_PWD_H
HAVE_PYTHON = _medprofile.HAVE_PYTHON
HAVE_STDBOOL_H = _medprofile.HAVE_STDBOOL_H
HAVE_STDINT_H = _medprofile.HAVE_STDINT_H
HAVE_STDLIB_H = _medprofile.HAVE_STDLIB_H
HAVE_STRINGS_H = _medprofile.HAVE_STRINGS_H
HAVE_STRING_H = _medprofile.HAVE_STRING_H
HAVE_SYS_STAT_H = _medprofile.HAVE_SYS_STAT_H
HAVE_SYS_TIMEB_H = _medprofile.HAVE_SYS_TIMEB_H
HAVE_SYS_TIME_H = _medprofile.HAVE_SYS_TIME_H
HAVE_SYS_TYPES_H = _medprofile.HAVE_SYS_TYPES_H
HAVE_UNISTD_H = _medprofile.HAVE_UNISTD_H
HAVE__BOOL = _medprofile.HAVE__BOOL
LT_OBJDIR = _medprofile.LT_OBJDIR
MED_API_23 = _medprofile.MED_API_23
MED_CHECK_23FORMAT = _medprofile.MED_CHECK_23FORMAT
MED_HAVE_FORTRAN = _medprofile.MED_HAVE_FORTRAN
MED_HAVE_PYTHON = _medprofile.MED_HAVE_PYTHON
MESGERR = _medprofile.MESGERR
PACKAGE = _medprofile.PACKAGE
PACKAGE_BUGREPORT = _medprofile.PACKAGE_BUGREPORT
PACKAGE_NAME = _medprofile.PACKAGE_NAME
PACKAGE_STRING = _medprofile.PACKAGE_STRING
PACKAGE_TARNAME = _medprofile.PACKAGE_TARNAME
PACKAGE_URL = _medprofile.PACKAGE_URL
PACKAGE_VERSION = _medprofile.PACKAGE_VERSION
SIZEOF_FORTRAN_INTEGER = _medprofile.SIZEOF_FORTRAN_INTEGER
SIZEOF_INT = _medprofile.SIZEOF_INT
SIZEOF_LONG = _medprofile.SIZEOF_LONG
STDC_HEADERS = _medprofile.STDC_HEADERS
TIME_WITH_SYS_TIME = _medprofile.TIME_WITH_SYS_TIME
VERSION = _medprofile.VERSION
H5F_LIBVER_18 = _medprofile.H5F_LIBVER_18
MED_MAJOR_NUM = _medprofile.MED_MAJOR_NUM
MED_MINOR_NUM = _medprofile.MED_MINOR_NUM
MED_RELEASE_NUM = _medprofile.MED_RELEASE_NUM
MED_NUM_MAJEUR = _medprofile.MED_NUM_MAJEUR
MED_NUM_MINEUR = _medprofile.MED_NUM_MINEUR
MED_NUM_RELEASE = _medprofile.MED_NUM_RELEASE
MED_VERSION_STR = _medprofile.MED_VERSION_STR
MED_MAX_PARA = _medprofile.MED_MAX_PARA
MED_COMMENT_SIZE = _medprofile.MED_COMMENT_SIZE
MED_IDENT_SIZE = _medprofile.MED_IDENT_SIZE
MED_NAME_SIZE = _medprofile.MED_NAME_SIZE
MED_SNAME_SIZE = _medprofile.MED_SNAME_SIZE
MED_LNAME_SIZE = _medprofile.MED_LNAME_SIZE
MED_SNAME_BLANK = _medprofile.MED_SNAME_BLANK
MED_NAME_BLANK = _medprofile.MED_NAME_BLANK
MED_PATHNAME_SIZE = _medprofile.MED_PATHNAME_SIZE
MED_MAX_CHFID_PATH = _medprofile.MED_MAX_CHFID_PATH
MED_FULL_INTERLACE = _medprofile.MED_FULL_INTERLACE
MED_NO_INTERLACE = _medprofile.MED_NO_INTERLACE
MED_UNDEF_INTERLACE = _medprofile.MED_UNDEF_INTERLACE
MED_UNDEF_STMODE = _medprofile.MED_UNDEF_STMODE
MED_GLOBAL_STMODE = _medprofile.MED_GLOBAL_STMODE
MED_COMPACT_STMODE = _medprofile.MED_COMPACT_STMODE
MED_GLOBAL_PFLMODE = _medprofile.MED_GLOBAL_PFLMODE
MED_COMPACT_PFLMODE = _medprofile.MED_COMPACT_PFLMODE
MED_UNDEF_PFLMODE = _medprofile.MED_UNDEF_PFLMODE
MED_ACC_RDONLY = _medprofile.MED_ACC_RDONLY
MED_ACC_RDWR = _medprofile.MED_ACC_RDWR
MED_ACC_RDEXT = _medprofile.MED_ACC_RDEXT
MED_ACC_CREAT = _medprofile.MED_ACC_CREAT
MED_ACC_UNDEF = _medprofile.MED_ACC_UNDEF
MED_UNSTRUCTURED_MESH = _medprofile.MED_UNSTRUCTURED_MESH
MED_STRUCTURED_MESH = _medprofile.MED_STRUCTURED_MESH
MED_UNDEF_MESH_TYPE = _medprofile.MED_UNDEF_MESH_TYPE
MED_CARTESIAN_GRID = _medprofile.MED_CARTESIAN_GRID
MED_POLAR_GRID = _medprofile.MED_POLAR_GRID
MED_CURVILINEAR_GRID = _medprofile.MED_CURVILINEAR_GRID
MED_UNDEF_GRID_TYPE = _medprofile.MED_UNDEF_GRID_TYPE
MED_CELL = _medprofile.MED_CELL
MED_DESCENDING_FACE = _medprofile.MED_DESCENDING_FACE
MED_DESCENDING_EDGE = _medprofile.MED_DESCENDING_EDGE
MED_NODE = _medprofile.MED_NODE
MED_NODE_ELEMENT = _medprofile.MED_NODE_ELEMENT
MED_STRUCT_ELEMENT = _medprofile.MED_STRUCT_ELEMENT
MED_ALL_ENTITY_TYPE = _medprofile.MED_ALL_ENTITY_TYPE
MED_UNDEF_ENTITY_TYPE = _medprofile.MED_UNDEF_ENTITY_TYPE
MED_N_ENTITY_TYPES = _medprofile.MED_N_ENTITY_TYPES
MED_COORDINATE = _medprofile.MED_COORDINATE
MED_CONNECTIVITY = _medprofile.MED_CONNECTIVITY
MED_NAME = _medprofile.MED_NAME
MED_NUMBER = _medprofile.MED_NUMBER
MED_FAMILY_NUMBER = _medprofile.MED_FAMILY_NUMBER
MED_COORDINATE_AXIS1 = _medprofile.MED_COORDINATE_AXIS1
MED_COORDINATE_AXIS2 = _medprofile.MED_COORDINATE_AXIS2
MED_COORDINATE_AXIS3 = _medprofile.MED_COORDINATE_AXIS3
MED_INDEX_FACE = _medprofile.MED_INDEX_FACE
MED_INDEX_NODE = _medprofile.MED_INDEX_NODE
MED_GLOBAL_NUMBER = _medprofile.MED_GLOBAL_NUMBER
MED_VARIABLE_ATTRIBUTE = _medprofile.MED_VARIABLE_ATTRIBUTE
MED_COORDINATE_TRSF = _medprofile.MED_COORDINATE_TRSF
MED_UNDEF_DATATYPE = _medprofile.MED_UNDEF_DATATYPE
MED_INTERNAL_FLOAT64 = _medprofile.MED_INTERNAL_FLOAT64
MED_INTERNAL_INT32 = _medprofile.MED_INTERNAL_INT32
MED_INTERNAL_INT64 = _medprofile.MED_INTERNAL_INT64
MED_INTERNAL_INT = _medprofile.MED_INTERNAL_INT
MED_INTERNAL_NAME = _medprofile.MED_INTERNAL_NAME
MED_INTERNAL_SNAME = _medprofile.MED_INTERNAL_SNAME
MED_INTERNAL_LNAME = _medprofile.MED_INTERNAL_LNAME
MED_INTERNAL_IDENT = _medprofile.MED_INTERNAL_IDENT
MED_INTERNAL_CHAR = _medprofile.MED_INTERNAL_CHAR
MED_INTERNAL_UNDEF = _medprofile.MED_INTERNAL_UNDEF
MED_FLOAT64 = _medprofile.MED_FLOAT64
MED_INT32 = _medprofile.MED_INT32
MED_INT64 = _medprofile.MED_INT64
MED_INT = _medprofile.MED_INT
MED_ATT_FLOAT64 = _medprofile.MED_ATT_FLOAT64
MED_ATT_INT = _medprofile.MED_ATT_INT
MED_ATT_NAME = _medprofile.MED_ATT_NAME
MED_ATT_UNDEF = _medprofile.MED_ATT_UNDEF
MED_MESH = _medprofile.MED_MESH
MED_FIELD = _medprofile.MED_FIELD
MED_LIBRARY = _medprofile.MED_LIBRARY
MED_FILE = _medprofile.MED_FILE
MED_MESH_SUPPORT = _medprofile.MED_MESH_SUPPORT
MED_ELSTRUCT = _medprofile.MED_ELSTRUCT
MED_FAMILY = _medprofile.MED_FAMILY
MED_EQUIVALENCE = _medprofile.MED_EQUIVALENCE
MED_GROUP = _medprofile.MED_GROUP
MED_JOINT = _medprofile.MED_JOINT
MED_LOCALIZATION = _medprofile.MED_LOCALIZATION
MED_PROFILE = _medprofile.MED_PROFILE
MED_FILTER = _medprofile.MED_FILTER
MED_INTERPOLATION = _medprofile.MED_INTERPOLATION
MED_NUMERICAL_DATA = _medprofile.MED_NUMERICAL_DATA
MED_LINK = _medprofile.MED_LINK
MED_CLASS_UNDEF = _medprofile.MED_CLASS_UNDEF
MED_CLASS_ALL = _medprofile.MED_CLASS_ALL
MED_POINT1 = _medprofile.MED_POINT1
MED_SEG2 = _medprofile.MED_SEG2
MED_SEG3 = _medprofile.MED_SEG3
MED_SEG4 = _medprofile.MED_SEG4
MED_TRIA3 = _medprofile.MED_TRIA3
MED_QUAD4 = _medprofile.MED_QUAD4
MED_TRIA6 = _medprofile.MED_TRIA6
MED_TRIA7 = _medprofile.MED_TRIA7
MED_QUAD8 = _medprofile.MED_QUAD8
MED_QUAD9 = _medprofile.MED_QUAD9
MED_TETRA4 = _medprofile.MED_TETRA4
MED_PYRA5 = _medprofile.MED_PYRA5
MED_PENTA6 = _medprofile.MED_PENTA6
MED_HEXA8 = _medprofile.MED_HEXA8
MED_TETRA10 = _medprofile.MED_TETRA10
MED_OCTA12 = _medprofile.MED_OCTA12
MED_PYRA13 = _medprofile.MED_PYRA13
MED_PENTA15 = _medprofile.MED_PENTA15
MED_HEXA20 = _medprofile.MED_HEXA20
MED_HEXA27 = _medprofile.MED_HEXA27
MED_POLYGON = _medprofile.MED_POLYGON
MED_POLYGON2 = _medprofile.MED_POLYGON2
MED_POLYHEDRON = _medprofile.MED_POLYHEDRON
MED_STRUCT_GEO_INTERNAL = _medprofile.MED_STRUCT_GEO_INTERNAL
MED_STRUCT_GEO_SUP_INTERNAL = _medprofile.MED_STRUCT_GEO_SUP_INTERNAL
MED_NONE = _medprofile.MED_NONE
MED_NO_GEOTYPE = _medprofile.MED_NO_GEOTYPE
MED_UNDEF_GEOTYPE = _medprofile.MED_UNDEF_GEOTYPE
MED_UNDEF_GEOMETRY_TYPE = _medprofile.MED_UNDEF_GEOMETRY_TYPE
MED_ALL_GEOTYPE = _medprofile.MED_ALL_GEOTYPE
MED_GEO_ALL = _medprofile.MED_GEO_ALL
MED_N_CELL_GEO = _medprofile.MED_N_CELL_GEO
MED_N_CELL_FIXED_GEO = _medprofile.MED_N_CELL_FIXED_GEO
MED_N_CELL_GEO_FIXED_CON = _medprofile.MED_N_CELL_GEO_FIXED_CON
MED_N_FACE_GEO = _medprofile.MED_N_FACE_GEO
MED_N_FACE_FIXED_GEO = _medprofile.MED_N_FACE_FIXED_GEO
MED_N_FACE_GEO_FIXED_CON = _medprofile.MED_N_FACE_GEO_FIXED_CON
MED_N_EDGE_TYPES = _medprofile.MED_N_EDGE_TYPES
MED_N_EDGE_FIXED_GEO = _medprofile.MED_N_EDGE_FIXED_GEO
MED_N_EDGE_GEO_FIXED_CON = _medprofile.MED_N_EDGE_GEO_FIXED_CON
MED_N_NODE_GEO = _medprofile.MED_N_NODE_GEO
MED_N_NODE_FIXED_GEO = _medprofile.MED_N_NODE_FIXED_GEO
MED_N_NODE_GEO_FIXED_CON = _medprofile.MED_N_NODE_GEO_FIXED_CON
MED_NODAL = _medprofile.MED_NODAL
MED_DESCENDING = _medprofile.MED_DESCENDING
MED_UNDEF_CONNECTIVITY_MODE = _medprofile.MED_UNDEF_CONNECTIVITY_MODE
MED_NO_CMODE = _medprofile.MED_NO_CMODE
MED_CARTESIAN = _medprofile.MED_CARTESIAN
MED_CYLINDRICAL = _medprofile.MED_CYLINDRICAL
MED_SPHERICAL = _medprofile.MED_SPHERICAL
MED_UNDEF_AXIS_TYPE = _medprofile.MED_UNDEF_AXIS_TYPE
MED_FALSE = _medprofile.MED_FALSE
MED_TRUE = _medprofile.MED_TRUE
MED_GAUSS_ELNO = _medprofile.MED_GAUSS_ELNO
MED_IPOINT_ELNO = _medprofile.MED_IPOINT_ELNO
MED_NO_NAME = _medprofile.MED_NO_NAME
MED_NO_MESHNAME = _medprofile.MED_NO_MESHNAME
MED_NO_MESH = _medprofile.MED_NO_MESH
MED_NO_MESH_SUPPORT = _medprofile.MED_NO_MESH_SUPPORT
MED_NO_LOCALIZATION = _medprofile.MED_NO_LOCALIZATION
MED_NO_INTERPOLATION = _medprofile.MED_NO_INTERPOLATION
MED_NO_IPOINT_INTERNAL = _medprofile.MED_NO_IPOINT_INTERNAL
MED_NO_PROFILE = _medprofile.MED_NO_PROFILE
MED_NO_GROUP = _medprofile.MED_NO_GROUP
MED_ALLENTITIES_PROFILE = _medprofile.MED_ALLENTITIES_PROFILE
MED_NO_PROFILE_INTERNAL = _medprofile.MED_NO_PROFILE_INTERNAL
MED_SAME_PROFILE_INTERNAL = _medprofile.MED_SAME_PROFILE_INTERNAL
MED_ALL_CONSTITUENT = _medprofile.MED_ALL_CONSTITUENT
MED_UNDEF_SIZE = _medprofile.MED_UNDEF_SIZE
MED_NO_PROFILE_SIZE = _medprofile.MED_NO_PROFILE_SIZE
MED_SORT_DTIT = _medprofile.MED_SORT_DTIT
MED_SORT_ITDT = _medprofile.MED_SORT_ITDT
MED_SORT_UNDEF = _medprofile.MED_SORT_UNDEF
MED_NO_DT = _medprofile.MED_NO_DT
MED_NO_IT = _medprofile.MED_NO_IT
MED_UNDEF_DT = _medprofile.MED_UNDEF_DT
MED_ATT_NOT_FILLED = _medprofile.MED_ATT_NOT_FILLED
MED_MAX_FILTER_SPACES = _medprofile.MED_MAX_FILTER_SPACES
class med_filter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, med_filter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, med_filter, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nspaces"] = _medprofile.med_filter_nspaces_set
    __swig_getmethods__["nspaces"] = _medprofile.med_filter_nspaces_get
    if _newclass:nspaces = _swig_property(_medprofile.med_filter_nspaces_get, _medprofile.med_filter_nspaces_set)
    __swig_setmethods__["memspace"] = _medprofile.med_filter_memspace_set
    __swig_getmethods__["memspace"] = _medprofile.med_filter_memspace_get
    if _newclass:memspace = _swig_property(_medprofile.med_filter_memspace_get, _medprofile.med_filter_memspace_set)
    __swig_setmethods__["diskspace"] = _medprofile.med_filter_diskspace_set
    __swig_getmethods__["diskspace"] = _medprofile.med_filter_diskspace_get
    if _newclass:diskspace = _swig_property(_medprofile.med_filter_diskspace_get, _medprofile.med_filter_diskspace_set)
    __swig_setmethods__["nentity"] = _medprofile.med_filter_nentity_set
    __swig_getmethods__["nentity"] = _medprofile.med_filter_nentity_get
    if _newclass:nentity = _swig_property(_medprofile.med_filter_nentity_get, _medprofile.med_filter_nentity_set)
    __swig_setmethods__["nvaluesperentity"] = _medprofile.med_filter_nvaluesperentity_set
    __swig_getmethods__["nvaluesperentity"] = _medprofile.med_filter_nvaluesperentity_get
    if _newclass:nvaluesperentity = _swig_property(_medprofile.med_filter_nvaluesperentity_get, _medprofile.med_filter_nvaluesperentity_set)
    __swig_setmethods__["nconstituentpervalue"] = _medprofile.med_filter_nconstituentpervalue_set
    __swig_getmethods__["nconstituentpervalue"] = _medprofile.med_filter_nconstituentpervalue_get
    if _newclass:nconstituentpervalue = _swig_property(_medprofile.med_filter_nconstituentpervalue_get, _medprofile.med_filter_nconstituentpervalue_set)
    __swig_setmethods__["constituentselect"] = _medprofile.med_filter_constituentselect_set
    __swig_getmethods__["constituentselect"] = _medprofile.med_filter_constituentselect_get
    if _newclass:constituentselect = _swig_property(_medprofile.med_filter_constituentselect_get, _medprofile.med_filter_constituentselect_set)
    __swig_setmethods__["switchmode"] = _medprofile.med_filter_switchmode_set
    __swig_getmethods__["switchmode"] = _medprofile.med_filter_switchmode_get
    if _newclass:switchmode = _swig_property(_medprofile.med_filter_switchmode_get, _medprofile.med_filter_switchmode_set)
    __swig_setmethods__["filterarraysize"] = _medprofile.med_filter_filterarraysize_set
    __swig_getmethods__["filterarraysize"] = _medprofile.med_filter_filterarraysize_get
    if _newclass:filterarraysize = _swig_property(_medprofile.med_filter_filterarraysize_get, _medprofile.med_filter_filterarraysize_set)
    __swig_setmethods__["filterarray23v30"] = _medprofile.med_filter_filterarray23v30_set
    __swig_getmethods__["filterarray23v30"] = _medprofile.med_filter_filterarray23v30_get
    if _newclass:filterarray23v30 = _swig_property(_medprofile.med_filter_filterarray23v30_get, _medprofile.med_filter_filterarray23v30_set)
    __swig_setmethods__["profilearraysize"] = _medprofile.med_filter_profilearraysize_set
    __swig_getmethods__["profilearraysize"] = _medprofile.med_filter_profilearraysize_get
    if _newclass:profilearraysize = _swig_property(_medprofile.med_filter_profilearraysize_get, _medprofile.med_filter_profilearraysize_set)
    __swig_setmethods__["storagemode"] = _medprofile.med_filter_storagemode_set
    __swig_getmethods__["storagemode"] = _medprofile.med_filter_storagemode_get
    if _newclass:storagemode = _swig_property(_medprofile.med_filter_storagemode_get, _medprofile.med_filter_storagemode_set)
    __swig_setmethods__["profilename"] = _medprofile.med_filter_profilename_set
    __swig_getmethods__["profilename"] = _medprofile.med_filter_profilename_get
    if _newclass:profilename = _swig_property(_medprofile.med_filter_profilename_get, _medprofile.med_filter_profilename_set)
    def __init__(self): 
        """__init__(self) -> med_filter"""
        this = _medprofile.new_med_filter()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _medprofile.delete_med_filter
    __del__ = lambda self : None;
med_filter_swigregister = _medprofile.med_filter_swigregister
med_filter_swigregister(med_filter)

MED_NO_FILTER_SIZE = _medprofile.MED_NO_FILTER_SIZE
MED_NO_PROFILE_F = _medprofile.MED_NO_PROFILE_F
class med_file_version(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, med_file_version, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, med_file_version, name)
    __repr__ = _swig_repr
    __swig_setmethods__["majeur"] = _medprofile.med_file_version_majeur_set
    __swig_getmethods__["majeur"] = _medprofile.med_file_version_majeur_get
    if _newclass:majeur = _swig_property(_medprofile.med_file_version_majeur_get, _medprofile.med_file_version_majeur_set)
    __swig_setmethods__["mineur"] = _medprofile.med_file_version_mineur_set
    __swig_getmethods__["mineur"] = _medprofile.med_file_version_mineur_get
    if _newclass:mineur = _swig_property(_medprofile.med_file_version_mineur_get, _medprofile.med_file_version_mineur_set)
    __swig_setmethods__["release"] = _medprofile.med_file_version_release_set
    __swig_getmethods__["release"] = _medprofile.med_file_version_release_get
    if _newclass:release = _swig_property(_medprofile.med_file_version_release_get, _medprofile.med_file_version_release_set)
    def __init__(self): 
        """__init__(self) -> med_file_version"""
        this = _medprofile.new_med_file_version()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _medprofile.delete_med_file_version
    __del__ = lambda self : None;
med_file_version_swigregister = _medprofile.med_file_version_swigregister
med_file_version_swigregister(med_file_version)

MED_PARTICLE_NAME = _medprofile.MED_PARTICLE_NAME
MED_BALL_NAME = _medprofile.MED_BALL_NAME
MED_BEAM_NAME = _medprofile.MED_BEAM_NAME
MED_PARTICLE_LABEL = _medprofile.MED_PARTICLE_LABEL
MED_BALL_DIAMETER = _medprofile.MED_BALL_DIAMETER
MED_BEAM_THICKNESS = _medprofile.MED_BEAM_THICKNESS
import medenum
class MEDBOOL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MEDBOOL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MEDBOOL, name)
    __repr__ = _swig_repr
    def iterator(self): return _medprofile.MEDBOOL_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _medprofile.MEDBOOL___nonzero__(self)
    def __bool__(self): return _medprofile.MEDBOOL___bool__(self)
    def __len__(self): return _medprofile.MEDBOOL___len__(self)
    def pop(self): return _medprofile.MEDBOOL_pop(self)
    def __getslice__(self, *args): return _medprofile.MEDBOOL___getslice__(self, *args)
    def __setslice__(self, *args): return _medprofile.MEDBOOL___setslice__(self, *args)
    def __delslice__(self, *args): return _medprofile.MEDBOOL___delslice__(self, *args)
    def __delitem__(self, *args): return _medprofile.MEDBOOL___delitem__(self, *args)
    def __getitem__(self, *args): return _medprofile.MEDBOOL___getitem__(self, *args)
    def __setitem__(self, *args): return _medprofile.MEDBOOL___setitem__(self, *args)
    def append(self, *args): return _medprofile.MEDBOOL_append(self, *args)
    def empty(self): return _medprofile.MEDBOOL_empty(self)
    def size(self): return _medprofile.MEDBOOL_size(self)
    def clear(self): return _medprofile.MEDBOOL_clear(self)
    def swap(self, *args): return _medprofile.MEDBOOL_swap(self, *args)
    def get_allocator(self): return _medprofile.MEDBOOL_get_allocator(self)
    def begin(self): return _medprofile.MEDBOOL_begin(self)
    def end(self): return _medprofile.MEDBOOL_end(self)
    def rbegin(self): return _medprofile.MEDBOOL_rbegin(self)
    def rend(self): return _medprofile.MEDBOOL_rend(self)
    def pop_back(self): return _medprofile.MEDBOOL_pop_back(self)
    def erase(self, *args): return _medprofile.MEDBOOL_erase(self, *args)
    def __init__(self, *args): 
        this = _medprofile.new_MEDBOOL(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _medprofile.MEDBOOL_push_back(self, *args)
    def front(self): return _medprofile.MEDBOOL_front(self)
    def back(self): return _medprofile.MEDBOOL_back(self)
    def assign(self, *args): return _medprofile.MEDBOOL_assign(self, *args)
    def resize(self, *args): return _medprofile.MEDBOOL_resize(self, *args)
    def insert(self, *args): return _medprofile.MEDBOOL_insert(self, *args)
    def reserve(self, *args): return _medprofile.MEDBOOL_reserve(self, *args)
    def capacity(self): return _medprofile.MEDBOOL_capacity(self)
    __swig_destroy__ = _medprofile.delete_MEDBOOL
    __del__ = lambda self : None;
MEDBOOL_swigregister = _medprofile.MEDBOOL_swigregister
MEDBOOL_swigregister(MEDBOOL)
cvar = _medprofile.cvar
MED_GET_ENTITY_TYPENAME = cvar.MED_GET_ENTITY_TYPENAME
MED_GET_CELL_GEOMETRY_TYPENAME = cvar.MED_GET_CELL_GEOMETRY_TYPENAME
MED_GET_FACE_GEOMETRY_TYPENAME = cvar.MED_GET_FACE_GEOMETRY_TYPENAME

MEDBOOL.__str__= lambda self: str([x for x in self])
MEDBOOL.__repr__= lambda self: "MEDBOOL("+str([x for x in self])+")"

class MEDFLOAT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MEDFLOAT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MEDFLOAT, name)
    __repr__ = _swig_repr
    def iterator(self): return _medprofile.MEDFLOAT_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _medprofile.MEDFLOAT___nonzero__(self)
    def __bool__(self): return _medprofile.MEDFLOAT___bool__(self)
    def __len__(self): return _medprofile.MEDFLOAT___len__(self)
    def pop(self): return _medprofile.MEDFLOAT_pop(self)
    def __getslice__(self, *args): return _medprofile.MEDFLOAT___getslice__(self, *args)
    def __setslice__(self, *args): return _medprofile.MEDFLOAT___setslice__(self, *args)
    def __delslice__(self, *args): return _medprofile.MEDFLOAT___delslice__(self, *args)
    def __delitem__(self, *args): return _medprofile.MEDFLOAT___delitem__(self, *args)
    def __getitem__(self, *args): return _medprofile.MEDFLOAT___getitem__(self, *args)
    def __setitem__(self, *args): return _medprofile.MEDFLOAT___setitem__(self, *args)
    def append(self, *args): return _medprofile.MEDFLOAT_append(self, *args)
    def empty(self): return _medprofile.MEDFLOAT_empty(self)
    def size(self): return _medprofile.MEDFLOAT_size(self)
    def clear(self): return _medprofile.MEDFLOAT_clear(self)
    def swap(self, *args): return _medprofile.MEDFLOAT_swap(self, *args)
    def get_allocator(self): return _medprofile.MEDFLOAT_get_allocator(self)
    def begin(self): return _medprofile.MEDFLOAT_begin(self)
    def end(self): return _medprofile.MEDFLOAT_end(self)
    def rbegin(self): return _medprofile.MEDFLOAT_rbegin(self)
    def rend(self): return _medprofile.MEDFLOAT_rend(self)
    def pop_back(self): return _medprofile.MEDFLOAT_pop_back(self)
    def erase(self, *args): return _medprofile.MEDFLOAT_erase(self, *args)
    def __init__(self, *args): 
        this = _medprofile.new_MEDFLOAT(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _medprofile.MEDFLOAT_push_back(self, *args)
    def front(self): return _medprofile.MEDFLOAT_front(self)
    def back(self): return _medprofile.MEDFLOAT_back(self)
    def assign(self, *args): return _medprofile.MEDFLOAT_assign(self, *args)
    def resize(self, *args): return _medprofile.MEDFLOAT_resize(self, *args)
    def insert(self, *args): return _medprofile.MEDFLOAT_insert(self, *args)
    def reserve(self, *args): return _medprofile.MEDFLOAT_reserve(self, *args)
    def capacity(self): return _medprofile.MEDFLOAT_capacity(self)
    def __iadd__(self, *args): return _medprofile.MEDFLOAT___iadd__(self, *args)
    def __add__(self, *args): return _medprofile.MEDFLOAT___add__(self, *args)
    def __isub__(self, *args): return _medprofile.MEDFLOAT___isub__(self, *args)
    def __sub__(self, *args): return _medprofile.MEDFLOAT___sub__(self, *args)
    def __imul__(self, *args): return _medprofile.MEDFLOAT___imul__(self, *args)
    def __mul__(self, *args): return _medprofile.MEDFLOAT___mul__(self, *args)
    def __idiv__(self, *args): return _medprofile.MEDFLOAT___idiv__(self, *args)
    def __div__(self, *args): return _medprofile.MEDFLOAT___div__(self, *args)
    def __le__(self, *args): return _medprofile.MEDFLOAT___le__(self, *args)
    def __lt__(self, *args): return _medprofile.MEDFLOAT___lt__(self, *args)
    def __gt__(self, *args): return _medprofile.MEDFLOAT___gt__(self, *args)
    def __ge__(self, *args): return _medprofile.MEDFLOAT___ge__(self, *args)
    def __eq__(self, *args): return _medprofile.MEDFLOAT___eq__(self, *args)
    def __ne__(self, *args): return _medprofile.MEDFLOAT___ne__(self, *args)
    __swig_destroy__ = _medprofile.delete_MEDFLOAT
    __del__ = lambda self : None;
MEDFLOAT_swigregister = _medprofile.MEDFLOAT_swigregister
MEDFLOAT_swigregister(MEDFLOAT)

MEDFLOAT.__str__= lambda self: str([x for x in self])
MEDFLOAT.__repr__= lambda self:"MEDFLOAT" +"("+str([x for x in self])+")"

class MEDINT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MEDINT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MEDINT, name)
    __repr__ = _swig_repr
    def iterator(self): return _medprofile.MEDINT_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _medprofile.MEDINT___nonzero__(self)
    def __bool__(self): return _medprofile.MEDINT___bool__(self)
    def __len__(self): return _medprofile.MEDINT___len__(self)
    def pop(self): return _medprofile.MEDINT_pop(self)
    def __getslice__(self, *args): return _medprofile.MEDINT___getslice__(self, *args)
    def __setslice__(self, *args): return _medprofile.MEDINT___setslice__(self, *args)
    def __delslice__(self, *args): return _medprofile.MEDINT___delslice__(self, *args)
    def __delitem__(self, *args): return _medprofile.MEDINT___delitem__(self, *args)
    def __getitem__(self, *args): return _medprofile.MEDINT___getitem__(self, *args)
    def __setitem__(self, *args): return _medprofile.MEDINT___setitem__(self, *args)
    def append(self, *args): return _medprofile.MEDINT_append(self, *args)
    def empty(self): return _medprofile.MEDINT_empty(self)
    def size(self): return _medprofile.MEDINT_size(self)
    def clear(self): return _medprofile.MEDINT_clear(self)
    def swap(self, *args): return _medprofile.MEDINT_swap(self, *args)
    def get_allocator(self): return _medprofile.MEDINT_get_allocator(self)
    def begin(self): return _medprofile.MEDINT_begin(self)
    def end(self): return _medprofile.MEDINT_end(self)
    def rbegin(self): return _medprofile.MEDINT_rbegin(self)
    def rend(self): return _medprofile.MEDINT_rend(self)
    def pop_back(self): return _medprofile.MEDINT_pop_back(self)
    def erase(self, *args): return _medprofile.MEDINT_erase(self, *args)
    def __init__(self, *args): 
        this = _medprofile.new_MEDINT(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _medprofile.MEDINT_push_back(self, *args)
    def front(self): return _medprofile.MEDINT_front(self)
    def back(self): return _medprofile.MEDINT_back(self)
    def assign(self, *args): return _medprofile.MEDINT_assign(self, *args)
    def resize(self, *args): return _medprofile.MEDINT_resize(self, *args)
    def insert(self, *args): return _medprofile.MEDINT_insert(self, *args)
    def reserve(self, *args): return _medprofile.MEDINT_reserve(self, *args)
    def capacity(self): return _medprofile.MEDINT_capacity(self)
    def __iadd__(self, *args): return _medprofile.MEDINT___iadd__(self, *args)
    def __add__(self, *args): return _medprofile.MEDINT___add__(self, *args)
    def __isub__(self, *args): return _medprofile.MEDINT___isub__(self, *args)
    def __sub__(self, *args): return _medprofile.MEDINT___sub__(self, *args)
    def __imul__(self, *args): return _medprofile.MEDINT___imul__(self, *args)
    def __mul__(self, *args): return _medprofile.MEDINT___mul__(self, *args)
    def __idiv__(self, *args): return _medprofile.MEDINT___idiv__(self, *args)
    def __div__(self, *args): return _medprofile.MEDINT___div__(self, *args)
    def __le__(self, *args): return _medprofile.MEDINT___le__(self, *args)
    def __lt__(self, *args): return _medprofile.MEDINT___lt__(self, *args)
    def __gt__(self, *args): return _medprofile.MEDINT___gt__(self, *args)
    def __ge__(self, *args): return _medprofile.MEDINT___ge__(self, *args)
    def __eq__(self, *args): return _medprofile.MEDINT___eq__(self, *args)
    def __ne__(self, *args): return _medprofile.MEDINT___ne__(self, *args)
    __swig_destroy__ = _medprofile.delete_MEDINT
    __del__ = lambda self : None;
MEDINT_swigregister = _medprofile.MEDINT_swigregister
MEDINT_swigregister(MEDINT)

MEDINT.__str__= lambda self: str([x for x in self])
MEDINT.__repr__= lambda self:"MEDINT" +"("+str([x for x in self])+")"

class MEDCHAR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MEDCHAR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MEDCHAR, name)
    __repr__ = _swig_repr
    def iterator(self): return _medprofile.MEDCHAR_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _medprofile.MEDCHAR___nonzero__(self)
    def __bool__(self): return _medprofile.MEDCHAR___bool__(self)
    def __len__(self): return _medprofile.MEDCHAR___len__(self)
    def pop(self): return _medprofile.MEDCHAR_pop(self)
    def __getslice__(self, *args): return _medprofile.MEDCHAR___getslice__(self, *args)
    def __setslice__(self, *args): return _medprofile.MEDCHAR___setslice__(self, *args)
    def __delslice__(self, *args): return _medprofile.MEDCHAR___delslice__(self, *args)
    def __delitem__(self, *args): return _medprofile.MEDCHAR___delitem__(self, *args)
    def __getitem__(self, *args): return _medprofile.MEDCHAR___getitem__(self, *args)
    def __setitem__(self, *args): return _medprofile.MEDCHAR___setitem__(self, *args)
    def append(self, *args): return _medprofile.MEDCHAR_append(self, *args)
    def empty(self): return _medprofile.MEDCHAR_empty(self)
    def size(self): return _medprofile.MEDCHAR_size(self)
    def clear(self): return _medprofile.MEDCHAR_clear(self)
    def swap(self, *args): return _medprofile.MEDCHAR_swap(self, *args)
    def get_allocator(self): return _medprofile.MEDCHAR_get_allocator(self)
    def begin(self): return _medprofile.MEDCHAR_begin(self)
    def end(self): return _medprofile.MEDCHAR_end(self)
    def rbegin(self): return _medprofile.MEDCHAR_rbegin(self)
    def rend(self): return _medprofile.MEDCHAR_rend(self)
    def pop_back(self): return _medprofile.MEDCHAR_pop_back(self)
    def erase(self, *args): return _medprofile.MEDCHAR_erase(self, *args)
    def __init__(self, *args): 
        this = _medprofile.new_MEDCHAR(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _medprofile.MEDCHAR_push_back(self, *args)
    def front(self): return _medprofile.MEDCHAR_front(self)
    def back(self): return _medprofile.MEDCHAR_back(self)
    def assign(self, *args): return _medprofile.MEDCHAR_assign(self, *args)
    def resize(self, *args): return _medprofile.MEDCHAR_resize(self, *args)
    def insert(self, *args): return _medprofile.MEDCHAR_insert(self, *args)
    def reserve(self, *args): return _medprofile.MEDCHAR_reserve(self, *args)
    def capacity(self): return _medprofile.MEDCHAR_capacity(self)
    def __iadd__(self, *args): return _medprofile.MEDCHAR___iadd__(self, *args)
    def __add__(self, *args): return _medprofile.MEDCHAR___add__(self, *args)
    def __isub__(self, *args): return _medprofile.MEDCHAR___isub__(self, *args)
    def __sub__(self, *args): return _medprofile.MEDCHAR___sub__(self, *args)
    def __imul__(self, *args): return _medprofile.MEDCHAR___imul__(self, *args)
    def __mul__(self, *args): return _medprofile.MEDCHAR___mul__(self, *args)
    def __idiv__(self, *args): return _medprofile.MEDCHAR___idiv__(self, *args)
    def __div__(self, *args): return _medprofile.MEDCHAR___div__(self, *args)
    def __le__(self, *args): return _medprofile.MEDCHAR___le__(self, *args)
    def __lt__(self, *args): return _medprofile.MEDCHAR___lt__(self, *args)
    def __gt__(self, *args): return _medprofile.MEDCHAR___gt__(self, *args)
    def __ge__(self, *args): return _medprofile.MEDCHAR___ge__(self, *args)
    def __eq__(self, *args): return _medprofile.MEDCHAR___eq__(self, *args)
    def __ne__(self, *args): return _medprofile.MEDCHAR___ne__(self, *args)
    __swig_destroy__ = _medprofile.delete_MEDCHAR
    __del__ = lambda self : None;
MEDCHAR_swigregister = _medprofile.MEDCHAR_swigregister
MEDCHAR_swigregister(MEDCHAR)

MEDCHAR.__str__= lambda self: str([x for x in self])
MEDCHAR.__repr__= lambda self:"MEDCHAR" +"("+str([x for x in self])+")"

MEDCHAR.__str__= lambda self: str([x for x in self])
MEDCHAR.__repr__= lambda self:"MEDCHAR" +"("+str([x for x in self])+")"

MEDCHAR.__str__= lambda self: str([x for x in self])
MEDCHAR.__repr__= lambda self:"MEDCHAR" +"("+str([x for x in self])+")"


def MEDnProfile(*args, **kwargs):
  """
    MEDnProfile(fid) -> med_int

    Parameters:
        fid: med_idt const

    """
  return _medprofile.MEDnProfile(*args, **kwargs)

def MEDprofileInfo(*args, **kwargs):
  """
    MEDprofileInfo(fid, profileit) -> med_err

    Parameters:
        fid: med_idt const
        profileit: int const

    """
  return _medprofile.MEDprofileInfo(*args, **kwargs)

def MEDprofileWr(*args, **kwargs):
  """
    MEDprofileWr(fid, profilename, profilesize, profilearray) -> med_err

    Parameters:
        fid: med_idt const
        profilename: char const *const
        profilesize: med_int const
        profilearray: med_int const *const

    """
  return _medprofile.MEDprofileWr(*args, **kwargs)

def MEDprofileSizeByName(*args, **kwargs):
  """
    MEDprofileSizeByName(fid, profilename) -> med_int

    Parameters:
        fid: med_idt const
        profilename: char const *const

    """
  return _medprofile.MEDprofileSizeByName(*args, **kwargs)

def MEDprofileRd(*args, **kwargs):
  """
    MEDprofileRd(fid, profilename, profilearray) -> med_err

    Parameters:
        fid: med_idt const
        profilename: char const *const
        profilearray: med_int *const

    """
  return _medprofile.MEDprofileRd(*args, **kwargs)
# This file is compatible with both classic and new-style classes.


