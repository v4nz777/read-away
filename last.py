from kivymd.uix.screen import MDScreen
from kivymd.uix.button import  MDFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty

class LastScreen(MDScreen):

    dialog = ObjectProperty(None)

    def on_enter(self, *args):
        self.show_alert_dialog()
        return super().on_enter(*args)

    def show_alert_dialog(self):
        if not self.dialog:
            dialog_text = 'You Have Completed Read Away!'
            dialog_title = 'CONGRATULATIONS!'

            self.dialog = MDDialog(
                title = dialog_title,
                text=dialog_text,
            )
        self.dialog.open()
