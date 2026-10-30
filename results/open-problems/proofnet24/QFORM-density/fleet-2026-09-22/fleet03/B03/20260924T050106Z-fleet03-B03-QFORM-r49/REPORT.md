SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B03, 2026-09-24T05:01:06Z.
attacking: the near-coloop puncture at fractional level — retain T-C-D dependence, prove a uniform half-Riesz budget and spend it through whole-copy time, an independent square, or an outer physical pair.

# fleet03/B03 r49 — near-coloop half-Riesz/time receiver

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source pins

The unrestricted target remains: independent real coordinates with one-dimensional densities bounded by one; real symmetric `A` with at least three eigenvalues of absolute value at least one; prove a universal output-density bound or give a valid counterexample. No moments, compact support, log-concavity, connected support, identical laws, Gaussianity, or independence after rotation is assumed.


The live near-coloop debt consumed here is the exact-rank-three null-pivot representation in

`yspennstate/math-open-problems@5117e9ec45221d02dfa74cedf6c4dcee9fae60c7`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260924T040707Z-fleet02-B11-QFORM-r12/R49_REFRESH.md`.

The outer indefinite-pair transducer used in Section 7 is the completed pair-log theorem

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

The designated partner result applied in Section 8 is fleet04/B03 r3,

`yspennstate/math-open-problems@8147f1247043e419eb6762911c4a34fa58494d0f`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260924T021651Z-fleet04-B03-hyperbola-fourvolume-r3/REPORT.md`.

## 2. Elementary cap-to-half-Riesz lemma

### Lemma 2.1

If a real random variable `Y` has a density bounded by `F`, then

`sup_a E |Y-a|^(-1/2) <= 2 sqrt(2F)`.

### Proof

For every `a`, layer cake gives

`E |Y-a|^(-1/2)
 = integral_0^infinity P(|Y-a|<u^(-2)) du`.

The density cap implies

`P(|Y-a|<u^(-2)) <= min(1,2F u^(-2))`.

With `u_0=sqrt(2F)`, integration gives

`u_0 + integral_(u_0)^infinity 2F u^(-2) du
 = sqrt(2F)+sqrt(2F)
 =2sqrt(2F)`.

QED.

## 3. Near-coloop conditional cap without false sum/difference independence

Let `X_0` be a genuine original-coordinate input with density bounded by one. Let `W` denote a disjoint residual original-coordinate bank, independent of `X_0`. Let

`(T,C,D)`

be three orthonormal linear forms of `W`; no independence among `T,C,D` is asserted. Fix `0<q<=1` and set

`Z=sqrt(q) X_0 + sqrt(1-q) T`.

For almost every `(c,d)`, conditioning first on `(C,D)=(c,d)` and then on `T=t` leaves

`Z = sqrt(q) X_0 + constant`.

Therefore its conditional density is a translate/rescale of the genuine independent scalar law of `X_0`, with cap `q^(-1/2)`. Mixing in the conditional law of `T` does not increase this cap. Hence

`||p_(Z | C=c,D=d)||_infinity <= q^(-1/2)`

for almost every `(c,d)`.

This is deliberately different from conditioning one conjugate sum/difference coordinate on the other. The cap comes from the source-disjoint physical `X_0`, not from a rotated or decoupled-coordinate independence claim.

Also, since `C` is a one-dimensional unit projection of a cap-one product law, the standard one-dimensional product-projection estimate used throughout the programme gives

`||p_C||_infinity <= sqrt(2)`.

Translations of `C` have the same cap.

## 4. Main theorem: near-coloop half-Riesz receiver

### Theorem 4.1 — `QFORM-NEAR-COLOOP-HALFRIESZ-TIME-v1`

Under Section 3, let `beta!=0`, let `ell` be any real number, and let `R(C,D)` be an arbitrary measurable real function. Define

`S = 2 beta Z C + ell Z + R(C,D)`.

Then

`boxed:
 sup_s E |S-s|^(-1/2)
 <= 2^(11/4) q^(-1/4) |beta|^(-1/2).`

No restriction at all is imposed on the dependence among `T,C,D`, and the same-bank term `R(C,D)` is retained exactly.

### Proof

Absorb the linear `Z` term by writing

`C_tilde = C + ell/(2 beta)`.

Then

`S-s = 2 beta C_tilde [ Z - a(C,D,s) ]`

for a measurable `a` wherever `C_tilde!=0`; the zero set can be ignored in the nonnegative extended expectation because `C_tilde` has an absolutely continuous law.

Condition on `(C,D)`. Lemma 2.1 and the conditional cap from Section 3 give

`E[ |Z-a|^(-1/2) | C,D ]
 <= 2 sqrt(2 q^(-1/2))
 =2 sqrt(2) q^(-1/4)`.

Therefore

`E[|S-s|^(-1/2)|C,D]
 <= (2|beta| |C_tilde|)^(-1/2)
    2 sqrt(2) q^(-1/4)
 = 2 q^(-1/4)|beta|^(-1/2)|C_tilde|^(-1/2).`

Average and apply Lemma 2.1 to `C_tilde`, using `||p_C||_infinity<=sqrt(2)`:

`E|C_tilde|^(-1/2)
 <= 2 sqrt(2 sqrt(2))
 =2^(7/4)`.

Thus

`sup_s E|S-s|^(-1/2)
 <= 2 * 2^(7/4) q^(-1/4)|beta|^(-1/2)
 =2^(11/4) q^(-1/4)|beta|^(-1/2)`.

QED.

## 5. Exact-rank-three null-pivot specialization

Take the exact-rank-three representation from the live near-coloop debt:

`A=R M R^T`, `R^T R=I_3`,

with every nonzero eigenvalue of symmetric invertible `M` of magnitude at least `s>0`. Let original coordinate `0` have row leverage

`q=||r_0||^2>0`

and physical diagonal

`A_00=0`.

Choose only a spectral bookkeeping basis with `e_1=r_0/sqrt(q)` and align the transverse plane. Then

`M = [[0,beta,0],
      [beta,alpha,delta],
      [0,delta,gamma]]`,

and the full exact-rank-three quadratic form has the near-coloop shape

`S = 2 beta sqrt(q) X_0 C
   +2 beta sqrt(1-q) T C
   +alpha C^2 +2delta C D +gamma D^2`,

where `(T,C,D)` is a genuine three-dimensional orthonormal projection of the residual original product bank.

A useful quantitative fact is immediate from the spectral gap:

`beta^2 = ||M e_1||^2 >= s^2`,

because all singular values of symmetric invertible `M` are at least `s`. Hence

`|beta|>=s`.

Applying Theorem 4.1 with the entire puncture and transverse curvature inside `R(C,D)` gives

`boxed:
 sup_u E|S-u|^(-1/2)
 <= 2^(11/4) q^(-1/4) s^(-1/2).`

In particular, throughout the genuinely near-coloop chamber `q>=1/2`,

`boxed:
 sup_u E|S-u|^(-1/2) <= 8 s^(-1/2).`

The estimate is uniform as `q -> 1` and retains the nonzero `T C` puncture exactly. It does **not** prove that `S` itself has a bounded density.

## 6. Assigned whole-copy time integral

Let `S'` be an independent copy of the whole scalar output `S`. With the convention

`phi_S(t)=E exp(i t S)`,

the one-dimensional Riesz-energy identity, justified by Abel/Gaussian regularization, is

`integral_R |t|^(-1/2)|phi_S(t)|^2 dt
 = sqrt(2 pi) E|S-S'|^(-1/2).`

Conditioning on `S'` and using the translation-uniform half-Riesz potential from Theorem 4.1 yields

`boxed:
 integral |t|^(-1/2)|phi_S(t)|^2 dt
 <= 2^(13/4) sqrt(pi) q^(-1/4)|beta|^(-1/2).`

In the exact-rank-three near-coloop chamber `q>=1/2`, `|beta|>=s`, this simplifies to

`boxed:
 integral |t|^(-1/2)|phi_S(t)|^2 dt
 <= 8 sqrt(2 pi) s^(-1/2).`

Numerically the dimensionless constant is

`8 sqrt(2 pi)=20.053026197048002...`.

The independent-copy identity is used only for the **whole** output difference `S-S'`. No variable of the form `X-X'` is declared independent of its conjugate `X+X'`.

## 7. Recovering linear small-ball scaling when a genuine extra square or pair exists

### 7.1 One source-disjoint physical square

Let `Y` be a cap-one original-coordinate input independent of the entire `S` bank, and let `d!=0`. Then

`W=d(Y+h)^2+S`.

The square pushforward has the standard envelope

`p_(d(Y+h)^2)(v) <= |d|^(-1/2)|v|^(-1/2)`

on its half-line. Therefore

`p_W(x)
 <= |d|^(-1/2) E|x-S|^(-1/2)`.

Hence

`boxed:
 ||p_W||_(infinity,ess)
 <= 2^(11/4) q^(-1/4)|d beta|^(-1/2).`

For `q>=1/2`, `|beta|>=s`,

`boxed:
 ||p_W||_(infinity,ess) <= 8 (|d|s)^(-1/2),`

and every interval `I` obeys the linear small-ball estimate

`P(W in I) <= 8 (|d|s)^(-1/2)|I|`.

This is essential boundedness. Continuity is not proved by this receiver.

### 7.2 Outer invertible indefinite physical pair via the completed pair-log theorem

Theorem 4.1 implies the small-ball budget

`sup_u P(|S-u|<rho)
 <= H sqrt(rho),`

with

`H=2^(11/4) q^(-1/4)|beta|^(-1/2)`.

Suppose a source-disjoint original-coordinate outer pair is invertible indefinite with

`D_B=|det B|`, `kappa=sigma_min(B)>0`,

and completing that pair leaves exactly the near-coloop remainder `S`. The completed pair-log theorem gives

`||p_Q||_infinity
 <=4 sqrt(2H) (D_B kappa)^(-1/4)`.

Therefore

`boxed:
 ||p_Q||_(infinity,ess)
 <= 2^(31/8) q^(-1/8)|beta|^(-1/4)(D_B kappa)^(-1/4).`

In the chamber `q>=1/2`, `|beta|>=s`, this simplifies to the clean target-scale branch

`boxed:
 ||p_Q||_(infinity,ess)
 <=16 s^(-1/4)(D_B kappa)^(-1/4).`

Again this branch proves essential boundedness, not continuity.

## 8. Required partner application: fleet04/B03 r3

The designated partner's completed zero-diagonal hyperbolic-pair theorem proves the translation-uniform envelope

`p_H(y) <= sqrt(2)|mu|^(-1/2)|y|^(-1/2)`

for the completed physical pair `H=2mu(U+alpha)(V+beta)`.

Apply that actual inequality with the near-coloop remainder `S` above. Conditioning on `S`,

`p_(H+S)(x)
 <= sqrt(2)|mu|^(-1/2) E|x-S|^(-1/2)`.

Thus Theorem 4.1 gives

`boxed:
 ||p_(H+S)||_(infinity,ess)
 <=2^(13/4) q^(-1/4)|mu beta|^(-1/2).`

In the exact-rank-three near-coloop chamber `q>=1/2`, `|beta|>=s`,

`boxed:
 ||p_(H+S)||_(infinity,ess)
 <=8 sqrt(2) (|mu|s)^(-1/2).`

This is a literal equation-level use of the completed fleet04/B03 result, not merely a citation.

## 9. Why the half-Riesz result must not be overclaimed as an L-infinity theorem

The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` warns that conditional caps alone do not replace genuine product structure. The following exact stress test shows the same boundary for the present interface.

Let `C,U` be independent Uniform[-1/2,1/2], let `D` be independent Uniform[0,1], and define for `C!=0`

`Z = U - D^2/(2C)`

(with any definition on the null event `C=0`). Then for every `(c,d)`, `Z|(C=c,D=d)` is a translate of a unit-uniform variable, so

`||p_(Z|C,D)||_infinity=1`,

and the pair `(C,D)` itself has joint density cap one. Nevertheless

`2 Z C + D^2 = 2 U C`.

For `0<|r|<1/2`, a direct product-density calculation gives

`p_(2UC)(r)=log(1/(2|r|))`,

which diverges at zero.

Thus the conditional cap used in Theorem 4.1 is strong enough for a half-Riesz potential, but **not** for a direct bounded-density conclusion. The actual near-coloop law has extra product-projection provenance in `(T,C,D)`; exploiting that provenance jointly with the `gamma D^2` curvature is still required if no source-disjoint square/pair is available.

## 10. Remaining implication

This run closes the following fractional/time step:

- the near-coloop puncture `2 beta sqrt(1-q) T C` does not blow the half-Riesz budget as `q->1`;
- for `q>=1/2`, the exact-rank-three null-pivot output has a dimension-free translation-uniform `1/2`-Riesz potential and the requested weighted whole-copy time integral;
- one genuine independent square, the completed pair-log outer pair, or the designated partner's hyperbolic outer pair converts that budget to linear small-ball / `L^infinity` control.

The unrestricted QFORM conjecture remains **OPEN**. The still-unpaid near-coloop endpoint is the one-copy density of the bare exact-rank-three punctured form when no source-disjoint smoothing resource is available. A valid closure must exploit the actual product-projection origin of `(T,C,D)` jointly with `gamma D^2`, or route the geometry to one of the paid outer receivers. Full-target continuity also remains **OPEN**.
