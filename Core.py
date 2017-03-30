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
        except RuntimeError:
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
