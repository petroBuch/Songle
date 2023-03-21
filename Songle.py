# C:\users/salop/documents/github/songle
import kivy
from kivy.properties import ObjectProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDIconButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.anchorlayout import MDAnchorLayout
Window.size = (360, 700)


class Songle(MDApp):
	def build(self):
		screen_manager = ScreenManager()
		screen_manager.add_widget(Builder.load_file("Login.kv"))
		screen_manager.add_widget(Builder.load_file("Register.kv"))
		screen_manager.add_widget(Builder.load_file("Home.kv"))
		screen_manager.add_widget(Builder.load_file("Test.kv"))
		screen_manager.add_widget(Builder.load_file("Player.kv"))
		screen_manager.current = "home"
		return screen_manager
	def on_start(self):
		for i in range(7):
			self.root.screens[2].ids.songgl.add_widget(
				SongImage()
			)
			self.root.screens[2].ids.songgl.add_widget(
				SongLabel()
			)

		for i in range(5):
			self.root.screens[2].ids.shadow_grid.add_widget(
				ShadowCard()
			)

		data = {
			"1": "Рекомендации",
			"2": "Новинки",
			"3": "Ремиксы",
			"4": "Relax & Chill",
			"5": "Новые имена",
			"6": "Исполнитель",
		}
		for num in data.keys():
			PLFloatLayout = MDFloatLayout(size_hint = (None, None), size = (150, 150))
			PLFloatLayout.add_widget(Image(source=f"Items/plimage{num}.png", pos_hint={"x": 0, "y": 0}))
			PLFloatLayout.add_widget(
				MDLabel(
					text = data[num],
					font_size = "16sp",
					size = (130, 20),
					pos_hint = {"x": 0.015, "center_y": 0.5},
					theme_text_color = "Custom",
					text_color = get_color_from_hex("#E4E4E4"),
					valign = "middle",
					halign = "center",
				)
			)
			PLFloatLayout.add_widget(
				MDLabel(
					text = "30 песен",
					font_size = "12sp",
					size_hint = (0.5, 0.08),
					pos_hint = {"x": 0.3, "y": 0.0333},
					theme_text_color = "Custom",
					text_color = get_color_from_hex("#E4E4E4"),
				)
			)
			PLFloatLayout.add_widget(
				MDIconButton(
					icon = "heart-outline",
					size_hint = (0.15, 0.15),
					pos_hint = {"x": 0.7, "y": 0.833},
					theme_icon_color = "Custom",
					icon_color = get_color_from_hex("#E4E4E4")
				)
			)
			PLFloatLayout.add_widget(
				MDIconButton(
					icon = "dots-vertical",
					size_hint = (0.1133, 0.15),
					pos_hint = {"x": 0.85, "y": 0.833},
					theme_icon_color = "Custom",
					icon_color = get_color_from_hex("#E4E4E4")
				)
			)

	# 		# self.root.screens[2].ids.plimage.source = f"Items/plimage{num}.png"
	# 		# # self.root.screens[2].ids.pltext.text = data[num]
			self.root.screens[2].ids.plgl.add_widget(PLFloatLayout)
	# 	self.root.screens[2].ids.mainfl.add_widget(
	# 		MDExpansionPanel(
	# 			content=EPBox(),
	# 			panel_cls=MDExpansionPanelOneLine(
	# 				text="По артисту",
	# 				theme_text_color="Custom",
	# 				text_color=get_color_from_hex("#E4E4E4"),
	# 				bg_color=get_color_from_hex("#4E3064"),
	# 				radius=10,
	# 				size_hint=(None, None),
	# 				size=(340, 40)
	# 			),
	# 			pos_hint = {"x": 0.0277, "y": 0.57},
	# 			size_hint=(None, None),
	# 			size=(340, 40)
	# 		)
	# 	)


class ShadowBox(CommonElevationBehavior, MDBoxLayout):
	pass		
class ShadowCard(CommonElevationBehavior, MDBoxLayout):
	pass
class ShadowImage(CommonElevationBehavior, Image):
	pass
class EPBox(MDBoxLayout):
	pass
class SongImage(Image):
	pass
class SongLabel(MDLabel):
	pass

if __name__ == '__main__':
	Songle().run()