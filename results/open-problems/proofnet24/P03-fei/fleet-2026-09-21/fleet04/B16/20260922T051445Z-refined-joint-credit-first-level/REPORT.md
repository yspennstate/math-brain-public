# fleet04/B16 — retain the forced negative zero-mode before Jensen: refined joint credit and a 7/40 critical-core exclusion

**Run:** `20260922T051445Z-fleet04-B16-fei-gate-joint-credit-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / REFINED_SIGNED_JOINT_CREDIT / FULL_FEI_OPEN`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Full unrestricted FEI:** **OPEN / NOT PROVED**

## 0. Later-owner precedence and exact sources consumed


The two inherited interface-C sources named by the standing B16 prompt were freshly read and retained at their proved scopes:

1. `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, creation revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`. After authentic same-syndrome signed aggregation its actual central parent weight is
   \[
   \mu^{\rm cen}_{R,j}=\frac{\varepsilon_{q_R,k_R}}{r_R}b_R^2,
   \]
   and the original-coordinate incidence bank is dimension-free. Relation coefficients are not positive-parted before the signed aggregate, and terminal/R16/entropy ledgers are not spent in that theorem.
2. `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, creation revision `4843e50690013fd18b85dd8763b53bdc75da79e8`. Its physical source is the oriented derivative curvature
   \[
   \kappa_i(w)=p_i(w)+4o_i(w),
   \]
   with opposite-sign overlap indispensable (parity has `p=0`, `kappa=4`) and paid under the ordered flag without consuming terminal or negative-entropy credits.

Their common lesson is used literally below: **do not replace a signed overlap by its absolute envelope until every forced orientation atom has been accounted for.** Dual-code multiplicity, R16/R32 negative credits, moment refunds, terminal terms, and the old finite-window remainder remain untouched in this all-gate calculation.

The live mathematical predecessor is fleet02/B13
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T045511Z-joint-credit-critical-core/REPORT.md` (scientific creation commit `547cb4e42877590ce8195a5a4859b0facb13877e`). It proved for arbitrary Boolean children at an unbiased pivot the signed-overlap/Jensen bound
\[
\mathcal C_j:=H(B\mid S)+I(S;J)
\ge
h_2\!\left(\frac{1-2\sqrt{\delta(1-\delta)}}2\right),
\tag{0.1}
\]
where `delta=Pr[f0 != f1]`, and from it obtained the central minimum-critical-core consequence
\[
\widehat f(\{j\})=0\Longrightarrow \operatorname{Inf}_j(f)<\frac14
\tag{0.2}
\]
for cap at least `13/2`.

A still newer compatible source, fleet02/B16
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260922T045841Z-source-bias-log-curvature/REPORT.md`, commit `831f7d862c785fddf0f77cbe3eb95a065e5ad902`, proves a coherent biased direction on the current composition-prime `n=18` source gate raises the requested gate margin at leading singular order. Its finite falsification remainder is not closed. The theorem below is orthogonal: it sharpens the exact central critical-core constraint and preserves a piece of signed information discarded by (0.1).

## 1. Exact balanced-parent geometry

Let the physical pivot `j` be unbiased and let the parent Boolean function be balanced. Its two restrictions
\[
f_0,f_1:\Omega\to\{-1,+1\}
\]
have opposite means. Write
\[
\mathbb E f_0=a,\qquad \mathbb E f_1=-a,
\qquad A:=a^2,
\qquad \delta:=\Pr[f_0\ne f_1].
\tag{1.1}
\]
In a real orthonormal Fourier basis write
\[
f_0=\sum_S a_S\chi_S,\qquad f_1=\sum_S b_S\chi_S,
\qquad T_S=\frac{a_S^2+b_S^2}{2}.
\]
For `T_S>0` put
\[
u_S=\frac{2|a_Sb_S|}{a_S^2+b_S^2},
\qquad \sigma_S=\operatorname{sgn}(a_Sb_S).
\tag{1.2}
\]
Then
\[
\sum_ST_S\sigma_Su_S
=\langle f_0,f_1\rangle
=1-2\delta.
\tag{1.3}
\]

The crucial extra fact, unavailable in the arbitrary-child version of (0.1), is that the empty Fourier atom is completely fixed:
\[
T_\varnothing=A,\qquad u_\varnothing=1,\qquad \sigma_\varnothing=-1.
\tag{1.4}
\]
Thus after removing that forced **negative orientation atom**, the residual signed overlap is exactly
\[
\sum_{S\ne\varnothing}T_S\sigma_Su_S
=1-2\delta+A,
\tag{1.5}
\]
and the residual mass is `1-A`. In particular feasibility itself gives
\[
\boxed{\delta\ge A=a^2.}
\tag{1.6}
\]
This is the familiar first-Fourier-coefficient/influence inequality, but here it appears as the capacity condition for the residual signed-overlap channel.

## 2. Refined signed joint-credit theorem

Following B13 define
\[
g(u)=h_2\!\left(\frac{1-u}{2}\right),
\qquad
\Psi(u)=1+g(\sqrt{1-u^2})-g(u).
\tag{2.1}
\]
The predecessor proves that `Psi` is strictly increasing and strictly convex on `(0,1)` and that the exact combined credit is
\[
\mathcal C_j=h_2(\delta)-1+\sum_ST_S\Psi(u_S).
\tag{2.2}
\]

Do **not** apply the triangle inequality to all atoms at once. Keep (1.4) exact, and apply triangle plus Jensen only to `S != emptyset`. Since `Psi(1)=2`,
\[
\begin{aligned}
\sum_ST_S\Psi(u_S)
&=2A+\sum_{S\ne\varnothing}T_S\Psi(u_S)\\
&\ge
2A+(1-A)\Psi\!\left(
\frac{|1-2\delta+A|}{1-A}
\right).
\end{aligned}
\]
Therefore:

### Theorem 2.1 — forced-zero-mode refined joint credit

For every balanced Boolean parent at an unbiased physical pivot, with notation (1.1),
\[
\boxed{
\mathcal C_j
\ge
h_2(\delta)-1+2A
+(1-A)\Psi\!\left(
\frac{|1-2\delta+A|}{1-A}
\right).
}
\tag{2.3}
\]
The endpoint `A=1` is interpreted by continuity and is trivial.

Equivalently, set
\[
s=\frac{\delta-A}{1-A}\in[0,1],
\qquad
y_s=\frac{1-2\sqrt{s(1-s)}}2.
\tag{2.4}
\]
Using the symmetry of binary entropy,
\[
\boxed{
\mathcal C_j
\ge
h_2(\delta)+A
+(1-A)\bigl[h_2(y_s)-h_2(s)\bigr].
}
\tag{2.5}
\]

At `A=0`, (2.3) reduces exactly to the B13 bound (0.1). For `A>0`, (2.3) is the source-valid refinement obtained by retaining the forced negative empty atom before convexification.

### Equality structure

Away from zero residual mass and zero residual overlap, equality in (2.3) requires triangle equality and strict Jensen equality **on the residual atoms**. Hence every residual common nonzero Fourier atom has the same relative sign and the same value of `u_S`; equivalently the residual coefficient ratios `|b_S|/|a_S|` take one reciprocal pair. The empty atom remains the forced opposite sign. This is an oriented two-sector rigidity statement, not a claim about arbitrary probability laws.

## 3. Exact insertion into the local gate cocycle

Let `Gamma` be any symmetric candidate potential and put
\[
C=\Gamma(1/2).
\]
For a balanced parent, symmetry gives child output biases
\[
r_0=\frac{1-a}{2},\qquad r_1=\frac{1+a}{2}.
\]
The exact restriction remainder at the unbiased pivot is
\[
\mathcal R_{\Gamma,j}
=\Gamma\!\left(\frac{1-|a|}{2}\right)-C
+\delta C-1-h_2(\delta).
\tag{3.1}
\]
Combining with (2.5) gives the new source-valid local bound
\[
\boxed{
\begin{aligned}
\mathcal R_{\Gamma,j}+\mathcal C_j
\ge Q_\Gamma(a,\delta):={}&
\Gamma\!\left(\frac{1-|a|}{2}\right)-C+C\delta-1+A\\
&+(1-A)\,[h_2(y_s)-h_2(s)].
\end{aligned}
}
\tag{3.2}
\]
No concavity, differentiability, or numerical interpolation property of `Gamma` is used.

For a minimum-essential-arity counterexample to the all-gate inequality, every proper physical child has nonnegative defect; therefore every essential pivot must satisfy
\[
\mathcal R_{\Gamma,j}+\mathcal C_j<0.
\tag{3.3}
\]
Consequently every balanced central minimum counterexample obeys the sharpened necessary condition
\[
\boxed{Q_\Gamma(|\widehat f(\{j\})|,\operatorname{Inf}_j(f))<0}
\tag{3.4}
\]
for each essential coordinate. This refines B13's one-variable tradeoff by retaining the exact signed zero mode.

## 4. A clean improvement for zero first-level mass: 1/4 -> 7/40

Now specialize to the current source candidate cap
\[
C_*=6.5218512=\frac{4076157}{625000}.
\]
When `a=0`, (3.2) is B13's scalar
\[
L_C(\delta)=C\delta-1-h_2(\delta)
+h_2\!\left(\frac{1-2\sqrt{\delta(1-\delta)}}2\right).
\tag{4.1}
\]
Writing `x=1-2delta`, B13's `Psi` gives
\[
L_C(\delta)=C\delta-2+\Psi(x).
\tag{4.2}
\]
Hence for `0<delta<1/2`,
\[
L_C'(\delta)=C-2\Psi'(x),
\qquad
L_C''(\delta)=4\Psi''(x)>0.
\tag{4.3}
\]
So `L_C` is strictly convex.

Take
\[
\delta_0=\frac7{40},\qquad x_0=\frac{13}{20},
\qquad v_0^2=1-x_0^2=\frac{231}{400}.
\]
For `0<=z<1`,
\[
\operatorname{artanh}z
\le z+\frac{z^3}{3(1-z^2)}.
\tag{4.4}
\]
Substituting this in the exact derivative formula
\[
\Psi'(x)=\frac{\operatorname{artanh}x+(x/v)\operatorname{artanh}v}{\ln2}
\]
gives at `x_0`
\[
\Psi'(x_0)
\le
\frac{1}{\ln2}
\left(2x_0+\frac{x_0^3}{3v_0^2}+\frac{v_0^2}{3x_0}\right)
=\frac{1}{\ln2}\frac{79039}{45045}.
\tag{4.5}
\]
Since `ln 2 > 2/3`,
\[
2\Psi'(x_0)<3\frac{79039}{45045}
=\frac{79039}{15015}<C_*.
\tag{4.6}
\]
Thus `L'_{C_*}(7/40)>0`; by strict convexity, `L_{C_*}` is increasing from `7/40` through `1/2`.

For the value itself,
\[
y(7/40)=\frac{20-\sqrt{231}}{40}>\frac3{25}
\]
because `231<(76/5)^2`. Binary entropy is increasing on `[0,1/2]`, hence
\[
L_{C_*}(7/40)
>
C_*\frac7{40}-1-h_2(7/40)+h_2(3/25).
\tag{4.7}
\]
The accompanying rational logarithm enclosure certifies
\[
\boxed{
C_*\frac7{40}-1-h_2(7/40)+h_2(3/25)
>0.0016689902308068254.
}
\tag{4.8}
\]
For `delta>=1/2`, the crude bound `h_2(delta)<=1` and nonnegativity of the last entropy term give `L_{C_*}(delta)>=C_*/2-2>0`.

Therefore:

### Corollary 4.1 — sharpened central critical-core exclusion

In every hypothetical minimum-essential-arity **balanced central** counterexample to the current cap-`C_*` all-gate candidate,
\[
\boxed{
\widehat f(\{j\})=0
\quad\Longrightarrow\quad
\operatorname{Inf}_j(f)<\frac7{40}=0.175.
}
\tag{4.9}
\]
This strictly improves the predecessor's `<1/4` exclusion. The numerical zero of `L_{C_*}` is about `0.17403113037837303`; that number is context only, not part of the theorem.

## 5. Decisive finite self-check

`check_b16_refined_joint_credit.py` does two independent things.

* It exhausts every ordered pair of Boolean child functions through three residual variables satisfying the balanced-parent condition `E f1 = -E f0`. There are **12,948** such pairs. It verifies `delta>=a^2` and (2.3) directly from Walsh coefficients. Minimum observed slack is `0`, attained at expected equality cases.
* It certifies (4.8) and (4.6) with exact rational atanh-series enclosures. The rigorous lower bounds are
  `L_7_40 > 0.0016689902308068254` and
  `L'_7_40 > 1.257848535997336`.

The finite census is a self-check; Theorems 2.1 and Corollary 4.1 are analytic and do not depend on finite extrapolation.

## 6. What changed and what remains

**New proved inference.** The arbitrary-child joint-credit theorem can be sharpened on every balanced parent by retaining the forced negative empty Fourier atom before triangle/Jensen. This yields the two-parameter exact necessary condition (3.4) and improves the zero-first-level critical-core influence threshold from `1/4` to `7/40` for the current cap.

**Why this is compatible with the old signed interface.** The proof uses exactly the same non-scalarization principle as the authentic parent-current and signed-flag-curvature theorems: a forced opposite orientation is kept live until after the legitimate cancellation/convexification. No dual-code multiplicity, R16/R32 negative credit, moment refund, terminal payment, or finite-window remainder is claimed as payment here.

**Remaining universal obligation.** Full FEI is open. The strongest current falsification lead is the fleet02/B16 coherent biased `n=18` prime-gate direction; its exact finite remainder check remains unpaid because the authentic current candidate bytes are absent from the authorized scientific folder. On the central critical-core route, (3.4) must be combined with actual properties of `Gamma_*` to eliminate the region `a != 0` and the remaining small-influence region, or a source-valid pivot-coverage theorem must force one paid coordinate.

No benchmark gold, mocks, paid/remote compute, workflow dispatch, email/Drive, unrelated private data, permission change, or notification enabling was used.
