import cairo 
import math

"""Set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,1000,800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0,0,0)
ctx.paint()

ctx.set_source_rgb(1, 0, 0)
ctx.arc(200, 400, 200, (3*math.pi/2), (math.pi/2))
ctx.stroke()

ctx.set_source_rgb(1, 0, 0)
ctx.arc(400, 200, 200, 0, math.pi)
ctx.stroke()

ctx.set_source_rgb(0, 0, 1)
ctx.arc(600, 400, 200, (math.pi / 2), (3*math.pi / 2))
ctx.stroke()

ctx.set_source_rgb(0, 0, 1)
ctx.arc(400, 600, 200, math.pi, 0)
ctx.stroke()

surface.write_to_png('output/task2.png')

