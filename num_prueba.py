#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on September 29, 2023, at 19:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'num_prueba'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\MRS\\Dropbox\\NumerosidadYDensidad\\num_prueba.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "consent" ---
consent_2 = visual.TextStim(win=win, name='consent_2',
    text='En esta prueba queremos evaluar la percepción de distintas imágenes. La prueba será en una computadora, donde se presentarán dos imágenes y deberás escoger una de acuerdo a la instrucción dada. Después, haremos unas preguntas referentes a cómo te sentiste durante la prueba. Todo el proceso debería tomar 10 minutos. Es muy importante que sepas que tu participación en este estudio es totalmente voluntaria y que puedes decidir no continuar en cualquier momento. \n\nLos datos obtenidos de la prueba serán únicamente con fines académicos. En ninguna circunstancia se harán públicos los datos personales de los participantes.  \n\nSi existe cualquier duda con respecto a los puntos que se mencionan o es necesario hacer claro algún punto en particular, es posible expresarlo ante el investigador y con gusto se ofrecerá ayuda.\n\nOtorgo mi consentimiento para que los datos derivados del estudio sean utilizados para cubrir los objetivos del proyecto de investigación en cuestión.\n',
    font='Open Sans',
    pos=(0, 0.03), height=0.03, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
consent_si = visual.ButtonStim(win, 
    text='Sí doy mi consentimiento', font='Arvo',
    pos=(0, -0.45),
    letterHeight=0.05,
    size=(0.5,0.15), borderWidth=0.0,
    fillColor=[1.0000, -0.4588, -1.0000], borderColor=[1.0000, -0.4588, -1.0000],
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-center',
    name='consent_si'
)
consent_si.buttonClock = core.Clock()

# --- Initialize components for Routine "intro_gral" ---
# Set experiment start values for variable component intro_gral_flag
intro_gral_flag = ''
intro_gral_flagContainer = []
text_up_2 = visual.TextStim(win=win, name='text_up_2',
    text='A continuación, te presentaremos dos imágenes, una del lado derecho y una del lado izquierdo.',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_mid_2 = visual.TextStim(win=win, name='text_mid_2',
    text='En cada caso, elige la imagen con MAYOR AREA',
    font='Open Sans',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_down_2 = visual.TextStim(win=win, name='text_down_2',
    text='Trata de responder tan rápido como puedas.',
    font='Open Sans',
    pos=(0, -0.05), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
button_hello_2 = visual.ButtonStim(win, 
    text='INICIAR', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=(0.3,0.15), borderWidth=0.0,
    fillColor=[1.0000, -0.4588, -1.0000], borderColor=[1.0000, -0.4588, -1.0000],
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-center',
    name='button_hello_2'
)
button_hello_2.buttonClock = core.Clock()

# --- Initialize components for Routine "TEST_illusion" ---
illusion = visual.ImageStim(
    win=win,
    name='illusion', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[56*0.72,28*0.72],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
LEFT_illusion = visual.Rect(
    win=win, name='LEFT_illusion',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[-0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.0, depth=-1.0, interpolate=True)
RIGHT_illusion = visual.Rect(
    win=win, name='RIGHT_illusion',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.0, depth=-2.0, interpolate=True)
mouse_illusion = event.Mouse(win=win)
x, y = [None, None]
mouse_illusion.mouseClock = core.Clock()

# --- Initialize components for Routine "inter" ---
inter_text = visual.TextBox2(
     win, text='Para ver la siguiente imagen\nHaz click sobre EL CIRCULO NARANJA', font='Calibri',
     pos=[0, 0.3],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='inter_text',
     autoLog=True,
)
inter_circulo = visual.ShapeStim(
    win=win, name='inter_circulo',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[1.0000, -0.4588, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)
inter_mouse = event.Mouse(win=win)
x, y = [None, None]
inter_mouse.mouseClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "intro_pastries" ---
# Set experiment start values for variable component intro_pastries_flag
intro_pastries_flag = ''
intro_pastries_flagContainer = []
text_up_3 = visual.TextStim(win=win, name='text_up_3',
    text='A continuación, te presentaremos dos imágenes, una del lado derecho y una del lado izquierdo.',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_mid_3 = visual.TextStim(win=win, name='text_mid_3',
    text='En cada caso, elige el o los pastelillos con MAYOR AREA',
    font='Open Sans',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_down_3 = visual.TextStim(win=win, name='text_down_3',
    text='Trata de responder tan rápido como puedas.',
    font='Open Sans',
    pos=(0, -0.05), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
button_hello_3 = visual.ButtonStim(win, 
    text='INICIAR', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=(0.3,0.15), borderWidth=0.0,
    fillColor=[1.0000, -0.4588, -1.0000], borderColor=[1.0000, -0.4588, -1.0000],
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-center',
    name='button_hello_3'
)
button_hello_3.buttonClock = core.Clock()

# --- Initialize components for Routine "TEST_illusion" ---
illusion = visual.ImageStim(
    win=win,
    name='illusion', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[56*0.72,28*0.72],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
LEFT_illusion = visual.Rect(
    win=win, name='LEFT_illusion',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[-0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.0, depth=-1.0, interpolate=True)
RIGHT_illusion = visual.Rect(
    win=win, name='RIGHT_illusion',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.0, depth=-2.0, interpolate=True)
mouse_illusion = event.Mouse(win=win)
x, y = [None, None]
mouse_illusion.mouseClock = core.Clock()

# --- Initialize components for Routine "inter" ---
inter_text = visual.TextBox2(
     win, text='Para ver la siguiente imagen\nHaz click sobre EL CIRCULO NARANJA', font='Calibri',
     pos=[0, 0.3],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='inter_text',
     autoLog=True,
)
inter_circulo = visual.ShapeStim(
    win=win, name='inter_circulo',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[1.0000, -0.4588, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)
inter_mouse = event.Mouse(win=win)
x, y = [None, None]
inter_mouse.mouseClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "intro_score" ---
# Set experiment start values for variable component intro_score_flag
intro_score_flag = ''
intro_score_flagContainer = []
text_up_4 = visual.TextStim(win=win, name='text_up_4',
    text='A continuación, te presentaremos dos imágenes, una del lado derecho y una del lado izquierdo.',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_mid_4 = visual.TextStim(win=win, name='text_mid_4',
    text='En cada caso, elige la imagen con MAYOR AREA. Por cada respuesta correcta, obtendras un peso ($1)',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_down_4 = visual.TextStim(win=win, name='text_down_4',
    text='Trata de responder tan rápido como puedas.',
    font='Open Sans',
    pos=(0, -0.05), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
button_hello_4 = visual.ButtonStim(win, 
    text='INICIAR', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=(0.3,0.15), borderWidth=0.0,
    fillColor=[1.0000, -0.4588, -1.0000], borderColor=[1.0000, -0.4588, -1.0000],
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-center',
    name='button_hello_4'
)
button_hello_4.buttonClock = core.Clock()
# Set experiment start values for variable component score
score = ''
scoreContainer = []

# --- Initialize components for Routine "TEST_score" ---
illusion_score = visual.ImageStim(
    win=win,
    name='illusion_score', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[56*0.72,28*0.72],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
LEFT_illusion_score = visual.Rect(
    win=win, name='LEFT_illusion_score',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[-0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.0, depth=-1.0, interpolate=True)
RIGHT_illusion_score = visual.Rect(
    win=win, name='RIGHT_illusion_score',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.0, depth=-2.0, interpolate=True)
mouse_illusion_score = event.Mouse(win=win)
x, y = [None, None]
mouse_illusion_score.mouseClock = core.Clock()

# --- Initialize components for Routine "inter" ---
inter_text = visual.TextBox2(
     win, text='Para ver la siguiente imagen\nHaz click sobre EL CIRCULO NARANJA', font='Calibri',
     pos=[0, 0.3],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='inter_text',
     autoLog=True,
)
inter_circulo = visual.ShapeStim(
    win=win, name='inter_circulo',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[1.0000, -0.4588, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)
inter_mouse = event.Mouse(win=win)
x, y = [None, None]
inter_mouse.mouseClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "show_score" ---
scoreTxT_2 = visual.TextStim(win=win, name='scoreTxT_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "fin" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='Has terminado la prueba.\n¡Gracias!',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color=[-0.4902, -0.1765, 0.7647], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "consent" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
consentComponents = [consent_2, consent_si]
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "consent" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *consent_2* updates
    if consent_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_2.frameNStart = frameN  # exact frame index
        consent_2.tStart = t  # local t and not account for scr refresh
        consent_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'consent_2.started')
        consent_2.setAutoDraw(True)
    
    # *consent_si* updates
    if consent_si.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        consent_si.frameNStart = frameN  # exact frame index
        consent_si.tStart = t  # local t and not account for scr refresh
        consent_si.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_si, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'consent_si.started')
        consent_si.setAutoDraw(True)
    if consent_si.status == STARTED:
        # check whether consent_si has been pressed
        if consent_si.isClicked:
            if not consent_si.wasClicked:
                consent_si.timesOn.append(consent_si.buttonClock.getTime()) # store time of first click
                consent_si.timesOff.append(consent_si.buttonClock.getTime()) # store time clicked until
            else:
                consent_si.timesOff[-1] = consent_si.buttonClock.getTime() # update time clicked until
            if not consent_si.wasClicked:
                continueRoutine = False  # end routine when consent_si is clicked
                None
            consent_si.wasClicked = True  # if consent_si is still clicked next frame, it is not a new click
        else:
            consent_si.wasClicked = False  # if consent_si is clicked next frame, it is a new click
    else:
        consent_si.wasClicked = False  # if consent_si is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "consent" ---
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('consent_si.numClicks', consent_si.numClicks)
if consent_si.numClicks:
   thisExp.addData('consent_si.timesOn', consent_si.timesOn)
   thisExp.addData('consent_si.timesOff', consent_si.timesOff)
else:
   thisExp.addData('consent_si.timesOn', "")
   thisExp.addData('consent_si.timesOff', "")
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
rblocks = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('randomblock.xlsx'),
    seed=None, name='rblocks')
thisExp.addLoop(rblocks)  # add the loop to the experiment
thisRblock = rblocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRblock.rgb)
if thisRblock != None:
    for paramName in thisRblock:
        exec('{} = thisRblock[paramName]'.format(paramName))

for thisRblock in rblocks:
    currentLoop = rblocks
    # abbreviate parameter names if possible (e.g. rgb = thisRblock.rgb)
    if thisRblock != None:
        for paramName in thisRblock:
            exec('{} = thisRblock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "intro_gral" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    intro_gral_flag = 0  # Set routine start values for intro_gral_flag
    # Run 'Begin Routine' code from code_intro_gral
    if intro_gral_flag == 0:
        intro_gral_flag = intro_gral_flag + 1
    else:
        continueRoutine = False
    # keep track of which components have finished
    intro_gralComponents = [text_up_2, text_mid_2, text_down_2, button_hello_2]
    for thisComponent in intro_gralComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro_gral" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_up_2* updates
        if text_up_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_up_2.frameNStart = frameN  # exact frame index
            text_up_2.tStart = t  # local t and not account for scr refresh
            text_up_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_up_2, 'tStartRefresh')  # time at next scr refresh
            text_up_2.setAutoDraw(True)
        
        # *text_mid_2* updates
        if text_mid_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_mid_2.frameNStart = frameN  # exact frame index
            text_mid_2.tStart = t  # local t and not account for scr refresh
            text_mid_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mid_2, 'tStartRefresh')  # time at next scr refresh
            text_mid_2.setAutoDraw(True)
        
        # *text_down_2* updates
        if text_down_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_down_2.frameNStart = frameN  # exact frame index
            text_down_2.tStart = t  # local t and not account for scr refresh
            text_down_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_down_2, 'tStartRefresh')  # time at next scr refresh
            text_down_2.setAutoDraw(True)
        
        # *button_hello_2* updates
        if button_hello_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_hello_2.frameNStart = frameN  # exact frame index
            button_hello_2.tStart = t  # local t and not account for scr refresh
            button_hello_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_hello_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_hello_2.started')
            button_hello_2.setAutoDraw(True)
        if button_hello_2.status == STARTED:
            # check whether button_hello_2 has been pressed
            if button_hello_2.isClicked:
                if not button_hello_2.wasClicked:
                    button_hello_2.timesOn.append(button_hello_2.buttonClock.getTime()) # store time of first click
                    button_hello_2.timesOff.append(button_hello_2.buttonClock.getTime()) # store time clicked until
                else:
                    button_hello_2.timesOff[-1] = button_hello_2.buttonClock.getTime() # update time clicked until
                if not button_hello_2.wasClicked:
                    continueRoutine = False  # end routine when button_hello_2 is clicked
                    None
                button_hello_2.wasClicked = True  # if button_hello_2 is still clicked next frame, it is not a new click
            else:
                button_hello_2.wasClicked = False  # if button_hello_2 is clicked next frame, it is a new click
        else:
            button_hello_2.wasClicked = False  # if button_hello_2 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro_gralComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro_gral" ---
    for thisComponent in intro_gralComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('intro_gral_flag.routineEndVal', intro_gral_flag)  # Save end routine value
    rblocks.addData('button_hello_2.numClicks', button_hello_2.numClicks)
    if button_hello_2.numClicks:
       rblocks.addData('button_hello_2.timesOn', button_hello_2.timesOn)
       rblocks.addData('button_hello_2.timesOff', button_hello_2.timesOff)
    else:
       rblocks.addData('button_hello_2.timesOn', "")
       rblocks.addData('button_hello_2.timesOff', "")
    # the Routine "intro_gral" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    A = data.TrialHandler(nReps=illusion_loop, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Imagenes/numerosity_condition_file.xlsx'),
        seed=None, name='A')
    thisExp.addLoop(A)  # add the loop to the experiment
    thisA = A.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisA.rgb)
    if thisA != None:
        for paramName in thisA:
            exec('{} = thisA[paramName]'.format(paramName))
    
    for thisA in A:
        currentLoop = A
        # abbreviate parameter names if possible (e.g. rgb = thisA.rgb)
        if thisA != None:
            for paramName in thisA:
                exec('{} = thisA[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "TEST_illusion" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        illusion.setImage(camino)
        # setup some python lists for storing info about the mouse_illusion
        mouse_illusion.x = []
        mouse_illusion.y = []
        mouse_illusion.leftButton = []
        mouse_illusion.midButton = []
        mouse_illusion.rightButton = []
        mouse_illusion.time = []
        mouse_illusion.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        TEST_illusionComponents = [illusion, LEFT_illusion, RIGHT_illusion, mouse_illusion]
        for thisComponent in TEST_illusionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TEST_illusion" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *illusion* updates
            if illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                illusion.frameNStart = frameN  # exact frame index
                illusion.tStart = t  # local t and not account for scr refresh
                illusion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(illusion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'illusion.started')
                illusion.setAutoDraw(True)
            if illusion.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > illusion.tStartRefresh + 15.0-frameTolerance:
                    # keep track of stop time/frame for later
                    illusion.tStop = t  # not accounting for scr refresh
                    illusion.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'illusion.stopped')
                    illusion.setAutoDraw(False)
            
            # *LEFT_illusion* updates
            if LEFT_illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LEFT_illusion.frameNStart = frameN  # exact frame index
                LEFT_illusion.tStart = t  # local t and not account for scr refresh
                LEFT_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LEFT_illusion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'LEFT_illusion.started')
                LEFT_illusion.setAutoDraw(True)
            if LEFT_illusion.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > LEFT_illusion.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    LEFT_illusion.tStop = t  # not accounting for scr refresh
                    LEFT_illusion.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'LEFT_illusion.stopped')
                    LEFT_illusion.setAutoDraw(False)
            
            # *RIGHT_illusion* updates
            if RIGHT_illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RIGHT_illusion.frameNStart = frameN  # exact frame index
                RIGHT_illusion.tStart = t  # local t and not account for scr refresh
                RIGHT_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RIGHT_illusion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RIGHT_illusion.started')
                RIGHT_illusion.setAutoDraw(True)
            if RIGHT_illusion.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RIGHT_illusion.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    RIGHT_illusion.tStop = t  # not accounting for scr refresh
                    RIGHT_illusion.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RIGHT_illusion.stopped')
                    RIGHT_illusion.setAutoDraw(False)
            # *mouse_illusion* updates
            if mouse_illusion.status == NOT_STARTED and t >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                mouse_illusion.frameNStart = frameN  # exact frame index
                mouse_illusion.tStart = t  # local t and not account for scr refresh
                mouse_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_illusion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_illusion.started', t)
                mouse_illusion.status = STARTED
                mouse_illusion.mouseClock.reset()
                prevButtonState = mouse_illusion.getPressed()  # if button is down already this ISN'T a new click
            if mouse_illusion.status == STARTED:  # only update if started and not finished!
                buttons = mouse_illusion.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([LEFT_illusion, RIGHT_illusion])
                            clickableList = [LEFT_illusion, RIGHT_illusion]
                        except:
                            clickableList = [[LEFT_illusion, RIGHT_illusion]]
                        for obj in clickableList:
                            if obj.contains(mouse_illusion):
                                gotValidClick = True
                                mouse_illusion.clicked_name.append(obj.name)
                        x, y = mouse_illusion.getPos()
                        mouse_illusion.x.append(x)
                        mouse_illusion.y.append(y)
                        buttons = mouse_illusion.getPressed()
                        mouse_illusion.leftButton.append(buttons[0])
                        mouse_illusion.midButton.append(buttons[1])
                        mouse_illusion.rightButton.append(buttons[2])
                        mouse_illusion.time.append(mouse_illusion.mouseClock.getTime())
                        
                        continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TEST_illusionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TEST_illusion" ---
        for thisComponent in TEST_illusionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for A (TrialHandler)
        A.addData('mouse_illusion.x', mouse_illusion.x)
        A.addData('mouse_illusion.y', mouse_illusion.y)
        A.addData('mouse_illusion.leftButton', mouse_illusion.leftButton)
        A.addData('mouse_illusion.midButton', mouse_illusion.midButton)
        A.addData('mouse_illusion.rightButton', mouse_illusion.rightButton)
        A.addData('mouse_illusion.time', mouse_illusion.time)
        A.addData('mouse_illusion.clicked_name', mouse_illusion.clicked_name)
        # the Routine "TEST_illusion" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "inter" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        inter_text.reset()
        # setup some python lists for storing info about the inter_mouse
        inter_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        interComponents = [inter_text, inter_circulo, inter_mouse, key_resp_2]
        for thisComponent in interComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "inter" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_text* updates
            if inter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_text.frameNStart = frameN  # exact frame index
                inter_text.tStart = t  # local t and not account for scr refresh
                inter_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_text, 'tStartRefresh')  # time at next scr refresh
                inter_text.setAutoDraw(True)
            
            # *inter_circulo* updates
            if inter_circulo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_circulo.frameNStart = frameN  # exact frame index
                inter_circulo.tStart = t  # local t and not account for scr refresh
                inter_circulo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_circulo, 'tStartRefresh')  # time at next scr refresh
                inter_circulo.setAutoDraw(True)
            # *inter_mouse* updates
            if inter_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_mouse.frameNStart = frameN  # exact frame index
                inter_mouse.tStart = t  # local t and not account for scr refresh
                inter_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('inter_mouse.started', t)
                inter_mouse.status = STARTED
                prevButtonState = inter_mouse.getPressed()  # if button is down already this ISN'T a new click
            if inter_mouse.status == STARTED:  # only update if started and not finished!
                buttons = inter_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(inter_circulo)
                            clickableList = inter_circulo
                        except:
                            clickableList = [inter_circulo]
                        for obj in clickableList:
                            if obj.contains(inter_mouse):
                                gotValidClick = True
                                inter_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *key_resp_2* updates
            if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in interComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "inter" ---
        for thisComponent in interComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for A (TrialHandler)
        x, y = inter_mouse.getPos()
        buttons = inter_mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(inter_circulo)
                clickableList = inter_circulo
            except:
                clickableList = [inter_circulo]
            for obj in clickableList:
                if obj.contains(inter_mouse):
                    gotValidClick = True
                    inter_mouse.clicked_name.append(obj.name)
        A.addData('inter_mouse.x', x)
        A.addData('inter_mouse.y', y)
        A.addData('inter_mouse.leftButton', buttons[0])
        A.addData('inter_mouse.midButton', buttons[1])
        A.addData('inter_mouse.rightButton', buttons[2])
        if len(inter_mouse.clicked_name):
            A.addData('inter_mouse.clicked_name', inter_mouse.clicked_name[0])
        # the Routine "inter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed illusion_loop repeats of 'A'
    
    
    # --- Prepare to start Routine "intro_pastries" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    intro_pastries_flag = 0  # Set routine start values for intro_pastries_flag
    # Run 'Begin Routine' code from code_intro_pastries
    if intro_pastries_flag == 0:
        intro_pastries_flag = intro_pastries_flag + 1
    else:
        continueRoutine = False
    # keep track of which components have finished
    intro_pastriesComponents = [text_up_3, text_mid_3, text_down_3, button_hello_3]
    for thisComponent in intro_pastriesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro_pastries" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_up_3* updates
        if text_up_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_up_3.frameNStart = frameN  # exact frame index
            text_up_3.tStart = t  # local t and not account for scr refresh
            text_up_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_up_3, 'tStartRefresh')  # time at next scr refresh
            text_up_3.setAutoDraw(True)
        
        # *text_mid_3* updates
        if text_mid_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_mid_3.frameNStart = frameN  # exact frame index
            text_mid_3.tStart = t  # local t and not account for scr refresh
            text_mid_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mid_3, 'tStartRefresh')  # time at next scr refresh
            text_mid_3.setAutoDraw(True)
        
        # *text_down_3* updates
        if text_down_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_down_3.frameNStart = frameN  # exact frame index
            text_down_3.tStart = t  # local t and not account for scr refresh
            text_down_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_down_3, 'tStartRefresh')  # time at next scr refresh
            text_down_3.setAutoDraw(True)
        
        # *button_hello_3* updates
        if button_hello_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_hello_3.frameNStart = frameN  # exact frame index
            button_hello_3.tStart = t  # local t and not account for scr refresh
            button_hello_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_hello_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_hello_3.started')
            button_hello_3.setAutoDraw(True)
        if button_hello_3.status == STARTED:
            # check whether button_hello_3 has been pressed
            if button_hello_3.isClicked:
                if not button_hello_3.wasClicked:
                    button_hello_3.timesOn.append(button_hello_3.buttonClock.getTime()) # store time of first click
                    button_hello_3.timesOff.append(button_hello_3.buttonClock.getTime()) # store time clicked until
                else:
                    button_hello_3.timesOff[-1] = button_hello_3.buttonClock.getTime() # update time clicked until
                if not button_hello_3.wasClicked:
                    continueRoutine = False  # end routine when button_hello_3 is clicked
                    None
                button_hello_3.wasClicked = True  # if button_hello_3 is still clicked next frame, it is not a new click
            else:
                button_hello_3.wasClicked = False  # if button_hello_3 is clicked next frame, it is a new click
        else:
            button_hello_3.wasClicked = False  # if button_hello_3 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro_pastriesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro_pastries" ---
    for thisComponent in intro_pastriesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('intro_pastries_flag.routineEndVal', intro_pastries_flag)  # Save end routine value
    rblocks.addData('button_hello_3.numClicks', button_hello_3.numClicks)
    if button_hello_3.numClicks:
       rblocks.addData('button_hello_3.timesOn', button_hello_3.timesOn)
       rblocks.addData('button_hello_3.timesOff', button_hello_3.timesOff)
    else:
       rblocks.addData('button_hello_3.timesOn', "")
       rblocks.addData('button_hello_3.timesOff', "")
    # the Routine "intro_pastries" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    B = data.TrialHandler(nReps=galletas_loop, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Galletas/numerosity_condition_file.xlsx'),
        seed=None, name='B')
    thisExp.addLoop(B)  # add the loop to the experiment
    thisB = B.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisB.rgb)
    if thisB != None:
        for paramName in thisB:
            exec('{} = thisB[paramName]'.format(paramName))
    
    for thisB in B:
        currentLoop = B
        # abbreviate parameter names if possible (e.g. rgb = thisB.rgb)
        if thisB != None:
            for paramName in thisB:
                exec('{} = thisB[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "TEST_illusion" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        illusion.setImage(camino)
        # setup some python lists for storing info about the mouse_illusion
        mouse_illusion.x = []
        mouse_illusion.y = []
        mouse_illusion.leftButton = []
        mouse_illusion.midButton = []
        mouse_illusion.rightButton = []
        mouse_illusion.time = []
        mouse_illusion.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        TEST_illusionComponents = [illusion, LEFT_illusion, RIGHT_illusion, mouse_illusion]
        for thisComponent in TEST_illusionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TEST_illusion" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *illusion* updates
            if illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                illusion.frameNStart = frameN  # exact frame index
                illusion.tStart = t  # local t and not account for scr refresh
                illusion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(illusion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'illusion.started')
                illusion.setAutoDraw(True)
            if illusion.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > illusion.tStartRefresh + 15.0-frameTolerance:
                    # keep track of stop time/frame for later
                    illusion.tStop = t  # not accounting for scr refresh
                    illusion.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'illusion.stopped')
                    illusion.setAutoDraw(False)
            
            # *LEFT_illusion* updates
            if LEFT_illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LEFT_illusion.frameNStart = frameN  # exact frame index
                LEFT_illusion.tStart = t  # local t and not account for scr refresh
                LEFT_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LEFT_illusion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'LEFT_illusion.started')
                LEFT_illusion.setAutoDraw(True)
            if LEFT_illusion.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > LEFT_illusion.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    LEFT_illusion.tStop = t  # not accounting for scr refresh
                    LEFT_illusion.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'LEFT_illusion.stopped')
                    LEFT_illusion.setAutoDraw(False)
            
            # *RIGHT_illusion* updates
            if RIGHT_illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RIGHT_illusion.frameNStart = frameN  # exact frame index
                RIGHT_illusion.tStart = t  # local t and not account for scr refresh
                RIGHT_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RIGHT_illusion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RIGHT_illusion.started')
                RIGHT_illusion.setAutoDraw(True)
            if RIGHT_illusion.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RIGHT_illusion.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    RIGHT_illusion.tStop = t  # not accounting for scr refresh
                    RIGHT_illusion.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RIGHT_illusion.stopped')
                    RIGHT_illusion.setAutoDraw(False)
            # *mouse_illusion* updates
            if mouse_illusion.status == NOT_STARTED and t >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                mouse_illusion.frameNStart = frameN  # exact frame index
                mouse_illusion.tStart = t  # local t and not account for scr refresh
                mouse_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_illusion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_illusion.started', t)
                mouse_illusion.status = STARTED
                mouse_illusion.mouseClock.reset()
                prevButtonState = mouse_illusion.getPressed()  # if button is down already this ISN'T a new click
            if mouse_illusion.status == STARTED:  # only update if started and not finished!
                buttons = mouse_illusion.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([LEFT_illusion, RIGHT_illusion])
                            clickableList = [LEFT_illusion, RIGHT_illusion]
                        except:
                            clickableList = [[LEFT_illusion, RIGHT_illusion]]
                        for obj in clickableList:
                            if obj.contains(mouse_illusion):
                                gotValidClick = True
                                mouse_illusion.clicked_name.append(obj.name)
                        x, y = mouse_illusion.getPos()
                        mouse_illusion.x.append(x)
                        mouse_illusion.y.append(y)
                        buttons = mouse_illusion.getPressed()
                        mouse_illusion.leftButton.append(buttons[0])
                        mouse_illusion.midButton.append(buttons[1])
                        mouse_illusion.rightButton.append(buttons[2])
                        mouse_illusion.time.append(mouse_illusion.mouseClock.getTime())
                        
                        continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TEST_illusionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TEST_illusion" ---
        for thisComponent in TEST_illusionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for B (TrialHandler)
        B.addData('mouse_illusion.x', mouse_illusion.x)
        B.addData('mouse_illusion.y', mouse_illusion.y)
        B.addData('mouse_illusion.leftButton', mouse_illusion.leftButton)
        B.addData('mouse_illusion.midButton', mouse_illusion.midButton)
        B.addData('mouse_illusion.rightButton', mouse_illusion.rightButton)
        B.addData('mouse_illusion.time', mouse_illusion.time)
        B.addData('mouse_illusion.clicked_name', mouse_illusion.clicked_name)
        # the Routine "TEST_illusion" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "inter" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        inter_text.reset()
        # setup some python lists for storing info about the inter_mouse
        inter_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        interComponents = [inter_text, inter_circulo, inter_mouse, key_resp_2]
        for thisComponent in interComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "inter" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_text* updates
            if inter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_text.frameNStart = frameN  # exact frame index
                inter_text.tStart = t  # local t and not account for scr refresh
                inter_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_text, 'tStartRefresh')  # time at next scr refresh
                inter_text.setAutoDraw(True)
            
            # *inter_circulo* updates
            if inter_circulo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_circulo.frameNStart = frameN  # exact frame index
                inter_circulo.tStart = t  # local t and not account for scr refresh
                inter_circulo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_circulo, 'tStartRefresh')  # time at next scr refresh
                inter_circulo.setAutoDraw(True)
            # *inter_mouse* updates
            if inter_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_mouse.frameNStart = frameN  # exact frame index
                inter_mouse.tStart = t  # local t and not account for scr refresh
                inter_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('inter_mouse.started', t)
                inter_mouse.status = STARTED
                prevButtonState = inter_mouse.getPressed()  # if button is down already this ISN'T a new click
            if inter_mouse.status == STARTED:  # only update if started and not finished!
                buttons = inter_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(inter_circulo)
                            clickableList = inter_circulo
                        except:
                            clickableList = [inter_circulo]
                        for obj in clickableList:
                            if obj.contains(inter_mouse):
                                gotValidClick = True
                                inter_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *key_resp_2* updates
            if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in interComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "inter" ---
        for thisComponent in interComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for B (TrialHandler)
        x, y = inter_mouse.getPos()
        buttons = inter_mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(inter_circulo)
                clickableList = inter_circulo
            except:
                clickableList = [inter_circulo]
            for obj in clickableList:
                if obj.contains(inter_mouse):
                    gotValidClick = True
                    inter_mouse.clicked_name.append(obj.name)
        B.addData('inter_mouse.x', x)
        B.addData('inter_mouse.y', y)
        B.addData('inter_mouse.leftButton', buttons[0])
        B.addData('inter_mouse.midButton', buttons[1])
        B.addData('inter_mouse.rightButton', buttons[2])
        if len(inter_mouse.clicked_name):
            B.addData('inter_mouse.clicked_name', inter_mouse.clicked_name[0])
        # the Routine "inter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed galletas_loop repeats of 'B'
    
    
    # --- Prepare to start Routine "intro_score" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    intro_score_flag = 0  # Set routine start values for intro_score_flag
    # Run 'Begin Routine' code from code_intro_score
    if intro_score_flag == 0:
        intro_score_flag = intro_score_flag + 1
    else:
        intro_score_flag = False
    score = 0  # Set routine start values for score
    # keep track of which components have finished
    intro_scoreComponents = [text_up_4, text_mid_4, text_down_4, button_hello_4]
    for thisComponent in intro_scoreComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro_score" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_up_4* updates
        if text_up_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_up_4.frameNStart = frameN  # exact frame index
            text_up_4.tStart = t  # local t and not account for scr refresh
            text_up_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_up_4, 'tStartRefresh')  # time at next scr refresh
            text_up_4.setAutoDraw(True)
        
        # *text_mid_4* updates
        if text_mid_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_mid_4.frameNStart = frameN  # exact frame index
            text_mid_4.tStart = t  # local t and not account for scr refresh
            text_mid_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_mid_4, 'tStartRefresh')  # time at next scr refresh
            text_mid_4.setAutoDraw(True)
        
        # *text_down_4* updates
        if text_down_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_down_4.frameNStart = frameN  # exact frame index
            text_down_4.tStart = t  # local t and not account for scr refresh
            text_down_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_down_4, 'tStartRefresh')  # time at next scr refresh
            text_down_4.setAutoDraw(True)
        
        # *button_hello_4* updates
        if button_hello_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_hello_4.frameNStart = frameN  # exact frame index
            button_hello_4.tStart = t  # local t and not account for scr refresh
            button_hello_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_hello_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_hello_4.started')
            button_hello_4.setAutoDraw(True)
        if button_hello_4.status == STARTED:
            # check whether button_hello_4 has been pressed
            if button_hello_4.isClicked:
                if not button_hello_4.wasClicked:
                    button_hello_4.timesOn.append(button_hello_4.buttonClock.getTime()) # store time of first click
                    button_hello_4.timesOff.append(button_hello_4.buttonClock.getTime()) # store time clicked until
                else:
                    button_hello_4.timesOff[-1] = button_hello_4.buttonClock.getTime() # update time clicked until
                if not button_hello_4.wasClicked:
                    continueRoutine = False  # end routine when button_hello_4 is clicked
                    None
                button_hello_4.wasClicked = True  # if button_hello_4 is still clicked next frame, it is not a new click
            else:
                button_hello_4.wasClicked = False  # if button_hello_4 is clicked next frame, it is a new click
        else:
            button_hello_4.wasClicked = False  # if button_hello_4 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro_scoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro_score" ---
    for thisComponent in intro_scoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('intro_score_flag.routineEndVal', intro_score_flag)  # Save end routine value
    rblocks.addData('button_hello_4.numClicks', button_hello_4.numClicks)
    if button_hello_4.numClicks:
       rblocks.addData('button_hello_4.timesOn', button_hello_4.timesOn)
       rblocks.addData('button_hello_4.timesOff', button_hello_4.timesOff)
    else:
       rblocks.addData('button_hello_4.timesOn', "")
       rblocks.addData('button_hello_4.timesOff', "")
    thisExp.addData('score.routineEndVal', score)  # Save end routine value
    # the Routine "intro_score" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    C = data.TrialHandler(nReps=score_loop, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Imagenes/numerosity_condition_file.xlsx'),
        seed=None, name='C')
    thisExp.addLoop(C)  # add the loop to the experiment
    thisC = C.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisC.rgb)
    if thisC != None:
        for paramName in thisC:
            exec('{} = thisC[paramName]'.format(paramName))
    
    for thisC in C:
        currentLoop = C
        # abbreviate parameter names if possible (e.g. rgb = thisC.rgb)
        if thisC != None:
            for paramName in thisC:
                exec('{} = thisC[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "TEST_score" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        illusion_score.setImage(camino)
        # setup some python lists for storing info about the mouse_illusion_score
        mouse_illusion_score.x = []
        mouse_illusion_score.y = []
        mouse_illusion_score.leftButton = []
        mouse_illusion_score.midButton = []
        mouse_illusion_score.rightButton = []
        mouse_illusion_score.time = []
        mouse_illusion_score.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        TEST_scoreComponents = [illusion_score, LEFT_illusion_score, RIGHT_illusion_score, mouse_illusion_score]
        for thisComponent in TEST_scoreComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TEST_score" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *illusion_score* updates
            if illusion_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                illusion_score.frameNStart = frameN  # exact frame index
                illusion_score.tStart = t  # local t and not account for scr refresh
                illusion_score.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(illusion_score, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'illusion_score.started')
                illusion_score.setAutoDraw(True)
            if illusion_score.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > illusion_score.tStartRefresh + 15.0-frameTolerance:
                    # keep track of stop time/frame for later
                    illusion_score.tStop = t  # not accounting for scr refresh
                    illusion_score.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'illusion_score.stopped')
                    illusion_score.setAutoDraw(False)
            
            # *LEFT_illusion_score* updates
            if LEFT_illusion_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LEFT_illusion_score.frameNStart = frameN  # exact frame index
                LEFT_illusion_score.tStart = t  # local t and not account for scr refresh
                LEFT_illusion_score.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LEFT_illusion_score, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'LEFT_illusion_score.started')
                LEFT_illusion_score.setAutoDraw(True)
            if LEFT_illusion_score.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > LEFT_illusion_score.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    LEFT_illusion_score.tStop = t  # not accounting for scr refresh
                    LEFT_illusion_score.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'LEFT_illusion_score.stopped')
                    LEFT_illusion_score.setAutoDraw(False)
            
            # *RIGHT_illusion_score* updates
            if RIGHT_illusion_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RIGHT_illusion_score.frameNStart = frameN  # exact frame index
                RIGHT_illusion_score.tStart = t  # local t and not account for scr refresh
                RIGHT_illusion_score.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RIGHT_illusion_score, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RIGHT_illusion_score.started')
                RIGHT_illusion_score.setAutoDraw(True)
            if RIGHT_illusion_score.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RIGHT_illusion_score.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    RIGHT_illusion_score.tStop = t  # not accounting for scr refresh
                    RIGHT_illusion_score.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RIGHT_illusion_score.stopped')
                    RIGHT_illusion_score.setAutoDraw(False)
            # *mouse_illusion_score* updates
            if mouse_illusion_score.status == NOT_STARTED and t >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                mouse_illusion_score.frameNStart = frameN  # exact frame index
                mouse_illusion_score.tStart = t  # local t and not account for scr refresh
                mouse_illusion_score.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_illusion_score, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_illusion_score.started', t)
                mouse_illusion_score.status = STARTED
                mouse_illusion_score.mouseClock.reset()
                prevButtonState = mouse_illusion_score.getPressed()  # if button is down already this ISN'T a new click
            if mouse_illusion_score.status == STARTED:  # only update if started and not finished!
                buttons = mouse_illusion_score.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([LEFT_illusion, RIGHT_illusion])
                            clickableList = [LEFT_illusion, RIGHT_illusion]
                        except:
                            clickableList = [[LEFT_illusion, RIGHT_illusion]]
                        for obj in clickableList:
                            if obj.contains(mouse_illusion_score):
                                gotValidClick = True
                                mouse_illusion_score.clicked_name.append(obj.name)
                        x, y = mouse_illusion_score.getPos()
                        mouse_illusion_score.x.append(x)
                        mouse_illusion_score.y.append(y)
                        buttons = mouse_illusion_score.getPressed()
                        mouse_illusion_score.leftButton.append(buttons[0])
                        mouse_illusion_score.midButton.append(buttons[1])
                        mouse_illusion_score.rightButton.append(buttons[2])
                        mouse_illusion_score.time.append(mouse_illusion_score.mouseClock.getTime())
                        
                        continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TEST_scoreComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TEST_score" ---
        for thisComponent in TEST_scoreComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for C (TrialHandler)
        C.addData('mouse_illusion_score.x', mouse_illusion_score.x)
        C.addData('mouse_illusion_score.y', mouse_illusion_score.y)
        C.addData('mouse_illusion_score.leftButton', mouse_illusion_score.leftButton)
        C.addData('mouse_illusion_score.midButton', mouse_illusion_score.midButton)
        C.addData('mouse_illusion_score.rightButton', mouse_illusion_score.rightButton)
        C.addData('mouse_illusion_score.time', mouse_illusion_score.time)
        C.addData('mouse_illusion_score.clicked_name', mouse_illusion_score.clicked_name)
        # Run 'End Routine' code from code_score
        response = str(mouse_illusion.clicked_name)
        response = response.split("_")[0]
        response = response.replace("['", "")
        if response == correctanswer or correctanswer == "NONE":
            score = score + 1
        
        # the Routine "TEST_score" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "inter" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        inter_text.reset()
        # setup some python lists for storing info about the inter_mouse
        inter_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        interComponents = [inter_text, inter_circulo, inter_mouse, key_resp_2]
        for thisComponent in interComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "inter" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_text* updates
            if inter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_text.frameNStart = frameN  # exact frame index
                inter_text.tStart = t  # local t and not account for scr refresh
                inter_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_text, 'tStartRefresh')  # time at next scr refresh
                inter_text.setAutoDraw(True)
            
            # *inter_circulo* updates
            if inter_circulo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_circulo.frameNStart = frameN  # exact frame index
                inter_circulo.tStart = t  # local t and not account for scr refresh
                inter_circulo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_circulo, 'tStartRefresh')  # time at next scr refresh
                inter_circulo.setAutoDraw(True)
            # *inter_mouse* updates
            if inter_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_mouse.frameNStart = frameN  # exact frame index
                inter_mouse.tStart = t  # local t and not account for scr refresh
                inter_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('inter_mouse.started', t)
                inter_mouse.status = STARTED
                prevButtonState = inter_mouse.getPressed()  # if button is down already this ISN'T a new click
            if inter_mouse.status == STARTED:  # only update if started and not finished!
                buttons = inter_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(inter_circulo)
                            clickableList = inter_circulo
                        except:
                            clickableList = [inter_circulo]
                        for obj in clickableList:
                            if obj.contains(inter_mouse):
                                gotValidClick = True
                                inter_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *key_resp_2* updates
            if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in interComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "inter" ---
        for thisComponent in interComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for C (TrialHandler)
        x, y = inter_mouse.getPos()
        buttons = inter_mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(inter_circulo)
                clickableList = inter_circulo
            except:
                clickableList = [inter_circulo]
            for obj in clickableList:
                if obj.contains(inter_mouse):
                    gotValidClick = True
                    inter_mouse.clicked_name.append(obj.name)
        C.addData('inter_mouse.x', x)
        C.addData('inter_mouse.y', y)
        C.addData('inter_mouse.leftButton', buttons[0])
        C.addData('inter_mouse.midButton', buttons[1])
        C.addData('inter_mouse.rightButton', buttons[2])
        if len(inter_mouse.clicked_name):
            C.addData('inter_mouse.clicked_name', inter_mouse.clicked_name[0])
        # the Routine "inter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed score_loop repeats of 'C'
    
    
    # --- Prepare to start Routine "show_score" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    scoreTxT_2.setText('Ganancia: $' + str(score) + ' pesos')
    # keep track of which components have finished
    show_scoreComponents = [scoreTxT_2]
    for thisComponent in show_scoreComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "show_score" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *scoreTxT_2* updates
        if scoreTxT_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scoreTxT_2.frameNStart = frameN  # exact frame index
            scoreTxT_2.tStart = t  # local t and not account for scr refresh
            scoreTxT_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scoreTxT_2, 'tStartRefresh')  # time at next scr refresh
            scoreTxT_2.setAutoDraw(True)
        if scoreTxT_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > scoreTxT_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                scoreTxT_2.tStop = t  # not accounting for scr refresh
                scoreTxT_2.frameNStop = frameN  # exact frame index
                scoreTxT_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_scoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "show_score" ---
    for thisComponent in show_scoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'rblocks'


# --- Prepare to start Routine "fin" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
finComponents = [text_2, mouse]
for thisComponent in finComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "fin" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "fin" ---
for thisComponent in finComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "fin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
