from colorsys import rgb_to_hls, hls_to_rgb,rgb_to_hsv, hsv_to_rgb
class Pallete:
    """Pallete object takes colors as RGB,HSV, or HLS"""
    def __init__(self,*args):
        newArgs=[]#converts 0-255 RGB values to 0.0-1.0 values for conversion
        percent=[value/float(255) for color in args for value in color]
        for i in range(0,len(percent),3):
            newArgs.append(tuple(percent[i:i+3]))
        self.rgb=[color for color in args]
        self.hls=[rgb_to_hls(*color) for color in newArgs]
        self.hsv=[rgb_to_hsv(*color) for color in newArgs]

    def offsetH(self,value):
        new=[]
        for color in self.hls:
            new.append((color[0]+value,color[1],color[2]))
        self.hls=new
        self.update()
    def offsetS(self,value):
        new=[]
        for color in self.hls:
            new.append((color[0],color[1],color[2]+value))
        self.hls=new
        self.update()
    def offsetL(self,value):
        new=[]
        for color in self.hls:
            new.append((color[0],color[1]+value,color[2]))
        self.hls=new
        self.update()

    def update(self):
        self.rgb=[]
        rgb=[hls_to_rgb(*color) for color in self.hls]
        rgb=[int(value*255) for color in rgb for value in color]
        for i in range(0,len(rgb),3):
            self.rgb.append(tuple(rgb[i:i+3]))
    pass
