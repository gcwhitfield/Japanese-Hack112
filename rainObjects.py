# George Whitfield 
# Hack 112 2018
# November 9 2018


class RainingObject(object):
    def __init__(self, word, reading, meaning, position, size, fallSpeed):
        self.word = word # word in japanese 
        self.reading = reading # the reading in japanese hiragana
        self.meaning = meaning # the meaning in english
        self.posx = position[0] # x value of the current position
        self.posy = position[1] # y value of the current position
        self.size = size 
        self.defaultRainSpeed = 7
        if fallSpeed != None:
            self.fallSpeed = fallSpeed
        else:
            self.fallSpeed = self.defaultRainSpeed 
    
    def calculateRainSpeed(self):
        lenWord = len(self.word)
        return self.defaultRainSpeed - lenWord
    
    def moveDown(self):
        self.posy += self.fallSpeed

    def isCollidingWithBottom(self, data):
        return (self.posy + 20 + self.size) > data.height
        
class KanjiRain(RainingObject):
    def __init__(self, word, reading, meaning, position, size, fallSpeed):
        super().__init__(word, reading, meaning, position, size, fallSpeed)