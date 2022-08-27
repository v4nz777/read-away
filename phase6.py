from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty
from materials import DIPTHONGS, DIPTHONGS_EX, DIGRAPHS, DIGRAPHS_EX,  CONSONANTBLENDS, CONSONANTBLENDS_EX, DIP_DIG_CON_QUIZ
import random
from kivy.clock import Clock

#from sound_recorder import rec
from jniusrecord import android_record, play_audio
from kivy.utils import platform




    
        


class Phase6Main(MDScreen):
    dipthongs_samp: ObjectProperty(None)
    digraphs_samp: ObjectProperty(None)
    consblends_samp: ObjectProperty(None)
    sound = ObjectProperty(None)
    
    def on_enter(self, *args):

        for dipt in DIPTHONGS:
            self.btn = MDRaisedButton(
                font_size='25sp',
                md_bg_color=(0.8, 0.3, 0.2, 1),
                font_name= 'ShadowsIntoLight-Regular.ttf'
                )
            self.btn.size_hint = 1,None
            self.btn.text = dipt
            self.btn.bind(on_release = self.listen)
            self.dipthongs_samp.add_widget(self.btn)

        for dig in DIGRAPHS:
            self.btn = MDRaisedButton(
                font_size='25sp',
                md_bg_color=(0.3, 0.8, 0.2, 1),
                font_name= 'ShadowsIntoLight-Regular.ttf'
                )
            self.btn.text = dig
            self.btn.size_hint = 1,None
            self.btn.bind(on_release = self.listen)
            self.digraphs_samp.add_widget(self.btn)

        for consbl in CONSONANTBLENDS:
            self.btn = MDRaisedButton(
                font_size='25sp',
                md_bg_color=(0.2, 0.3, 0.8, 1),
                font_name= 'ShadowsIntoLight-Regular.ttf'
                )
            self.btn.text = consbl
            self.btn.size_hint = 1,None
            self.btn.bind(on_release = self.listen)
            self.consblends_samp.add_widget(self.btn)
        return super().on_enter(*args)

    def listen(self, instance):

        try:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase2/phonogram/{instance.text}.ogg')
            self.sound.play()

        except:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase6/{instance.text}.ogg')
            self.sound.play()




class Dipthongs(MDScreen):

    def on_enter(self, *args):

        self.dipthongs = self.ids.dipthongs
        self.sound = None
        self.button = None
        if len(self.dipthongs.children) == 0:
            for word in DIPTHONGS_EX:
                self.button = MDRaisedButton(text=word,font_size='25sp', md_bg_color=(0.8, 0.3, 0.2, 1))
                self.button.bind(on_press=self.say_word)
                self.dipthongs.add_widget(self.button)

        return super().on_enter(*args)
    
    def say_word(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase6/examples/{instance.text}.ogg')
            self.sound.play()

class Digraphs(MDScreen):

    def on_enter(self, *args):
    
        self.digraphs = self.ids.digraphs
        self.sound = None
        self.button = None
        if len(self.digraphs.children) == 0:
            for word in DIGRAPHS_EX:
                self.button = MDRaisedButton(text=word,font_size='25sp', size_hint=(None,None), md_bg_color=(0.3, 0.8, 0.2, 1))
                self.button.bind(on_press=self.say_word)
                self.digraphs.add_widget(self.button)
        return super().on_enter(*args)
    
    def say_word(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase6/examples/{instance.text}.ogg')
            self.sound.play()

class ConsBlends(MDScreen):
    def on_enter(self, *args):

        self.consblends = self.ids.consblends
        self.sound = None
        self.button = None
        if len(self.consblends.children) == 0:
            for word in CONSONANTBLENDS_EX:
                self.button = MDRaisedButton(text=word,font_size='25sp', size_hint=(None,None), md_bg_color=(0.2, 0.3, 0.8, 1))
                self.button.bind(on_press=self.say_word)
                self.consblends.add_widget(self.button)
        return super().on_enter(*args)
    
    def say_word(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase6/examples/{instance.text}.ogg')
            self.sound.play()

class WordOutline(Scatter):
    word = StringProperty('')
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)


class P6Quiz(MDScreen):
    word_outline = ObjectProperty(None)
    current_answer = StringProperty('')
    shown = ListProperty([])
    tries = ListProperty([])

    sound = ObjectProperty(None)
    
    progress_bar = ObjectProperty(None)
    microphone = ObjectProperty(None)
    speaker = ObjectProperty(None)
    next_button = ObjectProperty(None)
    toolbar = ObjectProperty(None)

    def show_word(self):
        zzz = len(self.shown)/30
        self.progress_bar.value = zzz * 100
        if len(self.shown) != 30:
            self.current_answer = random.choice(DIP_DIG_CON_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(DIP_DIG_CON_QUIZ)

            self.word_outline.final_pos = self.word_outline.pos
            x,y = self.word_outline.final_pos
            self.word_outline.pos = (x, y+self.height)
            
            self.word_outline.children[0].source = f'imgs/dip_dig_con/{self.current_answer}.png'
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.word_outline)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            title = 'DDC Quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.shown)}/30'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL 30 ALREADY ANSWERED')

        self.speaker.theme_icon_color = 'Primary'
        self.next_button.disabled = True


    def start_show_word(self, dt):
        if len(self.shown) != 30:
            self.current_answer = random.choice(DIP_DIG_CON_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(DIP_DIG_CON_QUIZ)

    
            self.word_outline.final_pos = self.word_outline.pos
            x,y = self.word_outline.final_pos
            self.word_outline.pos = (x, y+self.height)
            
            self.word_outline.children[0].source = f'imgs/dip_dig_con/{self.current_answer}.png'
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.word_outline)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            title = 'DDC Quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.shown)}/30'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL 30 ALREADY ANSWERED')
    

    def on_enter(self):
        Clock.schedule_once(self.start_show_word)

    def validate(self):
        self.sound = SoundLoader.load('src/pre_record_sound.ogg')
        self.sound.play()
        answer = self.answer()
        while not answer:
            #self.microphone = MDSpinner()
            self.microphone.disabled = True
            self.microphone.theme_icon_color='Custom'
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
        #record = rec(f'answers/phase6/{self.answer_file}')
        record = android_record(f'/storage/emulated/0/pb/answers/phase6/{self.answer_file}')
        self.tries.append(self.answer_file)
        return record


    def listen_answer(self):
        self.answer_file = self.current_answer + '.m4a'

        if self.answer_file in self.tries:
            path_to_file = f'answers/phase6/{self.answer_file}'
            
            if platform == 'android':
                path_to_file = f'/storage/emulated/0/pb/answers/phase6/{self.answer_file}'
                play_audio(path_to_file)
            else:
                if self.sound:
                    self.sound.stop()
                self.sound = SoundLoader.load(path_to_file)
                self.sound.play()
        else:
            print('answer first!') 

class WordOutlineRed(Scatter):
    word = StringProperty('')
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)