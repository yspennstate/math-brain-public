SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-24T02:44:25Z.
attacking: generic-matrix zero-loss localization: remove exact Schur/pivot degeneracies by strict-margin approximation while preserving the universal density constant, arbitrary translations, fragments, unbounded supports, and no moment assumptions.

# fleet03/B14 — generic-matrix and source-law zero-loss closure

Run: `20260924T024425Z-fleet03-B14-QFORM-auto11`.
Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING LOCALIZATION THEOREM / PARTNER RESULT APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. This report proves a zero-loss closure reduction only; it does not prove the generic analytic core. No Gaussian, log-concavity, moment, compact-support, connected-support, finite-fragment, post-rotation independence, arbitrary-joint coarea, conditional-density-cap, or law-uniform pointwise van-der-Corput premise is used.

## 1. Small-ball formulation

For a probability law `mu` on the real line, the following implication is elementary and will be used throughout:

> If `mu(I) <= C |I|` for every bounded interval `I`, then `mu` is absolutely continuous with respect to Lebesgue measure and its Radon--Nikodym density satisfies `||p||_(infinity,ess) <= C`.

Indeed the interval estimate extends to open sets by writing every open subset of `R` as a countable disjoint union of intervals, and hence to all Lebesgue-null Borel sets by outer regularity. Lebesgue differentiation then gives the essential density cap. Conversely an essentially bounded density immediately gives the interval estimate.

Thus it is enough to preserve the interval constant exactly.

## 2. The generic symmetric class

For fixed `n`, let `Sym_n` denote the real symmetric matrices. Define `G_n` to be the set of `G in Sym_n` such that

1. every nonempty principal minor is nonzero;
2. the characteristic polynomial has no repeated root (equivalently, the spectral discriminant is nonzero);
3. every off-diagonal entry is nonzero.

The set `G_n` is open and dense in `Sym_n`. To see this, in the independent upper-triangular coordinates form the polynomial

`P(G) = Disc(chi_G) * prod_{empty != S subset [n]} det(G_{S,S}) * prod_{i<j} G_{ij}`.

Every factor is a nonzero polynomial: a principal determinant is nonzero on a suitable diagonal matrix, each coordinate polynomial is nonzero, and the discriminant is nonzero on a diagonal matrix with distinct diagonal entries. Since the polynomial ring is an integral domain, `P` is not the zero polynomial. Hence its zero set has empty interior, while `{P != 0}` is open. This is exactly `G_n`.

In particular, `G_n` is dense even inside every nonempty open ball. Consequently a rational symmetric matrix can also be chosen in each such ball if a countable algebraic core is desired.

The point of this class is structural rather than quantitative. Every physical principal block is invertible; after any permutation, every successive principal pivot in an `LDL^T` elimination is nonzero; and repeated eigenvalues are absent. **No lower bound on any pivot or minor is asserted.** Any proof on this generic core must therefore have a constant uniform as those nonzero quantities approach zero.

## 3. New theorem: generic-matrix zero-loss closure

### Theorem `QFORM-GENERIC-MATRIX-ZERO-LOSS-CLOSURE-v1`

Fix a finite constant `C`. Suppose the following restricted statement holds uniformly in every dimension `n`:

> For every independent cap-one product input `X`, every symmetric `G in G_n` with `s_3(G)>1`, every deterministic vector `b` and scalar `c` in whatever affine-uniform version is being invoked, and every interval `I`,
> 
> `P{ X^T G X + b^T X + c in I } <= C |I|`.

Then the identical constant `C` holds for every real symmetric `A` satisfying `s_3(A)>=1`, with the same arbitrary independent cap-one product inputs and the same deterministic affine terms. In particular, setting `b=c=0` gives the owner's full quadratic-density target once the restricted generic analytic statement is proved.

Here `s_3` is the third singular value. For a symmetric matrix it is the third largest absolute eigenvalue.

### Proof

Let `A` satisfy `s_3(A)>=1`. Fix `eta>0` and put

`A_eta=(1+eta) A`.

Then

`s_3(A_eta) >= 1+eta`.

Because `G_n` is dense, choose a sequence `G_k in G_n` with

`||G_k-A_eta||_op -> 0`.

For all sufficiently large `k`, singular-value perturbation gives

`s_3(G_k) >= s_3(A_eta)-||G_k-A_eta||_op > 1`.

Thus the restricted hypothesis applies to `G_k`.

For each outcome `x in R^n`,

`|x^T(G_k-A_eta)x| <= ||G_k-A_eta||_op ||x||_2^2 -> 0`.

Every real-valued random vector `X` is finite coordinatewise almost surely, so `||X||_2^2<infinity` almost surely. Therefore

`X^T G_k X + b^T X+c -> X^T A_eta X+b^T X+c`

almost surely. No expectation and hence no moment assumption is used.

Fix a closed interval `I=[u,v]` and `delta>0`; write `I^delta=(u-delta,v+delta)`. On every sample for which the preceding convergence holds,

`1_{ {X^T A_eta X+b^T X+c in I} } <= liminf_k 1_{ {X^T G_k X+b^T X+c in I^delta} }`.

Fatou's lemma therefore gives

`P{X^T A_eta X+b^T X+c in I}`
`<= liminf_k P{X^T G_k X+b^T X+c in I^delta}`
`<= C (|I|+2 delta)`.

Letting `delta downarrow 0` yields

`P{X^T A_eta X+b^T X+c in I} <= C |I|`.              (3.1)

For the homogeneous target `b=c=0`, `X^T A_eta X=(1+eta)X^TAX`. Hence, for any interval `J`, applying (3.1) to `(1+eta)J` gives

`P{X^TAX in J} <= C(1+eta)|J|`.

Finally `eta downarrow 0` gives

`P{X^TAX in J} <= C|J|`.                              (3.2)

For the affine-uniform statement with fixed `b,c`, scale them together with the quadratic expression before the last step, or equivalently apply the same closure directly to the augmented family with `(b,c)` arbitrary; because the restricted hypothesis is uniform in all deterministic affine terms, the same constant survives. This proves the theorem. QED.

### Consequence for exact degeneracies

For purposes of proving the universal **essential density bound**, one may therefore work on matrices satisfying simultaneously:

- strict target margin `s_3(G)>1`;
- full invertibility;
- simple spectrum;
- every physical principal minor nonzero;
- every physical off-diagonal coefficient nonzero.

Exact zero pivots, exact zero Schur minors, repeated eigenvalues, and exact zero coefficients may be postponed to the zero-loss closure. However, **near-zero** pivots/minors remain fully present; a bound containing their reciprocals is not made uniform by this reduction.

## 4. Source-law zero-loss closure, including remote fragments and unbounded support

The matrix reduction is compatible with a second exact closure that removes source roughness without changing `C`.

Let `f` be any probability density with `0<=f<=1`. For `R>0` put

`delta_R = int_{|x|>R} f(x) dx`

and define

`f_R(x)=f(x) 1_{[-R,R]}(x) + 1_{[R+1,R+1+delta_R]}(x)`.

Then `f_R` is a compactly supported probability density, `0<=f_R<=1`, and

`||f_R-f||_1 <= 2 delta_R -> 0`.                       (4.1)

This operation relocates tail **mass**; it never renormalizes a truncated density and never asks for a tail moment.

Convolve `f_R` with a nonnegative compactly supported `C^infinity` approximate identity. The resulting density `g` is smooth, compactly supported, has total mass one and still obeys `||g||_infinity<=1`; it may be chosen arbitrarily close to `f_R` in `L^1`.

If desired, connected support and a strict cap can also be imposed at zero closure cost. Choose a very broad smooth probability bump `q`, positive throughout the interior of one interval containing `supp(g)`, with `||q||_infinity<1`, and set

`h=(1-epsilon)g+epsilon q`.

Then `h in C_c^infinity`, `supp(h)` is one finite interval, `h>0` in its interior,

`||h||_infinity <1`,

and `||h-g||_1<=2 epsilon`.                             (4.2)

No uniform bound on the support diameter, no uniform positive bridge floor, and no derivative bound is obtained or needed.

For independent marginals, tensorization gives

`d_TV( tensor_i mu_i, tensor_i nu_i ) <= sum_i d_TV(mu_i,nu_i)`.

Measurable pushforward contracts total variation. Therefore for **every Borel map** `F:R^n->R`, not only a quadratic map,

`|P_mu{F in I}-P_nu{F in I}| <= sum_i d_TV(mu_i,nu_i)`.   (4.3)

If all smooth connected-support strict-subcap approximants obey `P{F in I}<=C|I|` with the same `C`, let the marginal `L^1` errors tend to zero in (4.3). The original arbitrarily fragmented, arbitrarily translated, unbounded laws obey the identical estimate `C|I|`.

Thus arbitrary shifts, distant fragments and unbounded supports introduce **zero localization tax**. The approximating connected interval may become arbitrarily long and the bridge density arbitrarily small; this is only a closure statement and does not assert interval-law extremality.

## 5. Combined exact reduction

Combining Sections 3 and 4 yields the following clean proof target:

> It is enough to prove one universal interval constant `C` for independent inputs whose densities are `C_c^infinity`, strictly below one, positive on the interior of a single compact interval, and for generic symmetric matrices `G in G_n` satisfying `s_3(G)>1`. The constant must be uniform in dimension, support diameter, bridge height, derivative norms, spectral margin above one, all nonzero principal minors and all nonzero pivots.

If that restricted theorem is proved, the **same** `C`, not `C+epsilon` and not a dimension-dependent loss, holds for the original arbitrary cap-one product laws and every symmetric `A` with `s_3(A)>=1`.

This is a genuine localization theorem: all exact support and algebraic degeneracies can be removed simultaneously while preserving the universal density constant. It does not solve the remaining analytic problem, which is uniformity as the regularized quantities approach their degenerate limits.

## 6. Designated partner result applied at an actual inequality

The completed partner theorem actually used is fleet04/B14 r10:

- repository: `yspennstate/math-open-problems`;
- commit: `deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`.

Its theorem says that if some three original coordinates form an invertible principal block `B` with

`sigma = min_j |lambda_j(B)| >0`,

then, for all independent cap-one inputs and arbitrary outside curvature/couplings,

`||p_(X^T A X)||_(infinity,ess) <= 6 sqrt(pi)/sigma`.     (6.1)

The generic closure above reproduces (6.1) with **no constant loss**, even if all other physical minors of `A` are singular. Indeed fix `eta>0`, put `A_eta=(1+eta)A`, and choose generic `G_k->A_eta`. Let `B_k` be the corresponding physical triple. Then

`sigma_k := sigma_min(B_k) -> (1+eta) sigma`.

Applying fleet04/B14 r10 to the actual approximants gives, for every interval `I`,

`P{X^T G_k X in I} <= (6 sqrt(pi)/sigma_k) |I|`.          (6.2)

Passing `k->infinity` by the same buffered-interval argument yields

`P{X^T A_eta X in I} <= [6 sqrt(pi)/((1+eta)sigma)] |I|`. (6.3)

Now `X^T A_eta X=(1+eta)X^TAX`; applying (6.3) to `(1+eta)J` gives exactly

`P{X^TAX in J} <= (6 sqrt(pi)/sigma)|J|`.                (6.4)

Thus the partner inequality survives simultaneous genericization and de-genericization with its exact scale constant. Numerically `6 sqrt(pi)=10.634723105433...`.

This application is deliberately only a consistency/control chamber. The bare target condition `s_3(A)>=1` still does not force a physical triple with `sigma` bounded below universally.

## 7. Continuity ledger

Sections 3 and 4 preserve an interval small-ball constant and therefore an essentially bounded density. They do **not** preserve continuity of density representatives under weak/TV limits in the required form. Even if every regularized approximant has a continuous density, continuity of the limiting density does not follow from these arguments. Full-target continuity therefore remains OPEN.

## 8. Remaining implication

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.

The reduction removes exact zeros and source roughness from the analytic core. The remaining proof must establish a constant uniform as:

- strict spectral margin `s_3(G)-1 downarrow 0`;
- physical principal pivots/minors approach zero without becoming exactly zero;
- support diameter tends to infinity and connected-support bridge height tends to zero;
- the three spectral resources become arbitrarily diffuse across physical coordinates.

In particular, a Schur or elimination proof may now assume every required pivot exists, but it may not pay a reciprocal pivot without a compensating product-aggregation mechanism. This is the next B14 structural interface.

## 9. Integrity

The proof uses only finite-dimensional matrix continuity, total variation, smooth approximation, and the source-pinned fleet04/B14 theorem. It does not use any refuted arbitrary-joint coarea or pointwise oscillatory-decay claim. Repository transport and native learned-memory ingestion are distinct; this run remains `WITHOUT_VERIFIED_BRAIN`.
