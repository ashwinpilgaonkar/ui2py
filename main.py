"""
TODO: Shift Text UI to right center
      Reference Help and About from UI and point to MenuHandler
      Implement Drag and Drop
      Resize messageboxes
      resize mainwindow
~Ashwin Pilgaonkar~
"""
from PyQt5 import QtWidgets
import sys
import os
import design
import tkinter.filedialog

class ui2py(QtWidgets.QMainWindow, design.Ui_ui2py):

    # Set initial path to current working directory
    savedir = os.getcwd()

    def __init__(self, parent=None):
        super(ui2py, self).__init__(parent)
        self.setupUi(self)
        self.OpenButton.clicked.connect(self.OpenUI)
        self.SaveButton.clicked.connect(self.Convert)
        self.ClearButton.clicked.connect(self.Clear)

        #MenuBar items (needs to be redone)
        bar = self.menuBar()
        help = bar.addMenu("Help")
        help.addAction("Usage")
        help.triggered[QtWidgets.QAction].connect(self.MenuHandler)

        about = bar.addMenu("About")
        about.addAction("Info")
        about.triggered[QtWidgets.QAction].connect(self.MenuHandler)

    def OpenUI(self):
        #Hides the Tkinter window
        root = tkinter.Tk()
        root.withdraw()

        count=0
        pathtext=""

        filepath = tkinter.filedialog.askopenfiles(initialdir=self.savedir, title="Select File", filetypes=(("PyQt Designer UI Files", "*.ui"), ("", "")))

        #Save the path of the selected file for easier selection
        self.savedir = filepath

        for file in self.savedir:
            #Check if file extension is *.ui
            if filepath[count].name[len(filepath[count].name)-1]!='i' and filepath[count].name[len(filepath[count].name)-2]!='u' :
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Oops, Wrong file!")
                msg.setInformativeText("Please select a QtDesigner *.ui file.")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                self.Clear()

            else:
                pathtext = pathtext + filepath[count].name + "   "
                count = count+1

                #Update UI elements
                self.SelectedFilesLabel.setText("%d files selected" %count)
                self.PathLabel.setText(pathtext)

    def Convert(self):
        #If no files are selected
        if isinstance(self.savedir, str):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Oops! No files selected")
            msg.setInformativeText("Please select one or more files.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        else:
            for file in self.savedir:
                #Change extension of output file to .py
                pyname = file.name
                pyname = pyname[:len(pyname)-2] + pyname[len(pyname):]
                pyname = pyname + "py"
                os.system("pyuic5 "+file.name+" -o "+pyname)
                self.PathLabel.setText("Done!")

    def Clear(self):
        #Clear UI Elements
        self.SelectedFilesLabel.setText("No files selected")
        self.PathLabel.setText("")

    #~~~~~~~~~~~~~~~~~~~~
    #needs to be implemented
    def MenuHandler(self):
        mode = 0
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        if mode==0:
            msg.setText("Usage:")
            msg.setInformativeText("WIP.")
            msg.setWindowTitle("Help")

        else:
            msg.setText("ui2py")
            msg.setInformativeText("Created by Ashwin Pilgaonkar")
            msg.setWindowTitle("About")

        msg.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ui2py()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()