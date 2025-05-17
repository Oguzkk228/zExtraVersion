from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle, choice
class Question():
    def __init__(self, q, rightAnswer, wrongAns1, wrongAns2, wrongAns3):
        self.question = q
        self.rightAnswer = rightAnswer
        self.wrongAns1 = wrongAns1
        self.wrongAns2 = wrongAns2
        self.wrongAns3 = wrongAns3
questions = []
questions.append(Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский'))
questions.append(Question('Как называется хлеб имеющий форму косички', 'Хала', 'Пита', 'Сайка', 'Лаваш'))
questions.append(Question('Сколько всего белых клеток на шахматной доске', '32', '38', '24', '18'))
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')
    print('Статистика')
    print('-Всего вопросов:', main_window.total)
    print('-Правильных ответов:', main_window.score)
    print('Рейтинг:', main_window.score / main_window.total * 100 , '%')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()
def ask(q:Question):
    shuffle(buttons)
    buttons[0].setText(q.rightAnswer)
    buttons[1].setText(q.wrongAns1)
    buttons[2].setText(q.wrongAns2)
    buttons[3].setText(q.wrongAns3)
    text.setText(q.question)
    correctanswer.setText(q.rightAnswer)
    show_question()
def check_answer():
    if buttons[0].isChecked():
        answer.setText('урппп правильно')
        main_window.score += 1
        show_result()
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        answer.setText('НЕПРАВИЛЬНООООООООООООООООООООООООООО')
        show_result()

def next_question():
    randQ = choice(questions)
    ask(randQ)
    main_window.total += 1
app = QApplication([])
main_window = QWidget()
main_window.score = 0
main_window.total = 0

main_window.setWindowTitle('Интеллектуальная игра')
main_window.resize(400, 400)
text = QLabel('глагол')
rbtn1 = QRadioButton('й')
rbtn2 = QRadioButton('ъ')
rbtn3 = QRadioButton('х')
rbtn4 = QRadioButton('ы')
buttons = [rbtn1, rbtn2, rbtn3, rbtn4]
btn = QPushButton('Ответить')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
answer = QLabel('Правильно/Неправильно')
correctanswer = QLabel('Правильный ответ')
RadioGroupBox = QGroupBox('Варианты')
AnsGroupBox = QGroupBox('Ответ')
AnsGroupBox.hide()
v_ansline = QVBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line4 = QHBoxLayout()
v_line2.addWidget(rbtn1)
v_line2.addWidget(rbtn2)
v_line3.addWidget(rbtn3)
v_line3.addWidget(rbtn4)
h_line4.addLayout(v_line2)
h_line4.addLayout(v_line3)
h_line1.addWidget(text)
h_line2.addWidget(RadioGroupBox)
h_line2.addWidget(AnsGroupBox)
h_line3.addWidget(btn)
v_ansline.addWidget(answer)
v_ansline.addWidget(correctanswer)
v_line1.addLayout(h_line1)
v_line1.addLayout(h_line2)
v_line1.addLayout(h_line3)
AnsGroupBox.setLayout(v_ansline)
RadioGroupBox.setLayout(h_line4)
main_window.setLayout(v_line1)
next_question()
btn.clicked.connect(start_test)
main_window.show()
app.exec()  