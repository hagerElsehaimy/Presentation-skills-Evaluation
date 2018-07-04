import wave
import pyaudio

class Audio:

    # size of each sample is 2 bytes
    __FORMAT = pyaudio.paInt16

    # Each frame will have 2 samples , Therefore size of each frame is 4 bytes.
    __CHANNELS = 2

    # "RATE" is the "sampling rate", i.e. the number of frames per second
    __RATE = 44100

    # number of frames in the buffer the (potentially very long) signals are split into
    __CHUNK = 1024

    # Length of record
    __RECORD_SECONDS = 5

    # Recorded File Name
    __WAVE_OUTPUT_FILENAME = "..\\Speech\\SpeechProcessing\\AudioFile.wav"

    def audioRecord(self):
       
        audio = pyaudio.PyAudio()

        # start Recording
        stream = audio.open(format=self.__FORMAT, channels=self.__CHANNELS,
                            rate=self.__RATE, input=True,
                            frames_per_buffer=self.__CHUNK)

        # "frames" list, size of each element must be 1024*4 bytes
        frames = []

        # Size is number of frames in the buffer * size of frame 4 bytes
        # number of frames that should be recorded
        for i in range(0, int(self.__RATE / self.__CHUNK * self.__RECORD_SECONDS)):
            # read chunk per chunk
            data = stream.read(self.__CHUNK)
            frames.append(data)
        # print "finished recording"

        # stop Recording and Close
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Create Wav File and write Frames on it
        waveFile = wave.open(self.__WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(self.__CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(self.__FORMAT))
        waveFile.setframerate(self.__RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

        return self.__WAVE_OUTPUT_FILENAME