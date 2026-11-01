# Free multiplicative convolution and log-unimodality: three questions of Hasebe, Ueda and Wang

Yitzchak Shmalo

The paper (`paper/main.pdf`) answers Problems 4.3, 4.7 and 4.11 of T. Hasebe, Y. Ueda and J.-C. Wang,
*Log-unimodality for free positive multiplicative Brownian motion*, Colloq. Math. 169 (2022), 209-226
([arXiv:2009.13848](https://arxiv.org/abs/2009.13848)).

- **Theorem A.** The free multiplicative convolution of two multiplicatively symmetric log-unimodal laws need not be
  log-unimodal. For L >= 6 the log-uniform law on [e^-L, e^L], convolved with itself, has a log-density with a strict
  local minimum at 0.
- **Theorem B.** For nu = (delta_{1/10} + delta_{10})/2, which has compact support, sigma_t boxtimes nu is not
  log-unimodal for any t > 0.
- **Proposition D.** If nu is log-unimodal and supported in [alpha, beta], then sigma_t boxtimes nu is log-unimodal
  for all t >= (pi/2)(beta/alpha + alpha/beta).
- **Theorem C.** sigma_t is not boxtimes-strongly log-unimodal for any t > 0.

## Contents

- `paper/`: the LaTeX source, the PDF and the two figures.
- `lean/LogUnimodality.lean`: a Lean 4 / Mathlib check of the inequalities (CL) behind Theorem A, the root count
  of Theorem B given the Hasebe-Ueda-Wang criterion, and the numerical inequalities and the choice of parameters in
  the proof of Theorem C. Section 6 of the
  paper lists what is and is not formalized. `LogUnimodality.out` records the axioms each theorem depends on
  (`propext`, `Classical.choice`, `Quot.sound` only).
- `computations/`: Python scripts behind the numerical remarks and the figures, with their outputs. None of the
  proofs depends on them.
  - `numerics.py`: the boundary value w_*, the constants A, B and C_6, and the density g for L = 6, computed both by
    continuation and from the subordination equations (`numerics_L6.out`).
  - `lscan.py`: the density for a range of L and the transition value L_c (`lscan.out`, `lscan_curves.json`).
  - `rmt.py`: a random-matrix comparison for L = 6 (`rmt_L6.out`).
  - `thmB_density.py`: the density of log(sigma_t boxtimes nu) for the two-atom measure (`thmB_density.out`,
    `thmB_curves.json`).
  - `check_thmC.py`: exact rational arithmetic for the inequalities in the proof of Theorem C (`check_thmC.out`).
  - `make_figures.py`: Figures 1 and 2.

## Reproducing

Lean (toolchain in `lean/lean-toolchain`, Mathlib pinned in `lean/lake-manifest.json`):

```
cd lean
lake exe cache get
lake env lean LogUnimodality.lean
```

Python 3 with NumPy, mpmath and Matplotlib:

```
cd computations
python numerics.py
python lscan.py
python rmt.py 6 1000 16
python thmB_density.py
python check_thmC.py
python make_figures.py
```

The paper builds with `pdflatex main.tex` (three passes) in `paper/`.
