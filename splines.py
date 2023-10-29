import cairo 

"""Set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,300,300)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

"""Multiple bezier curves"""
ctx.move_to(100,120)
ctx.curve_to(125, 150, 175, 150, 200, 110)
ctx.curve_to(220, 175, 220, 75, 240, 50)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png('output 2/splines.png')