# Corner angles of sandpile aggregates on a background of holes

Companion material for the paper of the same title (Y. Shmalo, October 2026). [Read the paper](paper/main.pdf).

Start the abelian sandpile on ℤ² with n chips at the origin, on a background in which every site absorbs the first H
chips it receives (for H < 0, every site starts with −H chips), and let S_{n,H} be the set of sites that fire.
Holroyd, Levine, Mészáros, Peres, Propp and Wilson (*Chip-firing and rotor-routing on directed graphs*, 2008,
Question 6.2) asked whether the limiting shape of S_{n,H} is a regular (4H+12)-gon. For H = −2 the set is a square for
every n, as Fey-den Boer and Redig showed. The paper shows that for H ≥ −1 no limit of the rescaled sets is a regular
(4H+12)-gon.

**Theorem 1.** Let H ≥ −1 be an integer, let n_j → ∞ and c_j > 0, and suppose that c_j S_{n_j,H} → K in the Hausdorff
metric. If K coincides near a point p with a closed sector of vertex p and opening α ∈ (0, π), then

α > π/2  and  sin α ≤ 1/(H+3).

**Corollary 2.** If such a limit K is a convex polygon with m vertices, then m is divisible by 4 and
m ≥ 2π / arcsin(1/(H+3)) > 4H+12. So m ≥ 12 for H = −1 (with equality only if every interior angle is 5π/6), m ≥ 20 for
H = 0, and in general m ≥ 4H+16.

The corners of a regular (4H+12)-gon have sin α = sin(π/(2(H+3))) > 1/(H+3), so they violate Theorem 1. The theorem
does not say that a limit exists or that it is a polygon. The proof works with the odometer. The least action
principle of Fey, Levine and Peres gives a reflection inequality, a count of last firings in the manner of Le Borgne
and Rossin gives a weighted lower bound for the final configuration, and the compactness argument of Pegden and Smart
passes both to a limit U ≥ 0 with ΔU = s, where H+2 ≤ s ≤ H+3 on the limit set and s = 0 outside it. A corner lemma
for such functions, proved by testing the equation against cos 2θ and the mean value inequality, gives the bound.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/checks.py`: computations (NumPy, Numba, SymPy, mpmath). Part A stabilizes S_{n,H} for H = −2, …, 2 and
  n = 4^5, …, 4^8, and n = 4^9 for H = −1, 0, and checks conservation, the final heights, the dihedral symmetry,
  monotonicity in n, the order-ideal property, the weighted last-firing inequality and the square at H = −2, and
  prints the inner and outer radii beside the constants of Levine and Peres. Part B checks the symbolic identities
  used in the corner lemma.
  Part C checks that the regular 4k-gon violates the corner inequality for k = 2, …, 1000 and that the explicit corner
  solutions of Remark 4.3 satisfy the lemma's hypotheses. It needs Python 3 with these four packages and runs in about
  seven minutes. `code/checks_output.txt` is its output.
- `code/Corner.lean`: the calculus and trigonometry of the corner lemma (the integrals of cos 2θ over sectors, the
  radial form of the Laplacian, the logarithmic growth of the quotient, the circle mean), Jordan's inequality, the
  angles of the regular polygon and the vertex counts of Corollary 2, checked with Lean 4.33.1 and Mathlib (commit
  0df444a360eaa60ab8c11dca51a86af692955474). `code/lean_output.txt` is the output of the check.
- `SHA256SUMS.txt`: checksums of the files above.

## Running the checks

    python code/checks.py > code/checks_output.txt

For the Lean file, in a Lake project that depends on Mathlib at the commit above:

    lake env lean Corner.lean

## Citation

Y. Shmalo, Corner angles of sandpile aggregates on a background of holes, 2026,
https://github.com/yspennstate/sandpile-holes-corner-angles
