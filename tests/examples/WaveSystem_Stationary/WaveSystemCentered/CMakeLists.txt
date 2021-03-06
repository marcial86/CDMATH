
SET(MESH_MED
  ../../../ressources/squareWithTriangles.med
  ../../../ressources/meshCube.med
  ../../../ressources/squareWithSquares.med
  ../../../ressources/cubeWithCubes.med
  ../../../ressources/diskWithTriangles.med
  ../../../ressources/diskWithSquares.med
  ../../../ressources/diskWithSpiderWeb.med
  ../../../ressources/diskWithHexagons.med
  ../../../ressources/ballWithTetrahedra.med
  )

file(COPY ${MESH_MED} DESTINATION ${CMAKE_BINARY_DIR}/tests/examples/WaveSystemCentered)
install(FILES ${MESH_MED} DESTINATION share/examples/WaveSystemCentered)

if (CDMATH_WITH_PYTHON AND CDMATH_WITH_PETSC AND CDMATH_WITH_POSTPRO)

    SET(MESH_FILE  ../../../ressources/meshSquare.med  )

    ADD_TEST(ExampleWaveSystem_2DVortex_Centered_SQUARE_triangles ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/WaveSystemCentered.py  ${MESH_FILE})
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_SQUARE_triangles PROPERTY ENVIRONMENT "LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${CMAKE_INSTALL_PREFIX}/lib/medcoupling:${CMAKE_INSTALL_PREFIX}/lib/med:${PETSC_DIR}/${PETSC_ARCH}/lib:${HDF5_ROOT_DIR}/lib:${PV_LIB_DIR}")
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_SQUARE_triangles APPEND PROPERTY ENVIRONMENT "PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}:${CDMATH_BINARY_DIR}/postprocessing:${CMAKE_INSTALL_PREFIX}/${MEDCOUPLING_INSTALL_PYTHON}:${PV_PYTHON_DIR}:${CMAKE_INSTALL_PREFIX}/lib/cdmath:${CMAKE_INSTALL_PREFIX}/bin/cdmath")

    SET(MESH_FILE  ../../../ressources/squareWithSquares.med  )

    ADD_TEST(ExampleWaveSystem_2DVortex_Centered_SQUARE_squares ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/WaveSystemCentered.py  ${MESH_FILE})
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_SQUARE_squares PROPERTY ENVIRONMENT "LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${CMAKE_INSTALL_PREFIX}/lib/medcoupling:${CMAKE_INSTALL_PREFIX}/lib/med:${PETSC_DIR}/${PETSC_ARCH}/lib:${HDF5_ROOT_DIR}/lib:${PV_LIB_DIR}")
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_SQUARE_squares APPEND PROPERTY ENVIRONMENT "PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}:${CDMATH_BINARY_DIR}/postprocessing:${CMAKE_INSTALL_PREFIX}/${MEDCOUPLING_INSTALL_PYTHON}:${PV_PYTHON_DIR}:${CMAKE_INSTALL_PREFIX}/lib/cdmath:${CMAKE_INSTALL_PREFIX}/bin/cdmath")

    SET(MESH_FILE  ../../../ressources/meshCube.med  )

    ADD_TEST(ExampleWaveSystem_3DVortex_Centered_CUBE_tetrahedra ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/WaveSystemCentered.py  ${MESH_FILE})
    SET_PROPERTY(TEST ExampleWaveSystem_3DVortex_Centered_CUBE_tetrahedra PROPERTY ENVIRONMENT "LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${CMAKE_INSTALL_PREFIX}/lib/medcoupling:${CMAKE_INSTALL_PREFIX}/lib/med:${PETSC_DIR}/${PETSC_ARCH}/lib:${HDF5_ROOT_DIR}/lib:${PV_LIB_DIR}")
    SET_PROPERTY(TEST ExampleWaveSystem_3DVortex_Centered_CUBE_tetrahedra APPEND PROPERTY ENVIRONMENT "PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}:${CDMATH_BINARY_DIR}/postprocessing:${CMAKE_INSTALL_PREFIX}/${MEDCOUPLING_INSTALL_PYTHON}:${PV_PYTHON_DIR}:${CMAKE_INSTALL_PREFIX}/lib/cdmath:${CMAKE_INSTALL_PREFIX}/bin/cdmath")

    SET(MESH_FILE  ../../../ressources/cubeWithCubes.med  )

    ADD_TEST(ExampleWaveSystem_3DVortex_Centered_CUBE_cubes ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/WaveSystemCentered.py  ${MESH_FILE})
    SET_PROPERTY(TEST ExampleWaveSystem_3DVortex_Centered_CUBE_cubes PROPERTY ENVIRONMENT "LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${CMAKE_INSTALL_PREFIX}/lib/medcoupling:${CMAKE_INSTALL_PREFIX}/lib/med:${PETSC_DIR}/${PETSC_ARCH}/lib:${HDF5_ROOT_DIR}/lib:${PV_LIB_DIR}")
    SET_PROPERTY(TEST ExampleWaveSystem_3DVortex_Centered_CUBE_cubes APPEND PROPERTY ENVIRONMENT "PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}:${CDMATH_BINARY_DIR}/postprocessing:${CMAKE_INSTALL_PREFIX}/${MEDCOUPLING_INSTALL_PYTHON}:${PV_PYTHON_DIR}:${CMAKE_INSTALL_PREFIX}/lib/cdmath:${CMAKE_INSTALL_PREFIX}/bin/cdmath")

    SET(MESH_FILE  ../../../ressources/diskWithTriangles.med  )

    ADD_TEST(ExampleWaveSystem_2DVortex_Centered_DISK_triangles ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/WaveSystemCentered.py  ${MESH_FILE})
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_DISK_triangles PROPERTY ENVIRONMENT "LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${CMAKE_INSTALL_PREFIX}/lib/medcoupling:${CMAKE_INSTALL_PREFIX}/lib/med:${PETSC_DIR}/${PETSC_ARCH}/lib:${HDF5_ROOT_DIR}/lib:${PV_LIB_DIR}")
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_DISK_triangles APPEND PROPERTY ENVIRONMENT "PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}:${CDMATH_BINARY_DIR}/postprocessing:${CMAKE_INSTALL_PREFIX}/${MEDCOUPLING_INSTALL_PYTHON}:${PV_PYTHON_DIR}:${CMAKE_INSTALL_PREFIX}/lib/cdmath:${CMAKE_INSTALL_PREFIX}/bin/cdmath")

    SET(MESH_FILE  ../../../ressources/diskWithSquares.med  )

    ADD_TEST(ExampleWaveSystem_2DVortex_Centered_DISK_squares ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/WaveSystemCentered.py  ${MESH_FILE})
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_DISK_squares PROPERTY ENVIRONMENT "LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${CMAKE_INSTALL_PREFIX}/lib/medcoupling:${CMAKE_INSTALL_PREFIX}/lib/med:${PETSC_DIR}/${PETSC_ARCH}/lib:${HDF5_ROOT_DIR}/lib:${PV_LIB_DIR}")
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_DISK_squares APPEND PROPERTY ENVIRONMENT "PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}:${CDMATH_BINARY_DIR}/postprocessing:${CMAKE_INSTALL_PREFIX}/${MEDCOUPLING_INSTALL_PYTHON}:${PV_PYTHON_DIR}:${CMAKE_INSTALL_PREFIX}/lib/cdmath:${CMAKE_INSTALL_PREFIX}/bin/cdmath")

    SET(MESH_FILE  ../../../ressources/diskWithSpiderWeb.med  )

    ADD_TEST(ExampleWaveSystem_2DVortex_Centered_DISK_spiderWeb ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/WaveSystemCentered.py  ${MESH_FILE})
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_DISK_spiderWeb PROPERTY ENVIRONMENT "LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${CMAKE_INSTALL_PREFIX}/lib/medcoupling:${CMAKE_INSTALL_PREFIX}/lib/med:${PETSC_DIR}/${PETSC_ARCH}/lib:${HDF5_ROOT_DIR}/lib:${PV_LIB_DIR}")
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_DISK_spiderWeb APPEND PROPERTY ENVIRONMENT "PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}:${CDMATH_BINARY_DIR}/postprocessing:${CMAKE_INSTALL_PREFIX}/${MEDCOUPLING_INSTALL_PYTHON}:${PV_PYTHON_DIR}:${CMAKE_INSTALL_PREFIX}/lib/cdmath:${CMAKE_INSTALL_PREFIX}/bin/cdmath")

    SET(MESH_FILE  ../../../ressources/diskWithHexagons.med  )

    ADD_TEST(ExampleWaveSystem_2DVortex_Centered_DISK_hexagons ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/WaveSystemCentered.py  ${MESH_FILE})
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_DISK_hexagons PROPERTY ENVIRONMENT "LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:${CMAKE_INSTALL_PREFIX}/lib/medcoupling:${CMAKE_INSTALL_PREFIX}/lib/med:${PETSC_DIR}/${PETSC_ARCH}/lib:${HDF5_ROOT_DIR}/lib:${PV_LIB_DIR}")
    SET_PROPERTY(TEST ExampleWaveSystem_2DVortex_Centered_DISK_hexagons APPEND PROPERTY ENVIRONMENT "PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}:${CDMATH_BINARY_DIR}/postprocessing:${CMAKE_INSTALL_PREFIX}/${MEDCOUPLING_INSTALL_PYTHON}:${PV_PYTHON_DIR}:${CMAKE_INSTALL_PREFIX}/lib/cdmath:${CMAKE_INSTALL_PREFIX}/bin/cdmath")

endif (CDMATH_WITH_PYTHON AND CDMATH_WITH_PETSC AND CDMATH_WITH_POSTPRO)


