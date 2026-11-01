# P04/D0038 source-convention erratum for `2026-09-20T00-19-58Z__report.md`

This immutable correction preserves the original report and fixes one endpoint/spacing transcription before the run is reported as complete. **The vector-algebraic no-go theorem remains valid; only the numerical separation constants and the induced one-dimensional dependence-range wording change.**

Bradley (1994), p. 593, defines

`G_{i,m}={k in Z^d : k_i < m}`

and

`H_{i,m}={k in Z^d : k_i > m}`,

and calls the field lattice-halfspace one-dependent when

`sigma(X_k:k in G_{i,m})` is independent of `sigma(X_k:k in H_{i,m+2})`

for every coordinate `i` and integer `m`.

Therefore the first report's display using `k_i<=m` versus `k_i>=m+2` should not be read as the literal source convention.

## Corrections to the proofs

### Vector-algebraic no-go

In Lemma 5.1, after Frobenius dilation, choose `n` so large that the distance in the selected coordinate between the rightmost point of the support of `L^(p^n)g` and the leftmost point of the support of `Rr^(p^n)g` is at least **4**, rather than merely 2. Then, writing the left support maximum as `a`, choose `m=a+1`; the left representative lies in `{k_i<m}`, and a right support minimum at least `a+4` lies in `{k_i>m+2}`. Bradley's exact halfspace independence applies. Since the Frobenius dilation makes the gap arbitrarily large, this correction changes no conclusion.

### Finite-cylinder tail evaporation

For a fixed finite transverse section `F` and `Y_n=(X_(n,u):u in F)`, the exact source definition gives

`sigma(Y_n:n<m) independent of sigma(Y_n:n>m+2)`.

Equivalently, in the standard past/future notation,

`sigma(Y_n:n<=j) independent of sigma(Y_n:n>=j+4)`

for every `j`.

Thus the induced strip sequence has a finite dependence range (its absolute-regularity coefficient is exactly zero for separations `n>=4`), rather than the first report's over-sharp wording `1-dependent` / `beta(n)=0 for n>=2`. It is still absolutely regular, so Bradley's standard implication `absolute regularity => trivial double tail` applies unchanged. Reverse martingale convergence therefore still gives

`I(Z ; sigma(Y_n:|n|>=N)) -> 0`

for every finite-valued `Z`.

## Corrected status

- `E_finite_tail = 0 -> 0` remains unchanged.
- Theorem 3.1 (no nondegenerate finite-dimensional `F_p`-linear Haar algebraic solution) remains proved with the gap constant corrected from 2 to 4.
- Theorem 8.1 remains proved as a **finite-range-cylinder tail evaporation theorem**; only the dependence-range label is corrected.
- The next attack remains a nonlinear cut-blind widening hierarchical code.
