from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Team import TeamRank
from Assist import AssistRank
from Goal import GoalRank
from AttackPoint import AttackPointRank

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
        selectLayout.addWidget(self.comboBox, 0, 0)

        # buttons
        goal_button = QPushButton('Score Rank')
        selectLayout.addWidget(goal_button)
        goal_button.clicked.connect(self.goalClicked)

        assist_button = QPushButton('Assist Rank')
        selectLayout.addWidget(assist_button)
        assist_button.clicked.connect(self.assistClicked)

        attack_point_button = QPushButton('Attack Point Rank')
        selectLayout.addWidget(attack_point_button)
        attack_point_button.clicked.connect(self.attackPointClicked)

        team_button = QPushButton('Team Rank')
        selectLayout.addWidget(team_button)
        team_button.clicked.connect(self.teamClickced)

        mainLayout = QGridLayout()
        mainLayout.addLayout(rankLayout, 0, 0)
        mainLayout.addLayout(selectLayout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle('축구 리그 정보')

    # connect
    def goalClicked(self):
        league = self.comboBox.currentText()  # 콤보박스에서 선택된 리그 가져오기
        goal_rank = GoalRank(league)
        self.rank_display.setText(goal_rank)

    def assistClicked(self):
        league = self.comboBox.currentText()  # 콤보박스에서 선택된 리그 가져오기
        assist_rank = AssistRank(league)
        self.rank_display.setText(assist_rank)

    def attackPointClicked(self):
        league = self.comboBox.currentText()  # 콤보박스에서 선택된 리그 가져오기
        attack_point_rank = AttackPointRank(league)
        self.rank_display.setText(attack_point_rank)

    def teamClickced(self):
        league = self.comboBox.currentText()  # 콤보박스에서 선택된 리그 가져오기
        team_rank = TeamRank(league)
        self.rank_display.setText(team_rank)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    soccer_info = Soccer_Info()
    soccer_info.show()
    sys.exit(app.exec_())
