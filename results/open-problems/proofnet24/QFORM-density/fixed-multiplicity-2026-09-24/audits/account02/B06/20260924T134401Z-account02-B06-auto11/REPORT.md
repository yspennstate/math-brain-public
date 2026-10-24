SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-24T13:44:01Z.
attacking: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924 — full 790-line audit, with B06 emphasis on the graph determinant/Jacobian/frame weights/regularizer and counterexample-oriented threshold checks.

# account02/B06 auto11 — complete audit

## Source pin and scope

Pinned mathematical source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes, 790 lines. The current package was reread from master and the manuscript blob is unchanged.

I read `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, all 790 manuscript lines, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The supplementary files that were absent in an earlier B06 snapshot are now present. `checks.json` is consistent with the current `verify.py`: 534 exact interpolation seeds, 18 exact volume comparisons, 9 strict sampling cases, 240 floating Schur-threshold diagnostics and 30 graph-weight diagnostics, with exact diagonal-dominance slack `297/2800`. I did not treat these finite checks as proof or independently certify their historical execution provenance.

Verdict on the pinned 17-eigenvalue mathematics: **PASS**. I found no false statement or fatal gap. The candidate statement is exactly: independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0` imply an essentially bounded density with `||p||_infinity<=10000 K^2/s`. No continuity theorem is asserted for all branches.

## Line ledger

- **PASS, lines 1–90:** preamble, abstract, definitions, quantifiers, theorem/corollary, normalization parameters, proof architecture and Fourier conventions. Scaling targets the correct `K^2/s` homogeneity and no hidden support/moment/log-concavity hypothesis is introduced.
- **PASS, lines 91–160:** Fourier/Plancherel/inversion, power envelope and Riesz half-potential. Gaussian regularization and Tonelli/dominated-convergence hypotheses are sufficient; the weighted integral giving `12 sqrt(u)` is correct.
- **PASS, lines 161–217:** singular-value perturbation, Schur spectral count, diagonal dominance. In particular the literal singular-`A` paragraph of the Schur lemma is already valid: if `q=N_A(t)-k>0`, the displayed moving-threshold argument gives `N_{S_epsilon}(t-|epsilon|)>=q`, equivalently `s_q(S_epsilon)>=t-|epsilon|`; continuity of ordered singular/eigenvalue moduli gives `s_q(S)>=t`. A fixed-`delta` rewrite is a harmless clarification, not a required mathematical repair.
- **PASS, lines 221–301:** heat-flow geometric Brascamp–Lieb, product projection density, scalar Fourier powers. The projection line `sum_i(1-b_i)=d` is exact when all original rows, including `b_i=0`, are included; zero rows contribute zero to `-b_i log b_i`, so there is no gap.
- **PASS, lines 303–400:** cross-form decomposition, decoupling, regularized determinant, Cauchy–Binet crossing volumes, order-five density and order-three half-potential envelopes. The B06 determinant/Jacobian reconstruction is recorded below.
- **PASS, lines 401–525:** scalar square/profile, definite-pair polar Jacobian, hyperbolic-pair Jacobian and tails, quarter-power concentration and logarithmic potential. The hyperbolic cutoff `3 log 2/4` exactly ensures the growing exponential dominates the decaying one by a factor two; the final use `Lambda>=2/sqrt(D)` has the correct direction.
- **PASS, lines 528–645:** pivot-volume definition, small-entry bound, volume-sampled interpolation, nonsymmetric completion, global rank `<=3r`, restricted rank `<=r`, spectral-to-volume contradiction, random cut and no-pivot analytic consequences. The diagonal part vanishes on the seed, so all forced large diagonal entries lie in `L`. At `r<=4`, `23/28<371/400`; the contradiction really occurs inside the restricted block.
- **PASS, lines 646–724:** truncated half potential, singular kernels, scalar/definite/indefinite pivot estimates and nine-eigenvalue half-potential proposition. Full versus truncated half potentials are not conflated: the outside-unit tail costs at most one.
- **PASS, lines 726–790:** main proof, scaling, threshold accounting, limitations, remarks and bibliography. Scalar pivot `17 -> 16 -> >=9`, pair pivot `17 -> 15`, and no-pivot order five are all invoked under satisfied hypotheses. `Y=KX` gives cap-one coordinates and `Q=(s/K^2) Qtilde`, hence the final factor `K^2/s`.

No mathematical manuscript line remains `UNCHECKED` in this run. Package execution provenance for the historical self-audit counts remains `UNCHECKED`; the current finite suite is a diagnostic only.

## B06 reconstruction of the graph determinant

For `a=2t`, `alpha=(2*pi*e)^2`, `H=alpha I+a^2 M^T M`, define

`c_j=alpha e_j^T H^{-1} e_j`, `d_i=a^2 m_i^T H^{-1}m_i`, and `theta=sum_i d_i=sum_j(1-c_j)`.

The frame vectors `sqrt(alpha) H^{-1/2}e_j` and `a H^{-1/2}m_i` have outer products summing to the identity. The substitution `x=H^{-1/2}z` contributes the exact Jacobian `det(H)^(-1/2)`. Normalizing the coordinate vector gives

`x_j=sqrt(c_j/alpha) u_j dot z`,

so its one-dimensional factor is `alpha^(c_j/2)c_j^(-c_j/2)||g_j||_(1/c_j)`. The Fourier-row scale is `sqrt(d_i)` and contributes `d_i^(-d_i/2)||h_i||_(1/d_i)`. Since `g_j<=1` and has mass one, its norm is at most one. The scalar Fourier-power lemma at `p=2/d_i` gives

`||h_i||_(1/d_i) <= (2*pi*sqrt(e*d_i))^(d_i)`,

which cancels the powers of `d_i`. Finally `prod c_j^(-c_j/2)<=e^(theta/2)`, so the row factors and entropy factor combine to `(2*pi*e)^theta`. Factoring `alpha^d` from `det H` leaves

`det(I+a^2 M^T M/alpha)^(-1/2) (2*pi*e/sqrt(alpha))^theta`,

and the prescribed alpha makes the last factor exactly one. Taking the fourth root yields

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

Boundary cases are benign: `d_i=0` implies the corresponding physical row is zero and its Fourier factor is one; `c_j` may equal one; as `c_j` tends to zero, `c_j^(-c_j/2)` tends to one. The sign of `t` disappears through absolute scales.

## New regularizer edge-case result

The companion improvement artifact proves a stronger statement than the previous scalar-alpha optimization: **even arbitrary positive diagonal, coordinate-dependent regularizers cannot improve this graph-BL majorant.** Thus neither scalar nor anisotropic coordinate regularizer retuning, even depending on `t` and `M`, can lower the crossing-rank endpoint of this proof mechanism.

## Threshold reduction independently reconstructed in this run

After the baseline audit, I independently reconstructed the complete threshold-nine replacement proof, including the grouped product-Fourier weighted-subset Jacobian, entropy term, row-promotion identities, pivot branches and scaling. The safe theorem is

` s_9(A)>=s >0  =>  ||p_(X^TAX+b^TX+c)||_infinity <=6010 K^2/s.`

The full dependency map and constants are in the companion improvement artifact. This is a fixed-multiplicity theorem only. The unrestricted three-large-eigenvalue conjecture remains OPEN.

## Status summary

`PASS`: pinned 17 mathematical chain; all manuscript lines; graph determinant/Jacobians/weights; complete threshold-nine replacement reconstruction.

`GAP`: none fatal in the pinned 17 mathematics. The previous missing-support-files package gap is closed in the current master package.

`FALSE`: the claim that the literal moving-threshold singular-Schur paragraph requires a mathematical repair; ordered-value continuity already closes it. Also false is any claim that scalar or diagonal anisotropic graph regularizer tuning can improve the determinant majorant.

`UNCHECKED`: formal verification; journal peer review; provenance of historical finite self-audit counts; unrestricted three-eigenvalue QFORM.

Next obligation: threshold eight. Current structural work leaves a repeated-anchor/overlap-one or nested-star product receiver. The present graph regularizer cannot pay that debt by retuning alone.