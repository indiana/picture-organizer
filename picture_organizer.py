from exif import Image
import os
from shutil import copyfile

picture_folder = r'c:\picture\folder'
target_folder = r'c:\target\folder'

for file in os.listdir(picture_folder):
    with open(picture_folder + os.path.sep + file, 'rb') as image_file:
        make = 'No make'
        model = 'No model'
        year = 'No year'
        month = 'No month'
        try:
            my_image = Image(image_file)
            if my_image.has_exif:
                if hasattr(my_image, 'make'):
                    if(my_image.make != ''):
                        make = my_image.make.strip()
                if hasattr(my_image, 'model'):
                    if(my_image.model != ''):
                        model = my_image.model.strip()
                if hasattr(my_image, 'datetime_original'):
                    if(my_image.datetime_original != ''):
                        year = my_image.datetime_original[:4]
                        month = my_image.datetime_original[5:7]
        except:
            print(f"Not an image?")
        finally:
            target_path = os.path.join(target_folder, make, model, year, month)
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            target_file = os.path.join(target_path, os.path.basename(image_file.name))
            print(f"Saving {target_file} ...")

            copyfile(image_file.name, target_file)
