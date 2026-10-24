# account03/B15 r11 — complete nine/400 audit, independent nine/361 retune check, and same-height C0 closure

Run: `20260924T152326Z-account03-B15-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source pin and verdict

Fresh control moved the active review from the historical seventeen-direction manuscript to the standalone nine-direction candidate. I therefore read the complete 955-line source in this invocation, rather than relying on previous B15 summaries.

Pinned source:

- repository: `yspennstate/math-open-problems`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`
- SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
- length: 955 lines.

I also read the source-pinned `README.md`, `NINE_400_AND_OVERLAP.md`, `AUDIT_NEW.md`, `MANIFEST.json`, and `proof_map.csv`.

**Verdict on the mathematical nine/400 candidate: PASS WITH ONE LOCAL PRESENTATION REPAIR.** I found no fatal mathematical gap in

\[
s_9(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 400 K^2/s
\]

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, arbitrary dimension, and arbitrary affine `b,c`.

The one local issue is in the negative-tail paragraph of the hyperbolic-pair proof: the text switches from the positive-tail vector `u` to the negative-tail vector `w` but then reuses the coordinate chosen because `|u_i|>=|u|/sqrt(2)`. The repair is to choose the maximizing original coordinate independently on the two tails: `i_+` for `u` and `i_-` for `w`. Since `|u|=|w|`, both cutoffs and all constants are unchanged. This is a notation/presentation repair, not a mathematical obstruction.

After finishing my own reading I found separate account01/B01 and account02/B02 reviews on current master. Both also pass the source; account02/B02 independently records the same negative-tail coordinate repair. I do not self-award owner/release validation status here.

## 2. Complete audit ledger

- **Lines 1–86 — PASS.** The theorem quantifiers, interval formulation, normalization, and parameters `d=3/40`, `p=1/400`, `h=2/25`, `kappa=h^2=4/625` are consistent. Scaling `Y=KX` and output rescaling by `s/K^2` gives exactly the `K^2/s` factor.
- **Lines 87–164 — PASS.** Fourier convention, Plancherel, Gaussian inversion, the power-envelope integral, and the Riesz half-potential constants are mutually consistent. In particular
  \[
  E|Z-a|^{-1/2}\le(2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|dt,
  \]
  and the `3/4` envelope integrates to `12 sqrt(u)` before the Fourier prefactor.
- **Lines 165–215 — PASS.** Singular-value perturbation, rank subtraction, singular Schur limiting argument, and strict diagonal dominance are applied to the correct (possibly nonsymmetric) auxiliaries.
- **Lines 216–297 — PASS.** The geometric Brascamp–Lieb heat-flow proof and product-projection lemma use deterministic orthogonal linear algebra only; no rotated random-coordinate independence is asserted. The explicit restricted-index inequality `sum_{b_i>0}(1-b_i)<=d` is present. Scalar Fourier-power normalization is correct.
- **Lines 298–396 — PASS.** Decoupling uses an independent copy only in a literal original-coordinate product bank. The regularized determinant frame, Cauchy–Binet volume expansion, graph weights, and determinant exponent `-1/8` check. No forbidden pointwise van-der-Corput claim appears.
- **Lines 397–477 — PASS.** This is the delicate grouped product-Fourier block. The phase-weighted image has an a priori `L2` density; Jensen is applied only after mollification; the duplicate is introduced only in the literal `J` bank; the pure `J` phase is discarded only after the original `I` variables are integrated; Holder is used for a finite, not necessarily probability, kernel measure; and the row-Gram Jacobian is the stated `S^2 det(C_TC_T^T)`. Approximate-identity convergence closes the unmollified estimate.
- **Lines 478–527 — PASS.** Row promotion keeps literal original coordinates as hubs. The Gram–Schmidt incident-volume identities are exact. The terminal constants recompute to
  \[
  C_3=3\sqrt2\,e(9/2)^{1/6}=14.818337662843\ldots<15,
  \]
  and
  \[
  C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots<14.
  \]
  Order three gives density; order two gives only a full half-potential.
- **Lines 528–562 — PASS.** Scalar-square and definite-pair changes of variables have the right Jacobians and are used as measure domination after conditioning on complementary original coordinates.
- **Lines 563–606 — PASS AFTER LOCAL REPAIR.** The hyperbolic parameterization and coarea Jacobian are correct. Positive-tail control uses an original physical coordinate and the one-dimensional density cap. The negative tail requires an independent maximizing coordinate for `w`, as described above; after that repair the same cutoff and bound follow.
- **Lines 607–662 — PASS.** Quarter-power concentration, atom exclusion, and logarithmic-potential layer cake are valid. The gamma coefficient estimate has room to spare.
- **Lines 663–715 — PASS.** Ordered disjoint volumes, determinant-squared seed sampling, bordered determinant identity, nonsymmetric completion, global rank `<=3r`, restricted rank `<=r`, and seed support are all correctly stated. Singular seeds are excluded from the probability measure, so the extension count is correctly an inequality.
- **Lines 716–766 — PASS.** The spectral-to-volume proof for `k<=3` closes. The exact worst diagonal-dominance margin at `r=2` is `51/2200>0`; the `r=1` margin is `1131/2200>0`. Random cut gives the order-two and order-three consequences with no dimension factor.
- **Lines 767–811 — PASS.** The sharper convolution kernel and full pair half-potential correctly distinguish definite and indefinite pairs and scale as `D^{-1/4}`. At `delta=1/64`, the normalized indefinite-pair bound is `12+5 log 2<16`.
- **Lines 812–860 — PASS.** The five-direction full half-potential trichotomy closes each scalar-pivot child. The main normalized branch values recompute numerically to approximately `370.458`, `255.604`, `261.279`, `360.847`, `62.832`, and `384.575`, all below the paper's safe rational envelopes and below 400. Full versus truncated half-potentials are not conflated.
- **Lines 861–927 — PASS.** The overlap theorem uses only nonsingular disjoint seeds. `D` diagonal and `E` zero diagonal give exact Frobenius orthogonality. Best rank-`3r` approximation and the two sampling expectations yield
  \[
  W_{r,1}^{\times}+(r+1)^2V_{r+1}\ge V_r\sum_{j>3r}s_j(A)^2.
  \]
  Under `s_8>=1`, the stated `W_{2,1}^{\times}>=2V_2-9V_3` follows. It is correctly not promoted to an eight-direction density theorem.
- **Lines 928–955 — PASS for mathematical dependency closure.** Threshold accounting is accurate: nine is sufficient, while eight and three remain open. The two bibliography entries are attribution only; no specialized unproved theorem is imported from them because the needed analytic inequalities are proved in the source itself.

No mathematical source range remains UNCHECKED in this B15 audit. I did not rerun the package's finite diagnostic script; those finite checks are not part of the all-dimensional proof.

## 3. Independent check of the new nine-direction constant-361 retuning

After the complete source audit, I independently checked the fresh account02/B02 retuning at

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account02/B02/account02-B02-20260924T151017Z-auto11/IMPROVEMENT_361.md`.

It changes only the structural parameters, retaining the now-audited analytic receivers. I find the retuning **PASS**.

Normalize `K=s=1` and take

\[
d=\frac{47}{625},\qquad
p=\frac{57}{20000},\qquad
h=\frac{411}{5000},\qquad \kappa=h^2.
\]

In the no-pivot chamber,

\[
p+d^2=\frac{106313}{12500000}
<\left(\frac{923}{10000}\right)^2,
\]
with exact slack `57/4000000`. Writing `q=923/10000`, the two nontrivial diagonal-dominance margins are exactly

\[
1-d-q-4h=\frac{5037}{10000}>0,
\]

and

\[
1-d-2q-9h=\frac1{2500}>0.
\]

Hence the same interpolation proof gives `V_k>=kappa^k` for `k<=3` at the required spectral thresholds. A fair cut yields `Z_3^{-1/6}<=2/h=10000/411` and `Z_2^{-1/8}<=sqrt(2/h)`.

The rational analytic certificates also check:

\[
C_3<\frac{232551}{15680}
\]

from `sqrt2<99/70`, `e<87/32`, `(9/2)^(1/6)<9/7`, and `C_2<13`. The logarithmic bounds

\[
\log2<347/500,\qquad \log5<161/100
\]

are certified by the displayed positive exponential Taylor partial sums; they imply

\[
J_0+2L_0<\frac{23449}{875},\qquad
6+\log16+L_0<\frac{2402}{125}.
\]

The six normalized branch bounds then satisfy, exactly as needed,

\[
\frac{232551}{15680}\frac{10000}{411}
=\frac{9689625}{26852}<361
\]
with slack `3947/26852`,

\[
C_2\sqrt{\frac2{dh}}<234,
\]

\[
16p^{-1/4}d^{-1/2}<270,
\]

\[
d^{-1/2}+\frac{J_0+2L_0}{d}
<\frac{473915}{1316}<361
\]
with slack `1161/1316`,

\[
\pi p^{-1/2}<59,
\]

and

\[
p^{-1/2}(6+\log16+L_0)+1/e
<\frac{1804}{5}=360.8<361.
\]

I separately evaluated the exact analytic expressions as a diagnostic: the corresponding values are approximately `360.5435`, `217.5598`, `252.5224`, `359.8924`, `58.8474`, and `360.2105`. The proof does not depend on those decimals.

Therefore the retuned theorem is mathematically supported by the audited source:

\[
\boxed{
 s_9(A)\ge s>0
 \Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_\infty<361\,K^2/s.
}
\]

This report is an independent second mathematical check of that parameter retuning, but owner/release status is not self-assigned here.

## 4. Absolute continuity is strictly easier than the height theorem

For clarity on the B15 role, density existence does not require nine, or even three, large eigenvalues.

Let the joint law of `X` be absolutely continuous and let

\[
q(x)=x^TAx+b^Tx+c
\]

be nonconstant. Its critical set is

\[
\{x:2Ax+b=0\},
\]

which is empty or a proper affine subspace, hence Lebesgue-null. If `N` is a one-dimensional null set, apply coarea on

\[
E_k=q^{-1}(N)\cap\{|\nabla q|\ge1/k\}.
\]

Then

\[
\int_{E_k}|\nabla q(x)|dx
=\int_N\mathcal H^{n-1}(E_k\cap q^{-1}(t))dt=0,
\]

so `|E_k|=0`. Adding the null critical set shows `|q^{-1}(N)|=0`. Thus every nonconstant affine quadratic pushforward of an absolutely continuous joint law is absolutely continuous. Product structure and the density cap are unnecessary for this qualitative implication. It supplies no universal height or continuity modulus.

## 5. New same-height C0 closure for the current nine-direction theorem

The current `paper.tex` deliberately states only an essentially bounded density globally, because several pivot branches are proved by measure domination rather than an `L1` characteristic-function envelope. At the target level this is no longer a separate obstruction.

A completed account03/B15 fixed-instance theorem, source-pinned at

`yspennstate/math-open-problems@b8cb4aa22c840d8f4fc76bcca6d0cb49d4aeb9f9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260924T092642Z-account03-B15-qform-auto11/REPORT.md`,

proves that for every fixed symmetric `A` with `rank(A)>=3`, arbitrary affine `b,c`, and arbitrary cap-one product marginals, the output has a canonical density in `C_0(R) cap L^infinity(R)`. Its proof is independent of any universal height constant and is uniform in the affine terms at fixed `A`.

Since `s_9(A)>=s>0` implies `rank(A)>=9`, combine that qualitative theorem with the retuned interval domination. If the continuous representative exceeded `361 K^2/s` at one point, continuity would give an interval whose probability exceeds the paid interval bound. Therefore the retuned theorem strengthens, at zero height cost, to

\[
\boxed{
 p_{X^TAX+b^TX+c}\in C_0(\mathbb R),\qquad
 \|p_{X^TAX+b^TX+c}\|_\infty<361\,K^2/s.
}
\]

There is no claim of a matrix-uniform modulus of continuity. The statement is that qualitative continuity and the quantitative universal height separate cleanly: once the interval height is paid, continuity costs no additional constant.

## 6. Designated account04/B15 result applied to an actual inequality

To satisfy the cross-worker obligation without attributing the affine extension to the partner, apply account04/B15 Theorem 6.1 from

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`.

That theorem states: for a fixed **homogeneous** rank-at-least-three quadratic form under cap-one product inputs, any separately proved interval estimate

\[
P\{X^TAX\in I\}\le M|I|
\]

upgrades to a canonical `C_0` representative with the identical height `M`.

Take the actual normalized inequality supplied by the independently checked retuning, with `K=s=1` and `b=c=0`:

\[
P\{X^TAX\in I\}<361|I|.
\]

Because `rank(A)>=9`, the partner theorem applies directly and yields

\[
\boxed{p_{X^TAX}\in C_0(\mathbb R),\qquad \|p_{X^TAX}\|_\infty\le361.}
\]

Scaling `Y=KX` and `A` by `s` gives the homogeneous general-scale statement with height `361K^2/s`. The arbitrary-affine conclusion in Section 5 uses the completed account03/B15 affine fixed-instance theorem, not a scope expansion of the account04 homogeneous theorem.

## 7. Relation to multiplicity eight

This regularity closure does not solve multiplicity eight. The newest eight-direction work retains a strong two-anchor cross map and four exterior singular directions, and a compatible-cut joint-`L2` receiver would close a substantial terminal chamber. The current source's overlap theorem supplies additional shared-coordinate mass, but no general product-preserving physicalization theorem converting those resources into a uniform `L^infinity` estimate has yet been proved.

Thus the correct threshold status after this run is:

- nine directions: complete bounded-density proof checked here; retuned constant `<361` independently checked here;
- nine directions, continuity: `C_0` with the same height constant by the fixed-instance regularity theorem and, in the homogeneous case, by the designated account04/B15 compiler applied to the actual interval inequality;
- eight directions: OPEN;
- unrestricted three-eigenvalue conjecture: OPEN;
- counterexample to the full conjecture: none found.

No Gaussian, log-concave, moment, support, connectedness, diagonal-basis, post-rotation independence, arbitrary-joint coarea height, or pointwise bounded-density phase-decay assumption is used.
