import parselmouth
import numpy as np
import matplotlib.pyplot as plt

class Plot :

    # Draw Spectogram
    def draw_spectrogram(self , spectrogram, dynamic_range=70):
        X, Y = spectrogram.x_grid(), spectrogram.y_grid()
        sg_db = 10 * np.log10(spectrogram.values)
        plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
        plt.ylim([spectrogram.ymin, spectrogram.ymax])
        plt.xlabel("time [s]")
        plt.ylabel("frequency [Hz]")

    # Draw Intensity
    def draw_intensity(self, intensity):
        plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
        plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
        plt.grid(False)
        #plt.ylabel("intensity [dB]")

    # Draw pitch
    def draw_pitch(self, pitch):
        # Extract selected pitch contour, and
        # replace unvoiced samples by NaN to not plot
        pitch_values = pitch.selected_array['frequency']
        pitch_values[pitch_values == 0] = np.nan
        plt.plot(pitch.xs(), pitch_values,  linewidth=3, color='w')
        plt.plot(pitch.xs(), pitch_values,  linewidth=1)
        plt.grid(False)
        plt.ylim(0, pitch.ceiling)
        plt.ylabel("pitch [Hz]")

    # Draw Amplitude and show Figure
    def draw_amplitude(self , snd):
        plt.figure()
        plt.plot(snd.xs(), snd.values.T)
        plt.xlim([snd.xmin, snd.xmax])
        plt.xlabel("time [s]")
        plt.ylabel("amplitude")
        plt.show()

    # Plottoing Sound Spectogram , Pitch , Intenstiy
    def draw_Sound(self , snd):
        # get parselmouth.Intensity
        intensity = snd.to_intensity(50,0.016)
        # get parselmouth.Pitch
        pitch = snd.to_pitch(0.020, 50.0, 500.0)
        # get parselmouth.Spectrogram
        spectrogram = snd.to_spectrogram(window_length=0.064)
        plt.figure().canvas.set_window_title('Extracted voiced Peaks')
        self.draw_spectrogram(spectrogram)
        plt.twinx()
        self.draw_intensity(intensity)
        #plt.show()
        plt.twinx()
        self.draw_pitch(pitch)
        plt.xlim([snd.xmin, snd.xmax])
        plt.show()

if __name__ == '__main__':
    snd = parselmouth.Sound("1_b.wav")
    Plot().draw_amplitude(snd)
    Plot().draw_Sound(snd)
