import math
import cairo 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,800,800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

ctx.set_source_rgb(0,0,0)
ctx.rectangle(200,150,480,360)
ctx.set_dash([5,5])
ctx.stroke()

ctx.translate(440,330)
ctx.rotate(math.pi/6)
ctx.translate(-440,-330)

ctx.set_source_rgb(0,0.5,0.5)
ctx.rectangle(200,150,480,360)
ctx.fill()

surface.write_to_png('output 2/rotation2.png')
