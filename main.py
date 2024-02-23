import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
import sqlite3
from kivy.core.audio import SoundLoader
kivy.require('2.1.0')

try:
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

except:
    print('DB exists')

class MainWindow(Screen):

    def press(self):
        sound = SoundLoader.load('tehe.mp3')
        if sound:
            sound.play()

    def release(self):
        sound = SoundLoader.load('senpai.mp3')
        if sound:
            sound.play()

class main_menu(Screen):

    def music(self):
        sound = SoundLoader.load('bongos.mp3')
        if sound:
            sound.play()

    def press(self):
        sound = SoundLoader.load('tehe.mp3')
        if sound:
            sound.play()

    def release(self):
        sound = SoundLoader.load('senpai.mp3')
        if sound:
            sound.play()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("penny.kv")

class Penny(App):
    def build(self):
        self.title = "PennyIQ"
        return kv


if __name__ == '__main__':
    Penny().run()