# QFORM B15 — absolute continuity is unconditional; continuity needs product-structure smoothing

**Programme:** QFORM-DENSITY-3EIG-20260922, owner revision 2026-09-22.5  
**Worker:** fleet03/B15  
**Run:** 20260922T142847Z-fleet03-B15-r11  
**Status:** ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target and separation of regularity questions

Let `X=(X_1,...,X_n)` have independent real coordinates, each with a probability density `0<=f_i<=1`, and let `A` be real symmetric with at least three eigenvalues of modulus at least one. Put

`Q(X)=X^T A X`.

The programme asks separately for:

1. absolute continuity of the law of `Q`;
2. a universal dimension-independent essential bound `||p_Q||_infinity<=C`;
3. the stronger existence of a continuous representative of the density.

This report proves (1) in greater generality, records the exact measure-theoretic equivalence for (2), applies the completed fleet04/B15 continuity theorem to an actual interval inequality, and proves that (3) cannot be obtained from rank-three curvature plus a joint `L^infinity` cap alone. Thus any full continuity proof must use the original product/independence structure (or an equivalent stronger input), not merely coarea geometry.

## 2. Universal absolute-continuity theorem

### Theorem A (nonzero quadratic pushforward is absolutely continuous)

Let `Y` be any `R^n`-valued random vector whose law is absolutely continuous with respect to Lebesgue measure; independence and a density cap are not needed. Let `A` be a nonzero real symmetric matrix and `q(x)=x^T A x`. Then the law of `q(Y)` is absolutely continuous on `R`.

In particular every target QFORM instance has an absolutely continuous law, because the three-large-eigenvalue assumption implies `A!=0` and the product input law has a joint density.

### Proof

The gradient is

`nabla q(x)=2Ax`.

Its critical set is `K=ker(A)`. Since `A!=0`, `K` is a proper linear subspace and hence has `n`-dimensional Lebesgue measure zero.

Let `N subset R` be a Lebesgue-null Borel set. For integers `m,R>=1` define

`E_{m,R}={x: |x|<=R, |2Ax|>=1/m}`.

The coarea formula applied to the locally Lipschitz map `q:R^n->R` gives

`int_{E_{m,R} cap q^{-1}(N)} |nabla q(x)| dx
 = int_N H^{n-1}(E_{m,R} cap q^{-1}(y)) dy =0`.

On `E_{m,R}`, `|nabla q|>=1/m`; therefore

`Leb_n(E_{m,R} cap q^{-1}(N))=0`.

Moreover

`R^n \ K = union_{m,R>=1} E_{m,R}`.

Hence `q^{-1}(N)` is contained, up to a null set, in the countable union of the above null sets plus `K`; consequently `Leb_n(q^{-1}(N))=0`. Since `Y` has an absolutely continuous law,

`P(q(Y) in N)=0`.

Thus `q(Y)<<Leb_1`. QED.

### Coarea representative

If `g` denotes the joint density of `Y`, then the same coarea argument yields, for almost every `y`, the density representative

`p_q(y)=int_{q^{-1}(y)\K} g(x)/|2Ax| dH^{n-1}(x)`.

The critical set contributes no mass. This formula establishes existence, not a universal pointwise height bound and not continuity.

## 3. Exact bounded-density implication

For any finite Borel measure `mu` on `R` and constant `C<infinity`, the following are equivalent:

- `mu(I)<=C|I|` for every bounded interval `I`;
- `mu<<Leb` and its Radon--Nikodym derivative satisfies `||dmu/dy||_infinity<=C`.

The reverse direction is immediate. For the forward direction, cover any open set by disjoint intervals and sum the interval bounds, then use outer regularity to obtain `mu(E)<=C Leb(E)` for every Borel set `E`; Radon--Nikodym then gives the essential bound.

Therefore the central QFORM conjecture can be attacked directly as the linear small-ball inequality

`P(Q in I)<=C|I|`

without first proving any pointwise or continuous density formula. Theorem A guarantees that absolute continuity itself is not the hard step.

## 4. Assigned partner result applied to an actual inequality

I consumed the completed fleet04/B15 result

- repository `yspennstate/math-open-problems`
- commit `657566d3f5026e672f5cbe6b8c03fe63766bf0fb`
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T132108Z-b15-qform-separator-regularity-r2/REPORT.md`.

Its theorem applies in original coordinates when

`A=[[B,0,E],[0,D,F],[E^T,F^T,G]]`,

where `B` is an invertible symmetric block of order `d=3` or `4`, and the affine quadratic carried by the `J` variables is nonconstant almost surely. It proves `p_Q in C_0(R)` and

`||p_Q||_infinity <= M_B`,

with

`M_B=(2*pi+3*sqrt(3))/sigma_min(B)` for `d=3`,

and

`M_B=(4*pi+8)/sigma_min(B)` for `d=4`.

Applying this completed theorem to the exact small-ball quantity gives, for every interval `I`,

`P(Q in I)=int_I p_Q(y)dy <= M_B |I|`.

Thus on this separator branch all three regularity levels are simultaneously certified:

- absolute continuity (also independently from Theorem A),
- an explicit essentially bounded density,
- a continuous `C_0` representative.

The matrix-dependent factor `sigma_min(B)^{-1}` and the separator hypothesis remain, so this is not the universal theorem.

## 5. New obstruction: coarea plus a joint density cap cannot prove continuity

The stronger target continuity statement is not a measure-theoretic consequence of either absolute continuity or essential boundedness. More sharply, even rank-three quadratic curvature together with a bounded *joint* density does not force a continuous pushforward density.

### Proposition B (rank three + joint `L^infinity` is insufficient for continuity)

In `R^3`, let

`q(x)=|x|^2`

and let `Y` have joint density

`g(x)=c 1_{1<|x|<2}`,

where

`c=1/Vol({1<|x|<2})=3/(28*pi)<1`.

Then `g` is a probability density with `||g||_infinity<1`, `q` has three eigenvalues equal to one, yet the density of `q(Y)` is

`p(y)=2*pi*c*sqrt(y) 1_{1<y<4}`.

Indeed the level surface `|x|^2=y` has area `4*pi y`, while `|nabla q|=2sqrt(y)`, so the coarea formula gives the displayed density. It has jumps at `y=1` and `y=4`; hence it has no continuous representative agreeing almost everywhere.

This is **not** a QFORM counterexample because `g` is not a product of independent one-dimensional densities. It is a rigorous obstruction to a proof mechanism: any argument for the stronger continuous-density conclusion that uses only (a) `rank(A)>=3`, (b) a joint `L^infinity` cap, and (c) coarea/curvature, while discarding the original product structure, is false.

This also explains why the fleet04/B15 separator theorem needs genuine conditional independence/convolution smoothing rather than merely a bounded conditional joint density.

## 6. What is now settled and what remains unpaid

### Settled at target scope

- **Absolute continuity:** completely proved for every target instance, in fact for every nonzero quadratic form of any absolutely continuous random vector. No bounded-density conjecture is needed for this.
- **Essential boundedness:** exactly equivalent to the programme's linear interval/small-ball inequality. Full universal `C` remains OPEN.

### Stronger continuity

- Proved on the fleet04/B15 separator branch with explicit matrix-dependent height.
- Proved on several other scoped branches in existing worker results.
- **Not** derivable from generic rank-three coarea plus a joint density cap; Proposition B shows product structure is indispensable.
- Full target-level continuity for arbitrary fully coupled matrices and arbitrary rough product marginals remains OPEN.

## 7. First unpaid implication after this run

For the central conjecture, the first unpaid implication remains a dimension- and matrix-independent linear small-ball estimate for fully coupled heavy-coordinate matrices. For the stronger continuity request specifically, the first unpaid implication is:

> exploit the original product structure in a fully coupled/no-separator instance to obtain output translation continuity (or a `C_0` representative) without assuming continuity of any input density and without a fixed well-conditioned principal block.

The direct joint-density/coarea mechanism is now ruled out by Proposition B. A next continuity attack should retain a genuine product-coordinate averaging or bilinear bank before collapsing to a joint projected density.

## 8. Corrections respected

No pointwise van-der-Corput decay, rotated-coordinate independence, bounded indefinite projection pushforward, finite fragment localization, or naive fiber-supremum estimate is used. Repeated eigenvalues are treated as nondegenerate whenever the Hessian is nonzero. No numerical histogram is used as proof.

**Full QFORM remains OPEN / NOT PROVED.**
