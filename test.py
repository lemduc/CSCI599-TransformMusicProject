#test read midi files



from utils import *
from joblib import Parallel, delayed
from joblib.pool import has_shareable_memory

# def printChordToFiles(components):
#      startPiano = False
#      for component in components:
#          if component.names['en'][0] == 'Piano':
#             startPiano = True
#          if type(component) is music21.chord.Chord:

import os
for file in os.listdir("data/MIDI"):
    if file.endswith(".mid"):
        path = os.path.join("data/MIDI", file)
        print(path)
        printPianoChordSequence(path)

#components= readMidiFile('data/LetItBe.mid')
# path = 'data/Imagine.mid'
# printPianoChordSequence(path)
#printPianoChord(path.split(".mid")[0] + "_chord.txt")
#extractNodeChord('data/Imagine_chord.txt')


