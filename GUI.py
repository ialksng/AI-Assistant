from tkinter import *
from PIL import Image, ImageTk
import speech2text
import action

root = Tk()
root.title("AI Assistant") 
root.geometry("550x675")
root.resizable(False, False)
root.config(bg = "#1E90FF")

# functions
def ask():
    user_val = speech2text.speech2text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->' + user_val + "\n")
    if bot_val != None:
        text.insert(END, 'Bot<---' + str(bot_val) + "\n")
    if bot_val == "Ok, shutting down!":
        root.destroy()

def delete():
    text.delete('1.0', "end")

def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User--->' + send + "\n")
    if bot != None:
        text.insert(END, 'Bot<---' + str(bot) + "\n")
    if bot == "Ok, shutting down!":
        root.destroy()


# frame
frame = LabelFrame(root, padx = 100, pady = 7, borderwidth = 3, relief = "raised")
frame.config(bg = "#00BFFF")
frame.grid(row = 0, column = 1, padx = 55, pady = 10)

# text label
text_label = Label(frame, text = "AlphaBot", font = ("comic Sans ms", 14, "bold"), bg = "#ADD8E6")
text_label.grid(row = 0, column = 0, padx = 20, pady = 10)

# image
image = ImageTk.PhotoImage(Image.open("C:/Users/ialks/OneDrive/Documents/Computer Science & Engineering/Programming Languages/Python/Projects/AI Assistant/static/AlphaBot.png"))
image_label = Label(frame, image = image)
image_label.grid(row = 1, column = 0, pady = 20)

# adding a text widget
text = Text(root, font = ('courier 10 bold'), bg = "#ADD8E6")
text.grid(row = 2, column = 0)
text.place(x = 100, y = 375, width = 375, height = 100)

# entry widget
entry = Entry(root, justify = CENTER)
entry.place(x = 100, y = 500, width = 350, height = 30)

# buttons
Button1 = Button(root, text = "ASK", bg = "#ADD8E6", pady = 16, padx = 40, borderwidth = 2, relief = SOLID, command = ask)
Button1.place(x = 70, y = 575)
Button2 = Button(root, text = "DELETE", bg = "#ADD8E6", pady = 16, padx = 40, borderwidth = 2, relief = SOLID, command = delete)
Button2.place(x = 225, y = 575)
Button3 = Button(root, text = "SEND", bg = "#ADD8E6", pady = 16, padx = 40, borderwidth = 2, relief = SOLID, command = send)
Button3.place(x = 400, y = 575)

root.mainloop()