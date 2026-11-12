# The binary and ternary harmonic measures of the Cantor set are mutually singular

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (LaTeX source in `paper/main.tex`).

Let E be the middle-thirds Cantor set. For an integer b ≥ 2, the coding tree of E in base b has as its vertices the b-adic intervals that meet E. Simple random walk on this tree is transient, and the law of its limiting end, pushed forward to E, is a probability measure ν_b; the measure ν_3 is the Cantor measure. Lyons and Peres (Probability on Trees and Networks, Question 16.7) asked whether ν_2 and ν_3 are mutually singular.

**Theorem 1.1.** The measures ν_2 and ν_3 are mutually singular.

The proof compares the conditional splits of the two measures on dyadic cells through Hellinger affinities. At the dyadic cell [4/128, 5/128], whose intersection with E is the ternary cylinder [8/243, 9/243], the Cantor measure splits evenly while the harmonic measure, computed as an electrical current, gives the left half more than 0.507 of the mass; the gap persists for nearby positions and scales of the cylinder. A Fourier argument based on Stewart's theorem on digit changes in the bases 2 and 3 shows that, if the measures were not singular, such cells would carry a fixed share of their overlap at infinitely many levels, which contradicts the summability of the Hellinger losses.

## Computations

`code/check_gap.py` (Python 3, standard library only; output in `code/check_gap_output.txt`) works with exact rational numbers. It computes the Cantor function at rational points, decides membership in E, and checks the description of the base cell, the membership claims used in Lemma 4.2, the flow energy and its tail on the left half, the radius-six wired conductance on the right half, and the resulting bound on the split.

`lean/CantorGapArithmetic.lean` is a Lean 4 file without external libraries. It checks by kernel evaluation the integer identities and inequalities behind the rational values of Section 4. The proofs in the paper depend on the files only through the numerical values stated there.

`SHA256SUMS.txt` lists the hashes of the files.
