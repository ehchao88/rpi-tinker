from image import *
import lcd5110 as LCD
import time
import sys

converter: ImageConverter = ImageConverter()
image = converter.convert_to_grayscale('test_images/rhett.png')
image.save('test_results/rhett_gray.png')

image = converter.convert_to_grayscale_and_resize('test_images/rhett.png')
image.save('test_results/rhett_resized.png')

imageBytes = converter.get_image_bytes('test_images/rhett.png')
print(len(imageBytes))

screen = LCD.LCD5110()
while True:
    try: 
        screen.printImage(imageBytes)
        time.sleep(5)
    except KeyboardInterrupt:
        screen.cleanup()
        sys.exit(0)