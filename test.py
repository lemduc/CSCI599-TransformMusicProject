#test read midi files
from os import *


from utils import *

# def printChordToFiles(components):
#      startPiano = False
#      for component in components:
#          if component.names['en'][0] == 'Piano':
#             startPiano = True
#          if type(component) is music21.chord.Chord:

for file in os.listdir("data/MIDI"):
    if file.endswith(".mid"):
        path = os.path.join("data/MIDI", file)
        print(path)
        printPianoChordSequence(path)

#extractNodeChordToFile("data/CHORDS/old/accustomed_chord.txt","chordTest1.chord","noteTest1.note")
#components= readMidiFile('data/LetItBe.mid')
# path = 'data/Imagine.mid'
# printPianoChordSequence(path)
#printPianoChord(path.split(".mid")[0] + "_chord.txt")
#extractNodeChord('data/Imagine_chord.txt')
#note = convertToNote('B-flat_in_octave_1_')
#print(note.name)
#newComponents = testMidiFile('imagine/Imagine.mid','test_data/imagine.node')
#print(newComponents)
#writeComponentsToMidiFile(newComponents,'imagine/Imagine_jazz2.mid')

#removeDuplicateChordinVocab('chord_20_data/vocab.chord')
#removeDuplicateChordinVocab('chord_20_data/vocab.node')

#extractChordToFileFromMidi('imagine/Imagine.mid', 20, 'imagine.chord')

#readMidiFile2('imagine/Imagine.mid')

testMidiFile2('imagine/Imagine.mid', 'test_data/imagine.node','test_data/Imagine_jazz2.mid')