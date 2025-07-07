import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.integrate import simps

# Simulated parameters
fs = 100                 # Sampling frequency
epoch_len = 30 * fs     # Samples per epoch (3000)
num_epochs = 10         # Total epochs

# Generate simulated EEG data
eeg_filtered = np.array([])
for i in range(num_epochs):
    t = np.arange(0, epoch_len) / fs
    eeg_epoch = np.sin(2 * np.pi * 10 * t + np.random.rand() * 2 * np.pi) + 0.5 * np.random.randn(len(t))
    eeg_filtered = np.concatenate((eeg_filtered, eeg_epoch))

# Create epochs matrix
epochs = eeg_filtered.reshape(num_epochs, epoch_len)

# Simulated labels: 0, 1, 2, 3, 4, 0, 1, 2, 3, 4
labels = np.array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4])

# Display number of valid labels
print(f'Number of valid labels: {np.sum(labels != -1)}')

# Feature extraction
print('Extracting features...')
features = []

for i in range(num_epochs):
    ep = epochs[i, :]
    mean_val = np.mean(ep)
    std_val = np.std(ep)
    max_val = np.max(ep)
    min_val = np.min(ep)
    ptp_val = np.ptp(ep)

    f, pxx = welch(ep, fs=fs, nperseg=fs*2)
    total_power = simps(pxx[(f >= 0.5) & (f <= 45)], f[(f >= 0.5) & (f <= 45)])
    delta = simps(pxx[(f >= 0.5) & (f < 4)], f[(f >= 0.5) & (f < 4)])
    theta = simps(pxx[(f >= 4) & (f < 8)], f[(f >= 4) & (f < 8)])
    alpha = simps(pxx[(f >= 8) & (f < 12)], f[(f >= 8) & (f < 12)])
    beta  = simps(pxx[(f >= 12) & (f < 30)], f[(f >= 12) & (f < 30)])
    gamma = simps(pxx[(f >= 30) & (f <= 45)], f[(f >= 30) & (f <= 45)])
    p_norm = pxx / np.sum(pxx)
    entropy_val = -np.sum(p_norm * np.log2(p_norm + np.finfo(float).eps))

    features.append([mean_val, std_val, max_val, min_val, ptp_val,
                     total_power, delta, theta, alpha, beta, gamma, entropy_val])

features = np.array(features)
print(f'Number of features extracted: {features.shape[0]}')

# ======= EEG signal plot (full) =======
plt.figure(figsize=(12, 4))
plt.plot(eeg_filtered, linewidth=1.5)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Simulated EEG Signal')
plt.grid(True)

# ======= Separate plots for each stage =======
stage_names = ['Wake', 'N1', 'N2', 'N3', 'REM']
stage_values = [0, 1, 2, 3, 4]

for s, stage_val in enumerate(stage_values):
    idx = np.where(labels == stage_val)[0]

    if len(idx) == 0:
        continue

    plt.figure()
    plt.plot(idx, labels[idx], 'o', markersize=8, linewidth=1.5)
    plt.xlabel('Epoch')
    plt.ylabel('Label')
    plt.yticks([0, 1, 2, 3, 4], ['Wake', 'N1', 'N2', 'N3', 'REM'])
    plt.ylim([-0.5, 4.5])
    plt.title(f'Hypnogram: {stage_names[s]}')
    plt.grid(True)

plt.show()
