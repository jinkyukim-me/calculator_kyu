# tkinter 모듈 추가
import tkinter as tk

# 이름과 사이즈 설정
calculator = tk.Tk()
calculator.title("Jinkyu Calulator")
calculator.geometry("500x500")

# func 함수
def func(event):
    print('this is test message!')

# display이라는 이름의 출력장 추가, 폭은 25
display = tk.Entry(calculator, width=25)

# 위치를 정해는주는 명령어
display.pack()

# Bind Key Input
calculator.bind('<Return>',func)

calculator.mainloop()
