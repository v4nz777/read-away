LIST_0 = [] # empty for indexing purposes only

LIST_1 = ['Be','But','Do','have','he','she','they','was','what','with']

LIST_2 = ['after','again','could','From','Had','Her','His','Of','Then','when']

LIST_3 = ['around','because','been','before','does','Don’t','goes','right','which','write']

LIST_4 = ['better','carry','eight','laugh','light','myself','only','shall','own','together']

LIST_5 = ['area','body','certain','complete','measure','notice','piece','questions','unit','usually']

LIST_6 = ['among','course','equation','language','machine','minutes','produce','quickly','shown','special']

LIST_7 = ['admire','love','move','though','ought','dough','fright','light','sigh','system']

LIST_8 = ['cyclone','rhythm','hydrogen','cyst','admirable','lovable','moveable','thought','bought','although']

LIST_9 = ['fight','thigh','hydrant','crystal','myth','cycle','lymph','sign','resign','benign']

LIST_10 = ['campaign','groan','grown','chord','cord','passed','past','pedal','petal','dessert']

LIST_11 = ['desert','align','course','guest','guessed','mist','missed','accept','except','whose']

LIST_12 = ['who’s','align','foreign','design','patients','patience','aid','add','air','heir']

LIST_13 = ['isle','bored','board','based','bass','site','sight','feet','feat','crews']

LIST_14 = ['cruise','chili','chilly','soar','sore','flour','flower','seem','ream','boy']

LIST_15 = ['buoy','impossible','improbable','immature','imprison','impractical','impatient','immoral','imprint','improper']

LIST_16 = ['impersonal','immortal','advertise','addressed','adapt','admire','adjust','advance','admit','irregular']

LIST_17 = ['irresponsible','irrational','irreversible','irresistible','illogical','illegible','illiterate','centigrade','century','centimeter']

LIST_18 = ['cent','accept','accent','access','accident','enclose','encounter','encourage','envelop','proceed']

LIST_19 = ['produce','progress','project','interrupt','intermission','interpret','international','circulate','circumference','circumstance']

LIST_20 = ['circus','incision','include','inhale','infect','transatlantic','transcend','transfer','translate','calculate']

LIST_21 = ['compute','diagram','divisible','equation','equivalent','evaluate','transcend','evaluate','formula','kilometer']

LIST_22 = ['mean','median','mode','polygon','probability','quotient','range','volume','agriculture','Antarctica']

LIST_23 = ['astronomy','atlas','Australia','civilization','compromise','conservative','economics' ,'empire','environment','erosion']

LIST_24 = ['Europe','government','historical','independence','industrial','interdependence','legislative','minority','neighborhood','patriotism']

LIST_25 = ['peninsula','political','range','relationship','republic','revolution','rural','San Joaquin','taxation']

LIST_26 = ['vineyard','bacteria','decomposes','eclipse','environment','evaporation','fungi','hypothesis','mixtures']

LIST_27 = ['photosynthesis','pollution','protists','solution','temperature','aerobic','athlete','characteristics','competitive']

LIST_28 = ['depressant','endurance','immunizations','infectious','relaxation','stimulant','alphabetical','antonym','apostrophe','capitalization']

LIST_29 = ['classification','contraction','dictation','elaborate','homophone','punctuation','syllables','synonym','although','among']


class SightWords:
    lists = [
        {'title':'List 1','list': LIST_1},
        {'title':'List 2','list': LIST_2},
        {'title':'List 3','list': LIST_3},
        {'title':'List 4','list': LIST_4},
        {'title':'List 5','list': LIST_5},
        {'title':'List 6','list': LIST_6},
        {'title':'List 7','list': LIST_7},
        {'title':'List 8','list': LIST_8},
        {'title':'List 9','list': LIST_9},
        {'title':'List 10','list': LIST_10},
        {'title':'List 11','list': LIST_11},
        {'title':'List 12','list': LIST_12},
        {'title':'List 13','list': LIST_13},
        {'title':'List 14','list': LIST_14},
        {'title':'List 15','list': LIST_15},
        {'title':'List 16','list': LIST_16},
        {'title':'List 17','list': LIST_17},
        {'title':'List 18','list': LIST_18},
        {'title':'List 19','list': LIST_19},
        {'title':'List 20','list': LIST_20},
        {'title':'List 21','list': LIST_21},
        {'title':'List 22','list': LIST_22},
        {'title':'List 23','list': LIST_23},
        {'title':'List 24','list': LIST_24},
        {'title':'List 25','list': LIST_25},
        {'title':'List 26','list': LIST_26},
        {'title':'List 27','list': LIST_27},
        {'title':'List 28','list': LIST_28},
        {'title':'List 29','list': LIST_29}
        ]

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivy.uix.carousel import Carousel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.label import MDLabel
from functools import partial
from kivy.utils import platform
from kivy.core.audio import SoundLoader
import os

#from sound_recorder import rec
from jniusrecord import android_record, play_audio


from kivy.properties import ObjectProperty, BooleanProperty, ListProperty, StringProperty

class SpecialButton(MDRaisedButton):
    list = ListProperty([])
    selected = BooleanProperty(False)

class View(Carousel):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.loop = True

    def on_touch_move(self, touch):
        pass

class SightWordsPage(MDScreen):
    sight_words = ObjectProperty(SightWords())
    current_displayed_list = ListProperty([])
    default_link = ObjectProperty(None)
    selected_link = ObjectProperty(None)
    links = ObjectProperty(None)
    view = ObjectProperty(None)
    word_on_screen = StringProperty('')
    sound_file = StringProperty('')
    sound = ObjectProperty(None)
    read_btn = ObjectProperty(None)
    listen_btn = ObjectProperty(None)
    recorded_words = ListProperty([])
    file_directory = ListProperty([])
    
    def on_enter(self, *args):
        self.links = self.ids.stacked_links
        self.view = self.ids.view
        if platform == 'android':
            self.file_directory = os.listdir('/storage/emulated/0/pb/answers/sight_words')
        else:
            self.file_directory = os.listdir('answers/sight_words')
        
        for index,i in enumerate(self.sight_words.lists):
            self.add_link(i, index)

        return super().on_pre_enter(*args)
          
    def add_link(self,instance, index):
        title = instance['title'].replace('List ', '')
        list_ = instance['list']

        link = SpecialButton(text=title, list=list_, font_style='Body2')

        # Highlight selected, otherwise highlight first item
        if self.selected_link != None:
            if title == self.selected_link.text:
                link.md_bg_color=(1,0.3,0,1)
                link.selected = True
        else:
            if index == 0:
                link.md_bg_color=(1,0.3,0,1)
                link.selected = True
                

        link.bind(on_release=self.display_sight_words)
        self.links.add_widget(link)
        if index == 0:
            self.default_link = link
            self.display_sight_words(self.default_link)
            #self.navigate(self.default_link, initial=True)

    def refresh_links(self):
        self.links.clear_widgets()
        for i in self.sight_words.lists:
            self.add_link(i)
    
    def switch_selected(self, instance, link):
        if self.selected_link:
            self.selected_link.md_bg_color = self.selected_link.theme_cls.primary_color
            self.selected_link.selected = False

            if link:
                self.selected_link = link
                link.selected = True
                link.md_bg_color = (1,0.3,0,1)
                self.navigate(link, initial=True)
        else:
            self.default_link.md_bg_color = self.default_link.theme_cls.primary_color
            self.default_link.selected = False

            if link:
                self.selected_link = link
                link.selected = True
                link.md_bg_color = (1,0.3,0,1)
                self.navigate(link, initial=True)

    def display_sight_words(self,instance):
        if instance.list == self.current_displayed_list:
            pass
        else:
            self.current_displayed_list = instance.list

            # switch links and change current displayed list
            
            self.view.clear_widgets()
            for li in instance.list:
                # Creating base layer
                self.base = MDGridLayout(rows=2)

                # Add the base to carousel
                self.view.add_widget(self.base)

                # Add sight word(with prev and next btns) -> base layer
                prev_main_next_section = MDGridLayout(cols=3)
                self.base.add_widget(prev_main_next_section)

                sight_word = MDLabel(text=li,theme_text_color = 'Custom',text_color=(1,0.3,0,1),font_style='H1',halign='center',valign='center',font_name='PTSans-Bold.ttf')
                prev_btn = MDIconButton(text='prev', icon='arrow-left-drop-circle')
                next_btn = MDIconButton(text='next', icon='arrow-right-drop-circle')
                prev_btn.bind(on_release=partial(self.navigate,initial=False))
                next_btn.bind(on_release=partial(self.navigate,initial=False))

                prev_main_next_section.add_widget(prev_btn)
                prev_main_next_section.add_widget(sight_word)
                prev_main_next_section.add_widget(next_btn)
                
                # Create function elements and add -> base layer
                self.elements = MDBoxLayout(spacing=15)
                self.base.add_widget(self.elements)

                read_ = MDAnchorLayout(anchor_x='right', anchor_y='center')
                listen_ = MDAnchorLayout(anchor_x='left', anchor_y='center')
                self.elements.add_widget(read_)
                self.elements.add_widget(listen_)

                self.read_btn = MDRaisedButton(text='Read', font_style='H3', md_bg_color=(1,0.3,0,1))
                self.listen_btn = MDRaisedButton(text='Listen', font_style='H3', md_bg_color_disabled=(0.5,0.5,0.5), disabled=True)

                file_recorded = f'{li}.m4a' in sorted(self.file_directory)
                subject_added = li in self.recorded_words
                if file_recorded or subject_added:
                    self.listen_btn.disabled = False

                self.read_btn.bind(on_release=self.record)
                self.listen_btn.bind(on_release=self.listen)

                read_.add_widget(self.read_btn)
                listen_.add_widget(self.listen_btn)

        self.switch_selected('placeholder', instance)
        self.selected_link = instance
        
    def navigate(self,instance,initial):
        if initial:
            self.word_on_screen = self.view.current_slide.children[1].children[1].text
            print(self.word_on_screen)
        else:
            if instance.text == 'next':
                self.view.load_next()
                self.word_on_screen = self.view.next_slide.children[1].children[1].text
                print(self.word_on_screen)

            elif instance.text == 'prev':
                self.view.load_previous()
                self.word_on_screen = self.view.previous_slide.children[1].children[1].text
                print(self.word_on_screen)
    

    def record(self, instance):
        self.sound_file = self.word_on_screen + '.m4a'

        if platform == 'android':
            android_record(f'/storage/emulated/0/pb/answers/sight_words/{self.sound_file}')
        else:
            rec(f'answers/sight_words/{self.sound_file}')

        if self.word_on_screen not in self.recorded_words:
            self.recorded_words.append(self.word_on_screen)

            #should be (self.listen_btn.disabled = False)
            #but unexpected bug will affect previous item
            self.view.current_slide.children[0].children[0].children[0].disabled = False
            
            print(f'{self.word_on_screen} added to the list')
        else:
            print(f'{self.word_on_screen} renewed to the list')
        
        self.listen('instance_placeholder')
        
    
    def listen(self,instance):
        path_to_file = f'answers/sight_words/{self.word_on_screen}.m4a'

        if platform == 'android':
            path_to_file = f'/storage/emulated/0/pb/answers/sight_words/{self.word_on_screen}.m4a'
            play_audio(path_to_file)
        else:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(path_to_file)
            self.sound.play()
