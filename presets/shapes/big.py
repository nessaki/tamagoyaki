### Copyright 2011, Magus Freston, Domino Marama, and Gaia Clary
### 
###
### This file is part of Tamagoyaki 1.
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
import tamagoyaki
from tamagoyaki import shape, util

arm    = util.get_armature(bpy.context.object)

dict={'head_size_682': 60.0, 'butt_size_795': 23.0, 'torso_length_38': 90.0, 'thickness_34': 57.0, 'neck_length_756': 70.0, 'breast_size_105': 74.0, 'breast_gravity_507': 42.0, 'leg_muscles_652': 49.0, 'breast_female_cleavage_684': 44.0, 'neck_thickness_683': 60.0, 'squash_stretch_head_647': 51.0, 'arm_length_693': 100.0, 'shoulders_36': 80.0, 'body_fat_637': 24.0, 'hip_width_37': 58.0, 'height_33': 47.0, 'love_handles_676': 23.0, 'hip_length_842': 33.0, 'leg_length_692': 67.0, 'belly_size_157': 33.0}
shape.resetToDefault(arm)
shape.fromDictionary(arm,dict)
