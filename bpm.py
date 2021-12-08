#calcul du rythme (battement par minute des musiques mp3
#par utilisation de la bibliotheque librosa
# d'apres https://github.com/librosa/librosa/blob/master/examples/beat_tracker.py
import librosa
import os
import warnings

warnings.simplefilter("ignore")

path = "/home/guillaume/Musique/Divers/"
# Use a default hop size of 512 samples @ 22KHz ~= 23ms
hop_length = 512
for element in os.listdir(path):
    if element.endswith('.mp3'):
        try:
            y, sr = librosa.load(path+element, sr=5000)
            tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length)
            print('Tempo: {0:0.2f} bpm  -> {1:s}'.format(tempo,element))
        except Exception as exception:
            # Output unexpected Exceptions.
            print(exception)