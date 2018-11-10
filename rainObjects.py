# George Whitfield 
# Hack 112 2018
# November 9 2018


class RainingObject(object):
    def __init__(self, word, reading, position):
        self.word = word # word in japanese 
        self.reading = reading # the reading in japanese hiragana
        self.posx = position[0] # x value of the current position
        self.posy = position[1] # y value of the current position
        self.defaultRainSpeed = 7
    
    def calculateRainSpeed(self):
        lenWord = len(self.word)
        return self.defaultRainSpeed - lenWord
    
class KanjiRain(RainingObject):
    def __init__(self, word, reading, position, kanjiSize):
        super().__init__(word, reading, position, kanjiSize)
        self.kanjiSize = kanjiSize
