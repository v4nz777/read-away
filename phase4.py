from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty
from materials import CVCE,CVCA, CVCE, CVCI, CVCO, CVCU, CVC_QUIZ, CVCLONGA, CVCLONGE, CVCLONGI, CVCLONGO, CVCLONGU
import random
from kivy.clock import Clock

#from sound_recorder import rec
from jniusrecord import android_record, play_audio
from kivy.utils import platform


class Cvc(MDScreen):
    pass

class VowelA(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):
        self._list = self.ids.cvc_a
        if len(self._list.children) == 0:
            for i in CVCA:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                    )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/short/a/{instance.text}.ogg')
            self.say_word.play()
    
class VowelE(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):
        self._list = self.ids.cvc_e
        if len(self._list.children) == 0:
            for i in CVCE:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                    )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/short/e/{instance.text}.ogg')
            self.say_word.play()

class VowelI(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):
        self._list = self.ids.cvc_i
        if len(self._list.children) == 0:
            for i in CVCI:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                     )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/short/i/{instance.text}.ogg')
            self.say_word.play()

class VowelO(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):
        self._list = self.ids.cvc_o
        if len(self._list.children) == 0:
            for i in CVCO:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                     )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/short/o/{instance.text}.ogg')
            self.say_word.play()

class VowelU(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):
        self._list = self.ids.cvc_u
        if len(self._list.children) == 0:
            for i in CVCU:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                    )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/short/u/{instance.text}.ogg')
            self.say_word.play()

class VowelALong(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):
        self._list = self.ids.cvc_a
        if len(self._list.children) == 0:
            for i in CVCLONGA:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                    )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/long/a/{instance.text}.ogg')
            self.say_word.play()
    
class VowelELong(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):
        self._list = self.ids.cvc_e
        if len(self._list.children) == 0:
            for i in CVCLONGE:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                    )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/long/e/{instance.text}.ogg')
            self.say_word.play()

class VowelILong(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):
        self._list = self.ids.cvc_i
        if len(self._list.children) == 0:
            for i in CVCLONGI:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                    )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/long/i/{instance.text}.ogg')
            self.say_word.play()

class VowelOLong(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):

        self._list = self.ids.cvc_o
        if len(self._list.children) == 0:
            for i in CVCLONGO:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                    )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/long/o/{instance.text}.ogg')
            self.say_word.play()

class VowelULong(MDScreen):
    say_word = ObjectProperty(None)
    _list = ObjectProperty(None)

    def on_enter(self, *args):
        self._list = self.ids.cvc_u
        if len(self._list.children) == 0:
            for i in CVCLONGU:
                if True: #if len(i) == 3:
                    self.btn = MDFillRoundFlatButton(
                        text=i, 
                        font_size='50sp', 
                        font_name='ShadowsIntoLight-Regular.ttf'
                     )
                    self.btn.bind(on_release=self.callbck)
                    self._list.add_widget(self.btn)
        return super().on_enter(*args)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/long/u/{instance.text}.ogg')
            self.say_word.play()
###################################### CVC GAME ############################################
class CvcQuiz(MDScreen):
    word_box = ObjectProperty(None)
    shown = ListProperty([])
    current_answer = StringProperty('')
    tries = ListProperty([])

    sound = ObjectProperty(None)
    
    progress_bar = ObjectProperty(None)
    microphone = ObjectProperty(None)
    speaker = ObjectProperty(None)
    next_button = ObjectProperty(None)
    toolbar = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(self.start_show_word)
        
    def show_word(self):
        zzz = len(self.shown)/50
        self.progress_bar.value = zzz * 100
        if len(self.shown) != 50:
            self.current_answer = random.choice(CVC_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(CVC_QUIZ)

            self.word_box.final_pos = self.word_box.pos
            x,y = self.word_box.final_pos
            self.word_box.pos = (x, y+self.height)

            self.word_box.children[0].source = f'imgs/word_blocks/{self.current_answer}.png'
            anim1 = Animation(y=y, size=(80, 80), t='out_bounce')
            anim1.start(self.word_box)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            title = 'CVC Quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.shown)}/50'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL 50 ALREADY ANSWERED')

        self.speaker.theme_icon_color = 'Primary'
        self.next_button.disabled = True

    def start_show_word(self, dt):
        if len(self.shown) != 50:
            self.current_answer = random.choice(CVC_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(CVC_QUIZ)
            
            self.word_box.final_pos = self.word_box.pos
            x,y = self.word_box.final_pos
            self.word_box.pos = (x, y+self.height)

            self.word_box.children[0].source = f'imgs/word_blocks/{self.current_answer}.png'
            anim1 = Animation(y=y, size=(80, 80), t='out_bounce')
            anim1.start(self.word_box)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            title = 'CVC Quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.shown)}/50'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL 50 ALREADY ANSWERED')
        self.next_button.disabled = True

    

    def validate(self):
        self.sound = SoundLoader.load('src/pre_record_sound.ogg')
        self.sound.play()
        answer = self.answer()
        while not answer:
            #self.microphone = MDSpinner()
            self.microphone.disabled = True
            self.microphone.theme_icon_color='Custom'
            self.microphone.icon = 'microphone-question'
            self.microphone.icon_color = (0,1,0.3,1)
          
        
        if self.answer_file in self.tries:
            self.speaker.theme_icon_color='Custom'
            self.speaker.icon_color = (0,1,0.3,1)
            self.next_button.disabled = False

        #then autoplay recorded
        self.listen_answer()
        

    def answer(self):
        self.answer_file = self.current_answer + '.m4a'
        duration = 4
        freq = 44100
        #record = rec(f'answers/phase4/{self.answer_file}')
        record = android_record(f'/storage/emulated/0/pb/answers/phase4/{self.answer_file}')

        self.tries.append(self.answer_file)
        return record


    def listen_answer(self):
        self.answer_file = self.current_answer + '.m4a'

        if self.answer_file in self.tries:
            path_to_file = f'answers/phase4/{self.answer_file}'
            
            if platform == 'android':
                path_to_file = f'/storage/emulated/0/pb/answers/phase4/{self.answer_file}'
                play_audio(path_to_file)
            else:
                if self.sound:
                    self.sound.stop()
                self.sound = SoundLoader.load(path_to_file)
                self.sound.play()
        else:
            print('answer first!')
         
class WordBox(Scatter):
    word = StringProperty('')
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)

    
    