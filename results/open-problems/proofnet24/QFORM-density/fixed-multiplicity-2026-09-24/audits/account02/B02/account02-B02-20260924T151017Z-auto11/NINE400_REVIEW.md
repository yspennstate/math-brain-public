# account02/B02 — independent complete review of `QFORM-NINE-EIGENVALUES-400-20260924`

Candidate source: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`.

Pinned candidate source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`. Git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`. Manifest SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`. Source: 955 lines, 60,749 bytes. I read all 955 lines, the manifest, proof map, and author self-audit. This review is separate from that self-audit.

## Verdict

**Mathematical PASS WITH ONE LOCAL PRESENTATION REPAIR** for

\[
s_9(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le400K^2/s.
\]

I found no fatal gap. One sentence in the hyperbolic-pair proof reuses the positive-tail coordinate symbol when treating the negative tail. The repair is immediate: choose the maximizing original coordinate independently for the `u` and `w` tail vectors. All displayed constants remain unchanged. I do not treat this review alone as satisfying the owner's two-independent-complete-review release gate.

## Complete line ledger

| lines | status | check |
|---|---|---|
| 1–46 | PASS | Preamble/abstract accurately summarize the theorem and limitations. |
| 47–86 | PASS | Main quantifiers, interval formulation, normalization, separate pivot scales `d=3/40`, `p=1/400`, `h=2/25`, and architecture are consistent. |
| 87–164 | PASS | Fourier/Plancherel/inversion, power envelope, Gaussian half-Riesz representation and constants recomputed. |
| 165–215 | PASS | Singular-value perturbation/rank, fixed-threshold singular Schur argument, and nonsymmetric strict diagonal dominance are correct. |
| 216–252 | PASS | Heat-flow proof of geometric rank-one Brascamp–Lieb has the correct monotonicity, Gaussian limit and approximation steps. |
| 253–297 | PASS | Product projection includes the needed `sum_{b_i>0}<=sum_i` step explicitly. Scalar Fourier-power normalization and convolution cap are correct. |
| 298–396 | PASS | Original-bank decoupling, regularized determinant BL frame, scale `alpha=(2*pi*e)^2`, exponent `-1/8`, Cauchy–Binet volumes and order-3/5 consequences are correct. |
| 397–477 | PASS | Grouped product-Fourier proof is dependence-safe. The phase-weighted image has an a priori `L2` density bound, Jensen is applied to mollified `L2`, weighted Holder is valid for the finite kernel measure, the row-Gram Jacobian is `S^2 det(C_TC_T^T)`, and approximate-identity convergence closes the unmollified estimate. |
| 478–527 | PASS | Terminal hub estimate and physical-row promotion tree correctly give `C3=3 sqrt(2)e(9/2)^(1/6)<15` and `C2=8 sqrt(e)2^(-1/8)<14`. Same-bank and outside phases are retained. |
| 528–562 | PASS | Scalar-square and definite-pair changes of variables have the stated coefficients and make no rotated-independence claim. |
| 563–589 | PASS | Hyperbolic coarea/Jacobian and positive-tail physical-coordinate argument are correct. |
| 590–606 | GAP (repaired) | For the negative tail the proof says to use `w` instead of `u` but then refers to the previously chosen coordinate satisfying `|u_i|>=|u|/sqrt2`. The same coordinate need not control `w`. Repair: choose `i_+` with `|u_{i_+}|>=|u|/sqrt2` for the positive tail and independently choose `i_-` with `|w_{i_-}|>=|w|/sqrt2` for the negative tail. Since `|u|=|w|`, both cutoffs obey the same displayed bound. No constant or downstream statement changes. |
| 607–662 | PASS | Quarter-power concentration, atom exclusion, logarithmic potential, and elementary gamma coefficient bound are correct. |
| 663–715 | PASS | New pivot-volume definitions, entry bound `p+d^2=13/1600<1/121`, volume sampling and nonsymmetric completion are correct, including singular-seed inequality direction. |
| 716–766 | PASS | Retuned spectral-to-volume proof closes for orders `1<=k<=3`: exact diagonal-dominance margins are `1131/2200` and `51/2200`; fair cut gives the stated order-2/3 consequences. |
| 767–789 | PASS | Sharper convolution kernel formula and constants are correct. |
| 790–811 | PASS | Full pair half-potential is correctly scaled as `D^-1/4`. For the indefinite case the rearrangement argument is valid by layer-cake interval overlaps; at `delta=1/64`, the normalized bound is `12+5 log 2<16`. |
| 812–860 | PASS | Five-eigenvalue full half-potential proposition correctly separates no-pivot, scalar-pivot and pair-pivot alternatives. Main theorem branch constants `<375,<280,<383,<320,<80,<392.5` check, and scaling gives exactly `400K^2/s`. |
| 861–927 | PASS | Overlap volume is defined only over nonsingular seeds. Frobenius orthogonality `||D+E||_F^2=||D||_F^2+||E||_F^2`, best rank-`3r` approximation, bordered-diagonal identity, and volume-sampling expectation prove `W+(r+1)^2V_{r+1}>=V_r T_{3r}`. The `s_8` corollary and explicit constant are correct. |
| 928–946 | PASS | Threshold accounting correctly says nine is sufficient and eight/three remain unproved. |
| 947–955 | UNCHECKED | Bibliographic attribution only; neither citation is used as an unproved mathematical dependency because the needed inequalities are proved in the manuscript. |

## B02 normalization/adversarial checks

For the cap-one Gaussian `f(x)=exp(-pi x^2)`, `fhat(t)=exp(-t^2/(4*pi))` and exactly

\[
\int|\widehat f(t)|^qdt=\frac{2\pi}{\sqrt q}.
\]

Thus the scalar-Fourier `q^-1/2` exponent used in the grouped compiler is sharp for the admissible class. For `Unif[-1/2,1/2]`, the difference density reaches one, so the convolution cap is sharp; `(X_1+X_2)/sqrt2` has peak `sqrt2`, giving a lower benchmark for projection constants. Finally, the cap-one law `X^2` has density `s^-1/2` on `(0,1/4)`, so `X_1^2-X_2^2` has infinite density at zero. This independently confirms that the order-two receiver must remain a fractional-potential endpoint rather than an `L-infinity` endpoint.

## Constant checks

The new full-pair estimate is especially important. A density cap `M` implies

\[
\sup_a E|Z-a|^{-1/2}\le\int_0^\infty\min(1,2Mt^{-2})dt=2\sqrt{2M}.
\]

For an indefinite pair, output scaling by `sqrt D` turns the hyperbolic envelope into `h(z)<=6+log_+(16/|z|)`; splitting at `delta=1/64` gives `8+(4+5log2)<16`. Therefore the `16D^-1/4` scaling in the scalar-pivot/pair-pivot branch is correct.

The main indefinite-pair branch is also normalized correctly:

\[
D^{-1/2}\bigl(6+\log16+L_0\bigr)+\frac1e
\le200+80\log10+\frac1e<392.5
\]

for `D>=1/400`. No missing factor two was found.

## Downstream

The candidate is mathematically sound after the local negative-tail notation repair. It is stronger than the `<536` retuning I derived earlier in this same invocation, so that earlier note is preserved as immutable history but is no longer the best constant. A separate improvement note in this run retunes the now-audited `400` proof further to `<361 K^2/s`; that new constant is not yet independently validated. Neither this review nor that retuning proves multiplicity eight or the unrestricted three-eigenvalue conjecture.
