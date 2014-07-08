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
            fp, pathname, description = imp.find_module('_medfamily', [dirname(__file__)])
        except ImportError:
            import _medfamily
            return _medfamily
        if fp is not None:
            try:
                _mod = imp.load_module('_medfamily', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _medfamily = swig_import_helper()
    del swig_import_helper
else:
    import _medfamily
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


class SwigPyIterator_medfamily_module(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator_medfamily_module, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator_medfamily_module, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _medfamily.delete_SwigPyIterator_medfamily_module
    __del__ = lambda self : None;
    def value(self): return _medfamily.SwigPyIterator_medfamily_module_value(self)
    def incr(self, n=1): return _medfamily.SwigPyIterator_medfamily_module_incr(self, n)
    def decr(self, n=1): return _medfamily.SwigPyIterator_medfamily_module_decr(self, n)
    def distance(self, *args): return _medfamily.SwigPyIterator_medfamily_module_distance(self, *args)
    def equal(self, *args): return _medfamily.SwigPyIterator_medfamily_module_equal(self, *args)
    def copy(self): return _medfamily.SwigPyIterator_medfamily_module_copy(self)
    def next(self): return _medfamily.SwigPyIterator_medfamily_module_next(self)
    def __next__(self): return _medfamily.SwigPyIterator_medfamily_module___next__(self)
    def previous(self): return _medfamily.SwigPyIterator_medfamily_module_previous(self)
    def advance(self, *args): return _medfamily.SwigPyIterator_medfamily_module_advance(self, *args)
    def __eq__(self, *args): return _medfamily.SwigPyIterator_medfamily_module___eq__(self, *args)
    def __ne__(self, *args): return _medfamily.SwigPyIterator_medfamily_module___ne__(self, *args)
    def __iadd__(self, *args): return _medfamily.SwigPyIterator_medfamily_module___iadd__(self, *args)
    def __isub__(self, *args): return _medfamily.SwigPyIterator_medfamily_module___isub__(self, *args)
    def __add__(self, *args): return _medfamily.SwigPyIterator_medfamily_module___add__(self, *args)
    def __sub__(self, *args): return _medfamily.SwigPyIterator_medfamily_module___sub__(self, *args)
    def __iter__(self): return self
    def __iter__(self): return self
SwigPyIterator_medfamily_module_swigregister = _medfamily.SwigPyIterator_medfamily_module_swigregister
SwigPyIterator_medfamily_module_swigregister(SwigPyIterator_medfamily_module)

ABSOLUTE_H5IPUBLIC_H = _medfamily.ABSOLUTE_H5IPUBLIC_H
ABSOLUTE_H5PUBLIC_H = _medfamily.ABSOLUTE_H5PUBLIC_H
HAVE_CC_C99 = _medfamily.HAVE_CC_C99
HAVE_CUSERID = _medfamily.HAVE_CUSERID
HAVE_DLFCN_H = _medfamily.HAVE_DLFCN_H
HAVE_FTIME = _medfamily.HAVE_FTIME
HAVE_GETEUID = _medfamily.HAVE_GETEUID
HAVE_GETPWUID = _medfamily.HAVE_GETPWUID
HAVE_GETTIMEOFDAY = _medfamily.HAVE_GETTIMEOFDAY
HAVE_H5IPUBLIC_H = _medfamily.HAVE_H5IPUBLIC_H
HAVE_H5PUBLIC_H = _medfamily.HAVE_H5PUBLIC_H
HAVE_INTTYPES_H = _medfamily.HAVE_INTTYPES_H
HAVE_LIBHDF5 = _medfamily.HAVE_LIBHDF5
HAVE_MALLOC_H = _medfamily.HAVE_MALLOC_H
HAVE_MEMORY_H = _medfamily.HAVE_MEMORY_H
HAVE_PWD_H = _medfamily.HAVE_PWD_H
HAVE_PYTHON = _medfamily.HAVE_PYTHON
HAVE_STDBOOL_H = _medfamily.HAVE_STDBOOL_H
HAVE_STDINT_H = _medfamily.HAVE_STDINT_H
HAVE_STDLIB_H = _medfamily.HAVE_STDLIB_H
HAVE_STRINGS_H = _medfamily.HAVE_STRINGS_H
HAVE_STRING_H = _medfamily.HAVE_STRING_H
HAVE_SYS_STAT_H = _medfamily.HAVE_SYS_STAT_H
HAVE_SYS_TIMEB_H = _medfamily.HAVE_SYS_TIMEB_H
HAVE_SYS_TIME_H = _medfamily.HAVE_SYS_TIME_H
HAVE_SYS_TYPES_H = _medfamily.HAVE_SYS_TYPES_H
HAVE_UNISTD_H = _medfamily.HAVE_UNISTD_H
HAVE__BOOL = _medfamily.HAVE__BOOL
LT_OBJDIR = _medfamily.LT_OBJDIR
MED_API_23 = _medfamily.MED_API_23
MED_CHECK_23FORMAT = _medfamily.MED_CHECK_23FORMAT
MED_HAVE_FORTRAN = _medfamily.MED_HAVE_FORTRAN
MED_HAVE_PYTHON = _medfamily.MED_HAVE_PYTHON
MESGERR = _medfamily.MESGERR
PACKAGE = _medfamily.PACKAGE
PACKAGE_BUGREPORT = _medfamily.PACKAGE_BUGREPORT
PACKAGE_NAME = _medfamily.PACKAGE_NAME
PACKAGE_STRING = _medfamily.PACKAGE_STRING
PACKAGE_TARNAME = _medfamily.PACKAGE_TARNAME
PACKAGE_URL = _medfamily.PACKAGE_URL
PACKAGE_VERSION = _medfamily.PACKAGE_VERSION
SIZEOF_FORTRAN_INTEGER = _medfamily.SIZEOF_FORTRAN_INTEGER
SIZEOF_INT = _medfamily.SIZEOF_INT
SIZEOF_LONG = _medfamily.SIZEOF_LONG
STDC_HEADERS = _medfamily.STDC_HEADERS
TIME_WITH_SYS_TIME = _medfamily.TIME_WITH_SYS_TIME
VERSION = _medfamily.VERSION
H5F_LIBVER_18 = _medfamily.H5F_LIBVER_18
MED_MAJOR_NUM = _medfamily.MED_MAJOR_NUM
MED_MINOR_NUM = _medfamily.MED_MINOR_NUM
MED_RELEASE_NUM = _medfamily.MED_RELEASE_NUM
MED_NUM_MAJEUR = _medfamily.MED_NUM_MAJEUR
MED_NUM_MINEUR = _medfamily.MED_NUM_MINEUR
MED_NUM_RELEASE = _medfamily.MED_NUM_RELEASE
MED_VERSION_STR = _medfamily.MED_VERSION_STR
MED_MAX_PARA = _medfamily.MED_MAX_PARA
MED_COMMENT_SIZE = _medfamily.MED_COMMENT_SIZE
MED_IDENT_SIZE = _medfamily.MED_IDENT_SIZE
MED_NAME_SIZE = _medfamily.MED_NAME_SIZE
MED_SNAME_SIZE = _medfamily.MED_SNAME_SIZE
MED_LNAME_SIZE = _medfamily.MED_LNAME_SIZE
MED_SNAME_BLANK = _medfamily.MED_SNAME_BLANK
MED_NAME_BLANK = _medfamily.MED_NAME_BLANK
MED_PATHNAME_SIZE = _medfamily.MED_PATHNAME_SIZE
MED_MAX_CHFID_PATH = _medfamily.MED_MAX_CHFID_PATH
MED_FULL_INTERLACE = _medfamily.MED_FULL_INTERLACE
MED_NO_INTERLACE = _medfamily.MED_NO_INTERLACE
MED_UNDEF_INTERLACE = _medfamily.MED_UNDEF_INTERLACE
MED_UNDEF_STMODE = _medfamily.MED_UNDEF_STMODE
MED_GLOBAL_STMODE = _medfamily.MED_GLOBAL_STMODE
MED_COMPACT_STMODE = _medfamily.MED_COMPACT_STMODE
MED_GLOBAL_PFLMODE = _medfamily.MED_GLOBAL_PFLMODE
MED_COMPACT_PFLMODE = _medfamily.MED_COMPACT_PFLMODE
MED_UNDEF_PFLMODE = _medfamily.MED_UNDEF_PFLMODE
MED_ACC_RDONLY = _medfamily.MED_ACC_RDONLY
MED_ACC_RDWR = _medfamily.MED_ACC_RDWR
MED_ACC_RDEXT = _medfamily.MED_ACC_RDEXT
MED_ACC_CREAT = _medfamily.MED_ACC_CREAT
MED_ACC_UNDEF = _medfamily.MED_ACC_UNDEF
MED_UNSTRUCTURED_MESH = _medfamily.MED_UNSTRUCTURED_MESH
MED_STRUCTURED_MESH = _medfamily.MED_STRUCTURED_MESH
MED_UNDEF_MESH_TYPE = _medfamily.MED_UNDEF_MESH_TYPE
MED_CARTESIAN_GRID = _medfamily.MED_CARTESIAN_GRID
MED_POLAR_GRID = _medfamily.MED_POLAR_GRID
MED_CURVILINEAR_GRID = _medfamily.MED_CURVILINEAR_GRID
MED_UNDEF_GRID_TYPE = _medfamily.MED_UNDEF_GRID_TYPE
MED_CELL = _medfamily.MED_CELL
MED_DESCENDING_FACE = _medfamily.MED_DESCENDING_FACE
MED_DESCENDING_EDGE = _medfamily.MED_DESCENDING_EDGE
MED_NODE = _medfamily.MED_NODE
MED_NODE_ELEMENT = _medfamily.MED_NODE_ELEMENT
MED_STRUCT_ELEMENT = _medfamily.MED_STRUCT_ELEMENT
MED_ALL_ENTITY_TYPE = _medfamily.MED_ALL_ENTITY_TYPE
MED_UNDEF_ENTITY_TYPE = _medfamily.MED_UNDEF_ENTITY_TYPE
MED_N_ENTITY_TYPES = _medfamily.MED_N_ENTITY_TYPES
MED_COORDINATE = _medfamily.MED_COORDINATE
MED_CONNECTIVITY = _medfamily.MED_CONNECTIVITY
MED_NAME = _medfamily.MED_NAME
MED_NUMBER = _medfamily.MED_NUMBER
MED_FAMILY_NUMBER = _medfamily.MED_FAMILY_NUMBER
MED_COORDINATE_AXIS1 = _medfamily.MED_COORDINATE_AXIS1
MED_COORDINATE_AXIS2 = _medfamily.MED_COORDINATE_AXIS2
MED_COORDINATE_AXIS3 = _medfamily.MED_COORDINATE_AXIS3
MED_INDEX_FACE = _medfamily.MED_INDEX_FACE
MED_INDEX_NODE = _medfamily.MED_INDEX_NODE
MED_GLOBAL_NUMBER = _medfamily.MED_GLOBAL_NUMBER
MED_VARIABLE_ATTRIBUTE = _medfamily.MED_VARIABLE_ATTRIBUTE
MED_COORDINATE_TRSF = _medfamily.MED_COORDINATE_TRSF
MED_UNDEF_DATATYPE = _medfamily.MED_UNDEF_DATATYPE
MED_INTERNAL_FLOAT64 = _medfamily.MED_INTERNAL_FLOAT64
MED_INTERNAL_INT32 = _medfamily.MED_INTERNAL_INT32
MED_INTERNAL_INT64 = _medfamily.MED_INTERNAL_INT64
MED_INTERNAL_INT = _medfamily.MED_INTERNAL_INT
MED_INTERNAL_NAME = _medfamily.MED_INTERNAL_NAME
MED_INTERNAL_SNAME = _medfamily.MED_INTERNAL_SNAME
MED_INTERNAL_LNAME = _medfamily.MED_INTERNAL_LNAME
MED_INTERNAL_IDENT = _medfamily.MED_INTERNAL_IDENT
MED_INTERNAL_CHAR = _medfamily.MED_INTERNAL_CHAR
MED_INTERNAL_UNDEF = _medfamily.MED_INTERNAL_UNDEF
MED_FLOAT64 = _medfamily.MED_FLOAT64
MED_INT32 = _medfamily.MED_INT32
MED_INT64 = _medfamily.MED_INT64
MED_INT = _medfamily.MED_INT
MED_ATT_FLOAT64 = _medfamily.MED_ATT_FLOAT64
MED_ATT_INT = _medfamily.MED_ATT_INT
MED_ATT_NAME = _medfamily.MED_ATT_NAME
MED_ATT_UNDEF = _medfamily.MED_ATT_UNDEF
MED_MESH = _medfamily.MED_MESH
MED_FIELD = _medfamily.MED_FIELD
MED_LIBRARY = _medfamily.MED_LIBRARY
MED_FILE = _medfamily.MED_FILE
MED_MESH_SUPPORT = _medfamily.MED_MESH_SUPPORT
MED_ELSTRUCT = _medfamily.MED_ELSTRUCT
MED_FAMILY = _medfamily.MED_FAMILY
MED_EQUIVALENCE = _medfamily.MED_EQUIVALENCE
MED_GROUP = _medfamily.MED_GROUP
MED_JOINT = _medfamily.MED_JOINT
MED_LOCALIZATION = _medfamily.MED_LOCALIZATION
MED_PROFILE = _medfamily.MED_PROFILE
MED_FILTER = _medfamily.MED_FILTER
MED_INTERPOLATION = _medfamily.MED_INTERPOLATION
MED_NUMERICAL_DATA = _medfamily.MED_NUMERICAL_DATA
MED_LINK = _medfamily.MED_LINK
MED_CLASS_UNDEF = _medfamily.MED_CLASS_UNDEF
MED_CLASS_ALL = _medfamily.MED_CLASS_ALL
MED_POINT1 = _medfamily.MED_POINT1
MED_SEG2 = _medfamily.MED_SEG2
MED_SEG3 = _medfamily.MED_SEG3
MED_SEG4 = _medfamily.MED_SEG4
MED_TRIA3 = _medfamily.MED_TRIA3
MED_QUAD4 = _medfamily.MED_QUAD4
MED_TRIA6 = _medfamily.MED_TRIA6
MED_TRIA7 = _medfamily.MED_TRIA7
MED_QUAD8 = _medfamily.MED_QUAD8
MED_QUAD9 = _medfamily.MED_QUAD9
MED_TETRA4 = _medfamily.MED_TETRA4
MED_PYRA5 = _medfamily.MED_PYRA5
MED_PENTA6 = _medfamily.MED_PENTA6
MED_HEXA8 = _medfamily.MED_HEXA8
MED_TETRA10 = _medfamily.MED_TETRA10
MED_OCTA12 = _medfamily.MED_OCTA12
MED_PYRA13 = _medfamily.MED_PYRA13
MED_PENTA15 = _medfamily.MED_PENTA15
MED_HEXA20 = _medfamily.MED_HEXA20
MED_HEXA27 = _medfamily.MED_HEXA27
MED_POLYGON = _medfamily.MED_POLYGON
MED_POLYGON2 = _medfamily.MED_POLYGON2
MED_POLYHEDRON = _medfamily.MED_POLYHEDRON
MED_STRUCT_GEO_INTERNAL = _medfamily.MED_STRUCT_GEO_INTERNAL
MED_STRUCT_GEO_SUP_INTERNAL = _medfamily.MED_STRUCT_GEO_SUP_INTERNAL
MED_NONE = _medfamily.MED_NONE
MED_NO_GEOTYPE = _medfamily.MED_NO_GEOTYPE
MED_UNDEF_GEOTYPE = _medfamily.MED_UNDEF_GEOTYPE
MED_UNDEF_GEOMETRY_TYPE = _medfamily.MED_UNDEF_GEOMETRY_TYPE
MED_ALL_GEOTYPE = _medfamily.MED_ALL_GEOTYPE
MED_GEO_ALL = _medfamily.MED_GEO_ALL
MED_N_CELL_GEO = _medfamily.MED_N_CELL_GEO
MED_N_CELL_FIXED_GEO = _medfamily.MED_N_CELL_FIXED_GEO
MED_N_CELL_GEO_FIXED_CON = _medfamily.MED_N_CELL_GEO_FIXED_CON
MED_N_FACE_GEO = _medfamily.MED_N_FACE_GEO
MED_N_FACE_FIXED_GEO = _medfamily.MED_N_FACE_FIXED_GEO
MED_N_FACE_GEO_FIXED_CON = _medfamily.MED_N_FACE_GEO_FIXED_CON
MED_N_EDGE_TYPES = _medfamily.MED_N_EDGE_TYPES
MED_N_EDGE_FIXED_GEO = _medfamily.MED_N_EDGE_FIXED_GEO
MED_N_EDGE_GEO_FIXED_CON = _medfamily.MED_N_EDGE_GEO_FIXED_CON
MED_N_NODE_GEO = _medfamily.MED_N_NODE_GEO
MED_N_NODE_FIXED_GEO = _medfamily.MED_N_NODE_FIXED_GEO
MED_N_NODE_GEO_FIXED_CON = _medfamily.MED_N_NODE_GEO_FIXED_CON
MED_NODAL = _medfamily.MED_NODAL
MED_DESCENDING = _medfamily.MED_DESCENDING
MED_UNDEF_CONNECTIVITY_MODE = _medfamily.MED_UNDEF_CONNECTIVITY_MODE
MED_NO_CMODE = _medfamily.MED_NO_CMODE
MED_CARTESIAN = _medfamily.MED_CARTESIAN
MED_CYLINDRICAL = _medfamily.MED_CYLINDRICAL
MED_SPHERICAL = _medfamily.MED_SPHERICAL
MED_UNDEF_AXIS_TYPE = _medfamily.MED_UNDEF_AXIS_TYPE
MED_FALSE = _medfamily.MED_FALSE
MED_TRUE = _medfamily.MED_TRUE
MED_GAUSS_ELNO = _medfamily.MED_GAUSS_ELNO
MED_IPOINT_ELNO = _medfamily.MED_IPOINT_ELNO
MED_NO_NAME = _medfamily.MED_NO_NAME
MED_NO_MESHNAME = _medfamily.MED_NO_MESHNAME
MED_NO_MESH = _medfamily.MED_NO_MESH
MED_NO_MESH_SUPPORT = _medfamily.MED_NO_MESH_SUPPORT
MED_NO_LOCALIZATION = _medfamily.MED_NO_LOCALIZATION
MED_NO_INTERPOLATION = _medfamily.MED_NO_INTERPOLATION
MED_NO_IPOINT_INTERNAL = _medfamily.MED_NO_IPOINT_INTERNAL
MED_NO_PROFILE = _medfamily.MED_NO_PROFILE
MED_NO_GROUP = _medfamily.MED_NO_GROUP
MED_ALLENTITIES_PROFILE = _medfamily.MED_ALLENTITIES_PROFILE
MED_NO_PROFILE_INTERNAL = _medfamily.MED_NO_PROFILE_INTERNAL
MED_SAME_PROFILE_INTERNAL = _medfamily.MED_SAME_PROFILE_INTERNAL
MED_ALL_CONSTITUENT = _medfamily.MED_ALL_CONSTITUENT
MED_UNDEF_SIZE = _medfamily.MED_UNDEF_SIZE
MED_NO_PROFILE_SIZE = _medfamily.MED_NO_PROFILE_SIZE
MED_SORT_DTIT = _medfamily.MED_SORT_DTIT
MED_SORT_ITDT = _medfamily.MED_SORT_ITDT
MED_SORT_UNDEF = _medfamily.MED_SORT_UNDEF
MED_NO_DT = _medfamily.MED_NO_DT
MED_NO_IT = _medfamily.MED_NO_IT
MED_UNDEF_DT = _medfamily.MED_UNDEF_DT
MED_ATT_NOT_FILLED = _medfamily.MED_ATT_NOT_FILLED
MED_MAX_FILTER_SPACES = _medfamily.MED_MAX_FILTER_SPACES
class med_filter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, med_filter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, med_filter, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nspaces"] = _medfamily.med_filter_nspaces_set
    __swig_getmethods__["nspaces"] = _medfamily.med_filter_nspaces_get
    if _newclass:nspaces = _swig_property(_medfamily.med_filter_nspaces_get, _medfamily.med_filter_nspaces_set)
    __swig_setmethods__["memspace"] = _medfamily.med_filter_memspace_set
    __swig_getmethods__["memspace"] = _medfamily.med_filter_memspace_get
    if _newclass:memspace = _swig_property(_medfamily.med_filter_memspace_get, _medfamily.med_filter_memspace_set)
    __swig_setmethods__["diskspace"] = _medfamily.med_filter_diskspace_set
    __swig_getmethods__["diskspace"] = _medfamily.med_filter_diskspace_get
    if _newclass:diskspace = _swig_property(_medfamily.med_filter_diskspace_get, _medfamily.med_filter_diskspace_set)
    __swig_setmethods__["nentity"] = _medfamily.med_filter_nentity_set
    __swig_getmethods__["nentity"] = _medfamily.med_filter_nentity_get
    if _newclass:nentity = _swig_property(_medfamily.med_filter_nentity_get, _medfamily.med_filter_nentity_set)
    __swig_setmethods__["nvaluesperentity"] = _medfamily.med_filter_nvaluesperentity_set
    __swig_getmethods__["nvaluesperentity"] = _medfamily.med_filter_nvaluesperentity_get
    if _newclass:nvaluesperentity = _swig_property(_medfamily.med_filter_nvaluesperentity_get, _medfamily.med_filter_nvaluesperentity_set)
    __swig_setmethods__["nconstituentpervalue"] = _medfamily.med_filter_nconstituentpervalue_set
    __swig_getmethods__["nconstituentpervalue"] = _medfamily.med_filter_nconstituentpervalue_get
    if _newclass:nconstituentpervalue = _swig_property(_medfamily.med_filter_nconstituentpervalue_get, _medfamily.med_filter_nconstituentpervalue_set)
    __swig_setmethods__["constituentselect"] = _medfamily.med_filter_constituentselect_set
    __swig_getmethods__["constituentselect"] = _medfamily.med_filter_constituentselect_get
    if _newclass:constituentselect = _swig_property(_medfamily.med_filter_constituentselect_get, _medfamily.med_filter_constituentselect_set)
    __swig_setmethods__["switchmode"] = _medfamily.med_filter_switchmode_set
    __swig_getmethods__["switchmode"] = _medfamily.med_filter_switchmode_get
    if _newclass:switchmode = _swig_property(_medfamily.med_filter_switchmode_get, _medfamily.med_filter_switchmode_set)
    __swig_setmethods__["filterarraysize"] = _medfamily.med_filter_filterarraysize_set
    __swig_getmethods__["filterarraysize"] = _medfamily.med_filter_filterarraysize_get
    if _newclass:filterarraysize = _swig_property(_medfamily.med_filter_filterarraysize_get, _medfamily.med_filter_filterarraysize_set)
    __swig_setmethods__["filterarray23v30"] = _medfamily.med_filter_filterarray23v30_set
    __swig_getmethods__["filterarray23v30"] = _medfamily.med_filter_filterarray23v30_get
    if _newclass:filterarray23v30 = _swig_property(_medfamily.med_filter_filterarray23v30_get, _medfamily.med_filter_filterarray23v30_set)
    __swig_setmethods__["profilearraysize"] = _medfamily.med_filter_profilearraysize_set
    __swig_getmethods__["profilearraysize"] = _medfamily.med_filter_profilearraysize_get
    if _newclass:profilearraysize = _swig_property(_medfamily.med_filter_profilearraysize_get, _medfamily.med_filter_profilearraysize_set)
    __swig_setmethods__["storagemode"] = _medfamily.med_filter_storagemode_set
    __swig_getmethods__["storagemode"] = _medfamily.med_filter_storagemode_get
    if _newclass:storagemode = _swig_property(_medfamily.med_filter_storagemode_get, _medfamily.med_filter_storagemode_set)
    __swig_setmethods__["profilename"] = _medfamily.med_filter_profilename_set
    __swig_getmethods__["profilename"] = _medfamily.med_filter_profilename_get
    if _newclass:profilename = _swig_property(_medfamily.med_filter_profilename_get, _medfamily.med_filter_profilename_set)
    def __init__(self): 
        """__init__(self) -> med_filter"""
        this = _medfamily.new_med_filter()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _medfamily.delete_med_filter
    __del__ = lambda self : None;
med_filter_swigregister = _medfamily.med_filter_swigregister
med_filter_swigregister(med_filter)

MED_NO_FILTER_SIZE = _medfamily.MED_NO_FILTER_SIZE
MED_NO_PROFILE_F = _medfamily.MED_NO_PROFILE_F
class med_file_version(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, med_file_version, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, med_file_version, name)
    __repr__ = _swig_repr
    __swig_setmethods__["majeur"] = _medfamily.med_file_version_majeur_set
    __swig_getmethods__["majeur"] = _medfamily.med_file_version_majeur_get
    if _newclass:majeur = _swig_property(_medfamily.med_file_version_majeur_get, _medfamily.med_file_version_majeur_set)
    __swig_setmethods__["mineur"] = _medfamily.med_file_version_mineur_set
    __swig_getmethods__["mineur"] = _medfamily.med_file_version_mineur_get
    if _newclass:mineur = _swig_property(_medfamily.med_file_version_mineur_get, _medfamily.med_file_version_mineur_set)
    __swig_setmethods__["release"] = _medfamily.med_file_version_release_set
    __swig_getmethods__["release"] = _medfamily.med_file_version_release_get
    if _newclass:release = _swig_property(_medfamily.med_file_version_release_get, _medfamily.med_file_version_release_set)
    def __init__(self): 
        """__init__(self) -> med_file_version"""
        this = _medfamily.new_med_file_version()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _medfamily.delete_med_file_version
    __del__ = lambda self : None;
med_file_version_swigregister = _medfamily.med_file_version_swigregister
med_file_version_swigregister(med_file_version)

MED_PARTICLE_NAME = _medfamily.MED_PARTICLE_NAME
MED_BALL_NAME = _medfamily.MED_BALL_NAME
MED_BEAM_NAME = _medfamily.MED_BEAM_NAME
MED_PARTICLE_LABEL = _medfamily.MED_PARTICLE_LABEL
MED_BALL_DIAMETER = _medfamily.MED_BALL_DIAMETER
MED_BEAM_THICKNESS = _medfamily.MED_BEAM_THICKNESS
import medenum
class MEDBOOL(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MEDBOOL, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MEDBOOL, name)
    __repr__ = _swig_repr
    def iterator(self): return _medfamily.MEDBOOL_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _medfamily.MEDBOOL___nonzero__(self)
    def __bool__(self): return _medfamily.MEDBOOL___bool__(self)
    def __len__(self): return _medfamily.MEDBOOL___len__(self)
    def pop(self): return _medfamily.MEDBOOL_pop(self)
    def __getslice__(self, *args): return _medfamily.MEDBOOL___getslice__(self, *args)
    def __setslice__(self, *args): return _medfamily.MEDBOOL___setslice__(self, *args)
    def __delslice__(self, *args): return _medfamily.MEDBOOL___delslice__(self, *args)
    def __delitem__(self, *args): return _medfamily.MEDBOOL___delitem__(self, *args)
    def __getitem__(self, *args): return _medfamily.MEDBOOL___getitem__(self, *args)
    def __setitem__(self, *args): return _medfamily.MEDBOOL___setitem__(self, *args)
    def append(self, *args): return _medfamily.MEDBOOL_append(self, *args)
    def empty(self): return _medfamily.MEDBOOL_empty(self)
    def size(self): return _medfamily.MEDBOOL_size(self)
    def clear(self): return _medfamily.MEDBOOL_clear(self)
    def swap(self, *args): return _medfamily.MEDBOOL_swap(self, *args)
    def get_allocator(self): return _medfamily.MEDBOOL_get_allocator(self)
    def begin(self): return _medfamily.MEDBOOL_begin(self)
    def end(self): return _medfamily.MEDBOOL_end(self)
    def rbegin(self): return _medfamily.MEDBOOL_rbegin(self)
    def rend(self): return _medfamily.MEDBOOL_rend(self)
    def pop_back(self): return _medfamily.MEDBOOL_pop_back(self)
    def erase(self, *args): return _medfamily.MEDBOOL_erase(self, *args)
    def __init__(self, *args): 
        this = _medfamily.new_MEDBOOL(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _medfamily.MEDBOOL_push_back(self, *args)
    def front(self): return _medfamily.MEDBOOL_front(self)
    def back(self): return _medfamily.MEDBOOL_back(self)
    def assign(self, *args): return _medfamily.MEDBOOL_assign(self, *args)
    def resize(self, *args): return _medfamily.MEDBOOL_resize(self, *args)
    def insert(self, *args): return _medfamily.MEDBOOL_insert(self, *args)
    def reserve(self, *args): return _medfamily.MEDBOOL_reserve(self, *args)
    def capacity(self): return _medfamily.MEDBOOL_capacity(self)
    __swig_destroy__ = _medfamily.delete_MEDBOOL
    __del__ = lambda self : None;
MEDBOOL_swigregister = _medfamily.MEDBOOL_swigregister
MEDBOOL_swigregister(MEDBOOL)
cvar = _medfamily.cvar
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
    def iterator(self): return _medfamily.MEDFLOAT_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _medfamily.MEDFLOAT___nonzero__(self)
    def __bool__(self): return _medfamily.MEDFLOAT___bool__(self)
    def __len__(self): return _medfamily.MEDFLOAT___len__(self)
    def pop(self): return _medfamily.MEDFLOAT_pop(self)
    def __getslice__(self, *args): return _medfamily.MEDFLOAT___getslice__(self, *args)
    def __setslice__(self, *args): return _medfamily.MEDFLOAT___setslice__(self, *args)
    def __delslice__(self, *args): return _medfamily.MEDFLOAT___delslice__(self, *args)
    def __delitem__(self, *args): return _medfamily.MEDFLOAT___delitem__(self, *args)
    def __getitem__(self, *args): return _medfamily.MEDFLOAT___getitem__(self, *args)
    def __setitem__(self, *args): return _medfamily.MEDFLOAT___setitem__(self, *args)
    def append(self, *args): return _medfamily.MEDFLOAT_append(self, *args)
    def empty(self): return _medfamily.MEDFLOAT_empty(self)
    def size(self): return _medfamily.MEDFLOAT_size(self)
    def clear(self): return _medfamily.MEDFLOAT_clear(self)
    def swap(self, *args): return _medfamily.MEDFLOAT_swap(self, *args)
    def get_allocator(self): return _medfamily.MEDFLOAT_get_allocator(self)
    def begin(self): return _medfamily.MEDFLOAT_begin(self)
    def end(self): return _medfamily.MEDFLOAT_end(self)
    def rbegin(self): return _medfamily.MEDFLOAT_rbegin(self)
    def rend(self): return _medfamily.MEDFLOAT_rend(self)
    def pop_back(self): return _medfamily.MEDFLOAT_pop_back(self)
    def erase(self, *args): return _medfamily.MEDFLOAT_erase(self, *args)
    def __init__(self, *args): 
        this = _medfamily.new_MEDFLOAT(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _medfamily.MEDFLOAT_push_back(self, *args)
    def front(self): return _medfamily.MEDFLOAT_front(self)
    def back(self): return _medfamily.MEDFLOAT_back(self)
    def assign(self, *args): return _medfamily.MEDFLOAT_assign(self, *args)
    def resize(self, *args): return _medfamily.MEDFLOAT_resize(self, *args)
    def insert(self, *args): return _medfamily.MEDFLOAT_insert(self, *args)
    def reserve(self, *args): return _medfamily.MEDFLOAT_reserve(self, *args)
    def capacity(self): return _medfamily.MEDFLOAT_capacity(self)
    def __iadd__(self, *args): return _medfamily.MEDFLOAT___iadd__(self, *args)
    def __add__(self, *args): return _medfamily.MEDFLOAT___add__(self, *args)
    def __isub__(self, *args): return _medfamily.MEDFLOAT___isub__(self, *args)
    def __sub__(self, *args): return _medfamily.MEDFLOAT___sub__(self, *args)
    def __imul__(self, *args): return _medfamily.MEDFLOAT___imul__(self, *args)
    def __mul__(self, *args): return _medfamily.MEDFLOAT___mul__(self, *args)
    def __idiv__(self, *args): return _medfamily.MEDFLOAT___idiv__(self, *args)
    def __div__(self, *args): return _medfamily.MEDFLOAT___div__(self, *args)
    def __le__(self, *args): return _medfamily.MEDFLOAT___le__(self, *args)
    def __lt__(self, *args): return _medfamily.MEDFLOAT___lt__(self, *args)
    def __gt__(self, *args): return _medfamily.MEDFLOAT___gt__(self, *args)
    def __ge__(self, *args): return _medfamily.MEDFLOAT___ge__(self, *args)
    def __eq__(self, *args): return _medfamily.MEDFLOAT___eq__(self, *args)
    def __ne__(self, *args): return _medfamily.MEDFLOAT___ne__(self, *args)
    __swig_destroy__ = _medfamily.delete_MEDFLOAT
    __del__ = lambda self : None;
MEDFLOAT_swigregister = _medfamily.MEDFLOAT_swigregister
MEDFLOAT_swigregister(MEDFLOAT)

MEDFLOAT.__str__= lambda self: str([x for x in self])
MEDFLOAT.__repr__= lambda self:"MEDFLOAT" +"("+str([x for x in self])+")"

class MEDINT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MEDINT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MEDINT, name)
    __repr__ = _swig_repr
    def iterator(self): return _medfamily.MEDINT_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _medfamily.MEDINT___nonzero__(self)
    def __bool__(self): return _medfamily.MEDINT___bool__(self)
    def __len__(self): return _medfamily.MEDINT___len__(self)
    def pop(self): return _medfamily.MEDINT_pop(self)
    def __getslice__(self, *args): return _medfamily.MEDINT___getslice__(self, *args)
    def __setslice__(self, *args): return _medfamily.MEDINT___setslice__(self, *args)
    def __delslice__(self, *args): return _medfamily.MEDINT___delslice__(self, *args)
    def __delitem__(self, *args): return _medfamily.MEDINT___delitem__(self, *args)
    def __getitem__(self, *args): return _medfamily.MEDINT___getitem__(self, *args)
    def __setitem__(self, *args): return _medfamily.MEDINT___setitem__(self, *args)
    def append(self, *args): return _medfamily.MEDINT_append(self, *args)
    def empty(self): return _medfamily.MEDINT_empty(self)
    def size(self): return _medfamily.MEDINT_size(self)
    def clear(self): return _medfamily.MEDINT_clear(self)
    def swap(self, *args): return _medfamily.MEDINT_swap(self, *args)
    def get_allocator(self): return _medfamily.MEDINT_get_allocator(self)
    def begin(self): return _medfamily.MEDINT_begin(self)
    def end(self): return _medfamily.MEDINT_end(self)
    def rbegin(self): return _medfamily.MEDINT_rbegin(self)
    def rend(self): return _medfamily.MEDINT_rend(self)
    def pop_back(self): return _medfamily.MEDINT_pop_back(self)
    def erase(self, *args): return _medfamily.MEDINT_erase(self, *args)
    def __init__(self, *args): 
        this = _medfamily.new_MEDINT(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _medfamily.MEDINT_push_back(self, *args)
    def front(self): return _medfamily.MEDINT_front(self)
    def back(self): return _medfamily.MEDINT_back(self)
    def assign(self, *args): return _medfamily.MEDINT_assign(self, *args)
    def resize(self, *args): return _medfamily.MEDINT_resize(self, *args)
    def insert(self, *args): return _medfamily.MEDINT_insert(self, *args)
    def reserve(self, *args): return _medfamily.MEDINT_reserve(self, *args)
    def capacity(self): return _medfamily.MEDINT_capacity(self)
    def __iadd__(self, *args): return _medfamily.MEDINT___iadd__(self, *args)
    def __add__(self, *args): return _medfamily.MEDINT___add__(self, *args)
    def __isub__(self, *args): return _medfamily.MEDINT___isub__(self, *args)
    def __sub__(self, *args): return _medfamily.MEDINT___sub__(self, *args)
    def __imul__(self, *args): return _medfamily.MEDINT___imul__(self, *args)
    def __mul__(self, *args): return _medfamily.MEDINT___mul__(self, *args)
    def __idiv__(self, *args): return _medfamily.MEDINT___idiv__(self, *args)
    def __div__(self, *args): return _medfamily.MEDINT___div__(self, *args)
    def __le__(self, *args): return _medfamily.MEDINT___le__(self, *args)
    def __lt__(self, *args): return _medfamily.MEDINT___lt__(self, *args)
    def __gt__(self, *args): return _medfamily.MEDINT___gt__(self, *args)
    def __ge__(self, *args): return _medfamily.MEDINT___ge__(self, *args)
    def __eq__(self, *args): return _medfamily.MEDINT___eq__(self, *args)
    def __ne__(self, *args): return _medfamily.MEDINT___ne__(self, *args)
    __swig_destroy__ = _medfamily.delete_MEDINT
    __del__ = lambda self : None;
MEDINT_swigregister = _medfamily.MEDINT_swigregister
MEDINT_swigregister(MEDINT)

MEDINT.__str__= lambda self: str([x for x in self])
MEDINT.__repr__= lambda self:"MEDINT" +"("+str([x for x in self])+")"

class MEDCHAR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MEDCHAR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MEDCHAR, name)
    __repr__ = _swig_repr
    def iterator(self): return _medfamily.MEDCHAR_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _medfamily.MEDCHAR___nonzero__(self)
    def __bool__(self): return _medfamily.MEDCHAR___bool__(self)
    def __len__(self): return _medfamily.MEDCHAR___len__(self)
    def pop(self): return _medfamily.MEDCHAR_pop(self)
    def __getslice__(self, *args): return _medfamily.MEDCHAR___getslice__(self, *args)
    def __setslice__(self, *args): return _medfamily.MEDCHAR___setslice__(self, *args)
    def __delslice__(self, *args): return _medfamily.MEDCHAR___delslice__(self, *args)
    def __delitem__(self, *args): return _medfamily.MEDCHAR___delitem__(self, *args)
    def __getitem__(self, *args): return _medfamily.MEDCHAR___getitem__(self, *args)
    def __setitem__(self, *args): return _medfamily.MEDCHAR___setitem__(self, *args)
    def append(self, *args): return _medfamily.MEDCHAR_append(self, *args)
    def empty(self): return _medfamily.MEDCHAR_empty(self)
    def size(self): return _medfamily.MEDCHAR_size(self)
    def clear(self): return _medfamily.MEDCHAR_clear(self)
    def swap(self, *args): return _medfamily.MEDCHAR_swap(self, *args)
    def get_allocator(self): return _medfamily.MEDCHAR_get_allocator(self)
    def begin(self): return _medfamily.MEDCHAR_begin(self)
    def end(self): return _medfamily.MEDCHAR_end(self)
    def rbegin(self): return _medfamily.MEDCHAR_rbegin(self)
    def rend(self): return _medfamily.MEDCHAR_rend(self)
    def pop_back(self): return _medfamily.MEDCHAR_pop_back(self)
    def erase(self, *args): return _medfamily.MEDCHAR_erase(self, *args)
    def __init__(self, *args): 
        this = _medfamily.new_MEDCHAR(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _medfamily.MEDCHAR_push_back(self, *args)
    def front(self): return _medfamily.MEDCHAR_front(self)
    def back(self): return _medfamily.MEDCHAR_back(self)
    def assign(self, *args): return _medfamily.MEDCHAR_assign(self, *args)
    def resize(self, *args): return _medfamily.MEDCHAR_resize(self, *args)
    def insert(self, *args): return _medfamily.MEDCHAR_insert(self, *args)
    def reserve(self, *args): return _medfamily.MEDCHAR_reserve(self, *args)
    def capacity(self): return _medfamily.MEDCHAR_capacity(self)
    def __iadd__(self, *args): return _medfamily.MEDCHAR___iadd__(self, *args)
    def __add__(self, *args): return _medfamily.MEDCHAR___add__(self, *args)
    def __isub__(self, *args): return _medfamily.MEDCHAR___isub__(self, *args)
    def __sub__(self, *args): return _medfamily.MEDCHAR___sub__(self, *args)
    def __imul__(self, *args): return _medfamily.MEDCHAR___imul__(self, *args)
    def __mul__(self, *args): return _medfamily.MEDCHAR___mul__(self, *args)
    def __idiv__(self, *args): return _medfamily.MEDCHAR___idiv__(self, *args)
    def __div__(self, *args): return _medfamily.MEDCHAR___div__(self, *args)
    def __le__(self, *args): return _medfamily.MEDCHAR___le__(self, *args)
    def __lt__(self, *args): return _medfamily.MEDCHAR___lt__(self, *args)
    def __gt__(self, *args): return _medfamily.MEDCHAR___gt__(self, *args)
    def __ge__(self, *args): return _medfamily.MEDCHAR___ge__(self, *args)
    def __eq__(self, *args): return _medfamily.MEDCHAR___eq__(self, *args)
    def __ne__(self, *args): return _medfamily.MEDCHAR___ne__(self, *args)
    __swig_destroy__ = _medfamily.delete_MEDCHAR
    __del__ = lambda self : None;
MEDCHAR_swigregister = _medfamily.MEDCHAR_swigregister
MEDCHAR_swigregister(MEDCHAR)

MEDCHAR.__str__= lambda self: str([x for x in self])
MEDCHAR.__repr__= lambda self:"MEDCHAR" +"("+str([x for x in self])+")"

MEDCHAR.__str__= lambda self: str([x for x in self])
MEDCHAR.__repr__= lambda self:"MEDCHAR" +"("+str([x for x in self])+")"

MEDCHAR.__str__= lambda self: str([x for x in self])
MEDCHAR.__repr__= lambda self:"MEDCHAR" +"("+str([x for x in self])+")"

MEDCHAR.__str__= lambda self: str([x for x in self])
MEDCHAR.__repr__= lambda self:"MEDCHAR" +"("+str([x for x in self])+")"

MEDCHAR.__str__= lambda self: str([x for x in self])
MEDCHAR.__repr__= lambda self:"MEDCHAR" +"("+str([x for x in self])+")"


def MEDfamilyCr(*args, **kwargs):
  """
    MEDfamilyCr(fid, meshname, familyname, familynumber, ngroup, groupname) -> med_err

    Parameters:
        fid: med_idt const
        meshname: char const *const
        familyname: char const *const
        familynumber: med_int const
        ngroup: med_int const
        groupname: char const *const

    """
  return _medfamily.MEDfamilyCr(*args, **kwargs)

def MEDnFamily(*args, **kwargs):
  """
    MEDnFamily(fid, meshname) -> med_int

    Parameters:
        fid: med_idt const
        meshname: char const *const

    """
  return _medfamily.MEDnFamily(*args, **kwargs)

def MEDnFamilyGroup(*args, **kwargs):
  """
    MEDnFamilyGroup(fid, meshname, famit) -> med_int

    Parameters:
        fid: med_idt const
        meshname: char const *const
        famit: int const

    """
  return _medfamily.MEDnFamilyGroup(*args, **kwargs)

def MEDfamilyInfo(*args, **kwargs):
  """
    MEDfamilyInfo(fid, meshname, famit, groupname) -> med_err

    Parameters:
        fid: med_idt const
        meshname: char const *const
        famit: int const
        groupname: char *const

    """
  return _medfamily.MEDfamilyInfo(*args, **kwargs)

def MEDnFamily23Attribute(*args, **kwargs):
  """
    MEDnFamily23Attribute(fid, meshname, famit) -> med_int

    Parameters:
        fid: med_idt const
        meshname: char const *const
        famit: int const

    """
  return _medfamily.MEDnFamily23Attribute(*args, **kwargs)

def MEDfamily23Info(*args, **kwargs):
  """
    MEDfamily23Info(fid, meshname, famit, attributenumber, attributevalue, attributedes, groupname) -> med_err

    Parameters:
        fid: med_idt const
        meshname: char const *const
        famit: int const
        attributenumber: med_int *const
        attributevalue: med_int *const
        attributedes: char *const
        groupname: char *const

    """
  return _medfamily.MEDfamily23Info(*args, **kwargs)
# This file is compatible with both classic and new-style classes.


