
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton

from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty

from sound_recorder import rec
#from jniusrecord import android_record, play_audio




from kivy.utils import platform


import random

from materials import FILIPINO_ALPHABETS, TOTAL_ALPHABETS




class IntroToAlphabets(MDScreen):
    sound = ObjectProperty(None)
    button = ObjectProperty(None)

    def on_enter(self, *args):
        self.abctable = self.ids.abc
        if len(self.abctable.children) == 0:
            for letter in FILIPINO_ALPHABETS:
                self.button = MDRaisedButton(text=letter+letter.lower(),font_size='30sp', size_hint=(1,None), font_name='ShadowsIntoLight-Regular.ttf')
                self.button.bind(on_press=self.say_the_letter)
                self.abctable.add_widget(self.button)
        return super().on_enter(*args)
        
    
    def say_the_letter(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop()
            if instance.text == 'NGng':
                self.sound = SoundLoader.load(f'src/phase1/alphabets/NG.ogg')
            elif instance.text == 'Ññ':
                self.sound = SoundLoader.load(f'src/phase1/alphabets/ENYE.ogg')
            else:
                self.sound = SoundLoader.load(f'src/phase1/alphabets/{instance.text[0]}.ogg')
            self.sound.play()


class PhaseOneTest(MDScreen):#IntroToAlphabets
    the_alphabet = ObjectProperty(None)
    progress_bar = ObjectProperty(None)
    microphone = ObjectProperty(None)
    speaker = ObjectProperty(None)
    next_button = ObjectProperty(None)
    toolbar = ObjectProperty(None)
    sound = ObjectProperty(None)

    tries = ListProperty([])
    corrected = ListProperty([])
    current_answer = StringProperty('')
    answer_file = StringProperty('')

    def on_enter(self, *args):
        self.the_alphabet.final_pos = self.the_alphabet.pos
        return super().on_enter(*args)

  
    def show_letter(self):

        zzz = len(self.corrected)/56
        self.progress_bar.value = zzz * 100
        if len(self.corrected) != 56:
            self.current_answer = random.choice(TOTAL_ALPHABETS)
            while self.current_answer in self.corrected:
                self.current_answer = random.choice(TOTAL_ALPHABETS)

            self.the_alphabet.final_pos = self.the_alphabet.pos
            x,y = self.the_alphabet.final_pos
            self.the_alphabet.pos = (x, y+self.height)

            self.the_alphabet.children[0].text = f'{self.current_answer}'
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.the_alphabet)
            self.corrected.append(self.current_answer)
            print(self.current_answer)
        else:
            title = 'Alphabet Quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.corrected)}/56'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL Letters ALREADY ANSWERED')

        self.speaker.theme_icon_color = 'Primary'
        self.next_button.disabled = True

    def start_show_letter(self, dt):

        if len(self.corrected) != 56:
            self.current_answer = random.choice(TOTAL_ALPHABETS)
            while self.current_answer in self.corrected:
                self.current_answer = random.choice(TOTAL_ALPHABETS)

            self.the_alphabet.final_pos = self.the_alphabet.pos
            x,y = self.the_alphabet.final_pos
            self.the_alphabet.pos = (x, y+self.height)
            
            self.the_alphabet.children[0].text = f'{self.current_answer}'
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.the_alphabet)
            self.corrected.append(self.current_answer)
            print(self.current_answer)
        else:
            title = 'Alphabet Quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.corrected)}/56'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL Letters ALREADY ANSWERED')
        self.next_button.disabled = True

    def on_enter(self):
        Clock.schedule_once(self.start_show_letter)

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
        if self.current_answer.isupper():
            self.answer_file = 'big' + '-' + self.current_answer + '.wav'
        else:
            self.answer_file = 'small' + '-' + self.current_answer + '.wav'
        duration = 3
        freq = 44100
        record = rec(f'answers/phase1/{self.answer_file}')   
        #record = android_record(f'/storage/emulated/0/pb/answers/phase1/{self.answer_file}')
        self.tries.append(self.answer_file)
        return record

        
    
    
    def listen_answer(self):
        if self.current_answer.isupper():
            self.answer_file = 'big' + '-' + self.current_answer + '.wav'
        else:
            self.answer_file = 'small' + '-' + self.current_answer + '.wav'

        if self.answer_file in self.tries:
            path_to_file = f'answers/phase1/{self.answer_file}'

            if platform == 'android':
                path_to_file = f'/storage/emulated/0/pb/answers/phase1/{self.answer_file}'
                play_audio(path_to_file)
            else:
                if self.sound:
                    self.sound.stop()
                self.sound = SoundLoader.load(path_to_file)
                self.sound.play()

        else:
            print('answer first!')

class TheAlphabet(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)

    
