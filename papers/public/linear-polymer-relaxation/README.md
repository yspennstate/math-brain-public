# Sharp relaxation, cutoff, and graph diffusion for a linear-polymer chain

Yitzchak Shmalo

[Read the paper](paper/main.pdf).

This repository contains the manuscript, LaTeX source, and reproducible calculations for a finite coagulation–fragmentation chain. Each unordered pair of polymer instances merges at rate `2/n`; each internal link breaks at rate `beta`.

The paper gives a direct proof that the full polymer spectral gap equals the cluster-count gap, an equality announced by Granovsky and Erlihson. It proves the uniform estimate

$$
\sqrt{\beta^2+4\beta}-\frac5n
\le \gamma_M(n,\beta)
\le \sqrt{\beta^2+4\beta}+\frac4n,
$$

together with bounds valid through the rare-fragmentation regime and a critical scaling function at `beta = b/n²`.

For `beta = b/n`, the count chain and the polymer chain from either extreme configuration have total-variation cutoff at

$$
t_n=\frac{\sqrt n\log n}{8\sqrt b}
$$

with a window of order at most `sqrt(n)`. From an arbitrary polymer configuration, the proved mixing upper bound has order `sqrt(n) (log n)²`. The worst-case polymer cutoff remains open.

The spatial extension adds exclusion diffusion on a connected weighted graph. Its gap is exactly

$$
\gamma_{\mathrm{sp}}=\min\{\gamma_M,\eta_1+D\lambda_G\},
$$

where `lambda_G` is the one-particle graph gap and `eta_1` is an explicitly defined radial reaction eigenvalue. The paper gives sharp estimates and critical limits for both reaction eigenvalues. It also treats bounded inhomogeneous reactions, directed permutation motion, a stationary circulation on the original polymer reaction graph, and reversible changes of the coagulation kernel.

The graph model retains globally count-dependent reaction rates. General spatial coagulation–fragmentation equations and unrestricted nonconstant kernels are outside the proved results.

## Reproduce the calculations

The exact checks in `code/check_certificates.py` use Python's standard library. The numerical checks require NumPy and SciPy; the figure also requires Matplotlib.

```sh
python -m pip install -r code/requirements.txt
python code/check_certificates.py
python code/check_extensions.py
python code/plot_scaling.py
```

The programs construct the finite generators independently of their radial reductions, check polynomial identities and transition rates, and compare finite spectra. Results are written to `results/`. Floating-point checks support reproducibility; the proofs establish the theorems for all stated parameters. The critical-operator calculations include the analytic truncation bounds separately from floating-point eigenvalue errors.

## Build the paper

A TeX installation with AMS packages, `latexmk`, and BibTeX is sufficient.

```sh
cd paper
latexmk -pdf main.tex
```

The funding, competing-interest, and AI-assistance declarations are included in the manuscript.
