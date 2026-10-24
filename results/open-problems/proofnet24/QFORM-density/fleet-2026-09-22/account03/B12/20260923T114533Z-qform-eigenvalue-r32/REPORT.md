SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T11:45:33Z.

attacking: singular-value reserve versus arbitrary spectral tails — let finitely many added eigenvalues be completely unbounded and charge only the first unreserved singular value of the added matrix.

# account03/B12 r32 — singular-reserve stability for arbitrary extra spectrum

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T114533Z-qform-eigenvalue-r32`  
Assignment: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / PARTNER RESULT APPLIED / NEWEST VOLUME RESULT APPLIED / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Continuity: **not claimed for the reserve branch; proved for the separate cross-volume branch in its exact scope**.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and mechanism change

The target remains the full arbitrary-law statement: for every dimension, every independent real input with marginal probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal density bound for `X^T A X`, or give a valid counterexample.

The previous B12 run used compression inheritance: arbitrary added spectrum is harmless if it misses a protected compression. This run changes mechanism. It allows the added spectrum to hit the protected physical block in arbitrary orientation. The price is paid by **spectral rank** rather than by magnitude: if the baseline physical block has `r` reserve singular directions beyond the three needed for QFORM, then the largest `r` singular directions of an arbitrary added matrix are completely free, and only the `(r+1)`-st singular value of the addition is charged.

No post-rotation independence is used. Singular-value decompositions below are deterministic matrix algebra only; conditioning, when used, is on ORIGINAL coordinates.

## 2. Sources actually consumed

Initial fresh brain main: `ebf71ec2b7b758e13c2a5c07ce60fb60f39da908`. Final prepublication control refresh before this report: brain main `8eb43713f0d60bb250c47cad0a8a8ac4b32f9ce2`; OWNER CONTROL remained revision `2026-09-22.15`, programme revision `2026-09-22.5`, with no pause/stop for account03/B12. Live correction inbox blob remained `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

Completed designated partner actually applied:

- `yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

The exact congruence factorization and singular-value inequality in its equations (4.7)--(4.10) are used in Section 6 below.

Newest required volume source actually applied:

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`
- `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its stable original-coordinate cross-block theorem is used in Section 7.

Finite-dimensional physical-core receiver used in Sections 5--6 is the current synthesis estimate: an actual original-coordinate principal block of size `m` with three eigenvalues of absolute value at least `gamma>0` gives

\[
\|p_{X^TAX}\|_\infty\le {2\sqrt{6\pi m}\over\gamma},
\]

after conditioning on all outside ORIGINAL coordinates. This receiver allows the resulting affine terms and outside couplings.

Current corrections are respected: no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea bound, no worst-fiber density-moment bound, no single universally good minor, and no claim that small matrix norm makes the random quadratic remainder small.

## 3. Deterministic rank-tail singular-value inequality

For an `m x m` matrix `M`, let

\[
s_1(M)\ge s_2(M)\ge\cdots\ge s_m(M)\ge0
\]

be its singular values.

### Theorem 3.1 (`QFORM-SINGULAR-RESERVE-TAIL-STABILITY-v1`)

Let `B` and `R` be real symmetric `m x m` matrices. For every integer `r>=0` and every `j>=1` with `j+r<=m`,

\[
\boxed{
 s_j(B+R)\ge s_{j+r}(B)-s_{r+1}(R).
}
\tag{3.1}
\]

In particular,

\[
\boxed{
 s_3(B+R)\ge s_{r+3}(B)-s_{r+1}(R).
}
\tag{3.2}
\]

Hence the top `r` singular directions of `R` may have arbitrary magnitude and either sign; only the first singular value outside that rank budget is charged.

### Proof

Because `R` is symmetric, retain in its spectral decomposition the `r` eigenmodes of largest absolute eigenvalue. Call the resulting symmetric rank-`r` matrix `R_r`, and put

\[
E=R-R_r.
\]

Then

\[
\operatorname{rank}R_r\le r,
\qquad
\|E\|_{\rm op}=s_{r+1}(R).
\tag{3.3}
\]

Apply the standard singular-value Weyl inequality to

\[
B=(B+R_r)+(-R_r).
\]

Since `s_{r+1}(R_r)=0`,

\[
s_{j+r}(B)
\le s_j(B+R_r)+s_{r+1}(-R_r)
=s_j(B+R_r).
\tag{3.4}
\]

A second Weyl inequality gives

\[
s_j(B+R_r+E)
\ge s_j(B+R_r)-\|E\|_{\rm op}.
\tag{3.5}
\]

Combining (3.3)--(3.5) proves (3.1). QED.

### Sharpness from this information

The coefficient one and the reserve index `j+r` cannot in general be improved. For example, take

\[
B=\operatorname{diag}(\underbrace{\mu,\ldots,\mu}_{r+3},0,\ldots,0)
\]

and let `R` cancel exactly `r` of those first modes. Then `s_{r+3}(B)=mu`, `s_{r+1}(R)=0`, and the final matrix has exactly three surviving singular values equal to `mu`, so equality holds in (3.2).

## 4. Spectral interpretation for adding arbitrary eigenvalues

Write the added symmetric matrix as

\[
R=\sum_{k=1}^m \tau_k v_kv_k^T,
\qquad
|\tau_1|\ge\cdots\ge|\tau_m|.
\tag{4.1}
\]

Then

\[
s_{r+1}(R)=|\tau_{r+1}|.
\tag{4.2}
\]

Therefore, if a baseline physical block has `r+3` singular values at least `mu` and all but the largest `r` added eigenvalues have magnitude at most `delta`, then

\[
\boxed{
s_3(B+R)\ge \mu-\delta.
}
\tag{4.3}
\]

The largest `r` added eigenvalues are unrestricted in sign and magnitude and their eigenvectors may be arbitrarily oriented relative to the baseline. This is genuinely stronger than an operator-norm perturbation bound when a few added modes are enormous.

## 5. Physical-core density compiler

Let `I` be an ACTUAL set of original coordinates, `|I|=m`, and split the final physical block as

\[
A[I,I]=B+R.
\]

### Corollary 5.1 (`QFORM-PHYSICAL-RESERVE-TAIL-COMPILER-v1`)

If for some `r>=0`

\[
s_{r+3}(B)\ge\mu,
\qquad
s_{r+1}(R)\le\delta<\mu,
\tag{5.1}
\]

then the full ambient quadratic form, with every matrix block outside `I` and every outside coupling arbitrary, has an essentially bounded density satisfying

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le
{2\sqrt{6\pi m}\over \mu-\delta}.
}
\tag{5.2}
\]

### Proof

Theorem 3.1 gives `s_3(A[I,I])>=mu-delta`. Condition on all ORIGINAL coordinates outside `I`. The variables indexed by `I` remain independent with density caps one. Outside quadratic terms become an additive constant and cross terms become deterministic affine terms. Apply the finite-dimensional physical-core receiver uniformly in the conditioning and average the interval bounds. QED.

### Concrete example

Take `m=8`, `r=2`, a baseline physical block with

\[
s_5(B)\ge2,
\]

and add an arbitrary symmetric `R` whose two largest singular values are completely unrestricted while

\[
s_3(R)\le1/4.
\]

Then

\[
s_3(B+R)\ge 7/4
\]

and

\[
\boxed{
\|p_Q\|_\infty
\le {2\sqrt{48\pi}\over 7/4}
=14.0341948518\ldots .
}
\tag{5.3}
\]

This remains true after adjoining arbitrarily many original coordinates with arbitrary additional spectrum and couplings.

## 6. Actual application of account04/B12: complementary shield plus a second arbitrary spectral packet

The designated account04/B12 r4 theorem uses a physical block

\[
H_0=B+U\Theta U^T
\]

and an orthogonal deterministic decomposition `[W,Z]`, with complementary block

\[
D=Z^TBZ,
\qquad
R_0=B_{12}D^{-1},
\qquad
\rho=\|R_0\|_{\rm op},
\qquad
\ell(\rho)={\sqrt{\rho^2+4}-\rho\over2}.
\]

Its completed proof gives the exact factorization

\[
\widehat H_0
=L\begin{pmatrix}S&0\\0&D\end{pmatrix}L^T,
\qquad
\sigma_{\min}(L)=\ell(\rho),
\tag{6.1}
\]

and the singular-value inequality

\[
s_k(PMR)\ge\sigma_{\min}(P)\sigma_{\min}(R)s_k(M).
\tag{6.2}
\]

Now assume the partner complementary block `D` has not just three but `r+3` singular values at least `mu`. Then the block diagonal matrix in (6.1) has `r+3` singular values at least `mu`, irrespective of the possibly singular/resonant Schur block `S`. Therefore the completed partner factorization yields the actual inequality

\[
\boxed{
 s_{r+3}(H_0)\ge \ell(\rho)^2\mu.
}
\tag{6.3}
\]

Apply Theorem 3.1 to a **second arbitrary symmetric added matrix** `R`. If

\[
s_{r+1}(R)\le\delta<\ell(\rho)^2\mu,
\]

then

\[
\boxed{
 s_3(H_0+R)
\ge \ell(\rho)^2\mu-\delta.
}
\tag{6.4}
\]

Consequently, on an actual physical core of size `m`,

\[
\boxed{
\|p_Q\|_\infty
\le
{2\sqrt{6\pi m}\over \ell(\rho)^2\mu-\delta}.
}
\tag{6.5}
\]

This is an equation-level use of the completed partner result. The first hostile packet `U Theta U^T` can be arbitrarily large and resonant because the complementary Schur shield handles it; the second packet `R` may also have `r` arbitrarily large signed eigenvalues in arbitrary directions, because the new singular reserve pays only `s_{r+1}(R)`.

For example, take `r=2`, `m=7`, `D=diag(2,-2,2,-2,2)`, the partner-style cross block with `rho=1/2`, and any symmetric `Theta`. Then

\[
\ell(1/2)^2={9-\sqrt{17}\over8},
\qquad
\ell(1/2)^2\mu
=1.219223593595585\ldots .
\]

Allow a second arbitrary symmetric `R` whose two largest singular values are unbounded but `s_3(R)<=1/5`. Equation (6.4) gives

\[
s_3\ge1.019223593595585\ldots
\]

and

\[
\boxed{
\|p_Q\|_\infty\le22.5403216327\ldots .
}
\tag{6.6}
\]

A separate stronger compression argument from the preceding B12 run can remove the shear loss when the protected object is itself used as a Hermitian compression; Section 6 is recorded because it is the required direct use of the completed account04/B12 factorization and it applies the new reserve principle to that partner mechanism.

## 7. Newest volume result applied to the same spectral-tail parameter

The newest stable-volume theorem states: for an actual ORIGINAL-coordinate cross block `M=M0+E`, if

\[
s_3(M_0)\ge a>0,
\qquad
\max_i(P_{\operatorname{Ran}M_0})_{ii}\le1/2,
\qquad
\|E\|_{\rm op}\le a/16,
\tag{7.1}
\]

then the full ambient quadratic form has a continuous `C_0` density and

\[
\boxed{
\|p_Q\|_\infty\le {24\sqrt3 e\over5a}< {23\over a}.
}
\tag{7.2}
\]

Let an arbitrary signed spectral addition `R` be decomposed exactly as in Theorem 3.1:

\[
R=R_r+E_r,
\qquad
\operatorname{rank}R_r\le r,
\qquad
\|E_r\|_{\rm op}=s_{r+1}(R).
\tag{7.3}
\]

Suppose the top-`r` spectral packet has zero footprint across the protected cut,

\[
(R_r)[J,K]=0,
\tag{7.4}
\]

while

\[
s_{r+1}(R)\le a/16.
\tag{7.5}
\]

Then the **actual final cross perturbation** obeys

\[
\|R[J,K]\|_{\rm op}
=\|E_r[J,K]\|_{\rm op}
\le\|E_r\|_{\rm op}
=s_{r+1}(R)
\le a/16.
\tag{7.6}
\]

Substitution into the newest volume theorem gives (7.2). Thus the same tail parameter `s_{r+1}(R)` controls a second branch: the top `r` added eigenvalues may be arbitrarily large and of either sign provided their spectral packet is one-sided with respect to the protected cut (or otherwise has zero cross footprint), while the dense residual spectrum is charged only through its first unreserved singular value. This branch proves continuity.

## 8. What changed and what remains open

New proved information in this run:

1. **Rank budget without magnitude payment:** `s_j(B+R)>=s_{j+r}(B)-s_{r+1}(R)`.
2. **Physical QFORM compiler:** `r` reserve singular directions in a bounded original-coordinate core make the largest `r` added eigenvalues completely free, regardless of sign, magnitude, or orientation.
3. **Partner composition:** the completed complementary-Schur factorization can first protect `r+3` reserve modes against one arbitrary hostile packet; the new theorem then survives a second arbitrary packet whose top `r` modes are unbounded.
4. **Volume composition:** if those unbounded top modes have zero cross footprint, the newest stable-volume theorem charges only the same `(r+1)`-st spectral tail and yields a continuous density.

The full conjecture is still OPEN / NOT PROVED / NOT DISPROVED. The global premise `s_3(A)>=1` supplies exactly three large modes, not the `r+3` reserve modes required to absorb an arbitrary rank-`r` hostile update by this mechanism. Therefore the remaining structural problem is to force either a bounded original-coordinate core with reserve, a protected compression/cut where the hostile packet has small footprint, or one of the already-paid grouped-bank/hub/ridge/pair mechanisms. This run does not prove that such a certificate follows universally.

Continuity is not proved by the reserve branch. It is proved only by the volume branch under (7.1), (7.4), (7.5).

## 9. Finite checks

`CHECK.py` tests:

- 10,000 random symmetric pairs `(B,R)` against (3.2);
- an exact equality/sharpness construction;
- 5,000 random partner-style matrices with two arbitrary large added spectral spikes and residual singular values at most `1/5`;
- the numerical constants in (5.3) and (6.6).

These computations are consistency checks only. The mathematical proof is the singular-value argument above; no Monte Carlo output is used as proof of the QFORM conjecture.
