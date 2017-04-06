from gimpfu import pdb
class Vector:
    """Class for GIMP vector objects and methods, corresponding to paths in the
     GIMP GUI. Takes either one or three 2-tuples as point and control points.
     The optional closed flag indicates a path's end meets itself at it's start.
     (pointX,PointY) if polygonal==True OR
     (((control1X,control1Y),(pointX,pointY),(control2X,control2Y)))
     if polygonal== False"""
    def __init__(self,img,points,closed=False,polygonal=False):
        self.closed=closed
        self.img=img
        self.vectorObj=pdb.gimp_vectors_new(self.img, 'Vector')
        if polygonal == True:
            self.points=[]
            for point in points:
                for _ in range(3):
                    self.points.append(point)
        else:
            self.points=points
        pdb.gimp_vectors_stroke_new_from_points(
        self.vectorObj,
        0, # 0 = Beziers Curve
        len(self.flatten()),
        # {controle1} {centre} {controle2}
        self.flatten(),
        self.closed) # Closed = True
    def stroke(self,layer,brush=None):
        if brush:
            brush.set()
        pdb.gimp_image_add_vectors(self.img, self.vectorObj, 0)
        pdb.gimp_edit_stroke_vectors(layer, self.vectorObj)
    def extend(self,*points,**kwargs):
        if kwargs.get('polygonal',False)==True:
            for point in points:
                for _ in range(3):
                    self.points.append(point)
        else:
            for point in points:
                self.points+=(point),
        pdb.gimp_vectors_stroke_new_from_points(
        self.vectorObj,
        0, # 0 = Beziers Curve
        len(self.flatten()),
        # {controle1} {centre} {controle2}
        self.flatten(),
        self.closed) # Closed = True
    def getpoints(self):
        stroke=pdb.gimp_vectors_get_strokes(self.vectorObj)[0] #returns Number of strokes+ stroke ID's
        points=pdb.gimp_vectors_stroke_get_points(self.vectorObj,stroke)[2]
        return points
    def flatten(self):
        '''Flatten list of points for use when making PDB calls'''
        flatPoints=[point for tupl in self.points for point in tupl]
        return flatPoints

    def remove(self):
        pdb.gimp_image_remove_vectors(self.vectorObj)
    def __iter__(self):
        return iter(self.points)
