from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Ellipse
import random

class CricketApp(App):

    def build(self):

        layout = FloatLayout()

        self.score_value = 0
        self.lives_value = 3

        self.background = Image(
            source="/storage/emulated/0/Download/background.jpg",
            size_hint=(1, 1)
        )

        self.player = Image(
            source="/storage/emulated/0/Download/cricket.png",
            size_hint=(None, None),
            size=(250, 250),
            pos=(180, 380)
        )

        self.score = Label(
            text="Score: 0",
            size_hint=(0.3, 0.1),
            pos_hint={"x":0.0, "y":0.9}
        )

        self.lives = Label(
            text="Lives: 3",
            size_hint=(0.3, 0.1),
            pos_hint={"x":0.7, "y":0.9}
        )

        self.game_over = Label(
            text="",
            font_size=50,
            size_hint=(1, 0.2),
            pos_hint={"x":0, "y":0.4}
        )

        self.restart_btn = Button(
            text="RESTART",
            size_hint=(0.4, 0.1),
            pos_hint={"x":0.3, "y":0.25},
            opacity=0,
            disabled=True
        )

        self.restart_btn.bind(on_press=self.restart_game)

        self.hit_sound = SoundLoader.load(
            "/storage/emulated/0/Download/hit.wav"
        )

        self.ball_x = random.randint(50, 500)
        self.ball_y = 900

        layout.add_widget(self.background)

        with layout.canvas.after:
            Color(1, 1, 0, 1)
            self.ball = Ellipse(
                pos=(self.ball_x, self.ball_y),
                size=(80, 80)
            )

        left_btn = Button(
            text="LEFT",
            size_hint=(0.3, 0.1),
            pos_hint={"x":0.05, "y":0.05}
        )

        right_btn = Button(
            text="RIGHT",
            size_hint=(0.3, 0.1),
            pos_hint={"x":0.65, "y":0.05}
        )

        left_btn.bind(on_press=self.start_left)
        left_btn.bind(on_release=self.stop_left)

        right_btn.bind(on_press=self.start_right)
        right_btn.bind(on_release=self.stop_right)

        layout.add_widget(self.player)
        layout.add_widget(self.score)
        layout.add_widget(self.lives)
        layout.add_widget(self.game_over)
        layout.add_widget(self.restart_btn)
        layout.add_widget(left_btn)
        layout.add_widget(right_btn)

        Clock.schedule_interval(self.move_ball, 0.03)

        return layout

    def start_left(self, instance):
        self.left_event = Clock.schedule_interval(self.go_left, 0.01)

    def stop_left(self, instance):
        if hasattr(self, "left_event"):
            self.left_event.cancel()

    def start_right(self, instance):
        self.right_event = Clock.schedule_interval(self.go_right, 0.01)

    def stop_right(self, instance):
        if hasattr(self, "right_event"):
            self.right_event.cancel()

    def go_left(self, dt):
        self.player.x -= 15
        if self.player.right < 0:
            self.player.x = 600

    def go_right(self, dt):
        self.player.x += 15
        if self.player.x > 600:
            self.player.x = -250

    def move_ball(self, dt):

        if self.lives_value <= 0:
            self.game_over.text = "GAME OVER"
            self.lives.text = "Final Score: " + str(self.score_value)
            self.restart_btn.opacity = 1
            self.restart_btn.disabled = False
            return

        self.ball_y -= 5
        self.ball.pos = (self.ball_x, self.ball_y)

        player_left = self.player.x
        player_right = self.player.x + self.player.width

        ball_left = self.ball_x
        ball_right = self.ball_x + 80

        if (
            ball_right > player_left and
            ball_left < player_right and
            self.ball_y <= self.player.y + 180 and
            self.ball_y >= self.player.y
        ):

            self.score_value += 1
            self.score.text = "Score: " + str(self.score_value)

            if self.hit_sound:
                self.hit_sound.play()

            self.ball_y = 900
            self.ball_x = random.randint(50, 500)

        if self.ball_y < 0:

            self.lives_value -= 1
            self.lives.text = "Lives: " + str(self.lives_value)

            self.ball_y = 900
            self.ball_x = random.randint(50, 500)

    def restart_game(self, instance):

        self.score_value = 0
        self.lives_value = 3

        self.score.text = "Score: 0"
        self.lives.text = "Lives: 3"

        self.game_over.text = ""

        self.ball_y = 900
        self.ball_x = random.randint(50, 500)

        self.restart_btn.opacity = 0
        self.restart_btn.disabled = True

CricketApp().run()
