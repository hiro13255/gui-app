# coding:utf-8

import tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import ttk

count = 0
StringBox = 0
combo = ""

exchange = {
    "こんにちは":"Hello",
    "いくらですか？":"How much is it?",
    "おげんきですか？":"How are you?"
}

class ButtonFunction():
    # ボタン押下時カウントがいくつか表示する
    def Total(event):
        inputString = StringBox.get()
        translation = combo.get()
        if (translation in exchange.keys()):
            transDisplay = exchange.get(translation)
        tkMessageBox.showinfo('確認', '合計=' + str(count) +
                              '押されました.\n[message]' + inputString + "[" + transDisplay + "]")

    # ボタンが押されたら+1する関数
    def CountUp(event):
        global count
        count += 1
        CountLabel['text'] = str(count)

    # ボタンが押されたら-1する関数
    def CountDown(event):
        global count
        if count > 0:
            count -= 1
        CountLabel['text'] = str(count)


def Display():
    global CountLabel
    global StringBox
    global combo
    # 画面表示
    root = tkinter.Tk()

    # ウィンドウ名
    root.title("sample")

    # ウィンドウの大きさを設定
    root.geometry("550x600")

    # ラベル表示
    Label1 = tkinter.Label(text="Hello World!")
    Label1.pack()

    CountLabel = tkinter.Label(text='0')
    CountLabel.pack()

    # ボタン表示
    TotalButton = tkinter.Button(text="合計表示")
    TotalButton.bind("<Button-1>", ButtonFunction.Total)
    TotalButton.place(x=245, y=80)

    CountButton = tkinter.Button(text='カウントアップ')
    CountButton.bind("<Button-1>", ButtonFunction.CountUp)
    CountButton.place(x=170, y=50)

    CountButton = tkinter.Button(text='カウントダウン')
    CountButton.bind("<Button-1>", ButtonFunction.CountDown)
    CountButton.place(x=285, y=50)

    # エントリーボックス表示
    '''
	日本語入力だと確定前の文字が表示されない
	'''
    StringBox = tkinter.Entry(width=50)
    StringBox.place(x=50, y=110)

    # プルダウン表示
    combo = ttk.Combobox(root, state="readonly", width=15)
    combo["values"] = ("こんにちは", "いくらですか？", "気分はどうですか？")
    combo.place(x=180, y=150)

    root.mainloop()


if __name__ == '__main__':
    Display()
