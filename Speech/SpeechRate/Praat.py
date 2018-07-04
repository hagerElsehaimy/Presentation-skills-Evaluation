import numpy as np
import parselmouth

class Praat:

    def calcSyllbale(self, snd):

        # Get parselmouth.Sound
        self.__soundAnalysis = snd

        # Process Step 1 --> Extract Intensity
        self.__extractIntensity()

        # Process Step 2  --> Take all peaks above certain threshold
        peaksThresh = self.__getPeaksAboveThreshold()

        # Process Step 3 -- > Inspect Dips and all Peaks from Intensity
        peaks , dips = self.__getPeaksAndDips()

        # Complete Process Step 3 --> Preceding Dip with a peak of at least 2 DB
        peaksfilter = self.__getSyllable(peaks , dips , peaksThresh)

        # Process of Step 4 --> Extract Pitch Contour
        self.__extractPitch()

        # Complete Process Step 4 --> Exclude all peaks that are unvoiced
        peaksfilter = self.__excludeUnvoicedPeaks(peaksfilter)

        # Count Syllable
        syllables = len(peaksfilter)
        #print("Count of Syllables : ", syllables)

        # Count Number of words
        words = int(round(syllables / 1.4))
        # print "Count of Words : ", Words

        return words
        # end Process

    # Step 1
    def __extractIntensity(self):
        intensity = self.__soundAnalysis.to_intensity(50, 0.016)
        self.__intensity_values = []
        for sublist in intensity.values:
            for item in sublist:
                self.__intensity_values.append(item)

    # Step 2
    def __getPeaksAboveThreshold(self):
        threshold = np.median(self.__intensity_values)
        # print(Threshold)
        peaksThresh = list(filter(lambda x: x > threshold, self.__intensity_values))
        return peaksThresh

    # Step 3 --> Part 1
    def __getPeaksAndDips(self):
        x = 1
        dips = []
        peaks = []
        dips.append(self.__intensity_values[0])

        flag = True
        while x < len(self.__intensity_values):
            if (self.__intensity_values[x] > self.__intensity_values[x - 1]) and not flag:
                dips.append(self.__intensity_values[x - 1])
                flag = True
            elif (self.__intensity_values[x] < self.__intensity_values[x - 1]) and flag:
                peaks.append(self.__intensity_values[x - 1])
                flag = False
            x += 1

        # Make length of dips and peaks equal
        if len(dips) < len(peaks):
            peaks.pop(len(peaks) - 1)
        elif len(peaks) < len(dips):
            dips.pop(len(dips) - 1)
        return peaks , dips

    # Step 3 --> Part 2
    def __getSyllable(self , peaks , dips , peaksThresh):
        peaksfilter = []
        i = 0
        while i < len(peaks):
            if (peaks[i] - dips[i]) >= 2 and peaks[i] in peaksThresh:
                peaksfilter.append(peaks[i])
            i += 1
        # print "From Step 3 This is Peaks Syllables : "
        # print peaksfilter
        return peaksfilter

    # Step 4 --> Part 1
    def __extractPitch(self):
        pitch = self.__soundAnalysis.to_pitch(0.020, 50.0, 500.0)
        pitchValues = pitch.to_matrix().values
        self.__pitch_values = []
        for sublist in pitchValues:
            for item in sublist:
                self.__pitch_values.append(item)


    # Get Pitch Indices to Exclude Unvoiced Peaks Indices
    def __getPitchIndices(self , listOfIndex , peaksfilter):
        j = 0

        while j < len(self.__intensity_values):
            for peak in peaksfilter:
                if peak == self.__intensity_values[j]:
                    if j >= len(self.__pitch_values):
                        listOfIndex.append(len(self.__pitch_values) - 1)
                    else:
                        listOfIndex.append(j)
            j += 1
        return listOfIndex

    # Step 4 --> Part 2
    def __excludeUnvoicedPeaks(self , peaksfilter):
        listOfIndex = []
        listOfIndex = self.__getPitchIndices(listOfIndex , peaksfilter)
        x = 0
        for index in listOfIndex:
            if self.__pitch_values[index] == 0:
                peaksfilter.pop(x)
                x -= 1
            x += 1

        # print "From Step 4 This is Voiced Peaks Syllables :"
        #print(peaksfilter)
        return peaksfilter

'''
if __name__ == '__main__':
    snd = parselmouth.Sound("E:/1_b.wav")
    Praat().calcSyllbale(snd)
'''
