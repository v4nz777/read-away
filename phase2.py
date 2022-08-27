from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.core.audio import SoundLoader
from kivy.uix.carousel import Carousel
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty


from sound_recorder import rec
#from jniusrecord import android_record, play_audio
from kivy.utils import platform



import random

from materials import FILIPINO_ALPHABETS, PHONOGRAM_ALPHA, PHONOGRAM_MULTI_CT, PHONOGRAM_MULTI_VT

from materials import lowercase as fil_lowercase


class PhonogramAlpha(MDScreen):
    toolbar = ObjectProperty(None)
    carousel = ObjectProperty(None)
    sound = ObjectProperty(None)
    button = ObjectProperty(None)

    def on_enter(self, *args):
        
        
        self.phonograms_alpha = self.ids.phonograms_alpha
        self.phonograms_ct = self.ids.phonograms_ct
        self.phonograms_vt = self.ids.phonograms_vt

        if len(self.phonograms_alpha.children) == 0 and len(self.phonograms_ct.children) == 0 and len(self.phonograms_vt.children) == 0:
            for letter in PHONOGRAM_ALPHA:
                self.button = MDRaisedButton(text=letter,font_size='25sp',font_name='ShadowsIntoLight-Regular.ttf')
                self.button.bind(on_press=self.letter_sound)
                self.phonograms_alpha.add_widget(self.button)
        
            for letter in PHONOGRAM_MULTI_CT:
                self.button = MDRaisedButton(text=letter,font_size='25sp', font_name='ShadowsIntoLight-Regular.ttf')
                self.button.bind(on_press=self.letter_sound)
                self.phonograms_ct.add_widget(self.button)
            
            for letter in PHONOGRAM_MULTI_VT:
                self.button = MDRaisedButton(text=letter,font_size='25sp', font_name='ShadowsIntoLight-Regular.ttf')
                self.button.bind(on_press=self.letter_sound)
                self.phonograms_vt.add_widget(self.button)

        return super().on_enter(*args)

    def letter_sound(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop() 
            filename = instance.text
            self.sound = SoundLoader.load(f'src/phase2/phonogram/{filename}.ogg')
            self.sound.play()

class Carou(Carousel):
    def on_touch_move(self, touch):
        # if self.index == 1:
        #     self.parent.toolbar.disabled = False
        return super().on_touch_move(touch)


class PhaseTwoTest(MDScreen):
    the_letter = ObjectProperty(None)
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
        self.the_letter.final_pos = self.the_letter.pos
        return super().on_enter(*args)

    def show_letter(self):
        zzz = len(self.corrected)/28
        self.progress_bar.value = zzz * 100
        if len(self.corrected) != 28:
            self.current_answer = random.choice(fil_lowercase)
            while self.current_answer in self.corrected:
                self.current_answer = random.choice(fil_lowercase)

            self.the_letter.final_pos = self.the_letter.pos
            x,y = self.the_letter.final_pos
            self.the_letter.pos = (x, y+self.height)

            self.the_letter.children[0].text = f'{self.current_answer}'
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.the_letter)
            self.corrected.append(self.current_answer)
            print(self.current_answer)
        else:
            title = 'Phonetics Quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.corrected)}/28'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL Letters ALREADY ANSWERED')
            
        self.speaker.theme_icon_color = 'Primary'
        self.next_button.disabled = True

    def start_show_letter(self, dt):

        if len(self.corrected) != 28:
            self.current_answer = random.choice(fil_lowercase)
            while self.current_answer in self.corrected:
                self.current_answer = random.choice(fil_lowercase)

            self.the_letter.final_pos = self.the_letter.pos
            x,y = self.the_letter.final_pos
            self.the_letter.pos = (x, y+self.height)

            self.the_letter.children[0].text = f'{self.current_answer}'
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.the_letter)
            self.corrected.append(self.current_answer)
            print(self.current_answer)
        else:
            title = 'Phonetics Quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.corrected)}/28'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL Letters ALREADY ANSWERED')

        self.speaker.theme_icon_color = 'Primary'
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
        self.answer_file = self.current_answer + '.wav'
        duration = 4
        freq = 44100
        record = rec(f'answers/phase2/{self.answer_file}')
        #record = android_record(f'/storage/emulated/0/pb/answers/phase2/{self.answer_file}')

        self.tries.append(self.answer_file)
        return record
    


    
    def listen_answer(self):
        self.answer_file = self.current_answer + '.wav'

        if self.answer_file in self.tries:

            path_to_file = f'answers/phase2/{self.answer_file}'
            
            if platform == 'android':
                path_to_file = f'/storage/emulated/0/pb/answers/phase2/{self.answer_file}'
                play_audio(path_to_file)
            else:
                if self.sound:
                    self.sound.stop()
                self.sound = SoundLoader.load(path_to_file)
                self.sound.play()
        else:
            print('answer first!')



class TheLetter(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)