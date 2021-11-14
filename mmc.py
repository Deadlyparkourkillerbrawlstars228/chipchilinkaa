from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox,QRadioButton,QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox,QButtonGroup
from random import shuffle,randint

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Российский мультфильм, удостоенный «Оскара», — это…' ,'«Cтарик и море»','«Винни-Пух»','«Простоквашино»','«Ну, погоди!»'))
question_list.append(Question('С помощью картинок-смайликов тут зашифровано название фильма. *🌍🐒*','«Планета обезьян»','«Десять негритят»','«Усатый нянь»','«Миллионер из трущоб»'))
question_list.append(Question('Столица США','Вашингтон','Канада','США','Астана'))
question_list.append(Question('Сколько месяцев в году содержат по 28 дней?','12','1','2','10'))
question_list.append(Question('Кто спит с открытыми глазами?','Рыбы','Птицы','Лошади','Воробьи'))
question_list.append(Question('Уличный термометр показывает 15 градусов. Сколько градусов покажут два таких термометра?','15','30','0','7'))
question_list.append(Question('Какие существа жуют желудком?','Раки','Верблюды','Куры','Шиншилы'))
question_list.append(Question('Какие часы показывают правильное время только два раза в сутки?','Cломанные','Биг бен','Песочные','Cолнечные'))
question_list.append(Question('Что теряют космонавты во время полёта?','Вес','Сознание','Память','Зрение'))
question_list.append(Question('Сколько прапрабабушек может быть у человека?','8','4','6','10'))
app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('С помощью картинок-смайликов тут зашифровано название фильма. *🌍🐒*')

window = QWidget()
window.setWindowTitle('Memory Card')

RadioGroupBox = QGroupBox('Варианты')
btn_answer1 = QRadioButton('«Десять негритят»')
btn_answer2 = QRadioButton('«Планета обезьян»')
btn_answer3 = QRadioButton('«Усатый нянь»')
btn_answer4 = QRadioButton('«Миллионер из трущоб»')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(btn_answer1)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)



layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)



AnsGroupBox = QGroupBox('Резалт')
lb_Result = QLabel('угадал?')
lb_Correct = QLabel('нет.Правильный ответ *Планета обезьян*')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox, alignment=Qt.AlignHCenter,stretch = 2)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('некст квешн')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)       
    


answers = [btn_answer1,btn_answer2,btn_answer3,btn_answer4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)    
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Райт')
        window.score +=1    
        print('Статистика\n-всего вопросов',window.total,'\n-Правильных ответов',window.score)
        print('Рейтинг: ',(window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Нот райт')
            print('Рейтинг: ',(window.score/window.total*100),'%')

def next_question():
    window.total += 1 
    print('Статистика\n-всего вопросов',window.total,'\n-Правильных ответов',window.score)
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question() 

window.score = 0
window.total = 0
btn_OK.clicked.connect(click_OK)

window.setLayout(layout_card)
next_question()
window.resize(400,200)
window.show()
app.exec_()
