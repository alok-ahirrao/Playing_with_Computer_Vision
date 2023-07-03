from tkinter import *
import sys

root = Tk()
root.title("PLAYING WITH COMPUTER VISION ヾ(⌐■_■)ノ♪")
# root.minsize(700, 500)

def game1():
    print("Game 1")

def game2():
    print("Game 2")

def game3():
    print("Game 3")

def game4():
    print("Game 4")

img1 = PhotoImage(file="game1.png").subsample(2)
img2 = PhotoImage(file="game2.png").subsample(2)
img3 = PhotoImage(file="game3.png").subsample(2)
img4 = PhotoImage(file="game4.png").subsample(2)

btn1 = Button(root, image=img1, command=game1, borderwidth=10)
btn2 = Button(root, image=img2, command=game2, borderwidth=10)
btn3 = Button(root, image=img3, command=game3, borderwidth=10)
btn4 = Button(root, image=img4, command=game4, borderwidth=10)

btn1.grid(row=0, column=0, pady=20, padx=20)
btn2.grid(row=0, column=1, pady=20, padx=20)
btn3.grid(row=1, column=0, pady=20, padx=20)
btn4.grid(row=1, column=1, pady=20, padx=20)

root.mainloop()
