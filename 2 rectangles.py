import cairo

"""Set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

"""Triangle"""
ctx.move_to(10,150)
ctx.line_to(10,350)
ctx.line_to(450,350)
ctx.close_path()
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.set_source_rgb(1,0,0)
ctx.set_line_width(10)
ctx.stroke()

"""Triangle 2"""
ctx.move_to(10,120)
ctx.line_to(470,120)
ctx.line_to(470,320)
ctx.close_path()
ctx.set_line_join(cairo.LINE_JOIN_ROUND)

ctx.set_source_rgba(1,0,0)
ctx.fill_preserve()

ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke()





surface.write_to_png('output/q2.png')