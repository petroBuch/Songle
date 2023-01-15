import kivy
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.uix.image import Image
Window.size = (360, 700)


class Songle(MDApp):
	def build(self):
		screen_manager = ScreenManager()
		screen_manager.add_widget(Builder.load_file("Login.kv"))
		screen_manager.add_widget(Builder.load_file("Register.kv"))
		screen_manager.add_widget(Builder.load_file("Home.kv"))
		screen_manager.current = "home"
		return screen_manager
			
class ShadowCard(FakeRectangularElevationBehavior, MDBoxLayout):
	pass
class ShadowImage(FakeRectangularElevationBehavior, Image):
	pass

if __name__ == '__main__':
	Songle().run()