import os


def load_result_images():
    rootdir = "./result_images/"
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            image_list.append(ImageTk.PhotoImage(Image.open(rootdir+file)))    

load_result_images()