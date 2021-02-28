
import element
from tkinter import *
import webbrowser

def importData(dataFile):
    data = open("data.txt", "r").readlines()
    elements = []
    for el in data:
        el = el.rstrip().split()
        x = element.Element(el[0], el[1], int(el[2]), float(el[3]), int(el[4]), int(el[5]))
        elements.append(x)
    return elements

def setBackgroundColours(allElements):
    backgroundColours = len(allElements)*["white"]
    for i in range(len(allElements)):
        el = allElements[i]
        if el.getGroup() == 18 and el.getPeriod() < 7:
            backgroundColours[i] = "green"
        elif el.getGroup() == 1 and el.getPeriod() >= 2:
            backgroundColours[i] = "red"
        elif el.getGroup() == 2:
            backgroundColours[i] = "orange"
        elif 3 <= el.getGroup() <= 11 and el.getPeriod() < 10:
            backgroundColours[i] = "pink"
        elif (el.getGroup() == 12 and el.getPeriod() < 10) or (el.getGroup() == 13 and 3 <= el.getPeriod() <= 6) or el.getSymbol() in ["Sn", "Pb", "Bi", "Po"]:
            backgroundColours[i] = "gray"
        elif el.getPeriod() >= 10:
            backgroundColours[i] = "white"
        elif el.getSymbol() in ["H", "C", "N", "O", "F", "P", "S", "Cl", "Se", "Br", "I"]:
            backgroundColours[i] = "yellow"
        elif el.getSymbol() in ["B", "Si", "Ge", "As", "Sb", "Te", "At"]:
            backgroundColours[i] = "light gray"

    return backgroundColours

def displayElement(el):
    #data = "%.2f\n\n %s \n\n %s \n\n%d" %(el.getMass(), el.getSymbol(), el.getName(), el.getAtomicNumber())
    mass.set(float("%.2f" %el.getMass()))
    symbol.set(el.getSymbol())
    name.set(el.getName())
    atomicNumber.set(el.getAtomicNumber())

def elementLabel(el):
    data = "\n%s\n" % (el.getSymbol())
    e = Button(root, text = data, width = 5, relief = "sunken", command = lambda: displayElement(el), background = colours[el.getAtomicNumber()-1], font=("serif", 10, "bold"))
    e.grid(row=el.getPeriod(), column = el.getGroup())

def openWiki(name):
    print(name)
    url = "https://en.wikipedia.org/wiki/"+name
    webbrowser.open(url) 

dataFile = "data.txt"

root = Tk()
root.title("Periodic table")
root.geometry("910x610")
Label(root, text = "PERIODIC TABLE OF ELEMENTS", font=("serif", 24)).grid(row=0, columnspan = 18)

elements = importData(dataFile)
colours = setBackgroundColours(elements)


for i in elements:
    elementLabel(i)

test = "1.01\n H \n Helium \n1"
h = elements[0]
f = Frame(root, relief = "sunken", highlightbackground="black", borderwidth=2)


mass = DoubleVar(f)
mass.set(float("%.2f" %h.getMass()))
symbol = StringVar(f)
symbol.set(h.getSymbol())
name = StringVar(f)
name.set(h.getName())
atomicNumber = IntVar(f)
atomicNumber.set(h.getAtomicNumber())

Label(f, textvariable = mass, width = 10, anchor="w").grid(row=0)
Label(f, textvariable = symbol, width = 5, font=("serif", 20)).grid(row=1)
Label(f, textvariable = name, width = 10).grid(row=2)
Label(f, textvariable = atomicNumber, width = 10, anchor="w").grid(row=3)

displayElement(elements[0]) #to display hydrogen info as default
f.grid(row=1, rowspan=3, column=7, columnspan=3)

infoButton = Button(root, text = "Open Wiki", command = lambda: openWiki(name.get())).grid(row = 2, column = 10, columnspan = 2)

Label(root, text="").grid(row=9, column = 0) #blank label for spacing
root.mainloop()

#https://en.wikipedia.org/wiki/ELEMENT_NAME