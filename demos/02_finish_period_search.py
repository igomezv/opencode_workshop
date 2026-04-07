
import numpy as np
from pathlib import Path

DATA = Path(__file__).parent / "data" / "tiny_lightcurve_noisy.csv"

data = np.loadtxt(DATA, delimiter=",", skiprows=1)
time = data[:,0]
flux = data[:,1]

def search_best_period(time, flux):

    freqs = np.linspace(0.2,3.0,300)

    # TODO: compute score for each frequency
    scores = ...

    best_freq = ...
    best_period = ...

    return best_period

period = search_best_period(time, flux)

print("Best period:", period)
