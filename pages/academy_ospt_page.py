from tools.webdriver_commands import WebdriverCommands
from tools.webdriver_commands import ElementNotFound

START_TRAINING_BUTTON = {'css_selector': "#btn-join", 'description': 'start training button'}
LESSON1 = {'css_selector': "div.post-9.is_not_sample > a", 'description': 'lesson1'}
LESSON2 = {'css_selector': "div.post-64.is_not_sample > a", 'description': 'lesson2'}
LESSON3 = {'css_selector': "div.post-67.is_not_sample > a", 'description': 'lesson3'}
LESSON5 = {'css_selector': "div.post-71.is_not_sample > a", 'description': 'lesson4'}
LESSON4 = {'css_selector': "div.post-14.is_not_sample > a", 'description': 'lesson5'}
LESSON6 = {'css_selector': "div.post-84.is_not_sample > a", 'description': 'lesson6'}
LESSON7 = {'css_selector': "div.post-91.is_not_sample > a", 'description': 'lesson7'}
BREADCRUMBS_1 = {'css_selector': "a[class='trail-begin'] span", 'description': 'breadcrumbs home'}
MARK_COMPLETE_BUTTON = {'css_selector': "#learndash_mark_complete_button", 'description': 'mark as complete button'}
NEXT_LESSON = {'css_selector': "a[class='next-link']", 'description': 'next lesson'}
LESSON3_QUIZ = {'css_selector': "#post-69", 'description': 'lesson3 quiz'}
LESSON4_QUIZ = {'css_selector': "#post-11", 'description': 'lesson4 quiz'}
LESSON5_QUIZ = {'css_selector': "#post-77", 'description': 'lesson5 quiz'}
LESSON6_QUIZ = {'css_selector': "#post-89", 'description': 'lesson6 quiz'}
START_QUIZ_BUTTON = {'css_selector': "input[name='startQuiz']", 'description': 'start quiz button'}
ANSWER_OPTIONS_LIST = {'css_selector': "ul[data-question_id='26']", 'description': 'answer options list'}
TEST_FINISHED_BUTTON = {'css_selector': "ol > li:last-of-type input[name='next']", 'description': 'weiter 1 button'}
TEST_FINISHED_BUTTON_NEXT = {'css_selector': "#quiz_continue_link", 'description': 'next test button'}
PARENT_CSS = ''
ANSWER1 = {'css_selector': "{} li[data-pos='0'] label".format(PARENT_CSS), 'description': 'answer options 1'}
ANSWER2 = {'css_selector': "{} li[data-pos='1'] label".format(PARENT_CSS), 'description': 'answer options 2'}
ANSWER3 = {'css_selector': "{} li[data-pos='2'] label".format(PARENT_CSS), 'description': 'answer options 3'}
ANSWER4 = {'css_selector': "{} li[data-pos='3'] label".format(PARENT_CSS), 'description': 'answer options 4'}
NEXT_QUESTION_BUTTON_1 = {'css_selector': "{} input[value='Weiter']".format(PARENT_CSS), 'description': 'weiter button'}


class AcademyOsptPage:

    def __init__(self, driver):
        self.page = WebdriverCommands(driver)

    def click_mache_dieses_training_button(self):
        try:
            self.page.click_element(START_TRAINING_BUTTON['css_selector'], START_TRAINING_BUTTON['description'], 2)
        except ElementNotFound:
            pass

    def click_lesson(self, lesson):
        if lesson == 1:
            self.page.move_to_element('lessons_list')
            self.page.click_element(LESSON1['css_selector'], LESSON1['description'])
        elif lesson == 2:
            self.page.move_to_element('lessons_list')
            self.page.click_element(LESSON2['css_selector'], LESSON2['description'])
        elif lesson == 3:
            self.page.move_to_element('lessons_list')
            self.page.click_element(LESSON3['css_selector'], LESSON3['description'])
        elif lesson == 4:
            self.page.move_to_element('lessons_list')
            self.page.click_element(LESSON4['css_selector'], LESSON4['description'])
        elif lesson == 5:
            self.page.move_to_element('lessons_list')
            self.page.click_element(LESSON5['css_selector'], LESSON5['description'])
        elif lesson == 6:
            self.page.move_to_element('lessons_list')
            self.page.click_element(LESSON6['css_selector'], LESSON6['description'])
        elif lesson == 7:
            self.page.move_to_element('lessons_list')
            self.page.click_element(LESSON7['css_selector'], LESSON7['description'])
        else:
            print('Lesson {} is not available !!!'.format(lesson))

    def set_parent_css(self, css):
        PARENT_CSS = css
        return PARENT_CSS

    def choose_answer(self, answer_combination, question):
        if answer_combination == 1:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER1['css_selector']), ANSWER1['description'])
        elif answer_combination == 2:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER2['css_selector']), ANSWER2['description'])
        elif answer_combination == 3:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER3['css_selector']), ANSWER3['description'])
        elif answer_combination == 4:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER4['css_selector']), ANSWER4['description'])
        elif answer_combination == 12:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER2['css_selector']), ANSWER2['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER1['css_selector']), ANSWER1['description'])

        elif answer_combination == 123:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER1['css_selector']), ANSWER1['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER2['css_selector']), ANSWER2['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER3['css_selector']), ANSWER3['description'])
        elif answer_combination == 124:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER1['css_selector']), ANSWER1['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER2['css_selector']), ANSWER2['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER4['css_selector']), ANSWER4['description'])
        elif answer_combination == 1234:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER1['css_selector']), ANSWER1['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER2['css_selector']), ANSWER2['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER3['css_selector']), ANSWER3['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER4['css_selector']), ANSWER4['description'])
        elif answer_combination == 13:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER1['css_selector']), ANSWER1['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER3['css_selector']), ANSWER3['description'])
        elif answer_combination == 134:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER1['css_selector']), ANSWER1['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER3['css_selector']), ANSWER3['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER4['css_selector']), ANSWER4['description'])
        elif answer_combination == 14:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER1['css_selector']), ANSWER1['description'])
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER4['css_selector']), ANSWER4['description'])
        elif answer_combination == 23:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER2['css_selector'], ANSWER2['description']))
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER3['css_selector'], ANSWER3['description']))
        elif answer_combination == 24:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER2['css_selector'], ANSWER2['description']))
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER4['css_selector'], ANSWER4['description']))
        elif answer_combination == 234:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER2['css_selector'], ANSWER2['description']))
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER3['css_selector'], ANSWER3['description']))
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER4['css_selector'], ANSWER4['description']))
        elif answer_combination == 34:
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER3['css_selector'], ANSWER3['description']))
            self.page.click_element((self.set_parent_css('ol.wpProQuiz_list li:nth-of-type({})'.format(question)) + ANSWER4['css_selector'], ANSWER4['description']))
        else:
            print('Answer for {} is not available !!!'.format(answer_combination))

    def click_next_lesson_button(self):
        try:
            self.page.move_to_element('learndash_next_prev_link')
            self.page.click_element(NEXT_LESSON['css_selector'], NEXT_LESSON['description'])
        except ElementNotFound:
            print('{} is not present on this page'.format(NEXT_LESSON['description']))
            pass

    def click_next_training_button(self):
        try:
            self.page.move_to_element('quiz_continue_link')
            self.page.click_element(TEST_FINISHED_BUTTON_NEXT['css_selector'], TEST_FINISHED_BUTTON_NEXT['description'])
        except ElementNotFound:
            print('Needs more wait time before clicking on \'complete test button\'')

    def click_mark_complete_button(self):
        try:
            self.page.move_to_element('learndash_next_prev_link')
            self.page.click_element(MARK_COMPLETE_BUTTON['css_selector'], MARK_COMPLETE_BUTTON['description'],3)
        except ElementNotFound:
            self.click_next_lesson_button()
            pass

    def click_breadcrumbs_first(self):
        self.page.click_element(BREADCRUMBS_1['css_selector'], BREADCRUMBS_1['description'],1)

    def click_quiz_on_lesson3(self):
        self.page.move_to_element('post-69')
        self.page.click_element(LESSON3_QUIZ['css_selector'], LESSON3_QUIZ['description'])

    def click_quiz_on_lesson4(self):
        self.page.move_to_element('post-11')
        self.page.click_element(LESSON4_QUIZ['css_selector'], LESSON4_QUIZ['description'])

    def click_quiz_on_lesson5(self):
        self.page.move_to_element('post-77')
        self.page.click_element(LESSON5_QUIZ['css_selector'], LESSON5_QUIZ['description'])

    def click_quiz_on_lesson6(self):
        self.page.move_to_element('post-89')
        self.page.click_element(LESSON6_QUIZ['css_selector'], LESSON6_QUIZ['description'])

    def click_start_quiz_button(self):
        self.page.click_element(START_QUIZ_BUTTON['css_selector'], START_QUIZ_BUTTON['description'])

    def simple_training_completion(self):
        try:
            self.click_mark_complete_button()
            self.click_breadcrumbs_first()
        except:
            self.click_breadcrumbs_first()
            pass

    def complex_training_completion(self, lesson):
        if lesson == 3:
            self.click_quiz_on_lesson3()
            self.click_start_quiz_button()
            x = 1
            self.choose_answer(12, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x += 1
            self.choose_answer(2, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x += 1
            self.choose_answer(12, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x += 1
            self.choose_answer(3, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x += 1
            self.choose_answer(123, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x += 1
            self.choose_answer(3, x)
            self.page.click_element(TEST_FINISHED_BUTTON['css_selector'], TEST_FINISHED_BUTTON['description'])
            try:
                self.page.wait_for_element_to_disappear('.course_progress', 'progress bar')
            except:
                pass
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training3_after_quiz.png')
            self.click_next_training_button()
        elif lesson == 4:
            self.click_quiz_on_lesson4()
            self.click_start_quiz_button()
            x = 1
            self.choose_answer(1, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x+= 1
            self.choose_answer(1, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x+= 1
            self.choose_answer(3, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x+= 1
            self.choose_answer(1, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x+= 1
            self.choose_answer(1, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x+= 1
            self.choose_answer(1234, x)
            self.page.click_element(TEST_FINISHED_BUTTON['css_selector'], TEST_FINISHED_BUTTON['description'])
            try:
                self.page.wait_for_element_to_disappear('.course_progress', 'progress bar')
            except:
                pass
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training4_after_quiz.png')
            self.click_next_training_button()
        elif lesson == 5:
            self.click_quiz_on_lesson5()
            self.click_start_quiz_button()
            x = 1
            self.choose_answer(12, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x += 1
            self.choose_answer(1, x)
            self.page.click_element(TEST_FINISHED_BUTTON['css_selector'], TEST_FINISHED_BUTTON['description'])
            try:
                self.page.wait_for_element_to_disappear('.course_progress', 'progress bar')
            except:
                pass
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training5_after_quiz.png')
            self.click_next_training_button()
        elif lesson == 6:
            self.click_quiz_on_lesson6()
            self.click_start_quiz_button()
            x=1
            self.choose_answer(1, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x +=1
            self.choose_answer(2, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x +=1
            self.choose_answer(12, x)
            self.page.click_element(self.set_parent_css('.wpProQuiz_quiz > ol > li:nth-child({})'.format(x)) + NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
            x +=1
            self.choose_answer(12, x)
            self.page.click_element(TEST_FINISHED_BUTTON['css_selector'], TEST_FINISHED_BUTTON['description'])
            try:
                self.page.wait_for_element_to_disappear('.course_progress', 'progress bar')
            except:
                pass
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training6_after_quiz.png')
            self.click_next_training_button()
        else:
            print('The training completion for lesson {} is not complex !!!'.format(lesson))
        self.click_breadcrumbs_first()

    def complete_training(self, training):
        self.click_lesson(training)
        if training == 1:
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training1_before.png')
            self.simple_training_completion()
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training1_after.png')
        elif training == 2:
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training2_before.png')
            self.simple_training_completion()
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training2_after.png')
        elif training == 3:
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training3_before.png')
            self.complex_training_completion(training)
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training3_after.png')
        elif training == 4:
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training4_before.png')
            self.complex_training_completion(training)
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training4_after.png')
        elif training == 5:
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training5_before.png')
            self.complex_training_completion(training)
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training5_after.png')
        elif training == 6:
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training6_before.png')
            self.complex_training_completion(training)
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training6_after.png')
        elif training == 7:
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training7_before.png')
            self.simple_training_completion()
            self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_training7_after.png')
        else:
            print('There is no training with this nr. {} !!!'.format(training))

    def complete_course(self):
        self.click_mache_dieses_training_button()
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_trainings_before.png')
        trainings = []
        lessons = self.page.get_web_elements('#lessons_list > div', '.notcompleted')
        for lesson in lessons:
            trainings.append(lesson.text)
            print(lesson.text)
        for x in range(len(trainings)):
            # try:
            self.complete_training(x+1)
            # except:
                # print('cazut la if {}'.format(x))
            x += 1
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/ospm_trainings_after.png')
        print("OSPM training finished")