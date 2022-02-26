import sys
from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)                      # neue App wird gestartet und Parameter (sys.argv) wird


#def test():
#    print("hey Arnold")
                                                            # übergeben = Anwendung ist erstellt
class MainWindow(QtWidgets.QMainWindow):                        # MainWindow erbt alle Eigenschaften von ()
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Time-Control")                     # Titel wird in der oberen Leiste benannt
        self.ui = Ui_MainWindow()                               # Erstelle neues Ui-Mainwindow()
        self.ui.setupUi(self)                                   # Erstellte Inhalt soll im Fenster gezeigt werden

# Kommen
        self.ui.input1.setText("Einen schönen Arbeitstag!")         # Bei input1 wird Text ausgegeben
        self.ui.bu_kommen.clicked.connect(self.on_bu_kommen_click)  # Beim Klicken des Buttons Kommen
        # self.ui.bu_kommen.clicked.connect(test)  # Beim Klicken des Buttons Kommen

        #self.ui.input1.hide()
        #self.ui.input1.show()

    def on_bu_kommen_click(self):
        text = self.ui.input1.text()
        print("on_button_click(): " + text)




window = MainWindow()                                           # Fenster wird erstellt

window.show()                                                   # Fenster wird angezeigt

sys.exit(app.exec_())

