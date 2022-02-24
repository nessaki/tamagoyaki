import bpy
import tamagoyaki
from tamagoyaki import shape, util

context = bpy.context
scene = context.scene
armobj = context.object
updateRigProp = scene.UpdateRigProp
sceneProps  = scene.SceneProp

armobj.data.pose_position = 'REST'
updateRigProp.srcRigType = 'MANUELLAB'
updateRigProp.tgtRigType = 'EXTENDED'
updateRigProp.handleTargetMeshSelection = 'DELETE'
updateRigProp.transferJoints = True
updateRigProp.JointType = 'PIVOT'
updateRigProp.SkeletonType = 'TAMAGOYAKI'
updateRigProp.rig_use_bind_pose = True
updateRigProp.sl_bone_ends = True
updateRigProp.sl_bone_rolls = True
updateRigProp.show_offsets = False
updateRigProp.attachSliders = True
updateRigProp.applyRotation = True
updateRigProp.use_male_shape = False
updateRigProp.use_male_skeleton = False
updateRigProp.apply_pose = False
