# C:\users/salop/documents/github/songle
import os

import ffpyplayer
from ffpyplayer.player import MediaPlayer

import random

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
from kivy.core.audio import SoundLoader
from kivymd.uix.slider import MDSlider
from kivy.clock import Clock

Window.size = (360, 700)


class Songle(MDApp):
	music_folder = "Music/"
	audio_list = os.listdir(music_folder)
	song_index = random.randint(0, len(audio_list)-1)
	player = SoundLoader.load(f"Music/{audio_list[song_index]}")


	def build(self):
		screen_manager = ScreenManager()
		screen_manager.add_widget(Builder.load_file("Login.kv"))
		screen_manager.add_widget(Builder.load_file("Register.kv"))
		screen_manager.add_widget(Builder.load_file("Home.kv"))
		screen_manager.add_widget(Builder.load_file("Test.kv"))
		screen_manager.add_widget(Builder.load_file("Player.kv"))
		screen_manager.current = "player"

		self.time = 0
		self.updater = None
		self.song_queue = []
		self.previous_song = []	
		self.curr_song = self.audio_list[self.song_index]	


		return screen_manager

	def on_start(self):
		for i in self.audio_list:
			if self.audio_list[self.song_index]==i:
				continue
			else:
				self.song_queue.append(i)

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

			self.root.screens[2].ids.plgl.add_widget(PLFloatLayout)

		Clock.schedule_interval(self.update_next, 2)

	def update_next(self, dt):
		if round(self.player.length)%60 == round(self.player.get_pos())%60:
			Clock.schedule_once(self.play_next, 1)

	def start_play(self, *args):
		if self.player.state == "play":
			self.root.screens[4].ids.player_butt.icon = "pause"
			self.time = self.player.get_pos()
			self.player.stop()
			self.root.screens[4].ids.player_butt.icon = "play"
			self.root.screens[2].ids.play_butt.icon = "play"

		elif self.player.state == "stop":
			self.root.screens[4].ids.player_butt.icon = "play"
			self.player.seek(self.time)
			self.player.play()
			self.root.screens[4].ids.player_butt.icon = "pause"
			self.root.screens[2].ids.play_butt.icon = "pause"
			self.update_all()
			if self.updater is None:
				self.updater = Clock.schedule_interval(self.update_slider_and_time, 0.5)

	def update_all(self):
		self.root.screens[4].ids.song_time_slider.max = round(self.player.length)
		self.root.screens[2].ids.pg_bar.max = round(self.player.length)
		self.root.screens[2].ids.song_name.text = self.curr_song[self.curr_song.find("-")+1:-4]
		self.root.screens[2].ids.song_artist.text = self.curr_song[:self.curr_song.find("-")-1]
		self.root.screens[4].ids.song_name.text = self.curr_song[self.curr_song.find("-")+1:-4]
		self.root.screens[4].ids.song_artist.text = self.curr_song[:self.curr_song.find("-")-1]
		self.root.screens[4].ids.song_image.source = f"Items/{self.curr_song[:-4]}.png"
		end_min = round(self.player.length)//60
		end_sec = round(self.player.length)%60
		self.root.screens[4].ids.end_time.text = str(end_min)+":"+"0"*(2-len(str(end_sec))) + str(end_sec)

	def update_slider_and_time(self, dt):
		self.root.screens[4].ids.song_time_slider.value = self.player.get_pos()
		self.root.screens[2].ids.pg_bar.value = self.player.get_pos() 
		cur_min = round(self.player.get_pos())//60
		cur_sec = round(self.player.get_pos())%60
		self.root.screens[4].ids.curr_time.text = str(cur_min)+":"+"0"*(2-len(str(cur_sec)))+str(cur_sec)

		if self.player.state == "play":
			self.root.screens[4].ids.player_butt.icon = "pause"
			self.root.screens[2].ids.play_butt.icon = "pause"

		else:
			self.root.screens[4].ids.player_butt.icon = "play"
			self.root.screens[2].ids.play_butt.icon = "play"


	def play_next(self, *args):
		print(self.player)
		self.previous_song.append(self.curr_song)
		self.player.stop()
		Songle.player = SoundLoader.load(f"Music/{self.song_queue[0]}")
		self.curr_song = self.song_queue[0]
		self.start_play()
		self.song_queue.remove(self.song_queue[0])
		print(self.player)

	def play_previous(self):
		self.player.stop()
		self.player = SoundLoader.load(f"Music/{self.previous_song[-1]}")
		self.curr_song = self.previous_song[-1]
		self.start_play()
		self.previous_song.remove(self.previous_song[-1])












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

class SongSlider(MDSlider):

	def on_touch_up(self, touch):

		if touch.grab_current == self:
			ret_val = super(SongSlider, self).on_touch_up(touch)

			Songle.player.seek(self.value)
			print(1, Songle.player)

			return ret_val
		else:
			return super(SongSlider, self).on_touch_up(touch)





if __name__ == '__main__':
	Songle().run()