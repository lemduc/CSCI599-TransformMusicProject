#test read midi files



from utils import *


 # def printChordToFiles(components):
 #     startPiano = False
 #     for component in components:
 #         if component.names['en'][0] == 'Piano':
 #            startPiano = True
 #         if type(component) is music21.chord.Chord:


#components= readMidiFile('data/LetItBe.mid')
printPianoChordSequence('data/LetItBe.mid')

