import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
from kivy.uix.label import Label
from kivy.uix.button import Button
import speech_recognition as sr
import pyttsx3
import time
import random
import  threading
from kivy.uix.relativelayout import RelativeLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config
class MyApp(App):
    def build(self):

        return Button(text="tst")



if __name__ == "__main__":
    MyApp().run()