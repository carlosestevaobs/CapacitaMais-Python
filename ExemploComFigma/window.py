from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    410.0, 525.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    1030.5, 325.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#b3a6fd",
    highlightthickness = 0)

entry0.place(
    x = 893.0, y = 308,
    width = 275.0,
    height = 32)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    1030.5, 413.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#b3a6fd",
    highlightthickness = 0)

entry1.place(
    x = 893.0, y = 396,
    width = 275.0,
    height = 32)

canvas.create_text(
    912.5, 381.0,
    text = "Senha:",
    fill = "#000000",
    font = ("None", int(12.0)))

canvas.create_text(
    916.0, 290.0,
    text = "Usuario:",
    fill = "#000000",
    font = ("None", int(12.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 942, y = 482,
    width = 154,
    height = 30)

window.resizable(False, False)
window.mainloop()
