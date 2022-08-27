import json
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import  MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivy.core.window import Window


from kivy.properties import ObjectProperty, NumericProperty,ListProperty, BooleanProperty, StringProperty

class StoryGrid(MDGridLayout):
    height_x2 = Window.height*2
    height_x2_5 = Window.height*2.5
    height_x3 = Window.height*3
    height_x4 = Window.height*4

    def __init__(self, *args, **kwargs):
        super(StoryGrid, self).__init__(*args, **kwargs)
        self.rows=2
        self.size_hint_y=None
        self.height=Window.height*1.5

class Choice(MDFillRoundFlatIconButton):
    correct = BooleanProperty(False)
    exercise = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Choice, self).__init__(**kwargs)
        self.icon = 'dots-circle'
    
    def on_release(self):
        self.exercise = self.parent.parent.parent.parent.parent.parent.parent.parent

        with open('p7scorecard.json', 'r') as read:
            dictionary = json.load(read)

        if self.correct:
            print('correct')
            self.md_bg_color_disabled = (0,1,0,1)
            self.icon = 'check'
            self.exercise.correct_answers.append(self.text)
        else:
            print('wrong')
            self.md_bg_color_disabled = (1,0,0,1)
            self.icon = 'close'

        self.exercise.total_answers.append(self.text)
        
        self.exercise.progress_bar.color = (1,1,0,1)
        zzz = len(self.exercise.total_answers)/self.exercise.num_items
        self.exercise.progress_bar.value = zzz * 100


        if len(self.exercise.total_answers) == self.exercise.num_items:
            self.exercise.show_alert_dialog()
            with open('p7scorecard.json', 'w') as scorecard:
                data = {
                    'name': self.exercise.manager.current,
                    'answered': self.exercise.total_answers,
                    'correct': self.exercise.correct_answers,
                    'answered_num': len(self.exercise.total_answers),
                    'correct_num': len(self.exercise.correct_answers),
                    'total_items': self.exercise.num_items
                }
                dictionary['scores_by_screen'].append(data)
                json.dump(dictionary, scorecard)
            
        return super().on_release()

class CustomDialog(MDDialog):
    page = StringProperty('')

class Exercise(MDScreen):
    exercise_num = NumericProperty(0)
    progress_bar = ObjectProperty(None)
    total_answers = ListProperty([])
    correct_answers = ListProperty([])
    num_items = NumericProperty(0)
    num_score = NumericProperty(0)
    dialog = ObjectProperty(None)
    toolbar7 = ObjectProperty(None)

    choice_1a: ObjectProperty(None)
    choice_1b: ObjectProperty(None)
    choice_1c: ObjectProperty(None)

    choice_2a: ObjectProperty(None)
    choice_2b: ObjectProperty(None)
    choice_2c: ObjectProperty(None)

    choice_3a: ObjectProperty(None)
    choice_3b: ObjectProperty(None)
    choice_3c: ObjectProperty(None)

    choice_4a: ObjectProperty(None)
    choice_4b: ObjectProperty(None)
    choice_4c: ObjectProperty(None)
    
    choice_5a: ObjectProperty(None)
    choice_5b: ObjectProperty(None)
    choice_5c: ObjectProperty(None)

    choice_6a: ObjectProperty(None)
    choice_6b: ObjectProperty(None)
    choice_6c: ObjectProperty(None)


    def show_alert_dialog(self):
        if not self.dialog:
            dialog_text = f'Exercise {self.exercise_num} Complete! \nScore: {len(self.correct_answers)}/{self.num_items}'
            dialog_title = 'Title'

            if len(self.correct_answers) <= self.num_items - 4:
                dialog_title = 'OK!'
            elif len(self.correct_answers) == self.num_items - 3:
                dialog_title = 'NOT BAD!'
            elif len(self.correct_answers) == self.num_items - 2:
                dialog_title = 'NICE!'
            elif len(self.correct_answers) == self.num_items - 1:
                dialog_title = 'CONGRATULATIONS!'
            elif len(self.correct_answers) == self.num_items:
                dialog_title = 'PERFECT!'

            self.manager.create_dialog_exercise(dialog_title,dialog_text)
            self.manager.opt_menu.open()

    def on_enter(self, *args):
        if len(self.total_answers) == self.num_items:
            self.show_alert_dialog()
        return super().on_enter(*args)

    def on_pre_leave(self, *args):
        self.update_state()
        if self.dialog:
            self.dialog.dismiss()
        return super().on_pre_leave(*args)

    def update_state(self):
        with open('state.json') as read:
            info = json.load(read)
        info['levels'].append({
            'level': self.exercise_num,
            'completed': True
        })

        with open('state.json', 'w') as write:
            json.dump(info, write)
        


    def select_1(self):
        # IF CORRECT
        if self.choice_1a.correct:
            self.choice_1a.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_1a.disabled = True
            self.choice_1b.disabled = True
            self.choice_1c.disabled = True

        elif self.choice_1b.correct:
            self.choice_1b.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_1a.disabled = True
            self.choice_1b.disabled = True
            self.choice_1c.disabled = True
            
        
        elif self.choice_1c.correct:
            self.choice_1c.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_1a.disabled = True
            self.choice_1b.disabled = True
            self.choice_1c.disabled = True


        # IF WRONG
        elif not self.choice_1a.correct:
            self.choice_1a.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_1a.disabled = True
            self.choice_1b.disabled = True
            self.choice_1c.disabled = True

        elif not self.choice_1b.correct:
            self.choice_1b.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_1a.disabled = True
            self.choice_1b.disabled = True
            self.choice_1c.disabled = True
        
        elif not self.choice_1c.correct:
            self.choice_1c.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_1a.disabled = True
            self.choice_1b.disabled = True
            self.choice_1c.disabled = True


    def select_2(self):
        # IF CORRECT
        if self.choice_2a.correct:
            self.choice_2a.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_2a.disabled = True
            self.choice_2b.disabled = True
            self.choice_2c.disabled = True

        elif self.choice_2b.correct:
            self.choice_2b.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_2a.disabled = True
            self.choice_2b.disabled = True
            self.choice_2c.disabled = True
        
        elif self.choice_2c.correct:
            self.choice_2c.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_2a.disabled = True
            self.choice_2b.disabled = True
            self.choice_2c.disabled = True

        # IF WRONG
        elif not self.choice_2a.correct:
            self.choice_2a.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_2a.disabled = True
            self.choice_2b.disabled = True
            self.choice_2c.disabled = True

        elif not self.choice_2b.correct:
            self.choice_2b.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_2a.disabled = True
            self.choice_2b.disabled = True
            self.choice_2c.disabled = True
        
        elif not self.choice_2c.correct:
            self.choice_2c.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_2a.disabled = True
            self.choice_2b.disabled = True
            self.choice_2c.disabled = True


    def select_3(self):
        # IF CORRECT
        if self.choice_3a.correct:
            self.choice_3a.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_3a.disabled = True
            self.choice_3b.disabled = True
            self.choice_3c.disabled = True

        elif self.choice_3b.correct:
            self.choice_3b.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_3a.disabled = True
            self.choice_3b.disabled = True
            self.choice_3c.disabled = True
        
        elif self.choice_3c.correct:
            self.choice_3c.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_3a.disabled = True
            self.choice_3b.disabled = True
            self.choice_3c.disabled = True

        # IF WRONG
        elif not self.choice_3a.correct:
            self.choice_3a.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_3a.disabled = True
            self.choice_3b.disabled = True
            self.choice_3c.disabled = True

        elif not self.choice_3b.correct:
            self.choice_3b.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_3a.disabled = True
            self.choice_3b.disabled = True
            self.choice_3c.disabled = True
        
        elif not self.choice_3c.correct:
            self.choice_3c.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_3a.disabled = True
            self.choice_3b.disabled = True
            self.choice_3c.disabled = True


    def select_4(self):
        # IF CORRECT
        if self.choice_4a.correct:
            self.choice_4a.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_4a.disabled = True
            self.choice_4b.disabled = True
            self.choice_4c.disabled = True

        elif self.choice_4b.correct:
            self.choice_4b.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_4a.disabled = True
            self.choice_4b.disabled = True
            self.choice_4c.disabled = True
        
        elif self.choice_4c.correct:
            self.choice_4c.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_4a.disabled = True
            self.choice_4b.disabled = True
            self.choice_4c.disabled = True

        # IF WRONG
        elif not self.choice_4a.correct:
            self.choice_4a.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_4a.disabled = True
            self.choice_4b.disabled = True
            self.choice_4c.disabled = True

        elif not self.choice_4b.correct:
            self.choice_4b.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_4a.disabled = True
            self.choice_4b.disabled = True
            self.choice_4c.disabled = True
        
        elif not self.choice_4c.correct:
            self.choice_4c.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_4a.disabled = True
            self.choice_4b.disabled = True
            self.choice_4c.disabled = True

    def select_5(self):
        # IF CORRECT
        if self.choice_5a.correct:
            self.choice_5a.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_5a.disabled = True
            self.choice_5b.disabled = True
            self.choice_5c.disabled = True

        elif self.choice_5b.correct:
            self.choice_5b.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_5a.disabled = True
            self.choice_5b.disabled = True
            self.choice_5c.disabled = True
        
        elif self.choice_5c.correct:
            self.choice_5c.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_5a.disabled = True
            self.choice_5b.disabled = True
            self.choice_5c.disabled = True

        # IF WRONG
        elif not self.choice_5a.correct:
            self.choice_5a.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_5a.disabled = True
            self.choice_5b.disabled = True
            self.choice_5c.disabled = True

        elif not self.choice_5b.correct:
            self.choice_5b.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_5a.disabled = True
            self.choice_5b.disabled = True
            self.choice_5c.disabled = True
        
        elif not self.choice_5c.correct:
            self.choice_5c.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_5a.disabled = True
            self.choice_5b.disabled = True
            self.choice_5c.disabled = True

    def select_6(self):
        # IF CORRECT
        if self.choice_6a.correct:
            self.choice_6a.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_6a.disabled = True
            self.choice_6b.disabled = True
            self.choice_6c.disabled = True

        elif self.choice_6b.correct:
            self.choice_6b.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_6a.disabled = True
            self.choice_6b.disabled = True
            self.choice_6c.disabled = True
        
        elif self.choice_6c.correct:
            self.choice_6c.icon_color = (0,1,0,1)

            #disable choices after answer
            self.choice_6a.disabled = True
            self.choice_6b.disabled = True
            self.choice_6c.disabled = True

        # IF WRONG
        elif not self.choice_6a.correct:
            self.choice_6a.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_6a.disabled = True
            self.choice_6b.disabled = True
            self.choice_6c.disabled = True

        elif not self.choice_6b.correct:
            self.choice_6b.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_6a.disabled = True
            self.choice_6b.disabled = True
            self.choice_6c.disabled = True
        
        elif not self.choice_6c.correct:
            self.choice_6c.md_bg_color_disabled = (1,0,0,1)

            #disable choices after answer
            self.choice_6a.disabled = True
            self.choice_6b.disabled = True
            self.choice_6c.disabled = True
            




class Comprehension(MDScreen):
    ex_1 = ObjectProperty(None)
    ex_2 = ObjectProperty(None)
    ex_3 = ObjectProperty(None)
    ex_4 = ObjectProperty(None)
    ex_5 = ObjectProperty(None)
    ex_6 = ObjectProperty(None)
    ex_7 = ObjectProperty(None)
    ex_8 = ObjectProperty(None)
    ex_9 = ObjectProperty(None)


class Exercise1(Exercise):
    # C
    # A
    # B
    # B
    # A
    def __init__(self, **kw):
        super(Exercise1, self).__init__(**kw)
        self.choice_1c.correct = True
        self.choice_2a.correct = True
        self.choice_3b.correct = True
        self.choice_4b.correct = True
        self.choice_5a.correct = True

        self.num_items = 5

    


class Exercise2(Exercise):
    pass

    # A
    # C
    # C
    # A
    # B
    def __init__(self, **kw):
        super(Exercise2, self).__init__(**kw)
        self.choice_1a.correct = True
        self.choice_2c.correct = True
        self.choice_3c.correct = True
        self.choice_4a.correct = True
        self.choice_5b.correct = True

        self.num_items = 5



class Exercise3(Exercise):
    

    # C
    # C
    # C
    # C
    # A
    def __init__(self, **kw):
        super(Exercise3, self).__init__(**kw)
        self.choice_1c.correct = True
        self.choice_2c.correct = True
        self.choice_3c.correct = True
        self.choice_4c.correct = True
        self.choice_5a.correct = True

        self.num_items = 5



class Exercise4(Exercise):
    

    # B
    # A
    # B
    # B
    # B
    # B
    def __init__(self, **kw):
        super(Exercise4, self).__init__(**kw)
        self.choice_1b.correct = True
        self.choice_2a.correct = True
        self.choice_3b.correct = True
        self.choice_4b.correct = True
        self.choice_5b.correct = True

        self.num_items = 5


class Exercise5(Exercise):
    

    # B
    # A
    # A
    # A
    # C
    def __init__(self, **kw):
        super(Exercise5, self).__init__(**kw)
        self.choice_1b.correct = True
        self.choice_2a.correct = True
        self.choice_3a.correct = True
        self.choice_4a.correct = True
        self.choice_5c.correct = True

        self.num_items = 5


class Exercise6(Exercise):
    

    # A
    # B
    # A
    # B
    # C
    def __init__(self, **kw):
        super(Exercise6, self).__init__(**kw)
        self.choice_1a.correct = True
        self.choice_2b.correct = True
        self.choice_3a.correct = True
        self.choice_4b.correct = True
        self.choice_5c.correct = True

        self.num_items = 5


class Exercise7(Exercise):
    

    # A
    # B
    # C
    # A
    # A
    def __init__(self, **kw):
        super(Exercise7, self).__init__(**kw)
        self.choice_1a.correct = True
        self.choice_2b.correct = True
        self.choice_3c.correct = True
        self.choice_4a.correct = True
        self.choice_5a.correct = True

        self.num_items = 5


class Exercise8(Exercise):
    

    # B
    # B
    # B
    # A
    # A
    def __init__(self, **kw):
        super(Exercise8, self).__init__(**kw)
        self.choice_1b.correct = True
        self.choice_2b.correct = True
        self.choice_3b.correct = True
        self.choice_4a.correct = True
        self.choice_5a.correct = True

        self.num_items = 5


class Exercise9(Exercise):
    

    # B
    # C
    # B
    # C
    # C
    # C
    def __init__(self, **kw):
        super(Exercise9, self).__init__(**kw)
        self.choice_1b.correct = True
        self.choice_2c.correct = True
        self.choice_3b.correct = True
        self.choice_4c.correct = True
        self.choice_5c.correct = True
        self.choice_6c.correct = True

        self.num_items = 6

