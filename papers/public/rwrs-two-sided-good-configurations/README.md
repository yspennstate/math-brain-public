# Good configurations of random walk in random scenery under two-sided conditioning

Yitzchak Shmalo

Let S be a nearest-neighbour walk on Z with probability p of a step to the right, and let Y_t = C(S_t) be the colour
record of an independent scenery of fair signs. Den Hollander and Steif conjectured (Random walk in random scenery: a
survey of some recent results, IMS Lecture Notes 48, 2006, Conjecture 2.16) that, when Y_0 is conditioned on the
colours at all nonzero times, every configuration is bad for 1/2 <= p < 4/5 and every configuration is good for
4/5 < p <= 1. The paper proves that every configuration is good for 27/28 < p <= 1: the finite-window conditional
probabilities converge uniformly, with an explicit modulus, to a version of the conditional probability that is
continuous everywhere. For colours with P(C=1) = alpha the same holds for p > 27/(27 + 4 beta^2), beta = min(alpha,
1 - alpha). The range 4/5 < p <= 27/28 and the bad half remain open.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/rwrs_exact.py`: exact finite-window conditional probabilities by a transfer over (position, range, colours),
  in integer and `fractions.Fraction` arithmetic, with self-checks against brute-force enumeration and against the
  interval-gas formula of the paper.
- `code/run_evidence.py`: computes the 840 comparisons of Remark 6.3 and writes `data/finite_windows.csv` and
  `data/computation_summary.txt`.
- `code/audit_proof.py`: checks the block structure, the bound L <= 3 ell and the bound h - r <= 2 ell on every block of
  every step sequence of length at most 14, and writes `data/proof_audit.txt`.
- `SHA256SUMS`: checksums of the files above.

Python 3, standard library only. The two scripts that write data refuse to run unless the process niceness is at least
10 and use the Unix `resource` module, so run them on Linux or macOS, for example `nice -n 10 python code/run_evidence.py`
from the repository root (about a minute). The computations are not part of the proof.

## License

MIT, see `LICENSE`.
