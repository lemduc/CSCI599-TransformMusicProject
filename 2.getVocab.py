from utils import *

vob = set()

with open('train.chord', 'r') as f:
    read_data = f.readlines()
for lines in read_data:
    for c in lines.split(" "):
        if c:
            vob.add(c)

with open('dev.chord', 'r') as f:
    read_data = f.readlines()
for lines in read_data:
    for c in lines.split(" "):
        if c:
            vob.add(c)

with open('test.chord', 'r') as f:
    read_data = f.readlines()
for lines in read_data:
    for c in lines.split(" "):
        if c:
            vob.add(c)

with open('vocab.chord', 'w') as f:
    for c in vob:
        if c:
            f.write(c+'\n')

removeDuplicateChordinVocab('vocab.chord')

vob = set()
with open('train.node', 'r') as f:
    read_data = f.readlines()
for lines in read_data:
    for c in lines.split(" "):
        if c:
            vob.add(c)

with open('dev.node', 'r') as f:
    read_data = f.readlines()
for lines in read_data:
    for c in lines.split(" "):
        if c:
            vob.add(c)

with open('test.node', 'r') as f:
    read_data = f.readlines()
for lines in read_data:
    for c in lines.split(" "):
        if c:
            vob.add(c)

with open('vocab.node', 'w') as f:
    #f.write('<unk>\n<s>\n<')
    for c in vob:
        if c:
            f.write(c+'\n')


# vob = set()
# with open('train.dura', 'r') as f:
#     read_data = f.readlines()
# for lines in read_data:
#     for c in lines.split(" "):
#         if c:
#             vob.add(c)
#
# with open('dev.dura', 'r') as f:
#     read_data = f.readlines()
# for lines in read_data:
#     for c in lines.split(" "):
#         if c:
#             vob.add(c)
#
# with open('test.dura', 'r') as f:
#     read_data = f.readlines()
# for lines in read_data:
#     for c in lines.split(" "):
#         if c:
#             vob.add(c)
#
# with open('vocab.dura', 'w') as f:
#     #f.write('<unk>\n<s>\n<')
#     for c in vob:
#         if c:
#             f.write(c+'\n')
#
# removeDuplicateChordinVocab('vocab.dura')

removeDuplicateChordinVocab('vocab.node')

vob = set()
with open('train.dura', 'r') as f:
    read_data = f.readlines()
for lines in read_data:
    for c in lines.split(" "):
        if c:
            vob.add(c)

with open('dev.dura', 'r') as f:
    read_data = f.readlines()
for lines in read_data:
    for c in lines.split(" "):
        if c:
            vob.add(c)

with open('test.dura', 'r') as f:
    read_data = f.readlines()
for lines in read_data:
    for c in lines.split(" "):
        if c:
            vob.add(c)

with open('vocab.dura', 'w') as f:
    #f.write('<unk>\n<s>\n<')
    for c in vob:
        if c:
            f.write(c+'\n')

removeDuplicateChordinVocab('vocab.dura')
