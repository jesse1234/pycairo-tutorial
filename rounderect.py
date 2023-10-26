import cairo 
import math

"""Set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

def rounderect(ctx,x,y,width,height,r):
    ctx.arc(x+r, y+r, r, math.pi, 3*math.pi/2)
    ctx.arc(x+width-r, y+r, r, 3*math.pi/2, 0)
    ctx.arc(x+width-r, y+height-r, r, 0, math.pi/2)
    ctx.arc(x+r, y+height-r, r, math.pi/2, math.pi)
    ctx.close_path()

ctx.set_line_width(10)
ctx.set_source_rgb(0,0,0.5)
rounderect(ctx, 100, 100, 400, 200, 50)
ctx.stroke()

surface.write_to_png('output 2/rounderect.png')
