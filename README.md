### CSCI 599 Deep Learning - Final Report
# Music Style Transfer Project 
### Team: VicDucLuan (Duc Le, Luan Tran, Vic Chen)

## 1. Introduction

Song composition is difficult and talent needed. Nowadays, there is more and more research to use learning algorithm especially deep learning to do jobs which require creativity, including composing music. In our project, we want to develop an intelligent system which can transfer music style of a song to a new genre. This work is inspired by the fact that a lot of indie musicians cover popular songs into different styles such as cover rock ’n roll to acoustic or cover folk to Jazz.

We choose Jazz style to be the targeted genre for this project because Jazz has several significant and unique attributes, like spontaneous tempo, lots of seventh chord and improvisation of notes. Even the people who don’t really know jazz can easily recognize them.

-  **Problem Formulation**
Our goal is training a machine learning model that knows how the chords played in Jazz songs and is able to translate the non-jazz style song to jazz style.	



## 2. Proposed Approach
When a song is covered, the melody usually is retained and the background music is changed. Therefore, we separate the songs into a monophonic part (melody) and background music (chord/harmony), and we focus on changing the background music.  In the background music, different ways to play chords - the note combinations produce different styles of music. Our approach is to learn a model that produces a jazz style chords. 

We use [music21](http://web.mit.edu/music21/) library to extract Piano track in midi files. A chord will have different expressions, especially in Jazz, performers would like to improvise some different notes. For example, E3 chord, there are at least 3 different expressions in song “Imagine”:

| Chord | Note Combination |
| --- | --- |
| E3 | {G in octave 3 , E in octave 3} E3-interval <br>{E in octave 3 , D in octave 4 , G in octave 3} E3-minor-seventh<br> {G in octave 3 , E in octave 3 , B in octave 3} E3-minor triad
|E3-minor-seventh | {E in octave 3, D in octave 4, G in octave 3, B in octave 3} <br> {D in octave 4 , G in octave 4, E in octave 3}


We use seq2seq model (Sutskever et al., 2014, Cho et al., 2014) which have already gotten great success in machine translation, speech recognition, and text summarization fields. The chord sequences are considered as the input language, and they are translated by NMT into sequences of notes (output language) that should be played.

![102](https://user-images.githubusercontent.com/18378723/33247016-c39ae760-d2cf-11e7-91e8-95f393cc6c47.jpeg)
![103](https://user-images.githubusercontent.com/18378723/33247019-c6118d3c-d2cf-11e7-9f56-5a9073dba565.jpeg)


In this study, we use 2 representations of a chord, i.e., common representation (E3-incomplete minor-seventh) and compact representation (E3). The objective is to find the note combination when playing a chord, e.g., E3 -> {E in octave 3 | D in octave 4 | G in octave 3} 

After the note combinations for chords are found, we incorporate them into the original song to produce a jazz style song. 

## 3. Experiments
Methodology: We evaluate the performance of our algorithm using the midi jazz files. The experiments are conducted on a Linux machine 3.4GHz, 8Gb memory, and a GPU. To measure the goodness of the model, we report the blue score of the test set. The default hyperparameters can be found  [here](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/iwslt15.json).

Datasets:  ~1500 jazz midi files are used. In that dataset, we use 802 files that have piano tracks for evaluation. We export chords and corresponding notes from midi files and separate chords into sentences with length L (default value  L = 20 chords). After that, we put them to train, dev, and test datasets. Train and dev datasets are used for model training. 

With default settings: 

|                            | Train | Dev   |  Test   |
| ---------------------- | ------- |-------- | -------- |
| Number of jazz files   |  562  | 80    | 160   |
| Number of sentences | 11049 | 1482 | 2897 | 

Vocabulary

|  | #Chords | #Note Combinations |
| - | ------- | ------ |
| Chord compact representation | 79 | 39837 | 
| Chord common representation | 2269  | 39387 |   


### 3.1. Varying the chord representation. 
In this section, we show the results with the 2 types of chord representation: common name and compact name. The compact name is a brief representation of common name. Multiple chords with different common names can have the same compact name. 

- Compact chord representation:
After training, the result of translating chord sequence to note combination sequence is summerized in the following table. 

| Dev perplexity | Dev blue score | Test perplexity | Test blue score | 
| -------------- | -------------- | --------------- | --------------- |
| 51871.42       |           10.5 | 71964.79        | 8.4             |      

![chord20_more_simple_piano](https://user-images.githubusercontent.com/5298482/33243942-85f0cfc8-d2a3-11e7-9b16-43bf7fc2612c.png)



Result: 

|  | Original Song | Transformed Song |
| - | ----------------- | ------------------------ |
| Name | Can you feel my love tonight | Can you feel my love tonight - jazz version |
| Music sheet (beginning part) | ![canyoufeelthelovetonight-1](https://user-images.githubusercontent.com/5298482/33243353-6bb8ddd0-d299-11e7-9e5b-107c7b120d85.png) | ![canyoufeelthelovetonight_more_simple_big_data_piano_track_jazz_11_26-1](https://user-images.githubusercontent.com/5298482/33243354-78b854de-d299-11e7-9958-db3fab91abd7.png) | 
| Full Midi file | [Can you feel my love tonight](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight.mid) | [Can you feel my love tonight jazz ](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight_more_simple_big_data_piano_track_jazz_11_26.mid) |


- Common chord representation:
After training, the result of translating chord sequence to note combination sequence is summerized in the following table. 

| Dev perplexity | Dev blue score | Test perplexity | Test blue score | 
| -------------- | -------------- | --------------- | --------------- |
| 21539.96       |           15.0 | 45704.38        | 10.7             | 

It is showed that this representation gives better results than the compact representation because it is more detailed. 
![chord_20_simple_piano png](https://user-images.githubusercontent.com/5298482/33243869-81cbdaf6-d2a2-11e7-8b09-af6b9c9a320f.png)

Result: 

|  | Original Song | Transformed Song |
| - | ----------------- | ------------------------ |
| Name | Can you feel my love tonight | Can you feel my love tonight - jazz version 2 |
| Music sheet (beginning part) | ![canyoufeelthelovetonight-1](https://user-images.githubusercontent.com/5298482/33243353-6bb8ddd0-d299-11e7-9e5b-107c7b120d85.png) | ![canyoufeelthelovetonight_simple_piano_track_jazz_11_26-1](https://user-images.githubusercontent.com/5298482/33244188-ede8e9d6-d2a7-11e7-95fa-5a8d7f442592.png)  | 
| Full Midi file | [Can you feel my love tonight](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight.mid) | [Can you feel my love tonight jazz 2 ](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight_simple_piano_track_jazz_11_26.mid) |

Because using common chord representation achieve better results, from now, we use it for the following experiments. 

### 3.2 Varying the sentence length

We separate each song (in train, dev, test datasets) to multiple sentences because each chord can depend on only some previous chords. We vary the length of a sentence from 5 to 20 chords.
Blue score: 
 
|  | L = 5 | L = 10 | L = 20 |
| - | ----- | ----- | ---- | 
| Test blue score | 10.8 | 10.5 | 10.7 | 

As we can see in the above table, we have similar results when using different lengths of a sentence. 
Below we present the detailed test results with L = 5 and L = 10. The result with L = 20 is already presented in the previous section: 

|  | Original Song | L = 5 | L = 10 |
| - | ----- | ----- | ---- | 
| Name | Can you feel my love tonight | Can you feel my love tonight - jazz5 | Can you feel my love tonight - jazz10 |
| Music sheet (beginning part) | ![canyoufeelthelovetonight-1](https://user-images.githubusercontent.com/5298482/33243353-6bb8ddd0-d299-11e7-9e5b-107c7b120d85.png)  | ![canyoufeelthelovetonight_simple_piano_track_5_jazz_11_26-1](https://user-images.githubusercontent.com/5298482/33246238-0b6c26a2-d2c7-11e7-87e5-37d24851d2c4.png) | ![canyoufeelthelovetonight_simple_piano_track_10_jazz_11_26-1](https://user-images.githubusercontent.com/5298482/33246242-1965d00a-d2c7-11e7-872d-3ec422b59289.png) | 
| Full Midi file | [Can you feel my love tonight](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight.mid) |  [Can you feel my love tonight - 5 ](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight_simple_piano_track_5_jazz_11_26.mid) |  [Can you feel my love tonight - 10](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight_simple_piano_track_10_jazz_11_26.mid) | 


The full music sheets of songs and other transformed songs are available  [here](https://github.com/lemduc/CSCI599-TransformMusicProject/tree/master/result_figures_wav)

Piano Track Result: 

 | Original Song | Transformed song | 
 | ------------------ | ----------------------- |
 | Can you feel the love tonight [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight.mid) | Can you feel the love tonight jazz, [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight_simple_piano_track_jazz_11_26.mid), [wav](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/canyoufeelthelovetonight_simple_piano_track_jazz_11_26.wav)  |
 | Imagine [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/Imagine_out.mid) | Imagine jazz, [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/Imagine_more_simple_big_data_piano_track_jazz_11_26.mid) [wav](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/Imagine_more_simple_big_data_piano_track_jazz_11_26.wav) | 
 | All of me [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/allofme.mid) | All of me jazz, [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/allofme_simple_piano_track_20_jazz_11_26.mid), [wav](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/allofme_simple_piano_track_20_jazz_11_26.wav) |
 | Nang am xa dan [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/nangamxadan.mid) | Nang am xa dan jazz, [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/nangamxadan_simple_piano_track_10_jazz_11_26.mid), [wav](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/nangamxadan_simple_piano_track_10_jazz_11_26.wav) | 
 | Ngoi nha hanh phuc - Full house [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/ngoinhahanhphuc.mid) | Ngoi nha hanh phuc jazz, [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/ngoinhahanhphuc_simple_piano_track_20_jazz_11_26.mid), [wav](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/ngoinhahanhphuc_simple_piano_track_20_jazz_11_26.wav) | 
 | Quay ve di [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/quayvedi.mid) | Quay ve di jazz, [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/quayvedi_simple_piano_track_20_jazz_11_26.mid), [wav](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/quayvedi_simple_piano_track_20_jazz_11_26.wav) | 
 | Set fire to the rain [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/setfiretotherain.mid) | Set fire to the rain jazz,  [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/setfiretotherain_simple_piano_track_20_jazz_11_26.mid), [wav](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/setfiretotherain_simple_piano_track_20_jazz_11_26.wav) | 
| Kiss the rain [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/Kiss%20The%20Rain.mid) | Kiss the rain jazz [midi](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/KissTheRain_more_simple_big_data_piano_track_jazz_11_26.mid), [wav](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/KissTheRain_more_simple_big_data_piano_track_jazz_11_26.wav) |

Combination of transformed piano and bass, harmonica:

For example, with the song [Imagine](https://github.com/lemduc/CSCI599-TransformMusicProject/blob/master/result_figures_wav/Imagine_more_simple_big_data_track0_jazz.mid). 

### 3.3. Adjusting Notes' Duration

Because another important element in Jazz is the varied durations, we would like to try to learn how to mimic how the Jazz performers do. Jazz performers are always playing the notes and chords spontaneously, for example, 4 single quarter notes will probably be played as one dot and dot and one dot and dot to express different emotion. If we can try to predict the how the Jazz song plays the chord at a different duration, it would let the song more close to Jazz.
![301](https://user-images.githubusercontent.com/18378723/33282229-ddf17024-d35c-11e7-9c9b-43758337097b.jpeg)
Our first thought is using the previous result to do chord sequences translate to duration(tempo) sequences, it means this idea is like "At this moment, the performer wants to play a C chord, how will he/she do?".
![302](https://user-images.githubusercontent.com/18378723/33282232-e0066536-d35c-11e7-9a1c-8d2d4ac6a93e.jpeg)

We extracted the chords-durations mapping to training our model. Unfortunately, even turning different hyper-parameters,  the initial results still converged to one or two different tempos. The possible reason is the vocabulary of chords are more than 2000 words, but durations are just 120 words. More, most chords have been played at 16th note(0.25) more than others. It causes that playing 16th note may always get a higher score by NMT. After 12000 iterations(8 hours) training, the input sentences are easy to be inferred to all 16th notes. It is not our expectation. 

At this point, translating chords to durations by NMT is not a successful approach. In conclusion, the chords are not related to the note durations directly in the dataset. There are other works for music creation by predicting what is the next note duration from a correlation between beats, that can be an interesting approach.
 

## 4. Related Work

Most of other music transfer works are belonging to two categories. In the first category, researchers tried to learn musical styles from samples to generate new songs of that style [1, 2, 3]. The authors also use musical knowledge to improve the quality of generated music pieces. In the second category, researchers tried to merge style the sound signals of a song (in WAV format) into another song [4, 5, 6] using techniques like [WaveNet](https://deepmind.com/blog/wavenet-generative-model-raw-audio/). However, this approach will require a large amount of data as well as resources for training. Rather than that, some simple transferring models give out very poor quality output [5].

In our approach, we have used some basic musical knowledge to transform the music transfer problem into sequence translation problem. We don't rely on any music knowledge about Jazz, rather than that, we train model to be able to create Jazz felling. We believe our approach is the first of its kind. 

1. [https://medium.com/artists-and-machine-intelligence/neural-nets-for-generating-music-f46dffac21c0](https://medium.com/artists-and-machine-intelligence/neural-nets-for-generating-music-f46dffac21c0)
2. [https://github.com/tensorflow/magenta](https://github.com/tensorflow/magenta)
3. [https://github.com/brangerbriz/midi-rnn](https://github.com/brangerbriz/midi-rnn)
4. [https://itp.nyu.edu/shows/thesis2017/towards-neural-music-style-transfer/](https://itp.nyu.edu/shows/thesis2017/towards-neural-music-style-transfer/)
5. [https://github.com/rupeshs/neuralsongstyle](https://github.com/rupeshs/neuralsongstyle)
6. [https://github.com/DmitryUlyanov/neural-style-audio-tf](https://github.com/DmitryUlyanov/neural-style-audio-tf)


## 5. Conclusions and Future Work

In this project, we successfully transformed non-jazz style song to a jazz style song using chord translation. The chords in the original song are played by the jazz style combination of notes which are produced by the model. We also experienced using duration translation but it needs to be explored more. Here, we note some directions can be explored in the future: 

1. Scale up/down the key of the dataset into the same key (e.g. C Major) to reduce the size of language vocabulary, which in turns increase the size of our training data.

2. Apply our approach to other types of instrument. 

3. Fine tune the parameters and try different algorithms/models enhance the result.

4. Divide the whole song into many pieces for 2 bars or 4 bars duration, because usually, the music in certain duration (like a whole music sentence) is relevant, that might be better to predict how the chord machine can learn to play.

## References

1. [Music21](http://web.mit.edu/music21/doc/index.html)
2. [Neural Machine Translation (seq2seq) Tutorial](https://github.com/tensorflow/nmt) 

## Members' contributions

- Duc Le: clean up raw data to get chord and note sequences, train the NMT model based on the collected data.
- Luan Tran: extract the raw representation of songs (notes, chords, tempo) from midi files, training the NMT models, regenerate midi output files by integrating the model’s output. 
- Vic Chen: collect jazz midi files, separate melodies, and background, cleanup generated jazz sample from the model, training models and analysis for tempo experiments.
