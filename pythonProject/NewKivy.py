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

Window.fullscreen = "auto"

Builder.load_string("""#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import sm kivy.uix.screenmanager


<MainWindow>:
    name : "main"
    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'welcome.gif'
        anim_loop : 1
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Label:
        font_size: 65
        font_name : "BuxtonSketch"
        bold : True
        color:(0,0,1,1)
        pos_hint: {"center_x":.65, "center_y":.6}
        text: "WHAT DO YOU WANT TO ATTEMPT"


    SmoothButton:
        id : btn_random
        font_size: 50
        text:"RANDOM"
        bold : True
        font_name : "BuxtonSketch"
        back_color: (0,.70,.70,1) if btn_random.state == "normal" else (.2,.52,1,1)
        size_hint: (.25,.15) if btn_random.state == "normal" else (.30,.20)
        pos_hint: {"center_x":.45, "center_y":.4}

        on_press:
            root.onclick_random()


    SmoothButton:
        id : btn_alphabet
        font_size: 50
        text:"ALPHABET"
        font_name : "BuxtonSketch"
        bold : True
        back_color: (0,.70,.70,1) if btn_alphabet.state == "normal" else (.2,.52,1,1)
        size_hint: (.25,.15) if btn_alphabet.state == "normal" else (.30,.20)
        pos_hint: {"center_x":.85, "center_y":.4}
        on_release:
            root.onclick_seq()

    SmoothButton:
        id : btn_close
        font_size: 50
        text:"Close"
        bold : True
        font_name : "BuxtonSketch"
        back_color: (.70,.23,0,1) if btn_close.state == "normal" else (.6,.2,0,1)
        size_hint: (.15,.1) if btn_close.state == "normal" else (.20,.15)
        pos_hint: {"center_x":.1, "center_y":.1}

        on_press:
            root.manager.current="end"



<CorrectWindow>:
    name : "correct"
    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Button :
        background_normal : 'homeiconBlue.png'
        background_down : 'homeiconRed.png'
        size_hint : .15,.15
        pos_hint: {"center_x":.06, "center_y":.93}
        keep_ratio: False
        allow_stretch: True
        on_press:
            root.manager.current="main"

    Image :
        source : 'correct.gif'
        anim_delay : .1
        size : 300,400
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Label :
        id : label1
        text : "CORRECT WELL DONE"
        bold : True
        color:(0,0.9,0,1)
        pos_hint: {"center_x":.65, "center_y":.6}
        font_size: 100
        font_name : "BuxtonSketch"

    SmoothButton:
        id : btn_next
        font_size: 40
        text:"NEXT"
        font_name : "BuxtonSketch"
        bold : True       
        back_color: (0,0.9,0,1) if btn_next.state == "normal" else (.2,.8,0.2,1)
        size_hint: (.15,.1) if btn_next.state == "normal" else (.20,.15)
        pos_hint: {"center_x":.75, "center_y":.4}
        on_release:
            root.next()

<TryAgainWindow>:
    name : "wrong"
    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True
    Button :
        background_normal : 'homeiconBlue.png'
        background_down : 'homeiconRed.png'
        size_hint : .15,.15
        pos_hint: {"center_x":.06, "center_y":.93}
        keep_ratio: False
        allow_stretch: True
        on_press:
            root.manager.current="main"
    Image :
        source : 'sorry.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Label :
        id : label1
        text : "OHH!! PLEASE TRY AGAIN"
        bold : True
        color:(0.9,0,0,1)
        pos_hint: {"center_x":.65, "center_y":.6}
        font_size: 100
        font_name : "BuxtonSketch"

    SmoothButton:
        id : btn_next
        font_size: 40
        text:"NEXT"
        font_name : "BuxtonSketch"
        bold : True
        back_color: (0,0.9,0,1) if btn_next.state == "normal" else (.2,.8,0.2,1)
        size_hint: (.15,.1) if btn_next.state == "normal" else (.20,.15)
        pos_hint: {"center_x":.75, "center_y":.4}
        on_release:
            root.next()

    SmoothButton:
        id : btn_tryagain 
        font_size: 40
        text:"TRY AGAIN"
        font_name : "BuxtonSketch"
        bold : True
        back_color: (0.9,0,0,1) if btn_tryagain.state == "normal" else (.8,.2,0.2,1)
        size_hint: (.15,.1) if btn_tryagain.state == "normal" else (.20,.15)
        pos_hint: {"center_x":.55, "center_y":.4}
        on_release:
            root.tryagain()

    Image :
        size : 5,5
        background_normal: 'Chemistry2.jpg'
        background_down: 'bg.png'
        pos_hint: {"center_x":.1, "center_y":.9}
        keep_ratio: False
        allow_stretch: True


<A>:
    name : "1"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'A.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<B>:
    name : "2"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'B.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<C>:
    name : "3"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'C.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<D>:
    name : "4"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'D.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<E>:
    name : "5"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'E.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<F>:
    name : "6"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'F.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<G>:
    name : "7"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'G.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<H>:
    name : "8"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'H.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"
<I>:
    name : "9"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'I.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<J>:
    name : "10"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'J.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<K>:
    name : "11"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'K.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<L>:
    name : "12"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'L.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<M>:
    name : "13"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'M.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<N>:
    name : "14"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'N.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<O>:
    name : "15"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'O.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<P>:
    name : "16"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'P.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<Q>:
    name : "17"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'Q.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<R>:
    name : "18"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'R.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<S>:
    name : "19"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'S.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<T>:
    name : "20"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'T.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<U>:
    name : "21"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'U.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<V>:
    name : "22"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'V.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<W>:
    name : "23"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'W.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<X>:
    name : "24"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'X.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<Y>:
    name : "25"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'Y.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"

<Z>:
    name : "26"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'try.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Image :
        source : 'Z.png'
        size_hint : .4,.4
        pos_hint: {"center_x":.65, "center_y":.4}
        keep_ratio: False
        allow_stretch: True



    Label :
        text : "TRY SPEAKING"
        bold : True
        color:(.7,.12,.12,1)
        pos_hint: {"center_x":.65, "center_y":.7}
        font_size: 100
        font_name : "BuxtonSketch"


<Finish>:
    name : "finish"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'thank_you.gif'
        size : 380,480
        pos_hint: {"center_x":.15, "center_y":.55}
        keep_ratio: False

    Label :
        text : "CONGRATULATIONS"
        bold : True
        color:(0,0,1,1)
        pos_hint: {"center_x":.65, "center_y":.6}
        font_size: 100
        font_name : "BuxtonSketch"
    Button :
        background_normal : 'homeiconBlue.png'
        background_down : 'homeiconRed.png'
        size_hint : .15,.15
        pos_hint: {"center_x":.06, "center_y":.93}
        keep_ratio: False
        allow_stretch: True
        on_press:
            root.manager.current="main"
    Label :
        text : "YOU HAVE COMPLETED ALL ALPHABETS"
        bold : True
        color:(0,0,1,1)
        pos_hint: {"center_x":.65, "center_y":.5}
        font_size: 60
        font_name : "BuxtonSketch"

<End>:
    name : "end"

    Image :
        source : 'bg.jpeg'
        size : 1600,1000
        pos : 0,0
        keep_ratio: False
        allow_stretch: True

    Image :
        source : 'thank_you.gif'
        size_hint: .75,.75
        pos_hint: {"center_x":.5, "center_y":.5}
        keep_ratio: False

    

<SmoothButton@Button>:
    background_color: (0,0,0,0)
    background_normal: ''
    back_color: (.2,.2,1,.8)
    border_radius: [40]
    canvas.before:
        Color:
            rgba: self.back_color
        RoundedRectangle:
            size : self.size
            pos: self.pos
            radius: self.border_radius



""")

#Config.set('graphics', 'resizable', True)

alphabets = {
    1: "A",
    2: "B",
    3: "D",
    4: "D",
    5: "K",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z",
}
pronun = {
    "A": ["A"],
    "B": ["B"],
    "C": ["C"],
    "D": ["D"],
    "E": ["E"],
    "F": ["F"],
    "G": ["G", "Ji"],
    "H": ["H"],
    "I": ["I"],
    "J": ["J", "Jay"],
    "K": ["K", "Ke"],
    "L": ["L"],
    "M": ["M"],
    "N": ["N"],
    "O": ["O"],
    "P": ["P"],
    "Q": ["Q"],
    "R": ["R", "Are"],
    "S": ["S"],
    "T": ["T"],
    "U": ["U", "You"],
    "V": ["V"],
    "W": ["W"],
    "X": ["X", "Eggs", "Egg"],
    "Y": ["Y", "Why"],
    "Z": ["Z"],
}

def st(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(command)
    engine.runAndWait()


def recognizing(alphabet):
    r = sr.Recognizer()
    r.energy_threshold = 5000
    with sr.Microphone() as source:
        ask_1 = '''Try speaking {} '''.format(alphabet)

        def speak():
            time.sleep(.55)
            st(ask_1)

        def listen():
            global audio
            audio = r.listen(source)

        t2 = threading.Thread(target=listen)
        t3 = threading.Thread(target=speak)
        t3.start()
        t2.start()
        t3.join()
        t2.join()
        st("Recognizing")
        try:
            text = r.recognize_google(audio).strip().capitalize()
            if text == pronun[alphabet][0] or text == pronun[alphabet][1] or text == pronun[alphabet][2] :
                sm.current="correct"

            else:
                #write try again
                sm.current="wrong"

        except:
            sm.current = "wrong"
# write



class MainWindow(Screen):
    def onclick_random(self):
        global p
        p = "r"
        a = str((random.randint(1,26)))
        global random_slide
        random_slide= a
        sm.current=random_slide

    def onclick_seq(self):
        global p
        p = "s"
        global m
        m=1
        sm.current=str(m)

    pass






class A(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("A")
    pass

class B(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("B")
    pass

class C(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("C")
    pass

class D(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("D")
    pass

class E(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("E")
    pass

class F(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("F")
    pass

class G(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("G")
    pass

class H(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("H")
    pass

class I(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("I")
    pass

class J(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("J")
    pass

class K(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("K")
    pass

class L(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("L")
    pass

class M(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("M")
    pass

class N(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("N")
    pass

class O(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("O")
    pass

class P(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("P")
    pass

class Q(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("Q")
    pass

class R(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("R")
    pass

class S(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("S")
    pass

class T(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("T")
    pass

class U(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("U")
    pass

class V(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("V")
    pass

class W(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("W")
    pass

class X(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("X")
    pass

class Y(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("Y")
    pass

class Z(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        recognizing("Z")
    pass




class CorrectWindow(Screen):
    def on_enter(self):
        time.sleep(0)
        self.callback()

    def callback(self):
        st("CORRECT WELL DONE")

    def next(self):
        if p=="r":
            a = str((random.randint(1, 26)))
            global random_slide
            random_slide = a
            sm.current = random_slide
        else:
            global m
            if m == 26:
                m = "finish"
            else:
                m = m + 1
            sm.current = str(m)


    pass


class TryAgainWindow(Screen):
    def on_enter(self):
        time.sleep(.75)
        self.callback()

    def callback(self):
        st("OH PLEASE TRY AGAIN")

    def next(self):
        if p=="r":
            a = str((random.randint(1, 26)))
            global random_slide
            random_slide = a
            sm.current = random_slide
        else:
            global m
            if m == 2:
                m="finish"
            else:
                m=m+1
            sm.current = str(m)

    def tryagain(self):
        if p=="r":

            sm.current = random_slide
        else:

            sm.current = str(m)

    pass

class Finish(Screen):
    pass
class End(Screen):
    def on_enter(self):
        time.sleep(2)
        self.callback()

    def callback(self):
        self.MyApp.exit()
    pass

sm = ScreenManager(transition = FadeTransition(duration=1.15))
sm.add_widget(MainWindow(name='main'))
sm.add_widget(CorrectWindow(name='correct'))
sm.add_widget(TryAgainWindow(name='wrong'))
sm.add_widget(Finish(name='finish'))
sm.add_widget(End(name='end'))
sm.add_widget(A(name='1'))
sm.add_widget(B(name='2'))
sm.add_widget(C(name='3'))
sm.add_widget(D(name='4'))
sm.add_widget(E(name='5'))
sm.add_widget(F(name='6'))
sm.add_widget(G(name='7'))
sm.add_widget(H(name='8'))
sm.add_widget(I(name='9'))
sm.add_widget(J(name='10'))
sm.add_widget(K(name='11'))
sm.add_widget(L(name='12'))
sm.add_widget(M(name='13'))
sm.add_widget(N(name='14'))
sm.add_widget(O(name='15'))
sm.add_widget(P(name='16'))
sm.add_widget(Q(name='17'))
sm.add_widget(R(name='18'))
sm.add_widget(S(name='19'))
sm.add_widget(T(name='20'))
sm.add_widget(U(name='21'))
sm.add_widget(V(name='22'))
sm.add_widget(W(name='23'))
sm.add_widget(X(name='24'))
sm.add_widget(Y(name='25'))
sm.add_widget(Z(name='26'))








class MyApp(App):
    def build(self):

        return sm



if __name__ == "__main__":
    MyApp().run()