# r36 affine upgrade — the near-double-zero collar survives arbitrary packet affine terms

This note strengthens REPORT.md using the rank-one affine small-ball theorem already consumed and proved in the immediately preceding fleet03/B05 run

`yspennstate/math-open-problems@3e6186c2577a073283e59d0d71a8d6ff935c7d90`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260924T004011Z-fleet03-B05-QFORM-r36/REPORT.md`.

It removes the affine-null-direction caveat stated in Sections 2, 8 and 9 of the first r36 REPORT. The stronger theorem below is the result to carry forward.

## 1. One-third envelope for the nearby-linear-form hyperbola

Keep the notation of REPORT.md. Thus

`B=[[a,c],[c,d]]`, `D=c^2-ad>0`,
`max(|a|,|d|)<=sqrt(D)/5`,
`kappa=c+sign(c)sqrt(D)`,
`alpha=d/kappa`, `beta=a/kappa`,
`delta=1-alpha beta`,

with

`|alpha|,|beta|<1/8`,
`|kappa|delta=2sqrt(D)`,
`gamma:=|kappa|/sqrt(D)<=1+sqrt(26/25)`.

For independent translated scalar inputs `y,z` with density caps `sqrt(2)`, set

`u=y+alpha z`, `v=z+beta y`.

REPORT.md proves that the integral in the exact product-density formula obeys

`I(w)<=23[1+log_+(1/|w|)]`,
`I(w)<=7|w|^(-1/2)`.                                                (1.1)

For `0<|w|<=1`,

`|w|^(1/3)[1+log(1/|w|)]
 <=3 exp(-2/3)`,                                                     (1.2)

while for `|w|>=1`, `|w|^(-1/2)<=|w|^(-1/3)`. Hence both ranges give

`boxed:
 I(w)<=C_I |w|^(-1/3),
 C_I=69 exp(-2/3)=35.4257812132... .
`                                                                       (1.3)

The density of the quadratic pair

`a y^2+2c yz+d z^2=kappa uv`

therefore satisfies

`p_pair(r)
 <= [C_I/(|kappa|delta)] (|kappa|/|r|)^(1/3)`
` = (C_I/2) gamma^(1/3) D^(-1/3)|r|^(-1/3).`                       (1.4)

This envelope is uniform in arbitrary translations of the two original independent scalar banks.

## 2. Rank-one affine first-bank small ball

Let the first product bank consist of independent original coordinates with density caps at most one and let

`V=(S,R)=Gamma^T X`, `Gamma^T Gamma=I_2`.

The source-pinned rank-one affine theorem used in the preceding run states that for

`T=lambda m S^2+b^T V+q0`,                                        (2.1)

with arbitrary `b`,

`P(|T-t|<rho)
 <=min{1,H sqrt(rho)},
 H=10/sqrt(|lambda|m).`                                             (2.2)

No conditional density of `S|R` is used. In the original first-bank coordinates, (2.1) is exactly a rank-one quadratic with an arbitrary affine form.

The elementary layer-cake lemma from that same run gives

`boxed:
 sup_t E|T-t|^(-1/3)
 <=3 H^(2/3)
 =3*10^(2/3)(|lambda|m)^(-1/3).
`                                                                       (2.3)

## 3. Full affine ratio-packet theorem on the collar

### Theorem `QFORM-RATIOPACKET-NEAR-DOUBLEZERO-AFFINE-v1`

Consider the complete ratio packet with arbitrary affine terms

`Q=V^T C V+2V^T P W+W^T B W
   +ell_V^T V+ell_W^T W+q0`,                                       (3.1)

where `W=(Y,Z)`, the first bank is disjoint from the scalar banks, `Y,Z` are mutually independent normalized scalar product projections with density caps at most `sqrt(2)`, and

`C-PB^(-1)P^T=lambda m e1e1^T`,
`mu=|det B||lambda|`.                                               (3.2)

Assume `B` is indefinite and satisfies the collar

`max(|a|,|d|)<=sqrt(|det B|)/5`.                                    (3.3)

Then

`boxed:
 ||p_Q||_(infinity,ess)
 <312 (mu m)^(-1/3).
`                                                                       (3.4)

The conclusion allows all affine terms in (3.1), including a nonzero affine component in the Schur-null `R` direction.

### Proof

Complete the scalar pair without changing the first-bank law. Put

`h(V)=B^(-1)(P^T V+ell_W/2)`.                                      (3.5)

Then

`Q=[W+h(V)]^T B[W+h(V)]+T(V)`,                                     (3.6)

where, by direct expansion,

`T(V)
 =V^T(C-PB^(-1)P^T)V
  +(ell_V-PB^(-1)ell_W)^T V+q1`
` =lambda m S^2+b^T V+q1`.                                        (3.7)

Condition on the first-bank environment `V`. The two coordinates of `W+h(V)` are translated versions of the two genuinely independent scalar banks. Apply (1.4) to their indefinite quadratic pair. At an output value `t`, the resulting conditional density is at most

`(C_I/2) gamma^(1/3)D^(-1/3)|t-T(V)|^(-1/3)`.                     (3.8)

Average (3.8) over the first bank and use (2.3):

`||p_Q||inf
 <= (3 C_I/2) 10^(2/3) gamma^(1/3)
    [D |lambda| m]^(-1/3).`                                        (3.9)

Since `D=|det B|` and `D|lambda|=mu`, while

`gamma<=1+sqrt(26/25)`,                                             (3.10)

the numerical constant is

`(3*69 exp(-2/3)/2)*10^(2/3)*[1+sqrt(26/25)]^(1/3)`
` =311.7791706964... <312.`                                        (3.11)

This proves (3.4). QED.

For the standard packet `m>=3/20`,

`boxed:
 ||p_Q||_(infinity,ess)
 <312(20/(3mu))^(1/3)
 <587.207 mu^(-1/3).
`                                                                       (3.12)

The constant is intentionally not optimized. The structural point is uniformity through `a,d ->0` with arbitrary rough inputs, arbitrary affine packet terms, arbitrary overlap shifts, and without conditioning the dependent first-bank residual.

## 4. Updated remaining factor

This theorem supersedes the affine-null caveat in the first REPORT. A ratio-packet survivor is no longer allowed to hide inside a nonzero affine `R` term while `B` remains in the near-double-zero collar.

The next B05 geometric debt is therefore outside the collar:

`QFORM-INDEFINITE-PAIR-OUTSIDE-COLLAR-COMPILER-v1`:

> in the live ratio packet, combine the existing raw-diagonal, scalar-heavy-crossing, exact-slope and convex-pair exits to control every indefinite `B` satisfying
> `max(|a|,|d|)>sqrt(|det B|)/5`, or isolate a quantitative escaped-curvature parameter that is forced by the three-large-eigenvalue hypothesis.

The full QFORM conjecture remains open. Continuity is not proved by this theorem; it supplies absolute continuity and an essential density bound.
