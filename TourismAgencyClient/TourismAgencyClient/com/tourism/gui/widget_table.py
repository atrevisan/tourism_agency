import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
  
class MyTable(QTableWidget):
    """Encapsulates a table widget.
    
    data : dict
        Map column names to list containing column elements.
     
    args : int
        dimensions
    """

    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def setmydata(self):
        """Add elements to the table."""

        horHeaders = []
        for n, key in enumerate(self.data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

    def get_row(self, row_index, number_of_columns):
        """Get elements of the row and remove it.
        
        Parameters
        -----------
        row_index : int
            The index of the row to be rempved.

        number_of_columns : int
            The horizontal width of this table.

        Returns
        --------
        row : list of str
            Elements of the row.
        """

        row = []
        for column_index in range(number_of_columns):

            row.append(self.item(row_index, column_index).text())

        self.removeRow(row_index)

        return row

    def get_column(self, column_index, number_of_rows):
        """Get elements of the column and remove it.
        
        Parameters
        -----------
        column_index : int
            The index of the column to be removed.

        number_of_rows : int
            The width width of this table.

        Returns
        --------
        column : list of str
            Elements of the column.
        """

        column = []
        for row_index in range(number_of_rows):

            column.append(self.item(row_index, column_index).text())

        self.removeColumn(column_index)

        return column
