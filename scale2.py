import cairo 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,600,600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

width = 100
height =100

ctx.set_source_rgb(1,0,0)
ctx.rectangle(150,200,width,height)
ctx.fill()

ctx.scale(2/3,1/3)
ctx.set_source_rgb(0,0,1)
ctx.rectangle(300,150,width,height)
ctx.fill()

surface.write_to_png('output 2/scale2.png')