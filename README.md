
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

## Install WezTerm

https://wezterm.org/installation.html

---

## Repository Structure

demos/
    01_fix_mean_bug.py
    02_finish_period_search.py
    03_fix_plot_and_peak.py
    data/
        tiny_lightcurve_clean.csv
        tiny_lightcurve_noisy.csv

---

## Demos

Demo 1 — Fix a bug in NumPy code.

Demo 2 — Complete a simple frequency search.

Demo 3 — Debug plotting and indexing errors.

Example prompt:

Explain the error in this file and fix it.

---

## Important

AI tools can generate syntactically correct but scientifically wrong code.
Always verify assumptions and results.
