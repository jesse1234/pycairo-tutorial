import math
import cairo 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,600,600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

x = 250
y = 300
width = 200
height = 100

ctx.set_source_rgb(0,0,0)
ctx.rectangle(x,y,width,height)
ctx.set_dash([5,5])
ctx.stroke()

ctx.rotate(math.pi/6)

ctx.set_source_rgb(0,0.5,0.5)
ctx.rectangle(x,y,width,height)
ctx.fill()

surface.write_to_png('output 2/rotation.png')
