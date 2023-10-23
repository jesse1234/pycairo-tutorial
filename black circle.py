import cairo 
import math

"""Set up the surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

"""Circle"""
ctx.arc(300,200,100,0,2*math.pi)
ctx.set_source_rgb(0,0,0)
ctx.fill()

"""Green Line"""
ctx.move_to(200,200)
ctx.line_to(400,200)
ctx.set_source_rgb(0,1,0)
ctx.set_line_width(5)
ctx.stroke()

"""Green line 2"""
ctx.move_to(300,100)
ctx.line_to(300,300)
ctx.set_source_rgb(0,1,0)
ctx.set_line_width(5)
ctx.stroke()

"""Arc"""
ctx.arc(300,200,100,0, math.pi/2)
ctx.set_source_rgb(0,1,0)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png('output/q3.png')