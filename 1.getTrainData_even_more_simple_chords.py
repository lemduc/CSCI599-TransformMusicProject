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

# extract train
SPLIT_LENGTH = 20
DIR_PREFIX = "data/CHORDS_track0/"

type = "train"
for file in os.listdir("data/"+type):
    if file.endswith(".txt"):
        path = os.path.join("data/"+type, file)
        print(path)
        #extractNodeChord(path, None)
        extractNodeMoreSimpleChord(path, 20, type)
        #extractDuration(path, 20, type)

# extract dev
type = "test"
for file in os.listdir("data/"+type):
    if file.endswith(".txt"):
        path = os.path.join("data/"+type, file)
        print(path)
        #extractNodeChord(path, None)
        extractNodeMoreSimpleChord(path, 20, type)
        #extractDuration(path, 20, type)

# extract test
type = "dev"
for file in os.listdir("data/"+type):
    if file.endswith(".txt"):
        path = os.path.join("data/"+type, file)
        print(path)
        #extractNodeChord(path, None)
        extractNodeMoreSimpleChord(path, 20, type)
        #extractDuration(path, 20, type)

for file in os.listdir(DIR_PREFIX + type):
    if file.endswith(".txt"):
        path = os.path.join(DIR_PREFIX + type, file)
        print(path)
        #extractNodeChord(path, None)
        extractNodeMoreSimpleChord(path, SPLIT_LENGTH, type)
        extractDuration(path, SPLIT_LENGTH, type)

# extract dev
type = "test"
for file in os.listdir(DIR_PREFIX + type):
    if file.endswith(".txt"):
        path = os.path.join(DIR_PREFIX + type, file)
        print(path)
        #extractNodeChord(path, None)
        extractNodeMoreSimpleChord(path, SPLIT_LENGTH, type)
        extractDuration(path, SPLIT_LENGTH, type)

# extract test
type = "dev"
for file in os.listdir(DIR_PREFIX + type):
    if file.endswith(".txt"):
        path = os.path.join(DIR_PREFIX + type, file)
        print(path)
        #extractNodeChord(path, None)
        extractNodeMoreSimpleChord(path, SPLIT_LENGTH, type)
        extractDuration(path, SPLIT_LENGTH, type)


