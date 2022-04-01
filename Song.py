from pydub import AudioSegment
from simpleaudio import play_buffer


class Song:
    def __init__(self, path):
        self.sound = AudioSegment.from_file(path)

    def play(self):
        play_object = play_buffer(
            self.sound.raw_data,
            self.sound.channels,
            self.sound.sample_width,
            self.sound.frame_rate
        )
        try:
            return play_object
        except KeyboardInterrupt:
            if play_object.is_playing():
                play_object.stop()
