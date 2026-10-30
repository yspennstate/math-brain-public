# fleet02/B13 independent end-to-end audit — fixed multiplicity, definite pairs / hyperbolic envelope

Run: `20260924T132744Z-fleet02-B13-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Fresh source pin before this run's writes: `yspennstate/math-open-problems@103319cbdf0724060c86293669e11feb51828ddc`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256 recorded by `SOURCE_MANIFEST.json`: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Baseline owner commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.

## Verdict

**Mathematical verdict: PASS for the written 17-eigenvalue theorem.** I independently reread the complete 790-line `manuscript.tex`, including every statement/proof range in `proof_map.csv`, and reconstructed the main algebraic and analytic chains. I found no fatal gap in

\[
s_{17}(A)\ge s>0\Longrightarrow
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature/remaining spectrum, and arbitrary affine terms.

This is one worker review, not an independently-validated release certificate, and it does **not** solve the unrestricted three-eigenvalue QFORM conjecture.

**Package verdict: PASS with one documentation GAP of no mathematical impact.** Unlike the earlier B13 audit, the current package now contains `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`. Their hashes/metadata are mutually consistent with the pinned manuscript blob. The current checker records 534 exact interpolation seeds, 18 exact volume comparisons, 240 floating Schur-threshold checks and 30 graph-weight checks. I independently replayed the exact arithmetic/random loops from the pinned `verify.py` and obtained the same `534 / 18 / 9 strict / 240 / 30` counts and the exact diagonal-dominance slack `297/2800`.

The remaining documentation GAP is historical only: `AUDIT.md` still says “all listed checks in verify.py passed” immediately before listing older counts (`504`, `10`, `192`, `800`, `1040`, `160`) that the current `verify.py` does not implement. `SOURCE_MANIFEST.json`, `README.md`, and `DELIVERY_STATUS.md` explicitly explain that the present checker is a new scoped suite and does not reproduce those historical counts, so this is not a proof defect. **Next obligation:** edit the historical sentence if a future package-cleanup pass wants zero ambiguity; do not reinterpret the old counts as current reproducibility evidence.

## Complete line/range audit

| Source range | Item | Status | Independent check / impact |
|---|---|---|---|
| 1–46 | front matter, abstract, notation | PASS | Scope matches theorem; no hidden support, moment, smoothness, log-concavity, or rotated-independence hypothesis. |
| 47–83 | `thm:main`, `cor:33`, normalization/architecture | PASS | Quantifiers are complete. Final `Y=KX`, `A/s` scaling returns exactly `K^2/s`. Seventeen is presented as sufficient, not optimal. |
| 84–160 | Fourier convention, Gaussian regularization, `lem:fourier`, `lem:envelope`, `lem:riesz` | PASS | Constants match the stated Fourier convention. Tonelli is used only on nonnegative majorants; the half-Riesz coefficient is `1/sqrt(2*pi)` and the `3/4` envelope gives `12 sqrt(u/(2*pi))`. |
| 161–220 | `lem:rank`, `lem:schur`, `lem:dd` | PASS | Nonsymmetric perturbations use singular values. In the singular Schur case, `N_{S_eps}(t-|eps|)>=q` is `s_q(S_eps)>=t-|eps|`; Lipschitz continuity of ordered singular values gives `s_q(S)>=t`, so the moving-threshold limit is valid as written. |
| 221–257 | geometric rank-one Brascamp–Lieb | PASS | Heat-flow identity has the correct sign; the frame map is a contraction; compact-support heat tails justify differentiation/integration by parts; truncation plus monotone convergence covers arbitrary nonnegative integrable inputs. |
| 258–309 | product projections; integrated scalar Fourier powers | PASS | Projection is a deterministic fiber integral of the original product density, not a claim of rotated independence. `|fhat|^{2m}` is integrable already by Plancherel, so inversion at zero is not circular. |
| 310–385 | two/four-copy decoupling; regularized crossing determinant | PASS | Difference coordinates remain independent cap-one. The graph frame weights satisfy the exact trace identity; the `d_i` powers cancel; `alpha=(2*pi*e)^2` cancels the entropy scale and fourth roots give determinant exponent `-1/8`. |
| 386–403 | crossing volumes and order-3/order-5 envelopes | PASS | Cauchy–Binet expansion is correct. `k=5` gives `5e Z_5^{-1/10}`; `k=3` is used only for a half-potential, not direct density inversion. |
| 404–422 | scalar square profile and conditional domination | PASS | Two inverse branches give the displayed square-root profile. The conditional formula is a measure domination statement; no independence between the completed square and Schur remainder is asserted. |
| 423–436 | `lem:definite` | PASS | Completing the square and orthogonally diagonalizing are deterministic changes in the two-dimensional integral. The `(delta,theta)` Jacobian is `1/(2 sqrt(|det B|))`, so angular integration gives `pi M/sqrt(|det B|)` without post-rotation independence. |
| 437–484 | `lem:hyperbola` | PASS | Full reconstruction below. The logarithmic singularity and both tails are handled in original coordinates; no pointwise exceptional-slice selection is used after conditioning. |
| 485–527 | quarter-power concentration/log potential | PASS | Random-sign splitting yields a physical cross block with norm `>=||S||/4`; one determinant factor gives `|t|^{-1/4}`; Gaussian smoothing at `v=1/8` has coefficient `<16`; layer cake gives `4+4 log 16`. |
| 528–544 | pivot/volume definitions and no-pivot entry bounds | PASS | Principal determinant convention and ordered disjoint-volume convention are consistent with later sampling/cut arguments. No-pivot implies all off-diagonal entries `<1/7` at the chosen constants. |
| 545–581 | volume sampling and nonsymmetric completion | PASS | Bordering formula is exact; singular seeds can have nonsingular extensions, hence the aggregate is correctly an inequality. `R-P` support gives global rank `<=3r`; `R[L,L]=P[L,L]` gives restricted rank `<=r`; `D` vanishes on the seed. |
| 582–653 | spectral-to-volume, random cut, no-pivot consequences | PASS | A bad volume ratio gives `||E||_F<=1/16`. Global rank forces `r+1` large diagonal entries in `L`; strict diagonal dominance of their `(r+1)` block contradicts restricted rank `<=r`. Each ordered minor survives a fair cut with probability `4^{-k}`. |
| 654–675 | elementary singular kernels | PASS | The near part of `J(d)` is scale invariant and bounded; the far part contributes the logarithm. The log-kernel overlap is maximized when interval centers coincide, giving `8`. |
| 676–715 | pivot control of truncated half potentials | PASS | Scalar branch uses Schur survival plus quarter-power logarithmic integrability. Definite pair is uniformly bounded. Indefinite pair integrates the hyperbolic logarithm against the truncated square-root kernel; `sup D^{-1/2} log_+ D=2/e` is used with correct coefficient. |
| 716–725 | nine-eigenvalue half-potential | PASS | Pivot/nonpivot cases cover all matrices; outside `|Q-a|<=1`, the kernel is at most one, so the full half-potential is `<=601`. |
| 726–760 | proof of main theorem and general scaling | PASS | No-pivot, scalar-pivot, definite-pair, indefinite-pair branches exhaust the cases. Scalar Schur leaves at least 16 unit directions; pair Schur leaves at least 15. Largest rounded branch is `6010<10000`. Scaling is exact. |
| 761–790 | threshold accounting, limitations, references | PASS | Manuscript accurately states that order five is needed by this Fourier endpoint and that the three-eigenvalue conjecture/continuity are not proved. |

No manuscript range remains UNCHECKED in this run.

## B13 reconstruction: definite pair

For a definite symmetric `2x2` matrix `B`, completing the square reduces to `mu_1 y_1^2+mu_2 y_2^2+v`, `mu_i>0`. The change

\[
y_1=\sqrt{\delta/\mu_1}\cos\theta,
\qquad y_2=\sqrt{\delta/\mu_2}\sin\theta
\]

has absolute Jacobian `1/(2 sqrt(det B))`. A joint density bounded by `M` therefore pushes forward to a density at most

\[
\frac{M}{2\sqrt{\det B}}\int_0^{2\pi}d\theta
=\frac{\pi M}{\sqrt{\det B}}.
\]

The orthogonal diagonalization only changes variables in this deterministic integral. In the theorem it is applied after conditioning on the complement of an **original-coordinate** pair, whose conditional joint density is the unchanged product of two cap-one densities. This is valid for arbitrary rough/fragmented supports.

## B13 reconstruction: hyperbolic envelope

For an indefinite pair with eigenvalues `mu_+>0>-mu_-`, `D=mu_+|mu_-|`, the positive level `delta=z-v>0` is covered by two branches

\[
w_\epsilon(t)=\epsilon\sqrt{\delta/\mu_+}\cosh t\,e_+
+\sqrt{\delta/|\mu_-|}\sinh t\,e_- .
\]

The absolute `(delta,t)` Jacobian is exactly `1/(2 sqrt D)`. Writing one branch as `u e^t+w e^{-t}` gives

\[
|u|=|w|=\rho_0=\frac12\sqrt{\delta(\mu_+^{-1}+|\mu_-|^{-1})}.
\]

Choose an original coordinate with `|u_i|>=rho_0/sqrt2`. For `t>=(3/4)log2`, the decaying term is at most half the growing term, so the coordinate is one-sign monotone and

\[
|y_i'(t)|\ge |y_i(t)|/3.
\]

Starting the tail when `|y_i|>=1`, the product density is bounded by the single original density `f_i`, and its total mass on that half-line is at most one. Therefore

\[
\int_T^\infty f_1(y_1(t))f_2(y_2(t))dt
\le3\int_{|y|\ge1,\,\text{one sign}}\frac{f_i(y)}{|y|}dy
\le3\log2.
\]

The negative tail uses the `w` coefficient, possibly a different original coordinate. The middle interval has length at most

\[
\frac{3}{2}\log2+\log_+\frac{32}{\delta\Lambda},
\qquad \Lambda=\mu_+^{-1}+|\mu_-|^{-1},
\]

and `Lambda>=2/sqrt D`. Inserting both tails into the coarea formula yields exactly

\[
p_q(z)\le D^{-1/2}
\left(6+\log_+\frac{16\sqrt D}{|z-v|}\right)
\]

for a.e. `z!=v`; the negative level is symmetric after swapping signs. The proof is a nonnegative-test-function statement, so rough densities and conditional critical values do not create exceptional-slice problems.

The logarithm is structurally necessary: for independent `X,Y~Unif[-1/2,1/2]`, `X^2-Y^2` has

\[
p(z)=\log\frac{1+\sqrt{1-4|z|}}{1-\sqrt{1-4|z|}}
=\log(1/|z|)+O(1)
\]

near zero. Thus a determinant-only bounded conditional density for an indefinite physical pair is false even for compact interval laws; the surviving Schur direction is genuinely needed to average the logarithm.

## Lower-threshold audit result

I found **no complete unconditional replacement proof lowering 17**. The current route still needs order-five crossing volume for an integrable Fourier envelope, and its worst sampled ratio is `r=4`, where the algebraic contradiction needs `m>=4r+1=17`.

The companion improvement artifact for this run gives an explicit no-pivot family showing that the completion lemma's two rank bounds are simultaneously sharp: `rank R=3r` and `rank R[L,L]=r` for every `r`. Therefore a threshold reduction cannot come merely from replacing either of those universal rank bounds by a smaller number inside the same completion construction. It must use a different seed-selection theorem, a different completion, an order-four endpoint receiver, or another analytic mechanism.
