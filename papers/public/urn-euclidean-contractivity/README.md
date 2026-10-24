# On a contractivity question of Neri and Pinto for generalized Pólya urns

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (LaTeX source in `paper/main.tex`).

Let R be the replacement matrix of a balanced d-colour generalized Pólya urn with balance λ, and let H be the hyperplane of vectors with coordinate sum zero. Neri and Pinto (arXiv:2607.07309, Remark 3.7) asked whether, for every tenable irreducible urn, the form w ↦ ⟨w(R − λI), w⟩ is negative definite on H for the Euclidean inner product on all d coordinates or on the first d − 1 of them (their Proposition 3.6 with p = d or p = d − 1). A positive answer would give rates in the strong law U(n)/T(n) → u for every such urn.

**Theorem 1.1.** For two colours both readings hold for every irreducible urn, with constant R₀₁ + R₁₀.

**Theorem 1.2.** For every d ≥ 3 there is an irreducible d-colour urn with nonnegative integer entries for which both readings fail, under every ordering of the colours (balance 6 for d ≥ 4, balance 100 for d = 3). There is also a six-colour example of balance 6 whose non-principal eigenvalues all have real part below λ/2. Read over all of ℝ^d, the case p = d never holds, since the all-ones vector gives the value 0.

**Theorem 1.3.** Let γ be the largest real part of an eigenvalue of R other than λ. For an irreducible urn γ < λ, and the Lyapunov equation on H gives, for every A < λ − γ, a positive semidefinite P, positive definite on H, with ⟨w(R − λI), w⟩_P ≤ −A‖w‖²_P on H. No such P does better than λ − γ.

**Corollary 1.4.** The rate theorem of Neri and Pinto (their Theorem 3.2) applies to every tenable irreducible urn with an adapted inner product, and their fast-rate theorem (Theorem 3.3, which needs A > λ/2) applies in this way exactly when γ < λ/2.

## Computations

`code/checks.py` (Python 3 with NumPy, SymPy and SciPy; output in `code/checks_output.txt`) checks the algebraic identities of the paper symbolically, the integer examples for d = 3, 4, ..., 60 and the six-colour example, the characteristic polynomial of the six-colour example, the relabelling invariance, the numerical values of the readings, and the Lyapunov construction on five of the urns.

`lean/UrnContractivity.lean` is a Lean 4 file without external libraries. It proves by kernel evaluation that the vectors of the paper for d = 3, 4, 5, 6 and the six-colour example lie in H and make each reading positive. The proofs in the paper do not depend on either file.

`SHA256SUMS.txt` lists the hashes of the files.
