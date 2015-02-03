# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QMainWindow

from com.tourism.gui.ui_main_window import Ui_main_window
from com.tourism.gui.widget_register_travel_pack import WidgetRegisterTravelPack
from com.tourism.gui.widget_packages import WidgetPackages
from com.tourism.gui.widget_register_plane_ticket import WidgetRegisterPlaneTicket
from com.tourism.gui.widget_plane_tickets import WidgetPlaneTickets

class MainWindow(QMainWindow, Ui_main_window):
    """The application main window."""

    def __init__(self):

        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

        # custom event handling
        self.button_register_travel_pack.clicked.connect(self.add_widget_register_travel_pack)
        self.button_packages.clicked.connect(self.add_widget_packages)
        self.button_register_plane_ticket.clicked.connect(self.add_widget_register_plane_ticket)
        self.button_plane_tickets.clicked.connect(self.add_widget_plane_tickets)

    def add_widget_packages(self):
        """Replaces the current widget for the widget packages."""
        widget_packages = WidgetPackages()

        self.clear_layout()
        self.vlayout_content.addWidget(widget_packages)
                
    def add_widget_plane_tickets(self):
        """Replaces the current widget for the widget plane tickets."""
        widget_plane_tickets = WidgetPlaneTickets()

        self.clear_layout()
        self.vlayout_content.addWidget(widget_plane_tickets)

    def add_widget_register_travel_pack(self):
        """Replaces the current widget for the widget register travel pack."""

        widget_register_travel_pack = WidgetRegisterTravelPack()

        self.clear_layout()
        self.vlayout_content.addWidget(widget_register_travel_pack)

    def add_widget_register_plane_ticket(self):
        """Replaces the current widget for the widget register plane ticket."""

        widget_register_plane_ticket = WidgetRegisterPlaneTicket()

        self.clear_layout()
        self.vlayout_content.addWidget(widget_register_plane_ticket)

    def clear_layout(self):
        """Remove all the widgets from the main layout."""
        
        while self.vlayout_content.count():
            child = self.vlayout_content.takeAt(0)
            child.widget().deleteLater()
    