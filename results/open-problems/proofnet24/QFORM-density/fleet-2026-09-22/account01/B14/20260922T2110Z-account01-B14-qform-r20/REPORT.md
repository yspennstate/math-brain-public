SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-22T21:10:00Z.
attacking: exact small-ball localization at the OPTIMAL CONSTANT level, including arbitrary affine/translation terms, then apply account02/B14's whole-bank theorem without fragment normalization.

# account01/B14 — exact optimal-constant localization compiler

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** 20260922T2110Z-account01-B14-qform-r20  
**Status:** ESSENTIAL_STEP_APPLIED / SUPPORTING LOCALIZATION THEOREM; full QFORM remains OPEN.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## 1. Source pins and corrections used

Coherent startup control: `yspennstate/math-research-brain@81635b9ae89574a6eabae5438d5231c59e90310e`; OWNER CONTROL observed there is revision `2026-09-22.15` (the programme identifier remains QFORM-DENSITY-3EIG-20260922, historical activation revision 2026-09-22.5). A pre-write refresh at `38db4836685c548a734ddd2750a1ad3472e4db83` still keeps QFORM exclusive and contains no later stop.

Assigned partner actually consumed: account02/B14 run `20260922T195844Z-account02-B14-QFORM-r20`, canonical mathematics `yspennstate/math-open-problems@0e2e038577460d99f7ddc10fbf87fdd5cf76a930:proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T195844Z-account02-B14-QFORM-r20/REPORT.md`. Its exact theorem used below is the disjoint-bank compression bound

\[
\|p_Q\|_\infty\le 32e\sqrt{10}\,|\det M|^{-1/3}
\tag{1.1}
\]

under the exact bank factorization `A_SS=UMU^T`, `A_SR=UC`, with arbitrary outside self block and arbitrary cap-one independent inputs. Its key localization warning is also used: fragmentwise normalization before reciprocal determinant payment creates an artificial scale tax, so whole unit-mass laws/banks must be retained.

Corrections respected: no bounded support-diameter reduction; no universal bounded fragment count; no post-rotation independence; no arbitrary-joint coarea; no positive conditional projection-density moment; no law-uniform pointwise quadratic Fourier decay; no one-small-minor extraction.

## 2. Exact localization theorem at the optimal constant level

Let

\[
\mathcal D:=\{f:\mathbb R\to[0,1]\text{ measurable}:\int f=1\}.
\]

Let `E` be the class of measurable sets of Lebesgue measure one and `E_fin` the subclass of bounded finite unions of intervals of total length one.

For bounded measurable `0<=Phi<=1` on `R^n`, define

\[
\mathfrak S(\Phi):=
\sup_{f_1,\dots,f_n\in\mathcal D}
\int_{\mathbb R^n}\Phi(x)\prod_i f_i(x_i)\,dx.
\]

### Theorem — `QFORM-EXACT-OPTIMAL-CONSTANT-LOCALIZATION-v2`

For every bounded measurable `0<=Phi<=1`,

\[
\boxed{
\mathfrak S(\Phi)
=
\sup_{E_1,\dots,E_n\in\mathcal E}
\int_{E_1\times\cdots\times E_n}\Phi(x)\,dx
=
\sup_{E_1,\dots,E_n\in\mathcal E_{\rm fin}}
\int_{E_1\times\cdots\times E_n}\Phi(x)\,dx.
}
\tag{2.1}
\]

The equality is exact: there is no support-radius, fragment-count, component-separation, moment, centering, or translation factor.

### Proof, first equality

Fix all densities except `f_i` and set

\[
g_i(t)=\int \Phi(x_1,\ldots,t,\ldots,x_n)
\prod_{j\ne i}f_j(x_j)\,dx_{-i}.
\]

Then `0<=g_i<=1` and the objective is the linear functional `int g_i f_i`. The cap-one bathtub principle gives

\[
\sup_{0\le f\le1,\ \int f=1}\int gf
=
\sup_{|E|=1}\int_E g.
\tag{2.2}
\]

Indeed choose a level `a` so that `{g>a}` has measure at most one and `{g>=a}` has measure at least one; nonatomicity of Lebesgue measure supplies a subset of `{g=a}` that fills the remaining mass. Its indicator is an optimizer (or an arbitrarily close optimizer in the degenerate infinite-level case).

Replace `f_1` by such an indicator without decreasing the objective, then `f_2`, and so on. After finitely many steps all marginals are indicators of unit-measure sets. This proves the first equality in (2.1).

### Proof, finite-union equality

Fix unit-measure measurable `E`. By regularity of Lebesgue measure, for every epsilon>0 there is a bounded finite union of intervals `F_0` with `|E triangle F_0|<epsilon` and `||F_0|-1|<epsilon`. Trim one interval if `|F_0|>1`, or add a disjoint interval of the missing length if `|F_0|<1`; call the resulting finite union `F`. Then `|F|=1` and `|E triangle F|<2epsilon`.

For product rectangles `R=prod E_i`, `R'=prod F_i` with every factor of measure one,

\[
|R\triangle R'|\le\sum_i |E_i\triangle F_i|.
\tag{2.3}
\]

Since `0<=Phi<=1`, the two integrals differ by at most the right side of (2.3). Letting all errors tend to zero proves the second equality in (2.1). QED.

## 3. Exact reduction of the FULL QFORM constant

For a real quadratic-affine polynomial

\[
q(x)=x^TAx+b^Tx+c
\]

and a bounded interval `J`, apply Theorem 2 with `Phi=1_{q in J}`. Define the optimal small-ball coefficient

\[
K(A,b,c)
:=\sup_{J:\ |J|>0}\frac1{|J|}
\sup_{f_i\in\mathcal D}
\Pr\{q(X)\in J\}.
\tag{3.1}
\]

Then

\[
\boxed{
K(A,b,c)
=
\sup_{J:\ |J|>0}\frac1{|J|}
\sup_{E_i\in\mathcal E_{\rm fin}}
\int_{\prod E_i}{\bf1}_{\{q(x)\in J\}}\,dx.
}
\tag{3.2}
\]

Thus the optimal universal constant in the original QFORM conjecture is EXACTLY the same if every one-dimensional input law is restricted to a uniform law on an arbitrary bounded finite union of intervals of total length one. The number of intervals and total diameter are allowed to depend on the approximation and are not uniformly bounded.

If the right side of (3.2) is <=C for all target matrices A, then every arbitrary cap-one product law satisfies `mu_Q(J)<=C|J|` for every interval J. Hence `mu_Q<<Leb` and its Radon--Nikodym density satisfies `||p_Q||_infty<=C`: first extend the interval bound to open sets by disjoint interval decomposition, then to all null sets by outer regularity. Conversely an `L^infinity` density bound implies the interval bound with the same constant. Therefore (3.2) preserves not merely a supporting estimate but the exact target constant.

Arbitrary coordinate translations are already included: translating an `E_i` preserves unit measure and finite-union status, while a coordinate translation of q only changes `(b,c)`. No moment or support-location quantity is introduced.

## 4. Conditional/mixture compiler

The same argument gives a useful conditional version. Suppose an outside variable Z is arbitrary and, for every deterministic z, every finite-union indicator law on the active original coordinates satisfies

\[
\Pr\{q_z(X)\in J\}\le C|J|
\tag{4.1}
\]

with the SAME C. Then Theorem 2 upgrades (4.1) to every cap-one product law on the active coordinates, still pointwise in z; averaging over Z yields the same unconditional C. Thus conditioning on outside original coordinates, completing squares, and introducing arbitrarily large z-dependent affine shifts incurs zero localization loss whenever the conditional theorem is shift-uniform.

This is precisely the safe order required by the current correction set: condition outside, keep whole active marginals, apply a shift-uniform theorem, then average. Do not split/normalize fragments before applying a reciprocal curvature estimate.

## 5. Actual application of the assigned partner theorem

Take the partner's exact disjoint-bank class

\[
A_{S,S}=UMU^T,\qquad A_{S,R}=UC,
\]

with three disjoint original-coordinate banks and nonsingular symmetric 3x3 M. For every outside realization `X_R=z`, the partner theorem reduces the conditional form to a three-bank quadratic plus an arbitrary affine term and proves the uniform bound (1.1).

Applying the compiler in Section 4 gives, for EVERY choice of arbitrarily translated, arbitrarily fragmented, unbounded-support cap-one input laws,

\[
\boxed{
K(A,0,0)\le32e\sqrt{10}\,|\det M|^{-1/3}.
}
\tag{5.1}
\]

No extra sum over fragments or normalized-component cap appears. In particular, if `|det M|>=1`, the whole class has the universal small-ball/density constant `32e sqrt(10)` under exact localization.

Using the sharper Ball--Rogozin scalar bank cap `||p_{u^T X}||_infty<=sqrt(2)` already source-pinned in account01/B14 r19, the identical determinant rescaling improves the numerical coefficient in this same partner class to

\[
\boxed{K(A,0,0)\le64\sqrt{10}\,|\det M|^{-1/3}.}
\tag{5.2}
\]

The mathematical point of this run is not the coefficient improvement; it is that (3.2) proves the localization step itself is EXACT at the final universal-constant level and therefore can never be blamed for support tails, translations, or arbitrarily many distant components.

## 6. What remains unpaid

The full conjecture is still open. Exact law localization is no longer the missing step. The missing implication is matrix-structural: from the bare spectral condition `s_3(A)>=1`, obtain a product-preserving grouped/ridge/cross-block branch to which one of the existing shift-uniform density theorems applies, without selecting and reciprocating one tiny physical minor and without normalizing fragments.

The current partner obstruction and account01/B14 r19 rainbow theorem show why this must be aggregate-before-inversion: the exterior-volume mass can be spread over many tiny physical packets while a whole-bank representation is uniformly payable.

**Classification:** ESSENTIAL_STEP_APPLIED / SUPPORTING_LOCALIZATION_THEOREM / FULL_QFORM_OPEN.
