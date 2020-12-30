from tkinter import*


def hex(event):
    l = ["", "", "", "", "", "", "", "", "", "", "A", "B", "C", "D", "E", "F"]
    if s1.get() < 10:
        v1 = s1.get()
    else:
        v1 = l[s1.get()]
    if s2.get() < 10:
        v2 = s2.get()
    else:
        v2 = l[s2.get()]
    if s3.get() < 10:
        v3 = s3.get()
    else:
        v3 = l[s3.get()]
    if s4.get() < 10:
        v4 = s4.get()
    else:
        v4 = l[s4.get()]
    if s5.get() < 10:
        v5 = s5.get()
    else:
        v5 = l[s5.get()]
    if s6.get() < 10:
        v6 = s6.get()
    else:
        v6 = l[s6.get()]
    hex1 = Button(root, text=f"#{v1}{v2}{v3}{v4}{v5}{v6}", borderwidth=2, relief=SOLID)
    hex1.place(x=220, y=210, width=70, height=50)
    code = f"#{v1}{v2}{v3}{v4}{v5}{v6}"
    print(code)
    frame.configure(bg=code)


root = Tk()
root.geometry("400x400")
root.title("Colour Picker")

heading = Label(root, text="Choose Colour", fg="black", font="lucidaconsole 14 bold").place(x=100, y=5, width=200, height=45)

c1 = Label(root, text="R1", font="lucidaconsole 8 bold", fg="red").place(x=20, y=60, width=30, height=30)
s1 = Scale(root, from_=0, to=15, orien=HORIZONTAL)
s1.place(x=60, y=50, width=150, height=40)

c2 = Label(root, text="R2", font="lucidaconsole 8 bold", fg="red").place(x=20, y=110, width=30, height=30)
s2 = Scale(root, from_=0, to=15, orien=HORIZONTAL)
s2.place(x=60, y=100, width=150, height=40)

c3 = Label(root, text="G1", font="lucidaconsole 8 bold", fg="green").place(x=20, y=160, width=30, height=30)
s3 = Scale(root, from_=0, to=15, orien=HORIZONTAL)
s3.place(x=60, y=150, width=150, height=40)

c4 = Label(root, text="G2", font="lucidaconsole 8 bold", fg="green").place(x=20, y=210, width=30, height=30)
s4 = Scale(root, from_=0, to=15, orien=HORIZONTAL)
s4.place(x=60, y=200, width=150, height=40)

c5 = Label(root, text="B1", font="lucidaconsole 8 bold", fg="blue").place(x=20, y=260, width=30, height=30)
s5 = Scale(root, from_=0, to=15, orien=HORIZONTAL)
s5.place(x=60, y=250, width=150, height=40)

c6 = Label(root, text="B2", font="lucidaconsole 8 bold", fg="blue").place(x=20, y=310, width=30, height=30)
s6 = Scale(root, from_=0, to=15, orien=HORIZONTAL)
s6.place(x=60, y=300, width=150, height=40)

demo = Label(root, text="# R1 R2 G1 G2 B1 B2", fg="black", font="lucidaconsole 12 bold")
demo.place(x=50, y=350, width=300, height=40)

btn = Button(root, text="HEX", borderwidth=2, relief=SOLID)
btn.bind('<Button-1>', hex)
btn.place(x=220, y=150, width=70, height=50)

frame = Frame(root, borderwidth=2, relief=SOLID)
frame.place(x=300, y=130, width=90, height=150)

root.mainloop()
