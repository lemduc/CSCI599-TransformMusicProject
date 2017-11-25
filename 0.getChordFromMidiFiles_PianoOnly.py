from utils import *

for file in os.listdir("data/midkar"):
    if file.endswith(".mid"):
        path = os.path.join("data/midkar", file)
        print(path)
        printPianoChordSequence(path)

