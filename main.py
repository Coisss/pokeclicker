import kivy
kivy.require('2.3.0')  # replace with your current kivy version!

from kivy.uix.accordion import Animation
from kivy.uix.accordion import NumericProperty
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.metrics import dp, sp
from kivy.clock import Clock
from kivy.lang import Builder
import time


class MenuScreen(Screen):
    def test(self):
        print('Click!')
        self.ids.title.text = "New Title"
        pass


class SettingsScreen(Screen):
    pass


class ShopScreen(Screen):
    pass


class GameScreen(Screen):
    pass


class CreditsScreen(Screen):
    pass


class RebirthScreen(Screen):
    pass


class ObjectGame(Image):
    anim_play = False

    def on_touch_down(self, touch):
        if self.collide_point(touch.pos[0], touch.pos[1]) and self.anim_play == False:
            self.anim_play = True
            app.points = app.points + app.number

            temp_x = self.x
            temp_y = self.y
            temp_width = self.width
            temp_height = self.height
            temp_center = self.center

            anim = Animation(width=dp(300), duration=0.03) + Animation(width=temp_width, duration=0.03)
            anim &= Animation(height=dp(300), duration=0.03) + Animation(height=temp_height, duration=0.03)
            anim &= Animation(center=self.parent.center, duration=0.03) + Animation(center=self.parent.center, duration=0.03)

            anim.start(self)
            anim.bind(on_complete=lambda a, b: setattr(self, 'anim_play', False))

            print('Touchy!')
        else:
            print('Owchie!')
        if app.points == 50:
            ...
        return super().on_touch_down(touch)

# надо будет сделать такое, чтоб если можно купить улучшение -
# кнопка будет зелёная, если нет
# кнопка будет серая

class DoubleClick(Button):
    anim_play = False
    price = NumericProperty(50)
    def on_touch_down(self, touch):

        if self.collide_point(touch.pos[0], touch.pos[1]) and self.anim_play == False and app.points >= self.price:
            app.number = app.number * 2
            app.points -= self.price
            app.ball = 'images/greatball.png'

            self.price *= 2
            #round(self.price, 0)

            print('Upgrade!')
        else:
            print('No Upgrade?')
        return super().on_touch_down(touch)


class Rebirth(Button):
    anim_play = False
    price = NumericProperty(10000)
    
    def on_touch_down(self, touch):
        if self.collide_point(touch.pos[0], touch.pos[1]) and self.anim_play == False and app.points >= self.price:
            app.points = 0
            app.k_passive_income = 0
            app.number = 1

            app.rebirth_count += 1
            self.price *= 3
            #round(self.price)

            print('Rebirth!')
        else:
            print('No Rebirth?')
        return super().on_touch_down(touch)


class Income(Button):
    anim_play = False
    price = NumericProperty(10)
    def on_touch_down(self, touch):
        if self.collide_point(touch.pos[0], touch.pos[1]) and self.anim_play == False and app.points >= self.price:
            app.k_passive_income += 1
            app.points -= self.price

            self.price *= 2
            #round(self.price)
            print(app.k_passive_income)
        else:
            print('No Upgrade?')
        return super().on_touch_down(touch)

class Money(Button):
    anim_play = False
    price = NumericProperty(0)
    def on_touch_down(self, touch):
        if self.collide_point(touch.pos[0], touch.pos[1]) and self.anim_play == False and app.points >= self.price:
            app.k_passive_income += 5000000
            app.points -= self.price

            print(app.k_passive_income)
        else:
            print('No Upgrade?')
        return super().on_touch_down(touch)


class PokeClicker(App):
    points = NumericProperty(0) 
    number = 1
    number2 = 1
    k_passive_income = 0
    k_bonus_multiplier = 1
    bonus_income = k_passive_income * k_bonus_multiplier
    bonus_number = number * number2
    rebirth_count = NumericProperty(0)
    ball = 'images/pokeball.png'

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='main'))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(ShopScreen(name="shop"))
        sm.add_widget(CreditsScreen(name="credits"))
        sm.add_widget(SettingsScreen(name="settings"))

        # с помощью модуля
        Clock.schedule_interval(self.update_points, 1)

        return sm

    def update_points(self, dt):
        self.points += self.k_passive_income


# Window.clearcolor = (1, 1, 1, 1)

if __name__ == '__main__':
    Window.size = (450, 900)
    app = PokeClicker()
    app.run()
