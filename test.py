#test read midi files



from utils import *


 # def printChordToFiles(components):
 #     startPiano = False
 #     for component in components:
 #         if component.names['en'][0] == 'Piano':
 #            startPiano = True
 #         if type(component) is music21.chord.Chord:


#components= readMidiFile('data/LetItBe.mid')
path = 'data/Imagine.mid'
printPianoChordSequence(path)
printPianoChord(path.split(".mid")[0] + "_chord.txt")
