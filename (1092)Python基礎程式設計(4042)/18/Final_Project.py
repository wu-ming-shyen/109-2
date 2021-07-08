#?A?B GAME
import random
import tkinter

Anser = ''
Guess = ''
Times = ''
#重新開始遊戲
def newGame():
    global Anser
    global Times
    Times = 0
    ResultLable.config(text = "Result : ")
    TimesLable.config(text = "Guess Times : " + str(Times))
    Anser = "".join(map(str, random.sample(range(0, 10), 4)))
    print(Anser)
#計算幾A幾B並顯示
def xAxB():
    global Anser
    global Guess
    global Times
    Guess = GuessInput.get()
    if (len(Guess)) == 4:
        Times += 1
        A = xA(Guess)
        B = xB(Guess)
        show_xAxB(A, B)
    else:
        tkinter.messagebox.showinfo("Remind", "Digits is " + str(4))
#計算幾個A
def xA(Guess):
    global Anser
    A = 0
    for i in range(len(Anser)):
        if (Guess[i] == Anser[i]):
            A = A + 1
    return A
#計算幾個B
def xB(Guess):
    global Anser
    B = 0
    for i in range(len(Anser)):
        for j in range(len(Anser)):
            if (i != j):
                if (Guess[i] == Anser[j]):
                    B = B + 1
    return B
#顯示結果
def show_xAxB(A, B):
    if (A == 4):
        result = "You Win!"
    else:
        result = "Result : " + str(A) + "A" + str(B) + "B"
    ResultLable.config(text = result)
    TimesLable.config(text = "Guess Times : " + str(Times))
#建立視窗
Window = tkinter.Tk()
Window.title("?A?B GAME!")
Window.geometry("720x360")
#設定物件
Window.config(bg="#FFF9E3")
GuessInput = tkinter.Entry(Window, font=("Arial", 20))
ResultLable = tkinter.Label(Window, text = "Result : ", font=("Arial", 20), bg="#FFC0FB")
TimesLable = tkinter.Label(Window, text = "Guess Times : ", font=("Arial", 20), bg="#FFC0FB")
GuessLable = tkinter.Label(Window, text = "Guess Number : ", font=("Arial", 20), bg="#FFC0FB")
GuessButton = tkinter.Button(Window, text = "Guess", font=("Arial", 20), bg="#DFFF00", command = xAxB)
NewGameButton = tkinter.Button(Window, text = "New Game", font=("Arial", 20), bg="#DFFF00", command = newGame)
#配置物件
GuessLable.grid(row=0, column=0)
GuessInput.grid(row=0, column=1)
GuessButton.grid(row=0, column=2)
ResultLable.grid(row=1, column=0)
TimesLable.grid(row=2, column=0)
NewGameButton.grid(row=2, column=2)
#呼叫newGame
newGame()
Window.mainloop()

