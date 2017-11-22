#test read midi files

from utils import *


# def printChordToFiles(components):
#      startPiano = False
#      for component in components:
#          if component.names['en'][0] == 'Piano':
#             startPiano = True
#          if type(component) is music21.chord.Chord:

import os
# for file in os.listdir("data/MIDI"):
#     if file.endswith(".mid"):
#         path = os.path.join("data/MIDI", file)
#         print(path)
#         printPianoChordSequence(path)

#components= readMidiFile('data/LetItBe.mid')
# path = 'data/Imagine.mid'
# printPianoChordSequence(path)
#printPianoChord(path.split(".mid")[0] + "_chord.txt")

import os
for file in os.listdir("data/CHORDS/test"):
    if file.endswith(".txt"):
        path = os.path.join("data/CHORDS/test", file)
        print(path)
        #extractNodeChord(path, None)
        extractNodeSimpleChord(path, 20)




