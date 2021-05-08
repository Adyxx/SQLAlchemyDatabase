from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from kivymd.uix.button import MDFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem, ImageLeftWidget, IconRightWidget
from kivymd.uix.menu import MDDropdownMenu

from modules.database import Database, Animal, Type, Photo


class TypeContent(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)


class TypeDialog(MDDialog):
    def __init__(self, *args, **kwargs):
       
        super(TypeDialog, self).__init__(
            type="custom",
        
            content_cls=TypeContent(),
            title='New animal type',
            size_hint=(.8, 1),
            buttons=[
                MDFlatButton(text='Save', on_release=self.save_dialog),
                MDFlatButton(text='Cancel', on_release=self.cancel_dialog)
            ]
        )

    def save_dialog(self, *args):

        typee = Type()
        typee.full_name = self.content_cls.ids.type_full_name.text
        app.animals.database.create_type(typee)
        self.dismiss()

    def cancel_dialog(self, *args):
        self.dismiss()

class AnimalContent(BoxLayout):
    def __init__(self, id, *args, **kwargs):
        super().__init__(**kwargs)
        if id:
            animal = vars(app.animals.database.read_animal_by_id(id))
        else:
            animal = {"id":"", "name":"", "type": "Type"}

        self.ids.animal_name.text = animal['name']

        types = app.animals.database.read_types()

        menu_items = [{"viewclass": "OneLineListItem", "text": f"{typee.full_name}", "on_release": lambda x=f"{typee.full_name}": self.set_item(x)} for typee in types]

        self.menu_types = MDDropdownMenu(
            caller=self.ids.type_item,
            items=menu_items,
            position="center",
            width_mult=5,
        )

        self.ids.type_item.set_item(animal['type'])
        self.ids.type_item.text = animal['type']

    def set_item(self, text_item):
       
        self.ids.type_item.set_item(text_item)
        self.ids.type_item.text = text_item
     
        self.menu_types.dismiss()


class AnimalDialog(MDDialog):
    def __init__(self, id, *args, **kwargs):
        super(AnimalDialog, self).__init__(
            type="custom",
            content_cls=AnimalContent(id=id),
            title='Details',
            text='enter text here...',
            size_hint=(.8, 1),
            buttons=[
                MDFlatButton(text='Save', on_release=self.save_dialog),
                MDFlatButton(text='Cancel', on_release=self.cancel_dialog)
            ]
        )
        self.id = id

    def save_dialog(self, *args):
        
        animal = {}
        animal['name'] = self.content_cls.ids.animal_name.text
        
        animal['typee'] = self.content_cls.ids.type_item.text # ################

        if self.id:
            animal["id"] = self.id
            app.animals.update(animal)
        else:
            app.animals.create(animal)

        self.dismiss()


    def cancel_dialog(self, *args):
        self.dismiss()


class MyItem(TwoLineAvatarIconListItem):
    def __init__(self, item, *args, **kwargs):
        super(MyItem, self).__init__()

        self.id = item['id']
        self.text = item['name']

        self.secondary_text = item['typee']

        self._no_ripple_effect = True

        self.image = ImageLeftWidget()

        self.image.source = f"images/{item['typee']}.png"
        self.add_widget(self.image)

        self.icon = IconRightWidget(icon="delete", on_release=self.on_delete)
        self.add_widget(self.icon)

    def on_press(self):

        self.dialog = AnimalDialog(id=self.id)
        self.dialog.open()
    
    def on_delete(self, *args):

        yes_button = MDFlatButton(text='Yes', on_release=self.yes_button_release)
        no_button = MDFlatButton(text='No', on_release=self.no_button_release)
        self.dialog_confirm = MDDialog(type="confirmation", title='Delete record', text="Do you really want to delete this?", buttons=[yes_button, no_button])
        self.dialog_confirm.open()

    def yes_button_release(self, *args):
       
        app.animals.delete(self.id)
        self.dialog_confirm.dismiss()

    def no_button_release(self, *args):
        self.dialog_confirm.dismiss()

class Animals(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Animals, self).__init__(orientation="vertical")
        global app
        app = App.get_running_app()
        scrollview = ScrollView()
        self.list = MDList()
        self.database = Database(dbtype='sqlite', dbname='animals.db')
        self.rewrite_list()
        scrollview.add_widget(self.list)
        self.add_widget(scrollview)
        button_box = BoxLayout(orientation='horizontal', size_hint_y=0.1)

        #button 1
        btn_animal = MDFlatButton()
        btn_animal.text = "Add new animal"
        btn_animal.font_style = "Button"
        btn_animal.on_release = self.on_create_animal

        # button 2 
        btn_type = MDFlatButton()
        btn_type.text = "Add new animal type"
        btn_type.font_style = "Button"
        btn_type.on_release  = self.on_create_type

        button_box.add_widget(btn_animal)
        button_box.add_widget(btn_type)
        self.add_widget(button_box)

    def rewrite_list(self):
        self.list.clear_widgets()
       
        animals = self.database.read_all()
       
        for animal in animals:
            print(vars(animal))
            self.list.add_widget(MyItem(item=vars(animal)))

    def on_create_animal(self, *args):

        self.dialog = AnimalDialog(id=None)
        self.dialog.open()

    def on_create_type(self, *args):

        self.dialog = TypeDialog()
        self.dialog.open()

    def create(self, animal):

        cr_animal = Animal()
        cr_animal.name = animal['name']
        cr_animal.typee = animal['typee']
       # cr_animal.info = animal['info']
       # cr_animal.photoo = animal['photoo']
        self.database.create_animal(cr_animal)
        self.rewrite_list()

    def update(self, animal):

        up_animal = self.database.read_animal_by_id(animal['id'])
        up_animal.name = animal['name']
        up_animal.typee = animal['typee']
       # up_animal.info = animal['info']
       # up_animal.photoo = animal['photoo']
        self.database.update()
        self.rewrite_list()

    def delete(self, id):

        self.database.delete_animal(id)
        self.rewrite_list()