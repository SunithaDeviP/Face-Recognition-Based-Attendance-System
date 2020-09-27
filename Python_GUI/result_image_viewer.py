from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('Attendance result Image Viewer')

image_list = []
my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)
start = 0
end = 0


def load_result_images():
    rootdir = "./result_images/"
    count =1
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            image_list.append(ImageTk.PhotoImage(Image.open(rootdir+file)))    
            count=count+1
    end = count

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global end

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number >= end:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)  
    button_forward.grid(row=1, column=2)


    
def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number <= start:
        button_back= Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)  
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back, state= DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(0))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
load_result_images()
root.mainloop()