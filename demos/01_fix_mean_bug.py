
from pathlib import Path
import numpy as np

DATA = Path(__file__).parent / "data" / "tiny_lightcurve_clean.csv"

data = np.loadtxt(DATA, delimiter=",", skiprows=1)
time = data[:,0]
flux = data[:,1]

# BUG: incorrect mean indexing
mean_flux = np.mean(flux)[0]

flux_norm = flux / mean_flux

print("First values:", flux_norm[:5])
