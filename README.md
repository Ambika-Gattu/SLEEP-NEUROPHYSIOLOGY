# SLEEP-NEUROPHYSIOLOGY-ANALYSIS-EEG-BASED-SLEEP-STAGE-CLASSIFICATION
MATLAB-based system for EEG sleep stage classification. <br>
EEG-Based Sleep Stage Classification  <br>
This project implements a MATLAB-style signal processing pipeline in Python to simulate and analyze EEG data for sleep stage classification. It focuses on extracting both statistical and spectral features from simulated EEG signals segmented into 30-second epochs, emulating real-world sleep research datasets.  <br>

Project Overview  <br>
- Objective: Simulate EEG signals, segment them into epochs, extract key features, and visualize sleep stages (Wake, N1, N2, N3, REM).  <br>
- Tools: Python, NumPy, SciPy, Matplotlib  <br>
- Domain: Sleep Neurophysiology, Biomedical Signal Processing, Feature Extraction  <br>

Key Features & Workflow  <br>
1. Signal Simulation: EEG signals are synthetically generated with a dominant 10 Hz alpha rhythm plus added noise. Simulated for 10 epochs of 30 seconds each at 100 Hz sampling rate.  <br>
2. Epoching & Labeling: Data segmented into 30-second epochs (3000 samples per epoch). Simulated hypnogram labels for 5 sleep stages: Wake, N1, N2, N3, REM.  <br>
3. Feature Extraction:  <br>
- Statistical Features: Mean, Std Dev, Max, Min, Peak-to-Peak  <br>
- Spectral Features using Welch’s method:  <br>
  - Total Power (0.5–45 Hz)  <br>
  - Band Powers: Delta, Theta, Alpha, Beta, Gamma  <br>
  - Spectral Entropy (Shannon entropy of normalized power spectrum)  <br>
4. Visualization:  <br>
- Full EEG signal plot  <br>
- Individual hypnogram plots for each sleep stage (epoch-wise labeling)  <br>

Relevance to VLSI / Biomedical Chip Design  <br>
This project demonstrates core signal processing techniques applicable in:  <br>
- Biomedical ICs for sleep monitoring and neurofeedback  <br>
- Feature extraction for on-chip classification  <br>
- Low-power DSP for medical-grade silicon systems  <br>

Future Extensions  <br>
- Real EEG dataset integration (e.g., Sleep-EDF)  <br>
- Classifier model for automated stage prediction  <br>
- Real-time streaming & embedded system porting  <br>
