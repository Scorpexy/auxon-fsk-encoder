import math
import wave
import struct

# -----------------------------
#  SINGLE SIN WAVE
# -----------------------------
def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=0.5):
    samples = []
    for i in range(int(duration * sample_rate)):
        t = i / sample_rate
        sample = amplitude * math.sin(2 * math.pi * freq * t)
        samples.append(sample)
    return samples

# -----------------------------
#  SAVE AS WAV
# -----------------------------
def save_wav(filename, samples, sample_rate=44100):
    wav_file = wave.open(filename, "w")
    wav_file.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))

    for s in samples:
        wav_file.writeframes(struct.pack('<h', int(s * 32767)))

    wav_file.close()


# -----------------------------
#  CONVERTS INPUTTED STRING TO MACHINE CODE
# -----------------------------
def text_to_bits(text):
    return ''.join(f"{ord(c):08b}" for c in text)


# -----------------------------
#     ENCODES TEXT AS FSK
# -----------------------------
def fsk_encode(text, f0=38000, f1=42000, bit_duration=0.05, sample_rate=44100):
    bits = text_to_bits(text)
    wave_data = []

    for bit in bits:
        freq = f1 if bit == '1' else f0
        wave_data += generate_sine_wave(freq, bit_duration, sample_rate)

    return wave_data


# -----------------------------
#        MAIN 
# -----------------------------
if __name__ == "__main__":
    message = input("Convert following to audio: ")
    print("Encoding:", message)

    samples = fsk_encode(
        message,
        f0=35000,    # FREQUENCY FOR 0
        f1=45000,    # FREQUENCY FOR 1
        bit_duration=0.005,  # 5.0MS PER BIT
        sample_rate=48000
    )

    save_wav("auxon_fsk.wav", samples)
    print("Saved as auxon_fsk.wav")
