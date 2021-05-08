from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from modules.animals import Animals

class DatabaseScreen(Screen):
    pass

class AnimalDatabase(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        builder = Builder.load_file('main.kv')
        self.animals = Animals()
        builder.ids.navigation.ids.tab_manager.screens[0].add_widget(self.animals)
        return builder

AnimalDatabase().run()