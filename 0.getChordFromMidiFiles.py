from utils import *

# for file in os.listdir("data/MIDI_1"):
#     if file.endswith(".mid"):
#         path = os.path.join("data/MIDI_1", file)
#         print(path)
#         printPianoChordSequence(path)
#
#
# for file in os.listdir("data/MIDI_2"):
#     if file.endswith(".mid"):
#         path = os.path.join("data/MIDI_2", file)
#         print(path)
#         printPianoChordSequence(path)
#
# for file in os.listdir("data/MidKar"):
#     if file.endswith(".mid"):
#         path = os.path.join("data/MidKar", file)
#         print(path)
#         printPianoChordSequence(path)

for file in os.listdir("data/standard-jazz1"):
    if file.endswith(".mid"):
        path = os.path.join("data/standard-jazz1", file)
        print(path)
        printPianoChordSequence(path)

