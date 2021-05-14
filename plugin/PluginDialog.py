# -*- coding: utf-8 -*-
import os

from PyQt5 import uic
from PyQt5 import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'plugin_dialog_base.ui'))

class PluginDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
  
        super(PluginDialog, self).__init__(parent)

        self.setupUi(self)
