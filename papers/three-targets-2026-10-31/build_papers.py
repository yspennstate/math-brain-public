"""Build the three public manuscripts; requires TeX Live and latexmk."""
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
JOBS = [
    ('T067/paper', '-pdf', 'T067_full_proof.tex', 'T067/T067_Finite_Mean_Reconstruction.pdf'),
    ('T228', '-pdf', 'T228_Nonlinear_SGD_Power_Tails.tex', 'T228/T228_Nonlinear_SGD_Power_Tails.pdf'),
    ('T357', '-xelatex', 'T357_Calibration_Along_Gradient_Descent.tex', 'T357/T357_Calibration_Along_Gradient_Descent.pdf'),
]
for folder, engine, source, destination in JOBS:
    subprocess.run(
        ['latexmk', engine, '-interaction=nonstopmode', '-halt-on-error', source],
        cwd=ROOT / folder, check=True,
    )
    built = ROOT / folder / Path(source).with_suffix('.pdf')
    target = ROOT / destination
    if built != target:
        shutil.copyfile(built, target)
    print(target.relative_to(ROOT))
