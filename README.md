# AUXON FSK Encoder

This project is the first step toward a larger ultrasonic communication system.  
It converts any input string into binary, then encodes each bit as a sine wave at different frequencies using **Frequency Shift Keying (FSK)**.

The generated audio can be transmitted through speakers or ultrasonic transducers, allowing offline data transfer using sound.

### ✨ Features
- Converts any text string into 8-bit binary
- Encodes each bit as a sine wave at two different frequencies (f0 and f1)
- Adjustable bit duration (controls bitrate)
- Configurable sample rate and frequencies
- Outputs a standard `.wav` file

### ⚙ How It Works
1. Input text → converted to binary  
2. `0` bits become frequency `f0`  
3. `1` bits become frequency `f1`  
4. All bit-tones are concatenated and saved as a WAV file  
5. The resulting audio can later be decoded with an FFT-based receiver

### 🚧 Notes
- Longer strings result in longer audio output (bitrate-dependent)
- High-frequency tones (>20 kHz) require hardware that supports high sample rates
- Laptop speakers cannot output real ultrasound — you’ll need ultrasonic transducers for proper tests

### 🛠 Planned Improvements
- Real-time transmitter (no WAV file required)
- FFT-based decoder to reconstruct text from audio
- Synchronisation headers + checksums
- Support for ultrasonic hardware (40–60 kHz)

---

This is a foundational component of the wider **AUXON** ultrasonic communication project.
