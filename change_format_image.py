from PIL import Image,UnidentifiedImageError
import os

"""set file path"""
old_file_path = os.path.join(os.getcwd(), 'images')
new_file_path = os.path.join(os.getcwd(), 'images_jpg')

# check path directory 
# print("Input folder:", old_file_path)
# print("Output folder:", new_file_path)

# try do for one image
# img = Image.open(old_file_path + "ic_add_location_white_48dp")
# img.rotate(-90).resize((128,128)).convert("RGB").save(new_file_path + "ic_add_location_white_48dp.jpg" )

def change_format(name):
    """ this fuction will recieve name of pic that specific in ..mylib../images can change in old_file_path 
        and not have any extension 
        it will return format of picture to rotate 90 degree clockwise and resize to 128x128 and 
        save in new_file_path with .jpg format"""
    curent_path = os.path.join(old_file_path, name)
    save_path = os.path.join(new_file_path, name)
    
    try:
        Image.open(curent_path)
    except UnidentifiedImageError:
        print(f"It not an image (skipping)", name)
        return
    
    img = Image.open(curent_path)
    img.rotate(-90).resize((128,128)).convert("RGB").save(save_path + ".jpg" )
    return

if __name__ == "__main__":
    for pic in os.listdir(old_file_path):
        #print(pic) #for check list of file name
        change_format(pic)
    
