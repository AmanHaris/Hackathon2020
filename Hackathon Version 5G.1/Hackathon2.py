import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.uix.button import ButtonBehavior
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.config import Config

Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '650')

class MyGrid(Widget):

	name = ObjectProperty(None)
	email = ObjectProperty(None)


	def btn(self):
		print("Name:", self.name.text, "Email:", self.email.text)
		self.name.text = ""
		self.email.text = ""

class MyApp(App):
	def build(self):
		return MyGrid()

if __name__ == "__main__":
    MyApp().run()