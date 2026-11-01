SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B03, 2026-09-24T02:59:16Z.
attacking: a tail-stable rank-two physical crossing when one source bank remains linear; derive one-copy density first and then a dependence-safe whole-copy time integral, without deleting extra crossing directions.

# fleet03/B03 r46 — one-linear-bank rank-two receiver

Status: **new supporting theorem proved; full QFORM remains OPEN; full-target continuity remains OPEN**.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction discipline

The target is the full arbitrary-product quadratic-form conjecture: independent real coordinates with densities bounded by one, no moment/support/log-concavity assumptions, and a real symmetric matrix with at least three eigenvalues of modulus at least one. This report does **not** claim the full theorem.

The proof below does not rotate the random vector and then assert independence, does not condition one conjugate sum/difference variable on the other, and does not use a law-uniform pointwise van-der-Corput bound. It is deliberately compatible with fragmented and unbounded-support cap-one densities.

The new result addresses a physical-bank configuration in which one bank enters the conditioned form only linearly. Unlike perturbative rank-one triangle arguments, all additional cross singular directions are retained through the full Euclidean coefficient norm; no nonzero crossing tail is deleted.

## 2. Two elementary cap lemmas

### Lemma 2.1 (planar reciprocal-radius bound)

Let `W` be an R^2-valued probability vector with density `rho_W` satisfying

`||rho_W||_infinity <= M`.

Then, for every `a in R^2`,

`E |W-a|^{-1} <= 2 sqrt(pi M)`.

**Proof.** For every `r>0`,

`P(|W-a|<r) <= min(1, pi M r^2)`.

Using layer cake,

`E |W-a|^{-1} = int_0^infinity P(|W-a|<1/t) dt`.

Split at `t0=sqrt(pi M)`. The portion below `t0` is at most `t0`; the portion above is at most

`int_t0^infinity pi M t^{-2} dt = pi M/t0=t0`.

Thus the sum is `2 sqrt(pi M)`. QED.

### Lemma 2.2 (one-dimensional half-Riesz bound from an L-infinity density cap)

If a real random variable `D` has density bounded by `H`, then

`E |D|^{-1/2} <= 2 sqrt(2H)`.

Indeed `P(|D|<r)<=min(1,2Hr)` and layer cake for `|D|^{-1/2}` with the split `u0=sqrt(2H)` gives the stated constant.

## 3. Input projection facts used

I use the standard product-projection bounds already used in the current QFORM fleet and in fleet03/B03 r45:

1. If `Y=(Y_j)` has independent scalar coordinates with densities at most one, then for every nonzero vector `w`, the scalar projection `<w,Y>` has a density bounded by

`L_1/||w||`, with `L_1=sqrt(2)`.

2. If `X=(X_i)` has independent scalar coordinates with densities at most one and `U` is an `m x 2` matrix with orthonormal columns, then `U^T X` has a two-dimensional density bounded by

`M_2=2`.

Only these two projection statements are imported. The theorem below is first proved with abstract constants `L_1,M_2`, making its dependence transparent.

## 4. Main theorem: a rank-two crossing with one linear bank

### Theorem 4.1 (`QFORM-ONE-LINEAR-BANK-R2-DENSITY-v1`)

Let `X in R^m` and `Y in R^n` be independent source banks. Let `Z` be any additional random element independent of `(X,Y)`. Assume:

- conditional on nothing, every scalar coordinate in the physical `X` and `Y` banks is independent and has density at most one;
- every scalar projection of `Y` has density at most `L_1/||w||` in direction `w`;
- every orthonormal two-dimensional projection of `X` has joint density at most `M_2`.

Let `M` be an `m x n` real matrix with singular values `s_1>=s_2>0` (all further singular values are arbitrary and are retained). Let `q=q(Z) in R^n` be arbitrary measurable, and let `F=F(X,Z)` be arbitrary measurable. Define

`S = F(X,Z) + 2 <M^T X + q(Z), Y>`.

Then `S` has a density and

`||p_S||_(infinity,ess) <= L_1 sqrt(pi M_2) (s_1 s_2)^(-1/2)`.

For cap-one product banks, `L_1=sqrt(2)` and `M_2=2`, so

`boxed( ||p_S||_(infinity,ess) <= 2 sqrt(pi) (s_1 s_2)^(-1/2) ).`       (4.1)

Consequently every interval `I` satisfies the linear small-ball bound

`boxed( P(S in I) <= 2 sqrt(pi) (s_1 s_2)^(-1/2) |I| ).`              (4.2)

No continuity conclusion is claimed from this argument.

### Proof

Take an SVD

`M = U Sigma V^T`,

and let `u_1,u_2` and `v_1,v_2` be the first two left/right singular directions. Write

`a(X,Z)=M^T X+q(Z)`.

Fix `(X,Z)=(x,z)`. Except on the set `a(x,z)=0`, the conditional law of

`F(x,z)+2<a(x,z),Y>`

has a density bounded by the scalar projection estimate:

`||p_(S|X=x,Z=z)||_infinity <= L_1/[2 ||a(x,z)||]`.                 (4.3)

The exceptional event `a=0` has probability zero: indeed its first two right-singular coordinates vanish, while those coordinates have an absolutely continuous two-dimensional distribution by the argument below.

Now project `a` onto `span(v_1,v_2)`. Its coordinate vector there is

`( v_1^T a, v_2^T a )
 = ( s_1 u_1^T X + v_1^T q(Z),
     s_2 u_2^T X + v_2^T q(Z) ).`                                (4.4)

Condition on `Z=z`. The vector `(u_1^T X,u_2^T X)` has density at most `M_2`. Scaling by `diag(s_1,s_2)` and translating by the displayed `q(z)` vector gives density cap

`M_2/(s_1 s_2)`                                                      (4.5)

for the two-vector in (4.4). Since

`||a|| >= |P_span(v1,v2) a|`,

Lemma 2.1, uniformly in `z`, yields

`E[ ||a(X,Z)||^{-1} | Z=z ]
 <= 2 sqrt( pi M_2/(s_1s_2) ).`                                    (4.6)

Average (4.3), using (4.6). Mixtures of the conditional densities are absolutely continuous because the exceptional set has probability zero, and

`||p_S||_infinity
 <= (L_1/2) E ||a||^{-1}
 <= L_1 sqrt(pi M_2) (s_1s_2)^(-1/2).`                             (4.7)

This proves the abstract bound and, with `L_1=sqrt(2), M_2=2`, (4.1). The interval estimate (4.2) follows by integrating the density over `I`. QED.

## 5. QFORM interpretation and tail stability

Consider a full physical quadratic form after conditioning on every original coordinate outside two disjoint physical banks `R,C`. Suppose the conditioned `C`-bank has **zero quadratic self block**, so the remaining dependence on `X_C` is linear, while the `R-C` crossing is a matrix `M=A[R,C]` (up to the conventional factor two in `x^T A x`). Arbitrary `R`-bank self curvature, arbitrary conditioned affine terms, and arbitrary additional singular directions of `M` are allowed.

If the two largest singular values of `M` satisfy `s_1(M)s_2(M)>=delta`, then Theorem 4.1 gives

`||p_Q||_(infinity,ess) <= 2 sqrt(pi) delta^(-1/2)`                 (5.1)

uniformly in the conditioned outside coordinates, hence also after averaging them back in.

Crucially, if

`M=M_2+E`

with `rank(M_2)=2`, the proof never drops `E`. The complete coefficient vector `M^T X+q` stays in the conditional scalar projection, and only the norm inequality

`||M^T X+q|| >= ||P_(v1,v2)(M^T X+q)||`

is used. Thus this receiver is stable under arbitrary additional crossing directions, provided the actual full matrix retains two singular values with controlled product. This is exactly the kind of nonperturbative tail retention that the live corrections require.

The limitation is equally explicit: arbitrary quadratic self curvature in the linearized `C` bank is **not** covered. The fleet02/B03 rank-two triangle instability shows why one must not silently add such curvature as a harmless perturbation.

## 6. Assigned dependence-safe time integral

Let `S'` be an independent copy of the **whole scalar output** `S`. From (4.1), set

`H=2 sqrt(pi) (s_1s_2)^(-1/2)`.

Then the difference `D=S-S'` has density

`p_D=p_S * p_(-S')`,

so `||p_D||_infinity<=H`. Lemma 2.2 gives

`E |S-S'|^{-1/2} <= 2 sqrt(2H)
 = 4 pi^(1/4) (s_1s_2)^(-1/4).`                                   (6.1)

For the Fourier convention `phi_S(t)=E exp(itS)`, regularized one-dimensional Riesz inversion gives

`int_R |t|^(-1/2) |phi_S(t)|^2 dt
 = sqrt(2pi) E |S-S'|^(-1/2).`                                    (6.2)

Combining (6.1)-(6.2),

`boxed(
 int_R |t|^(-1/2) |phi_S(t)|^2 dt
 <= 4 sqrt(2) pi^(3/4) (s_1s_2)^(-1/4)
 )`                                                                (6.3)

with numerical leading constant

`4 sqrt(2) pi^(3/4) = 13.348651463672827...`.

This uses the independent-copy identity only as

`|phi_S(t)|^2 = E exp(it(S-S'))`

for the whole scalar output. No claim is made that `X-X'` is independent of `X+X'`, and no conditional density cap for a conjugate sum/difference variable is introduced.

Notice that (6.3) is not being misused as a stand-alone route from half-Riesz energy to `L^infinity`; the one-copy density estimate (4.1) was proved first. Hence the run genuinely recovers linear small-ball scaling rather than stopping at an `L^2`/collision endpoint.

## 7. Designated partner fleet04/B03 actually applied

The latest completed designated partner result read this run is fleet04/B03 r3, canonical mathematics

`yspennstate/math-open-problems@19345adf8bb78f11da95a556d6fdcc47af957b19`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260924T021651Z-fleet04-B03-hyperbola-fourvolume-r3/REPORT.md`.

Its literal hyperbolic-pair determinant receiver proves, in its stated physical scope,

`||p_Q||_(infinity,ess) <= 8 Delta^(-1/4)`,

where `Delta=|det A[H union I,H union J]|` is the paid four-coordinate determinant.

Apply Lemma 2.2 to the whole-copy difference exactly as in Section 6. With

`H_partner=8 Delta^(-1/4)`,

one obtains the new explicit assigned-time consequence

`boxed(
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= 8 sqrt(2pi) Delta^(-1/8)
 )`.                                                               (7.1)

For the partner's concrete block `A_*`, `Delta=1`, hence

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt <= 8 sqrt(2pi)
 =20.053026197048002...`.                                          (7.2)

This is an actual application of the designated partner theorem to the B03 time-integral objective, not merely a citation.

## 8. Relation to the live frontier

Theorem 4.1 pays a genuine class that is not perturbative in the crossing tail: one physical bank may be linear while the other bank carries arbitrary same-bank curvature and the crossing can have arbitrary rank, with payment determined only by the top-two singular-value product of the **actual** crossing.

It does not by itself pay the current fully general aligned rank-two packet because that packet may contain nonzero self curvature on both banks. The exact remaining implication is therefore sharper:

> Find a product-preserving way, from the live structural packet, either to expose a bank with negligible/zero self block **in a manner that is exact rather than perturbative**, or to extend the time-integrated receiver so that one nonzero same-bank quadratic block can be retained without recreating the rank-two logarithmic singularity identified by fleet02/B03.

A plausible next mechanism is a hybrid: use fleet04/B03's literal hyperbolic-pair completion to absorb one same-bank direction, then apply the present reciprocal-radius argument to the remaining full crossing coefficient vector. Any such splice must be done by an exact physical-coordinate Schur identity; an approximate deletion is invalid under the current correction set.

## 9. Scope and conclusion

- Full QFORM conjecture: **OPEN**.
- Valid counterexample to the full target: **none produced**.
- New result: **proved supporting theorem**, equations (4.1)-(4.2), tail-stable in all extra crossing directions.
- Assigned whole-copy integrated estimate: **proved**, equation (6.3).
- Designated partner fleet04/B03: **applied to an actual inequality**, equation (7.1), concrete (7.2).
- Density regularity: **essential boundedness/absolute continuity proved in the stated branch; continuity not proved**.
- General rotations: never used to assert independence.
- Sum/difference dependence: never broken.
