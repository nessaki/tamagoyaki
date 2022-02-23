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
# import bpy
import tamagoyaki
from tamagoyaki import data, util

context = bpy.context
arm_obj = data.get_retarget_target(context)

dict={'COG': 'hip', 'Tinker': '', 'Spine1': '', 'Spine2': '', 'Torso': 'abdomen', 'Spine3': '', 'Spine4': '', 'Chest': 'chest', 'Neck': 'neck', 'Head': 'head', 'EyeRight': '', 'EyeLeft': '', 'FaceRoot': '', 'FaceEyeAltRight': '', 'FaceEyeAltLeft': '', 'FaceForeheadLeft': '', 'FaceForeheadRight': '', 'FaceEyebrowOuterLeft': '', 'FaceEyebrowCenterLeft': '', 'FaceEyebrowInnerLeft': '', 'FaceEyebrowOuterRight': '', 'FaceEyebrowCenterRight': '', 'FaceEyebrowInnerRight': '', 'FaceEyeLidUpperLeft': '', 'FaceEyeLidLowerLeft': '', 'FaceEyeLidUpperRight': '', 'FaceEyeLidLowerRight': '', 'FaceEar1Left': '', 'FaceEar2Left': '', 'FaceEar1Right': '', 'FaceEar2Right': '', 'FaceNoseLeft': '', 'FaceNoseCenter': '', 'FaceNoseRight': '', 'FaceCheekLowerLeft': '', 'FaceCheekUpperLeft': '', 'FaceCheekLowerRight': '', 'FaceCheekUpperRight': '', 'FaceJaw': '', 'FaceChin': '', 'FaceTeethLower': '', 'FaceLipLowerLeft': '', 'FaceLipLowerRight': '', 'FaceLipLowerCenter': '', 'FaceTongueBase': '', 'FaceTongueTip': '', 'FaceJawShaper': '', 'FaceForeheadCenter': '', 'FaceNoseBase': '', 'FaceTeethUpper': '', 'FaceLipUpperLeft': '', 'FaceLipUpperRight': '', 'FaceLipCornerLeft': '', 'FaceLipCornerRight': '', 'FaceLipUpperCenter': '', 'FaceEyecornerInnerLeft': '', 'FaceEyecornerInnerRight': '', 'FaceNoseBridge': '', 'CollarLinkLeft': '', 'CollarLeft': 'lCollar', 'ShoulderLeft': 'lShldr', 'ElbowLeft': 'lForeArm', 'WristLeft': 'lHand', 'HandMiddle1Left': '', 'HandMiddle2Left': '', 'HandMiddle3Left': '', 'HandIndex1Left': '', 'HandIndex2Left': '', 'HandIndex3Left': '', 'HandRing1Left': '', 'HandRing2Left': '', 'HandRing3Left': '', 'HandPinky1Left': '', 'HandPinky2Left': '', 'HandPinky3Left': '', 'HandThumb1Left': '', 'HandThumb2Left': '', 'HandThumb3Left': '', 'CollarLinkRight': '', 'CollarRight': 'rCollar', 'ShoulderRight': 'rShldr', 'ElbowRight': 'rForeArm', 'WristRight': 'rHand', 'HandMiddle1Right': '', 'HandMiddle2Right': '', 'HandMiddle3Right': '', 'HandIndex1Right': '', 'HandIndex2Right': '', 'HandIndex3Right': '', 'HandRing1Right': '', 'HandRing2Right': '', 'HandRing3Right': '', 'HandPinky1Right': '', 'HandPinky2Right': '', 'HandPinky3Right': '', 'HandThumb1Right': '', 'HandThumb2Right': '', 'HandThumb3Right': '', 'WingsRoot': '', 'Wing1Left': '', 'Wing2Left': '', 'Wing3Left': '', 'Wing4Left': '', 'Wing4FanLeft': '', 'Wing1Right': '', 'Wing2Right': '', 'Wing3Right': '', 'Wing4Right': '', 'Wing4FanRight': '', 'HipLinkLeft': '', 'HipLeft': 'lThigh', 'KneeLeft': 'lShin', 'AnkleLeft': 'lFoot', 'FootLeft': '', 'ToeLeft': '', 'HipLinkRight': '', 'HipRight': 'rThigh', 'KneeRight': 'rShin', 'AnkleRight': 'rFoot', 'FootRight': '', 'ToeRight': '', 'Tail1': '', 'Tail2': '', 'Tail3': '', 'Tail4': '', 'Tail5': '', 'Tail6': '', 'Groin': '', 'HindLimbsRoot': '', 'HindLimb1Left': '', 'HindLimb2Left': '', 'HindLimb3Left': '', 'HindLimb4Left': '', 'HindLimb1Right': '', 'HindLimb2Right': '', 'HindLimb3Right': '', 'HindLimb4Right': '', 'Skull': 'figureHair'}
#data.clear_mtui_bones(context, arm_obj)
data.fill_mtui_bones(context, dict, arm_obj)
