###tkinter

############################################################
##Reference
#Reference1: https://blog.naver.com/ivecoding/222678066094
#Reference2: https://www.youtube.com/watch?v=YXPyB4XeYLA 1:18:19 / 5:37:30

############################################################
##Import Library
from tkinter import *
from PIL import ImageTk,Image

############################################################
##Create
#Window
root = Tk()
root.title("Enter Title")
# root.geometry("400x300")
root.iconbitmap('C:/Users/lsyoo/Desktop/Python/pikachu_icon.ico')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("pika.png"))

#Label - Label(root, text="")
my_label = Label(image=my_img)
my_label.pack()
# myLabel = Label(root, text="Hello World!")
# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="Hola Mundo!")

#Entry - Entry(root, width=w, height=h, fg="red", bg="blue", borderwidth=x)
# e = Entry(root)
# e.pack()
# e.insert(0, "Enter Your Name: ") #Default text within input box

#Button - Button(root, text="", state=ENABLED/DISABLED, padx=X, pady=Y, fg="red", bg="blue", command=def function)
# def myClick():
#     myLabel_Input = "Hello " + e.get()
#     myLabel = Label(root, text=myLabel_Input)
#     myLabel.pack()

# myButton = Button(root, text="Click Me!", command=myClick)

# myButton1 = Button(root, text="Press", padx=20, pady=20)
# myButton2 = Button(root, text="Press", state=DISABLED)

# myButton1.grid(row=0, column=0)
# myButton2.grid(row=1, column=1)

############################################################
##Display

#Pack - (앞서 생성한 아이템).pack()
# myLabel.pack() 
# myButton.pack()

#Grid - (앞서 생성한 아이템).grid(row=n, column=m)
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

############################################################
##Creating an event loop
root.mainloop()

############################################################
##Notes

# #제목, 사이즈 지정
# rt.title("Hello World!")
# rt["height"] = 600
# rt["width"] = 600

# #프레임 나누기
# frame = Frame(rt)

# ##왼쪽 프레임(450x300, 검정색 바탕)
# frame_left = Frame(frame)
# frame_left["height"] = 300
# frame_left["width"] = 450
# frame_left["background"] = "black"

# ##오른쪽 프레임(300x600, 분홍색 바탕)
# frame_right = Frame(frame)
# frame_right["height"] = 600
# frame_right["width"] = 300
# frame_right["background"] = "pink"

# #화면에 프레임 표시
# frame.pack()
# frame_left.pack(side=LEFT)
# frame_right.pack(side=RIGHT)
# rt.mainloop()
