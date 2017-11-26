from utils import *

folder_name = "midkar2"

for file in os.listdir("data/" + folder_name):
    if file.endswith(".mid"):
        path = os.path.join("data/"+ folder_name, file)
        print(path)
        printPianoChordSequence(path)

