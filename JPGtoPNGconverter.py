import sys
import os
from PIL import Image


class JPGToPNGConverter():
    def __init__(self, source_f, target_f):
        self.source_f = source_f
        self.target_f = target_f
        self.images = []
        self.extensions = ['JPG', 'jpg', 'JPEG', 'jpeg']

    def _append_images(self):
        if os.listdir(self.source_f):
            for image in os.listdir(self.source_f):
                image_ext = image.split('.')
                if len(image_ext) == 1:
                    continue
                elif image_ext[-1] in self.extensions:
                    self.images.append(os.path.join(self.source_f, image))
                else:
                    continue
        else:
            print(f'\'{self.source_f}\' is empty!')
        return self.images

    def _save_images(self):
        for conv_image in self.images:
            img = Image.open(conv_image)
            img_name = os.path.basename(conv_image)
            png_img = os.path.join(
                self.target_f, os.path.splitext(img_name)[0] + ".png")
            if os.path.exists(png_img):
                print(
                    f'WARNING: \'{img_name}\' png image with the same name exists in \'{self.target_f}\'. It will be overwritten.')
                img.save(png_img, "PNG")
            else:
                img.save(png_img, "PNG")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        source_folder = sys.argv[1]
        target_folder = sys.argv[2]

        # Instantiate after taking the arguments
        png = JPGToPNGConverter(source_folder, target_folder)

        # If the folder exists, call the function
        if os.path.exists(png.source_f) and os.path.isdir(png.source_f):
            png._append_images()
        else:
            print(f'\'{png.source_f}\' does not exist.')

        if os.path.exists(png.target_f) and os.path.isdir(png.target_f):
            png._save_images()
            print('All done!')
        else:
            print(f'\'{png.target_f}\' does not exist. Please create one.')

    elif len(sys.argv) == 1:
        print('[USAGE] python3 JPGtoPNGconverter.py source_folder/ target_folder/')
    else:
        print('Incorrect number of arguments provided.')
