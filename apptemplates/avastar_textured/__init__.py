### Tamagoyaki license (GPL)

bl_info = {
    "name": "Tamagoyaki 2 Template",
    "author": "Machinimatrix",
    "version": (1, 0),
    "blender": (2, 78, 0),
    "location": "View3D > Toolshelf, Properties editor",
    "description": "Tamagoyaki 2 Template",
    "warning": "",
    "wiki_url":  "https://avalab.org/tamagoyaki/293/",
    "category": "Object",
}

import os

BASE_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

import bpy
from bpy.types import Operator
from bpy.props import (
    FloatVectorProperty,
    StringProperty,
)
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


def paths_from_id(dir_id):
    """(display_name, full_path)"""
    d = os.path.join(DATA_DIR, dir_id)
    for f in os.listdir(d):
        if f.endswith(".blend"):
            yield (bpy.path.display_name(f), os.path.join(d, f))


def add_object_menu(self, context):
    layout = self.layout
    for name, f in paths_from_id("object"):
        props = layout.operator(
            OBJECT_OT_add_object_from_blend.bl_idname,
            text=name,
            icon='PLUGIN',
        )
        props.filepath = f
        props.type_attr = "meshes"


def register():
    pass


def unregister():
    pass


if __name__ == "__main__":
 register()