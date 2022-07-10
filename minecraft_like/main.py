# pip install ursina
from ursina import *


class Object(Button):
        def __init__(self):
                super().__init__(
                        parent=scene,
                        position=(0, 0, 0),
                        model='cube',
                        oringin=0.5,
                        texture="white_cube",
                        color=color.white,
                        highlight_color=color.lime
                )


minecraft = Ursina()

voxel = Object()
minecraft.run()
