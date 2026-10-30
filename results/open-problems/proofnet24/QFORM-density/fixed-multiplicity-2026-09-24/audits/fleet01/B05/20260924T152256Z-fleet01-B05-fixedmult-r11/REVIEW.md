# fleet01/B05 independent audit — latest nine-eigenvalue constant-400 source

Run: `20260924T152256Z-fleet01-B05-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `fleet01/B05`  

## Source pin and scope

Canonical source audited in full:

- repository: `yspennstate/math-open-problems`
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- package completion commit used for auxiliary files: `af592913ccfc4a87dfbf7c3a49bf2c5d4bbae359`
- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`
- source git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`
- source SHA-256 reported by the pinned package: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
- length: 955 lines, 60,749 bytes.

I read all 955 source lines, `README.md`, `NINE_400_AND_OVERLAP.md`, `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json`. This report is one independent mathematical review of this exact revision. It is not a second independent review, journal review, formal proof certificate, or owner-level validation. The package-reported SHA-256 and PDF production metadata were not independently recomputed in this run; the git blob and source contents were retrieved at the pinned package commit.

Candidate audited:

> For independent real coordinates with densities at most `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, if `s_9(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density with `||p_Q||_infinity <=400 K^2/s`.

No multiplicity-eight or unrestricted multiplicity-three theorem is claimed.

## Verdict

**Mathematical verdict on the 955-line candidate: PASS.** I found no fatal gap, false statement, or missing hypothesis in the theorem proof or the overlap theorem. Every mathematical line range and every label listed in `proof_map.csv` was checked below. The delicate B05 issues — product-projection densities, deterministic orthogonal changes versus probabilistic independence, rough-density versions, mollified `L^2` limits, and exceptional slices — pass.

**Review status:** this run supplies one independent end-to-end PASS only. It does not satisfy the owner's two-separate-review gate by itself.

Non-mathematical items left **UNCHECKED** in this run: (i) exhaustive novelty/prior-art claims associated with the two bibliography entries; the paper does not depend on those sources for a proof, and (ii) the package's claim that the compiled PDF was visually inspected page-by-page; no PDF binary is stored in the audited GitHub directory. `verify_new.py` was read line-by-line and its recorded output was compared to `checks_new.json`; finite tests are not universal proof.

# 1. Urgent-defect scan

No urgent mathematical defect was found. In particular:

- **PASS — no rotated independence.** Every orthogonal map in the projection lemma, definite-pair integral, and hyperbolic level-set parametrization is a deterministic change of integration variables or a density pushforward. The proof never declares rotated coordinates independent.
- **PASS — rough laws.** Coordinate densities are replaced by globally pointwise-bounded Borel representatives only on null sets. Conditional density formulas are used through nonnegative test functions and Tonelli, so exceptional pointwise slices are not silently selected.
- **PASS — grouped mollified `L^2`.** The proof bounds `mu_t*rho_delta` first, obtains a bound uniform in `delta`, and only then uses the genuine `L^2` approximate-identity limit. It does not identify an unmollified pointwise density before proving it exists in `L^2`.
- **PASS — physical hubs.** Every promoted hub is a literal original coordinate. Its density cap and independence from the remaining source banks are therefore legitimate. Projected coordinates are never promoted as independent sources.
- **PASS — nonsymmetric auxiliaries.** Nonsymmetric `P,R,E` are used only in singular-value/rank/Frobenius arguments; the random quadratic form remains symmetric.
- **PASS — density/half-potential distinction.** The order-two crossing result is used only as a full negative-half-moment estimate, never as a bounded-density theorem.

# 2. Complete source-line audit

The statuses below cover every source line 1–955. `PASS` means the stated argument was independently reconstructed to the level needed by downstream uses.

| Lines | Status | Check |
|---|---|---|
| 1–38 | PASS | Preamble, abstract, notation and title accurately match the mathematical theorem and do not add assumptions. |
| 39–75 | PASS | Main quantifiers, essential-density convention, parameter choices, pivot definitions and architecture. `K^2/s` scaling is dimensionally and algebraically correct. |
| 76–117 | PASS | Fourier convention, Gaussian regularization, Plancherel, inversion, approximate-identity limit and Gaussian inversion. Constants are consistent with the chosen transform. |
| 118–127 | PASS | Power-envelope integration: `int min(1,(a/|t|)^p)=2ap/(p-1)` and inversion constant. |
| 128–160 | PASS | Riesz half-potential identity, Tonelli steps and `12 sqrt(u/(2pi))` envelope constant. |
| 161–178 | PASS | Singular-value approximation formula, perturbation and rank shift; symmetry is not required. |
| 179–203 | PASS | Schur spectral count. In the invertible case the complementary block of `A^{-1}` is `S^{-1`; positive and negative compression counts give the absolute-value count. Singular `A` is handled at a fixed lowered threshold and then by continuity. |
| 204–215 | PASS | Strict diagonal dominance argument. |
| 216–252 | PASS | Geometric rank-one Brascamp–Lieb heat-flow proof, including the contraction from the frame identity, large-time limit, Lebesgue-point pullbacks, truncation and monotone convergence. |
| 253–278 | PASS | Product-projection density theorem. The map `(y,z)->Uy+Wz` is only a deterministic orthogonal change of variables. Factors with `b_i=0` can be dropped because globally chosen versions obey `f_i<=1`. BL gives `prod b_i^{-b_i/2}` and `sum(1-b_i)=d`. No rotated independence is used. |
| 279–297 | PASS | Integrated scalar Fourier powers. `|hat f|^{2m}` is integrable, Fourier inversion supplies the continuous density value at zero, and the signed `2m`-coordinate linear form uses the projection theorem only as a density bound. |
| 298–320 | PASS | Cross-block decoupling. Cauchy–Schwarz is taken in an original product bank; the independent difference coordinates have cap-one densities; pure phases are discarded only after the relevant original-coordinate integration. |
| 321–370 | PASS | Regularized determinant bound. The BL frame is exact; `c_j,d_i` are valid exponents; scalar Fourier powers cancel the `d_i` factors; `prod c_j^{-c_j/2}<=e^{theta/2}` and `alpha=(2pi e)^2` cancel the remaining entropy/scaling term. Fourth root yields the displayed `-1/8` determinant power. |
| 371–396 | PASS | Cauchy–Binet crossing volumes and the order-five density/order-three half-potential envelopes, including all exponents. |
| 397–477 | PASS | Grouped product-Fourier lemma. See Section 3 below for the detailed B05 reconstruction. |
| 478–488 | PASS | Terminal physical-hub block. Literal hubs have phase-weighted `L^2` norm at most one; the disjoint bank projection has density cap `e^{q/2}/sqrt(G)`; Plancherel gives `|t|^{-q/2}`. Conditioning on other original coordinates is harmless. |
| 489–527 | PASS | Heavy-row promotion and marginal-free crossing estimates. Incident Gram volume factors exactly under Gram–Schmidt; selected hubs stay literal; all hub-to-left couplings remain in `M_I`; constants for `q=3` and `q=2` check. |
| 528–548 | PASS | Scalar-square density, inverse-image interval length and conditional domination profile. The random square/remainder are not declared independent; the test-function/Tonelli formulation is sufficient. |
| 549–562 | PASS | Definite pair. Orthogonal diagonalization is only in the two-dimensional deterministic integral; the joint density cap survives a determinant-one rotation. |
| 563–610 | PASS | Indefinite hyperbolic pair. Hyperbola Jacobian, physical-coordinate tail selection, one-sided `f_i(y)/|y|` bound, cutoff constants, AM–GM step and critical-level null-set treatment all check. |
| 611–662 | PASS | Quarter-power concentration. The deterministic sign cut has cross norm at least `L/4`; determinant envelope, Gaussian smoothing, Gamma bound and layer-cake logarithmic moment have correct constants. |
| 663–678 | PASS | Pivot/volume definitions and no-pivot entry bounds, including `p+d^2=13/1600<1/121`. |
| 679–699 | PASS | Volume-sampled interpolation. Bordered determinant identity is exact; sorting signs disappear after squaring; singular seeds are correctly excluded, yielding an inequality rather than a false equality. |
| 700–715 | PASS | Completion. `R-P` support gives global rank at most `3r`; `R_LL=P_LL` gives the crucial restricted rank at most `r`; `D` diagonal and `E` zero diagonal are exact. |
| 716–742 | PASS | No-pivot spectral-to-volume proposition. Ratio-drop argument, nonsymmetric singular-value perturbation, location of large diagonal entries outside the seed, and restricted diagonal-dominance contradiction all check. Exact margins are `1131/2200` and `51/2200`. |
| 743–753 | PASS | Fair coordinate cut; each ordered disjoint `k,k` pair lands across the cut with probability `4^{-k}`. |
| 754–766 | PASS | No-pivot consequences. Random cut plus marginal-free receiver gives half potential `<70` from five directions and density `<375` from nine. |
| 767–789 | PASS | Scalar convolution kernel `J`; exact hyperbolic/trigonometric formulas and logarithmic upper bound. |
| 790–811 | PASS | Full pair half potential. Definite branch follows from a density cap; indefinite branch uses centered interval rearrangement through nonnegative layer-cake indicators, not symmetry of the input law. `delta=1/64` gives `12+5 log2<16`; output scaling is `D^{-1/4}`. |
| 812–829 | PASS | Five-eigenvalue full half potential. Scalar branch correctly uses a truncated inner potential plus tail `<=1`; the next Schur remainder has a nonzero spectral direction and hence the quarter-power logarithmic bound. Pair branch conditions only original coordinates. |
| 830–860 | PASS | Main theorem case split and scaling. Normalized branch bounds are all `<400`; indefinite-pair averaging keeps the random critical value inside a uniform logarithmic potential. General `K,s` rescaling is exact. |
| 861–907 | PASS | Overlap volume and spectral-tail theorem. `D` diagonal and `E` zero diagonal are Frobenius orthogonal; best rank-`3r` approximation uses singular values and does not require symmetry; same-index border terms give the exact `W/V_r` diagonal-energy identity. |
| 908–925 | PASS | Eight-direction corollary. `T_6>=s_7^2+s_8^2>=2`; in the no-pivot `V_3<kappa^3` chamber the stated lower bound follows. No density theorem is inferred. |
| 926–955 | PASS / UNCHECKED metadata | Threshold accounting accurately summarizes the proved implications and explicitly leaves eight and three open. Mathematical bibliography dependence is nil. The historical/priority characterization of the cited antecedents was not independently re-searched in this run. |

# 3. B05 deep reconstruction: product projections and grouped `L^2`

This is the main lens assigned to this slot.

## 3.1 Product-projection lemma

Let `U` have orthonormal columns and complete it to `(U,W)`. After the orthogonal change of integration variables,

`p(y)=int prod_i f_i((Uy)_i+w_i dot z) dz`.

Put `b_i=|w_i|^2`. For `b_i>0`, the vectors `v_i=w_i/sqrt(b_i)` form the geometric BL frame

`sum_i b_i v_i v_i^T=I`.

The choice

`h_i(t)=f_i((Uy)_i+sqrt(b_i)t)^(1/b_i)`

is legitimate because pointwise `0<=f_i<=1`; hence `f_i^(1/b_i)<=f_i`. Therefore

`int h_i <= b_i^(-1/2)`

and

`p(y)<=prod b_i^(-b_i/2)<=exp(d/2)`.

Nothing in this calculation asserts that the coordinates of `U^T X` are independent. The orthogonal matrix is used only to parameterize a fiber integral.

## 3.2 The complex pushforward really is in `L^2`

In Lemma `grouped`, `M_J` has full row rank. Its image of the `J` product bank has ordinary density bounded by

`e^(k/2)/sqrt(det(M_JM_J^T))`.

The phase-weighted conditional image has total variation dominated by that ordinary image. Averaging translations over the `I` bank therefore produces a complex density `mu_t` dominated by an ordinary convolution having the same `L^infinity` cap and mass one. Thus `mu_t in L^1 cap L^2` before the approximate-identity limit is invoked.

## 3.3 Correct order of mollification, copying and phase removal

For a probability mollifier `rho_delta`, Hilbert-space Jensen gives

`||mu_t*rho_delta||_2^2 <= E_I ||nu_(t,I)*rho_delta||_2^2`.

After introducing an independent `J` copy, the kernel is `K_delta(M_JD)`, `D=X_J-X'_J`. The pure `I` phase cancels. Only after integrating the original independent `I` coordinates are the resulting scalar Fourier factors obtained; the remaining pure `J` phase is then removed by modulus. This order is essential and is respected in the manuscript.

Weighted Holder is applied to the finite nonnegative measure `K_delta(M_JD)dP_D`; it does not require this measure to have total mass one. For every determinant-weighted subset `T`, the map

`D -> (M_JD,(c_iD)_(i in T))`

has row Gram determinant

`det(M_JM_J^T) det(C_TC_T^T)`

because the residual rows are orthogonal to `row(M_J)`. The product-projection theorem controls the joint density of this deterministic linear image. At fixed first component, discarded row-space components are translations only; the integrated scalar Fourier-power bound is uniform under those translations.

The entropy inequality

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`

then removes the number of subsets. The final estimate is uniform in `delta`; since `mu_t` is genuinely in `L^2`, standard approximate-identity convergence returns the unmollified norm. This closes the potentially delicate exceptional-slice/rough-density point.

# 4. Equation/label checklist

Every mathematical label in the pinned `proof_map.csv` was checked and receives **PASS**:

`thm:main`, `eq:main`, `cor:33`, `eq:parameters`, `lem:fourier`, `eq:plancherel`, `eq:inversion`, `eq:gaussian-inversion`, `lem:envelope`, `eq:envelope`, `lem:riesz`, `eq:riesz`, `eq:riesz-power`, `lem:rank`, `eq:rank-perturb`, `lem:schur`, `lem:dd`, `thm:bl`, `eq:frame`, `eq:bl`, `lem:projection`, `eq:projection`, `lem:scalar-fourier`, `eq:scalar-fourier`, `sec:fourier`, `eq:cross-form`, `lem:decoupling`, `eq:decouple2`, `eq:decouple4`, `thm:determinant`, `eq:determinant`, `eq:graph-bl`, `eq:Zk`, `eq:det-expand`, `cor:vol-fourier`, `eq:vol-envelope`, `eq:five-volume`, `eq:three-volume`, `sec:grouped`, `lem:grouped`, `eq:grouped-form`, `eq:grouped-envelope`, `eq:grouped-constant`, `eq:hub-cs`, `eq:mollified-light`, `eq:subset-bound`, `eq:subset-entropy`, `lem:terminal`, `eq:terminal`, `thm:free-volume`, `eq:free-three`, `eq:free-two`, `sec:pivots`, `lem:square`, `eq:profile`, `lem:definite`, `lem:hyperbola`, `eq:hyperbola`, `eq:hyper-coarea`, `lem:quarter`, `eq:quarter`, `eq:log-bound`, `sec:skeleton`, `def:pivot-volume`, `eq:Vr`, `eq:small-entry`, `lem:sampling`, `eq:P`, `eq:sampling`, `lem:completion`, `eq:completion`, `eq:completion-bounds`, `prop:volume`, `eq:volume-lower`, `lem:cut`, `eq:cut`, `cor:no-pivot`, `eq:no-pivot-five`, `eq:no-pivot-nine`, `sec:finish`, `lem:kernels`, `eq:J`, `lem:pair-full`, `eq:pair-full`, `prop:five`, `eq:five-half`, `eq:scalar-branches`, `sec:overlap`, `eq:W`, `thm:overlap`, `eq:overlap-tail`, `eq:orthogonal-error`, `cor:eight-overlap`, `eq:eight-overlap`, `eq:eight-explicit`.

# 5. Audit-package files

- `README.md`: **PASS** for scope/source mapping; its mathematical claims match the source. PDF delivery/visual inspection metadata is not independently reproduced here.
- `NINE_400_AND_OVERLAP.md`: **PASS** as a faithful derivation/handoff; no stronger eight-direction claim is smuggled in.
- `AUDIT_NEW.md`: **PASS** as an authoring-agent self-audit description, but it is not independent evidence for this review.
- `MANIFEST.json`: **PASS** for internal consistency of paths/blob/line/byte metadata as reported by the package; SHA-256/PDF binary metadata **UNCHECKED** independently.
- `proof_map.csv`: **PASS**; labels/ranges agree with the source used above.
- `verify_new.py`: **PASS** for the finite algebraic checks it actually implements. It correctly labels floating spectral tests as diagnostics and does not purport to formalize the proof.
- `checks_new.json`: **PASS** as the recorded output corresponding to the checker logic. The exact margins/constants agree with independent arithmetic checks in this run. Universal proof status does not follow from these finite cases.

# 6. Independent-review conclusion

For the exact pinned nine-eigenvalue constant-400 revision, my verdict is **PASS**. I found no mathematical GAP or FALSE item. The only UNCHECKED items are nonessential production/prior-art metadata listed above. This is one complete independent reconstruction. A distinct second worker must still complete its own full source review before the owner-level independent-validation gate can be considered satisfied.

Multiplicity eight remains open in this review. A new fixed-anchor overlap receiver proved in the sibling improvement file sharpens the remaining analytic debt without claiming a lower theorem.
