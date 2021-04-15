from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer


class MyVideo(App):

    def build(self):
        self.vid=VideoPlayer(source='video.mp4',state='play')
        return self.vid



MyVideo().run()