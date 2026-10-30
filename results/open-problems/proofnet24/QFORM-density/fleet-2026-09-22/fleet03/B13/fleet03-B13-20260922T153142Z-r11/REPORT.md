# fleet03/B13 — profile-overlap bank forcing in the nested-heavy rank-three obstruction

**Run:** `fleet03-B13-20260922T153142Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED RANK-THREE PROFILE-OVERLAP BANK THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains **OPEN / NOT PROVED**. The theorem below is for the exact-rank-three nested-heavy core. Arbitrary additional spectrum remains a separate debt outside already completed scoped branches.

## 1. Exact target and source state

The owner target is one universal finite `C` such that for every dimension, every independent real input with one-dimensional density bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one,

`P(X^T A X in [t,t+h]) <= C h`

for all `t` and `h>0`. No moment, support, connectedness, log-concavity, or independence-after-rotation assumption is used here. Continuity of the output density is tracked separately.

The current correction state rules out law-uniform pointwise quadratic-phase decay, fiber-supremum closure, conditional-density substitutes for genuine independence, one-cross-minor closure, bounded-diameter localization, and any universal fixed fragment count. The present proof works entirely with original-coordinate product structure and physical spectral-frame minors.

The designated `fleet04/B13` current-QFORM artifact was not present in the fresh repository snapshot, so no result from that slot is fabricated. Work proceeds asynchronously using completed compatible peer mathematics.

## 2. Completed peer mathematics actually applied

### 2.1 Exact extremal-product reduction

Source:

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`

(fleet02/B13 exact bang-bang report).

For every measurable `0<=K<=1`,

`sup int K(x) prod_i f_i(x_i) dx`

over `0<=f_i<=1`, `int f_i=1`, equals the supremum over product indicators `f_i=1_{E_i}` with `|E_i|=1`. Hence the essential-density target is exactly equivalent to the geometric slab inequality on arbitrary unit-measure product sets. Bounded finite unions of intervals are dense, but no bounded fragment count or bounded diameter is available.

### 2.2 Fresh residual pair-incidence theorem

Source:

`yspennstate/math-open-problems@93bed74b07afe996a4aa08eaeb88f35060653134`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T152225Z-fleet02-B13-productset-7f3c9a/REPORT.md`.

This theorem supplies the exact nested-heavy pair weights and incidence identities used below. The present run strengthens its `1/2` concentration conclusion to asymptotically **complete common-coordinate concentration**.

### 2.3 Two-bank Fresnel theorem

Source:

`yspennstate/math-open-problems@0b5cf04790e5927df0efed8811a2a1295006e141`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260922T135910Z-fleet01-B13-qform-r13/REPORT.md`.

If `A=R Lambda R^T` has exact rank three, `R^T R=I_3`, and two disjoint original-coordinate banks `G,H` have positive-definite frame covariances `S_G,S_H`, then for arbitrary independent cap-one input densities,

`||p_Q||_infinity <= 6 |det Lambda|^(-1/3) (det S_G det S_H)^(-1/6)`.

The density is continuous in this scope. This is the density theorem applied to the new bank inequality below.

## 3. Nested-heavy coordinates and exact pair laws

Write

`A=R Lambda R^T`, `R^T R=I_3`,

and choose the nested-heavy rows

`r_i=sqrt(c)e1`,  `c>1/2`,

`r_j=rho e1+sqrt(h)e2`,  `h>1/2`.

For residual indices `k` write

`r_k=a_k e1+b_k e2+z_k e3`.

Parseval gives

`sum b_k^2 = B:=1-h`, `sum z_k^2=1`, `sum b_k z_k=0`.

Put

`s=h+rho^2`,
`beta=rho^2+h(1-c)`,
`u_k=(sqrt(h)a_k-rho b_k)/sqrt(s)`,
`U=sum u_k^2=beta/s`,
`d_*=max_k z_k^2`.

When `B,beta>0`, define normalized planar profiles

`x_k=b_k/sqrt(B)`, `y_k=u_k/sqrt(U)`.

Then

`sum x_k^2=sum y_k^2=sum z_k^2=1`,
`sum x_k z_k=sum y_k z_k=0`.

For every residual unordered pair `{k,l}`, define the genuine physical Pluecker weights

`p_{kl}=det(r_i,r_k,r_l)^2=c(b_k z_l-z_k b_l)^2`,

`q_{kl}=det(r_j,r_k,r_l)^2=s(u_k z_l-z_k u_l)^2`.

Their total masses are

`alpha=sum_{k<l}p_{kl}=cB`,

`beta=sum_{k<l}q_{kl}=rho^2+h(1-c)`.

The fleet02/B13 incidence identities read

`sum_{l!=k}p_{kl}=alpha(x_k^2+z_k^2)`,

`sum_{l!=k}q_{kl}=beta(y_k^2+z_k^2)`.

## 4. New theorem: profile overlap controls a disjoint pair of full-rank banks

Define the squared-profile overlap

`Theta := sum_k x_k^2 y_k^2`,

and the one-orientation disjoint residual pair mass

`M := sum_{ {k,l} cap {m,n}=empty } p_{kl} q_{mn}`.

### Theorem 4.1 — `QFORM-RANK3-PROFILE-OVERLAP-BANK-v1`

For `B,beta>0`,

`boxed( M >= alpha beta (1-Theta-3d_*) ).`                 (4.1)

Whenever the right side is positive, `Q=X^TAX` has a bounded continuous density and

`boxed( ||p_Q||_infinity`
` <= 6*2^(2/3) [alpha beta (1-Theta-3d_*)]^(-1/6) ).`      (4.2)

Under the target normalization `|lambda_j|>=1`, no additional spectral factor appears.

#### Proof of (4.1)

Normalize the pair weights to probability laws

`P(E={k,l})=p_{kl}/alpha`,

`P(F={m,n})=q_{mn}/beta`,

with `E,F` independent. The incidence identities give

`P(k in E)=x_k^2+z_k^2`,

`P(k in F)=y_k^2+z_k^2`.

Therefore, by the union bound for the event that the two random residual pairs intersect,

`1-M/(alpha beta)`
` = P(E cap F != empty)`
` <= sum_k P(k in E)P(k in F)`
` = sum_k (x_k^2+z_k^2)(y_k^2+z_k^2)`
` = Theta + sum x_k^2 z_k^2 + sum y_k^2 z_k^2 + sum z_k^4`
` <= Theta+3d_*`,

because each of the three probability profiles has total mass one and `max z_k^2=d_*`. This proves (4.1).

#### Proof of (4.2): actual application of the peer bank theorem

Color only the residual physical coordinates independently red/blue with probability `1/2`, while forcing `i` into bank `G` and `j` into bank `H`. By Cauchy--Binet,

`det S_G >= sum_{ {k,l} red } p_{kl}`,

`det S_H >= sum_{ {m,n} blue } q_{mn}`.

A disjoint residual edge pair contributes to their product with probability exactly `1/16`; an intersecting edge pair cannot contribute because a common physical coordinate cannot be both colors. Hence

`E[det S_G det S_H] >= M/16`.

Some deterministic partition therefore satisfies

`det S_G det S_H >= M/16`.

Apply the completed two-bank Fresnel theorem. Since `|det Lambda|>=1`,

`||p_Q||_infinity`
` <= 6(M/16)^(-1/6)`
` = 6*2^(2/3) M^(-1/6)`.

Combining with (4.1) proves (4.2). The peer theorem supplies a continuous density in this branch. QED.

### Corollary 4.2 — fixed quantitative collar

If for some `eta,epsilon>0`

`c<=1-eta`, `h<=1-eta`,

and

`Theta+3d_* <= 1-epsilon`,

then `alpha>=eta/2`, `beta>=eta/2`, and therefore

`boxed( ||p_Q||_infinity <= 12 eta^(-1/3) epsilon^(-1/6) ).`  (4.3)

For example, if `c,h<=7/8` and `Theta+3d_*<=1/2`, then

`||p_Q||_infinity <= 6*8192^(1/6)`
` = 26.9390891594...`.

This bound is dimension-free and makes no assumption on support fragments or their separation.

## 5. Main structural payoff: half-concentration upgrades to complete common-coordinate concentration

The previous fleet03/B13 theorem proved that any nested-heavy exact-rank-three sequence with unbounded density norm must satisfy

`d_* ->0`, `Delta->0`,

where `Delta=(1-c)(1-h)-rho^2`. The completed disjoint-exterior theorem also forces `D0->0`, where `D0` is the ordered disjoint triple mass. Since `D0>=2M`, necessarily `M->0`.

Now suppose the sequence stays away from leverage one: for some fixed `eta>0`, eventually

`c,h <=1-eta`.

Then `alpha beta>=eta^2/4`. From (4.1),

`1-Theta-3d_* <= M/(alpha beta) <= D0/(2alpha beta) ->0`.

Thus

`boxed(Theta ->1).`                                           (5.1)

This is much stronger than the preceding `1/2` incidence forcing.

Choose `k` maximizing `y_k^2`. Since

`Theta=sum x_l^2 y_l^2 <= max_l y_l^2`,

we have `y_k^2>=Theta`. Also

`Theta <= x_k^2 + sum_{l!=k}y_l^2 <= x_k^2 +1-Theta`,

so

`x_k^2 >= 2Theta-1`.

Consequently the **same physical residual coordinate** satisfies

`boxed(y_k^2 ->1, x_k^2 ->1, z_k^2<=d_*->0).`                (5.2)

The remaining residual planar mass vanishes. Indeed,

`sum_{l!=k} b_l^2 = B(1-x_k^2)->0`,

`sum_{l!=k} u_l^2 = U(1-y_k^2)->0`.

Since

`a_l=(sqrt(s)u_l+rho b_l)/sqrt(h)`

and `h>1/2`, it follows that

`sum_{l!=k} a_l^2 ->0`.                                      (5.3)

At the same time `sum z_l^2=1` and `z_k^2->0`. Thus, after removing the three physical rows `i,j,k`, the residual spectral-frame covariance becomes asymptotically supported only on the transverse line `Re3`.

### Corollary 5.1 — terminal geometry away from leverage one

Every putative unbounded nested-heavy exact-rank-three sequence has a subsequence in one of the following source-valid geometries:

1. `c->1` or `h->1` (leverage-one boundary); or
2. away from leverage one, three physical rows `i,j,k` carry asymptotically all planar spectral mass, while every remaining physical row is asymptotically transverse and the transverse variance remains diffuse (`d_*->0`).

The exact endpoint of alternative 2 has at most four projective spectral-row directions (`i`, `j`, `k`, and the transverse bank), and is therefore already covered by `QFORM-RANK3-FINITE-PROJECTIVE-BANKS-v1` with

`||p_Q||_infinity <= 91.8347018391...`.

The genuinely unpaid issue is **uniform stability of that four-direction endpoint under arbitrarily small planar leakage when the one-dimensional input laws have no support or moment control**. Small frame coefficients cannot simply be discarded: the inputs may have arbitrarily remote fragmented support.

## 6. Strong finite collar consequence

The profile theorem also gives an explicit near-total version. If `c,h<=1-eta`,

`d_*<=1/64`, and `D0<=eta^2/64`,

then `alpha beta>=eta^2/4` and

`Theta >= 1-3/64-(D0/(2 alpha beta)) >= 59/64`.

Choose `k` maximizing `y_k^2`. Then

`y_k^2 >=59/64`,

`x_k^2 >=2(59/64)-1=27/32`,

`z_k^2<=1/64`.

Thus

`b_k^2 >= (27/32)(1-h) >=27 eta/32`,

and, since `U=beta/s>=beta>=eta/2`,

`u_k^2 >= (59/64)U >=59 eta/128`.

This improves the earlier fixed collar from merely macroscopic third-row planar mass to near-total capture of **both** surviving normalized planar variance profiles by one common physical coordinate.

## 7. Exact geometric product-set implication

Let `J` be an interval and `E_1,...,E_n` arbitrary measurable sets of measure one. In every branch satisfying (4.1) with positive right side, apply (4.2) to the independent indicator inputs `X_i~1_{E_i}` to get

`|{x in prod_i E_i : x^T A x in J}|`
` <= 6*2^(2/3)[alpha beta(1-Theta-3d_*)]^(-1/6)|J|`.

The exact bang-bang theorem at commit `604a080...` then lifts this **same slab constant with zero loss** to every admissible independent product density. No single-interval, bounded-support, bounded-diameter, or bounded-fragment extremality is assumed.

## 8. Deterministic exact check

For the rational Parseval model

`c=h=3/5`, `rho=0`,

one residual `e1` row and one residual `e2` row each have squared weight `2/5`, while four transverse rows each have `z_k^2=1/4`. Then

`alpha=beta=6/25`, `Theta=0`, `d_*=1/4`.

The theorem gives

`M >= (6/25)^2(1-3/4)=9/625`.

The exact disjoint one-orientation mass is actually

`M=12(3/50)^2=27/625`,

so the bound is valid with a factor-three safety margin. The resulting bank-product lower bound from the theorem is `9/10000`, and the associated density constant is `19.3097876921...`. A deterministic checker in this run verifies these rational identities and the explicit collar constant.

## 9. Status and next unpaid implication

**Proved here:** the profile-overlap lower bound (4.1), the direct two-bank continuous-density estimate (4.2), and the resulting complete common-coordinate concentration theorem (5.2)-(5.3) for any putative unbounded nested-heavy rank-three sequence away from leverage one.

**Not proved:** stability of the four-direction endpoint under tiny planar leakage for arbitrary fragmented cap-one laws; the leverage-one boundary in full generality; arbitrary additional spectral directions; or the full owner conjecture.

The first B13 unpaid implication is now:

> **`QFORM-RANK3-FOUR-DIRECTION-STABILITY-COLLAR-v1` (OPEN).** Prove a dimension-free slab bound in the source-valid collar where three original coordinates carry nearly all planar spectral mass and the remaining independent coordinates form a high-cardinality transverse bank with arbitrarily small but nonzero planar leakage, without any support/moment assumption and without conditioning on a nonphysical variable with uncontrolled conditional density.

A successful theorem here would close the non-leverage-one terminal geometry left by the nested-heavy sequence. The leverage-one boundary and arbitrary extra spectrum would still have to be joined to the full target.

**Full QFORM status: OPEN / NOT PROVED.**
