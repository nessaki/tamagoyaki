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

dict={'COG': 'hip', 'Tinker': '', 'Spine1': 'Spine1', 'Spine2': 'Spine2', 'Torso': 'mTorso', 'Spine3': 'Spine3', 'Spine4': 'Spine4', 'Chest': 'mChest', 'Neck': 'mNeck', 'Head': 'mHead', 'EyeRight': 'EyeRight', 'EyeLeft': 'EyeLeft', 'FaceRoot': 'mFaceRoot', 'FaceEyeAltRight': 'mFaceEyeAltRight', 'FaceEyeAltLeft': 'mFaceEyeAltLeft', 'FaceForeheadLeft': 'mFaceForeheadLeft', 'FaceForeheadRight': 'mFaceForeheadRight', 'FaceEyebrowOuterLeft': 'mFaceEyebrowOuterLeft', 'FaceEyebrowCenterLeft': 'mFaceEyebrowCenterLeft', 'FaceEyebrowInnerLeft': 'mFaceEyebrowInnerLeft', 'FaceEyebrowOuterRight': 'mFaceEyebrowOuterRight', 'FaceEyebrowCenterRight': 'mFaceEyebrowCenterRight', 'FaceEyebrowInnerRight': 'mFaceEyebrowInnerRight', 'FaceEyeLidUpperLeft': 'mFaceEyeLidUpperLeft', 'FaceEyeLidLowerLeft': 'mFaceEyeLidLowerLeft', 'FaceEyeLidUpperRight': 'mFaceEyeLidUpperRight', 'FaceEyeLidLowerRight': 'mFaceEyeLidLowerRight', 'FaceEar1Left': 'mFaceEar1Left', 'FaceEar2Left': 'mFaceEar2Left', 'FaceEar1Right': 'mFaceEar1Right', 'FaceEar2Right': 'mFaceEar2Right', 'FaceNoseLeft': 'mFaceNoseLeft', 'FaceNoseCenter': 'mFaceNoseCenter', 'FaceNoseRight': 'mFaceNoseRight', 'FaceCheekLowerLeft': 'mFaceCheekLowerLeft', 'FaceCheekUpperLeft': 'mFaceCheekUpperLeft', 'FaceCheekLowerRight': 'mFaceCheekLowerRight', 'FaceCheekUpperRight': 'mFaceCheekUpperRight', 'FaceJaw': 'mFaceJaw', 'FaceChin': 'mFaceChin', 'FaceTeethLower': 'mFaceTeethLower', 'FaceLipLowerLeft': 'mFaceLipLowerLeft', 'FaceLipLowerRight': 'mFaceLipLowerRight', 'FaceLipLowerCenter': 'mFaceLipLowerCenter', 'FaceTongueBase': 'mFaceTongueBase', 'FaceTongueTip': 'mFaceTongueTip', 'FaceJawShaper': 'mFaceJawShaper', 'FaceForeheadCenter': 'mFaceForeheadCenter', 'FaceNoseBase': 'mFaceNoseBase', 'FaceTeethUpper': 'mFaceTeethUpper', 'FaceLipUpperLeft': 'mFaceLipUpperLeft', 'FaceLipUpperRight': 'mFaceLipUpperRight', 'FaceLipCornerLeft': 'mFaceLipCornerLeft', 'FaceLipCornerRight': 'mFaceLipCornerRight', 'FaceLipUpperCenter': 'mFaceLipUpperCenter', 'FaceEyecornerInnerLeft': 'mFaceEyecornerInnerLeft', 'FaceEyecornerInnerRight': 'mFaceEyecornerInnerRight', 'FaceNoseBridge': 'mFaceNoseBridge', 'CollarLinkLeft': '', 'CollarLeft': 'mCollarLeft', 'ShoulderLeft': 'mShoulderLeft', 'ElbowLeft': 'mElbowLeft', 'WristLeft': 'mWristLeft', 'HandMiddle1Left': 'mHandMiddle1Left', 'HandMiddle2Left': 'mHandMiddle2Left', 'HandMiddle3Left': 'mHandMiddle3Left', 'HandIndex1Left': 'mHandIndex1Left', 'HandIndex2Left': 'mHandIndex2Left', 'HandIndex3Left': 'mHandIndex3Left', 'HandRing1Left': 'mHandRing1Left', 'HandRing2Left': 'mHandRing2Left', 'HandRing3Left': 'mHandRing3Left', 'HandPinky1Left': 'mHandPinky1Left', 'HandPinky2Left': 'mHandPinky2Left', 'HandPinky3Left': 'mHandPinky3Left', 'HandThumb1Left': 'mHandThumb1Left', 'HandThumb2Left': 'mHandThumb2Left', 'HandThumb3Left': 'mHandThumb3Left', 'CollarLinkRight': '', 'CollarRight': 'mCollarRight', 'ShoulderRight': 'mShoulderRight', 'ElbowRight': 'mElbowRight', 'WristRight': 'mWristRight', 'HandMiddle1Right': 'mHandMiddle1Right', 'HandMiddle2Right': 'mHandMiddle2Right', 'HandMiddle3Right': 'mHandMiddle3Right', 'HandIndex1Right': 'mHandIndex1Right', 'HandIndex2Right': 'mHandIndex2Right', 'HandIndex3Right': 'mHandIndex3Right', 'HandRing1Right': 'mHandRing1Right', 'HandRing2Right': 'mHandRing2Right', 'HandRing3Right': 'mHandRing3Right', 'HandPinky1Right': 'mHandPinky1Right', 'HandPinky2Right': 'mHandPinky2Right', 'HandPinky3Right': 'mHandPinky3Right', 'HandThumb1Right': 'mHandThumb1Right', 'HandThumb2Right': 'mHandThumb2Right', 'HandThumb3Right': 'mHandThumb3Right', 'WingsRoot': 'mWingsRoot', 'Wing1Left': 'mWing1Left', 'Wing2Left': 'mWing2Left', 'Wing3Left': 'mWing3Left', 'Wing4Left': 'mWing4Left', 'Wing4FanLeft': 'mWing4FanLeft', 'Wing1Right': 'mWing1Right', 'Wing2Right': 'mWing2Right', 'Wing3Right': 'mWing3Right', 'Wing4Right': 'mWing4Right', 'Wing4FanRight': 'mWing4FanRight', 'HipLinkLeft': '', 'HipLeft': 'mHipLeft', 'KneeLeft': 'mKneeLeft', 'AnkleLeft': 'mAnkleLeft', 'FootLeft': 'mFootLeft', 'ToeLeft': 'mToeLeft', 'HipLinkRight': '', 'HipRight': 'mHipRight', 'KneeRight': 'mKneeRight', 'AnkleRight': 'mAnkleRight', 'FootRight': 'mFootRight', 'ToeRight': 'mToeRight', 'Tail1': 'mTail1', 'Tail2': 'mTail2', 'Tail3': 'mTail3', 'Tail4': 'mTail4', 'Tail5': 'mTail5', 'Tail6': 'mTail6', 'Groin': 'mGroin', 'HindLimbsRoot': 'mHindLimbsRoot', 'HindLimb1Left': 'mHindLimb1Left', 'HindLimb2Left': 'mHindLimb2Left', 'HindLimb3Left': 'mHindLimb3Left', 'HindLimb4Left': 'mHindLimb4Left', 'HindLimb1Right': 'mHindLimb1Right', 'HindLimb2Right': 'mHindLimb2Right', 'HindLimb3Right': 'mHindLimb3Right', 'HindLimb4Right': 'mHindLimb4Right', 'Skull': 'mSkull'}
#data.clear_mtui_bones(context, arm_obj)
data.fill_mtui_bones(context, dict, arm_obj)
