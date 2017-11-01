#test read midi files



from utils import *

chord_sequence  = getChordSequence('data/4on6.mid')
for chord in chord_sequence:
    print chord.fullName