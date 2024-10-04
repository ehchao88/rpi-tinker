#Converts full size images to 84x48 bitmap to be compatible with Nokia 5110 LCD

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
    
    # Converts black and white image to bitmap, with addressing compatible with Nokia 5110. 
    def get_image_bytes (self, file_path: str):
        resized_image = self.convert_to_grayscale_and_resize(file_path)
        w,h = resized_image.size
        bits = ''
        # Screen pixels are addressed by bytes, each representing a block of 8 pixel height and 1 pixel width
        cur_y = 0
        while cur_y < h:
            for x in range(w):
                cur_byte = ''
                for y in range(8):
                    real_y = cur_y + y
                    if resized_image.getpixel((x, real_y)) == 0xFF:
                        cur_byte += '0'
                    else:
                        cur_byte += '1'
                bits += cur_byte
            cur_y += 8

        # Convert bit string to byte representation
        byte_rep = int(bits, base=2).to_bytes(int(len(bits)/8), 'little')

        return byte_rep
    
