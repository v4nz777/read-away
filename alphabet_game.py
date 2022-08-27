
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty, BooleanProperty
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
from kivymd.uix.dialog import MDDialog
from kivy.core.audio import SoundLoader
from kivy.graphics import Line, Color, Rectangle, InstructionGroup
from materials import FILIPINO_ALPHABETS
from kivy.metrics import dp
from kivy.base import EventLoop
from kivy.utils import platform
import random

class CapitalLetter(MDRaisedButton, MagicBehavior):
    name = StringProperty("cap")
    used = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(CapitalLetter, self).__init__(**kwargs)
        self._min_width = dp(0)
        self.padding = [dp(8),dp(16),dp(8),dp(16)]

class SmallLetter(MDRaisedButton):
    name = StringProperty("small")
    def __init__(self, **kwargs):
        super(SmallLetter, self).__init__(**kwargs)
        self._min_width = dp(4)
        self.padding = [dp(8),dp(16),dp(8),dp(16)]
        self.text = self.text.lower()

  

class DrawingCanvas(MDWidget):
    started = BooleanProperty(False)
    item = ObjectProperty(None)
    initial_x = NumericProperty(0)
    initial_y = NumericProperty(0)

    final_x = NumericProperty(0)
    final_y = NumericProperty(0)

    selected = StringProperty("")
    score = NumericProperty(0)
    items_answered = ListProperty([])
    scorecard = ObjectProperty(None)

    pointers = ListProperty([])
    initialized_btns = ListProperty([])


    def set_initial(self, instance):
        self.item = instance
        self.initial_x = instance.x
        self.initial_y = instance.y
        if not self.started and not instance.used:
            self.draw_point(instance)
            self.selected = instance.text
            instance.used = True
            self.initialized_btns.append(instance)
            self.started = True
            pop = SoundLoader.load("pop.wav")
            pop.play()

        elif self.started and not instance.used and len(self.pointers) >= 1:
            for i in self.pointers:
                with self.canvas:
                    if i not in self.items_answered:
                        self.canvas.remove_group(i)
            for z in self.initialized_btns:
                z.used = False

            self.pointers.clear()
            self.draw_point(instance)
            self.selected = instance.text
            instance.used = True
            self.initialized_btns.append(instance)
            self.started = True
            pop = SoundLoader.load("pop.wav")
            pop.play()

        else:
            self.erase_point(instance)
            self.set_default(instance)
        
        print(self.pointers)
            
            
        
    
    def finish_line(self, instance):
        if self.started:
            self.final_x = instance.x
            self.final_y = instance.y
            self.draw_point(instance)
            self.draw_line(instance)
            if self.selected == instance.text.upper():
                self.item.disabled_color = (1,1,1,1)
                self.item.md_bg_color_disabled = (1,0.3,0,1)
                self.item.wobble()
                correct = SoundLoader.load("coin.wav")
                correct.play()
                self.score += 1
            else:
                self.item.twist()
                wrong = SoundLoader.load("wrong.wav")
                wrong.play()
            self.items_answered.append(self.selected)
            self.item.disabled = True
            self.item.used = True
            self.set_default(instance)
            print(self.items_answered)

            if len(self.items_answered) == 28:
                if self.score < 21:
                    score_status = "#C41E3A"
                elif self.score >= 21:
                    score_status = "#0000FF"
                elif self.score == 28:
                    score_status = "#228B22"

                close_btn = MDRaisedButton(text="Ok")
                self.scorecard = MDDialog(
                    buttons = [
                        close_btn,
                    ]
                )
                self.scorecard.title = f"Score: [color={score_status}]{self.score}[/color]/[color=#228B22]28[/color]"
                self.scorecard.open()
                close_btn.bind(on_release=self.scorecard.dismiss)
                finish = SoundLoader.load("game_win.wav")
                finish.play()


    def set_default(self, instance):
        self.initial_x = 0
        self.initial_y = 0

        self.final_x = 0
        self.final_y = 0
        self.started = False
        instance.used = False


    def draw_point(self, instance):
        btn_width = instance.width/2
        btn_height = instance.height/3
        if instance.name == "cap":
            x = instance.x + btn_width
            y = instance.y - btn_height
            self.initial_x = x
            self.initial_y = y
        elif instance.name == "small":
            x = instance.x + btn_width
            y = instance.y + (btn_height * 4)
            self.final_x = x
            self.final_y = y
        with self.canvas:
            Color(rgba=(0,0.7,1,1), group=instance.text)
            Line(points=(x,y,x,y), width=10, joint="round", close=True, cap="round", group=instance.text)
            if instance.name == "cap":
                self.pointers.append(instance.text)


    
    def erase_point(self, instance):

        if instance.name == "cap":
            with self.canvas:
                self.canvas.remove_group(instance.text)
                if len(self.pointers) > 0:
                    self.pointers.pop(-1)
            unpop = SoundLoader.load("unpop.wav")
            unpop.play()

        else:
            pass
        

    def draw_line(self, instance):
        if self.selected == instance.text.upper():
            color = (0,0,1,1)
        else:
            color = (1,0,0,1)
        with self.canvas.after:
            Color(rgba=color)
            Line(points=(self.initial_x,self.initial_y,self.final_x,self.final_y), width=2, joint="round", close=True, cap="round")






class AlphabetGame(MDScreen):
    caps = ObjectProperty(None)
    smalls = ObjectProperty(None)
    drawing_canvas = ObjectProperty(None)
    top_spacer = ObjectProperty(None)

    def on_enter(self, *args):
        # Confiure top spacer
        self.top_spacer = self.ids.top_spacer

        if platform == "android":
            self.top_spacer.size_hint_y = 0.4
        else:
            self.top_spacer.size_hint_y = None
            self.top_spacer.height = 0

        # Configure other elements
        self.caps = self.ids.capital_letters
        self.smalls = self.ids.small_letters

        self.caps.spacing = dp(15)
        self.smalls.spacing = dp(15)

        self.caps.padding = [dp(20), dp(20), dp(20), dp(20)]
        self.smalls.padding = [dp(20), dp(20), dp(20), dp(20)]
        if len(self.caps.children) == 0:
            for cap in FILIPINO_ALPHABETS:
                btn = CapitalLetter(text=cap, font_name="ShadowsIntoLight-Regular.ttf", font_size="20sp")
                btn.size_hint=(1, None)
                btn.bind(on_release=self.drawing_canvas.set_initial)
                self.caps.add_widget(btn)
        
        if len(self.smalls.children) == 0:
            shuffled = random.sample(FILIPINO_ALPHABETS, len(FILIPINO_ALPHABETS))
            for small in shuffled:

                btn = SmallLetter(text=small, font_name="ShadowsIntoLight-Regular.ttf", font_size="20sp")
                btn.bind(on_release=self.drawing_canvas.finish_line)
                self.smalls.add_widget(btn)
        

        return super().on_enter(*args)
    

    

