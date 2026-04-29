import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        result = emotion_detector("I am glad this happened")

        self.assertEqual(result['dominant_emotion'], 'joy')

unittest.main()