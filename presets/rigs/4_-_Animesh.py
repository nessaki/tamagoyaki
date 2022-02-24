import bpy
import tamagoyaki
from tamagoyaki import shape, util

sceneProps  = bpy.context.scene.SceneProp
sceneProps.tamagoyakiMeshType   = 'NONE'
sceneProps.tamagoyakiRigType    = 'EXTENDED'
sceneProps.tamagoyakiJointType  = 'PIVOT'
sceneProps.tamagoyakiSkeletonType  = 'ANIMESH'
