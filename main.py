from kivy.core.window import Window
import os

from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
import json
from last import LastScreen


#CONTENTS
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty
from phase1 import IntroToAlphabets, PhaseOneTest
from phase2 import  PhaseTwoTest, PhonogramAlpha
from phase3 import TwoLetterWords,TwoLetterWordsLevel3
from phase4 import Cvc, VowelA,VowelE,VowelI,VowelO,VowelU, VowelALong,VowelELong,VowelILong,VowelOLong,VowelULong,CvcQuiz
from phase5 import CVCandE, CvcQuiz2, CVCStory
from phase6 import Dipthongs, Digraphs, ConsBlends, Phase6Main, P6Quiz
from sight_words import SightWordsPage
from alphabet_game import AlphabetGame
from phase7 import Comprehension, Exercise1, Exercise2, Exercise3, Exercise4, Exercise5, Exercise6, Exercise7, Exercise8, Exercise9
from last import LastScreen
from answers import AnswerP1, AnswerP2, AnswerP3, AnswerP4, AnswerP5, AnswerP6, AnswerP7
from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import TwoLineAvatarListItem
from kivy.base import EventLoop
from kivy.lang import Builder
Builder.load_file('kv.kv')

from kivy.utils import platform
from materials import ANSWERS, PUBLIC, RESTRICTED, FINAL_EXERCISE


class MainMenu(MDScreen, MDWidget):
    main_read = ObjectProperty(None)
    main_away = ObjectProperty(None)

    options_bug = ObjectProperty(None)
    options_hopper = ObjectProperty(None)

    pages_menu = ObjectProperty(None)
    answers_menu = ObjectProperty(None)

    deped_als_valencia = ObjectProperty(None)

    pages = ListProperty([
        {'title':'Filipino Alphabet',
        'page':'IntroToAlphabets'},
        {'title':'ABC Connecting Game',
        'page':'AlphabetGame'},
        {'title':'Phonetics',
        'page':'PhonogramAlpha'},
        {'title':'Two Letter-Words',
        'page':'TwoLetterWords'},
        {'title':'CVC',
        'page':'Cvc'},
        {'title':'Practice Reading',
        'page':'CVCStory'},
        {'title':'CVC + e',
        'page':'CVCandE'},
        {'title':'DDC',
        'page':'Phase6Main'},
        {'title':'Sight Words',
        'page':'SightWordsPage'},
        {'title':'Reading Comprehension',
        'page':'Comprehension'},
    ])
    answers = ListProperty([
        {'title':'P1 Answers',
        'page':'AnswerP1'},
        {'title':'P2 Answers',
        'page':'AnswerP2'},
        {'title':'P3 Answers',
        'page':'AnswerP3'},
        {'title':'P4 Answers',
        'page':'AnswerP4'},
        {'title':'P5 Answers',
        'page':'AnswerP5'},
        {'title':'P6 Answers',
        'page':'AnswerP6'},
        {'title':'P7 Answers',
        'page':'AnswerP7'},
    ])

    def __init__(self, **kw):
        super(MainMenu, self).__init__(**kw)
        self.name = 'MainMenu'
        

    def on_enter(self):
        self.add_main_btn()
        self.add_pages_option()
        self.add_answers_option()
        self.add_deped_als_valencia()
        self.main_away.animate_away()
        self.options_bug.animate()
        self.options_hopper.animate()
    
    # add title as start button
    def add_main_btn(self):
        # !READ
        if not self.main_read:
            self.main_read = Image(
                source = 'imgs/readaway/read.png',
                allow_stretch = False,
                keep_ratio = True,
                size_hint = (None, None)
            )
            
            self.main_read.size = (self.main_read.texture.width/5,self.main_read.texture.height/5)
            self.main_read.x = (Window.width/2)-(self.main_read.width/2)
            self.main_read.y = Window.height/2

            self.add_widget(self.main_read)

        # !AWAY
        if not self.main_away:
            self.main_away = Away()
            self.main_away.source = 'imgs/readaway/away.png'
            self.main_away.size = (self.main_away.texture.width/5,self.main_away.texture.height/5)
            self.main_away.pos = self.main_read.pos
            self.main_away.y = self.main_away.y - (self.main_away.width/2.5)
            self.main_away.x = (Window.width/2)-(self.main_away.width/2)

            # save original position and parent width
            self.main_away.original_pos = self.main_away.pos
            self.main_away.parent_width = self.main_read.width/2
            self.main_away.parent_height = self.main_read.height/2


            self.add_widget(self.main_away)

    # Add menu button and menu for pages
    def add_pages_option(self):
        if not self.options_bug:
            self.options_bug = OptionsBug()
            self.options_bug.y = Window.height/6
            self.options_bug.x = Window.width - (Window.width/10)
            self.options_bug.bind(on_release=self.open_menu_pages)
            self.add_widget(self.options_bug)

            menu_items = [
                {
                'text': i['title'],
                'viewclass': 'OneLineListItem',
                'on_release': lambda page=i['page']: self.goto(page),
                } for i in self.pages
            ]
            self.pages_menu = MDDropdownMenu(
            items = menu_items,
            caller=self.options_bug,
            width_mult=4)
            
    def add_answers_option(self):
        if not self.options_hopper:
            self.options_hopper = OptionsHopper()
            self.options_hopper.y = Window.height/6
            self.options_hopper.x = Window.width/10
            self.options_hopper.bind(on_release=self.open_menu_answers)
            self.add_widget(self.options_hopper)

            menu_items = [
                {
                'text': i['title'],
                'viewclass': 'OneLineListItem',
                'on_release': lambda page=i['page']: self.goto(page),
                } for i in self.answers
            ]
            self.answers_menu = MDDropdownMenu(
            items = menu_items,
            caller=self.options_hopper,
            width_mult=4)


    # open menu(pages)
    def open_menu_pages(self, instance):
        self.pages_menu.open()

    # open menu(answers)
    def open_menu_answers(self, instance):
        self.answers_menu.open()

    def goto(self,page):
        if self.pages_menu:
            self.pages_menu.dismiss()

        if self.answers_menu:
            self.answers_menu.dismiss()
        self.manager.transition.direction = 'left'
        self.manager.current = page
    
    def add_deped_als_valencia(self):
        self.deped_als_valencia = CutomImgs(source='deped_als_valencia_off.png')
        self.deped_als_valencia.size_hint=(None,None)
        self.deped_als_valencia.size = (Window.width/3,Window.height/3)
        self.deped_als_valencia.x = (Window.width) - (self.deped_als_valencia.width/1.3)
        self.deped_als_valencia.y = self.main_away.y
        self.deped_als_valencia.bind(on_touch_down=lambda x,y: self.deped_als_valencia.make_flipper(y,'deped_als_valencia.png', 'deped_als_valencia_off.png'))
        self.add_widget(self.deped_als_valencia)



    


        
class Away(Image,MagicBehavior):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    original_pos = ReferenceListProperty(xxx,yyy)
    parent_width = NumericProperty(0)
    parent_height = NumericProperty

    def __init__(self, **kwargs):
        super(Away,self).__init__(**kwargs)
        self.size_hint = (None, None)

    
    def on_touch_down(self, touch, *args):
        if self.collide_point(*touch.pos):
            self.animate_away()
            return super().on_touch_down(touch, *args)

    def on_release(self):
        return super().on_release()
    
    def animate_away(self) -> None:
        animation = (
            (
                Animation(scale_y=0.1, d=0.5)
                & Animation(scale_x=1.4, d=0.5)
            )
            + (
    
                Animation(scale_x=0.1, d=0.3)
            )
            + (
                Animation(scale_y=1.4, d=0.5)
                & Animation(scale_x=0.1, d=0.5)
                & Animation(y=self.y + (self.parent_height*5), d=0.3)
            )
            + (
                Animation(scale_y=1.4, t='out_quad', d=0.3)
                & Animation(scale_x=0.1, t='out_quad', d=0.3)
                & Animation(pos=self.original_pos, t='out_quad', d=0.3)
            )
            + (
                Animation(scale_y=0.4, t='out_bounce', d=0.3)
                & Animation(scale_x=1.5, t='out_bounce', d=0.3)
            )
            + (
                Animation(scale_y=1, t='out_bounce', d=0.5)
                & Animation(scale_x=1, t='out_bounce', d=0.5)
                & Animation(x=self.x, t='out_bounce', d=0.5)
                & Animation(pos=self.original_pos, t='out_bounce', d=0.5)
            )
     
        )
        animation.start(self)
    
class CutomImgs(Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            return super().on_touch_down(touch)

    def change_source(self,new):
        self.source = new
    
    def make_flipper(self,touch,first,second):
        if self.collide_point(*touch.pos):
            if self.source == first:
                self.source = second
            elif self.source == second:
                self.source = first


class OptionsBug(Image,MDRaisedButton):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    original_pos = ReferenceListProperty(xxx,yyy)
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = 'imgs/readaway/bug.png'
        self.md_bg_color = (1,1,1,1)
        self.ripple_scale = 0.01
        
    
    def on_press(self):
        self.source = 'imgs/readaway/bug_open.png'
        squeak = SoundLoader.load('bug.wav')
        squeak.play()
        return super().on_press()
    
    def on_release(self):
        self.source = 'imgs/readaway/bug.png'
        return super().on_release()
    
    def animate(self) -> None:
        self.original_pos = (self.x,self.y)
        animation = (
  
            (
                Animation(x=self.x + (self.width*10), t='out_quad', d=0.1)
            )
            + (
                Animation(x=self.x - (self.width*20), t='out_circ', d=1)
                & Animation(y=self.y + (self.height*6), t='out_circ', d=1)
            )
            + (
                Animation(pos=self.original_pos, t='out_quad', d=3)
            )
     
        )
        animation.bind(on_start=lambda x,y:self.motion_mode())
        animation.bind(on_progress=lambda x,y,z:self.motion_mode())
        animation.bind(on_complete=lambda x,y:self.steady_mode())

        animation.start(self)
    
    def motion_mode(self):
        if self.source == 'imgs/readaway/bug_open.png':
            self.source = 'imgs/readaway/bug.png'
        else:
            self.source = 'imgs/readaway/bug_open.png'
        
    def steady_mode(self):
        self.source = 'imgs/readaway/bug.png'

class OptionsHopper(Image,MDRaisedButton):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    original_pos = ReferenceListProperty(xxx,yyy)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = 'imgs/readaway/hopper.png'
        self.md_bg_color = (1,1,1,1)
        self.ripple_scale = 0.01
    
    def on_press(self):
        self.source = 'imgs/readaway/hopper_open.png'
        self.squeaks()
        return super().on_press()

    def squeaks(self):
        squeak = SoundLoader.load('bug.wav')
        squeak.play()
    
    def bug_flying(self):
        squeak = SoundLoader.load('bugmotion.wav')
        squeak.play()

    def on_release(self):
        self.source = 'imgs/readaway/hopper.png'
        return super().on_release()

    def animate(self) -> None:
        self.original_pos = (self.x,self.y)
        animation = (
  
            (
                Animation(x=self.x - (self.width*10), t='out_quad', d=0.1)
            )
            + (
                Animation(pos=self.original_pos, t='out_quad', d=4)
            )
     
        )

        animation.bind(on_start=lambda x,y:self.motion_mode())
        animation.bind(on_progress=lambda x,y,z:self.motion_mode())
        animation.bind(on_complete=lambda x,y:self.steady_mode())

        animation.start(self)
    
    def motion_mode(self):
        if self.source == 'imgs/readaway/hopper_open.png':
            self.source = 'imgs/readaway/hopper.png'
        else:
            self.source = 'imgs/readaway/hopper_open.png'

        
    def steady_mode(self):
        self.source = 'imgs/readaway/hopper.png'
        self.squeaks()

class Item(TwoLineAvatarListItem):
    divider = None
    source = StringProperty('')


class MainMain(ScreenManager):
    opt_menu = ObjectProperty(None)
    answers = ListProperty([
        {'title':'P1 Answers',
        'page':'AnswerP1'},
        {'title':'P2 Answers',
        'page':'AnswerP2'},
        {'title':'P3 Answers',
        'page':'AnswerP3'},
        {'title':'P4 Answers',
        'page':'AnswerP4'},
        {'title':'P5 Answers',
        'page':'AnswerP5'},
        {'title':'P6 Answers',
        'page':'AnswerP6'},
        {'title':'P7 Answers',
        'page':'AnswerP7'},
    ])
    pages = ListProperty([
        {'title':'Filipino Alphabet',
        'page':'IntroToAlphabets'},
        {'title':'ABC Connecting Game',
        'page':'AlphabetGame'},
        {'title':'Phonetics',
        'page':'PhonogramAlpha'},
        {'title':'Two Letter-Words',
        'page':'TwoLetterWords'},
        {'title':'CVC',
        'page':'Cvc'},
        {'title':'Practice Reading',
        'page':'CVCStory'},
        {'title':'CVC + e',
        'page':'CVCandE'},
        {'title':'DDC',
        'page':'Phase6Main'},
        {'title':'Sight Words',
        'page':'SightWordsPage'},
        {'title':'Reading Comprehension',
        'page':'Comprehension'},
    ])
    restricted = ListProperty([
        {'title':'PhaseOneTest',
        'page':'PhaseOneTest'},
        {'title':'PhaseTwoTest',
        'page':'PhaseTwoTest'},
        {'title':'TwoLetterWordsLevel3',
        'page':'TwoLetterWordsLevel3'},
        {'title':'CvcQuiz',
        'page':'CvcQuiz'},
        {'title':'CvcQuiz2',
        'page':'CvcQuiz2'},
        {'title':'P6Quiz',
        'page':'P6Quiz'},
    ])
    final_exercise = ListProperty([
        {'title':'Exercise1',
        'page':'Exercise1'},
        {'title':'Exercise2',
        'page':'Exercise2'},
        {'title':'Exercise3',
        'page':'Exercise3'},
        {'title':'Exercise4',
        'page':'Exercise4'},
        {'title':'Exercise5',
        'page':'Exercise5'},
        {'title':'Exercise6',
        'page':'Exercise6'},
        {'title':'Exercise7',
        'page':'Exercise7'},
        {'title':'Exercise8',
        'page':'Exercise8'},
        {'title':'Exercise9',
        'page':'Exercise9'},
    ])
    def __init__(self, **kwargs):
        super(MainMain, self).__init__(**kwargs)
        # bind native key
        EventLoop.window.bind(on_keyboard=self.esc)

    def switch(self,screen, direction):
        if self.current == 'Cvc':
            self.current = 'CvcQuiz'
            self.transition.direction = 'left'
        else:
            self.current = screen
            self.transition.direction = direction
        
        if self.opt_menu:
            self.opt_menu.dismiss()
    

    def esc(self, window, key, *largs):
        if key == 27:
            if self.current == 'MainMenu':
                self.opt_menu = MDDialog(
                        title= 'Read Away',
                        type='simple',
                        items=[
                            Item(text='Jeneath Verallo', secondary_text='Mobile Teacher', source='imgs/people/maam_aneth.png'),
                            Item(text='Armelyn Nahini', secondary_text='Contributor', source='imgs/people/bug.png'),
                            Item(text='Alyssa Primacio-Salido', secondary_text='Voice Talent', source='imgs/people/bug.png'),
                            Item(text='Jimmy Verallo Jr.', secondary_text='Voice Talent', source='imgs/people/bug.png'),
                            Item(text='Van Salido', secondary_text='Developer', source='imgs/people/bug.png'),
                        ],
                        buttons=[
                            MDRaisedButton(
                                text = 'Exit',
                                on_release = lambda x: ReadAway().stop()
                            )
                        ]
                    )
                self.opt_menu.open()
            elif self.current in ANSWERS:
                for i in self.answers:
                    if i['page'] == self.current:
                        self.create_dialog_answers(i['title'])
                        self.opt_menu.open()
            elif self.current in PUBLIC:
                next = self.next()
                prev = self.previous()
                for i in self.pages:
                    if i['page'] == self.current:
                        self.create_dialog(prev,next,i['title'])
                        self.opt_menu.open()
            # elif self.current in RESTRICTED:
                
            #     if self.opt_menu.page == self.current:
            #         self.opt_menu.open()
            #     else:
            #         self.opt_menu = CustomDialog(
            #             text= 'Quiz in progress, finish first before you can proceed!'
            #         )
            #         self.opt_menu.open()
         
            elif self.current in FINAL_EXERCISE:
                if self.opt_menu:
                    if self.opt_menu.page == self.current:
                        self.opt_menu.open()
                    else:
                        self.opt_menu = CustomDialog(
                            text= 'Finish the test before going back'
                        )
                        self.opt_menu.open()
                else:
                    self.opt_menu = CustomDialog(
                        text= 'Quiz in progress, finish first before you can proceed!'
                        )
                    self.opt_menu.open()

            else:
                next = self.next()
                prev = self.previous()
                self.create_dialog(prev,next,'Menu')
                self.opt_menu.open()
            return True 
        else:
            return True 
    
    def create_dialog(self,prev,next, title):
        self.opt_menu = CustomDialog(
            text = title,
            buttons = [
                MDRaisedButton(text='Home', on_press=lambda x: self.switch('MainMenu','right')),
                MDRaisedButton(text='Previous', on_press=lambda x: self.switch(prev,'right')),
                MDRaisedButton(text='Continue', on_press=lambda x: self.switch(next,'left'))
            ]
        )
    
    def create_dialog_answers(self,title):
        self.opt_menu = CustomDialog(
            text = title,
            buttons = [
                MDRaisedButton(text='Home', on_press=lambda x: self.switch('MainMenu','right'))
            ]
        )

    def created_dialog_quiz(self, prev, next, title, page, score, disabled):
        back = MDRaisedButton(text='Back', disabled=disabled, on_press=lambda x: self.switch(prev,'right'))
        continue_ = MDRaisedButton(text='Continue', disabled=disabled, on_press=lambda x: self.switch(next,'left'))
        self.opt_menu = CustomDialog(
            title = title,
            text = score,
            page = page,
            buttons = [back,continue_]
        )
    
    def create_dialog_exercise(self, title, text):
        next = self.next()
        self.opt_menu = CustomDialog(
                title = title,
                text=text,
                page=self.current,
                buttons=[
                    MDFlatButton(
                        text='ALL STORIES',
                        theme_text_color='Custom',
                        text_color=(0,1,0,1),
                        on_release=lambda x: self.switch('Comprehension','right')
                    ),
                    MDFlatButton(
                        text='NEXT',
                        theme_text_color='Custom',
                        text_color=(0,0,1,1),
                        on_release=lambda x: self.switch(next,'left')
                    ),
                ],
            )

class CustomDialog(MDDialog):
    page = StringProperty('')


class ReadAway(MDApp):
    def build(self):
        self.icon = 'bulb.png'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'DeepOrange'

        sm = MainMain()
        sm.add_widget(MainMenu(name='MainMenu'))
        sm.add_widget(IntroToAlphabets(name='IntroToAlphabets'))
        sm.add_widget(AlphabetGame(name='AlphabetGame'))
        sm.add_widget(PhaseOneTest(name='PhaseOneTest'))
 
        sm.add_widget(PhonogramAlpha(name='PhonogramAlpha'))

        sm.add_widget(PhaseTwoTest(name='PhaseTwoTest'))
        sm.add_widget(TwoLetterWords(name='TwoLetterWords'))
        sm.add_widget(TwoLetterWordsLevel3(name='TwoLetterWordsLevel3'))
        sm.add_widget(Cvc(name='Cvc'))
        sm.add_widget(VowelA(name='VowelA'))
        sm.add_widget(VowelE(name='VowelE'))
        sm.add_widget(VowelI(name='VowelI'))
        sm.add_widget(VowelO(name='VowelO'))
        sm.add_widget(VowelU(name='VowelU'))
        sm.add_widget(VowelALong(name='VowelALong'))
        sm.add_widget(VowelELong(name='VowelELong'))
        sm.add_widget(VowelILong(name='VowelILong'))
        sm.add_widget(VowelOLong(name='VowelOLong'))
        sm.add_widget(VowelULong(name='VowelULong'))
        sm.add_widget(CvcQuiz(name='CvcQuiz'))
        sm.add_widget(CVCandE(name='CVCandE'))
        sm.add_widget(CvcQuiz2(name='CvcQuiz2'))
        sm.add_widget(CVCStory(name='CVCStory'))
        sm.add_widget(Phase6Main(name='Phase6Main'))
        sm.add_widget(Dipthongs(name='Dipthongs'))
        sm.add_widget(Digraphs(name='Digraphs'))
        sm.add_widget(ConsBlends(name='ConsBlends'))
        sm.add_widget(P6Quiz(name='P6Quiz'))
        sm.add_widget(SightWordsPage(name='SightWordsPage'))
        sm.add_widget(Comprehension(name='Comprehension'))
        sm.add_widget(Exercise1(name='Exercise1'))
        sm.add_widget(Exercise2(name='Exercise2'))
        sm.add_widget(Exercise3(name='Exercise3'))
        sm.add_widget(Exercise4(name='Exercise4'))
        sm.add_widget(Exercise5(name='Exercise5'))
        sm.add_widget(Exercise6(name='Exercise6'))
        sm.add_widget(Exercise7(name='Exercise7'))
        sm.add_widget(Exercise8(name='Exercise8'))
        sm.add_widget(Exercise9(name='Exercise9'))
        sm.add_widget(LastScreen(name='LastScreen'))
        sm.add_widget(AnswerP1(name='AnswerP1'))
        sm.add_widget(AnswerP2(name='AnswerP2'))
        sm.add_widget(AnswerP3(name='AnswerP3'))
        sm.add_widget(AnswerP4(name='AnswerP4'))
        sm.add_widget(AnswerP5(name='AnswerP5'))
        sm.add_widget(AnswerP6(name='AnswerP6'))
        sm.add_widget(AnswerP7(name='AnswerP7'))

        return sm

    def on_start(self):
        

        # ASK PERMNISSION IN ANDROID
        if platform == 'android':
            from android.permissions import request_permissions, Permission, check_permission
            perms = [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,Permission.INTERNET, Permission.RECORD_AUDIO, Permission.CAPTURE_AUDIO_OUTPUT]
            request_permissions(perms)
            # ADD DIRECTORIES
            answers_paths = [
            '/storage/emulated/0/pb/answers/phase1',
            '/storage/emulated/0/pb/answers/phase2',
            '/storage/emulated/0/pb/answers/phase3',
            '/storage/emulated/0/pb/answers/phase4',
            '/storage/emulated/0/pb/answers/phase5',
            '/storage/emulated/0/pb/answers/phase6',
            '/storage/emulated/0/pb/answers/sight_words',
            ]
            for _path in answers_paths:
                if os.path.exists(_path):
                    print(f'path: {_path} already exist')
                else:
                    print(f'creating directory... :>> {_path}')
                    os.makedirs(_path)
                    print(_path + ' Created!')

        else:
            # ADD DIRECTORIES
            answers_paths = [
                'answers/phase1',
                'answers/phase2',
                'answers/phase3',
                'answers/phase4',
                'answers/phase5',
                'answers/phase6',
                'answers/sight_words',
            ]
            for _path in answers_paths:
                if os.path.exists(_path):
                    print(f'path: {_path} already exist')
                else:
                    print(f'creating directory... :>> {_path}')
                    os.makedirs(_path)
                    print(_path + ' Created!')
        
        #CREATE JSONFILE FOR P7
        p7file = 'p7scorecard.json'
        if os.path.exists(p7file):
            print('P7 SCORECARD ALREADY EXIST')
        else:
            print('#CREATE JSONFILE FOR P7')
            #open('p7scorecard.json','w').close()
            with open('p7scorecard.json', 'w') as _scorecard:
                json.dump({'scores_by_screen': []}, _scorecard)
            _scorecard.close()

        return super().on_start()



    
    
    

if __name__ == '__main__':
    ReadAway().run()