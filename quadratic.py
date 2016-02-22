#!/usr/bin/python
import tkinter as tk
import math

def quit():
    global window
    window.destroy()


def quadraticSolver():

        inputA = int(entlblA.get())
        inputB = int(entlblB.get())
        inputC = int(entlblC.get())

        if ((inputB*inputB) - 4*inputA*inputC) < 0:
                newWindow = tk.Tk()
                newWindow.configure(background="#FFFFFF")
                newWindow.title("Answer")

                lbl1 = tk.Label(newWindow, text="I'm sorry this results in an imaginary number solution", fg="#383a39", bg="#FFFFFF")
                

                btn = tk.Button(newWindow, text="Thanks for Playing!", command=lambda: quit(), fg="#383a39", bg="#FFFFFF")
                btn.pack()
                
                lbl1.pack()
                lblA.pack()

                



                
        else:

                answer1 = (-inputB + math.sqrt((inputB*inputB) - 4*inputA*inputC))/(2*inputA)
                answer2 = (-inputB - math.sqrt((inputB*inputB) - 4*inputA*inputC))/(2*inputA)
                newWindow = tk.Tk()
                newWindow.configure(background="#FFFFFF")
                newWindow.title("Answer")
                


                lbl1 = tk.Label(newWindow, text="Answer 1: ", fg="#383a39", bg="#FFFFFF")
                lbl1A = tk.Label(newWindow, text="Answer 1: " + str(answer1), fg="#383a39", bg="#FFFFFF")
                lbl1.pack()
                lbl1A.pack()

                lbl1 = tk.Label(newWindow, text="Answer 2: ", fg="#383a39", bg="#FFFFFF")
                lbl1A = tk.Label(newWindow, text="Answer 2: " + str(answer2), fg="#383a39", bg="#FFFFFF")
                lbl1.pack()
                lbl1A.pack()


window = tk.Tk()
window.configure(background="#FFFFFF")
window.title("Dean's Quadratic Challenge")

photo = tk.PhotoImage(file="images.gif")
w = tk.Label(window, image=photo)
w.pack()

lblMain =tk.Label(window, text="Enter 3 values to get started:", fg="#383a39", bg="#FFFFFF", font=("Helvetica", 16))
lblMain.pack()


lblA = tk.Label(window, text="Value 1: ", fg="#383a39", bg="#FFFFFF")
entlblA = tk.Entry(window)


lblB = tk.Label(window, text="Value 1: ", fg="#383a39", bg="#FFFFFF")
entlblB = tk.Entry(window)


lblC = tk.Label(window, text="Value 1: ", fg="#383a39", bg="#FFFFFF")
entlblC = tk.Entry(window)

lblA.pack()
entlblA.pack()
lblB.pack()
entlblB.pack()
lblC.pack()
entlblC.pack()


btn = tk.Button(window, text="Get Solving", command=lambda: quadraticSolver(), fg="#383a39", bg="#FFFFFF")
btn.pack()


window.geometry("600x600")
window.mainloop()









