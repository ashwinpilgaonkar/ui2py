# ui2py
A nifty GUI utility that batch converts QtDesigner *.ui files to .py files

## Installation
* Requires PyQt5   `pip install pyqt5`
* Create a file named pyuic5.bat (if it doesn't exist already) with the following contents-
* `python -m PyQt5.uic.pyuic %1 %2 %3 %4 %5 %6 %7 %8 %9`
* Add it to **PATH**

## Usage
* Click **Open** to import *.ui files
* Supports batch conversion / Multiple file selection
* Click **Convert** to convert it to a .py file (saved in the same directory)
* Click **Clear** to clear the batch

## Screenshots
![ui2py](https://cloud.githubusercontent.com/assets/13731530/25042879/35036d26-2139-11e7-843d-9a4eb5d2bd96.png)
