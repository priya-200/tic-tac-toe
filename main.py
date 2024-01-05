from tkinter import *
from tkinter import font

CLICK_NUMBER = 0


def button_click(button):
    global CLICK_NUMBER
    current_text = button.cget("text")
    print(current_text)
    if current_text == '':
        if CLICK_NUMBER % 2 == 0:
            button.config(text='X', fg='red', font=font.Font(size=24, weight="bold"))
            display.config(text='O Turn To Play', fg='green')
        else:
            button.config(text='O', fg='green')
            display.config(text='X Turn To Play', fg='red')

        if finish():
            window.destroy()
            windows = Tk()
            windows.title('tic-tac-toe')
            if CLICK_NUMBER % 2 == 0:
                winner = Label(windows, text='Winner is X', font=font.Font(size=28, weight="bold"))
            else:
                winner = Label(windows, text='Winner is O', font=font.Font(size=28, weight="bold"))
            winner.grid(row=0, column=0)
        else:
            if CLICK_NUMBER == 8:
                display.config(text='Tie Match', fg='blue')
            else:
                CLICK_NUMBER += 1


def finish():
    for row in range(3):
        if buttons[row][0].cget('text')== buttons[row][1].cget('text') == buttons[row][2].cget('text') != '':
            return True
    for col in range(3):
        if buttons[0][col].cget('text') == buttons[1][col].cget('text') == buttons[2][col].cget('text') != '':
            return True
    if buttons[0][0].cget('text') == buttons[1][1].cget('text') == buttons[2][2].cget('text') != '':
        return True
    if buttons[0][2].cget('text') == buttons[1][1].cget('text') == buttons[2][0].cget('text') != '':
        return True
    return False


def create_button(row, col):
    return Button(
        text='',
        font=font.Font(size=24, weight="bold"),
        fg="black",
        width=8,
        height=4,
        bd=2,
        relief="solid",
        highlightthickness=9,
        highlightbackground="lightblue",
        command=lambda row=row, col=col: button_click(buttons[row - 1][col - 1])
    )


window = Tk()
window.title('tic-tac-toe')

display_frame = Frame(window)
display_frame.grid(row=0, column=0, columnspan=3)

display = Label(master=display_frame, text='Ready?', font=font.Font(size=28, weight="bold"))
display.grid(row=0, column=0, columnspan=3, pady=20, padx=10)

for i in range(1, 4):
    window.rowconfigure(i, weight=1, minsize=100)
    window.columnconfigure(i, weight=1, minsize=100)

buttons = [[create_button(row, col) for col in range(1, 4)] for row in range(1, 4)]

for row in range(1, 4):
    for col in range(1, 4):
        buttons[row - 1][col - 1].grid(row=row, column=col, padx=5, pady=5)

window.mainloop()
