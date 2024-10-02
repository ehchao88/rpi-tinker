import io
from PIL import Image, ImageFile

class ImageConverter:
    def __init__(self):
        self.width = 84
        self.height = 48
    
    def convert_to_grayscale(self, file_path: str) -> ImageFile.ImageFile:
        raw_image: ImageFile.ImageFile = Image.open(file_path)
        greyscale_image: ImageFile.ImageFile = raw_image.convert('L')
        return greyscale_image
    
    def convert_to_grayscale_and_resize(self, file_path: str):
        raw_image: ImageFile.ImageFile = Image.open(file_path)
        greyscale_image: ImageFile.ImageFile = raw_image.convert('L')
        size = (int(self.width/6) + 1, int(self.height/8) + 1)
        greyscale_image = greyscale_image.resize(size)
        return greyscale_image
    
    def get_image_bytes (self, file_path: str):
        resized_image = self.convert_to_grayscale_and_resize(file_path)
        resized_image = resized_image.convert(mode="1")
        resized_image = resized_image.tobitmap()
        return resized_image
    
