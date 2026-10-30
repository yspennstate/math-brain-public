# fleet02/B13 — independent fixed-multiplicity audit r14

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and scope

Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.

Baseline `manuscript.tex` git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Baseline `manuscript.tex` SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Baseline source size: 47,883 bytes, 790 lines.

Package snapshot actually read on live `master`: through `b9191448f57843bffd3718a9b328929bfec1e9c5`; the source manifest says `source_unchanged=true`, and the manuscript blob/hash at that snapshot is exactly the pinned baseline above.

Files read in full in this run: `README.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The full three-eigenvalue conjecture is **not** claimed solved.

## Verdict

**Baseline 17-eigenvalue manuscript: PASS.** I found no mathematical gap or false statement in the written theorem

\[
s_{17}(A)\ge s>0\Longrightarrow
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

under the stated arbitrary independent cap-`K` coordinate laws, arbitrary real symmetric `A`, arbitrary signs, dimension, remaining spectrum, and arbitrary affine terms. No source range remains `UNCHECKED` in this run.

**Package reproducibility/documentation: one non-mathematical GAP.** Historical `AUDIT.md` records older finite-test counts (for example 504 interpolation seeds and 800 Schur diagnostics), whereas the currently supplied reproducibility suite actually reports 534 interpolation seeds and 240 Schur threshold cases. `README.md` and `SOURCE_MANIFEST.json` explicitly disclose that the present checker is a new suite and does not reproduce the historical counts. Impact: none on the analytic proof; next obligation only if historical computational provenance itself is to be reconstructed.

## Exhaustive 790-line audit matrix

The following ranges partition the manuscript without gaps. “PASS” means I checked every definition, quantifier, displayed equation, proof step and cited hypothesis in the range; detailed high-risk checks follow the table.

| Lines | Content / labels | Status | Reasoning / impact / next obligation |
|---|---|---|---|
| 1–46 | Preamble, abstract, notation | PASS | The abstract matches the theorem actually proved; no hidden regularity, support, sign, moment or rotated-independence hypothesis is introduced. |
| 47–61 | `thm:main`, `cor:33` statements | PASS | Quantifiers and scaling target are coherent: independent densities `<=K`, symmetric `A`, `s_17(A)>=s`, arbitrary `b,c`, essential density bound `10000 K^2/s`. |
| 62–90 | Architecture, parameters `eta=1/100`, `kappa=1/80^2` | PASS | The later proof uses exactly these parameters; 9 and 17 arise as `4*3-3` and `4*5-3`, not as an unstated theorem hypothesis. |
| 91–160 | Fourier inversion, power envelope, Riesz half-potential | PASS | Fourier normalization, Gaussian regularization, Tonelli and the `1/sqrt(2pi)` Riesz constant all recompute correctly; extended nonnegative values are handled legitimately. |
| 161–217 | Singular values, Schur count, diagonal dominance | PASS | Nonsymmetric singular-value perturbation is used where required. The Schur count follows from inverse compression, separately for positive and negative eigenvalues; the singular case is a valid `A+eps I` limit. |
| 218–301 | Geometric Brascamp–Lieb, product projections, scalar Fourier powers | PASS | Heat-flow sign and limiting argument check. Projection proof uses an orthogonal change only inside a deterministic integral and never asserts rotated independence. Scalar Fourier-power constant follows from Plancherel plus the physical-coordinate projection cap. |
| 302–400 | Cross decoupling, regularized determinant, crossing volumes | PASS | Decoupling copies only the required bank; pure phases are discarded only after modulus. Graph frame/Jacobian, `alpha=(2pi e)^2`, `-1/8` determinant exponent, Cauchy–Binet expansion, order-5 density and order-3 Riesz exponents all check. |
| 401–434 | Scalar square and definite pair | PASS | Square inverse branches and interval preimage length are correct. Definite-pair elliptic coordinates have Jacobian `1/(2 sqrt(|det B|))`; integrating the cap-`M` joint density over `theta` gives `pi M/sqrt(|det B|)` with no independence-after-rotation claim. |
| 435–482 | Full indefinite/hyperbolic pair envelope | PASS | Reconstructed below. The proof is valid for merely measurable cap-one product densities with fragmented/unbounded support; the only pair conditioning is on original coordinates. |
| 483–525 | Quarter-power concentration and logarithmic potential | PASS | Diagonal and off-diagonal alternatives exhaust `S!=0`; sign partition gives a physical crossing block of norm `>=L/4`; Gaussian smoothing yields the stated quarter-power bound; layer cake gives `L0=4+4 log16`. |
| 526–645 | Pivot volume, sampled interpolation, completion, spectral-to-volume, fair cut, no-pivot consequences | PASS | Ordered disjoint minors, inequality for singular seeds, nonsymmetric interpolation support, global rank `<=3r`, restricted rank `<=r`, zero seed diagonal, perturbation, diagonal-dominance contradiction and random-cut factor `4^{-k}` all check. |
| 646–674 | Truncated half potential and two singular kernels | PASS | The scaled near-region estimate for `J(d)`, outer logarithm, and shifted log-kernel overlap argument are valid with the stated constants. |
| 675–714 | Pivot half-potential proposition | PASS | Scalar, definite and indefinite alternatives use their exact hypotheses. In particular the indefinite pair uses determinant, not a minimum singular-value floor, and the logarithm is averaged through the surviving Schur direction. |
| 715–724 | Nine-eigenvalue half-potential proposition | PASS | Pivot branch gives truncated `<=600`; no-pivot order-3 route gives a stronger full half-potential; adding at most one outside `|Q-a|<=1` gives `<=601`. |
| 725–749 | Main theorem proof and scaling | PASS | No-pivot, scalar, definite-pair and indefinite-pair cases exhaust all possibilities. Schur counts 16/15 are more than sufficient. The `Y=KX`, `A/s` scaling yields exactly `K^2/s`. |
| 750–790 | Threshold accounting, limitations, bibliography | PASS | The text accurately limits the result to 17 directions, distinguishes full/truncated half potentials, and makes no unrestricted-three-eigenvalue or global-continuity claim. |

## B13 reconstruction: definite pairs and the complete hyperbolic envelope

### Definite physical pair — PASS, no minimum-singular-value gate

Conditioning on all other **original** coordinates leaves a two-dimensional joint density bounded by one. Completing the square and orthogonally diagonalizing the deterministic integral does not rotate the product law as a probabilistic assertion. If the eigenvalues of the conditioned pair matrix are `mu_1,mu_2>0`, the coordinates

\[
w=w_0+\sqrt{\delta/\mu_1}\cos\theta\,e_1+
\sqrt{\delta/\mu_2}\sin\theta\,e_2
\]

have absolute Jacobian `1/(2 sqrt(det B))` in `(delta,theta)`. Therefore

\[
\|p_q\|_\infty\le \pi M/\sqrt{|\det B|}.
\]

The gate is solely `|det B|`; no lower bound on `s_2(B)` is used or needed.

### Indefinite physical pair — PASS under arbitrary rough inputs

Write the eigenvalues as `mu_+>0>mu_-`, `D=|det B|`, and

\[
\Lambda=\mu_+^{-1}+|\mu_-|^{-1}.
\]

For `delta=z-v>0`, the two hyperbola branches are

\[
w_\epsilon(t)=\epsilon\sqrt{\delta/\mu_+}\cosh t\,e_+
 +\sqrt{\delta/|\mu_-|}\sinh t\,e_-.
\]

Direct differentiation gives absolute `(delta,t)` Jacobian `1/(2 sqrt D)`. Each branch can be written `u e^t+w e^{-t}` with

\[
|u|=|w|=\sqrt{\delta\Lambda}/2.
\]

Choose one **literal original coordinate** with `|u_i|>=|u|/sqrt2`. After `T_1=(3/4)log2`, the growing term dominates the decaying one by a factor two, so that coordinate is monotone, has one sign, and satisfies `|x_i'(t)|>=|x_i(t)|/3`. Taking

\[
T=\max\{T_1,\log(2/|u_i|)\}
\]

makes the tail start at radius at least one. On that tail the product density is bounded by the single original-coordinate density `f_i`, and the monotone change of variables gives

\[
\int_T^\infty f_1(x_1(t))f_2(x_2(t))dt
\le 3\int_{|y|\ge m,\,\text{one sign}}f_i(y)\frac{dy}{|y|}
\le3\log(1+1/m)\le3\log2.
\]

The rearrangement step uses only `0<=f_i<=1` and mass at most one on that half-line; it is valid for disconnected, fragmented and unbounded supports. The negative tail is identical using the `w e^{-t}` coefficient. Both cutoffs obey

\[
T,T'\le\tfrac34\log2+\tfrac12\log_+\frac{32}{\delta\Lambda}.
\]

The middle interval is paid only by the pointwise density cap, giving each branch integral

\[
\le \tfrac{15}{2}\log2+
\log_+\frac{32}{\delta\Lambda}
<6+\log_+\frac{32}{\delta\Lambda}.
\]

Summing both branches cancels the Jacobian factor two, and `Lambda>=2/sqrt D` gives exactly

\[
p_q(z)\le D^{-1/2}
\left(6+\log_+\frac{16\sqrt D}{|z-v|}\right).
\]

For `delta<0` the signs swap. Every use after conditioning can be phrased against a nonnegative output test function and Tonelli, so no exceptional rough conditional slice is selected.

### Why the logarithm cannot be deleted — counterexample

Let independent `X,Y` be uniform on `[-1/2,1/2]` and put `Q=X^2-Y^2=(X-Y)(X+Y)`. The linear map `(X,Y)->(U,V)=(X-Y,X+Y)` has joint density `1/2` on `|U|+|V|<=1`. Product coarea gives, for `0<|z|<1/4`,

\[
p_Q(z)=\log\frac{1+\sqrt{1-4|z|}}
                 {1-\sqrt{1-4|z|}}
=\log(1/|z|)+O(1).
\]

Thus a determinant-only **bounded conditional density** estimate for an indefinite pair is false even for compact interval product laws. The manuscript correctly keeps the logarithm and pays it by a surviving Schur direction.

### Pair gate in the main proof — PASS

For a principal pair pivot the proof assumes only `D=|det B|>=eta`. Definite pairs pay immediately. Indefinite pairs lose two spectral directions by Schur complement and need only one nonzero surviving direction to invoke the quarter-power/logarithmic-potential lemma. Averaging the hyperbolic envelope yields

\[
\|p_Q\|_\infty
\le D^{-1/2}\bigl(6+\log_+(16\sqrt D)+L_0\bigr),
\qquad L_0=4+4\log16.
\]

Using `D>=1/100` and `sup_{D>0}D^{-1/2}log_+D=2/e` gives the manuscript's `<251` claim (in fact the displayed bound is below 239). No minimum singular value of `B`, no support radius and no post-rotation independence enters.

## Lowering 17: independent audit of the complete nine-direction replacement

I also read all 359 lines of the current complete replacement proof `QFORM-FIXED-MULTIPLICITY-9-B01-REVIEWED-v1` (blob `7ad10848181dcbd9b962803bd7f61e2bf446907a`). **Verdict: PASS after two zero-loss endpoint conventions are made explicit.** It proves

\[
s_9(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 6010 K^2/s,
\]

with all baseline hypotheses unchanged.

The new grouped product-Fourier compiler is valid. Conditioning on a literal `X_I=x`, regularizing the pushforward, and copying only the `J` bank leaves the pure `I` phase cancelled and the pure `J` phase as a modulus-one factor. The original independent `I` coordinates then produce the scalar characteristic functions. For an `ell`-subset of residual rows the stacked map has Gram determinant

\[
S^2\det(C_TC_T^T),
\]

so the baseline product-projection theorem applies to the independent difference coordinates. Weighted Hölder uses exponents `1/alpha_i`, and the entropy identity

\[
H(w)+\sum_i\alpha_i\log\alpha_i
\le \ell\log\ell-\log(\ell!)
\]

follows by uniformly ordering the sampled subset and applying entropy subadditivity. The resulting envelope and inversion constants recompute correctly.

**Minor notation GAP 1, repaired:** if a marginal `alpha_i=0`, `1/alpha_i` is undefined. Omit that factor before weighted Hölder; it occurs in no positive-weight subset and contributes identically one. Constants are unchanged.

**Minor notation GAP 2, repaired:** the balanced order-three branch formally uses the compiler with `k=0`. Interpret the hub bank as absent, the empty singular-value product as one, and the zero-dimensional density cap as one (equivalently run the light-bank proof directly). Constants are unchanged.

The marginal-free order-three receiver becomes

\[
\|p_Q\|_\infty\le C_3 E_3(M)^{-1/6},
\qquad
C_3=3\sqrt2\,e(9/2)^{1/6}=14.818337662843\ldots,
\]

and the one-dimension-lower receiver gives the **full** half-potential

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le C_2E_2(M)^{-1/8},
\qquad C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots .
\]

The second statement is deliberately not a rank-two density theorem; `2XY` for independent compactly supported uniforms has the familiar logarithmic singularity.

The complete nine-direction proof then closes as follows. In the no-pivot branch the baseline `k=3` spectral-to-volume theorem and fair cut give `E_3>=4^{-3}kappa^3`, hence density `<2400`. At a scalar pivot, the Schur remainder has at least eight unit directions; if it has a pivot, the baseline truncated half-potential theorem plus the outside tail gives full half-potential `<=601`, while if it has no pivot then `s_5>=1`, the baseline `k=2` volume theorem plus fair cut and the new `E_2` receiver give full half-potential `<153`. Thus the scalar branch stays `<=6010`. Definite pairs stay `<32`, and indefinite pairs need only a surviving Schur direction and stay `<251`. Scaling restores exactly `6010K^2/s`.

Closed dependency map: baseline Fourier inversion/Riesz; geometric BL/product projection/scalar Fourier powers; Schur and scalar/definite/hyperbolic pivot lemmas; nonsymmetric sampled interpolation/completion/spectral-to-volume/fair cut; plus the newly proved grouped compiler and finite literal-row promotion trees. There is no dependency on the 17-direction main theorem itself.

Therefore **nine is a complete lower fixed multiplicity supported by a replacement proof in the current repository and independently checked in this B13 run.** This audit does not rewrite the pinned 17 manuscript or self-award release status.

## Why I do not claim eight: exact collar GAP and a B13 counterexample to a tempting shortcut

I read the current threshold-eight structural reduction `QFORM-EIGHT-DIRECTION-TERMINAL-OVERLAP1-COLLAR-v1`. Its algebra is PASS as a structural theorem, not as a density theorem. Under no pivot and `s_8(A)>=1`, either `V_3>=kappa^3` and the new order-three receiver pays the density, or one has

\[
V_2\ge\kappa^2,
\qquad
\Omega_1\ge c_*^2\kappa^2,
\qquad
\Xi_2\ge(\delta_*^2/2)\kappa^2,
\]

where `epsilon_*=3sqrt2/80`, `c_*=1-epsilon_*`, and `delta_*=0.854335140191...`. The unpaid implication is a product-preserving receiver for this overlap-one/two-sided collar when the common physical diagonal may vanish.

A simple local counterexample shows why the B13 pair lemmas cannot close that implication merely by extracting a principal pair pivot. Let `S,H,T` be three two-coordinate banks and, for `0<c<1/10`, set

\[
A_c=\begin{pmatrix}
0&cI_2&0\\
cI_2&0&cI_2\\
0&cI_2&0
\end{pmatrix}.
\]

Every diagonal entry is zero and every principal two-coordinate determinant is either zero or `-c^2`, so there is no `eta=1/100` pair pivot. Nevertheless

\[
\det A_c[S,H]=c^2,
\qquad
\det A_c[H,T]=c^2,
\]

and this single two-sided collar contributes `c^8` to `Xi_2`, while the common principal block `A_c[H,H]` is identically zero. Numerically the guaranteed collar scale `(delta_*^2/2)kappa^2=8.9097721...*10^{-9}` has eighth root `0.0985674...<0.1`, so even a collar term at that scale is compatible with the no-pivot gate. This is **not** an `s_8` counterexample; it is a source-valid counterexample to the shortcut “two-sided collar => principal pair pivot.” Any eight-direction proof must spend the collar through a genuinely overlapping product-law receiver, not by silently dividing by the common diagonal or determinant.

## Final status and next obligation

Baseline 17 theorem: **PASS**. Complete nine-direction replacement: **PASS in this review after the two explicit zero-loss endpoint conventions above**. Threshold eight: **GAP**, reduced to `QFORM-EIGHT-OVERLAP1-TWOSIDED-COLLAR-RECEIVER-v1`; the displayed local matrix rules out the simplest principal-pair extraction. Unrestricted three-eigenvalue QFORM remains open.
