# Frozen edges of stationary tridiagonal dynamics with GUE spectra

Yitzchak Shmalo

Virag (Operator limits of random matrices, ICM 2014, Question 8) asked whether matrix-valued Brownian motion has an
operator limit. A natural candidate is a stationary diffusion on tridiagonal matrices with the Dumitriu-Edelman law
of the Gaussian unitary ensemble at every time. The paper shows that the simplest such diffusion, with independent
Ornstein-Uhlenbeck diagonal entries and independent radial Ornstein-Uhlenbeck off-diagonal entries, has frozen edge
eigenvalues on the time scale on which Dyson Brownian motion moves: for each fixed k, the k largest edge-scaled
eigenvalues converge uniformly on compact time intervals to a vector that does not depend on time, at rate
O(n^{-1/4} (log n)^{1/4}), so they do not converge to the Airy line ensemble. The same holds for every stationary
reversible tridiagonal diffusion with this invariant law whose entry noise is bounded uniformly in the dimension, and
an exact tridiagonal realization of Dyson Brownian motion with these marginals needs entry noise whose covariance
operator grows at least like n^{1/4} (log n)^{-1/4}. Virag's question remains open.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/simulate.py`: exact-transition paths of Hermitian Brownian motion (dense) and of the tridiagonal
  Ornstein-Uhlenbeck process at edge times s = 0, 1/4, 1, 3; writes `data/edge_samples.csv`,
  `data/edge_energies.csv` and `data/edge_metadata.json`.
- `code/analyze.py`: correlations with bootstrap intervals and mean squared increments; reads the two sample files
  and writes `data/summary.csv`, `data/energy_summary.csv`, `data/SUMMARY.txt` and `data/edge_comparison.svg`.
- `code/audit_math.py`: numerical checks of the normalizations and of the inequalities used in the proofs; writes
  `data/math_audit.json`.
- `data/`: the summaries behind Table 1 of the paper and the run metadata. The raw sample files (about 2 MB), the
  text summary and the figure are not included; `simulate.py` and `analyze.py` regenerate them.
- `SHA256SUMS`: checksums of the files above.

Python 3 with NumPy, SciPy, threadpoolctl and matplotlib. Run the scripts from the repository root, for example
`python code/simulate.py` and then `python code/analyze.py`. The recorded run used base seed 4620261113, took
about 5 minutes on one thread and peaked at about 700 MB of memory. `simulate.py` uses the Unix `resource` module,
so run it on Linux or macOS. The computations are not part of any proof.

## License

MIT, see `LICENSE`.
