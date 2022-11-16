import os



# get the path or directory
folder_dir = "C:/Image-Recognition/research/rock/"

i = 0
for image in os.listdir(folder_dir):
    old_path = str(folder_dir) + str(image)
    #value = str(i).zfill(4)
    new_path = str(folder_dir) + str(i) + ".jpg"
    os.rename(old_path, new_path)
    i += 1