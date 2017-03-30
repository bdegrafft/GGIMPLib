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
