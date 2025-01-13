# This Python file uses the following encoding: utf-8
import sys
#from reconhecimento import*
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QVBoxLayout, QLabel
from PySide6.QtCore import Qt  # Para usar Qt.AlignCenter, Qt.KeepAspectRatio, etc.
from PySide6.QtGui import QPixmap  # Para carregar e exibir imagens
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#from interface_Grafica.ui_form import Ui_Dialog
from ui_form import Ui_Dialog
#from controler.reconhecimento import *
#important:
#yOU

#É neste arquivo onde será dado todas ações ou funções dos comandos da interface gráfica
class Dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.ui.browseButton.clicked.connect(self.browse_file)#Este botão não existe, apenas foi gerado pelo QT para exemplificar como executamos os botões
        self.ui.botao_procura_imagem.clicked.connect(self.procurar_imagem)
        self.ui.botao_reconhecer.clicked.connect(self.reconhecer_imagem)
        
    #################################################################################################################################
    def procurar_imagem(self):
        diretorio_inicial = "projeto de reconhecimento facial poo/imagens"
        # Abre uma janela de diálogo para selecionar arquivos
        caminhos_imagens, _ = QFileDialog.getOpenFileNames(
            self,  # Janela pai
            "Selecione as Imagens",  # Título da janela
            diretorio_inicial,  # Diretório inicial (vazio para o diretório padrão)
            "Imagens (*.jpg *.png *.jpeg)"  # Filtro de tipos de arquivo
        )

        if caminhos_imagens:  # Se o usuário selecionou alguma imagem
            # Carrega a imagem usando QPixmap
            pixmap = QPixmap(caminhos_imagens)
            # Redimensiona a imagem para caber no QLabel (opcional)
            pixmap = pixmap.scaled(
                self.ui.widget.width(),  # Largura do QLabel
                self.ui.widget.height(),  # Altura do QLabel
                Qt.AspectRatioMode.KeepAspectRatio   # Mantém a proporção da imagem
            )

            # Exibe a imagem no wiget
            self.ui.widget.setStyleSheet(f"background-image: url({caminhos_imagens[0]}); background-repeat: no-repeat; background-position: center;")
            
            # Aqui você pode carregar as imagens e processá-las
            #imagens_treino = [cv2.imread(caminho, cv2.IMREAD_GRAYSCALE) for caminho in caminhos_imagens]
            QMessageBox.information(self, "Sucesso", "Imagens carregadas com sucesso!")
    #########################################################################################################################################           
    
    
    def reconhecer_imagem(self):
        pass
    ##################################################################################################################
    
    def pixelar_imagem(self):
        pass


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
