from VTK_routines import *
import cdmath

#Meshes and fields initialisation
#================================

#cell field on 2D structured mesh
M1 = cdmath.Mesh(0.0, 1.0, 10, 0., 1., 5)

field1 = cdmath.Field("test field 1", cdmath.CELLS, M1, 1)
for j in range(field1.getNumberOfComponents()):
    for i in range(field1.getNumberOfElements()):
        field1[i, j] = i + j

fileNameVTK1 = "2D_structured_cell_field"
field1.writeVTK(fileNameVTK1)

#node field on 2D unstructured mesh
M2 = cdmath.Mesh("meshSquare.med")
field2 = cdmath.Field("test field 2", cdmath.NODES, M2, 1)
for j in range(field2.getNumberOfComponents()):
    for i in range(field2.getNumberOfElements()):
        field2[i, j] = i + j

fileNameVTK2 = "2D_unstructured_node_field"
field2.writeVTK(fileNameVTK2)

#node field on 3D unstructured mesh
M3 = cdmath.Mesh("meshCube.med")
field3 = cdmath.Field("test field 3", cdmath.NODES, M3, 1)
for j in range(field3.getNumberOfComponents()):
    for i in range(field3.getNumberOfElements()):
        field3[i, j] = i + j

fileNameVTK3 = "3D_unstructured_node_field"
field3.writeVTK(fileNameVTK3)

#node field on sphere with unstructured mesh
M4 = cdmath.Mesh("meshSphere.med")
field4 = cdmath.Field("test field 4", cdmath.NODES, M4, 1)
for j in range(field4.getNumberOfComponents()):
    for i in range(field4.getNumberOfElements()):
        field4[i, j] = i + j

fileNameVTK4 = "Sphere_unstructured_node_field"
field4.writeVTK(fileNameVTK4)

#cell field on 3D structured mesh
M5 = cdmath.Mesh(0.0, 1.0, 4, 0.0, 1.0, 4, 0.0, 1.0, 4)
field5 = cdmath.Field("test field 5", cdmath.CELLS, M5, 1)
for j in range(field5.getNumberOfComponents()):
    for i in range(field5.getNumberOfElements()):
        field5[i, j] = i + j

fileNameVTK5 = "3D_structured_cell_field"
field5.writeVTK(fileNameVTK5)

#2D tests
#===========================================
point1=[1,0,0]
point2=[0,1,0]
resolution=100

outputFileName="Extract_VTK_over_line_"+fileNameVTK1+".csv"
Extract_VTK_data_over_line_to_csv_file(fileNameVTK1, outputFileName, point1, point2, resolution)

outputFileName="Extract_field_over_line_"+fileNameVTK1+".csv"
Extract_field_data_over_line_to_csv_file(field2, point1, point2, resolution, outputFileName)

point=[0.5,0.5,0]
normal=[1,1,0]
Slice_VTK_data_to_csv_file(fileNameVTK3, outputFileName, point, normal,resolution )
