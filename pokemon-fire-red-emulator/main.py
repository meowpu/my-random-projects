from cmu_graphics import *

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
# startScreen = Image('startscreenFrames/frame_0_delay-0.08s.gif',
#                     1000,
#                     1000,
#                     width=400,
#                     height=400)
startScreenCover = Rect(0, 0, 400, 400, opacity=0)


def onKeyPress(key):
  if (stage == 'startScreen' and key == 'enter' and startScreen.top == 0):
    app.startScreenFading = True


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
        startScreen.top = 1000
        startScreenCover.top = 1000
      else:
        startScreenCover.opacity += 1


cmu_graphics.run()
