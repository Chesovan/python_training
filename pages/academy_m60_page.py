from tools.webdriver_commands import WebdriverCommands
from tools.webdriver_commands import ElementNotFound

TRAINING_1 = {'css_selector': "div.post-532 > a", 'description': 'Fortgeschritten: Style Party Training'}
TRAINING_2 = {'css_selector': "div.post-639 > a", 'description': 'Fortgeschritten: Teamaufbau Training'}
TRAINING_3 = {'css_selector': "div.post-530 > a", 'description': 'Einführung: Teamaufbau Training'}
BREADCRUMBS_1 = {'css_selector': "a[class='trail-begin']", 'description': 'breadcrumbs home'}
MARK_COMPLETE_BUTTON = {'css_selector': "#learndash_mark_complete_button", 'description': 'mark as complete button'}
NEXT_LESSON = {'css_selector': "a[class='next-link']", 'description': 'next link'}
PREVIOUS_LESSON = {'css_selector': "a[class='prev-link']", 'description': 'previous link'}



class AcademyMeine60Page:

    def __init__(self, driver):
        self.page = WebdriverCommands(driver)

    def save_screen(self):
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine60.png')

    def click_training_1(self):
        self.page.move_to_element('lessons_list')
        self.page.click_element(TRAINING_1['css_selector'], TRAINING_1['description'])

    def click_training_2(self):
        self.page.move_to_element('lessons_list')
        self.page.click_element(TRAINING_2['css_selector'], TRAINING_2['description'])

    def click_training_3(self):
        self.page.move_to_element('lessons_list')
        self.page.click_element(TRAINING_3['css_selector'], TRAINING_3['description'])

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
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine60_before_training1.png')
        self.click_training_1()
        try:
            self.click_mark_complete_button()
            self.click_breadcrumbs_first()
        except:
            self.click_breadcrumbs_first()
            pass
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine60_after_training1.png')

    def complete_second_training(self):
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine60_before_training2.png')
        self.click_training_2()
        try:
            self.click_mark_complete_button()
            self.click_breadcrumbs_first()
        except:
            self.click_breadcrumbs_first()
            pass
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine60_after_training2.png')

    def complete_third_training(self):
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine60_before_training3.png')
        self.click_training_3()
        try:
            self.click_mark_complete_button()
            # self.click_breadcrumbs_first()
        except:
            # self.click_breadcrumbs_first()
            pass
        self.page.save_screenshot('C:/Users/mariuschesovan/Desktop/pat_screenshots/meine60_after_training3.png')

    def complete_course(self):
        trainings = []
        lessons = self.page.get_web_elements('#lessons_list > div', '.notcompleted')
        for lesson in lessons:
            trainings.append(lesson.text)
            # print(lesson.text)
        for x in range(len(trainings)):
            if trainings[x] == 'Fortgeschritten: Style Party Training':
                try:
                    self.complete_first_training()
                except:
                    print('cazut la if 1')
            elif trainings[x] == 'Fortgeschritten: Teamaufbau Training':
                try:
                    self.complete_second_training()
                except:
                    print('cazut la if 2')
            elif trainings[x] == 'Einführung: Teamaufbau Training':
                try:
                    self.complete_third_training()
                except:
                    print('cazut la if 3')
            x += 1
        print("Meine 60 training finished")