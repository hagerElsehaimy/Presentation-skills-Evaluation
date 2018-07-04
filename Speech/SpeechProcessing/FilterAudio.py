from scipy.io.wavfile import read, write
from scipy.signal.filter_design import butter, buttord
from scipy.signal import lfilter
import numpy as np
from Speech.SpeechProcessing.Audio import *


class Filter:

    __filteredFile = '..\\Speech\\SpeechProcessing\\FilteredAudio.wav'

    def low_filter(self, wavFile):
        rate, sound_samples = read(wavFile)
        sound_samples = np.float64(sound_samples / 32768.0)
        pass_freq = 0.2
        stop_freq = 0.3
        pass_gain = 0.5  # permissible loss (ripple) in passband (dB)
        stop_gain = 10.0  # attenuation required in stopband (dB)
        ord, wn = buttord(pass_freq, stop_freq, pass_gain, stop_gain)
        b, a = butter(ord, wn, btype='low')
        filtered = lfilter(b, a, sound_samples)
        filtered = np.int16(filtered * 32768 * 10)
        write(self.__filteredFile, rate, filtered)
        return self.__filteredFile

    def band_pass_filter(self, wavFile):
        rate, sound_samples = read(wavFile)  # f , fs
        sound_samples = np.float64(sound_samples / 32768.0)
        n = 7
        beginFreq = 700.0 / (rate / 2)
        endFreq = 12000.0 / (rate / 2)
        [b, a] = butter(n, [beginFreq, endFreq], 'bandpass')
        filtered = lfilter(b, a, sound_samples)
        filtered = np.int16(filtered * 32768 * 10)
        write(self.__filteredFile, rate, filtered)
        return self.__filteredFile

    # Filter Record Audio
    def getAudioFiltered(self):
        # First, Record Audio
        audio = Audio()
        wavFile = audio.audioRecord()

        # Second , Filter Audio with low pass Filter
        return self.low_filter(wavFile)
