from utils import *

for file in os.listdir("data/MIDI"):
    if file.endswith(".mid"):
        path = os.path.join("data/MIDI", file)
        print(path)
        printPianoChordSequence(path)

