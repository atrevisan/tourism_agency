# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4
from PyQt4.QtGui import QMessageBox

from collections import OrderedDict

from com.tourism.gui.ui_widget_packages import Ui_widget_packages
from com.tourism.gui.widget_table import MyTable
from com.tourism.webservice.webservice_handler import WebserviceHandler

class WidgetPackages(QWidget, Ui_widget_packages):
    """This widget is intended for travel packages display and revenue.
    
    The user can visualize the available travel packages and purchase one of them.

    Atributes
    -----------
    guest_ages : dict
        Map the pack id to its associated guest agest
        for display in another table when the row of this
        pack is selected.

    table_packs : MyTable
        Table for displaying the avalilable packs for purchase.
        Allows the user to selected one package for purchase.

    table_chosen_package : MyTable
        This table display the package chosen by the user.
        If the user wants he can remove it and choose
        another package.

    table_guests : MyTable
        This table displays the ages for the number of 
        guests that can be acomodated at the destination.
    """
    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        handler = WebserviceHandler()
        travel_packs = handler.get_travel_packs()

        ids = []
        origins = []
        destinations = []
        departure_dates = []
        arrival_dates = []
        number_of_rooms = []
        are_promo = []
        self.guest_ages = {}

        for travel_pack in travel_packs:

            ids.append(str(travel_pack.id))
            origins.append(travel_pack.origin)
            destinations.append(travel_pack.destination)
            departure_dates.append("%d/%d/%d" % (travel_pack.departureDay, travel_pack.departureMonth, travel_pack.departureYear))
            arrival_dates.append("%d/%d/%d" % (travel_pack.arrivalDay, travel_pack.arrivalMonth, travel_pack.arrivalYear))
            number_of_rooms.append(str(travel_pack.numberOfRooms))
            are_promo.append("yes" if travel_pack.isPromo else "no")
            self.guest_ages[str(travel_pack.id)] = travel_pack.guestAges

        data = OrderedDict([('id', ids),
                            ('origin', origins), 
                            ('destination', destinations), 
                            ('departure date', departure_dates), 
                            ('arrival date', arrival_dates),
                            ('rooms', number_of_rooms),
                            ("is promo", are_promo)])

        self.table_packs = MyTable(data, len(origins), 7)
        self.vlayout_table_content.addWidget(self.table_packs)

        data = OrderedDict([('id', []),
                            ('origin', []), 
                            ('destination', []), 
                            ('departure date', []), 
                            ('arrival date', []),
                            ('rooms', []),
                            ("is promo", [])])
        self.table_chosen_package = MyTable(data, 0, 7)
        self.vlayout_chosen_package.addWidget(self.table_chosen_package)

        data = OrderedDict([('Guest age', [])])
        self.table_guests = MyTable(data, 0, 1)
        self.vlayout_guest_ages.addWidget(self.table_guests)

        # event handling
        self.button_choose_package.clicked.connect(self.choose_package)
        self.button_remove_package.clicked.connect(self.remove_package)
        self.table_packs.clicked.connect(self.display_ages)

    def choose_package(self):
        """Get the selected package and add it to another table.
        
        The table to wich the package is added contains the
        package that the user is intended to buy.
        """

        if self.table_chosen_package.rowCount() == 0:
            
            row_index = self.table_packs.currentRow()
            row = self.table_packs.get_row(row_index, self.table_packs.columnCount())

            self.table_chosen_package.insertRow(0)
            self.table_chosen_package.setItem(0 , 0, QtGui.QTableWidgetItem(row[0]))
            self.table_chosen_package.setItem(0 , 1, QtGui.QTableWidgetItem(row[1]))
            self.table_chosen_package.setItem(0 , 2, QtGui.QTableWidgetItem(row[2]))
            self.table_chosen_package.setItem(0 , 3, QtGui.QTableWidgetItem(row[3]))
            self.table_chosen_package.setItem(0 , 4, QtGui.QTableWidgetItem(row[4]))
            self.table_chosen_package.setItem(0 , 5, QtGui.QTableWidgetItem(row[5]))
            self.table_chosen_package.setItem(0 , 6, QtGui.QTableWidgetItem(row[6]))

       
    def remove_package(self):
        """Remove a chosen package so the user can chose another one."""

        row = self.table_chosen_package.get_row(0, self.table_chosen_package.columnCount())

        new_row_index = self.table_packs.rowCount()
        self.table_packs.insertRow(new_row_index)
        
        self.table_packs.setItem(new_row_index , 0, QtGui.QTableWidgetItem(row[0]))
        self.table_packs.setItem(new_row_index , 1, QtGui.QTableWidgetItem(row[1]))
        self.table_packs.setItem(new_row_index , 2, QtGui.QTableWidgetItem(row[2]))
        self.table_packs.setItem(new_row_index , 3, QtGui.QTableWidgetItem(row[3]))
        self.table_packs.setItem(new_row_index , 4, QtGui.QTableWidgetItem(row[4]))
        self.table_packs.setItem(new_row_index , 5, QtGui.QTableWidgetItem(row[5]))
        self.table_packs.setItem(new_row_index , 6, QtGui.QTableWidgetItem(row[6]))



    def display_ages(self):
        """Add the associated guest ages to the table when selected."""

        self.table_guests.setRowCount(0)
        self.table_guests.setColumnCount(1)

        selected_row_index = self.table_packs.currentRow()

        column = self.guest_ages[self.table_packs.item(selected_row_index, 0).text()]

        for row_index in range(len(column)):

            new_row_index = self.table_guests.rowCount()
            self.table_guests.insertRow(new_row_index)

            self.table_guests.setItem(new_row_index , 0, QtGui.QTableWidgetItem(str(column[row_index])))