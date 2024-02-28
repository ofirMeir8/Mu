from tkinter import *
from PIL import ImageTk, Image
import time

def open(x: Tk):

    x.after(2000)

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
    img = ImageTk.PhotoImage(Image.open("gimetria.png"))
    label = Label(frame, image = img)
    label.pack()

    riddle_frame = Frame(x, width=100, height=100)
    riddle_frame.pack()
    riddle_frame.place(anchor='center', relx=0.5, rely=0.1)



    t = "\u0332".join(" 50")
    t += "\u0332".join(" 6")
    t += "\u0332".join(" 8")
    t += "\u0332".join(" 90")
    t += "\u0332".join(" 10")
    t += "\u0332".join(" 50")

    riddle = Label(riddle_frame, text = t)
    riddle.config(font=("Courier", 20))
    riddle.pack()


    x.mainloop()

if __name__ == "__main__":
    x = Tk()
    open(x)    

