# CSCI599-TransformMusicProject
CSCI599-TransformMusicProject

#Install music21
http://web.mit.edu/music21/doc/usersGuide/usersGuide_01_installing.html

#Run RNN

python -m nmt.nmt     --src=chord --tgt=node     --vocab_prefix=nmt/tmp/chord_data/vocab      --train_prefix=nmt/tmp/chord_data/train     --dev_prefix=nmt/tmp/chord_data/dev      --test_prefix=nmt/tmp/chord_data/test     --out_dir=nmt/tmp/chord_model     --num_train_steps=1200     --steps_per_stats=100     --num_layers=2     --num_units=128     --dropout=0.2     --metrics=bleu