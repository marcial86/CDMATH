// Copyright (C) 2007-2015  CEA/DEN, EDF R&D, OPEN CASCADE
//
// Copyright (C) 2003-2007  OPEN CASCADE, EADS/CCR, LIP6, CEA/DEN,
// CEDRAT, EDF R&D, LEG, PRINCIPIA R&D, BUREAU VERITAS
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
//
// See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
//

//  File   : MED_version.h
//  Author : Vadim SANDLER
//  Module : SALOME
//
#if !defined(__MED_VERSION_H__)
#define __MED_VERSION_H__

/*!
  Specify version of SALOME MED module, as follows

  SALOMEMED_VERSION_MAJOR       : (integer) number identifying major version
  SALOMEMED_VERSION_MINOR       : (integer) number identifying minor version
  SALOMEMED_VERSION_MAINTENANCE : (integer) number identifying maintenance version
  SALOMEMED_VERSION_STR         : (string)  complete version number "major.minor.maintenance"
  SALOMEMED_VERSION             : (hex)     complete version number (major << 16) + (minor << 8) + maintenance
  SALOMEMED_DEVELOPMENT         : (integer) indicates development version when set to 1
*/

#define SALOMEMED_VERSION_MAJOR       7
#define SALOMEMED_VERSION_MINOR       7
#define SALOMEMED_VERSION_MAINTENANCE 1
#define SALOMEMED_VERSION_STR         "7.7.1"
#define SALOMEMED_VERSION             0x070701
#define SALOMEMED_DEVELOPMENT         0

#endif // __MED_VERSION_H__
