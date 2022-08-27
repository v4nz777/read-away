from kivymd.uix.button import MDIconButton
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.core.audio import SoundLoader
#from jniusrecord import play_audio
from kivy.utils import platform
from kivymd.uix.card import MDCard, MDSeparator
from kivy.metrics import dp
import json

#CONTENTS
# from phase1 import IntroToAlphabets, PhaseOneTest
# from phase2 import Phoenetics, PhaseTwoTest
# from phase3 import TwoLetterWords,TwoLetterWordsLevel2,TwoLetterWordsLevel3
# from phase4 import Cvc, VowelA,VowelE,VowelI,VowelO,VowelU, CvcQuiz
# from phase5 import CVCandE, CvcQuiz2
# from phase6 import Dipthongs, Digraphs, ConsBlends, Phase6Main, P6Quiz

from kivy.properties import ListProperty, ObjectProperty
import os




class AnswerP1(Screen):
    sound = ObjectProperty(None)
    a_list = ListProperty([])
    directory = ListProperty([])
    def __init__(self, **kw):
        super(AnswerP1, self).__init__(**kw)
        self.table = self.ids.answers_p1

    def on_pre_leave(self, *args):
        if self.sound:
            self.sound.stop()
            
        return super().on_pre_leave(*args)

    def on_enter(self, *args):
        self.make_list()
        return super().on_enter(*args)

    def make_list(self):
        if platform == "android":
            self.directory = os.listdir("/storage/emulated/0/pb/answers/phase1")
        else:
            self.directory = os.listdir("answers/phase1")
            
        
        for i in sorted(self.directory):
            answer = i[-5]
            if i == "big-NG.wav":
                answer = "NG"
            elif i == "small-ng.wav":
                answer = "ng"
            elif i == "big-ENYE.wav":
                answer = "Ñ"
            elif i == "small-enye.wav":
                answer = "Ñ".lower()
            
            #SKIP DUPLICATES
            if answer in self.a_list:
                continue
             
            self.table.add_widget(Label(
                text=answer,
                font_name="NotoSerif-Regular.ttf",
                color=(0,0,.5,1),
                font_size="35sp",
                halign="center"
    
                )
            )

            self.btn = MDIconButton(
                icon="volume-high",
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

            #THEN ADD TO THE LIST TO AVOID DUPLICATION
            self.a_list.append(answer)

     

    def listen_answer(self, instance):
        answer = instance.text 
        if instance.text.isupper():
            answer = "big" + "-" + instance.text + ".wav"
        else:
            answer = "small" + "-" + instance.text + ".wav"

        path_to_file = f"answers/phase1/{answer}"
        if platform ==  "android":
            path_to_file = f"/storage/emulated/0/pb/answers/phase1/{answer}"
            play_audio(path_to_file)
        else:
            if self.sound:
                self.sound.stop()
            print(path_to_file)
            self.sound = SoundLoader.load(path_to_file)
            self.sound.play()


########################################################################################

class AnswerP2(Screen):
    a_list = ListProperty([])
    sound = ObjectProperty(None)
    directory = ListProperty([])
    def __init__(self, **kw):
        super(AnswerP2, self).__init__(**kw)
        self.table = self.ids.answers_p2

    def on_pre_leave(self, *args):
        if self.sound:
            self.sound.stop()
            
        return super().on_pre_leave(*args)

    def on_enter(self, *args):
        self.make_list()
        return super().on_enter(*args)

    def make_list(self):
        if platform == "android":
            self.directory = os.listdir("/storage/emulated/0/pb/answers/phase2")
        else:
            self.directory = os.listdir("answers/phase2")

        
        for i in self.directory:
            if i == "enye.wav":
                answer = "Ñ".lower()
            else:
                answer = i.replace(".wav", "")
            
            #SKIP DUPLICATES
            if answer in self.a_list:
                continue
             
            self.table.add_widget(Label(
                text=answer,
                font_name="NotoSerif-Regular.ttf",
                color=(0,0,.5,1),
                font_size="35sp",
                halign="center"
    
                )
            )

            self.btn = MDIconButton(
                icon="volume-high",
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

            #THEN ADD TO THE LIST TO AVOID DUPLICATION
            self.a_list.append(answer)


    def listen_answer(self, instance):
        answer = instance.text + ".wav"

        path_to_file = f"answers/phase2/{answer}"
        if platform ==  "android":
            path_to_file = f"/storage/emulated/0/pb/answers/phase2/{answer}"
            play_audio(path_to_file)
        else:
            if self.sound:
                self.sound.stop()
            print(path_to_file)
            self.sound = SoundLoader.load(path_to_file)
            self.sound.play()




########################################################################################    

class AnswerP3(Screen):
    a_list = ListProperty([])
    sound = ObjectProperty(None)
    directory = ListProperty([])
    def __init__(self, **kw):
        super(AnswerP3, self).__init__(**kw)
        self.table = self.ids.answers_p3


    def on_pre_leave(self, *args):
        if self.sound:
            self.sound.stop()
            
        return super().on_pre_leave(*args)

    def on_enter(self, *args):
        self.make_list()
        return super().on_enter(*args)

    def make_list(self):
        if platform == "android":
            self.directory = os.listdir("/storage/emulated/0/pb/answers/phase3")
        else:
            self.directory = os.listdir("answers/phase3")



        for i in self.directory:
            answer = i.replace(".wav", "")
            #SKIP DUPLICATES
            if answer in self.a_list:
                continue
             
            self.table.add_widget(Label(
                text=answer,
                font_name="NotoSerif-Regular.ttf",
                color=(0,0,.5,1),
                font_size="35sp",
                halign="center"
    
                )
            )

            self.btn = MDIconButton(
                icon="volume-high",
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

            #THEN ADD TO THE LIST TO AVOID DUPLICATION
            self.a_list.append(answer)


    def listen_answer(self, instance):
        answer = instance.text + ".wav"

        path_to_file = f"answers/phase3/{answer}"
        if platform ==  "android":
            path_to_file = f"/storage/emulated/0/pb/answers/phase3/{answer}"
            play_audio(path_to_file)
        else:
            if self.sound:
                self.sound.stop()

            print(path_to_file)
            self.sound = SoundLoader.load(path_to_file)
            self.sound.play()

########################################################################################  

class AnswerP4(Screen):
    a_list = ListProperty([])
    directory = ListProperty([])
    sound = ObjectProperty(None)
    def __init__(self, **kw):
        super(AnswerP4, self).__init__(**kw)
        self.table = self.ids.answers_p4
    
    def on_pre_leave(self, *args):
        if self.sound:
            self.sound.stop()
            
        return super().on_pre_leave(*args)

    def on_enter(self, *args):
        self.make_list()
        return super().on_enter(*args)

    def make_list(self):
        if platform == "android":
            self.directory = os.listdir("/storage/emulaed/0/pb/answers/phase4")
        else:
            self.directory = os.listdir("answers/phase4")


        for i in self.directory:
            answer = i.replace(".wav", "")
            #SKIP DUPLICATES
            if answer in self.a_list:
                continue
             
            self.table.add_widget(Label(
                text=answer,
                font_name="NotoSerif-Regular.ttf",
                color=(0,0,.5,1),
                font_size="35sp",
                halign="center"
    
                )
            )

            self.btn = MDIconButton(
                icon="volume-high",
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

            #THEN ADD TO THE LIST TO AVOID DUPLICATION
            self.a_list.append(answer)

    def listen_answer(self, instance):
        answer = instance.text + ".wav"

        path_to_file = f"answers/phase4/{answer}"
        if platform ==  "android":
            path_to_file = f"/storage/emulated/0/pb/answers/phase4/{answer}"
            play_audio(path_to_file)
        else:
            if self.sound:
                self.sound.stop()
            print(path_to_file)
            self.sound = SoundLoader.load(path_to_file)
            self.sound.play()


########################################################################################  

class AnswerP5(Screen):
    a_list = ListProperty([])
    directory = ListProperty([])
    sound = ObjectProperty(None)
    def __init__(self, **kw):
        super(AnswerP5, self).__init__(**kw)
        self.table = self.ids.answers_p5


    def on_pre_leave(self, *args):
        if self.sound:
            self.sound.stop()
            
        return super().on_pre_leave(*args)

    def on_enter(self, *args):
        self.make_list()
        return super().on_enter(*args)

    def make_list(self):
        if platform == "android":
            self.directory = os.listdir("/storage/emulated/0/pb/answers/phase5")

        else:
            self.directory = os.listdir("answers/phase5")


        for i in self.directory:
            answer = i.replace(".wav", "")
            #SKIP DUPLICATES
            if answer in self.a_list:
                continue
             
            self.table.add_widget(Label(
                text=answer,
                font_name="NotoSerif-Regular.ttf",
                color=(0,0,.5,1),
                font_size="35sp",
                halign="center"
    
                )
            )

            self.btn = MDIconButton(
                icon="volume-high",
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

            #THEN ADD TO THE LIST TO AVOID DUPLICATION
            self.a_list.append(answer)

    def listen_answer(self, instance):
        answer = instance.text + ".wav"

        path_to_file = f"answers/phase5/{answer}"
        if platform ==  "android":
            path_to_file = f"/storage/emulated/0/pb/answers/phase5/{answer}"
            play_audio(path_to_file)
        else:
            if self.sound:
                self.sound.stop()
            print(path_to_file)
            self.sound = SoundLoader.load(path_to_file)
            self.sound.play()


######################################################################################## 

class AnswerP6(Screen):
    a_list = ListProperty([])
    directory = ListProperty([])
    sound = ObjectProperty(None)
    def __init__(self, **kw):
        super(AnswerP6, self).__init__(**kw)
        self.table = self.ids.answers_p6


    def on_pre_leave(self, *args):
        if self.sound:
            self.sound.stop()
            
        return super().on_pre_leave(*args)

    def on_enter(self, *args):
        self.make_list()
        return super().on_enter(*args)

    def make_list(self):
        if platform == "android":
            self.directory = os.listdir("/storage/emulated/0/pb/answers/phase6")
        else:
            self.directory = os.listdir("answers/phase6")



        for i in self.directory:
            answer = i.replace(".wav", "")
            #SKIP DUPLICATES
            if answer in self.a_list:
                continue
             
            self.table.add_widget(Label(
                text=answer,
                font_name="NotoSerif-Regular.ttf",
                color=(0,0,.5,1),
                font_size="35sp",
                halign="center"
    
                )
            )

            self.btn = MDIconButton(
                icon="volume-high",
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

            #THEN ADD TO THE LIST TO AVOID DUPLICATION
            self.a_list.append(answer)

    def listen_answer(self, instance):
        answer = instance.text + ".wav"

        path_to_file = f"answers/phase6/{answer}"
        if platform ==  "android":
            path_to_file = f"/storage/emulated/0/pb/answers/phase6/{answer}"
        else:
            if self.sound:
                self.sound.stop()
            print(path_to_file)
            self.sound = SoundLoader.load(path_to_file)
            self.sound.play()


######################################################################################## 


######################################################################################## 

class AnswerP7(Screen):
    a_list = ListProperty([])
    card = ObjectProperty(None)
    def __init__(self, **kw):
        super(AnswerP7, self).__init__(**kw)
        self.table = self.ids.answers_p7


    def on_enter(self, *args):
        self.make_list()
        return super().on_enter(*args)

    def make_list(self):

        with open("p7scorecard.json", "r") as read_score:
            dataz = json.load(read_score)

        for i in dataz["scores_by_screen"]:
            print(i)
            name = i["name"]
            corrected = i["correct_num"]
            total = i["total_items"]

            if name in self.a_list:
                continue

            self.card = MDCard()
            self.card.size_hint = (1, 1)
            #self.card.size = (dp(500), dp(500))
            #self.card.pos_hint = {"center_x": .5, "center_y": .5}

            
            self.card.add_widget(MDLabel(text=f"{name} ===>"))
            self.card.add_widget(MDLabel(text=f"Score: {corrected}/{total}"))
            self.card.add_widget(MDSeparator(height = dp(1)))
            self.table.add_widget(self.card)

            self.a_list.append(name)




        




######################################################################################## 