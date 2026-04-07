
# OpenCode Mini Workshop (IAA–CSIC Stellar Variability Group)

Short internal workshop showing how **OpenCode** can help with research programming:
- debugging code
- completing missing functions
- refactoring scripts
- explaining unfamiliar code

All demos use **tiny local datasets** so they run in a few seconds on Linux, macOS, or Windows.

---

## Install Conda

Install Miniconda:

Windows
https://docs.conda.io/projects/conda/en/stable/user-guide/install/windows.html

macOS
https://docs.conda.io/projects/conda/en/stable/user-guide/install/macos.html

Linux
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

Check installation:

conda --version

---

## Create Environment

conda create -n opencode-workshop python=3.11 numpy matplotlib
conda activate opencode-workshop

Install pip dependencies:

pip install pandas scipy statsmodels seaborn tqdm joblib lightkurve astropy

Test:

python -c "import numpy, matplotlib; print('Environment OK')"

---

## Install OpenCode

https://opencode.ai/download

Linux / macOS:

curl -fsSL https://opencode.ai/install | bash

Check:

opencode --help

---

## Install WezTerm (optional, alternative to Unix terminal)

https://wezterm.org/installation.html

---

## Demos

Demo 1 — Fix a bug in NumPy code.

Demo 2 — Complete a simple peak search.

### Example Prompts

Explain the error in this file and fix it.

### DEMO Prompt 1: Download and Analyze TESS Data

Write a Python script that:

1. downloads a TESS light curve for TIC 25155310
2. removes outliers
3. flattens the light curve
4. computes a Lomb-Scargle periodogram
5. plots the light curve and the periodogram

Use lightkurve and astropy.

### DEMO Prompt 2: Read and Analyze Local FITS File

Write a Python script that:

1. reads the FITS file at `demos/data/hlsp_kepseismic_kepler_phot_kplr008006161-20d_kepler_v1_cor-filt-inp.fits`
2. extracts the time and flux columns
3. removes outliers (e.g., using sigma clipping)
4. flattens the light curve
5. computes a Lomb-Scargle periodogram
6. plots both the light curve and periodogram

### DEMO Prompt 3 with existing code.

1. Explain the code of MIARMA_python-main to me, translate it into English and correct it, give me a test.py file to verify it.
2. Messy notebook. 


---

## Important

AI tools can generate syntactically correct but scientifically wrong code.
Always verify assumptions and results.
