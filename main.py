from PyQt5 import QtWidgets
import sys
import os
import design
import tkinter.filedialog

#Set initial path to current working directory
savedir = os.getcwd()

class ui2py(QtWidgets.QMainWindow, design.Ui_ui2py):

    def __init__(self, parent=None):
        super(ui2py, self).__init__(parent)
        self.setupUi(self)
        self.OpenButton.clicked.connect(self.OpenUI)
        self.SaveButton.clicked.connect(self.Convert)

    def OpenUI(self):
        global savedir

        #Hides the Tkinter window
        root = tkinter.Tk()
        root.withdraw()

        filepath = tkinter.filedialog.askopenfiles(initialdir=savedir, title="Select File", filetypes=(("PyQt Designer UI Files", "*.ui"), ("", "")))

        #Save the path of the selected file for easier selection
        savedir = filepath

    def Convert(self):

        if isinstance(savedir, str):
            print("No file selected")

        else:
            for file in savedir:
                #Change extension of output file to .py
                pyname = file.name
                pyname = pyname[:len(pyname)-2] + pyname[len(pyname):]
                pyname = pyname + "py"
                print("pyuic5 "+file.name+" -o "+pyname)
                os.system("pyuic5 "+file.name+" -o "+pyname)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ui2py()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()