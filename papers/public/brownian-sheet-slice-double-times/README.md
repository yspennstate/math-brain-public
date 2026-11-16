# Double times on slices of the Brownian sheet in dimensions four and five

Yitzchak Shmalo

Let B be a d-dimensional Brownian sheet. For s > 0 the slice t -> B(s, t) is a multiple of Brownian
motion in R^d, so for d >= 4 a fixed slice has no double points, while for d in {4, 5} there are random
exceptional slices that have them. Khoshnevisan (Slices of a Brownian sheet: new results and open
problems, Open Problem 2) asked whether, outside a single null set, the set of double times of every
slice has Hausdorff dimension zero when d is 4 or 5.

The paper proves that it does. Almost surely, for every s > 0, the set of pairs u != v with
B(s, u) = B(s, v) has Hausdorff dimension zero, and its part in a product of two disjoint compact
intervals has upper box dimension zero. For d = 5 both statements also follow from the finiteness of
these sets stated in K. Chen's EPFL thesis (2026); the new case is d = 4. The proof bounds high moments of the number of
near-coincidences on a grid, using a conditional variance bound obtained from Brownian bridges, and
takes a union over a grid of slices whose cost is absorbed by the choice of the moment.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/check_lemmas.py`: numerical checks of the conditional variance bound (Lemma 2.1) on random
  configurations with repeated endpoints, and of the lattice sum (Lemma 3.1). Requires Python 3 and NumPy.
  Run `python code/check_lemmas.py` from the repository root.
- `data/lemma_checks.json`: the output of that script (seed 17017).
- `SHA256SUMS`: checksums of the files above.

The checks are not part of the proof.

## License

MIT, see `LICENSE`.
