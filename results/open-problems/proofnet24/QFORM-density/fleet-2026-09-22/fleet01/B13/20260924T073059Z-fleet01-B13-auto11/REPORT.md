SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-24T07:30:59.277381Z.
attacking: repair exact witnesswise product purification on the noncompact line, then strengthen the partner diameter escape to an on-slab positive-mass rough-tail obstruction.

# fleet01/B13 — exact purification v2 and double-slab difference-bank escape

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T073059Z-fleet01-B13-auto11`  
Control revision: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **ESSENTIAL SUPPORTING STEPS PROVED / FULL QFORM OPEN / CONTINUITY OPEN**.

No rotation of the independent variables is used. No pointwise law-uniform quadratic oscillatory decay, arbitrary-joint coarea gate, projection-density shortcut, interval extremality, centered-uniform extremality, bounded support diameter, or uniform fragment-count assumption is used.

The completed designated-partner input actually used is fleet02/B13 r11:

- `yspennstate/math-open-problems@c8bbb166c448ccd194451b47524b13d5de3eaed5`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260924T065522Z-fleet02-B13-qform-r11/REPORT.md`.

Its theorem `QFORM-TRANSLATION-INVARIANT-DIAMETER-ESCAPE-v1` pays a decomposition `A=M+F` whenever every affine `M`-form has a uniform density cap `C_M`, and shows that coefficient-small `F` cannot be activated merely by translating compact product factors. The same report records, in the current rank-one plus four-diagonal survivor,

`M=D_C+lambda_1 vv^T`, `|C|<=4`,

and for all sufficiently high-ratio witnesses with `s_3(M)>=1/2`, every affine `M`-form is paid by

`C_M = 500 e * 5 * (8+log 5) = 65302.90114768759...`.

It also retains

`F=E_sep+E_ent`, `||E_sep||op<=C_D/rho`, `C_D=2sqrt(30 pi)=19.41625912555699...`,

with `E_sep` diagonal off the named center set and `E_ent=lambda_2 ww^T` a retained secondary rank-one carrier.

The existing nonattained bathtub supremum theorem used below is source-pinned at

- `yspennstate/math-open-problems@df6d00a11422f16763e8bccccc6bada6e4949a83`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260923T121154Z-fleet04-B13-nonattained-bathtub-r1/REPORT.md`.

It proves equality of the one-coordinate fractional and indicator suprema without assuming threshold attainment.

## 1. Repair of exact witnesswise purification on the noncompact line

An earlier fleet01/B13 proof of exact witnesswise purification used the sentence that the top-level rearrangement value is attained by a measure-one set on the noncompact line. That sentence is not valid in general: the supremum can be nonattained. The theorem itself is nevertheless true. The following argument repairs the proof without asserting global attainment.

### Lemma 1 — `QFORM-ONECOORD-EXACT-PURIFICATION-v2`

Let `h:R->[0,M]` be measurable and let `f` satisfy `0<=f<=1`, `int f=1`. Then there is a measurable set `E`, `|E|=1`, such that

`int_E h >= int f h`.                                                   (1.1)

#### Proof

Let

`S_f = sup_{0<=g<=1, int g=1} int g h`,
`S_E = sup_{|E|=1} int_E h`.

The nonattained bathtub argument gives `S_f=S_E=:S`.

If `int f h<S`, the definition of the indicator supremum immediately supplies a set `E` of measure one with `int_E h>int f h`. No optimizer is needed.

It remains only to treat the equality case `int f h=S`, so `f` itself is a fractional maximizer. Put

`U={x:f(x)<1}`, `V={x:f(x)>0}`,

and define

`alpha=ess sup_U h`, `beta=ess inf_V h`.

We claim `alpha<=beta`. Otherwise choose numbers `beta<a<b<alpha`. Then both

`A=U cap {h>b}` and `B=V cap {h<a}`

have positive measure. Since

`U=union_k {f<=1-1/k}`, `V=union_l {f>=1/l}`,

there are positive-measure subpieces on which `f` stays a fixed distance from the corresponding cap. By sigma-finiteness and non-atomicity choose finite subpieces `A' subset A`, `B' subset B` of equal positive measure and choose `epsilon>0` so that

`f+epsilon 1_{A'}-epsilon 1_{B'}`

still lies in `[0,1]` and has the same total mass. Its objective is larger by at least

`epsilon |A'| (b-a)>0`,

contradicting maximality.

Choose `c in [alpha,beta]`. Then, up to null sets,

`f=1 on {h>c}`, `f=0 on {h<c}`.                                     (1.2)

Hence

`1=|{h>c}| + int_{h=c} f`,

so `|{h>c}|<=1<=|{h>=c}|`. By non-atomicity choose

`L subset {h=c}`, `|L|=1-|{h>c}|`,

and set `E={h>c} union L`. Then `|E|=1` and, using (1.2),

`int_E h = int f h = S`.

This proves (1.1). `QED`

The point is that threshold attainment is needed only if the given `f` itself attains the supremum; in that equality case the exchange argument forces a genuine threshold structure and therefore an indicator maximizer exists. If the supremum is nonattained, every feasible `f` lies strictly below it and an indicator can simply be chosen above the value of that particular witness.

### Theorem 2 — `QFORM-EXACT-SEQUENTIAL-BATHTUB-PURIFICATION-v2`

Let `K:R^n->[0,M]` be bounded, nonnegative and measurable. For every product of cap-one mass-one densities `f_i`, there are measurable sets `E_i`, `|E_i|=1`, with

`int K(x) prod_i 1_{E_i}(x_i) dx >= int K(x) prod_i f_i(x_i) dx`.       (1.3)

#### Proof

With all factors except coordinate `i` fixed, integrate them out and obtain a bounded nonnegative one-variable function `h_i`. Apply Lemma 1 to replace the current factor by a measure-one indicator without decreasing the objective. Freeze that replacement and continue through the finitely many original coordinates. `QED`

For the QFORM slab kernel `K=1_{x^T A x in J}`, every actual cap-one product-law witness therefore has, for the **same A and the same J**, a unit-product-set witness with zero ratio loss. This remains a witnesswise statement only; it does not say the global supremum is attained, and it gives no interval, bounded-diameter, or bounded-fragment conclusion.

## 2. New theorem: on-slab rough-tail mass, uniform over translations

The partner's diameter theorem uses a support supremum. A very remote fragment of tiny measure can make a support diameter huge, so support width alone is not yet smoothing currency. The same affine-uniform hypothesis yields a stronger probability statement in which a positive amount of the **actual slab mass** must see the retained rough tail.

### Theorem 3 — `QFORM-AFFINE-CORE-ONSLAB-ROUGH-MASS-v1`

Let `X=(X_1,...,X_n)` have independent cap-one densities and let

`A=M+F`                                                        (2.1)

be symmetric. Assume that for this class of product laws, every affine `M`-form

`Z^T M Z+b^T Z+c`

has density at most `C_M`, uniformly in the deterministic `b,c` and under coordinatewise translations of the input laws.

Let `J` be an interval of length `ell`, put

`p=P{X^T A X in J}`, `a=(p-C_M ell)_+`.                         (2.2)

Then for **every** deterministic center `m in R^n`, with `Y=X-m`, one has

`P{ X^T A X in J, |Y^T F Y| > a/(4 C_M) } >= a/2`.             (2.3)

Consequently, if `F!=0`,

`P{ X^T A X in J, ||X-m||_2^2 > a/(4 C_M ||F||op) } >= a/2`.  (2.4)

#### Proof

Expand the actual form without rotating any random variables:

`X^T A X = Q_m(Y)+Y^T F Y`,

where

`Q_m(Y)=Y^T M Y+2(Am)^T Y+m^T A m`.                             (2.5)

The possibly enormous translation `m` appears only as an affine term in the paid `M`-core. For `s>=0`,

`{X^T A X in J, |Y^T F Y|<=s}`

is contained in

`{Q_m(Y) in J+[-s,s]}`.

The latter probability is at most `C_M(ell+2s)`. Therefore

`P{X^T A X in J, |Y^T F Y|>s} >= p-C_M(ell+2s)`.               (2.6)

If `a>0`, choose `s=a/(4C_M)`; the right side becomes `a/2`. If `a=0`, (2.3) is trivial. Equation (2.4) follows from

`|Y^T F Y|<=||F||op ||Y||_2^2`. `QED`

For a slab ratio `rho=p/ell` with `rho>=2C_M`, `a>=(rho ell)/2`, so (2.4) gives

`P{Q in J, ||X-m||_2^2 > rho ell/(8 C_M ||F||op)} >= rho ell/4`. (2.7)

If `||F||op<=C_F/rho`, then for every center `m`,

`P{Q in J, ||X-m||_2^2 > rho^2 ell/(8 C_M C_F)} >= rho ell/4`.  (2.8)

Unlike a diameter bound, (2.8) cannot be satisfied by an arbitrarily tiny remote fragment: at least a fixed fraction (asymptotically one half) of the excess slab mass itself lies beyond the displayed radius.

## 3. Apply fleet02/B13 r11 to an actual inequality

Use the partner normal form

`M=D_C+lambda_1 vv^T`, `|C|<=4`,
`F=E_sep+lambda_2 ww^T`, `||w||_2=1`,                         (3.1)

in the branch where `s_3(M)>=1/2`. The partner theorem supplies the affine-uniform cap

`C_M=500 e * 5 * (8+log 5)`.                                  (3.2)

The retained separable tail is diagonal off `C` and satisfies

`||E_sep||op<=C_D/rho`, `C_D=2sqrt(30 pi)`.                    (3.3)

For any center `m`, write

`R_C^2(m)=sum_{i notin C} |X_i-m_i|^2`,
`L_w(m)=sum_i |w_i| |X_i-m_i|`.                                (3.4)

Then

`|(X-m)^T F (X-m)|
 <= (C_D/rho) R_C^2(m) + |lambda_2| L_w(m)^2`.                 (3.5)

Combining (2.3) with (3.5) gives the **actual on-slab bank inequality**

`P{ Q in J,
     (C_D/rho) R_C^2(m)+|lambda_2|L_w(m)^2 > a/(4C_M) }
 >= a/2`,                                                       (3.6)

where `a=(rho-C_M)ell` when `rho>C_M`.

If `lambda_2=0`, the second term in (3.6) vanishes and only the radial alternative below can occur. If `lambda_2!=0`, then for every center `m`, at least one of the following two alternatives holds:

`P{Q in J, R_C^2(m) > a rho/(8 C_M C_D)} >= a/4`,              (3.7)

or

`P{Q in J, L_w(m)^2 > a/(8 C_M |lambda_2|)} >= a/4`.           (3.8)

For `rho>=2C_M`, this simplifies to

`P{Q in J, R_C^2(m) > rho^2 ell/(16 C_M C_D)} >= rho ell/8`,   (3.9)

or, when `lambda_2!=0`,

`P{Q in J, L_w(m)^2 > rho ell/(16 C_M |lambda_2|)} >= rho ell/8`. (3.10)

Numerically,

`16 C_M C_D = 20287008.805346165...`.                          (3.11)

If the retained carrier obeys the partner-recorded high-density estimate

`|lambda_2|<=K_ent rho^(-7/6)`,                                (3.12)

then the second branch becomes

`P{Q in J,
     L_w(m)^2 > rho^(13/6) ell/(16 C_M K_ent)}
 >= rho ell/8`.                                                 (3.13)

The stronger fleet02/B13 lower-bound bootstrap is source-pinned at
`yspennstate/math-open-problems@21a48883fa1152dac179f3f6ebe1725785793520`.
If its `|lambda_2|=O(rho^(-7/3))` estimate is invoked in the same chamber, the exponent in (3.13) improves from `13/6` to `10/3`.

Equations (3.9)-(3.13) are strictly stronger product-geometric currency than the support-width alternative in the partner handoff: the rough bank must be large on a positive amount of the **slab itself**, not merely somewhere in the support.

## 4. Independent-copy formulation and double-slab geometry

Let `X'` be an independent copy of `X`. Because Theorem 3 holds for every deterministic center, conditioning on `X'=x'`, applying it with `m=x'`, and averaging gives

`P{Q(X) in J,
   |(X-X')^T F (X-X')| > a/(4C_M)} >= a/2`.                    (4.1)

The coordinate differences

`U_i=X_i-X_i'`

are independent across `i`, and their densities satisfy

`g_i(u)=int f_i(x)f_i(x-u)dx <= ||f_i||_infty int f_i <=1`.    (4.2)

So the forced spread lives in a genuine independent cap-one difference bank.

There is a stronger version that puts **both copies in the slab**. Assume `p>0` and draw `X'` from an independent copy of `X` conditioned on `Q(X') in J`. Theorem 3 is uniform in the deterministic center, so averaging over this conditional center and then multiplying by `p` yields

`P{Q(X) in J, Q(X') in J,
   |U^T F U| > a/(4C_M)} >= p a/2`.                             (4.3)

On this event one automatically has the exact bilinear narrowness identity

`|U^T A (X+X')|=|Q(X)-Q(X')|<=ell`.                            (4.4)

Thus the surviving rough bank is present on a positive fraction of actual **pairs of slab points**, in the original product-pair coordinates used by valid decoupling.

For the partner split (3.1)-(3.3), (4.3) implies one of

`P{Q(X),Q(X') in J,
   sum_{i notin C} U_i^2 > a rho/(8C_M C_D)} >= p a/4`,         (4.5)

or, when `lambda_2!=0`,

`P{Q(X),Q(X') in J,
   (sum_i |w_i||U_i|)^2 > a/(8C_M|lambda_2|)} >= p a/4`.        (4.6)

For `rho>=2C_M`, since `a>=p/2` and `p=rho ell`, at least one of the two branches has probability at least `p^2/8`. Equivalently, **conditioned on both copies lying in the slab**, at least `1/8` of the pair mass satisfies either

`sum_{i notin C} U_i^2 > rho^2 ell/(16C_M C_D)`,               (4.7)

or

`(sum_i |w_i||U_i|)^2 > rho ell/(16C_M|lambda_2|)`.             (4.8)

If `lambda_2=0`, the radial alternative (4.7) holds. In the radial branch the conditional pairwise second moment is therefore bounded below by one eighth of the threshold, so whenever the corresponding moments are finite,

`sum_{i notin C} Var(X_i | Q(X) in J)
 >= rho^2 ell/(256 C_M C_D)`.                                  (4.9)

The variance identity here is the elementary independent-copy relation
`E[(Z-Z')^2]=2 Var(Z)` under the conditional slab law. If the moment is infinite, (4.9) is true in the extended sense.

This double-slab form closes the tiny-fragment loophole sharply: the separation is carried by a fixed fraction of **slab-pair mass**, not by exceptional support points.

## 5. Geometric product-set form with zero purification loss

Apply Theorem 2 to the slab indicator for the same `A,J`. Every arbitrary cap-one product witness of ratio `rho` has unit-measure sets `E_i` for which the product-set slab volume is at least `rho ell`.

Apply Theorem 3 to the uniform product law on those sets. In the partner normal form and `rho>=2C_M`, for every center `m`, either

`|{x in prod E_i : x^T A x in J,
    sum_{i notin C}(x_i-m_i)^2 > rho^2 ell/(16 C_M C_D)}|
 >= rho ell/8`,                                                 (5.1)

or, when `lambda_2!=0`,

`|{x in prod E_i : x^T A x in J,
    (sum_i |w_i||x_i-m_i|)^2 > rho ell/(16 C_M |lambda_2|)}|
 >= rho ell/8`.                                                 (5.2)

The double-slab formulation says more. If

`S={x in prod_i E_i : x^T A x in J}`, `|S|=p_E>=rho ell`,

then, with the same thresholds using the original lower ratio `rho`, at least one branch has pair-volume

`|{(x,x') in S x S : bank-separation threshold holds}| >= |S|^2/8`.   (5.3)

If `lambda_2=0`, the radial branch must hold. No global product-set optimizer or interval structure is asserted.

## 6. What is still open

The full QFORM conjecture is not proved here. The first unpaid implication is

`QFORM-DOUBLESLAB-DIFFERENCE-BANK-TO-SMOOTHING-v1`:

> use the fixed positive pair-mass in (4.7) or (4.8), together with the exact bilinear narrowness `|U^T A(X+X')|<=ell` and the independent cap-one provenance of the difference coordinates, to obtain a dimension-free smoothing/payment while retaining `E_sep` and the secondary carrier; or construct a genuine product-indicator counterexample sequence satisfying these double-slab separation obligations and the existing fifth-cross-volume collapse on every physical cut.

The remaining obstruction is no longer a support-radius artifact. It is an actual large independent difference bank carried by a fixed fraction of pairs inside the high-density slab. Essential boundedness remains OPEN; no global continuity conclusion is claimed.