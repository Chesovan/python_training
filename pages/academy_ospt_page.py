from tools.webdriver_commands import WebdriverCommands
from tools.webdriver_commands import ElementNotFound

START_TRAINING_BUTTON = {'css_selector': "#btn-join", 'description': 'start training button'}
LESSON1 = {'css_selector': "div.post-9.is_not_sample > a", 'description': 'lesson1'}
LESSON2 = {'css_selector': "div.post-64.is_not_sample > a", 'description': 'lesson2'}
LESSON3 = {'css_selector': "div.post-67.is_not_sample > a", 'description': 'lesson3'}
LESSON4 = {'css_selector': "div.post-71.is_not_sample > a", 'description': 'lesson4'}
LESSON5 = {'css_selector': "div.post-14.is_not_sample > a", 'description': 'lesson5'}
LESSON6 = {'css_selector': "div.post-84.is_not_sample > a", 'description': 'lesson6'}
LESSON7 = {'css_selector': "div.post-91.is_not_sample > a", 'description': 'lesson7'}
MARK_COMPLETE_BUTTON = {'css_selector': "#learndash_mark_complete_button", 'description': 'mark as complete button'}
NEXT_LESSON = {'css_selector': "a[class='next-link']", 'description': 'next lesson'}
LESSON3_QUIZ = {'css_selector': "#post-69", 'description': 'lesson3 quiz'}
START_QUIZ_BUTTON = {'css_selector': "input[name='startQuiz']", 'description': 'start quiz button'}
ANSWER_OPTIONS_LIST = {'css_selector': "ul[data-question_id='26']", 'description': 'answer options list'}
NEXT_QUESTION_BUTTON_1 = {'css_selector': "li:nth-child(1) > input:nth-child(7)", 'description': 'weiter 1 button'}
ANSWERS = {'css_selector': "li[data-pos]", 'description': 'answer options 1'}
# ANSWER2 = {'css_selector': "li[data-pos='0']", 'description': 'answer options 2'}
# ANSWER3 = {'css_selector': "li[data-pos='0']", 'description': 'answer options 3'}
# ANSWER4 = {'css_selector': "li[data-pos='0']", 'description': 'answer options 4'}


class AcademyOsptPage:

    def __init__(self, driver):
        self.page = WebdriverCommands(driver)

    def click_mache_dieses_training_button(self):
        try:
            self.page.click_element(START_TRAINING_BUTTON['css_selector'], START_TRAINING_BUTTON['description'], 2)
        except ElementNotFound:
            pass

    def click_lesson1(self):
        self.page.move_to_element('lessons_list')
        self.page.click_element(LESSON1['css_selector'], LESSON1['description'])

    def click_lesson2(self):
        self.page.click_element(LESSON2['css_selector'], LESSON2['description'])

    def click_lesson3(self):
        self.page.click_element(LESSON3['css_selector'], LESSON3['description'])

    def click_lesson4(self):
        self.page.click_element(LESSON4['css_selector'], LESSON4['description'])

    def click_lesson5(self):
        self.page.click_element(LESSON5['css_selector'], LESSON5['description'])

    def click_lesson6(self):
        self.page.click_element(LESSON6['css_selector'], LESSON6['description'])

    def click_lesson7(self):
        self.page.click_element(LESSON7['css_selector'], LESSON7['description'])

    def click_next_lesson_button(self):
        try:
            self.page.move_to_element('learndash_next_prev_link')
            self.page.click_element(NEXT_LESSON['css_selector'], NEXT_LESSON['description'])
        except ElementNotFound:
            print('{} is not present on this page'.format(NEXT_LESSON['description']))
            pass

    def click_mark_complete_button(self):
        try:
            self.page.move_to_element('learndash_next_prev_link')
            self.page.click_element(MARK_COMPLETE_BUTTON['css_selector'], MARK_COMPLETE_BUTTON['description'],3)
        except ElementNotFound:
            self.click_next_lesson_button()
            pass

    def click_quiz_on_lesson3(self):
        self.page.move_to_element('post-69')
        self.page.click_element(LESSON3_QUIZ['css_selector'], LESSON3_QUIZ['description'])


    def click_start_quiz_button(self):
        self.page.click_element(START_QUIZ_BUTTON['css_selector'], START_QUIZ_BUTTON['description'])

    def complete_lesson_quiz(self, question_nr):
        print('ajunge pana la lesson_quiz')
        items = self.page.get_web_elements('.wpProQuiz_quiz > ol', 'list')
        if question_nr == 1:
            print("nic")

    answers_list = []
    def lesson_quiz(self, lesson):
        # questions_list = []
        answer_option_list = []

        questions = self.page.get_web_elements('.wpProQuiz_quiz > ol', 'list')
        for question in questions:
            question_nr = int(question.find_element_by_css_selector('.wpProQuiz_question_page > span:nth-child(1)').text)
            # quizzes = self.page.get_web_elements('.wpProQuiz_question > ul > li', 'li')

            contain = driver.find_element_by_css_selector('.wpProQuiz_question > ul')
            quizzes = contain.find_elements_by_tag_name('li > label > input')
            # self.answers_list.extend(quizzes)
            for quiz in quizzes:
                answer_option_list.append(quiz)

            print(answer_option_list)
            if lesson == 3:
                self.page.wait_a_second(9)
                if question_nr == 1:
                    print('pana aici a mers ... oare da click ?')
                    answer_option_list[0].click()
                    print('pana aici a mers ... oare da click ? 2')
                    answer_option_list[1].click()
                    self.page.click_element(NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])

        # for question in questions:
        #     question_nr = int(question.find_element_by_css_selector('.wpProQuiz_question_page > span:nth-child(1)').text)
        # print(self.answers_list)
        # self.page.wait_a_second(10)
        # # self.answers_list[0].click()
        # self.page.wait_a_second(10)
        # if lesson == 3:
        #     self.page.wait_a_second(2)
        #     if question_nr == 1:
        #         questions_list[0].answer_option_list[0].click()
        #         questions_list[0].answer_option_list[1].click()
        #         self.page.click_element(NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
        #
        #     elif question_nr == 2:
        #         questions_list[0].answer_option_list[1].click()
        #         self.page.click_element(NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
        #
        #     elif question_nr == 3:
        #         questions_list[0].answer_option_list[0].click()
        #         questions_list[0].answer_option_list[1].click()
        #         self.page.click_element(NEXT_QUESTION_BUTTON_1['css_selector'], NEXT_QUESTION_BUTTON_1['description'])
        #     elif question_nr == 4:
        #         answer_option_list[2].click()
        #         self.page.click_element(NEXT_QUESTION_BUTTON_1['css_selector'],
        #                                 NEXT_QUESTION_BUTTON_1['description'])
        #     elif question_nr == 5:
        #         answer_option_list[0].click()
        #         answer_option_list[1].click()
        #         answer_option_list[2].click()
        #         self.page.click_element(NEXT_QUESTION_BUTTON_1['css_selector'],
        #                                 NEXT_QUESTION_BUTTON_1['description'])
        #     elif question_nr == 6:
        #         answer_option_list[3].click()
        #         self.page.click_element(NEXT_QUESTION_BUTTON_1['css_selector'],
        #                                 NEXT_QUESTION_BUTTON_1['description'])

        #     questions_list.append(answer_option_list)
        # print('---------------------------')
        # print(answer_option_list)
        # print(questions_list)
        # print('---------------------------')





            #
            #
            #
            # if lesson == 3 and question_nr==1:
            #     answer_option_list[0].click()
            #     answer_option_list[1].click()
            #     self.page.click_element(NEXT_QUESTION_BUTTON_1['css_selector'],NEXT_QUESTION_BUTTON_1['description'])
            #
            #
            # if lesson == 3:
            #     for
            #     self.lesson_quiz(question_nr)
            # elif lesson == 4:
            #     print('tre facuta functie, cred')


        #     text = item.text
        #     if x in text:
        #         self.results_list_product_price = item.find_element_by_css_selector('span.price').text
        #         item.click()
        #         break
        # print(self.results_list_product_price)


    # results_list_product_price = 0
    # def get_search_result(self, x):
    #     items = self.page.get_web_elements('.container-fluid > div > ul','list')
    #     for item in items:
    #         text = item.text
    #         if x in text:
    #             self.results_list_product_price = item.find_element_by_css_selector('span.price').text
    #             item.click()
    #             break
    #     print(self.results_list_product_price)
