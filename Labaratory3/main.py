from tkinter import *


def getPositiveAndNegativeValues(event):
    inputtedString = inputField.get()
    result = list(map(int, inputtedString.split(',')))
    negativeValues = []
    positiveValues = []
    zeroValues = []
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


root = Tk()
root.title("Positive and Negative values")
root.geometry("800x300+600+200")
root.resizable(False, False)

label = Label(root, text="Enter here your values: ", font='16')
label.grid(row=0, column=0)

infoLabel = Label(root, text="Correct input example: -2, 45, 0, 11, 235, 18", font='16')
infoLabel.place(x=250, y=250)

inputField = Entry(root, font='16', width=60)
inputField.grid(row=0, column=1)

allocationButton = Button(root, text="Allocate", bg='green', fg='white', font=16, padx=13)
allocationButton.grid(row=0, column=2)

allocationButton.bind('<Button-1>', getPositiveAndNegativeValues)

positiveValuesLabel = Label(root, font='16')
positiveValuesLabel.grid(columnspan=2, sticky=W)

negativeValuesLabel = Label(root, font='16')
negativeValuesLabel.grid(columnspan=2, sticky=W)

zeroValuesLabel = Label(root, font='16')
zeroValuesLabel.grid(columnspan=2, sticky=W)

root.mainloop()
