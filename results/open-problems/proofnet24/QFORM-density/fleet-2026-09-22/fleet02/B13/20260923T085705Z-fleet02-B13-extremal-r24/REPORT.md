SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T08:57:05Z.
attacking: simultaneous finite-family purification and a cut-free higher-exterior-volume obstruction, then scalar-Schur descent to bordered high-order volume.

# fleet02/B13 — finite-family product purification and cut-free higher-volume obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Extremal product laws`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING REDUCTION + TARGET-LEVEL OBSTRUCTIONS / FULL QFORM OPEN / CONTINUITY OPEN**

## 1. Exact target and first unpaid implication

The target remains: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove

`P(X^T A X in J) <= C |J|`

for one universal finite `C`, every interval `J`, or give a valid counterexample. No moment, support, connectedness, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is allowed. Continuity is separate.

The full target remains OPEN. The first unpaid implication after this run is

`QFORM-TWOHUB-LOW-HIGHER-EXTERIOR-CLOSURE-v1`:

> In the high-density/no-pivot survivor, combine the partner's cut-free scalar-Schur twohub/trihub packet with the forced absence of every substantial disjoint exterior order `r>=5` and every substantial scalar-bordered exterior order `r+1>=6`, while preserving the original-coordinate product law. Prove a dimension-free linear slab bound, or construct a genuine bounded-finite-union product-indicator counterexample.

The new point is that this remaining class is now simultaneously **low in all high-order disjoint exterior volume** and, whenever order-two residual currency is not already analytically paid, **concentrated on a physical twohub/trihub packet**. One cannot replace that joint structure by one good minor, a bounded physical core, or a small random quadratic perturbation.

## 2. Source-valid premises actually used

1. **Designated partner fleet03/B13, cut-free compiler.**  
   `yspennstate/math-open-problems@dd467574f6ba35d976c5ace6124aabb9575aa3f6`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T063628Z-fleet03-B13-qform-r22/REPORT.md` and `POSTREFRESH_ADDENDUM.md`.

   For a finite matrix `S` on one physical index set, define

   `D_m^perp(S)=sum_{R,C: |R|=|C|=m, R cap C=empty} det S[R,C]^2`.

   A fair random partition `V=L disjoint_union Rside` satisfies

   `E e_m(S[L,Rside]^T S[L,Rside]) = 4^(-m) D_m^perp(S)`.        (2.1)

   Hence one ORIGINAL-coordinate cut has `e_m >=4^(-m)D_m^perp`.

   For an ORIGINAL scalar pivot `a=A_kk!=0`, with full scalar Schur complement

   `S=A_{-k,-k}-a^(-1)A_{-k,k}A_{k,-k}`,                         (2.2)

   the complete bordered energy satisfies exactly

   `B_{m+1,k}^perp(A)=a^2 D_m^perp(S)`.                           (2.3)

   The post-refresh partner alternative says, for `B_{3,k}^perp>0`, either

   `||p_Q||_infinity <24.011 (|a|^2 B_{3,k}^perp)^(-1/8)`,       (2.4)

   or a physical pivot-row-column trihub captures more than `1/128` of `B_{3,k}^perp`, with at most two row hubs and two column hubs in the actual cut provenance.

2. **Required pinned Claude/Fourier package.**  
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

   Its proved higher-volume theorem says: for an ORIGINAL-coordinate disjoint cross block `M=A[I,J]`, set

   `Z_r=e_r(M^T M)`.

   For every integer `r>=5`, taking the admissible exponent `q=2` in the general D_r estimate gives, with no marginal condition,

   `||p_Q||_infinity
      <= sqrt(2e) * r/(r-4) * Z_r^(-1/(2r)).`                    (2.5)

   All same-side quadratic blocks, outside couplings, and affine terms are retained. In particular, at `r=5` the constant is `5 sqrt(2e)=11.6582199079856...`.

3. **No-attainment product purification.**  
   `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5/REPORT.md`.

   Its Corollary 2.2 proves equality of the supremum of one bounded product kernel over arbitrary cap-one marginals with the supremum over unit-measure product indicators of bounded finite unions of intervals. It uses finite mixtures/L1 approximation and asserts neither an optimizer nor interval extremality.

The live corrections prohibiting bounded-diameter localization, a fixed fragment count, post-rotation independence, arbitrary-joint rank-three coarea, worst conditional-density moments, and one-good-minor extraction are respected throughout.

## 3. Finite-family product purification

The single-kernel purification above is enough for any one slab. For gluing structural alternatives it is useful to preserve a finite battery of bounded tests with one and the same product-indicator law.

### Theorem 3.1 — `QFORM-FINITE-FAMILY-PRODUCT-PURIFICATION-v1`

Let `K_1,...,K_N:R^n -> C` be bounded measurable kernels. Let `f_i` be probability densities satisfying `0<=f_i<=1`. For every `epsilon>0` there exist bounded finite unions of intervals `E_i subset R`, each with `|E_i|=1`, such that simultaneously for every `ell=1,...,N`,

`| int K_ell(x) prod_i f_i(x_i) dx
   - int_{prod_i E_i} K_ell(x) dx | < epsilon`.                  (3.1)

No maximizing product set is asserted.

#### Proof

**Step 1: compactify each marginal in L1 without changing the cap or mass.**

Fix one `f`. Choose `R` so that

`delta=int_{|x|>R} f(x) dx`

is as small as desired. Pick a bounded interval `I` disjoint from `[-R,R]` with length `delta`, and set

`g=f 1_{[-R,R]}+1_I`.

Then `0<=g<=1`, `int g=1`, `g` has bounded support, and

`||f-g||_1 <= int_{|x|>R}f + |I| =2delta`.                       (3.2)

Doing this in every coordinate and using the telescoping product estimate

`|| prod_i f_i-prod_i g_i ||_1 <= sum_i ||f_i-g_i||_1`           (3.3)

makes the error of every bounded `K_ell` arbitrarily small.

**Step 2: purify one coordinate while approximately preserving all N tests.**

Fix the other current marginals and let `g` be the current compactly supported marginal in coordinate `i`. For each `ell` define its bounded measurable partial expectation

`h_ell(x)=int K_ell(x,x_{-i}) prod_{j!=i} g_j(x_j) dx_{-i}`.      (3.4)

Let `S` be a bounded measurable set containing the support of `g`. Since `S` has finite Lebesgue measure, choose simple functions `s_ell` on one common finite measurable partition `S=C_1 disjoint_union ... disjoint_union C_M` such that

`||h_ell-s_ell||_{L1(S)}<eta`                                    (3.5)

for every `ell`.

For each cell choose a measurable subset `F_j subset C_j` with

`|F_j|=int_{C_j} g(x)dx`;                                        (3.6)

this is possible because Lebesgue measure is nonatomic and `0<=g<=1`. Put `F=union_j F_j`. Then `|F|=1`, and because every `s_ell` is constant on each cell,

`int_F s_ell = int_S g s_ell`.                                   (3.7)

Therefore

`|int_F h_ell-int g h_ell|
 <= int_S |h_ell-s_ell| (1_F+g)
 <=2 eta`.                                                       (3.8)

Replace `g_i` by `1_F`. Repeat this for coordinates `i=1,...,n`, choosing the successive `eta` values so that the accumulated error over all coordinates is below the desired budget. At no point is a threshold set or maximizer used.

**Step 3: make every purified factor a finite union of intervals.**

Every bounded measurable set of finite measure can be approximated in symmetric difference by a bounded finite union of intervals. Approximate each resulting unit-measure `F_i`; if the approximating union has measure slightly different from one, trim or add a sufficiently short interval to restore measure exactly one. Thus obtain bounded finite unions `E_i`, `|E_i|=1`, with arbitrarily small `|E_i triangle F_i|`. Again

`||1_{prod E_i}-1_{prod F_i}||_1
 <=sum_i |E_i triangle F_i|`,                                   (3.9)

so all finitely many bounded kernels change by arbitrarily little. Combining Steps 1-3 proves (3.1). QED.

### Corollary 3.2 — finite Pareto transfer

For any continuous function `Phi:C^N->R`, every supremum depending only on the finite vector

`( E K_1(X),...,E K_N(X) )`

has the same closure of attainable values over cap-one product laws as over bounded-finite-union unit product indicators. In particular, a strict simultaneous violation of finitely many bounded slab/test inequalities transfers to one common product-indicator law with arbitrarily small loss.

This is deliberately a **finite-family approximation theorem**. It does not purify countably many tests at once and does not produce an attained global bathtub optimizer.

## 4. Cut-free higher exterior-volume theorem

The pinned D_r theorem (2.5) is cut-dependent only through the chosen original-coordinate cross block. The partner's random-cut identity removes that choice before any reciprocal determinant is taken.

### Theorem 4.1 — `QFORM-CUTFREE-DR-v1`

For every integer `r>=5`, define

`D_r^perp(A)
 =sum_{R,C: |R|=|C|=r, R cap C=empty} det A[R,C]^2`.              (4.1)

If `D_r^perp(A)>0`, then for arbitrary independent cap-one inputs, and also with arbitrary affine terms added to the quadratic form,

`boxed:
 ||p_Q||_infinity
 <= C_r [D_r^perp(A)]^(-1/(2r)),
 C_r=2 sqrt(2e) * r/(r-4).
`                                                                    (4.2)

#### Proof

Apply (2.1) to `S=A`. Some ORIGINAL-coordinate partition `V=L disjoint_union Rside` has

`Z_r=e_r(A[L,Rside]^T A[L,Rside])
    >=4^(-r)D_r^perp(A)`.                                       (4.3)

Apply the pinned theorem (2.5) to this actual cross block. Since

`(4^(-r))^(-1/(2r))=2`,                                          (4.4)

we get exactly (4.2). No random variable is rotated and no support information is used. QED.

At `r=5`,

`boxed:
 ||p_Q||_infinity
 <=10 sqrt(2e) [D_5^perp(A)]^(-1/10)
 =23.316439815971... [D_5^perp(A)]^(-1/10).
`                                                                    (4.5)

### Corollary 4.2 — geometric sublevel-set form

For bounded finite-union sets `E_i` of measure one and every interval `J`,

`|{x in prod_i E_i: x^T A x in J}|
 <=C_r [D_r^perp(A)]^(-1/(2r)) |J|`.                             (4.6)

Theorem 3.1 transfers every fixed finite family of such slab bounds back to arbitrary cap-one product laws with zero loss in the limiting constant. Independently, the source theorem already has arbitrary-law scope.

### Corollary 4.3 — necessary obstruction for any high-density witness

If a slab witness has ratio

`R_0=P(Q in J)/|J|`,                                               (4.7)

then for every `r>=5`,

`boxed:
 D_r^perp(A) <= (C_r/R_0)^(2r).
`                                                                    (4.8)

Thus along any hypothetical counterexample sequence with `R_0 -> infinity`, **every fixed disjoint exterior order `r>=5` tends to zero quantitatively**. This is stronger than selecting one cut or one small singular value: it is a complete matrix-only sum over all disjoint `r x r` physical minors.

## 5. Scalar-Schur descent: bordered higher-volume theorem

The cut-free estimate can also be inserted after a genuine original scalar square, producing a new family of source-valid scalar-bordered exits.

Fix an ORIGINAL coordinate `k` with

`a=A_kk !=0`.                                                      (5.1)

Write the scalar completion

`Q=a (X_k+a^(-1)c^T Z)^2 + R(Z)`,                                (5.2)

where the quadratic part of `R` is the full Schur complement `S` in (2.2). The coordinates of `Z` remain the original independent variables.

We first record the elementary transducer used below.

### Lemma 5.1 — bounded density pays the half-Riesz kernel

If `Y` has probability density `p` with `||p||_infinity<=M`, then

`sup_s E |Y-s|^(-1/2) <=2 sqrt(2M)`.                              (5.3)

#### Proof

For every `u>0`,

`P(|Y-s|<u^(-2)) <=min(1,2M u^(-2))`.

Layer cake gives

`E|Y-s|^(-1/2)
 =int_0^infinity P(|Y-s|<u^(-2))du
 <=int_0^infinity min(1,2M/u^2)du
 =2sqrt(2M)`. QED.                                                (5.4)

The standard one-coordinate square peel from the pinned Fourier package gives

`||p_Q||_infinity <= |a|^(-1/2) H_{1/2}(R)`,                     (5.5)

where `H_{1/2}(R)=sup_s E|R-s|^(-1/2)`.

### Theorem 5.2 — `QFORM-SCALAR-BORDERED-HIGHER-EXTERIOR-v1`

For every integer `r>=5`, if `a=A_kk!=0` and `B_{r+1,k}^perp(A)>0`, then

`boxed:
 ||p_Q||_infinity
 <= S_r ( |a|^(2(r-1)) B_{r+1,k}^perp(A) )^(-1/(4r)),
 S_r=4(2e)^(1/4) sqrt(r/(r-4)).
`                                                                    (5.6)

#### Proof

By the partner identity (2.3),

`D_r^perp(S)=B_{r+1,k}^perp(A)/a^2`.                              (5.7)

Apply Theorem 4.1 to the residual `R`:

`||p_R||_infinity
 <=C_r [D_r^perp(S)]^(-1/(2r))=:M`.                              (5.8)

Then Lemma 5.1 and (5.5) yield

`||p_Q||_infinity
 <=2sqrt(2C_r) |a|^(-1/2) [D_r^perp(S)]^(-1/(4r)).               (5.9)

Since

`2sqrt(2C_r)=4(2e)^(1/4)sqrt(r/(r-4))=S_r`                       (5.10)

and substituting (5.7) changes the scalar power to

`|a|^(-1/2+1/(2r))=|a|^(-(r-1)/(2r))`,                           (5.11)

formula (5.6) follows. QED.

For `r=5`,

`boxed:
 ||p_Q||_infinity
 <=13.657654210287...
   ( |A_kk|^8 B_{6,k}^perp(A) )^(-1/20).
`                                                                    (5.12)

Therefore a slab witness of ratio `R_0` forces, for every nonzero original scalar pivot and every `r>=5`,

`boxed:
 |A_kk|^(2(r-1)) B_{r+1,k}^perp(A)
 <= (S_r/R_0)^(4r).
`                                                                    (5.13)

This does not compare `A` to a nearby matrix as a random quadratic variable; the Schur remainder is treated exactly, so arbitrary translations, fragmentation, and unbounded supports cause no perturbative gap.

## 6. Actual application to the designated partner's twohub survivor

The partner's strongest current order-two cut-free alternative (2.4) says that for each nonzero pivot `k` with `B_{3,k}^perp>0`, either the output is already paid or one physical pivot-row-column packet captures more than `B_{3,k}^perp/128`.

Combine this with (4.8) and (5.13). A hypothetical sequence with slab ratios `R_0 -> infinity` must satisfy simultaneously:

1. for every fixed `r>=5`, `D_r^perp(A)=O(R_0^(-2r))`;             (6.1)
2. for every nonzero physical pivot `k` and fixed `r>=5`,
   `|A_kk|^(2(r-1)) B_{r+1,k}^perp(A)=O(R_0^(-4r))`;             (6.2)
3. whenever `|A_kk|^2 B_{3,k}^perp(A)` is large enough that the paid bound (2.4) would fall below `R_0`, the paid branch is impossible, so the `>1/128` twohub/trihub structural branch must occur.                                                     (6.3)

This is a genuine new restriction on the partner's unresolved class: **large order-two bordered currency may survive only inside a matrix whose complete disjoint exterior orders five and above, and scalar-bordered orders six and above, have already collapsed at explicit powers of the desired slab ratio.**

The conclusion is not a full proof. In particular, `D_5^perp(A)=0` does not imply a uniformly bounded physical core: a diffuse exact-rank-three frame has every fifth minor zero while every fixed small principal block may be poorly conditioned. This is consistent with the live correction refuting a universal one-good-principal-block / rank-three-cross-cut dichotomy.

The successor must exploit the **joint** low-higher-exterior + twohub/trihub structure without replacing the original product law by generic low-dimensional marginal caps and without interpreting a small coefficient tail as a small random quadratic perturbation.

## 7. Extremal-law meaning and counterexample consequences

Theorem 3.1 means that any strict finite package of bounded geometric slab/test constraints can be transferred, with arbitrarily small loss, to one product law of the form

`prod_i 1_{E_i}(x_i),  |E_i|=1`,                                 (7.1)

where each `E_i` is a bounded finite union of intervals. There is no universal bound on the number of components or on their diameter. Thus if the remaining implication in Section 6 is false, one may search for a counterexample sequence **inside this finite-union product class**, provided each finite stage certifies the actual three-large-eigenvalue condition and the strict violation before purification.

Conversely, proving a linear geometric slab bound uniformly for all such product sets, with constants depending only on the matrix currencies displayed above, transfers to all arbitrary cap-one product laws by the same approximation mechanism.

The required pinned `COUNTEREXAMPLE_SEARCH.md` reports no valid counterexample in its tested families, but those numerics are not used as proof here.

## 8. Status

Proved in this run:

- `QFORM-FINITE-FAMILY-PRODUCT-PURIFICATION-v1`: finite simultaneous bounded-test purification to bounded finite-union unit product indicators, without attainment;
- `QFORM-CUTFREE-DR-v1`: for every `r>=5`, the no-marginal Fourier D_r theorem plus the partner random-cut compiler yields the cut-free matrix-only bound (4.2);
- `QFORM-SCALAR-BORDERED-HIGHER-EXTERIOR-v1`: exact scalar-Schur descent gives the bordered family (5.6), including the explicit order-six constant (5.12);
- a sharpened necessary normal form for any diverging counterexample sequence, combining those high-order collapses with the designated partner's current twohub/trihub alternative.

Not proved:

- the full universal QFORM bound;
- the twohub/low-higher-exterior closure stated in Section 1;
- the zero-diagonal chamber by this scalar descent alone;
- continuity of the full output density.

Independent end-to-end review status: **not independently reviewed**.
