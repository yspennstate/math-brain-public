SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T09:45:44Z.

attacking: rank-budget spectral-window shield: large low-rank coupling leakage costs protected-mode count, not magnitude.

# account03/B12 r30 — rank-budget leakage shield and reserve-versus-volume alternative

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T094544Z-qform-eigenvalue-r30`  
Assignment: additional eigenvalue control  
Status: **PROVED_SUPPORTING_THEOREM / FULL_QFORM_OPEN / NOT_INDEPENDENTLY_REVIEWED**  
Continuity: **proved only on the volume branch below; not claimed for the spectral-shield branch**.

## 1. Exact target and what is new

The full target remains: for every dimension, every independent real input with marginal density bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal density bound for `X^T A X`, or give a counterexample.

This report proves a deterministic spectral stability theorem useful for the assigned problem of adding arbitrary smaller/larger eigenvalues. It improves the previous spectral-window shield by replacing the full leakage norm `||BQ||op` with the **(k+1)-st leakage singular value**. Consequently the first `k` leakage directions may have arbitrarily large magnitude and either sign effect; they cost protected-mode count, not size.

The theorem never treats a small matrix as a small random quadratic variable and never rotates the random vector. All rotations below are deterministic matrix algebra inside an actual original-coordinate principal block.

## 2. Sources actually consumed

Initial fresh brain main for this run: `b62a5a6a771e37a12087944f73ce0a0f78ef2ec1`; OWNER CONTROL revision `2026-09-22.15`; programme revision `2026-09-22.5`.

Required partner theorem actually used at equations:

- `yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`
- in particular its exact complementary-Schur factorization and shear singular-value constant.

Newest required volume source actually used at equations:

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`
- `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`
- specifically its fractional three-volume theorem at `q=1`.

Finite-dimensional analytic receiver used only after an ACTUAL original-coordinate block is certified:

- `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`
- `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Theorem 3.1 / Corollary 4.1.

Current corrections were respected: no uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint coarea lemma, no worst conditional-density-moment gate, and no naive fiber-sup integration.

## 3. Main theorem: rank-budget spectral-window shield

Let `I` be an ACTUAL set of original coordinates. Split it into two disjoint ORIGINAL-coordinate banks, and write the corresponding principal block as

\[
H=\begin{pmatrix} C&B\\ B^T&D\end{pmatrix}.
\tag{3.1}
\]

The random coordinates are never transformed. For deterministic matrix algebra only, let `P` be an orthogonal reducing projection of `D`, put `Q=I-P`, and write

\[
D_P=D|_{\operatorname{Ran}P}.
\]

Assume `D_P` is invertible and has at least `j+2k` singular values at least `mu>0`, where `j>=1`, `k>=0`. Define

\[
R=BP D_P^{-1},\qquad
\rho=\|R\|_{\rm op},\qquad
\ell(\rho)=\frac{\sqrt{\rho^2+4}-\rho}{2},
\tag{3.2}
\]

and use the convention `s_{k+1}(BQ)=0` when `rank(BQ)<=k`.

### Theorem 3.1 (`QFORM-RANK-BUDGET-LEAKAGE-SHIELD-v1`)

Under the hypotheses above,

\[
\boxed{
 s_j(H)\ge
 \mu\,\ell(\rho)^2-s_{k+1}(BQ).
}
\tag{3.3}
\]

In particular, if `D_P` supplies `2k+3` protected singular modes,

\[
\boxed{
 s_3(H)\ge
 \mu\,\ell(\rho)^2-s_{k+1}(BQ).
}
\tag{3.4}
\]

Thus the first `k` singular directions of the coupling into the unprotected spectral sector are **completely free in magnitude**. If `rank(BQ)<=k`, their cost is exactly zero.

The complementary spectrum `D_Q=QDQ|Ran(Q)` is completely unrestricted: singular, tiny, huge, mixed-sign, and arbitrarily clustered are all allowed.

### Proof

Work in an orthonormal basis adapted to `P,Q` inside the second physical bank. This is only a matrix basis change; no probabilistic independence is asserted in that basis.

First delete the `BQ` coupling and set

\[
H_0=
\begin{pmatrix}
 C & BP & 0\\
 PB^T & D_P & 0\\
 0&0&D_Q
\end{pmatrix}.
\tag{3.5}
\]

The active upper-left block factors exactly as

\[
H_{\rm act}
=L\begin{pmatrix}S&0\\0&D_P\end{pmatrix}L^T,
\qquad
L=\begin{pmatrix}I&R\\0&I\end{pmatrix},
\tag{3.6}
\]

with

\[
S=C-BP D_P^{-1}PB^T.
\tag{3.7}
\]

This is the account04/B12 complementary-Schur factorization. Its exact shear calculation gives

\[
\sigma_{\min}(L)=\ell(\rho).
\tag{3.8}
\]

The block diagonal matrix in (3.6) has at least `j+2k` singular values at least `mu`, regardless of `S`. For singular values under two-sided invertible multiplication,

\[
s_r(P_1MP_2)\ge
\sigma_{\min}(P_1)\sigma_{\min}(P_2)s_r(M).
\]

Hence

\[
s_{j+2k}(H_{\rm act})\ge \mu\ell(\rho)^2.
\tag{3.9}
\]

Adding the direct summand `D_Q` cannot decrease the `(j+2k)`-th singular value, so

\[
s_{j+2k}(H_0)\ge g,
\qquad g:=\mu\ell(\rho)^2.
\tag{3.10}
\]

Now take a best rank-`k` singular-value truncation

\[
BQ=K+F,\qquad \operatorname{rank}K\le k,\qquad
\|F\|_{\rm op}=s_{k+1}(BQ).
\tag{3.11}
\]

The symmetric off-diagonal update generated by `K`,

\[
E_K=
\begin{pmatrix}
0&0&K\\
0&0&0\\
K^T&0&0
\end{pmatrix},
\]

has rank at most `2k`. Singular-value rank interlacing gives

\[
s_j(H_0+E_K)\ge s_{j+2k}(H_0)\ge g.
\tag{3.12}
\]

For completeness, (3.12) follows from the Weyl inequality applied to
`H_0=(H_0+E_K)+(-E_K)` and `s_{2k+1}(E_K)=0`.

The residual symmetric update

\[
E_F=
\begin{pmatrix}
0&0&F\\
0&0&0\\
F^T&0&0
\end{pmatrix}
\]

has operator norm exactly `||F||op`. Ordinary Weyl perturbation therefore yields

\[
s_j(H)
\ge s_j(H_0+E_K)-\|E_F\|_{\rm op}
\ge g-s_{k+1}(BQ),
\]

proving (3.3). QED.

## 4. Optimal reserve form and a local dense tail

Suppose `D_P` contains `r>=3` protected singular modes at scale `mu`. The largest completely free leakage rank available while retaining three protected modes is

\[
K=\left\lfloor\frac{r-3}{2}\right\rfloor.
\tag{4.1}
\]

Hence

\[
\boxed{
 s_3(H)\ge
 g-s_{K+1}(BQ),
\quad
 g=\mu\ell(\rho)^2.
}
\tag{4.2}
\]

If the final physical block is `H+T` with an arbitrary symmetric local tail satisfying only

\[
\|T\|_{\rm op}\le\delta,
\]

then

\[
\boxed{
 s_3(H+T)\ge g-s_{K+1}(BQ)-\delta.
}
\tag{4.3}
\]

Again, `T` is retained as a matrix perturbation. No statement is made that `X^T T X` is small for unbounded inputs.

## 5. Dependence-safe density corollary on a bounded actual core

Assume the block in Section 3 uses exactly `m` ORIGINAL coordinates and

\[
\gamma:=g-s_{K+1}(BQ)-\delta>0.
\]

Condition on every original coordinate outside this block. The remaining `m` variables stay independent with density caps one; all outside couplings become arbitrary affine terms. The finite-dimensional projected-gradient theorem therefore gives

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le {2\sqrt{6\pi m}\over\gamma}.
}
\tag{5.1}
\]

All matrix blocks outside the chosen physical core, and hence all additional outside eigenvalues and cross-couplings, are unrestricted. This is an essential-supremum conclusion. Continuity is not claimed in this branch.

This is an equation-level application of the account04/B12 shield: their exact factorization supplies `g`; the new rank-budget argument shows that arbitrarily large low-rank leakage need not be paid in operator norm.

## 6. Explicit arbitrary-magnitude rank-two leakage family

Take a 12-coordinate physical core split as `3+7+2`. In the displayed deterministic basis, which here may be chosen to coincide with the original coordinates, let

\[
D_P=\operatorname{diag}(2,-2,2,-2,2,-2,2),
\qquad BP=0,
\tag{6.1}
\]

while `C` is any symmetric `3x3` matrix, `D_Q` is any symmetric `2x2` matrix, and `BQ` is an arbitrary `3x2` matrix with **no norm bound whatsoever**.

Here `r=7`, `K=2`, `rho=0`, `ell(0)=1`, `g=2`, and

\[
s_3(BQ)=0
\]

because `BQ` has at most rank two. Therefore

\[
\boxed{s_3(H)\ge2}
\tag{6.2}
\]

for every magnitude and sign configuration hidden in `C,D_Q,BQ`. With no additional local tail, (5.1) gives

\[
\boxed{
\|p_Q\|_\infty\le\sqrt{72\pi}
=15.039769647786\ldots .
}
\tag{6.3}
\]

Arbitrarily many further coordinates with arbitrary spectrum and arbitrary couplings can be adjoined outside this 12-coordinate core at zero extra cost after conditioning on those ORIGINAL coordinates.

This concrete family demonstrates the point of the theorem: an arbitrarily large coupling is not automatically hostile if its rank can consume only finitely many protected modes.

## 7. Newest volume theorem applied: reserve-versus-volume alternative

The previous theorem also gives a structural alternative with the newest fractional-volume result.

Let `r>=7`, so `K=floor((r-3)/2)>=2`, and put

\[
\varepsilon=s_{K+1}(BQ).
\]

Recall that `B` itself is the ACTUAL original-coordinate cross block in (3.1). Since `P,Q` are orthogonal,

\[
BB^T=BPB^T+BQB^T\succeq BQB^T.
\tag{7.1}
\]

If

\[
\varepsilon\ge g/2,
\tag{7.2}
\]

then `K+1>=3`, hence

\[
s_3(B)
\ge s_3(BQ)
\ge s_{K+1}(BQ)
\ge g/2.
\tag{7.3}
\]

Suppose additionally that one side of this ORIGINAL-coordinate cross block is diffuse in the exact volume sense; after swapping the two banks if necessary, assume

\[
\max_i(P_{\operatorname{Ran}B})_{ii}\le1/2.
\tag{7.4}
\]

Apply the fractional three-volume theorem from `c2414ef...` with `M=B`, `q=1`. Its row-volume marginals obey `alpha_i<=1/2`, and

\[
E_3(B^TB)^{1/6}\ge s_1(B)s_2(B)s_3(B)\,^{1/3}\ge s_3(B),
\]

more directly

\[
E_3(B^TB)\ge s_1(B)^2s_2(B)^2s_3(B)^2\ge s_3(B)^6.
\tag{7.5}
\]

Therefore the **full ambient quadratic form**, with arbitrary self blocks and outside couplings, has a continuous `C_0` density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le {3e\over s_3(B)}
\le {6e\over g}.
}
\tag{7.6}
\]

This is a genuine application of the newest Claude-derived volume theorem to the actual remaining inequality.

On the complementary case

\[
\varepsilon<g/2,
\]

Theorem 3.1 gives

\[
s_3(H)>g/2.
\tag{7.7}
\]

Thus, whenever the actual physical core has bounded size `m<=M`, the two branches combine to

\[
\boxed{
\|p_Q\|_\infty
\le {1\over g}
\max\{4\sqrt{6\pi M},\,6e\},
}
\tag{7.8}
\]

provided the cross block satisfies the diffuse gate (7.4). The volume branch is continuous; the shield branch is only asserted essentially bounded.

Equation (7.8) is not the full conjecture: the remaining difficult case can have an unbounded physical core and/or a high-leverage cross block on both sides.

## 8. Why this is not an independence or convolution argument

The spectral projection `P` is never applied to the random vector as a probabilistic coordinate change. It is used only to prove a singular-value lower bound on an ACTUAL physical principal block. The probabilistic step, when used, conditions exclusively on ORIGINAL coordinates.

Likewise, the volume branch is applied only to the actual original-coordinate cross matrix `B`; it is not applied to the rotated matrix `BQ`. This distinction is essential because spectral rotation destroys product independence.

No moment, compact support, connected support, Gaussianity, log-concavity, or diagonal-basis hypothesis is used.

## 9. Computation

`CHECK.py` and `CHECK_RESULT.json` accompany this report. With deterministic seed `20260923094544`:

- 10,000 random mixed-sign/singular-tail instances produced zero violations of (3.4); minimum numerical margin was `0.3618416852796056`.
- 5,000 random projection instances produced zero violations of the auxiliary inequality `s3(B)>=s_{K+1}(BQ)` used in Section 7; minimum sampled margin was `0.19661902999074066`.
- the explicit rank-two leakage family was tested at leakage amplitudes `1e-6,1,1e3,1e6`; its sampled `s3` remained above the proved lower bound 2 and in fact grew at large amplitude.
- `sqrt(72*pi)=15.039769647786002` and `48sqrt(3)e/5=45.19874146735002` were recorded as arithmetic controls.

These are finite consistency checks only. The proof above is analytic; no histogram or Monte Carlo claim is used as evidence for the universal conjecture.

## 10. Remaining gap

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

The new theorem removes a specific obstruction: a few arbitrarily large coupling directions into an unprotected spectral sector do not need to be paid by operator norm when there is a reserve of protected complementary modes.

The unresolved structural step is to start only from `s3(A)>=1` and force, with universal constants, at least one of:

1. a bounded original-coordinate core with enough protected complementary reserve for (5.1);
2. a diffuse actual cross block triggering (7.6) or the more general three-volume theorem;
3. an already-paid grouped-bank, hub, ridge, physical-pair, or affine-rank-two mechanism.

The complementary unpaid geometry is a high-leverage, product-structured coupling in which protected spectral reserve is spread over too many original coordinates and the actual cross block is concentrated on both sides. That is the next B12 target.

No full-solution claim and no continuity claim outside the volume branch are made.
