import io
from PIL import Image, ImageFile

class ImageConverter:
    def __init__(self):
        self.width = 84
        self.height = 48
    
    def convert_to_grayscale(self, file_path: str) -> ImageFile.ImageFile:
        raw_image: ImageFile.ImageFile = Image.open(file_path)
        greyscale_image: ImageFile.ImageFile = raw_image.convert('1', dither=None)
        return greyscale_image
    
    def convert_to_grayscale_and_resize(self, file_path: str):
        raw_image: ImageFile.ImageFile = Image.open(file_path)
        greyscale_image: ImageFile.ImageFile = raw_image.convert('1', dither=None)
        size = (self.width, self.height)
        greyscale_image = greyscale_image.resize(size)
        return greyscale_image
    
    def get_image_bytes (self, file_path: str):
        resized_image = self.convert_to_grayscale_and_resize(file_path)
        w,h = resized_image.size
        bits = ''
        for y in range(h):
            for x in range(w):
                if resized_image.getpixel((x,y)) == 1:
                    bits += '1'
                else:
                    bits += '0'
        byte_rep = int(bits, base=2).to_bytes(int(len(bits)/8), 'little')

        return byte_rep
    
