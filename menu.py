# Sophia Ho
# different menus and their functions and displays

# Basic Animation Framework From 15-112 Course Notes

from tkinter import *

####################################
# customize these functions
####################################


# each menu has buttons that lead to submenus, background art, and music
# startMenu: displays submenus, 3 buttons, display high score
# startGame: starts game, displays pause button, displays actual game, room for 
# typing reading, display high score
# settings: displays buttons to change size of kanji, change speed, volume
# pauseScreen: displays rules, lets player quit, displays current score, high 
# score

def init(data):
    data.mode = "startScreen"
    data.fallSpeed = 10
    data.score = 0
    data.highScore = 0

def drawButtons(canvas, buttonData):
    for button in buttonData:
        x0, y0, x1, y1, buttonName = button
        midX = (x1 + x0) / 2
        midY = (y1 + y0) / 2
        canvas.create_rectangle(x0, y0, x1, y1, fill="gray")
        canvas.create_text(midX, midY, text = buttonName, fill="white")

def startScreenButtons(data):
    sideMargin = 50
    topMargin = data.height / 2 
    height = data.height / 15
    width = data.width - sideMargin * 2
    spacing = 10
    options = ["Start Game", "Settings", "Rules", ]
    result = []
    for i in range(len(options)):
        x0 = sideMargin
        y0 = topMargin + spacing + i * height 
        x1 = data.width - sideMargin
        y1 = height * (i + 1) + spacing + topMargin
        result.append([x0, y0, x1, y1, options[i]])
    return result

def gameModeScreenButtons(data):
    sideMargin = 50
    topMargin = data.height / 2 
    height = data.height / 15
    width = data.width - sideMargin * 2
    spacing = 10
    options = ["Hiragana", "Katakana", "Kanji", ]
    result = []
    for i in range(len(options)):
        x0 = sideMargin
        y0 = topMargin + spacing + i * height 
        x1 = data.width - sideMargin
        y1 = height * (i + 1) + spacing + topMargin
        result.append([x0, y0, x1, y1, options[i]])
    return result

def gameScreenButtons(data):
    sideMargin = 50
    bottomMargin = 10
    height = 20
    options = ["Start Screen", "Settings", "Pause"]
    width = (data.width - 2 * sideMargin) / 3
    result = []
    for i in range(len(options)):
        x0 = sideMargin + i * width
        y0 = data.height - bottomMargin - height
        x1 = sideMargin + (i + 1) * width
        y1 = data.height - bottomMargin
        result.append([x0, y0, x1, y1, options[i]])
    return result

def pauseScreenButtons(data):
    sideMargin = 50
    bottomMargin = 50
    height = 20
    options = ["Resume", "Settings"]
    width = (data.width - 2 * sideMargin) / 2
    result = []
    for i in range(len(options)):
        x0 = sideMargin + i * width
        y0 = data.height - bottomMargin - height
        x1 = sideMargin + (i + 1) * width
        y1 = data.height - bottomMargin
        result.append([x0, y0, x1, y1, options[i]])
    return result

def rulesScreenButtons(data):
    width = data.width / 5
    height = 20
    bottomMargin = 50
    x0, y0 = data.width / 2 - width / 2, data.height - bottomMargin - height
    x1, y1 = data.width / 2 + width / 2, data.height - bottomMargin
    return [[x0, y0, x1, y1, "Start Screen"]]

def settingsScreenButtons(data):
    sideMargin = 50
    topMargin = data.height / 2 
    height = data.height / 15
    width = data.width - sideMargin * 2
    spacing = 10
    options = ["Start Screen", "Size of Kanji", "Speed of Fall", ]
    result = []
    for i in range(len(options)):
        x0 = sideMargin
        y0 = topMargin + spacing + i * height 
        x1 = data.width - sideMargin
        y1 = height * (i + 1) + spacing + topMargin
        result.append([x0, y0, x1, y1, options[i]])
    return result
    
def getButtons(data):
    if data.mode == "startScreen":
        return startScreenButtons(data)
    elif data.mode == "gameModeScreen":
        return gameModeScreenButtons(data)
    elif data.mode == "gameScreen":
        return gameScreenButtons(data)
    elif data.mode == "settingsScreen":
        return settingsScreenButtons(data)
    elif data.mode == "rulesScreen":
        return rulesScreenButtons(data)
    elif data.mode == "pauseScreen":
        return pauseScreenButtons(data)

def buttonAction(data, buttonName):
    if buttonName == "Start Game": data.mode = "gameModeScreen"
    elif buttonName == "Settings": data.mode = "settingsScreen"
    elif buttonName == "Rules": data.mode = "rulesScreen"
    elif buttonName == "Start Screen": data.mode = "startScreen"
    elif buttonName == "Pause": data.mode = "pauseScreen"
    elif buttonName == "Quit": data.mode = "quitScreen"
    elif buttonName == "Size of Kanji": data.mode = "changeSizeScreen"
    elif buttonName == "Speed of Fall": data.mode = "changeSpeedScreen"
    elif buttonName == "Hiragana": data.mode = "gameScreen"
    elif buttonName == "Katakana": data.mode = "gameScreen"
    elif buttonName == "Kanji": data.mode = "gameScreen"
    elif buttonName == "Resume": data.mode = "gameScreen"

def drawStartScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="white", width=0)
    options = ["Start Game", "Settings", "Rules", ]
    buttonData = getButtons(data)
    drawButtons(canvas, buttonData)
    canvas.create_text(data.width / 2, data.height / 6, text="Kanji Rain", 
                        font=("Comic Sans MS", 50, "bold"))
    canvas.create_text(data.width / 2, data.height / 3, text="High Score: " +
                        str(data.highScore), font=("Comic Sans MS", 50, "bold"))
    
def drawGameModeScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="white", width=0)
    options = ["Hiragana", "Katakana", "Kanji"]
    buttonData = getButtons(data)
    drawButtons(canvas, buttonData)

def drawGameScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="white", width=0)
    canvas.create_text(data.width / 2, data.height / 2, text="game")
    options = ["Start Screen", "Settings", "Pause"]
    buttonData = getButtons(data)
    drawButtons(canvas, buttonData)

def drawSettingsScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="white", width=0)
    buttonData = getButtons(data)
    drawButtons(canvas, buttonData)

def drawRulesScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="white", width=0)
    canvas.create_text(data.width / 2, data.height / 2, text="rules")
    buttonData = getButtons(data)
    drawButtons(canvas, buttonData)

def drawPauseScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="white", width=0)
    buttonData = getButtons(data)
    drawButtons(canvas, buttonData)
    canvas.create_text(data.width / 2, data.height / 4, text="Paused",
                        font=("Comic Sans MS", 36, "bold"))
    canvas.create_text(data.width / 2, data.height / 2, text="Score: "
                        + str(data.score), font=("Comic Sans MS", 36, "bold"))

def mousePressed(event, data):
    buttons = getButtons(data)
    for button in buttons:
        x0, y0, x1, y1, buttonName = button
        if (x0 <= event.x <= x1 and y0 <= event.y <= y1):
            buttonAction(data, buttonName)

def keyPressed(event, data):
    pass

def redrawAll(canvas, data):
    if data.mode == "startScreen":
        drawStartScreen(canvas, data)
    elif data.mode == "gameModeScreen":
        drawGameModeScreen(canvas, data)
    elif data.mode == "gameScreen":
        drawGameScreen(canvas, data)
    elif data.mode == "rulesScreen":
        drawRulesScreen(canvas, data)
    elif data.mode == "settingsScreen":
        drawSettingsScreen(canvas, data)
    elif data.mode == "pauseScreen":
        drawPauseScreen(canvas, data)
    

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

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
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
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)