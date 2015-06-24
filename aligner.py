from PIL import Image, ImageDraw
from faces import Faces
from throttle import Throttle

class Aligner:
    """
       Takes two images and aligns the second image face to the first image face.
       - Assumes Jon is on the right
    """
    def __init__(self):
        self.faces = []

    def add_face_no_throttle(self, image_path):
        self.add_face(image_path)

    @Throttle(0.3)
    def add_face(self, image_path):
        faces = Faces()
        faces.from_file(image_path)
        image = Image.open(image_path)

        if not faces.data:
            raise MissingFaceException("image has no faces")
        
        face = self.find_key_face(faces, image)

        if not face:
            raise NoRectangleException("can't find valid rectangle for faces in image " + image_path)

        self.faces.append({"face": face, "image": image})

    def align(self, out_path):
        if len(self.faces) != 2:
            raise NotEnoughFacesException("need more faces")

        image1 = self.faces[0]["image"]
        image2 = self.faces[1]["image"]
        
        image1_rect = self.faces[0]["face"]["faceRectangle"]
        image2_rect = self.faces[1]["face"]["faceRectangle"]

        scale_factor = image1_rect["width"] / float(image2_rect["width"])

        width, height = image2.size
        image2 = image2.resize((int(width * scale_factor), int(height * scale_factor)), Image.ANTIALIAS)
        
        new_image = Image.new('RGBA', image1.size, 'black')
        new_rect = {"top": image2_rect["top"] * scale_factor, "left": image2_rect["left"] * scale_factor,
                   "width": image2_rect["width"] * scale_factor, "height": image2_rect["height"] * scale_factor}
        offset = (int(round(image1_rect["left"] - new_rect["left"])), int(round(image1_rect["top"] - new_rect["top"])))

        new_image.paste(image2, offset)
        new_image.save(out_path)

    def find_key_face(self, faces, image):
        # current algorithm is return the face that is further left than midpoint
        for face in faces.data:
            width, height = image.size
            if face["faceRectangle"]["left"] > width / 2:
                return face
        return None

class MissingFaceException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NoRectangleException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NotEnoughFacesException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
