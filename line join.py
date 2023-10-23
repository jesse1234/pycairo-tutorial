import cairo

"""Set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24,600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

"""Set line color and width"""
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(20)

"""Miter join"""
ctx.move_to(50,100)
ctx.line_to(180,300)
ctx.line_to(50,300)
ctx.set_line_join(cairo.LINE_JOIN_MITER)
ctx.stroke()

"""Round join"""
ctx.move_to(240,100)
ctx.line_to(370,300)
ctx.line_to(240,300)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.stroke()

"""Bevel join"""
ctx.move_to(430,100)
ctx.line_to(560,300)
ctx.line_to(430,300)
ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
ctx.stroke()

surface.write_to_png('output/line join.png')