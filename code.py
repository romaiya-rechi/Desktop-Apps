import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TemplateEdge App")
        self.setGeometry(100, 100, 1280, 800)

        browser = QWebEngineView()
        browser.load(QUrl("https://templateedge.com/"))
        self.setCentralWidget(browser)

app = QApplication(sys.argv)
window = WebApp()
window.show()
sys.exit(app.exec_())
