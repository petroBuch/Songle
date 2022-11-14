import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (360, 700)


class Songle(MDApp):
	def build(self): 
		global screen_manager
		screen_manager = ScreenManager()
		screen_manager.add_widget(Builder.load_file("Login.kv"))
		screen_manager.add_widget(Builder.load_file("Register.kv"))
		screen_manager.add_widget(Builder.load_file("Home.kv"))
		screen_manager.current = "login"
		return screen_manager
			
	def press_stay(self, *args):
		self.icon.icon = "steam"



if __name__ == '__main__':
	Songle().run()