import music21
from music21 import converter,instrument # or import *

from collections import Counter, defaultdict
from sklearn.cluster import KMeans
#from mingus.midi import fluidsynth
#from mingus.containers import NoteContainer
#import mingus.containers
import mingus.core.value as value
import pandas as pd
import numpy as np
import sys, re, itertools, random
#fluidsynth.init('piano.SF2',"alsa")

def readMidiFile(file_path):
    file = converter.parse(file_path)
    components = []
    # select the first channels
    for element in file[0].recurse():
        components.append(element)
    return components


def printPianoChordSequence(file_path):
    components = readMidiFile(file_path=file_path)
    startPiano = True #False
    printRatio = True
    printHighest = True
    printColumns = True
    output = ""
    notes = ""
    chords = ""
    for component in components:

        # if hasattr(component, 'instrumentName') and component.instrumentName == 'Piano':
        #     startPiano = True
        # elif hasattr(component, 'instrumentName') and not component.instrumentName == 'Piano':
        #     startPiano = False
        if startPiano and type(component) is music21.chord.Chord:
            tmp = component.fullName + "," + component.pitchedCommonName + "," + str(component.quarterLength) + "," + str(
                component.offset)
            output += tmp + "\n"
            print(tmp)
        elif type(component) is music21.meter.TimeSignature and printRatio:
            tmp = str(component.ratioString)
            output += tmp + "\n"
            print(tmp)
            printRatio = False
        elif type(component) is music21.stream.Score and printHighest:
            tmp = component.highestTime
            output += str(tmp) + "\n"
            print(tmp)
            printHighest = False
        elif not printHighest and not printRatio and printColumns:
            tmp = "FullName,CommonName,Len,Offset"
            output += tmp + "\n"
            print(tmp)
            printColumns = False
            # Write chords out into cleaned-up version of Oscar's chords

    with open((file_path.split(".mid")[0] + "_chord.txt").replace("MIDI", "CHORDS"), 'w') as f:
       f.write(output)

def printPianoChord(file_path):
    # Import the chord data.
    allchords = pd.read_csv(file_path, skiprows=2)[:].sort_values("Offset")
    allchords.index = range(1, len(allchords) + 1)
    with open(file_path, 'r') as f:
        metmark = float(f.readline())
        tsig_num, tsig_den = [i for i in f.readline().replace(' /', '').split()]

    print
    "Metronome, Timesig Numerator, Timesig Denominator, # chords played"
    print
    metmark, tsig_num, tsig_den, len(allchords)
    allchords.sort_values(by="Offset", ascending=True)[:10]
    allchords.head()

    oscarchords = getChords(allchords)
    print(len(oscarchords))
    oscarchords[:10]

    # Write chords out into cleaned-up version of Oscar's chords
    with open(file_path.split(".txt")[0] + "_extract.txt", 'w') as f:
        for chord in oscarchords:
            for n in chord:
                f.write(n)
                f.write(' ')
            f.write('\n')

# Convert music21 note to mingus note.
# This version (different from that in 3. Play Notes)
# doesn't return a Note object: returns a string.
def mingifytext(note):
    accidental = re.compile("[A-Z](-|#)[0-9]")
    if accidental.match(note):
        if '-' not in note: note = "%s%s-%s" % (note[0], note[1], note[2])
        else: note = note.replace('-', 'b-')
    else: note = "%s-%s" % (note[0], note[1])
    return note

# Given a MUSIC21 note, such as C5 or D#7, convert it
# into a note on the keyboard between 0 and 87 inclusive.
# Don't convert it for mingus; try to use music21 note style
# as much as possible for all this stuff.
def quantify(note):
    notevals = {
        'C' : 0,
        'D' : 2,
        'E' : 4,
        'F' : 5,
        'G' : 7,
        'A' : 9,
        'B' : 11
    }
    quantized = 0
    octave = int(note[-1]) - 1
    for i in note[:-1]:
        if i in notevals: quantized += notevals[i]
        if i == '-': quantized -= 1
        if i == '#': quantized += 1
    quantized += 12 * octave
    return quantized

# Extract notes in chords.
# Shorter single-note chords: lowest prob of being played
def getChords(allchords, mingify=True):
    chords_poss = []
    for chordname in allchords['FullName']:
        notenames = re.findall("[CDEFGAB]+[-]*[sharp|flat]*[in octave]*[1-9]", chordname)
        for ix in range(len(notenames)):
            notenames[ix] = notenames[ix].replace(" in octave ", '').replace("-sharp","#").replace("-flat","-")
        if mingify==True:
            notenames = [mingifytext(note) for note in notenames]
        else:
            notenames = [note for note in notenames]
        toDel = [ix for ix in range(len(notenames)) if "6" in notenames[ix]
                 or "5" in notenames[ix]] # rm chords with notes too high, e.g. oct == 6 or 5
        notenames = [i for ix, i in enumerate(notenames) if ix not in toDel]
        if len(notenames) > 2: # min num of notes in valid chord = 3. Can change this
            chords_poss.append(sorted(notenames)) # important to sort, else can't find duplicates
    result = sorted(list(chords_poss for chords_poss,_ in itertools.groupby(chords_poss)))
    result = list(result for result,_ in itertools.groupby(result))
    return result

def extractNodeChord(file_path, split_length):
    read_data = None
    full_name = ""
    common_name = ""
    count_length = 0
    with open(file_path, 'r') as f:
        read_data = f.readlines()
    for line in read_data[1:]:
        count_length += 1
        sl = line.split(",")
        i  = sl[0].index("{")
        j  = sl[0].index("}")
        full_name += sl[0][i:j+1].replace(" ", "_") + " "
        common_name += sl[1].replace(" ", "_") + " "
        if split_length is not None and count_length == split_length:
            full_name += "\n"
            common_name += "\n"
            count_length = 0


    with open("train_nodes.txt", 'a') as f:
        f.write(full_name + '\n')
    with open("train_ch.txt", 'a') as f:
        f.write(common_name + '\n')

def extractNodeChordToFile(file_path, chordFile,noteFile):
    read_data = None
    full_name = ""
    common_name = ""
    with open(file_path, 'r') as f:
        read_data = f.readlines()
    for line in read_data[1:]:
        sl = line.split(",")
        i = sl[0].index("{")
        j = sl[0].index("}")
        full_name += sl[0][i:j + 1].replace(" ", "_") + " "
        common_name += sl[1].replace(" ", "_") + " "

    with open(chordFile, 'a') as f:
        f.write(full_name + '\n')
    with open(noteFile, 'a') as f:
        f.write(common_name + '\n')

def convertToNote(str_note):
    str_note = str_note.replace("_"," ")
    str_note = str_note.strip()
    note = str_note[0]
    is_sharp = False
    is_flat = False
    if("sharp" in str_note):
        is_sharp = True
    if "flat" in str_note:
        is_flat = True
    index_octave = str_note.index("octave") + 7
    octave = str_note[index_octave:(index_octave+1)]
    if is_flat:
        note =  note + "-"
    elif is_sharp:
        note = note + "#"
    note = note + octave
    print("str_note="+str_note)
    print("note ="+note)
    return music21.note.Note(nameWithOctave=note)

def writeComponentsToMidiFile(components, outputFile):
    s = music21.stream.Stream()
    for component in components:
        s.repeatAppend(component,1)
    mf = music21.midi.translate.streamToMidiFile(s)
    mf.open(outputFile, 'wb')
    mf.write()
    mf.close()

def testMidiFile(midiFilePath, translatedChordListFile):
    components = readMidiFile(midiFilePath)
    chords = []
    with open(translatedChordListFile, 'r') as f:

        for line in f:
            line = line.strip()
            str_chords = line.split(" ")
            for str_chord in str_chords:
                str_notes = str_chord.replace("{","").replace("}","").split("|")
                notes =[]
                for str_note in str_notes:
                    note = convertToNote(str_note)
                    notes.append(note)
                chord = music21.chord.Chord(notes)
                chords.append(chord)
    new_components = []
    count = 0
    for component in components:
        if not type(component) is music21.chord.Chord:
            new_components.append(component)
        else:
            if count < len(chords):
                chords[count].duration = component.duration
                chords[count].quarterLength = component.quarterLength
                new_components.append(chords[count])

    return new_components




def matchTestChordFile(originalChordFile, translatedChordFile):
    output = []
    origLines = []
    with open(originalChordFile, 'r') as f:
        count = 0
        for line in f:
            if count >0:
                origLines.append(line.strip())
            else:count +=1
    translatedLines = []
    with open(translatedChordFile, 'r') as f:
        translatedLines.append(line.strip())
    for i in range(len(origLines)):
        line = origLines[i]
        openBracket = line.index("{")
        closeBracket = line.index("}")
        newLine = line[0:(openBracket+1)] + translatedLines[i] +line[closeBracket:]
        output.append(newLine)
    return output