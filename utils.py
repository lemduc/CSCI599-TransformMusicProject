import music21
from music21 import converter,instrument # or import *

def readMidiFile(file_path):
    file = converter.parse(file_path)
    components = []
    for element in file.recurse():
        components.append(element)
    return components


def printPianoChordSequence(file_path):
    components = readMidiFile(file_path=file_path)
    startPiano = False
    printRatio = True
    printHighest = True
    for component in components:

        if hasattr(component, 'instrumentName') and component.instrumentName == 'Piano':
            startPiano = True
        elif hasattr(component, 'instrumentName') and not component.instrumentName == 'Piano':
            startPiano = False
        if startPiano and type(component) is music21.chord.Chord:
            print(component.fullName + "," + component.commonName + "," + str(component.beatStrength) + "," + str(
                component.offset))
        elif type(component) is music21.meter.TimeSignature and printRatio:
            print component.ratioString
            printRatio = False
        elif type(component) is music21.stream.Score and printHighest:
            print component.highestTime
            printHighest = False





