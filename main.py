import sys
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
import keyboard
import time

def main_task(intArr, duration):
    dir = 'right'
    for x in intArr:
        print(x)
        if x<0:
            dir = 'left'
            x*=-1
        else:
            dir = 'right'
        i=0
        while i<x:
            print(dir)
            keyboard.press_and_release(dir)
            time.sleep(duration)
            i+=1

class PyHandler(QObject):
    @Slot(str, str, bool)
    def handleDone(self, input1, input2, reverse):
        print(reverse)
        try:
            print(f"Raw input1: '{input1}'")
            print(f"Raw input2: '{input2}'")
            int_array = list(map(int, input1.replace(',', ' ').split()))
            input2 = int(input2)
            
            print(f"Array from textfield 1: {int_array}")
            print(f"Integer from textfield 2: {input2}")
            print('\n\nIt will start to work in 5 seconds. Focus on instagram.')
            time.sleep(5)
            while True:
                main_task(int_array,input2)
                if reverse:
                    int_array=int_array[::-1]

        except ValueError:
            print("Invalid input: Make sure to enter integers in the correct format.")

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    pyHandler = PyHandler()
    engine.rootContext().setContextProperty("pyHandler", pyHandler)

    engine.load("ui.qml")

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()