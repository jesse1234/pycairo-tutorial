import cairo


class DrawingCanvas:
    def __init__(self, width, height, background_color=(0.8, 0.8, 0.8)):
        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
        self.ctx = cairo.Context(self.surface)
        self.ctx.set_source_rgb(*background_color)
        self.ctx.paint()

    def draw_line(self, start_x, start_y, end_x, end_y, color=(1, 0, 0), line_width=10):
        self.ctx.move_to(start_x, start_y)
        self.ctx.line_to(end_x, end_y)
        self.ctx.set_source_rgb(*color)
        self.ctx.set_line_width(line_width)
        self.ctx.stroke()

    def save_to_png(self, filename):
        self.surface.write_to_png(filename)

if __name__ == '__main__':
    canvas = DrawingCanvas(1080, 765)
    canvas.draw_line(100, 100, 500, 300)
    canvas.save_to_png('output/line.png')
