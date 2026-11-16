# Stationary measures of planar kinetically constrained models with bounded conditional odds

Yitzchak Shmalo

Martinelli, Shapira and Toninelli conjectured that every stationary measure of a kinetically constrained
spin model on Z^d is a mixture of the equilibrium product measure conditioned on the fibers of bootstrap
percolation (Long time behaviour of one facilitated kinetically constrained models: results and open
problems, arXiv:2510.20461). In dimension one, and for translation invariant stationary measures in every
dimension, stationarity is known to imply detailed balance. The paper proves that on Z^2 every stationary
measure whose single-site conditional probabilities are bounded away from 0 and 1 satisfies detailed
balance, without translation invariance and although the transition rates vanish on a large set. If large
boxes are also internally spanned at every positive density, such a measure is the equilibrium product
measure; this applies to the one- and two-neighbour Fredrickson-Andersen models at every density. The
proof adapts the entropy argument of Holley and Stroock to degenerate rates. The paper also records the
classification of all stationary measures of the one-neighbour model on strips Z x H with H finite.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/finite_checks.py`: exact checks, in rational arithmetic, for FA-1f and FA-2f on small boxes with
  filled, empty and periodic boundary conditions (40 cases): the product weight on each bootstrap fiber is
  stationary and reversible, and the space of stationary vectors has dimension equal to the number of
  fibers. Pure Python 3, no dependencies. Run `python code/finite_checks.py` from the repository root
  (about two minutes).
- `data/finite_checks.json`: the output of that script.
- `SHA256SUMS`: checksums of the files above.

The checks are not part of the proof.

## License

MIT, see `LICENSE`.
