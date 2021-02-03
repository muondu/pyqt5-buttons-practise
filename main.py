
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Random buttons')
layout = QHBoxLayout()
layout.addWidget(QPushButton('Like'))
layout.addWidget(QPushButton('Dislike'))
layout.addWidget(QPushButton('Subscribe'))
layout.addWidget(QPushButton('Cool Nesh'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())