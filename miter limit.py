import math
import cairo

"""Set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

"""Miter limit"""
ctx.move_to(100, 80)
ctx.line_to(500,80)
limit=1/math.sin(9/2)
ctx.set_miter_limit(limit)
ctx.stroke()

surface.write_to_png('output/miter.png')