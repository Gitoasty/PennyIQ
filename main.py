import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.uix.button import Button
import sqlite3
from kivy.core.audio import SoundLoader
kivy.require('2.1.0')

try:
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

except:
    print('DB exists')

class Sounds():


    def music(self):
        sound = SoundLoader.load('bongos.mp3')
        print(sound.state)
        if sound and sound.state == "stop":
            sound.volume = 0.5
            sound.play()
            sound.loop = True
            sound.state = "play"

    def press(self):
        sound = SoundLoader.load('press.mp3')
        if sound:
            sound.play()

    def release(self):
        sound = SoundLoader.load('release.mp3')
        if sound:
            sound.play()

class MainWindow(Screen):

    def press(self):
        Sounds.press(self)

    def release(self):
        Sounds.release(self)

class main_menu(Screen):

    def music(self):
        Sounds.music(self)

    def press(self):
        Sounds.press(self)

    def release(self):
        Sounds.release(self)

class textbook1(Screen):

    def music(self):
        Sounds.music(self)

    def press(self):
        Sounds.press(self)

    def release(self):
        Sounds.release(self)

class textbook2(Screen):

    def music(self):
        Sounds.music(self)

    def press(self):
        Sounds.press(self)

    def release(self):
        Sounds.release(self)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("penny.kv")

class Penny(App):
    def build(self):
        self.title = "PennyIQ"
        return kv


if __name__ == '__main__':
    Penny().run()