# fleet03/B08 r58 — current-invocation end-to-end baseline audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `fleet03/B08`  
Pinned manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**PASS on a fresh complete reread of source lines 1--790 in this invocation.** I found no fatal mathematical gap in the stated fixed-multiplicity theorem
\[
s_{17}(A)\ge s>0\Longrightarrow \|p_{X^TAX+b^TX+c}\|_\infty\le10^4K^2/s
\]
for arbitrary dimension, real symmetric `A`, arbitrary affine terms, and independent real coordinate densities bounded by `K`.

This is a mathematical review by one worker, not formal verification and not a release certificate. The theorem proves an essentially bounded density. Continuity is proved on the no-pivot Fourier branch but is not claimed globally. The unrestricted three-eigenvalue conjecture remains open.

## Line-range audit

| Lines | Status | Check |
|---|---|---|
| 1--83 | PASS | Definitions, quantifiers, `K^2/s` target, `eta=1/100`, `kappa=80^-2`, 9/17 architecture, and limitations are internally consistent. No hidden moments/support/log-concavity/rotation-independence assumption is introduced. |
| 84--121 | PASS | Fourier convention, Plancherel factor `2pi`, inversion `1/(2pi)`, Gaussian transform and approximate-identity argument are consistent. Uniform convergence after Gaussian damping identifies the rough-law density correctly. |
| 122--160 | PASS | Power-envelope integral is `2ap/(p-1)`. Riesz/Gamma representation gives coefficient `1/sqrt(2pi)` and the weighted `3/4` envelope integral is `12 sqrt(u)`. Tonelli handles extended values/atoms. |
| 161--220 | PASS | Singular-value approximation/rank lemma is valid without symmetry. Schur spectral count is valid including singular ambient matrices; the limiting threshold is in the correct direction. Strict row diagonal dominance is valid for nonsymmetric matrices. |
| 221--255 | PASS | Geometric rank-one BL heat-flow identity has the correct sign from the Parseval-frame contraction. Gaussian domination justifies integration by parts/large-time limit; Fatou and monotone truncation cover rough inputs. |
| 256--301 | PASS | Product-projection density proof uses orthogonal changes only inside deterministic integrals. The `b_i=0` factors may be dropped; extending `-b log b<=1-b` to `b=0` only enlarges the final right side. Scalar Fourier powers are integrable because `|hat f|^{2m}<=|hat f|^2`; inversion and the projection bound give the displayed constant. |
| 302--324 | PASS | Independent-copy decoupling duplicates literal original-coordinate variables. Pure same-bank phases are discarded only after legitimate Cauchy--Schwarz/modulus; Jensen gives the fourth-power inequality. |
| 325--403 | PASS | Regularized determinant frame, Jacobians, weights `c_j,d_i`, scalar Fourier exponents, entropy cancellation at `alpha=(2pi e)^2`, and the fourth-root exponent `-1/8` check. Cauchy--Binet gives the crossing volumes; order five is integrable, order three is used only with the Riesz weight. |
| 404--436 | PASS | Scalar square profile and interval preimage estimate are correct. The profile domination retains dependence through conditional/Tonelli formulation. Definite two-coordinate coarea gives `pi M/sqrt(|det B|)` uniformly in affine shifts. |
| 437--482 | PASS | Hyperbolic parameterization has Jacobian `1/(2sqrt D)`. The physical-coordinate tail choice uses only cap/mass one, not rotated independence. The two tail estimates plus middle length give the stated logarithmic envelope; `Lambda>=2/sqrt D` is used in the correct direction. |
| 483--525 | PASS | Quarter-power concentration: diagonal case is direct; sign partition creates a literal cross block with norm at least `L/4`. Determinant Fourier bound plus Gaussian smoothing yields the safe constant 16. Layer cake gives `4+4 log16` and excludes atoms. |
| 526--564 | PASS | Pivot and ordered disjoint volumes are coherent. In determinant-squared sampling, singular seeds are correctly omitted and extensions make the aggregate relation one-sided. The nonsymmetric interpolant satisfies exact seed-row/seed-column interpolation. |
| 565--580 | PASS | Completion support checked entrywise: `D=0` on `S union T`, `E` is off-diagonal on `LxL`, `R[L,L]=P[L,L]`, hence restricted rank `<=r`; `R-P` splits into rows `T` plus remaining columns `S`, hence global rank `<=3r`. No symmetry is needed downstream because singular values are used. |
| 581--619 | PASS | Failed `V_k` forces a ratio `<kappa`. The completion has `epsilon<=(r+1)/80<=1/16`; global rank `3r` and `m=4k-3>=4r+1` force `r+1` large diagonal entries outside the seed. Exact margins are `371/400` versus `<23/28`, so restricted rank `r` is contradicted by strict diagonal dominance. |
| 620--645 | PASS | Fair coordinate cut counts each ordered disjoint minor with probability `4^-k`. The no-pivot order-three half-potential and order-five density constants follow with `Z_k^{-1/(2k)}<=160`. |
| 646--674 | PASS | Truncated potential is explicit. The `J(d)` near/far split and logarithmic-kernel rearrangement are valid with the displayed safe constants. |
| 675--724 | PASS | Pivot truncated-half-potential proof separates scalar, definite pair and indefinite pair correctly. Scalar branch uses a surviving Schur direction only for the logarithmic potential. `s_9` proposition does not confuse truncated and full potentials: outside distance one contributes at most one. |
| 725--749 | PASS | Normalized main proof exhausts no-pivot, scalar pivot, definite pair and indefinite pair. Scalar pivot leaves 16 Schur directions and invokes the nine-direction full half-potential. Indefinite pair leaves 15 directions, more than enough for `||S||>=1`; Tonelli avoids exceptional-slice dependence issues. |
| 750--790 | PASS | Scaling `Y=KX` and `Q=(s/K^2) Qtilde` gives exactly `K^2/s`. Interval domination is equivalent to the essential density bound. Threshold accounting correctly distinguishes order-three half-potential from order-five density and explicitly does not claim the three-eigenvalue theorem or global continuity. |

## B08 sensitive point: nonsymmetric interpolation and both rank bounds

For a nonsingular disjoint seed `S,T` of size `r`, `B=A[S,T]` and
\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot},
\]
one has exactly
\[
P_{S,\cdot}=A_{S,\cdot},\qquad P_{\cdot,T}=A_{\cdot,T}.
\]
The completion gives
\[
R_{L,L}=P_{L,L},\qquad \operatorname{rank}R_{L,L}\le r.
\]
Writing `Q=R-P`, `Q` vanishes on rows `S`, columns `T`, and `LxL`; splitting its support as rows `T` plus the remaining columns `S` gives
\[
\operatorname{rank}(R-P)\le2r,
\qquad \operatorname{rank}R\le3r.
\]
The spectral-to-volume proof uses these estimates in different places and cannot replace them by one undifferentiated rank statement. `D` vanishing on the seed is what places all forced large diagonal coordinates in `L`, where the restricted rank applies.

## Current improvement frontier

The separate r58 improvement proves `QFORM-S7-OVERLAP-PLUS-MULTIDELETE-RIDGE-RIGIDITY-v1`: in the no-pivot `s_7>=1` chamber, either a `C_0` density is paid with constant `<2400`, or the invertible-seed overlap-one currency is bounded below by `5929/262144000000` and the same matrix carries three nested original-coordinate stars of norm `>9/(6400sqrt2)`. This is a supporting router, not a multiplicity-seven density theorem.

No manuscript source was overwritten.
