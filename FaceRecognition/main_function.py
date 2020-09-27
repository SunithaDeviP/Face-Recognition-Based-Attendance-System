import generate_train_dataset
import identify_face_video_copy
import data_preprocess
import train_main

import tkinter as tk
    

def Training():
    generate_train_dataset.generate_dataset()

    data_preprocess.data_preprocessing()

    train_main.train_data_classifier()

def Testing():
    identify_face_video_copy.recognize_face()


root = tk.Tk()

root.geometry("500x230") # set the root dimensions
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0) # makes the root window fixed in size.

frame = tk.Frame(root)
frame.place(height=250, width=500)

button1 = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button1.place(rely=0.35, relx=0.60)

button2 = tk.Button(frame,
                   text="Training",
                   command=Training)
button2.place(rely=0.35, relx=0.20)

button2 = tk.Button(frame,
                   text="Testing",
                   command=Testing)
button2.place(rely=0.35, relx=0.40)


root.mainloop()
