import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import typing_game_core


class Ui_logic():
    def setupUi_logic(self):
        self.start_timer_count = 5
        self.max_question = 5

        self.force_exit_btn.clicked.connect(self.on_force_exit_btn)

        self.p2_start_count_lcd.display(self.start_timer_count)

        self.p1_start_btn.clicked.connect(self.on_start_btn)

        self.p3_input_form.returnPressed.connect(self.p3_return_pressed)

        self.start_timer = QtCore.QTimer()
        self.start_timer.timeout.connect(self.p2_lcd_update)
        self.start_timer.setInterval(1000)

        self.game_step_timer = QtCore.QTimer()
        self.game_step_timer.timeout.connect(self.p3_lcd_update)
        self.game_step_timer.setInterval(1000)

    def on_force_exit_btn(self):
        isOk = input('you want reary to leave the game: (y or n)')
        if isOk == 'y':
            sys.exit()

    def on_start_btn(self):
        self.stackedWidget.setCurrentIndex(1)
        self.start_timer.start()

    def p2_lcd_update(self):
        self.start_timer_count -= 1

        if not self.start_timer_count:
            self.start_timer.stop()
            self.game_start()

        self.p2_start_count_lcd.display(self.start_timer_count)

    def game_start(self):
        self.stackedWidget.setCurrentIndex(2)
        self.game_count = 0
        self.game_step()

    def game_step(self):
        if not self.game_count:
            self.question_words = typing_game_core.get_words()
            self.game_step_timer.start()
            self.game_step_timer_count = 0

        self.game_count += 1

        if self.game_count != 11:  # n-1 questions
            print('{}問目'.format(self.game_count))
            self.question = typing_game_core.create_question(
                self.question_words)
            self.p3_question_word.setText(
                '{}問目: {}'.format(self.game_count, self.question))
        else:
            print(self.game_step_timer_count)
            self.game_step_timer.stop()
            self.stackedWidget.setCurrentIndex(3)
            self.p4_game_score.setText(
                '{}問 : {}秒'.format(self.game_count, self.game_step_timer_count)
            )

    def p3_lcd_update(self):
        self.game_step_timer_count += 1
        self.game_time_lcd.display(self.game_step_timer_count)

    def p3_return_pressed(self):
        inputed_word = self.p3_input_form.text()

        is_correct = typing_game_core.judge_input(inputed_word, self.question)
        if is_correct:
            self.p3_is_right_label.setText('正解!')
            self.game_step()
        else:
            self.p3_is_right_label.setText('不正解！もう一度！')

        self.p3_input_form.setText('')
