from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 512
height = 212

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( PointLight(point = (-1,-1,0) ))

rtx.scene.append( Donut(center=(0,-1.3,-10), externalRadius=1, internalRadius=0.5, material=stone ))
rtx.scene.append( Donut(center=(-5,-1.3,-10), externalRadius=2, internalRadius=1, material=brick ))
rtx.scene.append( Donut(center=(5,-1.3,-10), externalRadius=3, internalRadius=1.5, material=grass ))

rtx.glRender()

rtx.glFinish("output.bmp")