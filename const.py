### Copyright 2015, Gaia Clary
### Modifications 2015 Gaia Clary
### Modification  2015 Matrice Laville
### Modifications 2022 Nessaki
### Contains code from Machinimatrix
###
### This file is part of Tamagoyaki
###
### The module has been created based on this document:
### A Beginners Guide to Dual-Quaternions:
### http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.407.9047
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

import os
import re
import bpy
import logging
import bpy.utils.previews

from .messages import *
from math import *
from . import bl_info
from mathutils import Vector, Matrix
from collections import OrderedDict
from bpy.props import *

log=logging.getLogger("tamagoyaki.const")
registerlog = logging.getLogger("tamagoyaki.register")

MIN_VERSION = 63
SVN = None
def get_blender_revision():
    global SVN

    try:
        test = bpy.app.build_hash # check if we are in git
        n = bpy.app.version[0] * 100000 +\
            bpy.app.version[1] * 1000   +\
            bpy.app.version[2] * 100
    except:
        try:
            n = bpy.app.build_revision.decode().split(':')[-1].rstrip('M')
        except:
            n = bpy.app.build_revision.split(':')[-1].rstrip('M')
        try:
            n = int(n)
        except:

            v = bpy.app.version[1]
            logging.critical("The Build revision of your system seems broken: [%s]" % (str(bpy.app.build_revision)))
            logging.critical("We now get your Blender Version number %d from: [%s]" % (v, str(bpy.app.version)))
            if v < MIN_VERSION:
                n = 0
            else:
                if v > 67: v = 67
                n = {'63':45996,
                     '64':51026,
                     '65':52851,
                     '66':55078,
                     '67':56533}[str(v)]
    SVN = n
    return SVN




INDEX_COLLECTION_OBJECT=0
INDEX_COLLECTION_HIDE=1

TAMAGOYAKI_CUSTOM_SHAPES = 'tamagoyaki_custom_shapes'




MAX_PRIORITY = 6
MIN_PRIORITY = -1
NULL_BONE_PRIORITY = -2


LL_MAX_PELVIS_OFFSET = 5.0





CONTROL_BONE_RIG = 'CONTROL_BONE_RIG'
DEFORM_BONE_RIG  = 'DEFORM_BONE_RIG'





GP_NAME = 'tamagoyaki_grease_pencil'





UI_LOCATION = 'UI'

ICON_ADD = 'ADD'
ICON_ALIGN = 'CENTER_ONLY'
ICON_ARMATURE_DATA = 'ARMATURE_DATA'
ICON_ARROW_LEFTRIGHT = 'ARROW_LEFTRIGHT'
ICON_AUTO = 'AUTO'
ICON_BACK = 'BACK'
ICON_BLANK1 = 'BLANK1'
ICON_BOIDS = 'BOIDS'
ICON_BONE_DATA = 'BONE_DATA'
ICON_BRUSH_DATA = 'BRUSH_DATA'
ICON_CANCEL = 'CANCEL'
ICON_CHECKBOX_DEHLT = 'CHECKBOX_DEHLT'
ICON_CHECKBOX_HLT = 'CHECKBOX_HLT'
ICON_CHECKMARK = 'CHECKMARK'
ICON_CONSTRAINT_BONE = 'CONSTRAINT_BONE'
ICON_COPYDOWN = 'COPYDOWN'
ICON_DECORATE_OVERRIDE = 'DECORATE_OVERRIDE'
ICON_DISCLOSURE_TRI_DOWN = 'DISCLOSURE_TRI_DOWN'
ICON_DISCLOSURE_TRI_RIGHT = 'DISCLOSURE_TRI_RIGHT'
ICON_EDIT = 'EDIT'
ICON_ERROR = 'ERROR'
ICON_EXPORT = 'EXPORT'
ICON_EYEDROPPER = 'EYEDROPPER'
ICON_FILE = 'FILE'
ICON_FILE_BLANK = 'FILE_BLANK'
ICON_FILE_NEW = 'FILE_NEW'
ICON_FILE_REFRESH = 'FILE_REFRESH'
ICON_FILE_TICK = 'FILE_TICK'
ICON_FILTER = 'FILTER'
ICON_FORCE_CURVE = 'FORCE_CURVE'
ICON_FORWARD = 'FORWARD'
ICON_FREEZE = 'FREEZE'
ICON_FUND = 'FUND'
ICON_GRAPH = 'GRAPH'
ICON_GROUP_BONE = 'GROUP_BONE'
ICON_GROUP_UVS = 'GROUP_UVS'
ICON_GROUP_VERTEX = 'GROUP_VERTEX'
ICON_HAND = 'HAND'
ICON_HIDE_OFF = 'HIDE_OFF'
ICON_HIDE_ON = 'HIDE_ON'
ICON_IMAGE = 'IMAGE'
ICON_IMAGE_DATA = 'IMAGE_DATA'
ICON_IMPORT = 'IMPORT'
ICON_INFO = 'INFO'
ICON_IPO_LINEAR = 'IPO_LINEAR'
ICON_KEY_HLT = 'KEY_HLT'
ICON_KEYTYPE_BREAKDOWN_VEC = 'KEYTYPE_BREAKDOWN_VEC'
ICON_KEYTYPE_JITTER_VEC = 'KEYTYPE_JITTER_VEC'
ICON_LAYER_ACTIVE = 'LAYER_ACTIVE'
ICON_LAYER_USED = 'LAYER_USED'
ICON_LEFT_HANDLE ='LEFT_HANDLE'
ICON_LIBRARY_DATA_DIRECT = 'LIBRARY_DATA_DIRECT'
ICON_LIGHT = 'LIGHT'
ICON_LIGHT_AREA = 'LIGHT_AREA'
ICON_LIGHT_DATA = 'LIGHT_DATA'
ICON_LIGHT_HEMI = 'LIGHT_HEMI'
ICON_LIGHT_POINT = 'LIGHT_POINT'
ICON_LIGHT_SPOT = 'LIGHT_SPOT'
ICON_LIGHT_SUN = 'LIGHT_SUN'
ICON_LINKED = 'LINKED'
ICON_LOAD_FACTORY  = ICON_KEYTYPE_JITTER_VEC
ICON_LOCKED = 'LOCKED'
ICON_LOOP_FORWARDS = 'LOOP_FORWARDS'
ICON_MAN_SCALE = 'MAN_SCALE'
ICON_MESH_DATA = 'MESH_DATA'
ICON_MODIFIER = 'MODIFIER'
ICON_MOD_ARMATURE = 'MOD_ARMATURE'
ICON_MOD_MIRROR = 'MOD_MIRROR'
ICON_MOD_SMOOTH = 'MOD_SMOOTH'
ICON_MOD_VERTEX_WEIGHT = "MOD_VERTEX_WEIGHT"
ICON_MEMORY = "MEMORY"
ICON_MONKEY = 'MONKEY'
ICON_NONE = 'NONE'
ICON_OBJECT_DATA = 'OBJECT_DATA'
ICON_OBJECT_DATAMODE = 'OBJECT_DATAMODE'
ICON_OUTLINER = 'OUTLINER'
ICON_OUTLINER_DATA_ARMATURE = 'OUTLINER_DATA_ARMATURE'
ICON_OUTLINER_DATA_LIGHT = 'OUTLINER_DATA_LIGHT'
ICON_OUTLINER_OB_ARMATURE = 'OUTLINER_OB_ARMATURE'
ICON_OUTLINER_OB_LIGHT = 'OUTLINER_OB_LIGHT'
ICON_PASTEDOWN = 'PASTEDOWN'
ICON_POSE_HLT = 'POSE_HLT'
ICON_PIVOT_ACTIVE = 'PIVOT_ACTIVE'
ICON_PIVOT_CURSOR = 'PIVOT_CURSOR'
ICON_PIVOT_INDIVIDUAL = 'PIVOT_INDIVIDUAL'
ICON_PIVOT_MEDIAN = 'PIVOT_MEDIAN'
ICON_POSE_DATA = ICON_OUTLINER_OB_ARMATURE
ICON_PREFERENCES = 'PREFERENCES'
ICON_PROPERTIES = 'PROPERTIES'
ICON_QUESTION = 'QUESTION'
ICON_RADIO = 'RADIO'
ICON_RADIOBUT_ON = 'RADIOBUT_ON'
ICON_RADIOBUT_OFF = 'RADIOBUT_OFF'
ICON_RECOVER_AUTO = ICON_DECORATE_OVERRIDE
ICON_REMOVE = 'REMOVE'
ICON_RENDER_ANIMATION = 'RENDER_ANIMATION'
ICON_RESTRICT_SELECT_ON = 'RESTRICT_SELECT_ON'
ICON_RESTRICT_SELECT_OFF = 'RESTRICT_SELECT_OFF'
ICON_RENDER_ANIMATION = 'RENDER_ANIMATION'
ICON_SCRIPT = 'SCRIPT'
ICON_SHADING_BBOX = 'SHADING_BBOX'
ICON_SHADING_RENDERED = 'SHADING_RENDERED'
ICON_SHADING_SOLID = 'SHADING_SOLID'
ICON_SHADING_TEXTURE = 'SHADING_TEXTURE'
ICON_SHADING_WIRE = 'SHADING_WIRE'
ICON_SHAPEKEY_DATA = 'SHAPEKEY_DATA'
ICON_SNAP_ON = 'SNAP_ON'
ICON_SOLO_ON = 'SOLO_ON'
ICON_TEXT = 'TEXT'
ICON_TEXTURE = 'TEXTURE'
ICON_TOOL_SETTINGS = 'TOOL_SETTINGS'
ICON_UI = ICON_KEYTYPE_JITTER_VEC
ICON_UNLOCKED = 'UNLOCKED'
ICON_URL = 'URL'
ICON_VISIBLE_IPO_ON = 'VISIBLE_IPO_ON'
ICON_WINDOW = 'WINDOW'
ICON_WPAINT_HLT = 'WPAINT_HLT'
ICON_X = 'X'
ICON_XRAY = 'XRAY'
ICON_ZOOM_IN = 'ZOOM_IN'
ICON_ZOOM_OUT = 'ZOOM_OUT'





NEUTRAL_SHAPE = 'neutral_shape'
REFERENCE_SHAPE = 'reference_shape'
MORPH_SHAPE = 'bone_morph'

SHAPE_TRANSFORMS = 'transforms'
SHAPE_SLIDERS = 'sliders'
SHAPE_VALUES = 'values'
SHAPE_HOVER = 'hover'
SHAPE_BINDING = 'binding'
DIRTY_MESH = 'dirty_mesh'
DIRTY_RIG = 'dirty_rig'
DIRTY_SHAPE = 'dirty_shape'
MESH_STATS = 'stats'

STATS_DEFORMING_BONES = 'deforming_bones'
STATS_DISCARDED_BONES = 'discarded_bones'
STATS_BONE_COUNT = 'bone_count'
STATS_VERTEX_COUNT = 'vertex_count'
STATS_FACE_COUNT = 'face_count'
STATS_LOOP_COUNT = 'loop_count'
STATS_TRI_COUNT = 'tri_count'
STATS_TRI_COUNT_MAX = 'tri_count_max'
STATS_UV_COUNT = 'uv_count'
STATS_UV_LAYER_COUNT = 'uv_layer_count'
STATS_NORMAL_COUNT = 'normal_count'
STATS_MAT_COUNT = 'mat_count'
STATS_EXTENDED_MAT_COUNT = 'extended_mat_count'
STATS_RADIUS = 'radius'
STATS_VC_LOWEST = 'vc_lowest'
STATS_VC_LOW = 'vc_low'
STATS_VC_MID = 'vc_mid'
STATS_VC_HIGH = 'vc_high'
STATS_NWC_EFFECTIVE = 'nwc_effective'
STATS_NWC_DISCARDED = 'nwc_discarded'
STATS_UNASSIGNED_POLYS = 'unassigned_polys'
STATS_UNASSIGNED_SLOTS = 'unassigned_slots'
STATS_UNASSIGNED_MATS = 'unassigned_mats'


JOINT_BASE_HEAD_ID = 'relhead'
JOINT_BASE_TAIL_ID = 'reltail'
JOINT_BASE_OFFSET_ID = 'offset'

JOINT_OFFSET_HEAD_ID = 'orelhead'
JOINT_OFFSET_TAIL_ID = 'oreltail'
JOINT_O_HEAD_ID = 'ohead'
JOINT_O_TAIL_ID = 'otail'

TAMAGOYAKI_RIG_ID = 8
BASIC_RIG = 'BASIC'
EXTENDED_RIG = 'EXTENDED'
REFERENCE_RIG = 'REFERENCE'

BENTOBOX        = "https://github.com/nessaki/tamagoyaki"
DOCUMENTATION        = "https://github.com/nessaki/tamagoyaki/wiki"
TICKETS              = "https://github.com/nessaki/tamagoyaki/issues"
TOOL_PARAMETER       = "addon=tamagoyaki-%s.%s.%s" % bl_info['version']

TAMAGOYAKI_COLLADA        = DOCUMENTATION + "/help/io/collada-tamagoyaki/"
TAMAGOYAKI_EXPORT_TROUBLE = DOCUMENTATION + "/reference/troubleshooting/export/"

TAMAGOYAKI_WORKFLOW     = DOCUMENTATION + "/help/n-panel/tamagoyaki/workflows/"
TAMAGOYAKI_APPEARANCE   = DOCUMENTATION + "/help/n-panel/tamagoyaki/shape-editor/"
TAMAGOYAKI_RIG_DISPLAY  = DOCUMENTATION + "/help/n-panel/tamagoyaki/rig-display/"
TAMAGOYAKI_RIG_CONFIG   = DOCUMENTATION + "/help/n-panel/tamagoyaki/rig-config/"
TAMAGOYAKI_RIG_CONVERTER= DOCUMENTATION + "/help/n-panel/tamagoyaki/rig-inspector/rig-update-tool/update/"
TAMAGOYAKI_DEVKIT_MANAGER=DOCUMENTATION + "/help/n-panel/tamagoyaki/devkit_manager/"
TAMAGOYAKI_SKINNING     = DOCUMENTATION + "/help/n-panel/tamagoyaki/skinning/"
TAMAGOYAKI_MATERIALS    = DOCUMENTATION + "/help/n-panel/tamagoyaki/material-presets/"
TAMAGOYAKI_WEIGHT_COPY  = DOCUMENTATION + "/help/n-panel/tamagoyaki/weight-copy/"
TAMAGOYAKI_FITTING      = DOCUMENTATION + "/help/n-panel/tamagoyaki/the-fitting-panel/"
TAMAGOYAKI_POSING       = DOCUMENTATION + "/help/n-panel/tamagoyaki/posing/"
TAMAGOYAKI_TOOLS        = DOCUMENTATION + "/help/n-panel/tamagoyaki/tool-box/"
TAMAGOYAKI_MESH_INFO    = DOCUMENTATION + "/help/n-panel/tamagoyaki/mesh-inspector/"
TAMAGOYAKI_MAINTENANCE  = DOCUMENTATION + "/help/n-panel/tamagoyaki/maintenance/"
TAMAGOYAKI_JOINTS       = DOCUMENTATION + "/help/properties/data/"
RELEASE_INFO         = DOCUMENTATION + "/reference/release-changelog/"
REFERENCE_GUIDES     = DOCUMENTATION + "/help/"

TAMAGOYAKI_RIG_IMPORT   = DOCUMENTATION + "/help/rig-transfer-tool/"
TAMAGOYAKI_SHAPE_IO     = DOCUMENTATION + "/help/properties/object/shape/io/"
HELP_PAGE            = BENTOBOX+ "/help/"
TAMAGOYAKI_URL          = BENTOBOX+ "/tamagoyaki"
TAMAGOYAKI_REGISTER     = BENTOBOX+ "/register-download-page/"
TAMAGOYAKI_DOWNLOAD     = BENTOBOX+ "/my-account/products/"
XMLRPC_SERVICE       = BENTOBOX+ "/xmlrpc.php"
FIRST_STEPS          = DOCUMENTATION + "/reference/usermanual/first-steps/"

CHECKSUM = "ava_checksum"
WORKSPACE_SL_ANIMATION='SL Animation'

MANUAL_MAPPING = None

OPERATOR_MAPPING_FILE = "operator_mapping.txt"
URL_MAPPING_FILE = "url_mapping.txt"
UPDATED_URL_MAPPING_FILE = "updated_url_mapping.txt"


def init_url_manual_map(MANUAL_MAPPING):

    def file_has_lines(documap):
        with open(documap) as f:
            for line in f:
                return True
        return False

    documap = os.path.join(DATAFILESDIR, UPDATED_URL_MAPPING_FILE)
    if not (os.path.exists(documap) and file_has_lines(documap)):
        documap = os.path.join(DATAFILESDIR, URL_MAPPING_FILE)

    with open(documap) as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue

            array = line.split(',')
            if len(array) != 2:
                log.warn("URL_MAPPING failed to read line [%s]" % line)
                continue
            key = array[0].strip()
            link = "%s/?%s" % (array[1].strip(), TOOL_PARAMETER)
            val = MANUAL_MAPPING.get(key)
            if val:
                val[1]=link
            else:
                val = [None, link]
            MANUAL_MAPPING[key] = val


def init_operator_manual_map(MANUAL_MAPPING):
        map = os.path.join(DATAFILESDIR, OPERATOR_MAPPING_FILE)
        with open(map) as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or not line:
                    continue

                array = line.split(',')
                if len(array) != 2:
                    log.warn("OPERATOR_MAPPING failed to read line [%s]" % line)
                    continue
                key = array[0].strip()
                operator_regex = array[1].strip()

                val = MANUAL_MAPPING.get(key)
                if val:
                    val[0] = operator_regex
                else:
                    val = [operator_regex, None]
                
                MANUAL_MAPPING[key] = val


def get_manual_map(force_reload=False):

    global MANUAL_MAPPING
    if force_reload or MANUAL_MAPPING == None:
        MANUAL_MAPPING = {}
        init_url_manual_map(MANUAL_MAPPING)
        init_operator_manual_map(MANUAL_MAPPING)
    return MANUAL_MAPPING


def get_help_page(section):
    map = get_manual_map()
    entry = map.get(section)
    link = entry[1] if entry else 'help/toolshelf'
    return DOCUMENTATION+link

def has_module(module_name):
    return module_name in bpy.context.preferences.addons

TAMAGOYAKI_DIR    = os.path.dirname(os.path.abspath(__file__))
LOCALE_DIR     = os.path.join(os.path.dirname(__file__), 'locale')
TMP_DIR        = os.path.join(os.path.dirname(__file__), 'tmp')
TEMPLATE_DIR   = os.path.join(os.path.dirname(__file__), 'apptemplates')
LIB_DIR        = os.path.join(os.path.dirname(__file__), 'lib')
CONFIG_DIR     = os.path.join(os.path.dirname(__file__), 'config')
ICONS_DIR      = os.path.join(os.path.dirname(__file__), 'icons')

USER_PRESETS   = os.path.join(bpy.utils.user_resource('SCRIPTS'), 'presets/tamagoyaki')
RIG_PRESET_DIR = os.path.join(USER_PRESETS, "rigs")
DATAFILESDIR   = os.path.join(os.path.dirname(os.path.abspath(__file__)),'lib')
ASSETS         = os.path.join(DATAFILESDIR,'assets.blend')
STARTUP_BLEND  = os.path.join(LIB_DIR, 'startup.blend')
SHAPEBOARD     = os.path.join(TMP_DIR,'shapeboard.xml')

HAND_POSTURE_DEFAULT = '-1'


SEVERITY_ERROR          = "ERROR"
SEVERITY_MESH_ERROR     = "ERROR"
SEVERITY_ARMATURE_ERROR = "ERROR"
SEVERITY_EXPORT_ERROR   = "ERROR"
SEVERITY_WARNING        = "WARNING"
SEVERITY_INFO           = "INFO"
SEVERITY_HINT           = "HINT"
SEVERITY_STRONG_WARNING = "STRONG_WARNING"

COPY_ROTATION    = 'COPY_ROTATION'
COPY_LOCATION    = 'COPY_LOCATION'


BLtoBVH = Matrix.Rotation(-pi/2, 4, 'X')
YUPtoZUP = Matrix.Rotation(pi/2, 4, 'X')

INCHES_TO_METERS   = 0.02540005
DEGREES_TO_RADIANS = pi/180.0
RADIAN_TO_DEGREE   = 180/pi

Rz90 = Matrix((
       (0.0, 1.0, 0.0, 0.0),
       (-1.0, 0.0, 0.0, 0.0),
       (0.0, 0.0, 1.0, 0.0),
       (0.0, 0.0, 0.0, 1.0)
       ))
Rz90I = Rz90.inverted()

Ry90 = Matrix((
       ( 0.0, 0.0, 1.0, 0.0),
       ( 0.0, 1.0, 0.0, 0.0),
       (-1.0, 0.0, 0.0, 0.0),
       ( 0.0, 0.0, 0.0, 1.0)))
Ry90I = Ry90.inverted()

Rx90 = Matrix((
       (1.0, 0.0, 0.0, 0.0),
       (0.0, 0.0, 1.0, 0.0),
       (0.0, -1.0, 0.0, 0.0),
       (0.0, 0.0, 0.0, 1.0)
       ))
Rx90I = Rx90.inverted()

V0 = Vector((0,0,0))
V1 = Vector((1,1,1))

M0 = Matrix((
    (0,0,0,0),
    (0,0,0,0),
    (0,0,0,0),
    (0,0,0,0)))

OB_TRANSLATED = 1
OB_SCALED     = 2
OB_ROTATED    = 4
OB_NEGSCALED  = 8

VERY_CLOSE = 0.000001
CLOSE = 0.00001
MIN_BONE_LENGTH          = 0.0001
MIN_JOINT_OFFSET         = 0.0001
MIN_JOINT_OFFSET_RELAXED = 0.0001
MIN_JOINT_OFFSET_STRICT  = VERY_CLOSE

LArmBones = set(['ShoulderLeft','ElbowLeft','WristLeft','ikWristLeft','ikElbowTargetLeft'])
RArmBones = set(['ShoulderRight','ElbowRight','WristRight','ikWristRight','ikElbowTargetRight'])
LLegBones = set(['HipLeft','KneeLeft','AnkleLeft','ikHeelLeft','ikFootPivotLeft','ikKneeTargetLeft'])
RLegBones = set(['HipRight','KneeRight','AnkleRight','ikHeelRight','ikFootPivotRight','ikKneeTargetRight'])
LHindBones = set(['HindLimb1Left','HindLimb2Left','HindLimb3Left','ikHindHeelLeft','ikHindFootPivotLeft','ikHindLimb2TargetLeft'])
RHindBones = set(['HindLimb1Right','HindLimb2Right','HindLimb3Right','ikHindHeelRight','ikHindFootPivotRight','ikHindLimb2TargetRight'])
LFaceBones = set(['FaceCheekLowerLeft', 'FaceCheekUpperLeft', 'FaceLipCornerLeft', 'FaceLipUpperLeft', 'FaceLipLowerLeft', 'FaceNoseLeft', 'FaceEyebrowInnerLeft', 'FaceEyebrowCenterLeft', 'FaceEyebrowOuterLeft'])
RFaceBones = set(['FaceCheekLowerRight', 'FaceCheekUpperRight', 'FaceLipCornerRight', 'FaceLipUpperRight', 'FaceLipLowerRight', 'FaceNoseRight', 'FaceEyebrowInnerRight','FacEyebrowCenterRight', 'FaceEyebrowOuterRight'])
FaceBones = LFaceBones|RFaceBones|set(['FaceNoseCenter', 'FaceLipUpperCenter', 'FaceLipLowerCenter', 'FaceTeethLower', 'FaceJaw'])


def get_limb_from_ikbone(ikbone):
    if ikbone in LArmBones:
        return LArmBones
    if ikbone in RArmBones:
        return RArmBones
    if ikbone in LLegBones:
        return LLegBones
    if ikbone in RLegBones:
        return RLegBones
    if ikbone in LHindBones:
        return LHindBones
    if ikbone in RHindBones:
        return RHindBones
    return None

SLARMBONES = LArmBones.union(RArmBones)
SLLEGBONES = LLegBones.union(RLegBones)
LPinchBones= set(['ikIndexPinchLeft'])
RPinchBones= set(['ikIndexPinchRight'])
LGrabBones = set(['ikThumbTargetLeft', 'ikIndexTargetLeft', 'ikMiddleTargetLeft', 'ikRingTargetLeft', 'ikPinkyTargetLeft'])
RGrabBones = set(['ikThumbTargetRight', 'ikIndexTargetRight', 'ikMiddleTargetRight', 'ikRingTargetRight', 'ikPinkyTargetRight'])
GrabBones  = set(['ikThumbTargetRight', 'ikIndexTargetRight', 'ikMiddleTargetRight', 'ikRingTargetRight', 'ikPinkyTargetRight',
                  'ikThumbTargetLeft', 'ikIndexTargetLeft', 'ikMiddleTargetLeft', 'ikRingTargetLeft', 'ikPinkyTargetLeft'])
SolverBones = set(['ikThumbSolverRight', 'ikIndexSolverRight', 'ikMiddleSolverRight', 'ikRingSolverRight', 'ikPinkySolverRight',
                   'ikThumbSolverLeft', 'ikIndexSolverLeft', 'ikMiddleSolverLeft', 'ikRingSolverLeft', 'ikPinkySolverLeft'])

ALL_IK_BONES = LArmBones.union(RArmBones,LLegBones,RLegBones,LPinchBones,RPinchBones, LGrabBones, RGrabBones, LHindBones, RHindBones)

IK_TARGET_BONES = ["ikElbowTargetLeft", "ikElbowTargetRight", "ikKneeTargetLeft", "ikKneeTargetRight", "ikHindLimb2TargetLeft", "ikHindLimb2TargetRight"]
IK_LINE_BONES   = ["ikElbowLineLeft", "ikElbowLineRight", "ikKneeLineLeft", "ikKneeLineRight", "ikHindLimb2LineLeft", "ikHindLimb2LineRight"]
IK_POLE_BONES   = ["ElbowLeft", "ElbowRight", "KneeLeft", "KneeRight", "HindLimb2Left", "HindLimb2Right"]

BONE_UNSUPPORTED = 'UNSUPPORTED'
BONE_CONTROL     = 'CONTROL'
BONE_SL          = 'SL'
BONE_ATTACHMENT  = 'ATTACHMENT'
BONE_VOLUME      = 'VOLUME'
BONE_META        = 'META'



def sym(inlist):
    '''
    Return a list expanding  Left and Right for . suffix
    '''
    out = []

    for name in inlist:
        if "." in name:
            out.append(name.replace(".", "Left"))
            out.append(name.replace(".", "Right"))
        else:
            out.append(name)

    return out

def sym_expand(bone_names, inlist):
    '''
    Return a list expanding  Left and Right for . suffix
    '''
    work = sym(inlist)
    out  = []

    for name in work:
        if name[0]=='*':
            out.extend([bn for bn in bone_names if name[1:] in bn])
        elif name[-1]=='*':
            out.extend([bn for bn in bone_names if name[0:-1] in bn])
        else:
            split = name.split("*")
            if len(split) > 1:
                out.extend([bn for bn in bone_names if all( [split[i] in bn for i in range(0,1)])])
            else:
                out.append(name)

    return out


SL_LEAF_BONES = sym(["mSkull", "mToe."])

SLVOLBONES  = ["PELVIS", "BELLY", "CHEST", "NECK", "HEAD", "L_CLAVICLE", "L_UPPER_ARM",
               "L_LOWER_ARM", "L_HAND", "R_CLAVICLE", "R_UPPER_ARM", "R_LOWER_ARM", "R_HAND",
               "R_UPPER_LEG", "R_LOWER_LEG", "R_FOOT", "L_UPPER_LEG", "L_LOWER_LEG", "L_FOOT"]

SLOPTBONES    = []



MTUIBONES = [
         "Skull", "Head", "Neck",
         "CollarLeft", "ShoulderLeft", "ElbowLeft", "WristLeft",
         "CollarRight", "ShoulderRight", "ElbowRight", "WristRight",
         "Chest", "Torso", "COG", "Tinker",
         "HipLeft", "KneeLeft", "AnkleLeft", "FootLeft", "ToeLeft",
         "HipRight", "KneeRight", "AnkleRight", "FootRight", "ToeRight",
    ]

MTUIBONES_EXTENDED = [
         "Skull", "Head", "Neck",

         'FaceRoot',
         'EyeRight', 'EyeLeft', 'FaceEyeAltRight', 'FaceEyeAltLeft',
         'FaceForeheadCenter',
         'FaceForeheadLeft',  'FaceEyebrowOuterLeft',  'FaceEyebrowCenterLeft',  'FaceEyebrowInnerLeft',
         'FaceForeheadRight', 'FaceEyebrowOuterRight', 'FaceEyebrowCenterRight', 'FaceEyebrowInnerRight',

         'FaceEyeLidUpperLeft', 'FaceEyeLidLowerLeft',
         'FaceEyeLidUpperRight', 'FaceEyeLidLowerRight',
         'FaceEar1Left', 'FaceEar2Left', 'FaceEar1Right', 'FaceEar2Right',
         'FaceNoseBase', 'FaceNoseLeft', 'FaceNoseCenter', 'FaceNoseRight',
         'FaceCheekLowerLeft', 'FaceCheekUpperLeft', 'FaceCheekLowerRight', 'FaceCheekUpperRight',

         'FaceJaw',
         'FaceChin',

         'FaceTeethLower',
         'FaceLipLowerLeft', 'FaceLipLowerRight', 'FaceLipLowerCenter',
         'FaceTongueBase', 'FaceTongueTip', 'FaceJawShaper',

         'FaceTeethUpper',
         'FaceLipUpperLeft', 'FaceLipUpperRight', 'FaceLipCornerLeft', 'FaceLipCornerRight', 'FaceLipUpperCenter',
         'FaceEyecornerInnerLeft', 'FaceEyecornerInnerRight', 'FaceNoseBridge',

         'CollarLinkLeft', 'CollarLeft', 'ShoulderLeft', 'ElbowLeft', 'WristLeft',
         'HandMiddle0Left', 'HandMiddle1Left', 'HandMiddle2Left', 'HandMiddle3Left',
         'HandIndex0Left', 'HandIndex1Left', 'HandIndex2Left', 'HandIndex3Left',
         'HandRing0Left', 'HandRing1Left', 'HandRing2Left', 'HandRing3Left',
         'HandPinky0Left', 'HandPinky1Left', 'HandPinky2Left', 'HandPinky3Left',
         'HandThumb0Left', 'HandThumb1Left', 'HandThumb2Left', 'HandThumb3Left',

         'CollarLinkRight', 'CollarRight', 'ShoulderRight', 'ElbowRight', 'WristRight',
         'HandMiddle0Right', 'HandMiddle1Right', 'HandMiddle2Right', 'HandMiddle3Right',
         'HandIndex0Right', 'HandIndex1Right', 'HandIndex2Right', 'HandIndex3Right',
         'HandRing0Right', 'HandRing1Right', 'HandRing2Right', 'HandRing3Right',
         'HandPinky0Right', 'HandPinky1Right', 'HandPinky2Right', 'HandPinky3Right',
         'HandThumb0Right', 'HandThumb1Right', 'HandThumb2Right', 'HandThumb3Right',

         'WingsRoot',
         'Wing1Left', 'Wing2Left', 'Wing3Left', 'Wing4Left', 'Wing4FanLeft',
         'Wing1Right', 'Wing2Right', 'Wing3Right', 'Wing4Right', 'Wing4FanRight',

         'Chest','Spine4', 'Spine3', 'Torso', 'Spine2', 'Spine1', 'COG', 'Tinker',

         'HipLinkLeft', 'HipLeft', 'KneeLeft', 'AnkleLeft', 'FootLeft', 'ToeLeft',
         'HipLinkRight', 'HipRight', 'KneeRight', 'AnkleRight', 'FootRight', 'ToeRight',

         'Tail1', 'Tail2', 'Tail3', 'Tail4', 'Tail5', 'Tail6',
         'Groin',

         'HindLimbsRoot',
         'HindLimb1Left', 'HindLimb2Left', 'HindLimb3Left', 'HindLimb4Left',
         'HindLimb1Right', 'HindLimb2Right', 'HindLimb3Right', 'HindLimb4Right'
]

MTUI_SEPARATORS = ['FaceRoot', 'FaceForeheadCenter', 'FaceEyeLidUpperLeft', 'FaceJaw', 'FaceTeethLower',
    'Chest', 'CollarLinkLeft', 'CollarLinkRight',
    'WingsRoot', 'Tail1',
    'HipLinkLeft', 'HipLinkRight', 'HindLimbsRoot'
    ]

RETARGET_MAPPING = {
 'abdomen': ['mTorso', 'Torso'],
 'chest'  : ['mChest', 'Chest'],
 'neck'   : ['mNeck', 'Neck'],
 'head'   : ['mHead', 'Head'],
 'lCollar': ['mCollarLeft', 'CollarLeft'],
 'rCollar': ['mCollarRight', 'CollarRight'],
 'lShldr' : ['mShoulderLeft', 'ShoulderLeft'],
 'rShldr' : ['mShoulderRight', 'ShoulderRight'],
 'lForeArm':['mElbowLeft', 'ElbowLeft'],
 'rForeArm':['mElbowRight', 'ElbowRight'],
 'lHand'   :['mWristLeft', 'WristLeft'],
 'rHand'   :['mWristRight', 'WristRight'],
 'lThigh'  :['mHipLeft', 'HipLeft'],
 'rThigh'  :['mHipRight', 'HipRight'],
 'lShin'   :['mKneeLeft', 'KneeLeft'],
 'rShin'   :['mKneeRight', 'KneeRight'],
 'lFoot'   :['mAnkleLeft', 'AnkleLeft'],
 'rFoot'   :['mAnkleRight', 'AnkleRight'],
 'Skull'   :['mSkull', 'Skull'],
 'EyeRight':['mEyeRight', 'EyeRight'],
 'EyeLeft' :['mEyeLeft', 'EyeLeft'],
 'Spine1'  :['mSpine1', 'Spine1'],
 'Spine2'  :['mSpine2', 'Spine2'],
 'Spine3'  :['mSpine3', 'Spine3'],
 'Spine4'  :['mSpine4', 'Spine4'],
 'figureHair' :['mSkull', 'Skull']
}


MTBONES = [
         "COG",'Tinker',
         "Torso", "Chest", "Neck", "Head", "Skull",
         "CollarLinkLeft", "CollarLeft", "ShoulderLeft", "ElbowLeft", "WristLeft",
         "CollarLinkRight", "CollarRight", "ShoulderRight", "ElbowRight", "WristRight",

         "HipLinkLeft",  "HipLeft",  "KneeLeft",  "AnkleLeft",  "FootLeft",  "ToeLeft",
         "HipLinkRight", "HipRight", "KneeRight", "AnkleRight", "FootRight", "ToeRight",
    ]
MTBONES_EXTENDED = [
        "COG",'Tinker', 'Spine1', 'Spine2', 'Torso', 'Spine3', 'Spine4',
        'Chest', 'Neck', 'Head', 'Skull',
        'EyeRight', 'EyeLeft',
        'FaceRoot',
        'FaceEyeAltRight', 'FaceEyeAltLeft',
        'FaceForeheadLeft', 'FaceForeheadRight',
        'FaceEyebrowOuterLeft', 'FaceEyebrowCenterLeft', 'FaceEyebrowInnerLeft',
        'FaceEyebrowOuterRight', 'FaceEyebrowCenterRight', 'FaceEyebrowInnerRight',
        'FaceEyeLidUpperLeft', 'FaceEyeLidLowerLeft', 'FaceEyeLidUpperRight', 'FaceEyeLidLowerRight',
        'FaceEar1Left', 'FaceEar2Left', 'FaceEar1Right', 'FaceEar2Right',
        'FaceNoseLeft', 'FaceNoseCenter', 'FaceNoseRight', 'FaceCheekLowerLeft', 'FaceCheekUpperLeft', 'FaceCheekLowerRight', 'FaceCheekUpperRight',
        'FaceJaw', 'FaceChin', 'FaceTeethLower',
        'FaceLipLowerLeft', 'FaceLipLowerRight', 'FaceLipLowerCenter',
        'FaceTongueBase', 'FaceTongueTip', 'FaceJawShaper',
        'FaceForeheadCenter', 'FaceNoseBase',
        'FaceTeethUpper', 'FaceLipUpperLeft', 'FaceLipUpperRight', 'FaceLipCornerLeft', 'FaceLipCornerRight', 'FaceLipUpperCenter',
        'FaceEyecornerInnerLeft', 'FaceEyecornerInnerRight', 'FaceNoseBridge',

        'CollarLinkLeft', 'CollarLeft', 'ShoulderLeft', 'ElbowLeft', 'WristLeft',
        'HandMiddle0Left', 'HandMiddle1Left', 'HandMiddle2Left', 'HandMiddle3Left',
        'HandIndex0Left', 'HandIndex1Left', 'HandIndex2Left', 'HandIndex3Left',
        'HandRing0Left', 'HandRing1Left', 'HandRing2Left', 'HandRing3Left',
        'HandPinky0Left', 'HandPinky1Left', 'HandPinky2Left', 'HandPinky3Left',
        'HandThumb0Left', 'HandThumb1Left', 'HandThumb2Left', 'HandThumb3Left',

        'CollarLinkRight', 'CollarRight', 'ShoulderRight', 'ElbowRight', 'WristRight',
        'HandMiddle0Right', 'HandMiddle1Right', 'HandMiddle2Right', 'HandMiddle3Right',
        'HandIndex0Right', 'HandIndex1Right', 'HandIndex2Right', 'HandIndex3Right',
        'HandRing0Right', 'HandRing1Right', 'HandRing2Right', 'HandRing3Right',
        'HandPinky0Right', 'HandPinky1Right', 'HandPinky2Right', 'HandPinky3Right',
        'HandThumb0Right', 'HandThumb1Right', 'HandThumb2Right', 'HandThumb3Right',

        'WingsRoot',
        'Wing1Left', 'Wing2Left', 'Wing3Left', 'Wing4Left', 'Wing4FanLeft',
        'Wing1Right', 'Wing2Right', 'Wing3Right', 'Wing4Right', 'Wing4FanRight',

        'HipLinkLeft', 'HipLeft', 'KneeLeft', 'AnkleLeft', 'FootLeft', 'ToeLeft',
        'HipLinkRight', 'HipRight', 'KneeRight', 'AnkleRight', 'FootRight', 'ToeRight',

        'Tail1', 'Tail2', 'Tail3', 'Tail4', 'Tail5', 'Tail6', 'Groin',

        'HindLimbsRoot',
        'HindLimb1Left', 'HindLimb2Left', 'HindLimb3Left', 'HindLimb4Left',
        'HindLimb1Right', 'HindLimb2Right', 'HindLimb3Right', 'HindLimb4Right'
    ]


MCMBONES = [
        "Hips", "Hips",
        "LowerBack", "Spine", "Spine1", "Neck1", "Head",
        "", "LeftShoulder",  "LeftArm",  "LeftForeArm",  "LeftHand",
        "", "RightShoulder", "RightArm", "RightForeArm", "RightHand",

        "", "LeftUpLeg",  "LeftLeg",  "LeftFoot",  "LeftToeBase",  "",
        "", "RightUpLeg", "RightLeg", "RightFoot", "RightToeBase", "",
    ]
MCMBONES_EXTENDED = [
        'Hips', 'Hips',
        'Spine1', 'Spine2', 'LowerBack', 'Spine', 'Spine1',
        'Chest', 'Neck1', 'Head', 'Skull',
        'EyeRight', 'EyeLeft',
        'FaceRoot',
        'FaceEyeAltRight', 'FaceEyeAltLeft',
        'FaceForeheadLeft', 'FaceForeheadRight',
        'FaceEyebrowOuterLeft', 'FaceEyebrowCenterLeft', 'FaceEyebrowInnerLeft',
        'FaceEyebrowOuterRight', 'FaceEyebrowCenterRight', 'FaceEyebrowInnerRight',
        'FaceEyeLidUpperLeft', 'FaceEyeLidLowerLeft', 'FaceEyeLidUpperRight', 'FaceEyeLidLowerRight',
        'FaceEar1Left', 'FaceEar2Left', 'FaceEar1Right', 'FaceEar2Right',
        'FaceNoseLeft', 'FaceNoseCenter', 'FaceNoseRight', 'FaceCheekLowerLeft', 'FaceCheekUpperLeft', 'FaceCheekLowerRight', 'FaceCheekUpperRight',
        'FaceJaw', 'FaceChin', 'FaceTeethLower',
        'FaceLipLowerLeft', 'FaceLipLowerRight', 'FaceLipLowerCenter',
        'FaceTongueBase', 'FaceTongueTip', 'FaceJawShaper',
        'FaceForeheadCenter', 'FaceNoseBase',
        'FaceTeethUpper', 'FaceLipUpperLeft', 'FaceLipUpperRight', 'FaceLipCornerLeft', 'FaceLipCornerRight', 'FaceLipUpperCenter',
        'FaceEyecornerInnerLeft', 'FaceEyecornerInnerRight', 'FaceNoseBridge',

        '', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand',
        'HandMiddle0Left', 'HandMiddle1Left', 'HandMiddle2Left', 'HandMiddle3Left',
        'HandIndex0Left', 'HandIndex1Left', 'HandIndex2Left', 'HandIndex3Left',
        'HandRing0Left', 'HandRing1Left', 'HandRing2Left', 'HandRing3Left',
        'HandPinky0Left', 'HandPinky1Left', 'HandPinky2Left', 'HandPinky3Left',
        'HandThumb0Left', 'HandThumb1Left', 'HandThumb2Left', 'HandThumb3Left',

        '', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand',
        'HandMiddle0Right', 'HandMiddle1Right', 'HandMiddle2Right', 'HandMiddle3Right',
        'HandIndex0Right', 'HandIndex1Right', 'HandIndex2Right', 'HandIndex3Right',
        'HandRing0Right', 'HandRing1Right', 'HandRing2Right', 'HandRing3Right',
        'HandPinky0Right', 'HandPinky1Right', 'HandPinky2Right', 'HandPinky3Right',
        'HandThumb0Right', 'HandThumb1Right', 'HandThumb2Right', 'HandThumb3Right',

        'WingsRoot',
        'Wing1Left', 'Wing2Left', 'Wing3Left', 'Wing4Left', 'Wing4FanLeft',
        'Wing1Right', 'Wing2Right', 'Wing3Right', 'Wing4Right', 'Wing4FanRight',

        '', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', '',
        '', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase', '',

        'Tail1', 'Tail2', 'Tail3', 'Tail4', 'Tail5', 'Tail6', 'Groin',

        'HindLimbsRoot', 'HindLimb1Left', 'HindLimb2Left', 'HindLimb3Left', 'HindLimb4Left',
        'HindLimb1Right', 'HindLimb2Right', 'HindLimb3Right', 'HindLimb4Right'
    ]



MSLBONES = [
        "hip", '',
        "abdomen", "chest", "neck", "head", "figureHair",
        '', "lCollar", "lShldr", "lForeArm", "lHand",
        '', "rCollar", "rShldr", "rForeArm", "rHand",

        '', "lThigh", "lShin", "lFoot", 'mFootLeft', 'mToeLeft',
        '', "rThigh", "rShin", "rFoot", 'mFootRight', 'mToeRight'
    ]

MSLBONES_EXTENDED = [
        'hip', '', 'mSpine1', 'mSpine2', 'abdomen', 'mSpine3', 'mSpine4',
        'chest', 'neck', 'head', 'figureHair',
        'EyeRight', 'EyeLeft',

        'mFaceRoot',
        'mFaceEyeAltRight', 'mFaceEyeAltLeft',
        'mFaceForeheadLeft', 'mFaceForeheadRight',
        'mFaceEyebrowOuterLeft', 'mFaceEyebrowCenterLeft', 'mFaceEyebrowInnerLeft',
        'mFaceEyebrowOuterRight', 'mFaceEyebrowCenterRight', 'mFaceEyebrowInnerRight',
        'mFaceEyeLidUpperLeft', 'mFaceEyeLidLowerLeft', 'mFaceEyeLidUpperRight', 'mFaceEyeLidLowerRight',
        'mFaceEar1Left', 'mFaceEar2Left', 'mFaceEar1Right', 'mFaceEar2Right',
        'mFaceNoseLeft', 'mFaceNoseCenter', 'mFaceNoseRight',
        'mFaceCheekLowerLeft', 'mFaceCheekUpperLeft', 'mFaceCheekLowerRight', 'mFaceCheekUpperRight',
        'mFaceJaw', 'mFaceChin', 'mFaceTeethLower',
        'mFaceLipLowerLeft', 'mFaceLipLowerRight', 'mFaceLipLowerCenter',
        'mFaceTongueBase', 'mFaceTongueTip', 'mFaceJawShaper',
        'mFaceForeheadCenter', 'mFaceNoseBase',
        'mFaceTeethUpper', 'mFaceLipUpperLeft', 'mFaceLipUpperRight', 'mFaceLipCornerLeft', 'mFaceLipCornerRight', 'mFaceLipUpperCenter',
        'mFaceEyecornerInnerLeft', 'mFaceEyecornerInnerRight',
        'mFaceNoseBridge',

        '', 'lCollar', 'lShldr', 'lForeArm', 'lHand',
        'mHandMiddle0Left', 'mHandMiddle1Left', 'mHandMiddle2Left', 'mHandMiddle3Left',
        'mHandIndex0Left', 'mHandIndex1Left', 'mHandIndex2Left', 'mHandIndex3Left',
        'mHandRing0Left', 'mHandRing1Left', 'mHandRing2Left', 'mHandRing3Left',
        'mHandPinky0Left', 'mHandPinky1Left', 'mHandPinky2Left', 'mHandPinky3Left',
        'mHandThumb0Left', 'mHandThumb1Left', 'mHandThumb2Left', 'mHandThumb3Left',

        '', 'rCollar', 'rShldr', 'rForeArm', 'rHand',
        'mHandMiddle0Right', 'mHandMiddle1Right', 'mHandMiddle2Right', 'mHandMiddle3Right',
        'mHandIndex0Right', 'mHandIndex1Right', 'mHandIndex2Right', 'mHandIndex3Right',
        'mHandRing0Right', 'mHandRing1Right', 'mHandRing2Right', 'mHandRing3Right',
        'mHandPinky0Right', 'mHandPinky1Right', 'mHandPinky2Right', 'mHandPinky3Right',
        'mHandThumb0Right', 'mHandThumb1Right', 'mHandThumb2Right', 'mHandThumb3Right',

        'mWingsRoot',
        'mWing1Left',  'mWing2Left',  'mWing3Left',  'mWing4Left',  'mWing4FanLeft',
        'mWing1Right', 'mWing2Right', 'mWing3Right', 'mWing4Right', 'mWing4FanRight',

        '', 'lThigh', 'lShin', 'lFoot', 'mFootLeft', 'mToeLeft',
        '', 'rThigh', 'rShin', 'rFoot', 'mFootRight', 'mToeRight',

        'mTail1', 'mTail2', 'mTail3', 'mTail4', 'mTail5', 'mTail6', 'mGroin',

        'mHindLimbsRoot',  'mHindLimb1Left',  'mHindLimb2Left',  'mHindLimb3Left', 'mHindLimb4Left',
        'mHindLimb1Right', 'mHindLimb2Right', 'mHindLimb3Right', 'mHindLimb4Right'
    ]



ANIMBONE_MAP = {
         "COG"            : "hip",
         "Torso"          : "abdomen",
         "Chest"          : "chest",
         "Neck"           : "neck",
         "Head"           : "head",
         "Skull"          : "figureHair",
         "CollarLeft"     : "lCollar",
         "ShoulderLeft"   : "lShldr",
         "ElbowLeft"      : "lForeArm",
         "WristLeft"      : "lHand",
         "CollarRight"    : "rCollar",
         "ShoulderRight"  : "rShldr",
         "ElbowRight"     : "rForeArm",
         "WristRight"     : "rHand",
         "Tinker"      : "hip",
         "Pelvis"         : "hip",
         "HipLeft"        : "lThigh",
         "KneeLeft"       : "lShin",
         "AnkleLeft"      : "lFoot",
         "FootLeft"       : None,
         "ToeLeft"        : None,
         "HipRight"       : "rThigh",
         "KneeRight"      : "rShin",
         "AnkleRight"     : "rFoot",
         "FootRight"      : None,
         "ToeRight"       : None
    }


ANIMATION_BONE_MAP = OrderedDict ( [
        ( 'COG'                    , {'sl':'hip',                      'cm':'Hips'} ),
        ( 'Tinker'                 , {'sl':'',                         'cm':'Hips'} ),
        ( 'Spine1'                 , {'sl':'mSpine1',                  'cm':'Spine1'} ),
        ( 'Spine2'                 , {'sl':'mSpine2',                  'cm':'Spine2'} ),
        ( 'Torso'                  , {'sl':'abdomen',                  'cm':'LowerBack'} ),
        ( 'Spine3'                 , {'sl':'mSpine3',                  'cm':'Spine'} ),
        ( 'Spine4'                 , {'sl':'mSpine4',                  'cm':'Spine3'} ),
        ( 'Chest'                  , {'sl':'chest',                    'cm':'Chest'} ),
        ( 'Neck'                   , {'sl':'neck',                     'cm':'Neck1'} ),
        ( 'Head'                   , {'sl':'head',                     'cm':'Head'} ),
        ( 'Skull'                  , {'sl':'figureHair',               'cm':'Skull'} ),
        ( 'EyeRight'               , {'sl':'EyeRight',                 'cm':'EyeRight'} ),
        ( 'EyeLeft'                , {'sl':'EyeLeft',                  'cm':'EyeLeft'} ),
        ( 'FaceRoot'               , {'sl':'mFaceRoot',                'cm':'FaceRoot'} ),
        ( 'FaceEyeAltRight'        , {'sl':'mFaceEyeAltRight',         'cm':'FaceEyeAltRight'} ),
        ( 'FaceEyeAltLeft'         , {'sl':'mFaceEyeAltLeft',          'cm':'FaceEyeAltLeft'} ),
        ( 'FaceForeheadLeft'       , {'sl':'mFaceForeheadLeft',        'cm':'FaceForeheadLeft'} ),
        ( 'FaceForeheadRight'      , {'sl':'mFaceForeheadRight',       'cm':'FaceForeheadRight'} ),
        ( 'FaceEyebrowOuterLeft'   , {'sl':'mFaceEyebrowOuterLeft',    'cm':'FaceEyebrowOuterLeft'} ),
        ( 'FaceEyebrowCenterLeft'  , {'sl':'mFaceEyebrowCenterLeft',   'cm':'FaceEyebrowCenterLeft'} ),
        ( 'FaceEyebrowInnerLeft'   , {'sl':'mFaceEyebrowInnerLeft',    'cm':'FaceEyebrowInnerLeft'} ),
        ( 'FaceEyebrowOuterRight'  , {'sl':'mFaceEyebrowOuterRight',   'cm':'FaceEyebrowOuterRight'} ),
        ( 'FaceEyebrowCenterRight' , {'sl':'mFaceEyebrowCenterRight',  'cm':'FaceEyebrowCenterRight'} ),
        ( 'FaceEyebrowInnerRight'  , {'sl':'mFaceEyebrowInnerRight',   'cm':'FaceEyebrowInnerRight'} ),
        ( 'FaceEyeLidUpperLeft'    , {'sl':'mFaceEyeLidUpperLeft',     'cm':'FaceEyeLidUpperLeft'} ),
        ( 'FaceEyeLidLowerLeft'    , {'sl':'mFaceEyeLidLowerLeft',     'cm':'FaceEyeLidLowerLeft'} ),
        ( 'FaceEyeLidUpperRight'   , {'sl':'mFaceEyeLidUpperRight',    'cm':'FaceEyeLidUpperRight'} ),
        ( 'FaceEyeLidLowerRight'   , {'sl':'mFaceEyeLidLowerRight',    'cm':'FaceEyeLidLowerRight'} ),
        ( 'FaceEar1Left'           , {'sl':'mFaceEar1Left',            'cm':'FaceEar1Left'} ),
        ( 'FaceEar2Left'           , {'sl':'mFaceEar2Left',            'cm':'FaceEar2Left'} ),
        ( 'FaceEar1Right'          , {'sl':'mFaceEar1Right',           'cm':'FaceEar1Right'} ),
        ( 'FaceEar2Right'          , {'sl':'mFaceEar2Right',           'cm':'FaceEar2Right'} ),
        ( 'FaceNoseLeft'           , {'sl':'mFaceNoseLeft',            'cm':'FaceNoseLeft'} ),
        ( 'FaceNoseCenter'         , {'sl':'mFaceNoseCenter',          'cm':'FaceNoseCenter'} ),
        ( 'FaceNoseRight'          , {'sl':'mFaceNoseRight',           'cm':'FaceNoseRight'} ),
        ( 'FaceCheekLowerLeft'     , {'sl':'mFaceCheekLowerLeft',      'cm':'FaceCheekLowerLeft'} ),
        ( 'FaceCheekUpperLeft'     , {'sl':'mFaceCheekUpperLeft',      'cm':'FaceCheekUpperLeft'} ),
        ( 'FaceCheekLowerRight'    , {'sl':'mFaceCheekLowerRight',     'cm':'FaceCheekLowerRight'} ),
        ( 'FaceCheekUpperRight'    , {'sl':'mFaceCheekUpperRight',     'cm':'FaceCheekUpperRight'} ),
        ( 'FaceJaw'                , {'sl':'mFaceJaw',                 'cm':'FaceJaw'} ),
        ( 'FaceChin'               , {'sl':'mFaceChin',                'cm':'FaceChin'} ),
        ( 'FaceTeethLower'         , {'sl':'mFaceTeethLower',          'cm':'FaceTeethLower'} ),
        ( 'FaceLipLowerLeft'       , {'sl':'mFaceLipLowerLeft',        'cm':'FaceLipLowerLeft'} ),
        ( 'FaceLipLowerRight'      , {'sl':'mFaceLipLowerRight',       'cm':'FaceLipLowerRight'} ),
        ( 'FaceLipLowerCenter'     , {'sl':'mFaceLipLowerCenter',      'cm':'FaceLipLowerCenter'} ),
        ( 'FaceTongueBase'         , {'sl':'mFaceTongueBase',          'cm':'FaceTongueBase'} ),
        ( 'FaceTongueTip'          , {'sl':'mFaceTongueTip',           'cm':'FaceTongueTip'} ),
        ( 'FaceJawShaper'          , {'sl':'mFaceJawShaper',           'cm':'FaceJawShaper'} ),
        ( 'FaceForeheadCenter'     , {'sl':'mFaceForeheadCenter',      'cm':'FaceForeheadCenter'} ),
        ( 'FaceNoseBase'           , {'sl':'mFaceNoseBase',            'cm':'FaceNoseBase'} ),
        ( 'FaceTeethUpper'         , {'sl':'mFaceTeethUpper',          'cm':'FaceTeethUpper'} ),
        ( 'FaceLipUpperLeft'       , {'sl':'mFaceLipUpperLeft',        'cm':'FaceLipUpperLeft'} ),
        ( 'FaceLipUpperRight'      , {'sl':'mFaceLipUpperRight',       'cm':'FaceLipUpperRight'} ),
        ( 'FaceLipCornerLeft'      , {'sl':'mFaceLipCornerLeft',       'cm':'FaceLipCornerLeft'} ),
        ( 'FaceLipCornerRight'     , {'sl':'mFaceLipCornerRight',      'cm':'FaceLipCornerRight'} ),
        ( 'FaceLipUpperCenter'     , {'sl':'mFaceLipUpperCenter',      'cm':'FaceLipUpperCenter'} ),
        ( 'FaceEyecornerInnerLeft' , {'sl':'mFaceEyecornerInnerLeft',  'cm':'FaceEyecornerInnerLeft'} ),
        ( 'FaceEyecornerInnerRight', {'sl':'mFaceEyecornerInnerRight', 'cm':'FaceEyecornerInnerRight'} ),
        ( 'FaceNoseBridge'         , {'sl':'mFaceNoseBridge',          'cm':'FaceNoseBridge'} ),
        ( 'CollarLinkLeft'         , {'sl':'',                         'cm':''} ),
        ( 'CollarLeft'             , {'sl':'lCollar',                  'cm':'LeftShoulder'} ),
        ( 'ShoulderLeft'           , {'sl':'lShldr',                   'cm':'LeftArm'} ),
        ( 'ElbowLeft'              , {'sl':'lForeArm',                 'cm':'LeftForeArm'} ),
        ( 'WristLeft'              , {'sl':'lHand',                    'cm':'LeftHand'} ),
        ( 'HandMiddle1Left'        , {'sl':'mHandMiddle1Left',         'cm':'HandMiddle1Left'} ),
        ( 'HandMiddle2Left'        , {'sl':'mHandMiddle2Left',         'cm':'HandMiddle2Left'} ),
        ( 'HandMiddle3Left'        , {'sl':'mHandMiddle3Left',         'cm':'HandMiddle3Left'} ),
        ( 'HandIndex1Left'         , {'sl':'mHandIndex1Left',          'cm':'HandIndex1Left'} ),
        ( 'HandIndex2Left'         , {'sl':'mHandIndex2Left',          'cm':'HandIndex2Left'} ),
        ( 'HandIndex3Left'         , {'sl':'mHandIndex3Left',          'cm':'HandIndex3Left'} ),
        ( 'HandRing1Left'          , {'sl':'mHandRing1Left',           'cm':'HandRing1Left'} ),
        ( 'HandRing2Left'          , {'sl':'mHandRing2Left',           'cm':'HandRing2Left'} ),
        ( 'HandRing3Left'          , {'sl':'mHandRing3Left',           'cm':'HandRing3Left'} ),
        ( 'HandPinky1Left'         , {'sl':'mHandPinky1Left',          'cm':'HandPinky1Left'} ),
        ( 'HandPinky2Left'         , {'sl':'mHandPinky2Left',          'cm':'HandPinky2Left'} ),
        ( 'HandPinky3Left'         , {'sl':'mHandPinky3Left',          'cm':'HandPinky3Left'} ),
        ( 'HandThumb1Left'         , {'sl':'mHandThumb1Left',          'cm':'HandThumb1Left'} ),
        ( 'HandThumb2Left'         , {'sl':'mHandThumb2Left',          'cm':'HandThumb2Left'} ),
        ( 'HandThumb3Left'         , {'sl':'mHandThumb3Left',          'cm':'HandThumb3Left'} ),
        ( 'CollarLinkRight'        , {'sl':'',                         'cm':''} ),
        ( 'CollarRight'            , {'sl':'rCollar',                  'cm':'RightShoulder'} ),
        ( 'ShoulderRight'          , {'sl':'rShldr',                   'cm':'RightArm'} ),
        ( 'ElbowRight'             , {'sl':'rForeArm',                 'cm':'RightForeArm'} ),
        ( 'WristRight'             , {'sl':'rHand',                    'cm':'RightHand'} ),
        ( 'HandMiddle1Right'       , {'sl':'mHandMiddle1Right',        'cm':'HandMiddle1Right'} ),
        ( 'HandMiddle2Right'       , {'sl':'mHandMiddle2Right',        'cm':'HandMiddle2Right'} ),
        ( 'HandMiddle3Right'       , {'sl':'mHandMiddle3Right',        'cm':'HandMiddle3Right'} ),
        ( 'HandIndex1Right'        , {'sl':'mHandIndex1Right',         'cm':'HandIndex1Right'} ),
        ( 'HandIndex2Right'        , {'sl':'mHandIndex2Right',         'cm':'HandIndex2Right'} ),
        ( 'HandIndex3Right'        , {'sl':'mHandIndex3Right',         'cm':'HandIndex3Right'} ),
        ( 'HandRing1Right'         , {'sl':'mHandRing1Right',          'cm':'HandRing1Right'} ),
        ( 'HandRing2Right'         , {'sl':'mHandRing2Right',          'cm':'HandRing2Right'} ),
        ( 'HandRing3Right'         , {'sl':'mHandRing3Right',          'cm':'HandRing3Right'} ),
        ( 'HandPinky1Right'        , {'sl':'mHandPinky1Right',         'cm':'HandPinky1Right'} ),
        ( 'HandPinky2Right'        , {'sl':'mHandPinky2Right',         'cm':'HandPinky2Right'} ),
        ( 'HandPinky3Right'        , {'sl':'mHandPinky3Right',         'cm':'HandPinky3Right'} ),
        ( 'HandThumb1Right'        , {'sl':'mHandThumb1Right',         'cm':'HandThumb1Right'} ),
        ( 'HandThumb2Right'        , {'sl':'mHandThumb2Right',         'cm':'HandThumb2Right'} ),
        ( 'HandThumb3Right'        , {'sl':'mHandThumb3Right',         'cm':'HandThumb3Right'} ),
        ( 'WingsRoot'              , {'sl':'mWingsRoot',               'cm':'WingsRoot'} ),
        ( 'Wing1Left'              , {'sl':'mWing1Left',               'cm':'Wing1Left'} ),
        ( 'Wing2Left'              , {'sl':'mWing2Left',               'cm':'Wing2Left'} ),
        ( 'Wing3Left'              , {'sl':'mWing3Left',               'cm':'Wing3Left'} ),
        ( 'Wing4Left'              , {'sl':'mWing4Left',               'cm':'Wing4Left'} ),
        ( 'Wing4FanLeft'           , {'sl':'mWing4FanLeft',            'cm':'Wing4FanLeft'} ),
        ( 'Wing1Right'             , {'sl':'mWing1Right',              'cm':'Wing1Right'} ),
        ( 'Wing2Right'             , {'sl':'mWing2Right',              'cm':'Wing2Right'} ),
        ( 'Wing3Right'             , {'sl':'mWing3Right',              'cm':'Wing3Right'} ),
        ( 'Wing4Right'             , {'sl':'mWing4Right' ,             'cm':'Wing4Right'} ),
        ( 'Wing4FanRight'          , {'sl':'mWing4FanRight',           'cm':'Wing4FanRight'} ),
        ( 'HipLinkLeft'            , {'sl':'',                         'cm':''} ),
        ( 'HipLeft'                , {'sl':'lThigh',                   'cm':'LeftUpLeg'} ),
        ( 'KneeLeft'               , {'sl':'lShin',                    'cm':'LeftLeg'} ),
        ( 'AnkleLeft'              , {'sl':'lFoot',                    'cm':'LeftFoot'} ),
        ( 'FootLeft'               , {'sl':'mFootLeft',                'cm':'LeftToeBase'} ),
        ( 'ToeLeft'                , {'sl':'mToeLeft',                 'cm':''} ),
        ( 'HipLinkRight'           , {'sl':'',                         'cm':''} ),
        ( 'HipRight'               , {'sl':'rThigh',                   'cm':'RightUpLeg'} ),
        ( 'KneeRight'              , {'sl':'rShin',                    'cm':'RightLeg'} ),
        ( 'AnkleRight'             , {'sl':'rFoot',                    'cm':'RightFoot'} ),
        ( 'FootRight'              , {'sl':'mFootRight',               'cm':'RightToeBase'} ),
        ( 'ToeRight'               , {'sl':'mToeRight',                'cm':''} ),
        ( 'Tail1'                  , {'sl':'mTail1',                   'cm':'Tail1'} ),
        ( 'Tail2'                  , {'sl':'mTail2',                   'cm':'Tail2'} ),
        ( 'Tail3'                  , {'sl':'mTail3',                   'cm':'Tail3'} ),
        ( 'Tail4'                  , {'sl':'mTail4',                   'cm':'Tail4'} ),
        ( 'Tail5'                  , {'sl':'mTail5',                   'cm':'Tail5'} ),
        ( 'Tail6'                  , {'sl':'mTail6',                   'cm':'Tail6'} ),
        ( 'Groin'                  , {'sl':'mGroin',                   'cm':'Groin'} ),
        ( 'HindLimbsRoot'          , {'sl':'mHindLimbsRoot',           'cm':'HindLimbsRoot'} ),
        ( 'HindLimb1Left'          , {'sl':'mHindLimb1Left',           'cm':'HindLimb1Left'} ),
        ( 'HindLimb2Left'          , {'sl':'mHindLimb2Left',           'cm':'HindLimb2Left'} ),
        ( 'HindLimb3Left'          , {'sl':'mHindLimb3Left',           'cm':'HindLimb3Left'} ),
        ( 'HindLimb4Left'          , {'sl':'mHindLimb4Left',           'cm':'HindLimb4Left'} ),
        ( 'HindLimb1Right'         , {'sl':'mHindLimb1Right',          'cm':'HindLimb1Right'} ),
        ( 'HindLimb2Right'         , {'sl':'mHindLimb2Right',          'cm':'HindLimb2Right'} ),
        ( 'HindLimb3Right'         , {'sl':'mHindLimb3Right',          'cm':'HindLimb3Right'} ),
        ( 'HindLimb4Right'         , {'sl':'mHindLimb4Right',          'cm':'HindLimb4Right'} )
	]
	)




BONE_TAIL_LOCATIONS = {

    "Origin"       : (-0.20,    0.0,  0.0     ),
    "COG"          : (-0.15368, 0.0,  0.0     ),

    }



DEFAULT_BONE_LIMITS= {

    "COG"            :[(0.95,0.95,0.95),  None,       None,      None,      None],
    "Tinker"      :[(0.85,0.85,0.85), (-90,40),   (-60,60),  (-40,40),   None],
    "Torso"          :[(0.85,0.85,0.85), (-40,80),   (-60,60),  (-40,40),   None],
    "Pelvis"         :[None,              None,       None,      None,      None],
    "Chest"          :[(0.8,0.8,0.8),    (-40,50),   (-60,60),  (-40,40),   None],
    "Neck"           :[(0.75,0.75,0.75), (-50,40),   (-60,60),  (-40,40),   None],
    "Head"           :[(0.8,0.8,0.8),    (-70,40),   (-80,80),  (-40,40),   None],
    "Skull"          :[(0.8,0.8,0.8),     None,       None,      None,      None],
    "CollarLinkLeft" :[None,              None,       None,      None,      -45],
    "CollarLinkRight":[None,              None,       None,      None,      45],
    "CollarLeft"     :[(0.9,0.9,0.9),    (-80,80),   (-80,80),  (-80,80),   None],
    "CollarRight"    :[(0.9,0.9,0.9),    (-80,80),   (-80,80),  (-80,80),   None],
    "ShoulderLeft"   :[(0.3,0.3,0.3),    (-120,30),  (-90,90),  (-100,30),  None],
    "ShoulderRight"  :[(0.3,0.3,0.3),    (-120,30),  (-90,90),  (-30,100),  None],
    "ElbowLeft"      :[(0.2, 0.2, 0.2),  (-45,45),   (-10,10),  (-160,15) , None],
    "ElbowRight"     :[(0.2, 0.2, 0.2),  (-45,45),   (-10,10),  (-15,160) , None],
    "WristLeft"      :[(0.5, 0.5, 0.5),  (-100,100), (-45,45),  (-30,40) ,  None],
    "WristRight"     :[(0.5, 0.5, 0.5),  (-100,100), (-45,45),  (-40,30) ,  None],
    "HipLinkLeft"    :[None,              None,       None,      None,      -45],
    "HipLinkRight"   :[None,              None,       None,      None,      45],
    "HipLeft"        :[(0.5,0.5,0.5),    (-160,40),  (-60,40),  (-100,30),  None],
    "HipRight"       :[(0.5,0.5,0.5),    (-160,40),  (-40,60),  (-30,100),  None],
    "KneeLeft"       :[(0.6,0.6,0.6),    (-10,160),  (-40,40),  (0,0),      None],
    "KneeRight"      :[(0.6,0.6,0.6),    (-10,160),  (-40,40),  (0,0),      None],
    "AnkleLeft"      :[(0.75,0.75,0.75), (-50,70),   (-50,20),  (-20,20),   None],
    "AnkleRight"     :[(0.75,0.75,0.75), (-50,70),   (-20,50),  (-20,20),   None],
    "FootLeft"       :[(0.8,0.8,0.8),     None,       None,      None,      None],
    "FootRight"      :[(0.8,0.8,0.8),     None,       None,      None,      None],

    "HindLimb1Left"  :[(0.5,0.5,0.5),    (-160,40),  (-60,40),  (-100,30),  None],
    "HindLimb1Right" :[(0.5,0.5,0.5),    (-160,40),  (-40,60),  (-30,100),  None],
    "HindLimb2Left"  :[(0.6,0.6,0.6),    (-10,160),  (-40,40),  (0,0),      None],
    "HindLimb2Right" :[(0.6,0.6,0.6),    (-10,160),  (-40,40),  (0,0),      None],
    "HindLimb3Left"  :[(0.75,0.75,0.75), (-50,70),   (-50,20),  (-20,20),   None],
    "HindLimb3Right" :[(0.75,0.75,0.75), (-50,70),   (-20,50),  (-20,20),   None],
    "HindLimb4Left"  :[(0.8,0.8,0.8),     None,       None,      None,      None],
    "HindLimb4Right" :[(0.8,0.8,0.8),     None,       None,      None,      None],

    "ToeLeft"        :[(0.8,0.8,0.8),     None,       None,      None,      None],
    "ToeRight"       :[(0.8,0.8,0.8),     None,       None,      None,      None],
    "EyeLeft"        :[None,              None,       None,      None,      None],
    "EyeRight"       :[None,              None,       None,      None,      None],
    }


NONDEFORMS = ['mFaceEyeAltLeft', 'mFaceEyeAltRight', 'mEyeLeft', 'mEyeRight', 'mFaceTongueBase', 'mFaceTongueTip', 'mFaceTeethUpper', 'mFaceTeethLower']
EXTRABONES = ["mHead", 'mEyeLeft', 'mEyeRight']
B_LAYER_COUNT       = 32

B_LAYER_ORIGIN          = 0
B_LAYER_TORSO           = 1
B_LAYER_ARMS            = 2
B_LAYER_LEGS            = 3
B_LAYER_EYE_TARGET      = 4
B_LAYER_EYE_ALT_TARGET  = 5
B_LAYER_ATTACHMENT      = 6
B_LAYER_VOLUME          = 7

B_LAYER_FACE            =  8
B_LAYER_HAND            =  9
B_LAYER_WING            = 10
B_LAYER_TAIL            = 11
B_LAYER_GROIN           = 12
B_LAYER_SPINE           = 13
B_LAYER_LIMB            = 14
B_LAYER_EXTRA           = 15

B_LAYER_SL              = 16
B_LAYER_IK_ARMS         = 17
B_LAYER_IK_LEGS         = 18
B_LAYER_IK_LIMBS        = 19
B_LAYER_IK_FACE         = 20
B_LAYER_IK_HAND         = 21
B_LAYER_IK_HIDDEN       = 21
B_LAYER_STRUCTURE       = 22
B_LAYER_EXTENDED        = 23

B_LAYER_DEFORM_FACE     = 24
B_LAYER_DEFORM_HAND     = 25
B_LAYER_DEFORM_WING     = 26
B_LAYER_DEFORM_TAIL     = 27
B_LAYER_DEFORM_GROIN    = 28
B_LAYER_DEFORM_SPINE    = 29
B_LAYER_DEFORM_LIMB     = 30
B_LAYER_DEFORM          = 31


B_EXTENDED_LAYER_SL_EYES = 32
B_EXTENDED_LAYER_ALT_EYES = 33
B_EXTENDED_LAYER_SPINE_LOWER = 34
B_EXTENDED_LAYER_SPINE_UPPER = 35
B_EXTENDED_LAYER_ALL = 36

LAYER_NAMES = {
B_LAYER_ORIGIN          : "ORIGIN",
B_LAYER_TORSO           : "TORSO",
B_LAYER_ARMS            : "ARMS",
B_LAYER_LEGS            : "LEGS",
B_LAYER_EYE_TARGET      : "EYE_TARGET",
B_LAYER_EYE_ALT_TARGET  : "EYE_ALT_TARGET",
B_LAYER_ATTACHMENT      : "ATTACHMENT",
B_LAYER_VOLUME          : "VOLUME",

B_LAYER_FACE            : "FACE",
B_LAYER_HAND            : "HAND",
B_LAYER_WING            : "WING",
B_LAYER_TAIL            : "TAIL",
B_LAYER_GROIN           : "GROIN",
B_LAYER_SPINE           : "SPINE",
B_LAYER_LIMB            : "LIMB",
B_LAYER_EXTRA           : "EXTRA",

B_LAYER_SL              : "SL",
B_LAYER_IK_ARMS         : "IK_ARMS",
B_LAYER_IK_LEGS         : "IK_LEGS",
B_LAYER_IK_LIMBS        : "IK_LIMBS",
B_LAYER_IK_FACE         : "IK_FACE",
B_LAYER_IK_HAND         : "IK_HAND",
B_LAYER_IK_HIDDEN       : "IK_HIDDEN",
B_LAYER_STRUCTURE       : "STRUCTURE",
B_LAYER_EXTENDED        : "EXTENDED",

B_LAYER_DEFORM_FACE     : "DEFORM_FACE",
B_LAYER_DEFORM_HAND     : "DEFORM_HAND",
B_LAYER_DEFORM_WING     : "DEFORM_WING",
B_LAYER_DEFORM_TAIL     : "DEFORM_TAIL",
B_LAYER_DEFORM_GROIN    : "DEFORM_GROIN",
B_LAYER_DEFORM_SPINE    : "DEFORM_SPINE",
B_LAYER_DEFORM_LIMB     : "DEFORM_LIMB",
B_LAYER_DEFORM          : "DEFORM",

B_EXTENDED_LAYER_SL_EYES : "SL_EYES",
B_EXTENDED_LAYER_ALT_EYES : "ALT_EYES",
B_EXTENDED_LAYER_SPINE_LOWER : "SPINE_LOWER",
B_EXTENDED_LAYER_SPINE_UPPER : "SPINE_UPPER",
B_EXTENDED_LAYER_ALL : "ALL",

}

B_REFERENCE_POSE_LAYERS = [ \
B_LAYER_VOLUME,
B_LAYER_SL
]

B_DEFAULT_POSE_LAYERS = [ \
B_LAYER_ORIGIN,
B_LAYER_TORSO,
B_LAYER_ARMS,
B_LAYER_LEGS,
B_LAYER_HAND,
B_LAYER_FACE,
]

B_LEGACY_POSE_LAYERS = [ \
B_LAYER_ORIGIN,
B_LAYER_TORSO,
B_LAYER_ARMS,
B_LAYER_LEGS,
]

B_VISIBLE_LAYERS_SL = [ \
B_LAYER_ORIGIN,
B_LAYER_TORSO,
B_LAYER_ARMS,
B_LAYER_LEGS,
B_LAYER_FACE
]

B_VISIBLE_LAYERS_MANUEL = [ \
B_LAYER_TORSO,
B_LAYER_ARMS,
B_LAYER_LEGS,
B_LAYER_HAND,
B_LAYER_EXTRA
]

B_VISIBLE_LAYERS_TAMAGOYAKI =  B_DEFAULT_POSE_LAYERS

B_SIMPLE_POSE_LAYERS = [ \
B_LAYER_ORIGIN,
B_LAYER_TORSO,
B_LAYER_ARMS,
B_LAYER_LEGS,
B_LAYER_EYE_TARGET,
B_LAYER_EYE_ALT_TARGET,
B_LAYER_FACE,
B_LAYER_HAND,
B_LAYER_WING,
B_LAYER_TAIL,
B_LAYER_GROIN,
B_LAYER_SPINE,
B_LAYER_LIMB,
B_LAYER_EXTRA,
]

B_STANDARD_POSE_LAYERS = [ \
B_LAYER_ORIGIN,
B_LAYER_TORSO,
B_LAYER_ARMS,
B_LAYER_LEGS,
B_LAYER_EYE_TARGET,
B_LAYER_EYE_ALT_TARGET,
B_LAYER_ATTACHMENT,
B_LAYER_VOLUME,
B_LAYER_FACE,
B_LAYER_HAND,
B_LAYER_WING,
B_LAYER_TAIL,
B_LAYER_GROIN,
B_LAYER_SPINE,
B_LAYER_LIMB,
B_LAYER_EXTRA,
]

B_SIMPLE_DEFORM_LAYERS = [ \
B_LAYER_DEFORM_FACE,
B_LAYER_DEFORM_HAND,
B_LAYER_DEFORM_WING,
B_LAYER_DEFORM_TAIL,
B_LAYER_DEFORM_GROIN,
B_LAYER_DEFORM_SPINE,
B_LAYER_DEFORM_LIMB,
B_LAYER_DEFORM,
B_LAYER_ORIGIN,
B_LAYER_EYE_TARGET,
B_LAYER_EYE_ALT_TARGET,
]

B_STANDARD_DEFORM_LAYERS = [ \
B_LAYER_DEFORM_FACE,
B_LAYER_DEFORM_HAND,
B_LAYER_DEFORM_WING,
B_LAYER_DEFORM_TAIL,
B_LAYER_DEFORM_GROIN,
B_LAYER_DEFORM_SPINE,
B_LAYER_DEFORM_LIMB,
B_LAYER_DEFORM,
B_LAYER_ORIGIN,
B_LAYER_EYE_TARGET,
B_LAYER_EYE_ALT_TARGET,
B_LAYER_VOLUME,
]

DEFORM_TO_POSE_MAP = {
B_LAYER_ARMS: [B_LAYER_SL,B_LAYER_DEFORM],
B_LAYER_LEGS: [B_LAYER_SL,B_LAYER_DEFORM],
B_LAYER_TORSO: [B_LAYER_SL,B_LAYER_DEFORM],
B_LAYER_FACE: [B_LAYER_DEFORM_FACE,B_LAYER_DEFORM],
B_LAYER_HAND: [B_LAYER_DEFORM_HAND,B_LAYER_DEFORM],
B_LAYER_WING: [B_LAYER_DEFORM_WING,B_LAYER_DEFORM],
B_LAYER_TAIL: [B_LAYER_DEFORM_TAIL,B_LAYER_DEFORM],
B_LAYER_GROIN: [B_LAYER_DEFORM_GROIN,B_LAYER_DEFORM],
B_LAYER_SPINE: [B_LAYER_DEFORM_SPINE,B_LAYER_DEFORM],
B_LAYER_LIMB: [B_LAYER_DEFORM_LIMB,B_LAYER_DEFORM],
B_LAYER_VOLUME: [B_LAYER_VOLUME],
B_LAYER_DEFORM: [B_LAYER_DEFORM]
}

LAYER_MAP = {
    'Origin':     [B_LAYER_ORIGIN],
    'Torso':      [B_LAYER_TORSO],
    'Collision':  [B_LAYER_VOLUME],
    'Extra':      [B_LAYER_EXTRA],
    'Arms':       [B_LAYER_ARMS],
    'Legs':       [B_LAYER_LEGS],
    'IK Arms':    [B_LAYER_IK_ARMS],
    'IK Legs':    [B_LAYER_IK_LEGS],
    'IK Limbs':   [B_LAYER_IK_LIMBS],
    'Structure':  [B_LAYER_STRUCTURE],
    'SL Base':    [B_LAYER_SL],
    'SL Extended':[B_LAYER_EXTENDED],
    'Eye Target': [B_LAYER_EYE_TARGET],
    'Eye Alt Target': [B_LAYER_EYE_ALT_TARGET],
    'Attachment': [B_LAYER_ATTACHMENT],

    'Face':    [B_LAYER_FACE,   B_LAYER_DEFORM_FACE],
    'Lip':     [B_LAYER_FACE,   B_LAYER_DEFORM_FACE],
    'Lips':    [B_LAYER_FACE,   B_LAYER_DEFORM_FACE],
    'Eye':     [B_LAYER_FACE,   B_LAYER_DEFORM_FACE],
    'Eyes':    [B_LAYER_FACE,   B_LAYER_DEFORM_FACE],
    'Mouth':   [B_LAYER_FACE,   B_LAYER_DEFORM_FACE],
    'Nose':    [B_LAYER_FACE,   B_LAYER_DEFORM_FACE],
    'Ear':     [B_LAYER_FACE,   B_LAYER_DEFORM_FACE],
    'Ears':    [B_LAYER_FACE,   B_LAYER_DEFORM_FACE],

    'Hand':    [B_LAYER_HAND,   B_LAYER_DEFORM_HAND],
    'IK Hands':[B_LAYER_IK_HAND],
    'IK Face': [B_LAYER_IK_FACE],
    'Wing':    [B_LAYER_WING,   B_LAYER_DEFORM_WING],
    'Groin':   [B_LAYER_GROIN,  B_LAYER_DEFORM_GROIN],
    'Tail':    [B_LAYER_TAIL,   B_LAYER_DEFORM_TAIL],
    'Limb':    [B_LAYER_LIMB,   B_LAYER_DEFORM_LIMB],
    'Spine':   [B_LAYER_SPINE,  B_LAYER_DEFORM_SPINE],
}

BONESHAPE_MAP = {
    "COG": "CustomShape_COG",
    "Tinker": "CustomShape_Pelvis",
    "Torso": "CustomShape_Torso",
    "Pelvis": "CustomShape_Target",
    "HipLeft": "CustomShape_Circle03",
    "HipRight": "CustomShape_Circle03",
    "CollarLeft": "CustomShape_Collar",
    "CollarRight": "CustomShape_Collar",
    "Chest": "CustomShape_Circle10",
    "Neck": "CustomShape_Neck",
    "Head": "CustomShape_Head",
    "ShoulderLeft": "CustomShape_Circle03",
    "ShoulderRight": "CustomShape_Circle03",
    "ElbowLeft": "CustomShape_Circle03",
    "ElbowRight": "CustomShape_Circle03",
    "WristLeft": "CustomShape_Circle10",
    "WristRight": "CustomShape_Circle10",
    "KneeLeft": "CustomShape_Circle03",
    "KneeRight": "CustomShape_Circle03",
    "AnkleLeft": "CustomShape_Circle05",
    "AnkleRight": "CustomShape_Circle05",
    "HindLimb1Right": "CustomShape_Circle03",
    "HindLimb1Left": "CustomShape_Circle03",
    "HindLimb2Right": "CustomShape_Circle03",
    "HindLimb2Left": "CustomShape_Circle03",
    "HindLimb3Right": "CustomShape_Circle05",
    "HindLimb3Left": "CustomShape_Circle05",
    "FaceLipLowerLeft": "CustomShape_Face",
    "FaceLipLowerCenter": "CustomShape_Face",
    "FaceLipLowerRight": "CustomShape_Face",
    "FaceLipCornerLeft": "CustomShape_Face",
    "FaceLipCornerRight": "CustomShape_Face",
    "FaceLipUpperLeft": "CustomShape_Face",
    "FaceLipUpperCenter": "CustomShape_Face",
    "FaceLipUpperRight": "CustomShape_Face",
    "FaceCheekLowerLeft": "CustomShape_Face",
    "FaceCheekLowerRight": "CustomShape_Face",
    "FaceCheekUpperLeft": "CustomShape_Face",
    "FaceCheekUpperRight": "CustomShape_Face",
    "FaceNoseBase": "CustomShape_Face",
    "FaceNoseCenter": "CustomShape_Face",
    "FaceNoseBridge": "CustomShape_Face",
    "FaceNoseLeft": "CustomShape_Face",
    "FaceNoseRight": "CustomShape_Face",
    "FaceForeheadLeft": "CustomShape_Face",
    "FaceForeheadCenter": "CustomShape_Face",
    "FaceForeheadRight": "CustomShape_Face",
    "FaceEyebrowOuterLeft": "CustomShape_Face",
    "FaceEyebrowOuterRight": "CustomShape_Face",
    "FaceEyebrowCenterLeft": "CustomShape_Face",
    "FaceEyebrowCenterRight": "CustomShape_Face",
    "FaceEyebrowInnerLeft": "CustomShape_Face",
    "FaceEyebrowInnerRight": "CustomShape_Face",
    "FaceEyeLidUpperLeft": "CustomShape_Face",
    "FaceEyeLidUpperRight": "CustomShape_Face",
    "FaceEyeLidLowerLeft": "CustomShape_Face",
    "FaceEyeLidLowerRight": "CustomShape_Face",
    "FaceEyecornerInnerLeft": "CustomShape_Face",
    "FaceEyecornerInnerRight": "CustomShape_Face",
    "FaceChin": "CustomShape_Face",

    "mFaceLipLowerLeft": "CustomShape_Face",
    "mFaceLipLowerCenter": "CustomShape_Face",
    "mFaceLipLowerRight": "CustomShape_Face",
    "mFaceLipCornerLeft": "CustomShape_Face",
    "mFaceLipCornerRight": "CustomShape_Face",
    "mFaceLipUpperLeft": "CustomShape_Face",
    "mFaceLipUpperCenter": "CustomShape_Face",
    "mFaceLipUpperRight": "CustomShape_Face",
    "mFaceCheekLowerLeft": "CustomShape_Face",
    "mFaceCheekLowerRight": "CustomShape_Face",
    "mFaceCheekUpperLeft": "CustomShape_Face",
    "mFaceCheekUpperRight": "CustomShape_Face",
    "mFaceNoseBase": "CustomShape_Face",
    "mFaceNoseCenter": "CustomShape_Face",
    "mFaceNoseBridge": "CustomShape_Face",
    "mFaceNoseLeft": "CustomShape_Face",
    "mFaceNoseRight": "CustomShape_Face",
    "mFaceForeheadLeft": "CustomShape_Face",
    "mFaceForeheadCenter": "CustomShape_Face",
    "mFaceForeheadRight": "CustomShape_Face",
    "mFaceEyebrowOuterLeft": "CustomShape_Face",
    "mFaceEyebrowOuterRight": "CustomShape_Face",
    "mFaceEyebrowCenterLeft": "CustomShape_Face",
    "mFaceEyebrowCenterRight": "CustomShape_Face",
    "mFaceEyebrowInnerLeft": "CustomShape_Face",
    "mFaceEyebrowInnerRight": "CustomShape_Face",
    "mFaceEyeLidUpperLeft": "CustomShape_Face",
    "mFaceEyeLidUpperRight": "CustomShape_Face",
    "mFaceEyeLidLowerLeft": "CustomShape_Face",
    "mFaceEyeLidLowerRight": "CustomShape_Face",
    "mFaceEyecornerInnerLeft": "CustomShape_Face",
    "mFaceEyecornerInnerRight": "CustomShape_Face",
    "mFaceChin": "CustomShape_Face",

    "ThumbControllerLeft"  : "CustomShape_COG",
    "ThumbControllerRight" : "CustomShape_COG",

}


BONEGROUP_MAP_THEME = 0
BONEGROUP_MAP_LAYERS = 1

BONEGROUP_MAP = {

    'Origin'         : ['THEME12', [B_LAYER_ORIGIN]         ],
    'SL Base'        : ['THEME04', [B_LAYER_SL]             ], # blues
    'SL Extended'    : ['THEME11', [B_LAYER_EXTENDED]       ], # purples
    'Structure'      : ['THEME08', [B_LAYER_STRUCTURE]      ],
    'Handstructure'  : ['THEME08', [B_LAYER_STRUCTURE, B_LAYER_HAND]],
    'Custom'         : ['THEME12', [B_LAYER_EXTENDED]       ],
    'Eye Target'     : ['THEME12', [B_LAYER_EYE_TARGET]     ],
    'Eye Alt Target' : ['THEME12', [B_LAYER_EYE_ALT_TARGET] ],
    'IK Arms'        : ['THEME09', [B_LAYER_IK_ARMS]        ], # yellows
    'IK Legs'        : ['THEME09', [B_LAYER_IK_LEGS]        ], # yellows
    'IK Limbs'       : ['THEME09', [B_LAYER_IK_LIMBS]       ], # yellows
    'IK Face'        : ['THEME09', [B_LAYER_IK_FACE]        ], # yellows

    'Attachment'     : ['THEME01', [B_LAYER_ATTACHMENT]     ], # reds
    'Collision'      : ['THEME02', [B_LAYER_VOLUME]         ], # oranges

    'Torso'          : ['THEME12', [B_LAYER_TORSO]          ],
    'Arms'           : ['THEME12', [B_LAYER_ARMS]           ],
    'Legs'           : ['THEME12', [B_LAYER_LEGS]           ],
    'Extra'          : ['THEME12', [B_LAYER_EXTRA]          ],
    'Face'        : ['THEME12', [B_LAYER_FACE]           ], #extended bones are light green
    'Hand'        : ['THEME12', [B_LAYER_HAND]           ],
    'Wing'        : ['THEME12', [B_LAYER_WING]           ],
    'Tail'        : ['THEME12', [B_LAYER_TAIL]           ],
    'Groin'       : ['THEME12', [B_LAYER_GROIN]          ],
    'Eye'         : ['THEME12', [B_LAYER_FACE]           ],
    'Eyes'        : ['THEME02', [B_LAYER_FACE]           ], #compatibility thing
    'Ear'         : ['THEME12', [B_LAYER_FACE]           ],
    'Ears'        : ['THEME14', [B_LAYER_FACE]           ], #compatibility thing
    'Lip'         : ['THEME12', [B_LAYER_FACE]           ],
    'Lips'        : ['THEME01', [B_LAYER_FACE]           ], #compatibility thing
    'Mouth'       : ['THEME13', [B_LAYER_FACE]           ],
    'Nose'        : ['THEME11', [B_LAYER_FACE]           ],
    'Limb'        : ['THEME12', [B_LAYER_LIMB]           ],
    'Spine'       : ['THEME03', [B_LAYER_SPINE]          ],

    'mTorso'         : ['THEME04', [B_LAYER_SL,           B_LAYER_DEFORM] ],
    'mArms'          : ['THEME04', [B_LAYER_SL,           B_LAYER_DEFORM] ],
    'mLegs'          : ['THEME04', [B_LAYER_SL,           B_LAYER_DEFORM] ],
    'mExtra'         : ['THEME04', [B_LAYER_SL,           B_LAYER_DEFORM] ],

    'mFace'       : ['THEME11', [B_LAYER_DEFORM_FACE,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ], #extended bones are purple
    'mHand'       : ['THEME11', [B_LAYER_DEFORM_HAND,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mWing'       : ['THEME11', [B_LAYER_DEFORM_WING,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mTail'       : ['THEME11', [B_LAYER_DEFORM_TAIL,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mGroin'      : ['THEME11', [B_LAYER_DEFORM_GROIN, B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mEye'        : ['THEME11', [B_LAYER_DEFORM_FACE,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mEar'        : ['THEME11', [B_LAYER_DEFORM_FACE,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mLip'        : ['THEME11', [B_LAYER_DEFORM_FACE,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mEyes'       : ['THEME11', [B_LAYER_DEFORM_FACE,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mEars'       : ['THEME11', [B_LAYER_DEFORM_FACE,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mLips'       : ['THEME11', [B_LAYER_DEFORM_FACE,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mMouth'      : ['THEME11', [B_LAYER_DEFORM_FACE,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mNose'       : ['THEME11', [B_LAYER_DEFORM_FACE,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mLimb'       : ['THEME11', [B_LAYER_DEFORM_LIMB,  B_LAYER_EXTENDED, B_LAYER_DEFORM] ],
    'mSpine'      : ['THEME11', [B_LAYER_DEFORM_SPINE, B_LAYER_EXTENDED, B_LAYER_DEFORM] ]
}


GENERATE_SKELETON_DATA = os.path.join(DATAFILESDIR, "avatar_skeleton.xml")

SLBONES = sym(["mHead", "mNeck" ,"mCollar.", "mShoulder.", "mElbow.",
               "mWrist.", "mChest", "mTorso", "mPelvis", "mHip.",
               "mKnee.", "mAnkle.", "mFoot."])

SL_EYE_BONES  = sym(["mEye."])
SL_ALT_EYE_BONES = sym(["mFaceEyeAlt."])
SL_ALL_EYE_BONES = SL_EYE_BONES + SL_ALT_EYE_BONES
SL_SPINE_LOWER_BONES = ["mSpine1", "mSpine2"]
SL_SPINE_UPPER_BONES = ["mSpine3", "mSpine4"]
SL_SPINE_BONES = SL_SPINE_UPPER_BONES + SL_SPINE_LOWER_BONES

SLATTACHMENTS = ["aSkull", "aChin", "aRight Ear", "aLeft Ear", "aRight Eyeball",
               "aLeft Eyeball", "aNose", "aMouth", "aNeck", "aRight Shoulder",
               "aLeft Shoulder", "aR Upper Arm", "aL Upper Arm", "aR Forearm",
               "aL Forearm", "aRight Hand", "aLeft Hand", "aRight Pec", "aLeft Pec",
               "aChest", "aSpine", "aStomach", "aAvatar Center", "aRight Hip",
               "aLeft Hip", "aPelvis", "aR Upper Leg", "aL Upper Leg",
               "aR Lower Leg", "aL Lower Leg", "aRight Foot", "aLeft Foot",
               "aLeft Ring Finger", "aRight Ring Finger",
               "aTail Base", "aTail Tip",
               "aLeft Wing", "aRight Wing",
               "aAlt Left Ear", "aAlt Right Ear",
               "aAlt Left Eye", "aAlt Right Eye",
               "aJaw", "aTongue", "aGroin"
               ]

SLSHAPEVOLBONES = ["UPPER_BACK", "LOWER_BACK", "LEFT_PEC", "RIGHT_PEC", "LEFT_HANDLE", "RIGHT_HANDLE", "BUTT"]

SLOPTBONES.extend(SL_LEAF_BONES+SL_EYE_BONES)
SLVOLBONES.extend(SLSHAPEVOLBONES)
SLBASEBONES   = SLOPTBONES+SLBONES
SLALLBONES    = SLBASEBONES+SLATTACHMENTS+SLVOLBONES
REGULAR_BONES = ['Origin', 'Tinker','COG', '_EyeTarget', '_CollarLinkRight', '_CollarLinkLeft']
HOVER_POINTS  = ['COG', 'Pelvis', 'mPelvis']

SLMAP = 'SL'
MANUELMAP = 'MANUELLAB'
GENERICMAP = 'GENERIC'
TAMAGOYAKIMAP = 'TAMAGOYAKI'

MANUEL2Tamagoyaki = {
"upperarm_L" : "ShoulderLeft",
"upperarm_R" : "ShoulderRight",
"lowerarm_L" : "ElbowLeft",
"lowerarm_R" : "ElbowRight",
"hand_L"     : "WristLeft",
"hand_R"     : "WristRight",
"thumb01_L"  : "HandThumb1Left",
"thumb02_L"  : "HandThumb2Left",
"thumb03_L"  : "HandThumb3Left",
"thumb01_R"  : "HandThumb1Right",
"thumb02_R"  : "HandThumb2Right",
"thumb03_R"  : "HandThumb3Right",
"index01_L"  : "HandIndex1Left",
"index02_L"  : "HandIndex2Left",
"index03_L"  : "HandIndex3Left",
"index01_R"  : "HandIndex1Right",
"index02_R"  : "HandIndex2Right",
"index03_R"  : "HandIndex3Right",
"middle01_L" : "HandMiddle1Left",
"middle02_L" : "HandMiddle2Left",
"middle03_L" : "HandMiddle3Left",
"middle01_R" : "HandMiddle1Right",
"middle02_R" : "HandMiddle2Right",
"middle03_R" : "HandMiddle3Right",
"ring01_L"   : "HandRing1Left",
"ring02_L"   : "HandRing2Left",
"ring03_L"   : "HandRing3Left",
"ring01_R"   : "HandRing1Right",
"ring02_R"   : "HandRing2Right",
"ring03_R"   : "HandRing3Right",
"pinky01_L"  : "HandPinky1Left",
"pinky02_L"  : "HandPinky2Left",
"pinky03_L"  : "HandPinky3Left",
"pinky01_R"  : "HandPinky1Right",
"pinky02_R"  : "HandPinky2Right",
"pinky03_R"  : "HandPinky3Right",
"clavicle_L" : "CollarLeft",
"clavicle_R" : "CollarRight",
"neck"       : "Neck",
"spine02"    : "Torso",
"spine03"    : "Chest",
"head"       : "Head",
"thigh_L"    : "HipLeft",
"thigh_R"    : "HipRight",
"calf_L"     : "KneeLeft",
"calf_R"     : "KneeRight",
"pelvis"     : "Pelvis",
"foot_L"     : "AnkleLeft",
"foot_R"     : "AnkleRight",
"toes_L"     : "FootLeft",
"toes_R"     : "FootRight",
"chest"      : "Chest",
"breast_R"   : "RIGHT_PEC",
"breast_L"   : "LEFT_PEC",
}

MANUEL_UNSUPPORTED = {
"spine01"    : "Pelvis",
"root"       : "Origin",
"index00_L"  : "WristLeft",
"index00_R"  : "WristRight",
"middle00_L" : "WristLeft",
"middle00_R" : "WristRight",
"ring00_L"   : "WristLeft",
"ring00_R"   : "WristRight",
"pinky00_L"  : "WristLeft",
"pinky00_R"  : "WristRight",
}

def map_sl_to_Tamagoyaki(SourceBonename, type=SLMAP, all=True):
    if type == MANUELMAP:
        result = MANUEL2Tamagoyaki.get(SourceBonename, MANUEL_UNSUPPORTED.get(SourceBonename, None) if all else None)
        return result

    if SourceBonename[0]=='m':
        result = SourceBonename[1:]
    elif 'm'+SourceBonename in SLBASEBONES:
        result = SourceBonename
    elif 'a'+SourceBonename in SLATTACHMENTS:
        result = 'a'+SourceBonename
    else:
        result = SourceBonename


    return result

def map2SL(armobj, SourceBonename):
    if SourceBonename[0]!='m' and 'm'+SourceBonename in armobj.data.bones:
        SourceBonename = 'm' + SourceBonename

    return SourceBonename

MANUEL_CUSTOM_SHAPE_SCALES = {
    "Head"           : 0.5,
    "Neck"           : 0.5,
    "CollarLeft"     : 0.5,
    "CollarRight"    : 0.5,
    "WristLeft"      : 2.0,
    "WristRight"     : 2.0,
    "Chest"          : 0.8,
    "Torso"          : 0.7,
    "Tinker"      : 0.8,
    "KneeLeft"       : 0.8,
    "KneeRight"      : 0.8,
    "AnkleLeft"      : 0.7,
    "AnkleRight"     : 0.7,
    "ikWristRight"   : 2.0,
    "ikWristLeft"    : 2.0,
    "ikFaceLipShape" : 0.4
}

def adjust_custom_shape(pbone, armature_type):

    if armature_type == MANUELMAP:
        scale = MANUEL_CUSTOM_SHAPE_SCALES.get(pbone.name, 1.0)
        try:
            pbone.custom_shape_scale = scale
        except:
            print("Can not fix Custom Shape scale (not supported in this Version of Blender")

BONEMAP_EXTENDED_TO_BASIC = {
    'mFace.*'       : 'mHead',
    'mTail.*'       : 'mPelvis',
    'mHand.*Left'   : 'mWristLeft',
    'mHand.*Right'  : 'mWristRight',
    'mEyeAlt.*Left' : 'mEyeLeft',
    'mEyeAlt.*Right': 'mEyeRight',
    'mWing.*'       : 'mTorso'
}

def get_export_bonename(groups, group, target_system):

    if group >= len(groups):
        return None

    vgroup = groups[group]
    if not vgroup:
        return None

    bonename = vgroup.name
    if target_system != 'BASIC' or bonename in SLALLBONES:
        return bonename

    for key in BONEMAP_EXTENDED_TO_BASIC:
        if re.search(key, bonename):
            mappedname = BONEMAP_EXTENDED_TO_BASIC[key]

            bonename = mappedname
            break

    return bonename if bonename in SLALLBONES else None


MAX_EXPORT_BONES = 110

UI_SIMPLE   = 0
UI_STANDARD = 1
UI_ADVANCED = 2
UI_EXPERIMENTAL = 3




custom_icons = None
def register_icons():
    global custom_icons

    if custom_icons:
        return #Already registered

    custom_icons = bpy.utils.previews.new()
    custom_icons.load("eyec", os.path.join(ICONS_DIR, "eyec.png"), 'IMAGE')
    custom_icons.load("eye", os.path.join(ICONS_DIR, "eye.png"), 'IMAGE')
    custom_icons.load("aeye", os.path.join(ICONS_DIR, "aeye.png"), 'IMAGE')
    custom_icons.load("beye", os.path.join(ICONS_DIR, "beye.png"), 'IMAGE')
    custom_icons.load("aeyec", os.path.join(ICONS_DIR, "aeyec.png"), 'IMAGE')
    custom_icons.load("ceyec", os.path.join(ICONS_DIR, "ceyec.png"), 'IMAGE')
    custom_icons.load("ceye", os.path.join(ICONS_DIR, "ceye.png"), 'IMAGE')
    custom_icons.load("veyec", os.path.join(ICONS_DIR, "veyec.png"), 'IMAGE')
    custom_icons.load("veye", os.path.join(ICONS_DIR, "veye.png"), 'IMAGE')
    custom_icons.load("ieyec", os.path.join(ICONS_DIR, "ieyec.png"), 'IMAGE')
    custom_icons.load("ieye", os.path.join(ICONS_DIR, "ieye.png"), 'IMAGE')
    custom_icons.load("cbone", os.path.join(ICONS_DIR, "cbone.png"), 'IMAGE')
    custom_icons.load("meyec", os.path.join(ICONS_DIR, "meyec.png"), 'IMAGE')
    custom_icons.load("meye", os.path.join(ICONS_DIR, "meye.png"), 'IMAGE')
    custom_icons.load("mbone", os.path.join(ICONS_DIR, "mbone.png"), 'IMAGE')
    custom_icons.load("vbone", os.path.join(ICONS_DIR, "vbone.png"), 'IMAGE')
    custom_icons.load("ebone", os.path.join(ICONS_DIR, "ebone.png"), 'IMAGE')
    custom_icons.load("cbones", os.path.join(ICONS_DIR, "cbones.png"), 'IMAGE')
    custom_icons.load("mbones", os.path.join(ICONS_DIR, "mbones.png"), 'IMAGE')
    custom_icons.load("vbones", os.path.join(ICONS_DIR, "vbones.png"), 'IMAGE')
    custom_icons.load("ebones", os.path.join(ICONS_DIR, "ebones.png"), 'IMAGE')
    custom_icons.load("fbones", os.path.join(ICONS_DIR, "fbones.png"), 'IMAGE')
    custom_icons.load("xbones", os.path.join(ICONS_DIR, "xbones.png"), 'IMAGE')
    custom_icons.load("alock", os.path.join(ICONS_DIR, "alock.png"), 'IMAGE')
    custom_icons.load("elock", os.path.join(ICONS_DIR, "elock.png"), 'IMAGE')
    custom_icons.load("mlock", os.path.join(ICONS_DIR, "mlock.png"), 'IMAGE')
    custom_icons.load("aunlock", os.path.join(ICONS_DIR, "aunlock.png"), 'IMAGE')
    custom_icons.load("eunlock", os.path.join(ICONS_DIR, "eunlock.png"), 'IMAGE')
    custom_icons.load("munlock", os.path.join(ICONS_DIR, "munlock.png"), 'IMAGE')
    custom_icons.load("retarget", os.path.join(ICONS_DIR, "retarget.png"), 'IMAGE')
    custom_icons.load("defaultshape", os.path.join(ICONS_DIR, "shape_default.png"), 'IMAGE')
    custom_icons.load("baseshape", os.path.join(ICONS_DIR, "shape_base.png"), 'IMAGE')
    custom_icons.load("defaultmale", os.path.join(ICONS_DIR, "shape_male_default.png"), 'IMAGE')
    custom_icons.load("basemale", os.path.join(ICONS_DIR, "shape_male_base.png"), 'IMAGE')
    custom_icons.load("female", os.path.join(ICONS_DIR, "female.png"), 'IMAGE')
    custom_icons.load("male", os.path.join(ICONS_DIR, "male.png"), 'IMAGE')
    custom_icons.load("limit", os.path.join(ICONS_DIR, "limit.png"), 'IMAGE')
    custom_icons.load("optimize", os.path.join(ICONS_DIR, "optimize.png"), 'IMAGE')
    custom_icons.load("suzi", os.path.join(ICONS_DIR, "suzi.png"), 'IMAGE')
    custom_icons.load("bindshape", os.path.join(ICONS_DIR, "shape_bind.png"), 'IMAGE')
    custom_icons.load("bindshapemale", os.path.join(ICONS_DIR, "shape_male_bind.png"), 'IMAGE')
    custom_icons.load("rightside", os.path.join(ICONS_DIR, "right_side.png"), 'IMAGE')
    custom_icons.load("leftside", os.path.join(ICONS_DIR, "left_side.png"), 'IMAGE')
    custom_icons.load("modified", os.path.join(ICONS_DIR, "modified.png"), 'IMAGE')
    custom_icons.load("warningdot", os.path.join(ICONS_DIR, "warningdot.png"), 'IMAGE')



def unregister_icons():
    global custom_icons
    if custom_icons:
        bpy.utils.previews.remove(custom_icons)

def get_sys_icon(key):
    return bpy.types.UILayout.bl_rna.functions['prop'].parameters['icon'].enum_items[key].value

def get_icon(key):
    global custom_icons
    if not custom_icons:
        register_icons()
    icon = get_cust_icon(key)
    return icon if icon else get_sys_icon(key)

def get_cust_icon(key, default=None):
    global custom_icons
    if not custom_icons:
        register_icons()
    icon = custom_icons.get(key)
    if not icon:
        return default
    return icon.icon_id

eye_icons = {
   'animation' : 'ceye',
   'deform'    : 'meye',
   'ik'        : 'ieye',
   'volume'    : 'veye',
   'attachment': 'aeye',
   'extended'  : 'beye',
   'SL'        : 'meye',
   'EXT'       : 'beye',
   'VOL'       : 'veye',
   'POS'       : 'ceye',
   'MAP'       : 'ceye'
}

def visIcon(armobj, layer, type=None):
    closed_eye = bpy.types.UILayout.bl_rna.functions['prop'].parameters['icon'].enum_items[ICON_HIDE_ON].value
    if type == None or not armobj.data.layers[layer]:
        return closed_eye

    key = eye_icons.get(type)
    val = get_cust_icon(key)
    return val if val else closed_eye

def get_eye_icon(key, enabled):
    return get_cust_icon(key) if enabled else get_sys_icon('RESTRICT_VIEW_ON')




sl_bone_rolls = BoolProperty(
    name="Enforce SL Bone Roll",
    description = "Ensure that the bone Rolls are defined according to the SL Skeleton Specification\n\nNote:\nThis can be good for cleaning up (human) devkits.\nUsage with non human skeletons may cause damage!",
    default     = False
)

GJointTypeItems = [
    ('POS',   'Pos' ,    'Create a rig based on the pos values from the avatar skeleton definition\nFor making Cloth Textures for the System Character (for the paranoid user)'),
    ('PIVOT', 'Pivot'  , 'Create a rig based on the pivot values from the avatar skeleton definition\nFor Creating Mesh items (usually the correct choice)')
]

GJointType = EnumProperty(
    items = GJointTypeItems,
    name="Joint Type",
    description= "SL supports 2 Skeleton Defintions.\n\n- The POS definition is used for the System Avatar (to make cloth).\n- The PIVOT definition is used for mesh characters\n\nAttention: You need to use POS if your Devkit was made with POS\nor when you make cloth for the System Avatar",
    default='PIVOT')

GSkeletonTypeItems = [
    ('TAMAGOYAKI', 'Avatar'  , 'Create a rig for Standard Avatars  (human or creature)'),
    ('ANIMESH', 'Animesh' , 'Create a rig for Animesh characters(human or creature)')
]

GSkeletonType = EnumProperty(
    items=GSkeletonTypeItems,
    name="Skeleton Type",
    description=\
'''The Skeleton type can be:
- TAMAGOYAKI (default, good for Avatars of any kind)
- ANIMESH (only useful for Animesh development) ''',
    default='TAMAGOYAKI'
)

g_apply_pose = BoolProperty(
    name="Apply Pose",
    default=False,
    description=\
'''Apply pose of source rig to character mesh(es) before Update/Transfer the rig.

You want to enable this option if

- Either the current pose is not the Restpose
- Or you update from a rig version < 5
- Or updating the rig with that option turned off moves meshes out of place'''
)

g_apply_armature_on_unbind = BoolProperty(
    default     = False,
    name        = "Apply Pose",
    description = "Apply the visual Pose to selected Meshes before unbinding"
)

g_snap_control_to_rig = BoolProperty(
    name        = "snap_control_to_rig",
    description = SceneProp_snap_control_to_rig_description,
    default     = False
)

g_store_as_bind_pose = BoolProperty(
    name        = "Store as Bind Pose",
    description = SceneProp_store_as_bind_pose_description,
    default     = False
)

g_handleTargetMeshSelection = EnumProperty(
    items=(
        ('KEEP',   'Keep', 'Keep Tamagoyaki Meshes in Target Armature(s)'),
        ('HIDE',   'Hide', 'Hide Tamagoyaki meshes in Target Armature(s)'),
        ('DELETE', 'Delete', 'Delete Tamagoyaki Meshes from Target Armature(s)')),
    name="Original",
    description="How to treat the Tamagoyaki Meshes in the Target Armature(s)",
    default='DELETE'
)

g_up_axis = EnumProperty(
    items = (
        ('Y', 'Y Up', 'Imported Rig Y Axis points upwards'),
        ('Z', 'Z Up', 'Imported Rig Z Axis points upwards')
    ),
    name = "Axis",
    description = UpdateRigProp_up_axis_text,
    default='Z'
)

g_reset_shape_sliders = BoolProperty(
    default = False,
    name = "Rebase Sliders",
    description = \
'''The Restpose will be used as the new Neutral Slider shape (White stickman)
Note: When you wear the mesh in SL you will want to use a default shape'''
)

g_applyRotation = BoolProperty(
    default=True,
    name="Apply Rot&Scale",
    description= \
'''Apply Scale & Rotation to the rigged Mesh objects.
Note: use this only if the Rig contains meshes
with inconsistent rotations and scales'''
)

g_appearance_editable = BoolProperty(
    name = "Lock Avatar Shape",
    default = True,
    description= "Make the Avatar shape read only, Sliders are locked with their current value\n\n"\
               + "Note:\n"
               + "When you select the Animesh Preset (White Stickman)\n"
               + "the Avatar shape are automatically locked\n"
               + "However you always can unlock even when you selected Animesh mode"
                    )


g_use_male_shape = BoolProperty(
    default=False,
    name="Male Sliders",
    description= \
'''Use the Male Gender for Sliders
Note: Most SL Rigs are created based on the female Skeleton.
However most custom male bodies still use the Male Sliders In SL.

Tip: For Male custom meshes you will probably ENABLE this option.
However for male models you probably also need to
disable 'Use Male Skeleton' (see below) '''
)


g_use_male_skeleton = BoolProperty(
    default=False,
    name="Male Skeleton",
    description= \
'''Use the Male skeleton for binding.
Note: Most SL Rigs are created based on the female Skeleton.

Tip: For the majority of custom meshes (male or female)
you probably need to keep this option DISABLED.
However for Male models you probably want to
enable 'Use Male Sliders' (see above) '''
)


g_srcRigType = EnumProperty(
    items=(
        (SLMAP,      SLMAP,      'Second Life Base Rig\n\nWe assume the character looks towards positive X\nwhich means it looks to the right side when in front view'),
        (MANUELMAP,  MANUELMAP,  'Manuel Bastioni Rig\n\nWe assume the character has been imported directly from Manuellab and has not changed.'),
        (GENERICMAP, GENERICMAP, 'Generic Rig\n\nWe assume the character looks towards negative Y\nwhich means it looks at you when in Front view'),
	(TAMAGOYAKIMAP, TAMAGOYAKIMAP, 'Tamagoyaki Rig\n\nThe character is already rigged to an Tamagoyaki or Tamagoyaki Rig\nNote: Do not use this option unless you have been instructed to set it'),
        (TAMAGOYAKIMAP, TAMAGOYAKIMAP, 'Avastar Rig\n\nThe character is already rigged to an Avastar or Tamagoyaki Rig\nNote: Do not use this option unless you have been instructed to set it'),

    ),
    name="Source Rig",
    description="Rig Type of the active Object, can be TAMAGOYAKI, MANUELLAB, SL or Generic",
    default='SL'
)

g_tgtRigType = EnumProperty(
    items=(
        ('BASIC',       'Basic', 'Second Life Base Rig\n\nWe only create the 26 legacy bones, the volume bones and the attachment bones, all for the old fashioned "classic" Rig'),
        ('EXTENDED', 'Extended', 'Second Life Extended Rig\n\nCreate a rig compatibvle to the new SL boneset (Bento)')
    ),
    name="Target Rig",
    description="Rig Type of the target Object\n\nBasic: 26 Bones + 26 Volume bones (the classic SL rig)\nExtended: The full Boneset of the new SL Bento Rig",
    default='EXTENDED'
)

weight_source_items_for_bind = [
    ('NONE',       'Preserve Weights',     'Do not touch weight Groups (keep existing weight groups untouched)'),
    ('EMPTY',      'Create Empty Groups',  'Add empty weight groups (keep existing weight groups untouched)'),
    ('AUTOMATIC',  'Automatic from Bones', 'Generate weights from Bones (most commonly used, works out of the box)'),
    ('COPY',       'Copy from Meshes',     'Copy weights from Meshes parented to same Armature.\nSelect the source meshes from the Weight sources list below')
]

weight_source_items_for_copy = [
    ('EMPTY',      'Create Empty Groups',  'Add empty weight groups (keep existing weight groups untouched)'),
    ('AUTOMATIC',  'Automatic from Bones', 'Generate weights from Bones (most commonly used, works out of the box)'),
    ('COPY',       'Copy from Meshes',     'Copy weights from Meshes parented to same Armature.\nSelect the source meshes from the Weight sources list below'),
    ('FACEGEN', 'Face Map Generator',    'Generate Head Weight Maps. Works only on head bones (face bones)!.\nPlease use the Operator panel to tweak the values!\nHandle with care')
]

g_weightSourceSelection = EnumProperty(
    items=weight_source_items_for_copy,
    name="Method",
    description="From where to get the weight data",
    default='AUTOMATIC')

g_bindSourceSelection = EnumProperty(
    items=weight_source_items_for_bind,
    name="Method",
    description="From where to get the weight data",
    default='COPY')


g_apply_as_bindshape = BoolProperty(name="Apply Bindshape",
    description = \
'''Replace original Bindshape by current Bindshape

Note: Take care here!

The original bindshape will be permanently
replaced by the current bindshape''',
    default=False)


g_weightBoneSelection = EnumProperty(
    items=(
        ('SELECTED',
            'Selected enabled Deform Bones',
            'Create weights for all Selected Deform Bones'),
        ('VISIBLE',
            'Visible enabled Deform Bones',
            'Create Weights for all Visible Bones\nNote: Please add All Extended (Bento) Bones\nwhich might affect the weights of the visible bones'),
        ('ALL',
            'Enabled Deform Bones',
            'Create weights for all enabled Deform Groups\n'\
        +'Note: You must select at least one of the bone groups\n'\
        +'from the list of enabled Deform Groups')
        ),
    name="For",
    description="The set of bones used for generating the target weight maps.\n\n"\
                +"Notes:\n"\
                +"* This selection specifies the set of possibly generated Target maps.\n"\
                +"* This selection depends on the set of enabled Deform Groups.\n"\
                +"* The set of finally generated target maps also depends on the Mesh topology\n"\
                ,
    default='SELECTED')

g_save_shape_selection = EnumProperty(
    items=(
        ('FILE', 'File',      'Export Shape to Disk'),
        ('DATA', 'Textblock', "Export Shape to textblock (view with Blender's Text Editor)")),
    name="Store Type",
    description="Store Shape data in a File or in a Textblock (view with Blender's Text editor)",
    default='FILE')


g_break_parenting_on_unbind = BoolProperty(
            name        = "break Parenting",
            default     = True,
            description = "When Unbinding also move the Object out of the Parent-Child hierarchy of the Armature")


g_spkg_filter_boundary_verts = BoolProperty(
    name="Only align boundary Verts",
    default=True,
    description="Only process verts on boundary edges (edges which belong only to one face)\nBeware: Disabling this option is slow for large meshes"
)

g_spkg_filter_smooth_faces = BoolProperty(
    name="Only align smooth Faces",
    default=True,
    description="Only align verts for Faces with Smooth Shading enabled\n"
)

g_clearTargetWeights = BoolProperty(
            name="Clear Target Maps",
            default=True,
            description="Make sure the target Weight maps are empty before Copying the weights to them\n"\
                       +"Note: Only target weight maps are affected. All other weight maps remain unchanged.\n"\
                       +"This option is disabled on purpose when you enable the Selected verts option")

g_smoothTargetWeights = BoolProperty(
            name="Smooth weights",
            default = True,
            description = "Smooth weightmaps after weighting")


g_reference_frame = IntProperty(name='Reference Frame',
                  min=0,
                  default=0,
                  description= "In the reference frame the poses of the source and the target match best to each other.\n"
                             + "We need this match pose to find the correct translations\n"
                             + "between the source animation and the target animation"
                  )


msg_too_many_bones = 'Max Bonecount(32) exceeded|'\
                +  'DETAIL:\n'\
                +  'This animation uses %d bones, while in SL the maximum number\n'\
                +  'of bones per animation sequence is limitted to 32.\n'\
                +  'You possibly run into this problem when you first \n'\
                +  'select all bones and then add a keyframe.\n\n'\
                +  'YOUR ACTION:\n'\
                +  'Remove unnecessary bones from the animation (use the Dopesheet)\n'\
                +  'or split the animation into 2 or more separate animations\n'\
                +  'and run the animations in parallel in the target system.|'


g_use_restpose = BoolProperty(name="Use Restpose",
               default=True,
               description = "Assume the restpose of the source armature\n"
                           + "matches best to the current pose of the target armature.\n"
                           + "Hint:Enable this option when you import animations\n"
                           + "which have been made for SL"
               )


g_keep_reference_frame = BoolProperty(
                   name="Keep Reference frame",
                   default=False,
                   description="Often the first frame of a BVH Animation is only a control frame.\n"\
                              +"However You may want to keep this frame for debugging purposes"
                   )






IKNAME = "AVA IK"
TARGETLESS_NAME = "AVA TargetlessIK"
LIMIT_ROTATION_NAME = "AVA Limit Rotation"
STRETCHTO_NAME = "AVA Stretch To"
COPY_ROTATION_NAME = "AVA Copy Rotation"
COPY_LOCATION_NAME = "AVA Copy Location"
COPY_SCALE_NAME = "AVA Copy Scale"





SHAPEUI = OrderedDict()
SHAPEUI["Body"] = [ "male_80", "height_33", "thickness_34", "body_fat_637"]
SHAPEUI["Head"] = [ "head_size_682", "squash_stretch_head_647", "head_shape_193", "egg_head_646", "head_length_773", "face_shear_662", "forehead_angle_629", "big_brow_1", "puffy_upper_cheeks_18", "sunken_cheeks_10", "high_cheek_bones_14"]
SHAPEUI["Eyes"] = [ "eye_size_690", "wide_eyes_24", "eye_spacing_196", "eyelid_corner_up_650", "eyelid_inner_corner_up_880", "eye_depth_769", "upper_eyelid_fold_21", "baggy_eyes_23", "puffy_lower_lids_765", "eyelashes_long_518", "pop_eye_664"]
SHAPEUI["Ears"] = [ "big_ears_35", "ears_out_15", "attached_earlobes_22", "pointy_ears_796"]
SHAPEUI["Nose"] = [ "nose_big_out_2", "wide_nose_517", "broad_nostrils_4", "low_septum_nose_759", "bulbous_nose_20", "noble_nose_bridge_11", "lower_bridge_nose_758", "wide_nose_bridge_27", "upturned_nose_tip_19", "bulbous_nose_tip_6", "crooked_nose_656"]
SHAPEUI["Mouth"] = [ "lip_width_155", "tall_lips_653", "lip_thickness_505", "lip_ratio_799", "mouth_height_506", "mouth_corner_659", "lip_cleft_deep_764", "wide_lip_cleft_25", "shift_mouth_663"]
SHAPEUI["Chin"] = [ "weak_chin_7", "square_jaw_17", "deep_chin_185", "jaw_angle_760", "jaw_jut_665", "jowls_12", "cleft_chin_5", "cleft_chin_upper_13", "double_chin_8"]
SHAPEUI["Torso"] = [ "torso_muscles_649", "torso_muscles_678", "neck_thickness_683", "neck_length_756", "shoulders_36", "breast_size_105", "breast_gravity_507", "breast_female_cleavage_684", "chest_male_no_pecs_685", "arm_length_693", "hand_size_675", "torso_length_38", "love_handles_676", "belly_size_157"]
SHAPEUI["Legs"] = [ "leg_muscles_652", "leg_length_692", "hip_width_37", "hip_length_842", "butt_size_795", "male_package_879", "saddlebags_753", "bowed_legs_841", "foot_size_515"]

SHAPEUI["Shoes"] = [ "heel_height_198", "heel_shape_513", "toe_shape_514", "shoe_toe_thick_654", "platform_height_503", "shoe_platform_width_508"]
SHAPEUI["Shirt"] = [ "loose_upper_clothing_828", "shirtsleeve_flair_840"]
SHAPEUI["Pants"] = [ "pants_length_815", "loose_lower_clothing_816", "leg_pantflair_625", "low_crotch_638"]
SHAPEUI["Skirt"] = [ "skirt_looseness_863", "skirt_bustle_848"]
SHAPEUI["Hair"] = [ "hair_volume_763", "hair_front_133", "hair_sides_134" , "hair_back_135" , "hair_big_front_181" , "hair_big_top_182" , "hair_big_back_183" , "front_fringe_130" , "side_fringe_131" , "back_fringe_132" , "hair_sides_full_143" , "hair_sweep_136" , "hair_shear_front_762" , "hair_shear_back_674" , "hair_taper_front_755" , "hair_taper_back_754" , "hair_rumpled_177" , "pigtails_785" , "ponytail_789" , "hair_spiked_184" , "hair_tilt_137" , "hair_part_middle_140" , "hair_part_right_141" , "hair_part_left_142" , "bangs_part_middle_192"]
SHAPEUI["Eyebrows"] = ["eyebrow_size_119", "eyebrow_density_750", "lower_eyebrows_757", "arced_eyebrows_31", "pointy_eyebrows_16"]



SHAPE_FILTER = OrderedDict()
SHAPE_FILTER["Skeleton"] = [
        "height_33", "thickness_34",
        "head_size_682", "head_length_773", "face_shear_662",
        "eye_size_690", "eye_spacing_196", "eye_depth_769",
        "neck_thickness_683", "neck_length_756", "shoulders_36", "arm_length_693", "hand_size_675", "torso_length_38",
        "leg_length_692", "hip_width_37", "hip_length_842",
        "heel_height_198", "platform_height_503",
        "nose_big_out_2", "wide_nose_517", "broad_nostrils_4", "bulbous_nose_20", "noble_nose_bridge_11", "upturned_nose_tip_19",
        "lower_bridge_nose_758", "wide_nose_bridge_27", "crooked_nose_656", "low_septum_nose_759", "bulbous_nose_tip_6",
        "lip_width_155",  "tall_lips_653", "lip_thickness_505", "lip_ratio_799", "mouth_height_506", "mouth_corner_659",
        "lip_cleft_deep_764", "wide_lip_cleft_25", "shift_mouth_663",
        "big_ears_35", "pointy_ears_796",
        "deep_chin_185","jaw_jut_665", "weak_chin_7", "jaw_angle_760", "double_chin_8", "square_jaw_17", "head_shape_193",
        "wide_eyes_24",  "eyelid_corner_up_650", "eyelid_inner_corner_up_880", "upper_eyelid_fold_21", "puffy_lower_lids_765", "baggy_eyes_23",
        "forehead_angle_629", "big_brow_1", "puffy_upper_cheeks_18", "sunken_cheeks_10", "high_cheek_bones_14", "egg_head_646", "squash_stretch_head_647"
        ]
SHAPE_FILTER["Changed"] = []
SHAPE_FILTER["Deforming Active Object"] = []
SHAPE_FILTER["Fitted"]  = [
        "body_fat_637", "squash_stretch_head_647", "torso_muscles_649", "torso_muscles_678",
        "breast_size_105", "breast_gravity_507", "breast_female_cleavage_684",
        "love_handles_676", "belly_size_157", "chest_male_no_pecs_685",
        "leg_muscles_652", "saddlebags_753", "butt_size_795",
        "bowed_legs_841", "foot_size_515"
        ]
SHAPE_FILTER["Extended"] = [
        "nose_big_out_2", "wide_nose_517", "broad_nostrils_4", "bulbous_nose_20", "noble_nose_bridge_11", "upturned_nose_tip_19",
        "lower_bridge_nose_758", "wide_nose_bridge_27", "crooked_nose_656", "low_septum_nose_759", "bulbous_nose_tip_6",
        "lip_width_155",  "tall_lips_653", "lip_thickness_505", "lip_ratio_799", "mouth_height_506", "mouth_corner_659",
        "lip_cleft_deep_764", "wide_lip_cleft_25", "shift_mouth_663",
        "big_ears_35", "pointy_ears_796",
        "deep_chin_185","jaw_jut_665", "weak_chin_7", "jaw_angle_760", "double_chin_8", "square_jaw_17", "head_shape_193",
        "wide_eyes_24",  "eyelid_corner_up_650", "eyelid_inner_corner_up_880", "upper_eyelid_fold_21", "puffy_lower_lids_765", "baggy_eyes_23",
        "forehead_angle_629", "big_brow_1", "puffy_upper_cheeks_18", "sunken_cheeks_10", "high_cheek_bones_14", "egg_head_646", "squash_stretch_head_647"
        ]



class ShapeDrivers(bpy.types.PropertyGroup):
    bl_description = "Shape drivers control how the Shape Sliders\naffect the bones and Shape Keys of the Tamagoyaki character.\nThe data is loaded form the avatar lad file"

    Freeze : IntProperty(name = 'Freeze', min = 0, max = 1,
                         soft_min = 0, soft_max = 1, default = 0)

    def get_attributes(self):
        attributes = {}
        for key, val in self.items():
            attributes[key]=val
        return attributes



class ShapeValues(bpy.types.PropertyGroup):
    bl_description = "Shape values are very similar to ShapeDrivers, except that the vlaues are float values derived from the ShapeDriver slider settings.\nNote: The ShapeValues for the default Shape do not correspond to exact Slider values\n"

    def get_attributes(self):
        attributes = {}
        for key, val in self.items():
            attributes[key]=val
        return attributes

classes = (
    ShapeDrivers,
    ShapeValues
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        registerlog.info("Registered const:%s" % cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        registerlog.info("Unregistered const:%s" % cls)
