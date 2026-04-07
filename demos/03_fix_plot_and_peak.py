
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).parent / "data" / "tiny_lightcurve_noisy.csv"

data = np.loadtxt(DATA, delimiter=",", skiprows=1)
time = data[:,0]
flux = data[:,1]

smooth = np.convolve(flux, np.ones(5)/5, mode="same")

# BUG: wrong use of shape
peak_idx = np.argmax(smooth.shape)

plt.plot(smooth, time)
plt.axvline(time[peak_idx])

plt.show()
