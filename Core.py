try:
    from gimpfu import *
except:
    pass
import traceback

def initalize(height=2000,width=2000,numLayers=1,fill=True,debug=True):#add undogroup here and in finalize
    img = gimp.Image(height, width, RGB)
    layers=[]
    if debug:
        pass
    else:
        pdb.gimp_image_undo_group_start(img)
    for l in range(numLayers):
        new=gimp.Layer(img, "Layer {}".format(l), height, width, RGB_IMAGE, 100, NORMAL_MODE)
        img.add_layer(new, -1)
        if fill==True:
            new.fill(BACKGROUND_FILL)
        layers.append(new)
    return img,layers
def finalize(img):
        pdb.gimp_image_flatten(img)
        gimp.Display(img)
        gimp.displays_flush()
def addLayer(img,name='New Layer'):
        height,width=img.height,img.width
        new=gimp.Layer(img, name, height, width, RGBA_IMAGE, 100, NORMAL_MODE)
        img.add_layer(new, -1)
        new.fill(BACKGROUND_FILL)
        return new
def gmic(img,command,layer=None):
    if layer==None:
        layer=img.active_layer
        try:
            pdb.plug_in_gmic(img,layer,1,command,run_mode=RUN_NONINTERACTIVE)
        except:
            tb=traceback.format_exc()
            pdb.gimp_message('{} -- Calling Error'.format(command))
class Brush:
    """Brush Class, used to define variables related to creating brush strokes"""
    def __init__(self, size=1,style='1. Pixel',tool='pencil',mode=0,dynamics='Dynamics Off',opacity=100):
        self.size = size
        self.style= style
        self.tool = tool.lower()
        self.mode = mode
        self.dynamics = dynamics
        self.opacity= opacity
        self.brushstrings=pdb.gimp_brushes_get_list('.*')[1]
        self.dynamicsStrings = pdb.gimp_dynamics_get_list('.*')[1]
    def set(self):
        pdb.gimp_context_set_brush(self.style)
        pdb.gimp_context_set_brush_size(self.size)
        pdb.gimp_context_set_opacity(self.opacity)
        pdb.gimp_context_set_paint_mode(self.mode)
        pdb.gimp_context_set_dynamics(self.dynamics)
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
            # new_vectors=pdb.gimp_vectors_new(img, 'Vectors!')
            # pdb.gimp_vectors_stroke_new_from_points(
            # new_vectors,
            # 0, # 0 = Beziers Curve
            # 12,
            # # {controle1} {centre} {controle2}
            # [ 0,0,0,0,50,10,560,450,500,500,1000,1000],
            # False) # Closed = True
            # pdb.gimp_image_add_vectors(img, new_vectors, 0)
class Vector:
    def __init__(self,img,points,closed=False):
        self.points=points
        self.closed=closed
        self.vectorObj=pdb.gimp_vectors_new(img, 'Vector')
        # pdb.gimp_vectors_stroke_new_from_points(
        # self.vectorObj,
        # 0, # 0 = Beziers Curve
        # len(points),
        # # {controle1} {centre} {controle2}
        # points,
        # self.closed) # Closed = True
        # pdb.gimp_image_add_vectors(img, self.vectorObj, 0)
    def stroke(self,layer,brush=None):
        if brush:
            brush.set()
        pdb.gimp_edit_stroke_vectors(layer, self.vectorObj)
