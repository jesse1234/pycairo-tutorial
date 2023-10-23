import cairo

class Drawing:
    def __init__(self, width, height):
        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
        self.ctx = cairo.Context(self.surface)

    def set_background(self, r, g, b):
        self.ctx.set_source_rgb(r, g, b)
        self.ctx.paint()

    def draw_rectangle(self, x, y, width, height, r, g, b, fill=True, line_width=1):
        self.ctx.rectangle(x, y, width, height)
        self.ctx.set_source_rgb(r, g, b)
        
        if fill:
            self.ctx.fill()
        else:
            self.ctx.set_line_width(line_width)
            self.ctx.stroke()

    def save_to_png(self, filename):
        self.surface.write_to_png(filename)

if __name__ == '__main__':
    drawing = Drawing(600, 400)
    
    # Set background
    drawing.set_background(0.8, 0.8, 0.8)
    
    # Red Rectangle
    drawing.draw_rectangle(100, 100, 100, 240, 1, 0, 0)
    
    # Green Rectangle
    drawing.draw_rectangle(250, 100, 100, 240, 0, 1, 0, fill=False, line_width=5)
    
    # Blue Square
    drawing.draw_rectangle(400, 100, 100, 240, 0, 0, 1)
    
    drawing.save_to_png('output/output.png')