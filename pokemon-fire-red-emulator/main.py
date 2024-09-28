from cmu_graphics import *

controlsText = Label('CONTROLS', 0, 0, fill='white', opacity=0, size=15)
controlsText
controlsScreenNext=Group(Rect(325,10,20,20,fill='white',opacity=0),Label('A',335,20,fill='blue',opacity=0),Label('NEXT',375,20,fill='white',size=15,opacity=0))
controlsText.left = 25
controlsText.top = 15
controlsScreen1 = Group(controlsText,controlsScreenNext)
newGameButton = Image('start.png', 50, 40, opacity=0, width=300)
buttons = Group(newGameButton)

app.startScreenFading = False
app.startScreenOpacity = 100
app.steps = 0
stage = 'copyrightScreen'
app.stepsPerSecond = 100
app.background = 'black'
copyrightScreen = Image('copyright-screen.png', 0, 0, width=400, height=400)
startScreen = Group(
    Image('startscreenFrames/frame_0_delay-0.08s.gif',
          1000,
          1000,
          width=400,
          height=400))

startScreenCover = Rect(0, 0, 400, 400, opacity=0)


def onKeyPress(key):
  global stage
  if (stage == 'startScreen' and key == 'enter' and startScreen.top == 0):
    app.startScreenFading = True
  if (stage == 'newGameSelect' and key == 'a'):
    stage = 'controlsScreen1'


def onStep():
  global stage
  global startScreen

  app.steps += 1
  if (app.steps >= 100 and app.steps < 200):
    copyrightScreen.opacity -= 1
  if (app.steps == 200):
    app.background = 'white'
    copyrightScreen.top = 5000
    stage = 'startScreen'
  if (stage == 'startScreen'):
    frameNumber = (app.steps + 17) % 31
    urlString = 'startscreenFrames/frame_' + str(
        frameNumber) + '_delay-0.08s.gif'

    startScreen.add(Image(urlString, 0, 0, width=400, height=400))
    if (app.startScreenFading):
      if (startScreenCover.opacity == 100):
        app.startScreenFading = False

        startScreenCover.opacity = 0
        startScreen.opacity = 0
        newGameButton.opacity = 100
        stage = 'newGameSelect'
        app.background = 'darkBlue'
      else:
        startScreenCover.opacity += 1
  if (stage == 'controlsScreen1'):
    newGameButton.opacity = 0
    controlsScreen1.opacity = 100


cmu_graphics.run()
