import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

x1 = 100
y1 = 200
x2 = 100
y2 = 400
x3 = 200
y3 = 300

ctx.move_to(x1,y1)
ctx.line_to(x2,y2)
ctx.line_to(x3,y3)
ctx.close_path()
ctx.set_source_rgb(1,0,0)
ctx.stroke()

ctx.scale(-1,1)
ctx.translate(-600,0)

ctx.move_to(x1,y1)
ctx.line_to(x2,y2)
ctx.line_to(x3,y3)
ctx.close_path()
ctx.set_source_rgb(1,0,0)
ctx.fill()

surface.write_to_png('output 2/flipping.png')
