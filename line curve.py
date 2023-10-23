import cairo
import math

"""set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

"""Bezier Curve"""
ctx.move_to(100,200)
ctx.curve_to(200,300,300,100,450,200)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke()

"""Line 1"""
ctx.move_to(100,200)
ctx.line_to(160,340)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(3)
ctx.stroke()


"""Line 2"""
ctx.move_to(450,200)
ctx.line_to(350,50)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(3)
ctx.stroke()

surface.write_to_png('output/q1.png')