import os
import json
from datetime import datetime

PATH = "data\\interface.json"


class Interface:

    def __init__(self):
        self._parse_data()

    def draw_main(self, track_name=''):
        print(self._greetings())
        print(self._current_time())
        print()
        if track_name == '':
            print(self._menu())
        else:
            print(self._current_track(track_name))
            print("3. Stop playing")

    def draw_music_list(self, names: list):
        print("0. Back to main screen.")
        print("Music in selected folder:")
        for name in self._music_list(names):
            print(name)

    def _menu(self):
        return [obj["value"] for obj in self.data
                if obj["name"] == "menu"].pop()

    def _music_list(self, names: list):
        return [f'{number + 1}. {name}' for number, name in enumerate(names)]

    def _parse_data(self):
        try:
            with open(PATH, 'r', encoding="utf-8") as file:
                self.data = json.loads(file.read())
        except FileNotFoundError as e:
            return e

    def _greetings(self):
        return [obj["value"] for obj in self.data
                if obj["name"] == "greetings"].pop() + os.getenv('username')

    def _current_track(self, track_name: str):
        return [obj["value"] for obj in self.data
                if obj["name"] == "current_track"].pop() + track_name

    def _current_time(self):
        now = datetime.now()
        return [obj["value"] for obj in self.data
                if obj["name"] == "current_time"].pop() + now.strftime("%H:%M")

    def clear(self):
        os.system('cls')

