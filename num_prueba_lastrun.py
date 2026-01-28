#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.5),
    on November 12, 2024, at 12:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.5'
expName = 'num_prueba'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
_loggingLevel = logging.getLevel('exp')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\MRS\\Dropbox\\MS_NumerosidadYDensidad\\num_prueba_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = True
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
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
        name='consent_si',
        depth=-1
    )
    consent_si.buttonClock = core.Clock()
    # Set experiment start values for variable component score
    score = 0
    scoreContainer = []
    
    # --- Initialize components for Routine "intro_gral" ---
    # Set experiment start values for variable component intro_gral_flag
    intro_gral_flag = 0
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
        name='button_hello_2',
        depth=-5
    )
    button_hello_2.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "TEST_illusion" ---
    illusion = visual.ImageStim(
        win=win,
        name='illusion', units='cm', 
        image='default.png', mask=None, anchor='center',
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
         win, text='Para ver la siguiente imagen\nHaz click sobre EL CIRCULO NARANJA', placeholder='Type here...', font='Calibri',
         pos=[0, 0.3],     letterHeight=0.06,
         size=(None, None), borderWidth=2.0,
         color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='inter_text',
         depth=0, autoLog=True,
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
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "intro_pastries" ---
    # Set experiment start values for variable component intro_pastries_flag
    intro_pastries_flag = 0
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
        name='button_hello_3',
        depth=-5
    )
    button_hello_3.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "TEST_illusion" ---
    illusion = visual.ImageStim(
        win=win,
        name='illusion', units='cm', 
        image='default.png', mask=None, anchor='center',
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
         win, text='Para ver la siguiente imagen\nHaz click sobre EL CIRCULO NARANJA', placeholder='Type here...', font='Calibri',
         pos=[0, 0.3],     letterHeight=0.06,
         size=(None, None), borderWidth=2.0,
         color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='inter_text',
         depth=0, autoLog=True,
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
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "intro_score" ---
    # Set experiment start values for variable component intro_score_flag
    intro_score_flag = 0
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
        name='button_hello_4',
        depth=-5
    )
    button_hello_4.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "TEST_score" ---
    illusion_score = visual.ImageStim(
        win=win,
        name='illusion_score', units='cm', 
        image='default.png', mask=None, anchor='center',
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
         win, text='Para ver la siguiente imagen\nHaz click sobre EL CIRCULO NARANJA', placeholder='Type here...', font='Calibri',
         pos=[0, 0.3],     letterHeight=0.06,
         size=(None, None), borderWidth=2.0,
         color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='inter_text',
         depth=0, autoLog=True,
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
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "fin" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Has terminado la prueba.\n¡Gracias!',
        font='Open Sans',
        pos=(0, 0.25), height=0.1, wrapWidth=None, ori=0.0, 
        color=[-0.0353, -0.1843, 0.8667], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    show_score_final = visual.TextStim(win=win, name='show_score_final',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color=[-0.0353, -0.1843, 0.8667], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "consent" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('consent.started', globalClock.getTime(format='float'))
    # reset consent_si to account for continued clicks & clear times on/off
    consent_si.reset()
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *consent_2* updates
        
        # if consent_2 is starting this frame...
        if consent_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consent_2.frameNStart = frameN  # exact frame index
            consent_2.tStart = t  # local t and not account for scr refresh
            consent_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consent_2.started')
            # update status
            consent_2.status = STARTED
            consent_2.setAutoDraw(True)
        
        # if consent_2 is active this frame...
        if consent_2.status == STARTED:
            # update params
            pass
        # *consent_si* updates
        
        # if consent_si is starting this frame...
        if consent_si.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            consent_si.frameNStart = frameN  # exact frame index
            consent_si.tStart = t  # local t and not account for scr refresh
            consent_si.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent_si, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consent_si.started')
            # update status
            consent_si.status = STARTED
            consent_si.setAutoDraw(True)
        
        # if consent_si is active this frame...
        if consent_si.status == STARTED:
            # update params
            pass
            # check whether consent_si has been pressed
            if consent_si.isClicked:
                if not consent_si.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    consent_si.timesOn.append(consent_si.buttonClock.getTime())
                    consent_si.timesOff.append(consent_si.buttonClock.getTime())
                elif len(consent_si.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    consent_si.timesOff[-1] = consent_si.buttonClock.getTime()
                if not consent_si.wasClicked:
                    # end routine when consent_si is clicked
                    continueRoutine = False
                if not consent_si.wasClicked:
                    # run callback code when consent_si is clicked
                    pass
        # take note of whether consent_si was clicked, so that next frame we know if clicks are new
        consent_si.wasClicked = consent_si.isClicked and consent_si.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
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
    thisExp.addData('consent.stopped', globalClock.getTime(format='float'))
    thisExp.addData('consent_si.numClicks', consent_si.numClicks)
    if consent_si.numClicks:
       thisExp.addData('consent_si.timesOn', consent_si.timesOn)
       thisExp.addData('consent_si.timesOff', consent_si.timesOff)
    else:
       thisExp.addData('consent_si.timesOn', "")
       thisExp.addData('consent_si.timesOff', "")
    
    thisExp.nextEntry()
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
            globals()[paramName] = thisRblock[paramName]
    
    for thisRblock in rblocks:
        currentLoop = rblocks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRblock.rgb)
        if thisRblock != None:
            for paramName in thisRblock:
                globals()[paramName] = thisRblock[paramName]
        
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
                globals()[paramName] = thisA[paramName]
        
        for thisA in A:
            currentLoop = A
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisA.rgb)
            if thisA != None:
                for paramName in thisA:
                    globals()[paramName] = thisA[paramName]
            
            # --- Prepare to start Routine "intro_gral" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('intro_gral.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_intro_gral
            if intro_gral_flag > 0:
                continueRoutine = False
            else:
                intro_gral_flag = intro_gral_flag + 1
            # reset button_hello_2 to account for continued clicks & clear times on/off
            button_hello_2.reset()
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_up_2* updates
                
                # if text_up_2 is starting this frame...
                if text_up_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_up_2.frameNStart = frameN  # exact frame index
                    text_up_2.tStart = t  # local t and not account for scr refresh
                    text_up_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_up_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_up_2.status = STARTED
                    text_up_2.setAutoDraw(True)
                
                # if text_up_2 is active this frame...
                if text_up_2.status == STARTED:
                    # update params
                    pass
                
                # *text_mid_2* updates
                
                # if text_mid_2 is starting this frame...
                if text_mid_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_mid_2.frameNStart = frameN  # exact frame index
                    text_mid_2.tStart = t  # local t and not account for scr refresh
                    text_mid_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_mid_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_mid_2.status = STARTED
                    text_mid_2.setAutoDraw(True)
                
                # if text_mid_2 is active this frame...
                if text_mid_2.status == STARTED:
                    # update params
                    pass
                
                # *text_down_2* updates
                
                # if text_down_2 is starting this frame...
                if text_down_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_down_2.frameNStart = frameN  # exact frame index
                    text_down_2.tStart = t  # local t and not account for scr refresh
                    text_down_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_down_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_down_2.status = STARTED
                    text_down_2.setAutoDraw(True)
                
                # if text_down_2 is active this frame...
                if text_down_2.status == STARTED:
                    # update params
                    pass
                # *button_hello_2* updates
                
                # if button_hello_2 is starting this frame...
                if button_hello_2.status == NOT_STARTED and tThisFlip >= 0.15-frameTolerance:
                    # keep track of start time/frame for later
                    button_hello_2.frameNStart = frameN  # exact frame index
                    button_hello_2.tStart = t  # local t and not account for scr refresh
                    button_hello_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_hello_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_hello_2.started')
                    # update status
                    button_hello_2.status = STARTED
                    button_hello_2.setAutoDraw(True)
                
                # if button_hello_2 is active this frame...
                if button_hello_2.status == STARTED:
                    # update params
                    pass
                    # check whether button_hello_2 has been pressed
                    if button_hello_2.isClicked:
                        if not button_hello_2.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_hello_2.timesOn.append(button_hello_2.buttonClock.getTime())
                            button_hello_2.timesOff.append(button_hello_2.buttonClock.getTime())
                        elif len(button_hello_2.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_hello_2.timesOff[-1] = button_hello_2.buttonClock.getTime()
                        if not button_hello_2.wasClicked:
                            # end routine when button_hello_2 is clicked
                            continueRoutine = False
                        if not button_hello_2.wasClicked:
                            # run callback code when button_hello_2 is clicked
                            pass
                # take note of whether button_hello_2 was clicked, so that next frame we know if clicks are new
                button_hello_2.wasClicked = button_hello_2.isClicked and button_hello_2.status == STARTED
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('intro_gral.stopped', globalClock.getTime(format='float'))
            
            A.addData('button_hello_2.numClicks', button_hello_2.numClicks)
            if button_hello_2.numClicks:
               A.addData('button_hello_2.timesOn', button_hello_2.timesOn)
               A.addData('button_hello_2.timesOff', button_hello_2.timesOff)
            else:
               A.addData('button_hello_2.timesOn', "")
               A.addData('button_hello_2.timesOff', "")
            # the Routine "intro_gral" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "TEST_illusion" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('TEST_illusion.started', globalClock.getTime(format='float'))
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *illusion* updates
                
                # if illusion is starting this frame...
                if illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    illusion.frameNStart = frameN  # exact frame index
                    illusion.tStart = t  # local t and not account for scr refresh
                    illusion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(illusion, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'illusion.started')
                    # update status
                    illusion.status = STARTED
                    illusion.setAutoDraw(True)
                
                # if illusion is active this frame...
                if illusion.status == STARTED:
                    # update params
                    pass
                
                # if illusion is stopping this frame...
                if illusion.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > illusion.tStartRefresh + 15.0-frameTolerance:
                        # keep track of stop time/frame for later
                        illusion.tStop = t  # not accounting for scr refresh
                        illusion.tStopRefresh = tThisFlipGlobal  # on global time
                        illusion.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'illusion.stopped')
                        # update status
                        illusion.status = FINISHED
                        illusion.setAutoDraw(False)
                
                # *LEFT_illusion* updates
                
                # if LEFT_illusion is starting this frame...
                if LEFT_illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    LEFT_illusion.frameNStart = frameN  # exact frame index
                    LEFT_illusion.tStart = t  # local t and not account for scr refresh
                    LEFT_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LEFT_illusion, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'LEFT_illusion.started')
                    # update status
                    LEFT_illusion.status = STARTED
                    LEFT_illusion.setAutoDraw(True)
                
                # if LEFT_illusion is active this frame...
                if LEFT_illusion.status == STARTED:
                    # update params
                    pass
                
                # if LEFT_illusion is stopping this frame...
                if LEFT_illusion.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LEFT_illusion.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        LEFT_illusion.tStop = t  # not accounting for scr refresh
                        LEFT_illusion.tStopRefresh = tThisFlipGlobal  # on global time
                        LEFT_illusion.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'LEFT_illusion.stopped')
                        # update status
                        LEFT_illusion.status = FINISHED
                        LEFT_illusion.setAutoDraw(False)
                
                # *RIGHT_illusion* updates
                
                # if RIGHT_illusion is starting this frame...
                if RIGHT_illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RIGHT_illusion.frameNStart = frameN  # exact frame index
                    RIGHT_illusion.tStart = t  # local t and not account for scr refresh
                    RIGHT_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RIGHT_illusion, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RIGHT_illusion.started')
                    # update status
                    RIGHT_illusion.status = STARTED
                    RIGHT_illusion.setAutoDraw(True)
                
                # if RIGHT_illusion is active this frame...
                if RIGHT_illusion.status == STARTED:
                    # update params
                    pass
                
                # if RIGHT_illusion is stopping this frame...
                if RIGHT_illusion.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RIGHT_illusion.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        RIGHT_illusion.tStop = t  # not accounting for scr refresh
                        RIGHT_illusion.tStopRefresh = tThisFlipGlobal  # on global time
                        RIGHT_illusion.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'RIGHT_illusion.stopped')
                        # update status
                        RIGHT_illusion.status = FINISHED
                        RIGHT_illusion.setAutoDraw(False)
                # *mouse_illusion* updates
                
                # if mouse_illusion is starting this frame...
                if mouse_illusion.status == NOT_STARTED and t >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_illusion.frameNStart = frameN  # exact frame index
                    mouse_illusion.tStart = t  # local t and not account for scr refresh
                    mouse_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_illusion, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_illusion.started', t)
                    # update status
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
                            clickableList = environmenttools.getFromNames([LEFT_illusion, RIGHT_illusion], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
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
                            
                            continueRoutine = False  # end routine on response
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('TEST_illusion.stopped', globalClock.getTime(format='float'))
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
            # update component parameters for each repeat
            thisExp.addData('inter.started', globalClock.getTime(format='float'))
            inter_text.reset()
            # setup some python lists for storing info about the inter_mouse
            inter_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # create starting attributes for key_resp_2
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *inter_text* updates
                
                # if inter_text is starting this frame...
                if inter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inter_text.frameNStart = frameN  # exact frame index
                    inter_text.tStart = t  # local t and not account for scr refresh
                    inter_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inter_text, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inter_text.status = STARTED
                    inter_text.setAutoDraw(True)
                
                # if inter_text is active this frame...
                if inter_text.status == STARTED:
                    # update params
                    pass
                
                # *inter_circulo* updates
                
                # if inter_circulo is starting this frame...
                if inter_circulo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inter_circulo.frameNStart = frameN  # exact frame index
                    inter_circulo.tStart = t  # local t and not account for scr refresh
                    inter_circulo.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inter_circulo, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inter_circulo.status = STARTED
                    inter_circulo.setAutoDraw(True)
                
                # if inter_circulo is active this frame...
                if inter_circulo.status == STARTED:
                    # update params
                    pass
                # *inter_mouse* updates
                
                # if inter_mouse is starting this frame...
                if inter_mouse.status == NOT_STARTED and t >= 0.01-frameTolerance:
                    # keep track of start time/frame for later
                    inter_mouse.frameNStart = frameN  # exact frame index
                    inter_mouse.tStart = t  # local t and not account for scr refresh
                    inter_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inter_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('inter_mouse.started', t)
                    # update status
                    inter_mouse.status = STARTED
                    prevButtonState = inter_mouse.getPressed()  # if button is down already this ISN'T a new click
                if inter_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = inter_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames(inter_circulo, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(inter_mouse):
                                    gotValidClick = True
                                    inter_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # end routine on response
                
                # *key_resp_2* updates
                
                # if key_resp_2 is starting this frame...
                if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    key_resp_2.clock.reset()  # now t=0
                if key_resp_2.status == STARTED:
                    theseKeys = key_resp_2.getKeys(keyList=['p'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('inter.stopped', globalClock.getTime(format='float'))
            # store data for A (TrialHandler)
            x, y = inter_mouse.getPos()
            buttons = inter_mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(inter_circulo, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
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
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed illusion_loop repeats of 'A'
        
        
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
                globals()[paramName] = thisB[paramName]
        
        for thisB in B:
            currentLoop = B
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisB.rgb)
            if thisB != None:
                for paramName in thisB:
                    globals()[paramName] = thisB[paramName]
            
            # --- Prepare to start Routine "intro_pastries" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('intro_pastries.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_intro_pastries
            if intro_pastries_flag > 0:
                continueRoutine = False
            else:
                intro_pastries_flag = intro_pastries_flag + 1
            # reset button_hello_3 to account for continued clicks & clear times on/off
            button_hello_3.reset()
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_up_3* updates
                
                # if text_up_3 is starting this frame...
                if text_up_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_up_3.frameNStart = frameN  # exact frame index
                    text_up_3.tStart = t  # local t and not account for scr refresh
                    text_up_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_up_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_up_3.status = STARTED
                    text_up_3.setAutoDraw(True)
                
                # if text_up_3 is active this frame...
                if text_up_3.status == STARTED:
                    # update params
                    pass
                
                # *text_mid_3* updates
                
                # if text_mid_3 is starting this frame...
                if text_mid_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_mid_3.frameNStart = frameN  # exact frame index
                    text_mid_3.tStart = t  # local t and not account for scr refresh
                    text_mid_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_mid_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_mid_3.status = STARTED
                    text_mid_3.setAutoDraw(True)
                
                # if text_mid_3 is active this frame...
                if text_mid_3.status == STARTED:
                    # update params
                    pass
                
                # *text_down_3* updates
                
                # if text_down_3 is starting this frame...
                if text_down_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_down_3.frameNStart = frameN  # exact frame index
                    text_down_3.tStart = t  # local t and not account for scr refresh
                    text_down_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_down_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_down_3.status = STARTED
                    text_down_3.setAutoDraw(True)
                
                # if text_down_3 is active this frame...
                if text_down_3.status == STARTED:
                    # update params
                    pass
                # *button_hello_3* updates
                
                # if button_hello_3 is starting this frame...
                if button_hello_3.status == NOT_STARTED and tThisFlip >= 0.15-frameTolerance:
                    # keep track of start time/frame for later
                    button_hello_3.frameNStart = frameN  # exact frame index
                    button_hello_3.tStart = t  # local t and not account for scr refresh
                    button_hello_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_hello_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_hello_3.started')
                    # update status
                    button_hello_3.status = STARTED
                    button_hello_3.setAutoDraw(True)
                
                # if button_hello_3 is active this frame...
                if button_hello_3.status == STARTED:
                    # update params
                    pass
                    # check whether button_hello_3 has been pressed
                    if button_hello_3.isClicked:
                        if not button_hello_3.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_hello_3.timesOn.append(button_hello_3.buttonClock.getTime())
                            button_hello_3.timesOff.append(button_hello_3.buttonClock.getTime())
                        elif len(button_hello_3.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_hello_3.timesOff[-1] = button_hello_3.buttonClock.getTime()
                        if not button_hello_3.wasClicked:
                            # end routine when button_hello_3 is clicked
                            continueRoutine = False
                        if not button_hello_3.wasClicked:
                            # run callback code when button_hello_3 is clicked
                            pass
                # take note of whether button_hello_3 was clicked, so that next frame we know if clicks are new
                button_hello_3.wasClicked = button_hello_3.isClicked and button_hello_3.status == STARTED
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('intro_pastries.stopped', globalClock.getTime(format='float'))
            
            B.addData('button_hello_3.numClicks', button_hello_3.numClicks)
            if button_hello_3.numClicks:
               B.addData('button_hello_3.timesOn', button_hello_3.timesOn)
               B.addData('button_hello_3.timesOff', button_hello_3.timesOff)
            else:
               B.addData('button_hello_3.timesOn', "")
               B.addData('button_hello_3.timesOff', "")
            # the Routine "intro_pastries" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "TEST_illusion" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('TEST_illusion.started', globalClock.getTime(format='float'))
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *illusion* updates
                
                # if illusion is starting this frame...
                if illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    illusion.frameNStart = frameN  # exact frame index
                    illusion.tStart = t  # local t and not account for scr refresh
                    illusion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(illusion, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'illusion.started')
                    # update status
                    illusion.status = STARTED
                    illusion.setAutoDraw(True)
                
                # if illusion is active this frame...
                if illusion.status == STARTED:
                    # update params
                    pass
                
                # if illusion is stopping this frame...
                if illusion.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > illusion.tStartRefresh + 15.0-frameTolerance:
                        # keep track of stop time/frame for later
                        illusion.tStop = t  # not accounting for scr refresh
                        illusion.tStopRefresh = tThisFlipGlobal  # on global time
                        illusion.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'illusion.stopped')
                        # update status
                        illusion.status = FINISHED
                        illusion.setAutoDraw(False)
                
                # *LEFT_illusion* updates
                
                # if LEFT_illusion is starting this frame...
                if LEFT_illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    LEFT_illusion.frameNStart = frameN  # exact frame index
                    LEFT_illusion.tStart = t  # local t and not account for scr refresh
                    LEFT_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LEFT_illusion, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'LEFT_illusion.started')
                    # update status
                    LEFT_illusion.status = STARTED
                    LEFT_illusion.setAutoDraw(True)
                
                # if LEFT_illusion is active this frame...
                if LEFT_illusion.status == STARTED:
                    # update params
                    pass
                
                # if LEFT_illusion is stopping this frame...
                if LEFT_illusion.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LEFT_illusion.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        LEFT_illusion.tStop = t  # not accounting for scr refresh
                        LEFT_illusion.tStopRefresh = tThisFlipGlobal  # on global time
                        LEFT_illusion.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'LEFT_illusion.stopped')
                        # update status
                        LEFT_illusion.status = FINISHED
                        LEFT_illusion.setAutoDraw(False)
                
                # *RIGHT_illusion* updates
                
                # if RIGHT_illusion is starting this frame...
                if RIGHT_illusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RIGHT_illusion.frameNStart = frameN  # exact frame index
                    RIGHT_illusion.tStart = t  # local t and not account for scr refresh
                    RIGHT_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RIGHT_illusion, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RIGHT_illusion.started')
                    # update status
                    RIGHT_illusion.status = STARTED
                    RIGHT_illusion.setAutoDraw(True)
                
                # if RIGHT_illusion is active this frame...
                if RIGHT_illusion.status == STARTED:
                    # update params
                    pass
                
                # if RIGHT_illusion is stopping this frame...
                if RIGHT_illusion.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RIGHT_illusion.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        RIGHT_illusion.tStop = t  # not accounting for scr refresh
                        RIGHT_illusion.tStopRefresh = tThisFlipGlobal  # on global time
                        RIGHT_illusion.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'RIGHT_illusion.stopped')
                        # update status
                        RIGHT_illusion.status = FINISHED
                        RIGHT_illusion.setAutoDraw(False)
                # *mouse_illusion* updates
                
                # if mouse_illusion is starting this frame...
                if mouse_illusion.status == NOT_STARTED and t >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_illusion.frameNStart = frameN  # exact frame index
                    mouse_illusion.tStart = t  # local t and not account for scr refresh
                    mouse_illusion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_illusion, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_illusion.started', t)
                    # update status
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
                            clickableList = environmenttools.getFromNames([LEFT_illusion, RIGHT_illusion], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
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
                            
                            continueRoutine = False  # end routine on response
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('TEST_illusion.stopped', globalClock.getTime(format='float'))
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
            # update component parameters for each repeat
            thisExp.addData('inter.started', globalClock.getTime(format='float'))
            inter_text.reset()
            # setup some python lists for storing info about the inter_mouse
            inter_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # create starting attributes for key_resp_2
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *inter_text* updates
                
                # if inter_text is starting this frame...
                if inter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inter_text.frameNStart = frameN  # exact frame index
                    inter_text.tStart = t  # local t and not account for scr refresh
                    inter_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inter_text, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inter_text.status = STARTED
                    inter_text.setAutoDraw(True)
                
                # if inter_text is active this frame...
                if inter_text.status == STARTED:
                    # update params
                    pass
                
                # *inter_circulo* updates
                
                # if inter_circulo is starting this frame...
                if inter_circulo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inter_circulo.frameNStart = frameN  # exact frame index
                    inter_circulo.tStart = t  # local t and not account for scr refresh
                    inter_circulo.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inter_circulo, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inter_circulo.status = STARTED
                    inter_circulo.setAutoDraw(True)
                
                # if inter_circulo is active this frame...
                if inter_circulo.status == STARTED:
                    # update params
                    pass
                # *inter_mouse* updates
                
                # if inter_mouse is starting this frame...
                if inter_mouse.status == NOT_STARTED and t >= 0.01-frameTolerance:
                    # keep track of start time/frame for later
                    inter_mouse.frameNStart = frameN  # exact frame index
                    inter_mouse.tStart = t  # local t and not account for scr refresh
                    inter_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inter_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('inter_mouse.started', t)
                    # update status
                    inter_mouse.status = STARTED
                    prevButtonState = inter_mouse.getPressed()  # if button is down already this ISN'T a new click
                if inter_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = inter_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames(inter_circulo, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(inter_mouse):
                                    gotValidClick = True
                                    inter_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # end routine on response
                
                # *key_resp_2* updates
                
                # if key_resp_2 is starting this frame...
                if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    key_resp_2.clock.reset()  # now t=0
                if key_resp_2.status == STARTED:
                    theseKeys = key_resp_2.getKeys(keyList=['p'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('inter.stopped', globalClock.getTime(format='float'))
            # store data for B (TrialHandler)
            x, y = inter_mouse.getPos()
            buttons = inter_mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(inter_circulo, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
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
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed galletas_loop repeats of 'B'
        
        
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
                globals()[paramName] = thisC[paramName]
        
        for thisC in C:
            currentLoop = C
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisC.rgb)
            if thisC != None:
                for paramName in thisC:
                    globals()[paramName] = thisC[paramName]
            
            # --- Prepare to start Routine "intro_score" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('intro_score.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_intro_score
            if intro_score_flag > 0:
                continueRoutine = False
            else:
                intro_score_flag = intro_score_flag + 1
            # reset button_hello_4 to account for continued clicks & clear times on/off
            button_hello_4.reset()
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_up_4* updates
                
                # if text_up_4 is starting this frame...
                if text_up_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_up_4.frameNStart = frameN  # exact frame index
                    text_up_4.tStart = t  # local t and not account for scr refresh
                    text_up_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_up_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_up_4.status = STARTED
                    text_up_4.setAutoDraw(True)
                
                # if text_up_4 is active this frame...
                if text_up_4.status == STARTED:
                    # update params
                    pass
                
                # *text_mid_4* updates
                
                # if text_mid_4 is starting this frame...
                if text_mid_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_mid_4.frameNStart = frameN  # exact frame index
                    text_mid_4.tStart = t  # local t and not account for scr refresh
                    text_mid_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_mid_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_mid_4.status = STARTED
                    text_mid_4.setAutoDraw(True)
                
                # if text_mid_4 is active this frame...
                if text_mid_4.status == STARTED:
                    # update params
                    pass
                
                # *text_down_4* updates
                
                # if text_down_4 is starting this frame...
                if text_down_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_down_4.frameNStart = frameN  # exact frame index
                    text_down_4.tStart = t  # local t and not account for scr refresh
                    text_down_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_down_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_down_4.status = STARTED
                    text_down_4.setAutoDraw(True)
                
                # if text_down_4 is active this frame...
                if text_down_4.status == STARTED:
                    # update params
                    pass
                # *button_hello_4* updates
                
                # if button_hello_4 is starting this frame...
                if button_hello_4.status == NOT_STARTED and tThisFlip >= 0.15-frameTolerance:
                    # keep track of start time/frame for later
                    button_hello_4.frameNStart = frameN  # exact frame index
                    button_hello_4.tStart = t  # local t and not account for scr refresh
                    button_hello_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button_hello_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_hello_4.started')
                    # update status
                    button_hello_4.status = STARTED
                    button_hello_4.setAutoDraw(True)
                
                # if button_hello_4 is active this frame...
                if button_hello_4.status == STARTED:
                    # update params
                    pass
                    # check whether button_hello_4 has been pressed
                    if button_hello_4.isClicked:
                        if not button_hello_4.wasClicked:
                            # if this is a new click, store time of first click and clicked until
                            button_hello_4.timesOn.append(button_hello_4.buttonClock.getTime())
                            button_hello_4.timesOff.append(button_hello_4.buttonClock.getTime())
                        elif len(button_hello_4.timesOff):
                            # if click is continuing from last frame, update time of clicked until
                            button_hello_4.timesOff[-1] = button_hello_4.buttonClock.getTime()
                        if not button_hello_4.wasClicked:
                            # end routine when button_hello_4 is clicked
                            continueRoutine = False
                        if not button_hello_4.wasClicked:
                            # run callback code when button_hello_4 is clicked
                            pass
                # take note of whether button_hello_4 was clicked, so that next frame we know if clicks are new
                button_hello_4.wasClicked = button_hello_4.isClicked and button_hello_4.status == STARTED
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('intro_score.stopped', globalClock.getTime(format='float'))
            
            C.addData('button_hello_4.numClicks', button_hello_4.numClicks)
            if button_hello_4.numClicks:
               C.addData('button_hello_4.timesOn', button_hello_4.timesOn)
               C.addData('button_hello_4.timesOff', button_hello_4.timesOff)
            else:
               C.addData('button_hello_4.timesOn', "")
               C.addData('button_hello_4.timesOff', "")
            # the Routine "intro_score" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "TEST_score" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('TEST_score.started', globalClock.getTime(format='float'))
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *illusion_score* updates
                
                # if illusion_score is starting this frame...
                if illusion_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    illusion_score.frameNStart = frameN  # exact frame index
                    illusion_score.tStart = t  # local t and not account for scr refresh
                    illusion_score.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(illusion_score, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'illusion_score.started')
                    # update status
                    illusion_score.status = STARTED
                    illusion_score.setAutoDraw(True)
                
                # if illusion_score is active this frame...
                if illusion_score.status == STARTED:
                    # update params
                    pass
                
                # if illusion_score is stopping this frame...
                if illusion_score.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > illusion_score.tStartRefresh + 15.0-frameTolerance:
                        # keep track of stop time/frame for later
                        illusion_score.tStop = t  # not accounting for scr refresh
                        illusion_score.tStopRefresh = tThisFlipGlobal  # on global time
                        illusion_score.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'illusion_score.stopped')
                        # update status
                        illusion_score.status = FINISHED
                        illusion_score.setAutoDraw(False)
                
                # *LEFT_illusion_score* updates
                
                # if LEFT_illusion_score is starting this frame...
                if LEFT_illusion_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    LEFT_illusion_score.frameNStart = frameN  # exact frame index
                    LEFT_illusion_score.tStart = t  # local t and not account for scr refresh
                    LEFT_illusion_score.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LEFT_illusion_score, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'LEFT_illusion_score.started')
                    # update status
                    LEFT_illusion_score.status = STARTED
                    LEFT_illusion_score.setAutoDraw(True)
                
                # if LEFT_illusion_score is active this frame...
                if LEFT_illusion_score.status == STARTED:
                    # update params
                    pass
                
                # if LEFT_illusion_score is stopping this frame...
                if LEFT_illusion_score.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LEFT_illusion_score.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        LEFT_illusion_score.tStop = t  # not accounting for scr refresh
                        LEFT_illusion_score.tStopRefresh = tThisFlipGlobal  # on global time
                        LEFT_illusion_score.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'LEFT_illusion_score.stopped')
                        # update status
                        LEFT_illusion_score.status = FINISHED
                        LEFT_illusion_score.setAutoDraw(False)
                
                # *RIGHT_illusion_score* updates
                
                # if RIGHT_illusion_score is starting this frame...
                if RIGHT_illusion_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RIGHT_illusion_score.frameNStart = frameN  # exact frame index
                    RIGHT_illusion_score.tStart = t  # local t and not account for scr refresh
                    RIGHT_illusion_score.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RIGHT_illusion_score, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RIGHT_illusion_score.started')
                    # update status
                    RIGHT_illusion_score.status = STARTED
                    RIGHT_illusion_score.setAutoDraw(True)
                
                # if RIGHT_illusion_score is active this frame...
                if RIGHT_illusion_score.status == STARTED:
                    # update params
                    pass
                
                # if RIGHT_illusion_score is stopping this frame...
                if RIGHT_illusion_score.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RIGHT_illusion_score.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        RIGHT_illusion_score.tStop = t  # not accounting for scr refresh
                        RIGHT_illusion_score.tStopRefresh = tThisFlipGlobal  # on global time
                        RIGHT_illusion_score.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'RIGHT_illusion_score.stopped')
                        # update status
                        RIGHT_illusion_score.status = FINISHED
                        RIGHT_illusion_score.setAutoDraw(False)
                # *mouse_illusion_score* updates
                
                # if mouse_illusion_score is starting this frame...
                if mouse_illusion_score.status == NOT_STARTED and t >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_illusion_score.frameNStart = frameN  # exact frame index
                    mouse_illusion_score.tStart = t  # local t and not account for scr refresh
                    mouse_illusion_score.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_illusion_score, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_illusion_score.started', t)
                    # update status
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
                            clickableList = environmenttools.getFromNames([LEFT_illusion, RIGHT_illusion], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
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
                            
                            continueRoutine = False  # end routine on response
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('TEST_score.stopped', globalClock.getTime(format='float'))
            # store data for C (TrialHandler)
            C.addData('mouse_illusion_score.x', mouse_illusion_score.x)
            C.addData('mouse_illusion_score.y', mouse_illusion_score.y)
            C.addData('mouse_illusion_score.leftButton', mouse_illusion_score.leftButton)
            C.addData('mouse_illusion_score.midButton', mouse_illusion_score.midButton)
            C.addData('mouse_illusion_score.rightButton', mouse_illusion_score.rightButton)
            C.addData('mouse_illusion_score.time', mouse_illusion_score.time)
            C.addData('mouse_illusion_score.clicked_name', mouse_illusion_score.clicked_name)
            # Run 'End Routine' code from code_score
            response = str(mouse_illusion_score.clicked_name)
            response = response.split("_")[0]
            response = response.replace("['", "")
            if response == correctanswer or correctanswer == "NONE":
                score = score + 1
                
            print(score)
            # the Routine "TEST_score" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "inter" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('inter.started', globalClock.getTime(format='float'))
            inter_text.reset()
            # setup some python lists for storing info about the inter_mouse
            inter_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # create starting attributes for key_resp_2
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *inter_text* updates
                
                # if inter_text is starting this frame...
                if inter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inter_text.frameNStart = frameN  # exact frame index
                    inter_text.tStart = t  # local t and not account for scr refresh
                    inter_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inter_text, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inter_text.status = STARTED
                    inter_text.setAutoDraw(True)
                
                # if inter_text is active this frame...
                if inter_text.status == STARTED:
                    # update params
                    pass
                
                # *inter_circulo* updates
                
                # if inter_circulo is starting this frame...
                if inter_circulo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inter_circulo.frameNStart = frameN  # exact frame index
                    inter_circulo.tStart = t  # local t and not account for scr refresh
                    inter_circulo.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inter_circulo, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inter_circulo.status = STARTED
                    inter_circulo.setAutoDraw(True)
                
                # if inter_circulo is active this frame...
                if inter_circulo.status == STARTED:
                    # update params
                    pass
                # *inter_mouse* updates
                
                # if inter_mouse is starting this frame...
                if inter_mouse.status == NOT_STARTED and t >= 0.01-frameTolerance:
                    # keep track of start time/frame for later
                    inter_mouse.frameNStart = frameN  # exact frame index
                    inter_mouse.tStart = t  # local t and not account for scr refresh
                    inter_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inter_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('inter_mouse.started', t)
                    # update status
                    inter_mouse.status = STARTED
                    prevButtonState = inter_mouse.getPressed()  # if button is down already this ISN'T a new click
                if inter_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = inter_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames(inter_circulo, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(inter_mouse):
                                    gotValidClick = True
                                    inter_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # end routine on response
                
                # *key_resp_2* updates
                
                # if key_resp_2 is starting this frame...
                if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    key_resp_2.clock.reset()  # now t=0
                if key_resp_2.status == STARTED:
                    theseKeys = key_resp_2.getKeys(keyList=['p'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('inter.stopped', globalClock.getTime(format='float'))
            # store data for C (TrialHandler)
            x, y = inter_mouse.getPos()
            buttons = inter_mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(inter_circulo, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
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
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed score_loop repeats of 'C'
        
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'rblocks'
    
    
    # --- Prepare to start Routine "fin" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fin.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from code
    print("fin")
    print(score)
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    show_score_final.setText('Ganancia: $' + str(score) + ' pesos')
    # keep track of which components have finished
    finComponents = [text_2, mouse, show_score_final]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    continueRoutine = False  # end routine on response        
        # *show_score_final* updates
        
        # if show_score_final is starting this frame...
        if show_score_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            show_score_final.frameNStart = frameN  # exact frame index
            show_score_final.tStart = t  # local t and not account for scr refresh
            show_score_final.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(show_score_final, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'show_score_final.started')
            # update status
            show_score_final.status = STARTED
            show_score_final.setAutoDraw(True)
        
        # if show_score_final is active this frame...
        if show_score_final.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
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
    thisExp.addData('fin.stopped', globalClock.getTime(format='float'))
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
    
    
    
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
