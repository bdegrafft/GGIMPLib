from gimpfu import pdb
class Vector:
    def __init__(self,img,startpoint,closed=False):
        self.startpoint = startpoint
        self.closed=closed
        self.img=img
        self.vectorObj=pdb.gimp_vectors_new(self.img, 'Vector')
        self.points=[self.startpoint[0],self.startpoint[1],self.startpoint[0],self.startpoint[1],self.startpoint[0],self.startpoint[1]]

    def stroke(self,layer,brush=None):
        if brush:
            brush.set()
        pdb.gimp_vectors_stroke_new_from_points(
        self.vectorObj,
        0, # 0 = Beziers Curve
        len(self.points),
        # {controle1} {centre} {controle2}
        self.points,
        self.closed) # Closed = True
        pdb.gimp_image_add_vectors(self.img, self.vectorObj, 0)

        pdb.gimp_edit_stroke_vectors(layer, self.vectorObj)
    def extend(self,c1,center,c2):
        self.points.extend([c1[0],c1[1],center[0],center[1],c2[0],c2[1]])
