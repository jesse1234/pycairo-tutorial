import math
import cairo 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,800,800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

ctx.save()
ctx.set_source_rgb(1,0,0)
ctx.rectangle(0,0,100,100)
ctx.stroke()

ctx.save()
ctx.set_line_width(20)
ctx.rectangle(100,100,100,200)
ctx.stroke()
ctx.restore()

ctx.rectangle(200,200,100,200)
ctx.stroke()
ctx.restore()

surface.write_to_png('output 2/save_restore.png')
