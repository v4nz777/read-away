from kivymd.uix.screen import MDScreen
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, BooleanProperty, ListProperty
from materials import CONSONANTS, VOWELS, CONSONANTS_EZ
from kivy.metrics import dp
import random
from kivy.clock import Clock
from kivymd.uix.behaviors.magic_behavior import MagicBehavior

from sound_recorder import rec
#from jniusrecord import android_record, play_audio
from kivy.utils import platform


from kivy.core.window import Window


class TwoLetterWords(MDScreen):
    blank_1 = ObjectProperty(None)
    blank_2 = ObjectProperty(None)
    consonants = ObjectProperty(None)
    vowels = ObjectProperty(None)
    bg_water = ObjectProperty(None)
    create_scat = ObjectProperty(None)

    def on_enter(self, *args):
        if self.create_scat == None: 
            for consonant in CONSONANTS:
                self.create_scat = Cons(size_hint=(None, None), size=(dp(55),dp(50)), letter=consonant.lower())
                
                if consonant == 'ñ'.upper() or consonant == 'ng'.upper() or consonant == 'q'.upper():
                    continue
                self.create_scat.children[0].source = f'imgs/letter_blocks/{consonant.lower()}.png'
                self.consonants.add_widget(self.create_scat)
        
            for vowel in VOWELS:
                self.create_scat = Vowl(size_hint=(None, None), size=(dp(55),dp(50)), letter=vowel.lower())
                self.create_scat.add_widget(Image(size=(dp(55),dp(50))))

                self.create_scat.children[0].source = f'imgs/letter_blocks/bl{vowel.lower()}.png'

                self.vowels.add_widget(self.create_scat)
            
        return super().on_enter(*args)



class Cons(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    letter = StringProperty('')
    sound = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Cons,self).__init__(**kwargs)
        self.initial_pos = self.pos
        self.auto_bring_to_front = False
        self.size_hint = (None,None)
        self.do_rotation = False
        self.do_scale = False

        self.add_widget(Image(size=self.size, pos=self.pos))
        


    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.sound:
                    self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase2/letter_sounds/{self.letter.upper()}.ogg')
            self.sound.play()
        return super().on_touch_down(touch)




    def on_touch_up(self, touch):
        target1 = self.parent.parent.parent.parent.parent.blank_1
        target2 = self.parent.parent.parent.parent.parent.blank_2

        if self.collide_widget(target1):
            if target2.letter_inside.upper() not in CONSONANTS:
                if self.letter == 'ñ':
                    target1.children[0].source = f'imgs/letter_blocks/enye.png'
                else:
                    target1.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
                target1.letter_inside = self.letter
                target1.filled = True
                #TODO SOUND
                if target1.filled and target2.filled:
                    target1.shake()
                    target2.shake()
                    print(f'{target1.letter_inside}{target2.letter_inside}')
                    if self.sound:
                        self.sound.stop()
                    self.sound = SoundLoader.load(f'src/phase3/{target1.letter_inside}{target2.letter_inside}.ogg')
                    self.sound.play()
            
        elif self.collide_widget(target2):
            if target1.letter_inside.upper() not in CONSONANTS:
                if self.letter == 'ñ':
                    target2.children[0].source = f'imgs/letter_blocks/enye.png'
                else:
                    target2.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
                target2.letter_inside = self.letter
                target2.filled = True
                #TODO SOUND
                if target1.filled and target2.filled:
                    target1.shake()
                    target2.shake()
                    print(f'{target1.letter_inside}{target2.letter_inside}')
                    if self.sound:
                        self.sound.stop()
                    self.sound = SoundLoader.load(f'src/phase3/{target1.letter_inside}{target2.letter_inside}.ogg')
                    self.sound.play()
        

        if touch in self._touches and touch.grab_state:
            touch.ungrab(self)
            del self._last_touch_pos[touch]
            self._touches.remove(touch)
            x,y = self.initial_pos
            self.pos = (x,y)
            #trick to refresh boxes in their places
            temp_size = Window.size
            xx,yy = temp_size
            Window.size = (xx+1,  yy+1)
            #Get to normal size
            Window.size = (xx-1,  yy-1)
            
            

class Vowl(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    letter = StringProperty('')
    sound = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Vowl,self).__init__(**kwargs)
        self.initial_pos = self.pos
        self.auto_bring_to_front = False
        self.size_hint = (None,None)
        self.do_rotation = False
        self.do_scale = False

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.sound:
                    self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase2/letter_sounds/{self.letter.upper()}.ogg')
            self.sound.play()
        return super().on_touch_down(touch)
        
    def on_touch_up(self, touch):
        target1 = self.parent.parent.parent.parent.parent.blank_1
        target2 = self.parent.parent.parent.parent.parent.blank_2

        if self.collide_widget(target1):
            
            if target2.letter_inside.upper() not in VOWELS:
                target1.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
                target1.letter_inside = self.letter
                target1.filled = True
                if target1.filled and target2.filled:
                    target1.shake()
                    target2.shake()
                    print(f'{target1.letter_inside}{target2.letter_inside}')
                    if self.sound:
                        self.sound.stop()
                    self.sound = SoundLoader.load(f'src/phase3/{target1.letter_inside}{target2.letter_inside}.ogg')
                    self.sound.play()
            
        elif self.collide_widget(target2):
            if target1.letter_inside.upper() not in VOWELS:
                target2.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
                target2.letter_inside = self.letter
                target2.filled = True
                #TODO SOUND
                if target1.filled and target2.filled:
                    target1.shake()
                    target2.shake()
                    print(f'{target1.letter_inside}{target2.letter_inside}')
                    if self.sound:
                        self.sound.stop()
                    self.sound = SoundLoader.load(f'src/phase3/{target1.letter_inside}{target2.letter_inside}.ogg')
                    self.sound.play()
        

        if touch in self._touches and touch.grab_state:
            touch.ungrab(self)
            del self._last_touch_pos[touch]
            self._touches.remove(touch)
            self.pos = self.parent.pos
            x,y = self.initial_pos
            self.pos = (x,y)
            #trick to refresh boxes in their places
            temp_size = Window.size
            xx,yy = temp_size
            Window.size = (xx+1,  yy+1)
            #Get to normal size
            Window.size = (xx-1,  yy-1)


class Blanky(Scatter, MagicBehavior):
    letter_inside = StringProperty('')
    filled = BooleanProperty(False)

    def on_touch_down(self, touch):
        self.letter_inside = ''
        self.filled = False
        self.children[0].source = 'imgs/letter_blocks/empty.png'
        return super().on_touch_down(touch)





###################################### LEVEL 3 ############################################
class TwoLetterWordsLevel3(MDScreen):
    first_box = ObjectProperty(None)
    second_box = ObjectProperty(None)
    current_answer = StringProperty('')
    showed = ListProperty([])
    tries = ListProperty([])
    corrected = ListProperty([])

    sound = ObjectProperty(None)
    
    progress_bar = ObjectProperty(None)
    microphone = ObjectProperty(None)
    speaker = ObjectProperty(None)
    next_button = ObjectProperty(None)
    toolbar = ObjectProperty(None)

    def option_1(self):

        cltr = random.choice(CONSONANTS_EZ)
        vltr = random.choice(VOWELS)
        self.first_box.letter = cltr.lower()
        if self.first_box.letter == 'ñ'.upper():
            self.first_box.children[0].source = f'imgs/letter_blocks/enye.png'
        else:    
            self.first_box.children[0].source = f'imgs/letter_blocks/{self.first_box.letter}.png'

        
        self.second_box.letter = vltr.lower()
        if self.second_box.letter == 'ñ'.upper():
            self.second_box.children[0].source = f'imgs/letter_blocks/enye.png'
        else:
            self.second_box.children[0].source = f'imgs/letter_blocks/{self.second_box.letter}.png'

        self.first_box.final_pos = self.first_box.pos
        x,y = self.first_box.final_pos
        self.first_box.pos = (x-self.width,y)
        anim1 = Animation(x=x, size=(80, 80), t='out_bounce')
        anim1.start(self.first_box)

        self.second_box.final_pos = self.second_box.pos
        xx,yy = self.second_box.final_pos
        self.second_box.pos = (xx+self.width,yy)
        anim2 = Animation(x=xx, size=(80, 80), t='out_bounce')
        anim2.start(self.second_box)
        return self.first_box.letter + self.second_box.letter
    
    def option_2(self):

        cltr = random.choice(CONSONANTS_EZ)
        vltr = random.choice(VOWELS)
        self.first_box.letter = vltr.lower()
        if self.first_box.letter == 'ñ'.upper():
            self.first_box.children[0].source = f'imgs/letter_blocks/enye.png'
        else:
            self.first_box.children[0].source = f'imgs/letter_blocks/{self.first_box.letter}.png'

        self.second_box.letter = cltr.lower()
        if self.second_box.letter == 'ñ'.upper():
            self.second_box.children[0].source = f'imgs/letter_blocks/enye.png'
        else:
            self.second_box.children[0].source = f'imgs/letter_blocks/{self.second_box.letter}.png'
        
        self.first_box.final_pos = self.first_box.pos
        x,y = self.first_box.final_pos
        self.first_box.pos = (x-self.width,y)
        anim1 = Animation(x=x, size=(80, 80), t='out_bounce')
        anim1.start(self.first_box)

        self.second_box.final_pos = self.second_box.pos
        xx,yy = self.second_box.final_pos
        self.second_box.pos = (xx+self.width,yy)
        anim2 = Animation(x=xx, size=(80, 80), t='out_bounce')
        anim2.start(self.second_box)
        return self.first_box.letter + self.second_box.letter

 
    def next(self):
        choices = [self.option_1, self.option_2]
        zzz = len(self.showed)/10
        self.progress_bar.value = zzz * 100
        if len(self.showed) != 10:
            self.current_answer = random.choice(choices)()
            while self.current_answer in self.showed:
                self.current_answer = random.choice(choices)()

            self.showed.append(self.current_answer)
            print(self.current_answer)
        else:
            title = '2 letter-words quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.showed)}/10'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL Letters ALREADY ANSWERED')
        self.speaker.theme_icon_color = 'Primary' 
        self.next_button.disabled = True
    
    def initial(self,dt):
        choices = [self.option_1, self.option_2]
        if len(self.showed) != 10:
            self.current_answer = random.choice(choices)()
            while self.current_answer in self.showed:
                self.current_answer = random.choice(choices)()
                
            self.showed.append(self.current_answer)
            print(self.current_answer)
        else:
            title = '2 letter-words quiz'
            prev = self.manager.previous()
            next = self.manager.next()
            page = self.manager.current
            disabled = False
            score = f'Congratulations! Quiz Complete! \nTotal Answered: {len(self.showed)}/10'
            self.manager.created_dialog_quiz(prev, next, title, page, score, disabled)
            self.manager.opt_menu.open()
            print('ALL Letters ALREADY ANSWERED')

    def on_enter(self):
        Clock.schedule_once(self.initial)

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
        record = rec(f'answers/phase3/{self.answer_file}')
        #record = android_record(f'/storage/emulated/0/pb/answers/phase3/{self.answer_file}')



        
        self.tries.append(self.answer_file)
        return record
    

    def listen_answer(self):
        self.answer_file = self.current_answer + '.wav'

        if self.answer_file in self.tries:
            path_to_file = f'answers/phase3/{self.answer_file}'
            
            if platform == 'android':
                path_to_file = f'/storage/emulated/0/pb/answers/phase3/{self.answer_file}'
                play_audio(path_to_file)
            else:
                if self.sound:
                    self.sound.stop()
                self.sound = SoundLoader.load(path_to_file)
                self.sound.play()
        else:
            print('answer first!')

        
class FirstBox(Scatter):
    letter = StringProperty('')
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)
    
class SecondBox(Scatter):
    letter = StringProperty('')
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)

