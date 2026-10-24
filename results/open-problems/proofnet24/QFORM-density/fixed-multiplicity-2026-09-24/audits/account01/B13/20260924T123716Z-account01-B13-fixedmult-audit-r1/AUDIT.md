# account01/B13 independent audit — definite pair and full hyperbolic envelope

Run: `20260924T123716Z-account01-B13-fixedmult-audit-r1`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution status: `WITHOUT_VERIFIED_BRAIN`

## Source pin

- Canonical repository/branch: `yspennstate/math-open-problems`, `master`.
- Canonical manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
- Owner-pinned initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Manuscript git blob read in full: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Owner-pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Fresh `master` observed during this review at `0822f7541df7d2229d591c4212b049b8e44923e5`; the manuscript blob remained the pinned blob above.

I read the complete 790-line manuscript independently before consulting completed peer audits. The assigned starting lens was the definite-pair Jacobian, both signs of the hyperbolic level set, original-coordinate tail changes, cap/mass use, logarithmic envelope, and critical-value averaging. I then performed a forward line audit and a separate reverse dependency audit of the full theorem.

## Verdict

**Mathematical verdict on the pinned 17-eigenvalue theorem: PASS.** I found no theorem-breaking FALSE statement and no fatal mathematical GAP in the written claim

\[
s_{17}(A)\ge s>0,\quad 0\le f_i\le K\ \text{a.e.}
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s,
\]

with arbitrary dimension, signature, remaining spectrum, affine terms, and independent rough coordinate laws.

This is one worker's independent mathematical audit, not a self-awarded validation certificate and not a proof of the unrestricted three-eigenvalue conjecture.

**GAP-PRESENTATION, theorem unaffected:** the theorem states density caps almost everywhere, while the square/hyperbola inverse-branch formulas write pointwise values of selected density representatives. At the outset one should choose Borel representatives and clip them pointwise to `[0,K]`; this changes no law and makes every later pointwise cap literal. The manuscript already makes this choice locally in the projection lemma, but one global sentence would remove the ambiguity everywhere.

**GAP-PACKAGING / UNCHECKED diagnostics:** fresh direct root reads returned 404 for `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, although README/AUDIT advertise them. The manuscript proof is self-contained, so this is not a mathematical gap. I did not count the advertised finite-test totals as evidence. I ran only the limited independent numerical diagnostics described below.

## B13 reconstruction 1: definite pair

Source: `manuscript.tex` lines 401–438, `lem:definite`.

**PASS.** Let the two-coordinate quadratic part be a symmetric definite matrix `B`. After a deterministic translation and sign change, take eigenvalues `mu_1,mu_2>0` and an orthonormal eigenbasis. The level `q(w)=v+delta`, `delta>0`, is parametrized by

\[
w=w_0+\sqrt{\delta/\mu_1}\cos\theta\,e_1+
\sqrt{\delta/\mu_2}\sin\theta\,e_2,
\qquad 0\le\theta<2\pi.
\]

The absolute Jacobian of `(delta,theta) -> w` is exactly

\[
\frac1{2\sqrt{\mu_1\mu_2}}=\frac1{2\sqrt{|\det B|}}.
\]

If the joint input density is bounded by `M`, integrating in `theta` yields

\[
p_q(z)\le \frac{\pi M}{\sqrt{|\det B|}}.
\]

The orthogonal eigenbasis change is a deterministic integration change of variables with Jacobian one; it never asserts independence of rotated random coordinates. In the theorem, conditioning on all other *original* coordinates leaves the selected pair independent with joint density at most one, so the lemma applies exactly as stated.

## B13 reconstruction 2: hyperbolic pair, both signs and original-coordinate tails

Source: lines 439–492, `lem:hyperbola`.

**PASS after the global density-representative convention above.** Write the eigenvalues of the fixed indefinite pair as `mu_+>0>-nu`, `nu=|mu_-|`, and set `D=mu_+ nu`, `Lambda=mu_+^{-1}+nu^{-1}`.

For `delta=z-v>0`, the two connected components of the level set are

\[
w_\epsilon(t)=\epsilon\sqrt{\delta/\mu_+}\cosh t\,e_+
 +\sqrt{\delta/\nu}\sinh t\,e_-,\qquad \epsilon=\pm1.
\]

A direct determinant calculation gives

\[
\left|\det \frac{\partial w_\epsilon}{\partial(\delta,t)}\right|
=\frac1{2\sqrt D}.
\]

Hence the output density, interpreted via nonnegative test functions/coarea, is

\[
p_q(v+\delta)=\frac1{2\sqrt D}
\sum_{\epsilon=\pm1}\int_\mathbb R
f_1(w_{\epsilon,1}(t))f_2(w_{\epsilon,2}(t))\,dt.
\]

For one branch write `w_epsilon(t)=u e^t+w e^{-t}`. Orthogonality gives

\[
|u|=|w|=\rho_0=\frac12\sqrt{\delta\Lambda}.
\]

Choose an **original physical coordinate** `i` with `|u_i|>=rho_0/sqrt(2)`. Since `|w_i|<=rho_0`, the ratio is at most `sqrt(2)`. For

\[
t\ge T_1=\frac34\log2,
\]

one has `|w_i|e^{-t} <= |u_i|e^t/2`, so the original coordinate is monotone, stays on one side of zero, and

\[
\frac12|u_i|e^t\le |w_i(t)|\le\frac32|u_i|e^t,
\qquad |w_i'(t)|\ge |w_i(t)|/3.
\]

Taking

\[
T=\max\{T_1,\log(2/|u_i|)\}
\]

ensures the coordinate magnitude is at least one at the tail entrance. Because the other marginal density is pointwise at most one,

\[
f_1(w_1(t))f_2(w_2(t))\le f_i(w_i(t)).
\]

Changing variables in that **original coordinate** gives

\[
\int_T^\infty f_1(w_1(t))f_2(w_2(t))dt
\le3\int_{|y|\ge m,\,\text{one sign}}\frac{f_i(y)}{|y|}dy,
\qquad m\ge1.
\]

The cap-one/mass-one hypotheses are both used here: among `0<=f<=1` with mass at most one on that half-line, the decreasing weight `1/|y|` is maximized by filling the length-one interval adjacent to `m`, giving at most `3 log(1+1/m)<=3 log2`. No moment or support assumption is used.

The negative tail is identical after using a (possibly different) original coordinate in which `w` is large. From `|u_i|,|w_j|>=sqrt(delta Lambda)/(2sqrt2)`, both cutoffs are bounded by

\[
\frac34\log2+\frac12\log_+\frac{32}{\delta\Lambda}.
\]

The middle interval is paid by the trivial product-density bound one. Thus each branch contributes at most

\[
\frac{15}{2}\log2+\log_+\frac{32}{\delta\Lambda}
<6+\log_+\frac{32}{\delta\Lambda}.
\]

Summing the two branches cancels the factor `1/2` in the Jacobian. Since `Lambda>=2/sqrt(D)`, this yields exactly

\[
p_q(v+\delta)\le D^{-1/2}
\left(6+\log_+\frac{16\sqrt D}{\delta}\right).
\]

For `delta<0`, apply the same derivation to `-B` (equivalently swap the positive and negative eigendirections). The determinant modulus and original-coordinate density caps are unchanged, so the same bound holds. The critical level `delta=0` is a single Lebesgue-null output value and is never used as a pointwise conditional-density assertion; the later argument uses integrated domination/Tonelli.

## B13 reconstruction 3: logarithmic critical-value averaging

Source: lines 652–760, especially `lem:kernels`, `prop:pivot-H`, and the main indefinite-pair branch.

**PASS.** Conditioning on the complement and completing the square in a fixed original indefinite pair produces an environment-dependent critical value `R` whose quadratic matrix is exactly the Schur complement. The Schur spectral-count lemma gives at least one surviving eigenvalue of modulus at least one in the main theorem, hence `||S||>=1`. The quarter-power concentration lemma therefore gives uniformly in `a`

\[
\mathbb E\log_+\frac1{|R-a|}\le L_0=4+4\log16.
\]

The elementary inequality

\[
\log_+\frac{16\sqrt D}{|z-R|}
\le \log_+(16\sqrt D)+\log_+\frac1{|z-R|}
\]

is legitimate for all positive factors. Averaging the hyperbolic envelope by Tonelli consequently gives an a.e. density bound. No common exceptional conditional-output slice is selected, and no conditional marginal density cap is inferred from a rotated or projected marginal.

For the truncated half-potential branch, the logarithmic kernel integral

\[
\int_{-1}^{1}|x|^{-1/2}\log_+\frac1{|x-a|}\,dx\le8
\]

is correctly obtained by layer-cake overlap: both superlevel sets are intervals, and their overlap is maximal when their centers coincide.

## Forward end-to-end audit

| Source range | Object | Status | Reasoning / downstream impact |
|---|---|---|---|
| 1–100 | definitions; theorem/corollary; normalization; Fourier conventions | PASS | Quantifiers retain all signs, dimensions, affine terms, remaining spectrum and rough product laws. `Y=KX` later gives the correct `K^2/s` scaling. |
| 101–160 | Plancherel/inversion; power envelope; Riesz half potential | PASS | Gaussian regularization avoids assuming an output density. Riesz Tonelli steps are on nonnegative majorants. The weighted `3/4` envelope integral is exactly `12 sqrt(u)`. |
| 161–220 | singular-value perturbation; Schur spectral count; diagonal dominance | PASS | Nonsymmetric singular-value perturbation is used in the right direction. In the invertible Schur proof, `S^{-1}` is the complementary principal block of `A^{-1}` and positive/negative interlacing separately gives the absolute-count inequality. The singular approximation with threshold `t-|eps|` closes by continuity. |
| 221–300 | geometric BL; product projections; scalar Fourier powers | PASS | Heat-flow derivative has the correct sign by the Parseval-frame contraction. Projection rotates only deterministic integration variables. Scalar Fourier powers use Plancherel integrability plus the genuine cap-one product projection. |
| 301–400 | decoupling; regularized determinant; crossing volumes/envelopes | PASS | Cauchy/Jensen exponents are correct. BL graph weights satisfy an exact frame identity; `alpha=(2 pi e)^2` cancels the entropy factor and the fourth root gives determinant exponent `-1/8`. Cauchy–Binet normalization and order-3/order-5 exponents are correct. |
| 401–526 | scalar square; definite pair; hyperbolic pair; quarter concentration | PASS with presentation repair | Square preimage length and definite Jacobian constants are correct. Hyperbolic proof reconstructed above. Quarter random-sign cut stays in original coordinates; Gaussian smoothing coefficient is `<16`; layer cake gives `L0`. |
| 527–600 | disjoint volumes; sampled interpolation; completion | PASS | Bordered determinant identity is exact; singular seeds justify `<=`, not an equality. `P=A[:,T]B^{-1}A[S,:]` interpolates rows `S` and columns `T`; `R-P` is supported on rows `T` or columns `S`, so `rank R<=3r`; on `LxL`, `R=P`, hence restricted rank `<=r`; `D` vanishes on the seed. |
| 601–651 | spectral-to-volume; random cut; no-pivot analytic consequences | PASS | With `eps<=(r+1)/80<=1/16`, `m=4k-3` forces `r+1` large entries of `D` in `L`. On their block, diagonal lower bound `371/400` exceeds row off-diagonal sum `23/28` by `297/2800>0`, contradicting restricted rank. Random cut factor is exactly `4^{-k}`. |
| 652–720 | singular kernels; pivot half potential; nine-direction bound | PASS | Kernel estimates use nonnegative Tonelli/rearrangement. Scalar pivot uses measure domination plus Schur/quarter potential; pair bounds are uniform in all induced affine shifts. Truncation plus the outside kernel bound one correctly gives full half potential. |
| 721–760 | four main branches; general `K,s` scaling | PASS | No-pivot, scalar, definite and indefinite branches exhaust pivots. Schur count loses only pivot dimension. Output scaling gives exactly `K^2/s`. |
| 761–790 | threshold accounting; limitations; regularity | PASS | Order five is used for direct density, order three only for half-potential. No claim of `s_3` sufficiency or global continuity is made. |

No mathematical manuscript range remains UNCHECKED in this review. Only the missing advertised finite-check package is UNCHECKED.

## Separate reverse dependency review

I performed a second, reverse-direction audit rather than rereading the table mechanically:

1. Main no-pivot branch -> order-five volume envelope -> random cut -> `prop:volume` -> completion/sampling -> singular-value rank lemma and entry bounds. All hypotheses close; no symmetry is silently imposed on `R,E`.
2. Main scalar branch -> square profile -> nine-direction full half potential -> pivot/no-pivot split -> Schur count/quarter potential or order-three crossing. Affine terms survive every completion of squares.
3. Main definite branch -> conditional two-coordinate joint cap -> deterministic definite Jacobian. No rotated independence is used.
4. Main indefinite branch -> conditional hyperbolic envelope -> Schur survivor -> quarter logarithmic potential -> Tonelli average. Both hyperbola signs and the critical value are covered.
5. Crossing determinant -> decoupling -> scalar Fourier powers/product projection -> geometric BL -> Fourier normalization. The product structure is used only before deterministic integrations; no spectral rotation of the random coordinates is introduced.
6. Final normalization -> `Y=KX`, matrix `A/s`, affine rescaling, scalar output scaling. The theorem constant acquires exactly `K^2/s`.

This second pass found no additional theorem-breaking gap. Because it is the same worker, it is **not** counted as a second independent validation review.

## Limited independent diagnostics (not proof)

The advertised root checker files are absent, so I did not claim to rerun them. I did run small independent diagnostics for arithmetic and the B13-sensitive spectral link:

- 2,000 random symmetric Schur-complement cases, dimensions 3–11 and pivot sizes 1–3, tested at thresholds `0.1,0.3,1,2`: zero violations of `N_S(t)>=N_A(t)-k`.
- Exact/numerical constants: diagonal-dominance slack `371/400-23/28 = 0.106071428571...`; quarter-power coefficient `3.99525936158<16`; no-pivot half-potential constant `12 sqrt(80e)=176.959336187<200`; no-pivot density branch `800e=2174.62546277<2400`.
- Hyperbola middle/tail constant `(15/2)log2=5.19860385420<6`.

These are diagnostics only; the symbolic arguments above are the proof.

## Threshold-lowering audit

The global multiplicity **is not lowered below 17 in this run**. I tested the only direct same-architecture reduction, `17 -> 16`, and it fails at a precise terminal rank saturation rather than at a loose numerical constant.

For order-five crossing, the telescoping bad ratio can occur at `r=4`. The completion then has

\[
\operatorname{rank}R\le12,\qquad \operatorname{rank}R[L,L]\le4.
\]

Under `s_17(A)>=1`, global rank perturbation leaves **five** entries of `D` of modulus at least `1-eps`; all are in `L`. Their `5x5` block of `R[L,L]` is strictly diagonally dominant, hence rank five, contradicting the restricted rank bound four.

Under only `s_16(A)>=1`, the identical argument forces only **four** large diagonal entries. A strictly diagonally dominant `4x4` block has rank four, which is fully compatible with `rank R[L,L]<=4`. Thus simply replacing `17` by `16` in the manuscript is invalid. This is a rigorous barrier for the present interpolation/rank mechanism, not a counterexample to the 16-eigenvalue theorem.

Branchwise, the proof needs much less multiplicity whenever a pivot is present: a scalar pivot needs only ten original spectral directions (nine after the one-coordinate Schur loss); a definite pair needs no spectral survivor for its conditional density estimate; an indefinite pair needs three original directions (one after a two-coordinate Schur loss). The **sole global 17-direction bottleneck is the no-pivot order-five crossing branch**.

I also examined whether order-four crossing plus the already-proved half-potential/logarithmic controls would close a 13-direction theorem. It does not: the determinant envelope is then only `|t|^{-1}`, which is nonintegrable, and bounded negative-half/logarithmic potentials do not by themselves imply an `L^infty` density (a logarithmically singular density is the model obstruction). A genuinely new receiver, not a constant tweak, is required to lower the global multiplicity.

## Constant sharpening (valid without changing multiplicity)

The manuscript rounds the nine-direction truncated half-potential to `600`. Keeping its exact dominant scalar-pivot value gives

\[
H_*=10(8+3L_0)=200+120\log16,
\qquad L_0=4+4\log16.
\]

The full nine-direction half-potential is therefore at most

\[
201+120\log16=533.7106466687\ldots.
\]

The main scalar-pivot branch is bounded by

\[
10(201+120\log16)
=2010+1200\log16
=5337.1064666877\ldots.
\]

All other normalized branches are smaller (`800e≈2174.63`, definite pair `10pi≈31.42`; the exact monotone maximization of the main indefinite branch over `D>=1/100` is `10[6+L_0+log(1.6)]≈215.60`). Thus the **same proven 17-eigenvalue argument** supports the stronger universal constant

\[
\boxed{(2010+1200\log16)K^2/s}
\]

without any new hypothesis. This is a constant improvement only; it does not lower multiplicity.

## Review/validation status

After completing my own audit, I observed actual complete audit artifacts from `account01/B11` and `account03/B14`. I do not substitute their verdicts for my reasoning and do not self-award an independent-validation certificate. Any release/validation status should be set by the designated release gate after checking the actual artifacts and current control. The unrestricted three-eigenvalue problem remains OPEN.
