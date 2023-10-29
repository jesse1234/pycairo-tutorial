import cairo 

"""Set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

ctx.set_source_rgb(0,0,0)

"""Rectangle"""
x = 100
y = 100
height = 100
width = 200
ctx.move_to(100,100)
ctx.line_to(x + width, y)
ctx.line_to(x + width,y + height)
ctx.line_to(x,y + height)
ctx.close_path()
ctx.stroke()

surface.write_to_png('output 2/rectangle.png')