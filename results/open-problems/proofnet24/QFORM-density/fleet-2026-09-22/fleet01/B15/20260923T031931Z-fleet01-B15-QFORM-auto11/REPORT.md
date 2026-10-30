# QFORM B15 — exact compact smooth-kernel regularity normal form

Run: `20260923T031931Z-fleet01-B15-QFORM-auto11`  
Logical worker: `fleet01/B15`  
Status: **ESSENTIAL_STEP_APPLIED / EXACT_COMPACT_SMOOTH_KERNEL_NORMAL_FORM / FULL QFORM OPEN**

## 1. Target and correction discipline

The target is the unrestricted conjecture: for independent real coordinates with densities `0<=f_i<=1` and real symmetric `A` with at least three eigenvalues of modulus at least one, bound the density of `Q=X^T A X` by one universal finite constant. No moments, connected support, smoothness, post-rotation independence, or spectral localization is added.

This report uses no law-uniform pointwise quadratic Fourier decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea bound, and no projection-only/X-ray shortcut. Continuity is not used to infer the central `L^infinity` bound.

## 2. Absolute continuity needs almost nothing

### Proposition 2.1 — nonconstant quadratic pushforwards of absolutely continuous laws are absolutely continuous

Let `q:R^n->R` be a nonconstant quadratic polynomial and let `mu(dx)=F(x)dx` be any absolutely continuous probability law. Then `q_# mu` is absolutely continuous with respect to Lebesgue measure on `R`.

For the target homogeneous form `q(x)=x^T A x`, nonconstancy is automatic because `A` has at least three nonzero eigenvalues.

### Proof

For a nonconstant quadratic polynomial, the critical set

`C={x: grad q(x)=0}`

is an affine subspace of codimension at least one, hence has Lebesgue measure zero. Let `N subset R` have one-dimensional Lebesgue measure zero. For integers `m,k>=1`, put

`E_{m,k}={x in B(0,m): |grad q(x)|>=1/k}`.

The coarea formula applied on `E_{m,k}` to the nonnegative function

`g(x)=1_{q(x) in N}/|grad q(x)|`

gives

`|q^{-1}(N) intersect E_{m,k}| = int_N int_{q^{-1}(t) intersect E_{m,k}} 1/|grad q| dH^{n-1} dt =0.`

Since `R^n\C = union_{m,k} E_{m,k}`, `q^{-1}(N)` is Lebesgue-null. Absolute continuity of `mu` gives `mu(q^{-1}(N))=0`. Therefore `q_#mu<<dt`.

This proves existence of an output density before any boundedness or continuity argument. Independence is not needed for this proposition.

## 3. Sharp spectral normalization

Let `s(A)=s_3(A)` denote the third largest eigenvalue modulus and let `p_{A,f}` denote the a.e.-defined density from Proposition 2.1. Define the extended sharp target constant

`C_* = sup_{target instances} ||p_{A,f}||_infinity in [0,infinity].`

For `c>0`,

`p_{cA,f}(t)=c^{-1} p_{A,f}(t/c)`.

Consequently, normalizing `B=A/s(A)` gives `s_3(B)=1` and

`||p_{A,f}||_infinity = s(A)^{-1} ||p_{B,f}||_infinity.`

Hence, in the extended sense,

`C_* = sup_{s_3(A)=1,f} ||p_{A,f}||_infinity
     = sup_{target instances} s(A)||p_{A,f}||_infinity.`

This identity is only homogeneity; it does not assume `C_*<infinity`.

## 4. Exact kernel-invariance theorem — continuity is unnecessary

Fix any nonnegative compactly supported `K in L^1(R)` with

`int_R K(u)du=1`.

For a target instance define

`H_K(A,f;y)=E K(y-X^T A X).`

### Theorem 4.1 — exact fixed-kernel normal form

For every fixed `R>0`,

`C_* = sup_{target instances, |y|>=R} s(A) H_K(A,f;y).`

This remains true if `C_*=infinity`. No continuity or boundedness of the individual raw output density is assumed in the proof.

### Proof: upper bound

Since the output law has density `p`,

`H_K(y)=int K(y-u)p(u)du <= ||p||_infinity int K = ||p||_infinity.`

Therefore

`s(A)H_K(y) <= s(A)||p||_infinity <= C_*.`

### Proof: reverse bound by Lebesgue differentiation

Fix one target instance, write `s=s(A)`, `Q=X^TAX`, and let `p` be its density. Let `M<s||p||_infinity` be finite. The set

`{t: s p(t)>M}`

has positive measure, so it contains a nonzero Lebesgue point `t` of `p`.

For `a>1`, replace `A` by `A_a=aA`. This is still a target matrix, with `s(A_a)=as`, and its output is `aQ`. Evaluate at `y_a=at`:

`(as) E K(at-aQ)
 = as int K(a(t-u))p(u)du
 = s int K(v) p(t-v/a)dv.`

The family `aK(a .)` is an approximate identity. At the chosen Lebesgue point,

`s int K(v)p(t-v/a)dv -> s p(t)`.

For all sufficiently large `a`, `|at|>=R`. Thus the right-hand supremum is at least `M`. Let `M` increase to `s||p||_infinity`, then take the supremum over target instances.

If `C_*=infinity`, the same argument is applied for arbitrary finite `M`; no bounded-density premise has been smuggled in.

### Consequence

The earlier critical-gap/tent reduction can be made logically stronger: the exact sharp constant can be recovered from one fixed positive kernel using only **absolute continuity plus Lebesgue differentiation**. A `C_0` representative is not needed for the central reduction.

## 5. Choose one compact `C^infinity` kernel

Let

`kappa(u)=c_0 exp(-1/(1-u^2)) 1_{|u|<1}`

with `c_0` chosen so `int kappa=1`. Then Theorem 4.1 gives, for example at `R=2`,

`boxed: C_* = sup_{target, |y|>=2} s_3(A) E kappa(y-X^TAX).`

This is an exact reformulation of the full universal density conjecture.

Because `supp kappa subset (-1,1)`, every contributing point obeys

`|X^TAX| >= |y|-|y-X^TAX| > 1`

when `|y|>=2`. For the homogeneous quadratic map `q(x)=x^TAx`, every critical point satisfies `Ax=0` and hence has critical value `q(x)=0`. Thus the exact normal form can be placed a fixed distance from the only critical output value. This removes the cone vertex from the *output window* but does not by itself control product-law mass along the remaining regular level surface.

## 6. Uniform regularity after one fixed compact smoothing

For every target instance,

`H_kappa(y)=E kappa(y-Q)`

is `C^infinity`, and differentiation under the probability integral gives

`H_kappa^(m)(y)=E kappa^(m)(y-Q)`

for every `m>=0`. Hence

`boxed: ||H_kappa^(m)||_infinity <= ||kappa^(m)||_infinity,  m>=0,`

uniformly in dimension, matrix, and source laws.

This is a genuine target-level regularity statement, but the scale-correct quantity in the exact theorem is `s_3(A)H_kappa`, whose derivatives carry the same prefactor. I do **not** claim a uniform raw-output continuity modulus, BV bound, Besov bound, or desmoothing estimate; live source-valid counterexamples forbid those stronger assertions.

The logical separation is now:

1. absolute continuity — automatic for every nonconstant quadratic pushforward of an absolutely continuous joint law;
2. universal bounded density — exactly the finite bound for the compact smooth kernel functional above;
3. continuity of the raw density — an additional property and unnecessary for the equality in Theorem 4.1.

## 7. Exact extreme-source reduction for the smooth kernel functional

Fix `A,y` and the nonnegative bounded payoff

`G(x)=kappa(y-x^T A x)`.

For one coordinate, holding the other marginals fixed, the functional is

`int h_i(u) f_i(u)du`,

where `0<=h_i<=||kappa||_infinity`. The bathtub principle gives

`sup_{0<=f_i<=1, int f_i=1} int h_i f_i
 = sup_{E_i measurable, |E_i|=1} int_{E_i} h_i.`

Iterating this equality through the finitely many coordinates yields

`sup_{product cap-one densities} E G(X)
 = sup_{|E_1|=...=|E_n|=1} int_{E_1 x ... x E_n} G(x)dx.`

No independence after rotation is involved: the reduction is performed in the original physical coordinates.

Every finite-measure measurable `E_i` can be approximated in symmetric difference by a bounded finite union of intervals of the same total measure one. Since `G` is bounded,

`|int_{prod E_i}G-int_{prod F_i}G|
 <= ||kappa||_infinity sum_i |E_i triangle F_i|.`

Therefore the sharp constant admits the exact geometric formulation

`boxed:
C_* = sup s_3(A) int_{E_1 x ... x E_n}
             kappa(y-x^T A x) dx,`

where the supremum is over target matrices, `|y|>=2`, and **bounded finite unions of intervals** `E_i` with `|E_i|=1`.

The number of components and their mutual separations are not bounded. This explicitly respects the live `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1` correction.

## 8. Completed fleet02/B15 result applied to the new normal form

I independently rechecked the completed fleet02/B15 physical definite-pair theorem from

`yspennstate/math-open-problems@159482a9594e177145fa61c337bf16e1f9fefc55`

(`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T212015Z-fleet02-B15-qform-r18/REPORT.md`).

If an ORIGINAL-coordinate `2x2` principal block `B` is positive or negative definite, conditioning on all other original coordinates and completing the physical square gives

`||p_Q||_infinity <= pi/sqrt(|det B|).`

Applying this completed partner theorem to the actual compact-kernel inequality gives

`boxed:
s_3(A) E kappa(y-Q)
 <= pi s_3(A)/sqrt(|det B|).`

In particular, if

`|det B| >= eta s_3(A)^2`,

then this entire branch is paid by

`boxed: s_3(A) E kappa(y-Q) <= pi/sqrt(eta).`

Thus the kernel normal form interfaces directly with a proved physical-coordinate branch: the unresolved geometry may be restricted to matrices for which no definite physical pair supplies such a scale-comparable determinant, together with the already-known diffuse/bank/cross alternatives. This application uses original-coordinate conditioning and does not transfer independence to eigen-coordinates.

The newest fleet02/B15 handoff (`20260923T030440Z-fleet02-B15-QFORM-auto11`) was also read. Its rough-source stability and ambient one-sheet statements are compatible with the present normal form; they are not needed as premises for Theorem 4.1.

## 9. First unpaid implication

The full conjecture is now **exactly equivalent** to the following one positive, fixed-scale, smooth, full-dimensional inequality:

`sup_{n,A,y,E_i}
 s_3(A) int_{E_1 x ... x E_n}
 kappa(y-x^T A x) dx < infinity,`

subject only to

- `s_3(A)>=1`;
- `|y|>=2`;
- each `E_i` is a bounded finite union of intervals of total length one;
- no uniform bound on the number, diameter, or separation of components.

On the support of the integrand, `|x^TAx|>1`, so this fixed-scale inequality is separated from the quadratic critical value. The remaining difficulty is not regularity: it is a dimension-free estimate that retains original-coordinate product geometry while aggregating diffuse physical curvature before reciprocal local-minor payment.

## 10. Status

This report proves a target-level exact reduction and a qualitative absolute-continuity theorem. It does **not** prove the universal finite constant. Full QFORM remains OPEN.

Execution context: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write is durable transport, not native learned-memory ingestion.
