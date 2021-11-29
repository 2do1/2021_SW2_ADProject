from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class Soccer_Info(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 500, 300)

        # rank window
        self.rank_display = QTextEdit()
        self.rank_display.setReadOnly(True)
        self.rank_display.setAlignment(Qt.AlignLeft)

        # Layout
        rankLayout = QGridLayout()
        rankLayout.addWidget(self.rank_display)

        selectLayout = QGridLayout()

        # combo box
        self.comboBox = QComboBox()
        self.comboBox.addItem('EPL')
        self.comboBox.addItem('Bundesliga')
        self.comboBox.addItem('Laliga')
        self.comboBox.addItem('Serie A')
        self.comboBox.addItem('Ligue 1')
        self.comboBox.addItem('K League')
        selectLayout.addWidget(self.comboBox, 0, 0)

        # buttons
        score_button = QPushButton('Score Rank')
        selectLayout.addWidget(score_button)
        score_button.clicked.connect(self.scoreClicked)

        assist_button = QPushButton('Assist Rank')
        selectLayout.addWidget(assist_button)
        assist_button.clicked.connect(self.assistClicked)

        point_button = QPushButton('Attack Point Rank')
        selectLayout.addWidget(point_button)
        point_button.clicked.connect(self.pointClicked)

        team_button = QPushButton('Team Rank')
        selectLayout.addWidget(team_button)
        team_button.clicked.connect(self.teamClickced)

        mainLayout = QGridLayout()
        mainLayout.addLayout(rankLayout, 0, 0)
        mainLayout.addLayout(selectLayout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle('축구 리그 정보')

    # connect
    def scoreClicked(self):
        pass

    def assistClicked(self):
        pass

    def pointClicked(self):
        pass

    def teamClickced(self):
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    soccer_info = Soccer_Info()
    soccer_info.show()
    sys.exit(app.exec_())
