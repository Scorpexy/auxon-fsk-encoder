import math
import wave
import struct

def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=0.5):
    samples = []
    for i in range(int(duration * sample_rate)):
        t = i / sample_rate
        sample = amplitude * math.sin(2 * math.pi * freq * t)
        samples.append(sample)
    return samples

def save_wav(filename, samples, sample_rate=44100):
    wav_file = wave.open(filename, "w")
    wav_file.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))

    for s in samples:
        wav_file.writeframes(struct.pack('<h', int(s * 32767)))

    wav_file.close()

# EXAMPLE: 40 kHz ultrasonic tone, 1 second
samples = generate_sine_wave(15000, 1.0)   # 40,000 Hz for 1 second
save_wav("15kHz.wav", samples)
