from tkinter import *
#імпортуємо біблотеку інтерфейсу користувача

def getPositiveAndNegativeValues(event):
    inputtedString = inputField.get()
    # зчитуємо ввід даних
    result = list(map(int, inputtedString.split(',')))
    negativeValues = []
    positiveValues = []
    zeroValues = []
    # розділяємо на три масива додатніх, від'ємних та нульових значень
    for i in result:
        if i > 0:
            positiveValues.append(i)
            positiveValuesLabel["text"] = "Array of positive values: " + str(positiveValues)
        elif i < 0:
            negativeValues.append(i)
            negativeValuesLabel["text"] = "Array of negative values: " + str(negativeValues)
        else:
            zeroValues.append(i)
            zeroValuesLabel["text"] = "Array of zero's values: " + str(zeroValues)
#розкидуємо значення по масивам, додаючи в кінець кожне


root = Tk()
root.title("Positive and Negative values")
root.geometry("800x300+600+200")
root.resizable(False, False)
#розміри форми

label = Label(root, text="Enter here your values: ", font='16')
label.grid(row=0, column=0)
#налаштування інформаційних міток

infoLabel = Label(root, text="Correct input example: -2, 45, 0, 11, 235, 18", font='16')
infoLabel.place(x=250, y=250)
#налаштування мітки підказки

inputField = Entry(root, font='16', width=60)
inputField.grid(row=0, column=1)
#налаштування поля вводу

allocationButton = Button(root, text="Allocate", bg='green', fg='white', font=16, padx=13)
allocationButton.grid(row=0, column=2)

allocationButton.bind('<Button-1>', getPositiveAndNegativeValues)
#налаштування кнопки розподілення

positiveValuesLabel = Label(root, font='16')
positiveValuesLabel.grid(columnspan=2, sticky=W)

negativeValuesLabel = Label(root, font='16')
negativeValuesLabel.grid(columnspan=2, sticky=W)

zeroValuesLabel = Label(root, font='16')
zeroValuesLabel.grid(columnspan=2, sticky=W)
#налаштування міток для виводу трьох розділених масивів

root.mainloop()