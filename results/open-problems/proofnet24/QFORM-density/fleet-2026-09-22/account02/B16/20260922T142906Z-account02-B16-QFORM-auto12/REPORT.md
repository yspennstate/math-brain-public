# account02/B16 — zero-diagonal physical triple closure by product-log ridge averaging

**Run:** `20260922T142906Z-account02-B16-QFORM-auto12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `NEW SUPPORTING THEOREM + COMPLETED PARTNER APPLICATION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, live controls, and first unpaid implication

The full target remains open: for independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `X^T A X` has an essentially bounded density with one universal dimension/matrix/law-independent constant, or produce a valid target-level counterexample.

Fresh control was resolved through the authorized repository connector. The last pre-write control snapshot used here is `yspennstate/math-research-brain@d8fec50af1cc51a6f1ece33b468d979be8fb26c2`, owner revision `2026-09-22.5`. The live correction inbox at that snapshot has blob `337bc9adc6b8ed81d688dd32367c68c4b9b2a636`; in particular this proof respects `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`.

The completed assigned partner result actually used is **account03/B16** run `B16-20260922T135620Z-r11`, canonical mathematics `yspennstate/math-open-problems@1defc84f1bfd79994a103a6d683c887d9dead1e7`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/B16-20260922T135620Z-r11/REPORT.md`, report blob `d64c5e5cfc01bf3783cdcdeac2f03dd766bbda3d`. Its theorem `QFORM-ALL-SCHUR-PIVOT-PRODUCT-TRACE-v1` pays every invertible physical `3x3` principal block having a nonzero diagonal pivot, under arbitrary outside couplings. It explicitly leaves the all-zero-diagonal invertible triple to a two-coordinate pivot.

**First unpaid implication attacked here:** close that all-zero-diagonal physical triple without rotating the independent inputs and without replacing them by a bounded projection density.

## 2. A sharp enough envelope for a product of two cap-one variables

Let `U,V` be independent real variables with probability densities `f,g` satisfying `0<=f,g<=1`. For `w!=0`, the density of `UV` is

`h(w)=int f(u) g(w/u) du/|u|`.

Put `r=sqrt(|w|)` and split at `|u|=r`.

On `|u|>r`,

`int_{|u|>r} f(u)g(w/u)du/|u| <= int_{|u|>r} f(u)du/|u|`.

Among all cap-one probability densities the right side is maximized by filling the nearest available set of total length one, namely the two intervals adjacent to `+-r`. Hence

`int_{|u|>r} f(u)du/|u| <= 2 log(1+1/(2r))`.

On `|u|<=r`, use `v=w/u`; then `du/|u|=dv/|v|` and the region maps to `|v|>=r`, so exactly the same bound with `g` in place of `f` applies. Therefore

`h(w) <= 4 log(1+1/(2 sqrt(|w|)))`.                              (2.1)

Consequently the density of `2aUV`, for `a!=0`, obeys the translation-uniform envelope

`K_a(t):=(2/|a|) log(1+sqrt(|a|/(2|t|)))`, `t!=0`.                (2.2)

This logarithmic ridge is essential. Replacing it by a crude `|t|^(-1/2)` envelope would recreate a nonintegrable square-root/square interaction at the next coordinate.

## 3. Quadratic sublevel geometry pays the logarithmic ridge

For every real `tau`, every `d!=0`, and every `h>0`,

`|{z: |tau-d z^2|<h}| <= 4 sqrt(h/|d|)`.                         (3.1)

After scaling `|d|=1`: if the centered level is within `h` of zero, the set lies in an interval of radius `sqrt(2h)`; otherwise it is the union of two root neighborhoods and the difference-of-square-roots formula gives the displayed bound.

Define

`F(eta)=log(1+eta)+eta log(1+1/eta)`, `eta>0`.                    (3.2)

Let `Z` have any probability density bounded by one. For arbitrary affine `P(z)=d z^2+e z+c`, completing the square and translating `Z` preserve the density cap. Layer cake applied to (2.2) and (3.1) gives, uniformly in the target level `s`,

`int f_Z(z) K_a(s-P(z)) dz
 <= (2/|a|) F(eta),`                                              (3.3)

where

`eta=2 sqrt(2) sqrt(|a|/|d|)`.                                  (3.4)

Indeed, `K_a(r)>t` iff

`|r| < |a|/[2(exp(|a|t/2)-1)^2]`.

Thus its `z`-level set has Lebesgue measure at most

`eta/(exp(u)-1)`, `u=|a|t/2`.

Because `f_Z<=1` and has mass one, its probability is at most the minimum of this quantity and one. The remaining integral is exact:

`int_0^infinity min(1, eta/(e^u-1)) du
 = log(1+eta)+eta log(1+1/eta)=F(eta)`.                           (3.5)

No conditional density cap stronger than the original coordinate cap is assumed.

## 4. New theorem: every invertible all-zero-diagonal physical triple is locally paid

### Theorem 4.1 — `QFORM-ZERODIAG-TRIPLE-PRODUCT-TRACE-v1`

Let `X,Y,Z` be independent real variables with probability densities bounded by one. Let

`B = [[0,a,b],[a,0,c],[b,c,0]]`

be an invertible real symmetric matrix, so `abc!=0` and `det B=2abc`. Allow an arbitrary affine perturbation

`L(x,y,z)=alpha x+beta y+gamma z+delta`.

Then the quadratic polynomial

`Q_B=(x,y,z)B(x,y,z)^T+L(x,y,z)`

has an essentially bounded density. For each choice of edge called `a`,

`||p_{Q_B}||_infinity
 <= (2/|a|) F( 2|a|/sqrt(|bc|) ).`                                (4.1)

In particular, with

`C_off = 2^(4/3) F(2)
       = 2^(4/3) [log 3 + 2 log(3/2)]
       = 4.8117455951457755...`,

one has the symmetric determinant-only estimate

`boxed( ||p_{Q_B}||_infinity <= C_off |det B|^(-1/3) ).`          (4.2)

The conclusion is stable under arbitrary outside couplings when `B` is a physical principal block of a larger quadratic form: conditioning outside the triple creates only the permitted affine perturbation.

### Proof

Condition on `Z=z`. Set

`U_z = X + (c/a)z + beta/(2a)`,

`V_z = Y + (b/a)z + alpha/(2a)`.

For each fixed `z`, `U_z,V_z` remain independent translates of the original cap-one densities. Direct expansion gives

`Q_B = 2a U_z V_z + P(z)`,                                      (4.3)

where

`P(z)=-(2bc/a)z^2 + [gamma-(c alpha+b beta)/a]z
      +[delta-alpha beta/(2a)]`.                                 (4.4)

Thus the leading coefficient in (3.3) is `d=-2bc/a`. Apply (2.2) conditionally and average in `Z`. Formula (3.4) becomes

`eta=2|a|/sqrt(|bc|)`,

which is (4.1).

For (4.2), put `g=(|abc|)^(1/3)` and choose the largest of `|a|,|b|,|c|` as the edge called `a`; write `|a|=g x`, `x>=1`. Since `|bc|=g^2/x`, the right side of (4.1) equals

`(2/g) x^(-1) F(2 x^(3/2))`.                                    (4.5)

Now `F'(eta)=log(1+1/eta)`. Differentiating the factor in (4.5), with `eta=2x^(3/2)`, gives a sign proportional to

`-log(1+eta) + (eta/2) log(1+1/eta)`.                            (4.6)

For `eta>=2`, `eta log(1+1/eta)<1` while `log(1+eta)>=log 3>1/2`; hence (4.6) is strictly negative. The maximum over `x>=1` occurs at `x=1`, giving

`||p_{Q_B}||_infinity <= (2/g)F(2)`.

Finally `g=(|det B|/2)^(1/3)`, yielding (4.2). QED.

## 5. Exact application of the completed account03/B16 partner theorem

Combining Theorem 4.1 with account03/B16's completed `QFORM-ALL-SCHUR-PIVOT-PRODUCT-TRACE-v1` closes **every invertible physical `3x3` principal block locally**.

Let `B` be any invertible physical principal triple of an ambient symmetric matrix and condition on all outside original coordinates.

* If some diagonal entry `a=B_ii` is nonzero, account03/B16 proves

`||p_Q||_infinity <= 16 sqrt(15) (|a det B|)^(-1/4)`             (5.1)

for the indefinite Schur branch, while its incorporated completed account04/B18 dependency pays the definite Schur branch; the unified constant in (5.1) is valid in either case.

* If all three diagonal entries vanish, Theorem 4.1 gives

`||p_Q||_infinity <= 4.811746 |det B|^(-1/3)`.                   (5.2)

Thus the former local sign/pivot hole is gone. No rotation of the input variables, projected-coordinate independence, conditional-cap assumption, support bound, or moment hypothesis is used.

This is a supporting theorem, not the full conjecture: the spectral hypothesis does not force a single physical triple with determinant bounded below.

## 6. Why aggregate determinant mass still cannot simply average reciprocal local payments

The remaining obstacle is genuinely aggregate. Consider the exact-rank-three family on `3m` coordinates

`A_m = (J_m/m) direct_sum (J_m/m) direct_sum (-J_m/m)`.

Its nonzero spectrum is `{1,1,-1}`. Every invertible physical principal triple chooses exactly one coordinate from each block and has

`B_I=diag(1/m,1/m,-1/m)`, `|det B_I|=m^(-3)`, `|B_{ii}|=m^(-1)`.

There are `m^3` such triples, so their total absolute determinant mass is exactly one. Nevertheless the local scalar-pivot estimate (5.1) on every such triple is proportional to

`(|B_ii det B_I|)^(-1/4)=m`.                                     (6.1)

Therefore even determinant-normalized linear averaging of these local reciprocal estimates stays of order `m`, although the determinant mass itself is perfectly normalized. This is the same structural warning as the live `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` family: **independent coordinate banks must be aggregated before reciprocal-minor payment.** The new local theorem removes a missing branch; it does not justify averaging the resulting local constants.

## 7. Status and next implication

**Proved here:** an explicit source-valid local theorem for the all-zero-diagonal invertible physical triple, with arbitrary affine perturbations and determinant-only constant `4.811746 |det B|^(-1/3)`. Combined with the completed account03/B16 theorem, every invertible physical principal triple is now locally controlled under arbitrary outside couplings.

**Still open:** turn the three-large-eigenvalue hypothesis into a dimension-free global payment when all useful physical minors are small. Any successful bridge must aggregate original-coordinate banks/diffuse pieces before taking reciprocal local determinants; total third-minor mass alone does not control the linear average of (5.1). Arbitrary additional spectral components and all input-law quantifiers remain live.

No claim of a universal final QFORM constant, continuity for this new branch, novelty, or independent end-to-end review is made.
