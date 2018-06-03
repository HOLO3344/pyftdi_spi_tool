import sys

import numpy as np

try:
    sys.path.append("../ui")
    sys.path.append("../image")
    from pc_tool import Ui_MainWindow
except Exception as e:
    print(e)
finally:
    pass

from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QRegExp


COLUMN_COUNT = 8    # display table is 8 columns per row
REG_BYTE_WIDTH = 4  # register is four bytes width


class my_app(QMainWindow, Ui_MainWindow):
    """docstring for my_app"""

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.button_read_spi_reg.clicked.connect(self.on_button_read_spi_reg)
        self.button_read_cambridge_mem.clicked.connect(self.on_button_read_cambridege_mem)

        self.tablewidget_cambridge_mem.setColumnCount(COLUMN_COUNT)
        self.tablewidget_cambridge_mem.cellChanged.connect(self.on_tablewidget_cambridge_mem_cell_changed)
        self.fresh_memory_table()

        self.lineedit_address.setInputMask("HHHHHHHH")
        self.lineedit_address.setPlaceholderText("AABBCCDD")

        self.is_fresh_memory_table = False

    def on_button_read_spi_reg(self):
        print("on_button_read_spi_reg")

    def on_button_read_cambridege_mem(self):
        print("on_button_read_cambridege_mem")
        try:
            text = self.lineedit_address.text()
            if len(text) != 8:
                QMessageBox.warning(self, "Error", "Address format error!")
            else:
                add = int(self.lineedit_address.text(), 16)
                print(hex(add))
                reg_val = self.generation_random_arr()
                self.fresh_memory_table(add, reg_val)
        except Exception as e:
            print("Error: " + str(e))
        finally:
            pass

    def fresh_memory_table(self, start_addr=0x60000000, reg_val=list(range(0x100))):
        self.is_fresh_memory_table = True
        row_cnt = int(len(reg_val) / COLUMN_COUNT)
        self.tablewidget_cambridge_mem.setRowCount(row_cnt)
        for i in list(range(row_cnt)):
            addr_str = hex(start_addr)
            start_addr += (REG_BYTE_WIDTH * COLUMN_COUNT)
            item = QTableWidgetItem(addr_str)
            self.tablewidget_cambridge_mem.setVerticalHeaderItem(i, item)

        for row in list(range(row_cnt)):
            for col in list(range(COLUMN_COUNT)):
                val_str = str.format("0x%08x" % reg_val[COLUMN_COUNT * row + col])
                item = QTableWidgetItem(val_str)
                self.tablewidget_cambridge_mem.setItem(row, col, item)

        self.is_fresh_memory_table = False

    def generation_random_arr(self, len=0x100):
        arr = np.random.randint(0, 0x7FFFFFFF, len)
        return arr

    def on_tablewidget_cambridge_mem_cell_changed(self, row, col):
        if not self.is_fresh_memory_table:
            print("row = %d, col = %d" % (row, col))
            par = QRegExp(r"^0x[0-9A-Fa-f]{8}")
            item = self.tablewidget_cambridge_mem.item(row, col)
            if not par.exactMatch(item.text()):
                QMessageBox.warning(self, "Error", "Input data error, input format: 0xhhhhhhhh")
                self.tablewidget_cambridge_mem.setItem(row, col, QTableWidgetItem("0x00000000"))
            else:
                print(item.text())
                reg_val = int(item.text(), 16)
                print(hex(reg_val))


if __name__ == '__main__':
    print("App start...")
    app = QApplication(sys.argv)
    window = my_app()
    window.show()
    sys.exit(app.exec_())
