# Polynomial components in spectrally subcritical percolation on near-regular graphs

Yitzchak Shmalo

Keep each edge of a finite graph G with probability p = (1 - eps)/lambda, where lambda is the spectral radius and
Delta the maximum degree. Christoph, Morawski and Wigderson (arXiv:2608.19145, Question 5.2) asked for the size of
the largest component in this regime, in particular for graphs with Delta <= (1 + delta) lambda. The paper shows that
the answer turns on (1 - eps)(1 + delta). Below one the largest component is O(log n), by a known maximum-degree
argument. Above one there are connected graphs, a clique joined to a blown-up regular tree, whose largest component
has at least n^c vertices with high probability, with lambda of any order n^a, 0 <= a < 1. At one the largest
component is O((log n)^3). A refinement of the resolvent bound of Christoph, Morawski and Wigderson is proved for
graphs with bounded ratio Delta/lambda. The optimal exponent in the polynomial regime is open.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/verify.py`: independent small-graph checks of the edge sampler, the spectral computations (full matrices
  against quotients), the component counts, the second-moment recursion and the example of Remark 2.4; writes
  `data/verification.json`.
- `code/simulate.py`: 40 percolation samples on each of 30 host graphs of up to 1,118,688 vertices, with exact
  Bernoulli edges by geometric skipping and SciPy connected components; writes `data/summary.csv`, `data/trials.csv`,
  `data/hosts.json`, `data/simulation_metadata.json` and `data/simulation_progress.txt`.
- `code/analyze.py`: least-squares fits of log median L1 against log n with bootstrap intervals; writes
  `data/fits.csv`, `data/fit_notes.txt` and `data/scaling.svg`.
- `SHA256SUMS`: checksums of the files above.

Python 3 with NumPy and SciPy (the recorded run used NumPy 2.2.3 and SciPy 1.15.2); `analyze.py` also uses
matplotlib. Run the scripts from the repository root, for example `python code/simulate.py`. The simulation took
about 11 seconds and 1 GB of memory. The scripts use the Unix `resource` module, so run them on Linux or macOS. The
computations are not part of any proof, and the fitted slopes are descriptive only.

## License

MIT, see `LICENSE`.
