import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
audio_file = "D:\projects\post_project\coin.wav"
samples, sample_rate = librosa.load( audio_file )
fig = plt.figure(figsize =[5,5])
ax = fig.add_subplot(111)
ax.axes.get_xaxis().set_visible( False )
ax.axes.get_yaxis().set_visible( False )
ax.set_frame_on(False)
S = librosa.feature . melspectrogram (y = samples , sr = sample_rate )
K = librosa.power_to_db(S, ref = np .max)
librosa.display.specshow(K)