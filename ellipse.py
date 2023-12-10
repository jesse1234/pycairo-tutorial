import math
import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

ctx.save()
ctx.translate(300,350)
ctx.scale(2,1)
ctx.translate(-300,-350)

ctx.arc(300,350,100,0,math.pi*2)
ctx.restore()

ctx.set_source_rgb(0.8,0,0)
ctx.fill_preserve()
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png('output 2/ellipse.png')

