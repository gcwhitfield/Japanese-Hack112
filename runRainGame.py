# George Whitfield 
# Hack 112 2018
# November 9 2018

# Updated Animation Starter Code

from tkinter import *
import readJapaneseWordFiles
import rainObjects
import random

# ---------------------------------------------------- #
# --------------- global variables ------------------- #
# ---------------------------------------------------- #

# this is a dictionary of the words that we are currently using for the level
wordBank = readJapaneseWordFiles.formatJapanese(
    readJapaneseWordFiles.readFile('textFiles/jlptn5words.txt')
) 

# ---------------------------------------- #
# -------- Kanji Rain Game Logic --------- #
# ---------------------------------------- #

def addNewRainingWord(data):
    newWord = data.wordBank[random.randint(0, len(data.wordBank))] # get a random word
    data.rainingKanjis.add(rainObjects.KanjiRain(
        word = newWord[0],
        reading = newWord[1],
        meaning = newWord[2],
        position = (
            random.randint(data.wordMargin, data.width - data.wordMargin),
            0
        ),
        size = 70,
        fallSpeed = 3
    ))

def kanjiCollisions(data): # remove the kanji when it hits the bottom of screen
    kanjisToRemove = set()
    for kanji in data.rainingKanjis:
        if kanji.isCollidingWithBottom(data):
            kanjisToRemove.add(kanji)
    for kanji in kanjisToRemove:
        data.rainingKanjis.remove(kanji)

def runEveryFrame(data): # run this every animation frame
    moveKanjis(data)
    kanjiCollisions(data)

def runEveryWordAddInterval(data):# run this every second
    addNewRainingWord(data)

def moveKanjis(data):
    for kanji in data.rainingKanjis:
        kanji.moveDown()

def drawKanjis(canvas, data):
    for kanji in data.rainingKanjis:
        assert(type(kanji) == rainObjects.KanjiRain)
        canvas.create_text(
            kanji.posx,
            kanji.posy,
            text = kanji.word,
            font = 'Arial ' + str(kanji.size) + ' bold',
            fill = 'black'
        )

def drawBackground(canvas, data):
    canvas.create_image(data.width//2, data.height//2,
                        image = data.backGroundImage)

# --------------------------------------------------------- #
# -------------- Animation Functions ---------------------- #
# --------------------------------------------------------- #

def init(data):
    data.currGameTime = 0
    data.remainingGameTime = 3600 # game time limit

    data.score = 0
    data.rainingKanjis = set()
    data.wordBank = wordBank
    data.currentInput = ''
    data.wordMargin = 100 # margin on the right and left sides of screen

    data.wordFreqency = 30 # number of seconds between each new word generated
    
    data.backGroundImage = PhotoImage(file = 'images/kanjibackground.gif')

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    data.currGameTime += 1
    runEveryFrame(data)
    if data.currGameTime % data.wordFreqency == 0:
        runEveryWordAddInterval(data)

def redrawAll(canvas, data):
    drawBackground(canvas, data)
    drawKanjis(canvas, data)
    

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 1000)