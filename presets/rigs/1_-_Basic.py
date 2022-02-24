import bpy
import tamagoyaki
from tamagoyaki import shape, util

sceneProps  = bpy.context.scene.SceneProp
sceneProps.tamagoyakiMeshType   = 'QUADS'
sceneProps.tamagoyakiRigType    = 'BASIC'
sceneProps.tamagoyakiJointType  = 'PIVOT'
sceneProps.tamagoyakiSkeletonType = 'TAMAGOYAKI'
