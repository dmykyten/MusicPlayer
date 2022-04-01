from App import App
from Interface import Interface

class Player:
    def __init__(self, path):
        self.path = path
        self.input_value = ''
        self.interface = Interface()
        self.player = App(self.interface)
        self.track = None
        self.track_name = ''
        self.main_screen()

    def music_list_screen(self):
        while self.input_value != 0:
            self.player.display_music_list(self.path)
            self.input_value = input()
            if int(self.input_value) in range(1, len(self.player.music) + 1):
                self.track_name = self.player.music[int(self.input_value) - 1]
                self.track = self.player.play_track(self.path + '\\' + self.track_name)
                self.input_value = 0

    def main_screen(self):
        while True:
            self.player.display_main_screen(self.track_name)
            self.input_value = input()
            if self.input_value == '1':
                self.music_list_screen()
            if self.input_value == '3' and self.track is not None:
                self.track.stop()
                self.track = None
                self.track_name = ''


if __name__ == '__main__':
    a = Player('music')