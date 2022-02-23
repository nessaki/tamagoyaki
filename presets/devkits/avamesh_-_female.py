### Copyright 2011, Magus Freston, Domino Marama, and Gaia Clary
### Modifications 2022, Nessaki Kinskey
###
### This file is part of Tamagoyaki.
### This file contains code from Machinematrix (Avastar 1) 
###

### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
kitprop = bpy.context.scene.UpdateRigProp

kitprop.devkit_filepath=r'TAMAGOYAKI\lib\avamesh-basic.blend'
kitprop.devkit_brand=r'Avamesh'
kitprop.devkit_snail=r'Female'
kitprop.srcRigType='AVASTAR'
kitprop.tgtRigType='EXTENDED'
kitprop.JointType='PIVOT'
kitprop.tgtgJointType='PIVOT'
kitprop.devkit_use_sl_head=False
kitprop.use_male_shape=False
kitprop.use_male_skeleton=False
kitprop.transferJoints=False
kitprop.devkit_use_bind_pose=False
kitprop.sl_bone_ends=False
kitprop.sl_bone_rolls=False
kitprop.fix_reference_meshes=False
