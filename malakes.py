from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.widget import Widget
import random

KV = '''
Screen:

    MDBoxLayout:
        orientation: 'vertical'
        spacing: "20dp"
        padding: "20dp"

        MDLabel:
            text: "Welcome to the Malakas Detector App!"
            halign: "center"
            font_style: "H5"
            size_hint_y: None
            height: self.texture_size[1]

        MDTextField:
            id: name_input
            hint_text: "Enter your name"
            size_hint: None, None
            size: "300dp", "40dp"
            font_size: "16sp"

        MDBoxLayout:
            spacing: "10dp"

            MDRaisedButton:
                text: "Check"
                font_size: "20sp"
                on_release: app.check_name()
                elevation_normal: 6
                md_bg_color: app.theme_cls.primary_color

            MDRaisedButton:
                text: "Restart"
                font_size: "20sp"
                on_release: app.restart_app()
                elevation_normal: 6
                md_bg_color: app.theme_cls.accent_color

            MDRaisedButton:
                text: "Close App"
                font_size: "20sp"
                on_release: app.close_app()
                elevation_normal: 6
                md_bg_color: app.theme_cls.error_color

        MDLabel:
            id: output_label
            text: ""
            halign: "center"
            font_size: "20sp"
            size_hint_y: None
            height: self.texture_size[1]
'''

class MalakasDetectorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_name(self):
        name_input = self.root.ids.name_input
        output_label = self.root.ids.output_label
        name = name_input.text.lower()

        predefined_names = ["marios", "nikos", "thslis", "thalis", "talis", "muffin", "trito pedi", "3 pedi", "3pedi", "3 pedi", "bill", "tasos"]
        additional_names = ["kostas", "xalkias", "tasios"]

        if name in predefined_names:
            # Handle predefined names
            if name == "marios":
                output_label.text = "You are Marios, the killer with a spoon. You are definitely malakas!"
            elif name == "nikos":
                output_label.text = "You are Nikos, the very short man with a small pipi. Sorry, you are not malakas."
            elif name in ["thslis", "thalis", "talis"]:
                output_label.text = "You are Thalis, you have a big armonio, and you are an anime fan!"
            elif name == "muffin":
                output_label.text = "You are Muffin, the idiot and annoying kid."
            elif name in ["trito pedi", "3 pedi", "3pedi", "3 pedi"]:
                output_label.text = "You are Trito Pedi, the very tall and handy man."
            elif name == "bill":
                output_label.text = "You are Bill, a very handy man with a large pipi."
            elif name == "tasos":
                output_label.text = "You are Tasos. You shouldn't have been an English teacher, you should have been a math teacher." 
        elif name in additional_names:
            # Handle additional names
            if name == "kostas":
                output_label.text = "You are Kostas. You are a criminal."
            elif name == "xalkias":
                output_label.text = "You are Xalkias. You are acoustic."
            elif name == "tasios":
                output_label.text = "You are Tasios. You are eating white chocolate."
        else:
            # If name is not on the list, randomly pick one of the options
            options = ["You are gay.", "You are a lesbian.", "You are an idiot.", "You are not hot.", "You are Batman.", "You are Spiderman."]
            random_option = random.choice(options)
            output_label.text = random_option

    def restart_app(self):
        name_input = self.root.ids.name_input
        output_label = self.root.ids.output_label
        name_input.text = ""
        output_label.text = ""

    def close_app(self):
        self.stop()

if __name__ == '__main__':
    MalakasDetectorApp().run()

