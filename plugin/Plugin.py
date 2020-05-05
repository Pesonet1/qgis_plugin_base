# -*- coding: utf-8 -*-

from .PluginDialog import PluginDialog
from .WindowDialog import WindowDialog

from ..utilities.DbConnection import DbConnection

class Plugin:
    """ Plugin base constructor """

    def __init__(self, iface):
        self.iface = iface
        self.dlg = PluginDialog()
        # self.db = DbConnection()

        self.dlg.close_button.clicked.connect(self.__closeDialog)
        self.dlg.open_window_button.clicked.connect(self.__openWindowDialog)

    def __closeDialog(self):
        """ Closes dialog """

        self.dlg.close()

    def __openWindowDialog(self):
        """ Opens window dialog """

        self.windowDialog = WindowDialog(parent=None)

        if self.windowDialog.exec_():
          print('ok pressed')
        else:
          print('cancel pressed')
