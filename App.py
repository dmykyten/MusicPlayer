import os
from Interface import Interface
from Song import Song


class App:
    def __init__(self, interface: Interface):
        self.interface = interface
        self.music = []

    def display_main_screen(self, track_name=''):
        self.interface.draw_main(track_name)

    def display_music_list(self, path_to_dir: str):
        self.interface.clear()
        self.get_music_list(path_to_dir)
        self.interface.draw_music_list(self.music)

    def play_track(self, path_to_track:str):
        track = Song(path_to_track)
        return track.play()

    def get_music_list(self, path_to_dir: str):
        self.music = os.listdir(path_to_dir)





