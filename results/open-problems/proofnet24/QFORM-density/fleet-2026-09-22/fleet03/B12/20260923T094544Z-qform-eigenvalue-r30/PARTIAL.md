SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T09:45:44Z.

attacking: rank-budget spectral-window shield: large low-rank coupling leakage costs protected-mode count, not magnitude.

# Early substantive checkpoint

Let an ACTUAL original-coordinate principal block be written, only for deterministic matrix algebra, as

\[
H=\begin{pmatrix}C&B\\B^T&D\end{pmatrix}.
\]
Choose a reducing spectral projection `P` of `D`, put `Q=I-P`, and assume `D_P=D|Ran(P)` has at least `j+2k` singular values at least `mu>0`. Define

\[
rho=\|BP D_P^{-1}\|_{op},\qquad
ell(rho)=\frac{\sqrt{rho^2+4}-rho}{2},\qquad
varepsilon_k=s_{k+1}(BQ).
\]

The first missing implication is now proved:

\[
\boxed{s_j(H)\ge mu\,ell(rho)^2-varepsilon_k.}
\]

Proof core. Remove the `BQ` coupling. The fleet04/B12 complementary-Schur factorization gives the active block as

\[
L\,diag(S,D_P)L^T,\quad L=\begin{pmatrix}I&BP D_P^{-1}\\0&I\end{pmatrix},
\]
with `sigma_min(L)=ell(rho)`. Hence the decoupled matrix has at least `j+2k` singular values at least `g=mu ell(rho)^2`. Split `BQ=K+R` with `rank(K)<=k` and `||R||op=s_{k+1}(BQ)`. The symmetric off-diagonal update made from `K` has rank at most `2k`, so singular-value rank interlacing leaves `s_j>=g`; restoring `R` costs exactly `||R||op` by Weyl. This proves the display.

In particular, for `j=3`, arbitrarily large leakage of rank at most `k` costs ZERO provided `2k+3` protected complementary modes are available. The arbitrary complementary spectrum `D_Q` is never inverted and may be singular, huge, tiny, or of either sign.

This is a supporting deterministic theorem; the full QFORM conjecture remains open. The final report will add the density corollary, the newest volume-theorem alternative, computations, and exact source pins.
