'''import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("say anything")
    audio = r.listen(source)
# Speech recognition using Google Speech Recognition
try:
    print("انت قولت: " + r.recognize_google(audio,language ="ar-AR"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))'''
'''from gtts import gTTS
from playsound import playsound
tts=gTTS("my text",lang='ar')
tts.save("testt.mp3")
'''
from gtts import gTTS
from docx import Document
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
ui,_ = loadUiType('main.ui')
class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_button()
    def handle_button(self):
        self.txt_btn.clicked.connect(self.get_file_text)
        self.docs_btn.clicked.connect(self.get_word_text)
        self.process_btn.clicked.connect(self.start)
    def get_file_text(self):
        url_dir = QFileDialog.getOpenFileName(self, 'Select file text', '', 'Txt Files (*.txt)')
        Directory = url_dir[0]
        with open(Directory) as f:
            content = f.read().splitlines()
        r= ' '.join(content)
        self.lineEdit.setText(r)
    def get_word_text(self):
        url_dir = QFileDialog.getOpenFileName(self, 'Select word file', '', 'word Files (*.docx)')
        Directory = url_dir[0]
        doc = Document(Directory)
        c = []
        for i in doc.paragraphs:
            c.append(i.text)
        r= '\n'.join(c)
        self.lineEdit.setText(r)
    def start(self):
        try:
          r=self.lineEdit.text()
          url_output = QFileDialog.getSaveFileName(self, 'Save As', '', 'sounds (*.mp3)')
          saved_location=url_output[0]
          QMessageBox.about(self, ' wait', 'waiting it can take view minutes ...!')
          tts = gTTS(str(r), lang='ar')
          tts.save(saved_location)
          QMessageBox.about(self, ' complete', 'your mp3 is saved sucessly')
        except :
            QMessageBox.about(self, ' error', 'you faced an error ...!')

app = QApplication(sys.argv)
window = MainApp()
window.show()
app.exec_()

