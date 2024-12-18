# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from interface_Grafica.ui_form import Ui_Dialog
#important:
#yOU

#É neste arquivo onde será dado todas ações ou funções dos comandos da interface gráfica
class Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.browseButton.clicked.connect(self.browse_file)#Este botão não existe, apenas foi gerado pelo QT para exemplificar como executamos os botões
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
