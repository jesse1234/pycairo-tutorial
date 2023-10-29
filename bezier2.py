import cairo

"""Set up pycairo"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,300,300)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

"""Bezier curve"""
ax = 100
ay = 100

bx = 125
by = 50

cx = 175
cy = 50

dx = 200
dy = 100

ctx.move_to(ax,ay)
ctx.curve_to(bx,by,cx,cy,dx,dy)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png('output 2/bezier2.png')