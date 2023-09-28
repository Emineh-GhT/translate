from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from googletrans import Translator

class TranslationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('design.ui')
        self.ui.show()
        self.ui.setWindowTitle('translate')
        self.ui.translate_entofa_btn.clicked.connect(self.translate_entofa)
        self.ui.translate_fatoen_btn.clicked.connect(self.translate_fatoen)
        self.ui.clear_btn.clicked.connect(self.clear)

    def translate_entofa(self):
        text = self.ui.tb_in.text()
        translator = Translator()
        translation = translator.translate(text, dest='fa')  # Translate to Persian
        self.ui.tb_out.setText(translation.text)

    def translate_fatoen(self):
        text = self.ui.tb_in.text()
        translator = Translator()
        translation = translator.translate(text, dest='en')  # Translate to English
        self.ui.tb_out.setText(translation.text)

    def clear (self) :
        self.ui.tb_in.setText('')
        self.ui.tb_out.setText('')



app = QApplication([])
window = TranslationWindow()
app.exec()