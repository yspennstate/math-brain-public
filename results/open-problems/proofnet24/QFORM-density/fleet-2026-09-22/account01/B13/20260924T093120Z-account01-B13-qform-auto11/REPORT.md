SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-24T09:31:20.716020Z.
attacking: exact finite-certificate purification from arbitrary cap-one product laws to product indicators, followed by a geometric trimmed-width inequality using the completed account02/B13 rough-law obstruction.

# account01/B13 — exact product purification and trimmed quantile geometry

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T093120Z-account01-B13-qform-auto11`  
Owner control consumed: revision `2026-09-22.15` and continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Model self-report: `GPT-5.6 Sol`; configured reasoning effort `UNKNOWN`; provider reasoning telemetry `null / not exposed`.

**Status.** The full unrestricted QFORM theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains a separate stronger conclusion. No rotated independence, uniform pointwise quadratic oscillatory decay, arbitrary-joint coarea bound, or projection-density-only closure is used below.

## 1. New theorem: exact finite-certificate purification on the whole line

The previous reduction in this slot oscillated between an optimizer-free approximation and a one-functional bathtub argument whose noncompact attainment justification required care. The following theorem is stronger and avoids both issues.

### Theorem 1 — `QFORM-GLOBAL-FINITE-CERTIFICATE-PRODUCT-PURIFICATION-v1`

Let `f_i:R->[0,1]` be probability densities, `int f_i=1`, for `i=1,...,n`. Let

`Phi_1,...,Phi_m : R^n -> R`

be any finite family of bounded measurable functions. Then there exist measurable sets `E_i subset R` with

`|E_i|=1`

such that, simultaneously for every `r=1,...,m`,

\[
\boxed{
\int_{\mathbb R^n}\Phi_r(x)\prod_{i=1}^n1_{E_i}(x_i)\,dx
=
\int_{\mathbb R^n}\Phi_r(x)\prod_{i=1}^nf_i(x_i)\,dx .
}
\tag{1.1}
\]

Thus any finite vector of bounded statistics of an arbitrary cap-one product law can be realized **exactly** by a product of unit-measure indicator densities. There is no compact-support assumption and no optimization or attainment hypothesis.

### Proof: one-dimensional simultaneous purification

It is enough first to prove the following one-dimensional lemma.

Let `0<=f<=1`, `int_R f=1`, and let `h_1,...,h_m` be bounded measurable real functions. Then there exists measurable `E subset R`, `|E|=1`, such that

\[
\int_E h_r(t)\,dt=\int_{\mathbb R}f(t)h_r(t)\,dt,
\qquad r=1,...,m.
\tag{1.2}
\]

Partition the line into the unit cells

\[
C_k=[k,k+1),\qquad k\in\mathbb Z.
\]

On each cell define the finite atomless vector measure

\[
\nu_k(A)=\int_A G(t)\,dt,
\qquad
G(t)=(1,h_1(t),...,h_m(t))\in\mathbb R^{m+1}.
\tag{1.3}
\]

By Lyapunov's convexity theorem, the range

\[
\mathcal R_k=\{\nu_k(A): A\subseteq C_k\text{ measurable}\}
\]

is a compact convex subset of `R^{m+1}`. Put

\[
v_k=\int_{C_k}f(t)G(t)\,dt.
\]

Using the exact layer-cake identity

\[
f(t)=\int_0^1 1_{\{f(t)>s\}}\,ds,
\]

we obtain

\[
v_k
=
\int_0^1
\nu_k\bigl(C_k\cap\{f>s\}\bigr)\,ds.
\tag{1.4}
\]

The right side is a barycenter of points of the compact convex set `R_k`, hence belongs to `R_k`. Therefore there is a measurable `E_k subseteq C_k` with

\[
\nu_k(E_k)=v_k.
\tag{1.5}
\]

Let

\[
E=\bigcup_{k\in\mathbb Z}E_k.
\]

The first coordinate of (1.5) gives

\[
|E|=\sum_k|E_k|=\sum_k\int_{C_k}f=1.
\]

For each bounded `h_r`, the series of cell integrals is absolutely summable because

\[
\sum_k\int_{E_k}|h_r|
\le \|h_r\|_\infty\sum_k|E_k|
=\|h_r\|_\infty,
\]

and similarly on the `f` side. Summing the corresponding coordinates of (1.5) over `k` proves (1.2).

### Product iteration

Now start with the product marginals `g_i=f_i`. At coordinate `i`, keeping all other current marginals fixed, define for each certificate

\[
h_{i,r}(t)=
\int_{\mathbb R^{n-1}}
\Phi_r(x_1,...,x_{i-1},t,x_{i+1},...,x_n)
\prod_{j\ne i}g_j(x_j)\,dx_{-i}.
\tag{1.6}
\]

Every current `g_j` has mass one (it is either an original density or a previously purified indicator), so

\[
|h_{i,r}(t)|\le\|\Phi_r\|_\infty.
\]

Apply the one-dimensional lemma to the finite family `h_{i,1},...,h_{i,m}` and the current `g_i`; replace `g_i` by `1_{E_i}`. Equations (1.2) and (1.6) show that **every** certificate integral is unchanged. Repeating through `i=1,...,n` yields (1.1). `QED`

### Consequence: equality of finite certificate ranges

For every finite bounded certificate family `Phi=(Phi_1,...,Phi_m)`, the set of vectors

\[
\left\{
\left(\int \Phi_r\prod_i f_i\right)_{r=1}^m:
0\le f_i\le1,\ \int f_i=1
\right\}
\]

is exactly the same as the set obtained by restricting every marginal to `1_{E_i}` with `|E_i|=1`. The reverse inclusion is immediate because indicator densities are admissible.

This is stronger than equality of suprema and stronger than preserving only one objective.

## 2. Exact equivalence with a geometric product-set small-ball problem

Apply Theorem 1 with the single bounded certificate

\[
\Phi(x)=1_{\{x^TAx\in J\}}
\]

for a fixed symmetric `A` and fixed interval `J`. For every cap-one product law there is a unit-measure product set

\[
E=E_1\times\cdots\times E_n,
\qquad |E_i|=1,
\]

with **exactly the same** slab probability:

\[
\boxed{
\Pr\{X^TAX\in J\}
=
\left|\{x\in E:x^TAx\in J\}\right|.
}
\tag{2.1}
\]

Hence the original target small-ball inequality is equivalent, with no loss and for the same `A,J`, to the geometric statement

\[
\boxed{
\left|\{x\in\prod_iE_i:x^TAx\in J\}\right|
\le C|J|
\quad
\text{for all measurable }|E_i|=1.
}
\tag{2.2}
\]

One direction follows from (2.1); the other follows because indicator densities themselves are allowed. If (2.2) holds for all intervals, then the pushforward measure is absolutely continuous with Radon–Nikodym derivative at most `C` almost everywhere (equivalently use Lebesgue differentiation after the interval domination). Thus the assignment's extremal-law reduction is exact at the essential-bounded-density level.

No claim is made that any `E_i` is an interval, centered, bounded, connected, or has a uniformly bounded number of components. This is consistent with the live fragment-count and diameter corrections.

## 3. Multiple slab certificates and exact geometric provenance

The simultaneous form matters. For example, given finitely many intervals `J_1,...,J_m`, one may take

\[
\Phi_r(x)=1_{\{x^TAx\in J_r\}}
\]

and preserve all `m` slab probabilities in one product-indicator law. For bounded-support observables one may likewise preserve finitely many conditional-moment numerators together with the slab mass. This does **not** assert preservation of unbounded moments without an integrability/truncation step; the theorem is deliberately stated for bounded certificates.

In particular, any finite collection of tests used by a proposed counterexample search can be purified without changing their values. This prevents a proof from gaining an advantage merely by replacing arbitrary cap-one marginals by convex mixtures unless it also uses genuinely infinite-dimensional information.

## 4. Compact self-consistent near-extremizers

The exact global purification does not say that a global maximizing product set exists. For geometric work one can nevertheless obtain compact self-consistent near-extremizers.

### Proposition 4.1 — `QFORM-COMPACT-SELFCONSISTENT-BATHTUB-v1`

Let `B_i subset R` be bounded intervals with `|B_i|>=1`, and let `K` be bounded measurable on `B=prod_i B_i`. Then

\[
\sup_{\substack{0\le f_i\le1,\ \int_{B_i}f_i=1}}
\int_B K(x)\prod_i f_i(x_i)\,dx
\]

is attained by a product indicator `prod_i1_{E_i}`, `E_i subset B_i`, `|E_i|=1`. Every maximizing product set is coordinatewise self-consistent: for

\[
h_i(t)=\int K(t,x_{-i})\prod_{j\ne i}1_{E_j}(x_j)\,dx_{-i},
\tag{4.1}
\]

there is a threshold `tau_i` such that, up to null sets,

\[
\boxed{
\{h_i>\tau_i\}\subseteq E_i\subseteq\{h_i\ge\tau_i\}.
}
\tag{4.2}
\]

#### Proof

Each feasible one-coordinate set is weak-star compact in `L^infty(B_i)`, and the finite product of these compact sets is compact. Joint continuity of the multilinear objective follows first for finite sums of rectangle tensors, for which the integral is a finite sum of products of weak-star continuous linear functionals; a general bounded measurable `K` is approximated in `L^1(B)` by such simple functions, and

\[
\left|\int_B(K-S)\prod_i f_i\right|\le\|K-S\|_{L^1(B)}
\]

uniformly over the feasible set. Therefore a maximizing tuple exists. Applying the finite-space version of Theorem 1 to its single objective yields an indicator maximizer. Holding all other sets fixed, `E_i` must maximize `int_{E_i}h_i` over all unit-measure subsets of `B_i`; the standard bathtub exchange argument gives (4.2). `QED`

For an arbitrary unit product set witness, truncate each `E_i` inside a sufficiently large bounded interval, fill the missing measure inside that interval, and use the telescoping estimate for product indicators to make the slab-mass loss arbitrarily small. Maximizing inside those boxes then produces bounded, possibly highly fragmented near-witnesses satisfying all coordinate threshold equations (4.2). There remains no uniform diameter or fragment-count conclusion.

This gives a concrete structural target for the geometric inequality: a hypothetical sequence with slab ratio tending to infinity may be assumed, up to arbitrary small loss, to consist of compact product sets in which every coordinate set is a best response to the exact slab fiber score.

## 5. Designated partner applied: intrinsic trimmed-quantile profile

The newest completed designated partner `account02/B13` report used here is

`math-open-problems@8645efc6fb96cefa195328f92caae05dbadb168b`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260924T084755Z-account02-B13-QFORM-r11/REPORT.md`.

Its theorem `QFORM-SLAB-MASS-TRIMMED-DIAMETER-ESCAPE-v1` states: if

\[
A=M+F
\]

and every translated affine `M`-form has density at most `C_M`, then a slab of length `ell`, mass `p=rho ell`, and ratio `rho>=4C_M` forces, for every physical-coordinate interval family `I_i=[m_i-h_i,m_i+h_i]` with

\[
\sum_i\Pr\{X_i\notin I_i\}\le p/2,
\]

the retained rough quadratic width

\[
\sup_{|y_i|\le h_i}|y^TFy|
\ge {p\over8C_M}.
\tag{5.1}
\]

I now apply this theorem to the exact product-indicator representation (2.1), converting it into a purely geometric sublevel-set constraint.

For a unit set `E_i` and `0<=eta<1`, define the open-budget concentration radius

\[
r_i(\eta)=
\inf\left\{
 h\ge0:
 \exists m\in\mathbb R,
 \ |E_i\cap[m-h,m+h]|>1-\eta
\right\}.
\tag{5.2}
\]

(The strict `>` is intentional: it lets any allocation with `sum eta_i<p/2` feed directly into the partner theorem without a boundary-attainment issue.)

### Corollary 5.2 — `QFORM-TRIMMED-QUANTILE-PROFILE-v1`

In the partner's current rank-one-plus-four-diagonal rough normal form

\[
A=D_C+\lambda_1vv^T+E_{\rm sep}+\lambda_2ww^T,
\qquad |C|\le4,
\tag{5.3}
\]

with

\[
\|E_{\rm sep}\|_{op}\le {C_D\over\rho},
\qquad C_D=2\sqrt{30\pi},
\tag{5.4}
\]

and affine-core cap

\[
C_M=500e\,5(8+\log5),
\tag{5.5}
\]

let a unit product set `E=prod_iE_i` satisfy

\[
S_E=\{x\in E:x^TAx\in J\},
\qquad
p=|S_E|=\rho|J|,
\qquad \rho\ge4C_M.
\tag{5.6}
\]

Then for **every** choice `eta_i>=0` with

\[
\sum_i\eta_i<p/2,
\tag{5.7}
\]

its concentration radii obey

\[
\boxed{
C_D\sum_{i\notin C}r_i(\eta_i)^2
+
\rho|\lambda_2|
\left(\sum_i|w_i|r_i(\eta_i)\right)^2
\ge
{\rho p\over8C_M}.
}
\tag{5.8}
\]

#### Proof

For each `i` choose an interval centered at some `m_i` with half-width

\[
h_i<r_i(\eta_i)+\varepsilon
\]

and

\[
|E_i\cap[m_i-h_i,m_i+h_i]|>1-\eta_i.
\]

Under the uniform law on `E_i`, the omitted marginal probability is `<eta_i`; therefore the total omitted probability is `<p/2`. The partner theorem applies. Its exact bound for (5.3) is

\[
C_D H_{\rm tail}^2
+
\rho|\lambda_2|W_w^2
\ge {\rho^2|J|\over8C_M}
={\rho p\over8C_M},
\tag{5.9}
\]

where

\[
H_{\rm tail}^2=\sum_{i\notin C}h_i^2,
\qquad
W_w=\sum_i|w_i|h_i.
\]

Let `epsilon downarrow0`; (5.8) follows. `QED`

Thus a high-ratio geometric witness is not allowed to hide all of its required roughness in support fragments carrying negligible coordinate mass. Even after granting a **total deletion budget comparable to half of the actual bad-slab mass**, every surviving product-box profile must pay (5.8).

### Ultra-collapse fork

If the partner's ultra-collapse branch holds,

\[
|\lambda_2|\le L_0\rho^{-2},
\qquad L_0=\sqrt{3072e^2},
\tag{5.10}
\]

then for every allocation (5.7), at least one of

\[
\boxed{
\sum_{i\notin C}r_i(\eta_i)^2
\ge
{\rho p\over16C_MC_D}
}
\tag{5.11}
\]

or

\[
\boxed{
\left(\sum_i|w_i|r_i(\eta_i)\right)^2
\ge
{\rho^2p\over16C_ML_0}
}
\tag{5.12}
\]

must hold. This follows by splitting the two nonnegative terms in (5.8) at half the right side and using `rho|lambda_2|<=L_0/rho`.

The statement is in original independent physical coordinates throughout. No latent rotation is applied to the random vector.

## 6. What this does and does not close

The exact finite-certificate purification completes the extremal-product reduction itself: arbitrary cap-one product laws and unit-measure product indicators have exactly the same finite bounded-statistic range, and in particular exactly the same attainable one-slab probabilities for fixed `A,J`.

The partner application further shows that in the present rough normal form every exact product-set witness must satisfy the trimmed quantile profile (5.8), with the stronger ultra-collapse fork (5.11)–(5.12). Combined with Proposition 4.1, any compact near-extremal witness can additionally be taken coordinatewise self-consistent with the slab fiber score.

What remains unpaid is the receiver that converts this **self-consistent, mass-trimmed spread** into a dimension-free slab bound while retaining both the `O(rho^-1)` separable diagonal tail and the secondary rank-one carrier inside the phase. Coefficient-small quadratic terms cannot be deleted because supports may be remote and fragmented.

The first unpaid implication after this run is therefore

`QFORM-THRESHOLD-PROFILE-TO-ROUGH-RECEIVER-v1`:

> In the partner normal form (5.3), rule out arbitrarily large slab ratio for compact product sets satisfying the coordinatewise threshold equations (4.2) and the all-budget trimmed profile (5.8), without replacing arbitrary fragmented sets by intervals and without discarding `E_sep` or `lambda_2 ww^T` as a small random perturbation.

A genuine counterexample would instead have to realize these constraints simultaneously with the other live matrix obstructions (including the every-cut D5 collapse), so this is strictly narrower than the unconstrained product-set problem. Full QFORM remains OPEN.

## 7. Source integrity / correction scope

Fresh controls and live corrections were read before this write. The argument uses only original-coordinate product structure. It does not use the refuted arbitrary-joint rank-three coarea cap, post-rotation independence, uniform pointwise quadratic oscillatory decay, projection-density-only closure, bounded-diameter localization, or a universal fixed fragment count. The newly merged hub-star mixed-norm correction is also respected: no absoluteized `|t|^{-1/2}||G_t||_2` integral appears here.

The designated partner dependency was read from its canonical math report, not only its summary handoff. All claims above are scoped as supporting theorems; none is labeled a full proof of the unrestricted conjecture.
