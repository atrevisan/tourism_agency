# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from com.tourism.gui.main_window import MainWindow    


# Main entry to the program.  Sets up the main app and create a new window.
def main(argv):
 
    # create Qt application
    app = QApplication(argv)
 
    # create main window
    wnd = MainWindow() # classname
    wnd.show()
 
    # Connect signal for app finish
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
 
    # Start the app up
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main(sys.argv)
