from tkinter import *
from PIL import ImageTk, Image

x = Tk()

x.after(1800)

x.title("Lets See If You Can Get The Password...")
x.lift()
x.attributes('-topmost', True)

screen_width = x.winfo_screenwidth()
screen_height = x.winfo_screenheight()

window_width = 400  
window_height = 400 

x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

x.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

frame = Frame(x, width=200, height=200)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("riddleTwo.png"))
label = Label(frame, image = img)
label.pack()

riddle_frame = Frame(x, width=300, height=20)
riddle_frame.pack()
riddle_frame.place(anchor='center', relx=0.5, rely=0.1)
img2 = ImageTk.PhotoImage(Image.open("r.png"))
label2 = Label(riddle_frame, image = img2)
label2.pack()




x.mainloop()