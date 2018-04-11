from tools.webdriver_commands import WebdriverCommands
from tools.webdriver_commands import ElementNotFound

# START_TRAINING_BUTTON = {'css_selector': "#btn-join", 'description': 'start training button'}
TRAINING_1 = {'css_selector': "div.post-456 > a", 'description': 'Meine Basics'}
TRAINING_2 = {'css_selector': "div.post-464 > a", 'description': 'Style Party Training'}
TRAINING_3 = {'css_selector': "div.post-471 > a", 'description': 'IT-Management'}
TRAINING_4 = {'css_selector': "div.post-530 > a", 'description': 'Teamaufbau Training'}
THEMEN_1 = {'css_selector': "ul > li:nth-child(1) > span > a", 'description': 'themen 1'}
BREADCRUMBS_1 = {'css_selector': "a[class='trail-begin']", 'description': 'breadcrumbs home'}

LESSON4 = {'css_selector': "div.post-71.is_not_sample > a", 'description': 'lesson4'}
LESSON5 = {'css_selector': "div.post-14.is_not_sample > a", 'description': 'lesson5'}
LESSON6 = {'css_selector': "div.post-84.is_not_sample > a", 'description': 'lesson6'}
LESSON7 = {'css_selector': "div.post-91.is_not_sample > a", 'description': 'lesson7'}
MARK_COMPLETE_BUTTON = {'css_selector': "#learndash_mark_complete_button", 'description': 'mark as complete button'}
NEXT_LESSON = {'css_selector': "a[class='next-link']", 'description': 'next link'}
PREVIOUS_LESSON = {'css_selector': "a[class='prev-link']", 'description': 'previous link'}
LESSON3_QUIZ = {'css_selector': "#post-69", 'description': 'lesson3 quiz'}
START_QUIZ_BUTTON = {'css_selector': "input[name='startQuiz']", 'description': 'start quiz button'}
ANSWER_OPTIONS_LIST = {'css_selector': "ul[data-question_id='26']", 'description': 'answer options list'}
NEXT_QUESTION_BUTTON_1 = {'css_selector': "li:nth-child(1) > input:nth-child(7)", 'description': 'weiter 1 button'}
ANSWERS = {'css_selector': "li[data-pos]", 'description': 'answer options 1'}
# ANSWER2 = {'css_selector': "li[data-pos='0']", 'description': 'answer options 2'}
# ANSWER3 = {'css_selector': "li[data-pos='0']", 'description': 'answer options 3'}
# ANSWER4 = {'css_selector': "li[data-pos='0']", 'description': 'answer options 4'}


class AcademyMeine30Page:

    def __init__(self, driver):
        self.page = WebdriverCommands(driver)

    def save_screen(self):
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine30.png')

    def click_training_1(self):
        self.page.move_to_element('lessons_list')
        self.page.click_element(TRAINING_1['css_selector'], TRAINING_1['description'])

    def click_training_2(self):
        self.page.move_to_element('lessons_list')
        self.page.click_element(TRAINING_2['css_selector'], TRAINING_2['description'])

    def click_training_3(self):
        self.page.move_to_element('lessons_list')
        self.page.click_element(TRAINING_3['css_selector'], TRAINING_3['description'])

    def click_training_4(self):
        self.page.move_to_element('lessons_list')
        self.page.click_element(TRAINING_4['css_selector'], TRAINING_4['description'])

    def click_lesson1(self):
        self.page.move_to_element('learndash_lesson_topics_list')
        self.page.click_element(THEMEN_1['css_selector'], THEMEN_1['description'])

    def click_next_link(self):
        try:
            self.page.move_to_element('learndash_next_prev_link')
            self.page.click_element(NEXT_LESSON['css_selector'], NEXT_LESSON['description'],1)
        except ElementNotFound:
            print('{} is not present on this page'.format(NEXT_LESSON['description']))
            pass

    def click_previous_link(self):
        try:
            self.page.move_to_element('learndash_next_prev_link')
            self.page.click_element(PREVIOUS_LESSON['css_selector'], PREVIOUS_LESSON['description'], 1)
        except ElementNotFound:
            print('{} is not present on this page'.format(PREVIOUS_LESSON['description']))
            pass

    def click_mark_complete_button(self):
        try:
            self.page.move_to_element('learndash_next_prev_link')
            self.page.click_element(MARK_COMPLETE_BUTTON['css_selector'], MARK_COMPLETE_BUTTON['description'],1)
        except ElementNotFound:
            self.click_next_link()
            pass

    def click_breadcrumbs_first(self):
        self.page.click_element(BREADCRUMBS_1['css_selector'], BREADCRUMBS_1['description'],1)

    def complete_first_training(self):
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine30_before_training1.png')
        self.click_training_1()
        lessons = []
        themes = self.page.get_web_elements('#learndash_topic_dots-456 > ul li', 'a')
        for theme in themes:
            lessons.append(theme.text)
        print(lessons)
        self.click_lesson1()
        for x in range(len(lessons)):
            self.click_mark_complete_button()
            x += 1
        self.click_breadcrumbs_first()
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine30_after_training1.png')

    def complete_second_training(self):
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine30_before_training2.png')
        self.click_training_2()
        lessons = []
        themes = self.page.get_web_elements('#learndash_topic_dots-464 > ul li', 'a')
        for theme in themes:
            lessons.append(theme.text)
        print(lessons)
        self.click_lesson1()
        for x in range(len(lessons)):
            self.click_mark_complete_button()
            x += 1
        self.click_breadcrumbs_first()
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine30_after_training2.png')

    def complete_third_training(self):
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine30_before_training3.png')
        self.click_training_4()
        lessons = []
        themes = self.page.get_web_elements('#learndash_topic_dots-530 > ul li', 'a')
        for theme in themes:
            lessons.append(theme.text)
        print(lessons)
        self.click_lesson1()
        for x in range(len(lessons)):
            self.click_mark_complete_button()
            x += 1
        self.click_breadcrumbs_first()
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine30_after_training3.png')

    def complete_forth_training(self):
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine30_before_training4.png')
        self.click_training_3()
        lessons = []
        themes = self.page.get_web_elements('#learndash_topic_dots-471 > ul li', 'a')
        for theme in themes:
            lessons.append(theme.text)
        print(lessons)
        self.click_lesson1()
        for x in range(len(lessons)):
            self.click_mark_complete_button()
            x += 1
        self.click_breadcrumbs_first()
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine30_after_training4.png')

    def complete_course(self):
        trainings = []
        lessons = self.page.get_web_elements('#lessons_list > div', '.notcompleted')
        print(lessons)
        for lesson in lessons:
            trainings.append(lesson.text)
            print(lesson.text)
        for x in range(len(trainings)):
            if trainings[x] == 'Meine Basics':
                try:
                    self.complete_first_training()
                except:
                    print('cazut la if 1')
            elif trainings[x] == 'Einführung: Style Party Training':
                try:
                    self.complete_second_training()
                except:
                    print('cazut la if 2')
            elif trainings[x] == 'Einführung: Teamaufbau Training':
                try:
                    self.complete_third_training()
                except:
                    print('cazut la if 3')
            elif trainings[x] == 'Einführung: IT-Management':
                try:
                    self.complete_forth_training()
                except:
                    print('........poate urmatorul curs......')

            x += 1
        # print(trainings[0])
        # print(trainings[1])
        # print(trainings[2])
        # print(trainings[3])



    #
    # def click_lesson2(self):
    #     self.page.click_element(LESSON2['css_selector'], LESSON2['description'])
    #
    # def click_lesson3(self):
    #     self.page.click_element(LESSON3['css_selector'], LESSON3['description'])
    #
    # def click_lesson4(self):
    #     self.page.click_element(LESSON4['css_selector'], LESSON4['description'])
    #
    # def click_lesson5(self):
    #     self.page.click_element(LESSON5['css_selector'], LESSON5['description'])
    #
    # def click_lesson6(self):
    #     self.page.click_element(LESSON6['css_selector'], LESSON6['description'])
    #
    # def click_lesson7(self):
    #     self.page.click_element(LESSON7['css_selector'], LESSON7['description'])
    #
    # def click_next_link(self):
    #     try:
    #         self.page.move_to_element('learndash_next_prev_link')
    #         self.page.click_element(NEXT_LESSON['css_selector'], NEXT_LESSON['description'])
    #     except ElementNotFound:
    #         print('{} is not present on this page'.format(NEXT_LESSON['description']))
    #         pass
    #
    # def click_mark_complete_button(self):
    #     try:
    #         self.page.move_to_element('learndash_next_prev_link')
    #         self.page.click_element(MARK_COMPLETE_BUTTON['css_selector'], MARK_COMPLETE_BUTTON['description'],3)
    #     except ElementNotFound:
    #         self.click_next_link()
    #         pass
    #
    # def click_quiz_on_lesson3(self):
    #     self.page.move_to_element('post-69')
    #     self.page.click_element(LESSON3_QUIZ['css_selector'], LESSON3_QUIZ['description'])
    #
    #
    # def click_start_quiz_button(self):
    #     self.page.click_element(START_QUIZ_BUTTON['css_selector'], START_QUIZ_BUTTON['description'])
    #
    # def complete_lesson_quiz(self, question_nr):
    #     print('ajunge pana la lesson_quiz')
    #     items = self.page.get_web_elements('.wpProQuiz_quiz > ol', 'list')
    #     if question_nr == 1:
    #         print("nic")

    # def complete_first_training(self):
