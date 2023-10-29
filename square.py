import cairo

"""Set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.move_to(100,100)
ctx.line_to(200,100)
ctx.line_to(200,200)
ctx.line_to(100,200)
ctx.close_path()
ctx.set_source_rgb(1,0,0)
ctx.fill()

surface.write_to_png('output 2/square.png')