import music21
from music21 import converter,instrument # or import *

def readMidiFile(file_path):
    file = converter.parse(file_path)
    components = []
    for element in file.recurse():
        components.append(element)
    return components

def getChordSequence(file_path):
    components = readMidiFile(file_path=file_path)
    chord_sequence = []
    for component in components:
        if type(component) is music21.chord.Chord:
            chord_sequence.append(component)
    return chord_sequence



