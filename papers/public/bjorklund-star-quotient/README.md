# A homogeneous space with no nonconstant quasiharmonic functions

Yitzchak Shmalo

M. Björklund, in *Five remarks about random walks on groups* (arXiv:1406.0763, Appendix II, Problem 2), asks for a countable measured group (G, μ) and a subgroup H of infinite index such that G/H admits no nonconstant left μ-harmonic or μ-quasiharmonic functions.

The paper gives such an example. G is the group of finitely supported permutations of {0, 1, 2, ...}, H is the stabiliser of 0, and μ gives mass p_n > 0 to each transposition (0 n), with the p_n summing to 1. The walk induced on G/H is a walk on an infinite star. At a leaf k the quasiharmonic equation forces u(k) = u(0) − c/p_k, where c is the defect. The equation at the centre is then a series whose terms tend to −c, so c = 0 and u is constant. G is not finitely generated and μ has infinite support; the finitely generated case is not treated.

- `paper/main.pdf`, `paper/main.tex`: the paper.
- `code/checks.py`: exact checks (Python 3, standard library) of the identities used in the proof on finite truncations. Run `python code/checks.py`; its output is in `code/checks_output.txt`.
- `SHA256SUMS.txt`: hashes of the files above.
