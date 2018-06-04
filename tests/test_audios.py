import unittest
import pygame
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from simian.audio.audios import Sound, Music
from simian.audio.audio_manager import AudioManager

class SoundTest(unittest.TestCase):
    def setUp(self):
        self.audio_manager = AudioManager()

    def test_play_sound(self):
        sound = Sound('assets/audio/sound.wav')
        self.assertTrue(sound.play())

    def test_play_music(self):
        music = Music('assets/audio/music.mp3')
        self.assertTrue(music.play())