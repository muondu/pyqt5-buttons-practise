import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGridLayout')
layout = QGridLayout()
layout.addWidget(QPushButton('Cool'), 0, 0)
layout.addWidget(QPushButton('Awsome'), 0, 1)
layout.addWidget(QPushButton('Dub'), 0, 2)
layout.addWidget(QPushButton('Subscribe'), 1, 0)
layout.addWidget(QPushButton('Hit the bell'), 1, 1)
layout.addWidget(QPushButton('Like'), 1, 2)
layout.addWidget(QPushButton('Do all of them'), 2, 0)
layout.addWidget(QPushButton('Yahoo'), 2, 1,1,2)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())