# account03/B05 — nonzero coloop closure and full physical n=3 density theorem

**Run:** `20260922T184033Z-account03-B05-QFORM-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound  
**Fresh owner control at start:** revision `2026-09-22.11`, brain main `0d1639eb53505457bd534ed187089173498949fb`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TWO SUPPORTING THEOREMS / FULL QFORM OPEN`.

## 1. Exact target and first missing implication

The full target remains: for arbitrary dimension, arbitrary independent real input coordinates with one-dimensional probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound for the essential density of `X^T A X`, or give a target-valid counterexample. No Gaussian, support, moment, log-concavity, sign, or post-rotation independence assumption is made. Continuity remains a separate desired conclusion.

The preceding B05 run refuted the proposed normalized scalar worst-fiber bridge: `sup_b ||p_{Q3|Q'=b}||_infinity` can grow like `log m` in a four-dimensional target-valid product example. The lost quantity is the unnormalized scalar-fiber mass. Thus this run does not take any normalized fiber supremum.

The first local coarea debt inherited from the earlier B05 coloop classification is also very concrete. In the exact-rank-three plane-plus-singleton endpoint, the exceptional spectral direction is an untouched physical coordinate `X0`. The exact zero physical pivot `a=0` was already paid uniformly, and a minority-sign nonzero pivot was paid by square smoothing. The unpaid sign branch was a **nonzero majority-sign pivot**, with a near-zero deterioration still lurking.

This report proves two things:

1. `QFORM-COLOOP-NONZERO-HALF-RIESZ-v1`: **every nonzero coloop pivot is paid, with no sign restriction**. This closes the earlier majority-sign branch. The only local coloop debt is now the **uniform transition as `a -> 0`**, not the sign of `a`.
2. `QFORM-PHYSICAL-N3-ENDTOEND-v1`: the **entire original-coordinate dimension `n=3` target** is uniformly bounded, all signs and all rotations, by an explicit universal constant assembled from a scalar-pivot half-Riesz branch and a quantitatively forced indefinite physical-pair branch.

The second theorem is not the arbitrary-dimensional conjecture, but it removes the fully coupled three-coordinate endpoint that had remained open in the account04/B18 report.

## 2. Source-valid dependencies actually used

### 2.1 Orientation-free rank-two half-Riesz theorem

Canonical source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For `U^T U=I_2`, invertible symmetric `2 x 2` `Lambda`, arbitrary affine term `b`, and independent cap-one inputs,

`sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2)
 <=128 |det Lambda|^(-1/4)`.

When the affine term lies in `range(U)`, including `b=0`, the source gives the sharper constant

`16 sqrt(30) |det Lambda|^(-1/4)`.                                      (2.1)

A scoped independent review of this theorem was recorded by account03/B16. I use only the `b=0` case below.

### 2.2 Full-matrix indefinite physical-pair theorem

Canonical source:

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

If `s_3(A)>=s>0` and an ORIGINAL-coordinate `2 x 2` principal pair `B` is invertible indefinite, with

`D=|det B|`, `kappa=sigma_min(B)`,

then the complete supplied argument gives

`||p_Q||_infinity
 <=3*400^(1/3) (D^2 kappa s)^(-1/6)`.                                  (2.2)

All additional spectrum, outside couplings and affine terms are allowed. The source is a complete supporting analytic argument; its requested independent review is a separate status from this report.

### 2.3 Actual account04 theorem applied to an inequality

The designated assignment partner is `account04/B05`. A fresh directory read of

`proofnet24/QFORM-density/fleet-2026-09-22/account04/`

contains B01 and B11--B20 but **no B05 directory**, and the shared B05 handoff root is absent. Thus there is still no completed current-QFORM artifact from the exact designated slot, and none is fabricated.

I do apply completed compatible account04 mathematics to the current theorem: account04/B18,

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` / `QFORM-SCHUR-PIVOT-SMOOTHING-v1`,

canonical source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

For a scalar physical pivot `a != 0` whose `2 x 2` Schur complement is definite, it gives

`||p_Q||_infinity <=2 sqrt(pi) (|a| |det B_3|)^(-1/4)`.                 (2.3)

Section 4 applies (2.3) to the actual `n=3` scalar-pivot branch.

## 3. Every nonzero spectral-coloop pivot is paid

Recall the exact-rank-three plane-plus-singleton endpoint from the earlier B05 classification. Parseval rigidity makes the singleton row exactly a unit normal to the spectral plane. Hence, after choosing only a spectral bookkeeping basis, the corresponding spectral coordinate is literally one original coordinate `X0`, while the remaining two spectral coordinates are

`Y=V^T X_rest`, `V^T V=I_2`,

and `X0` is genuinely independent of `X_rest`.

Write the invertible spectral matrix as

`Lambda = [[a,b^T],[b,C]]`,                                            (3.1)

and suppose `a != 0`. Put

`S=C-b b^T/a`.                                                         (3.2)

Then `det S=det Lambda/a`, so `S` is invertible. Completing the square only in the untouched physical coordinate gives the exact identity

`Q=a (X0+a^(-1)b^T Y)^2 + Y^T S Y`.                                   (3.3)

### Theorem 3.1 — `QFORM-COLOOP-NONZERO-HALF-RIESZ-v1`

Under (3.1)--(3.3), with arbitrary independent cap-one original-coordinate laws,

`boxed(
 ||p_Q||_infinity
 <=16 sqrt(30) (|a| |det Lambda|)^(-1/4).
)`                                                                       (3.4)

No sign or inertia restriction on `a` is imposed.

#### Proof

Condition on `Y`. Since `X0` is independent of `Y`, the translated scalar

`X0+a^(-1)b^T Y`

still has conditional density at most one. The conditional square-density formula therefore gives, for almost every `t`,

`p_Q(t)
 <= |a|^(-1/2) E |Y^T S Y-t|^(-1/2)`.                                (3.5)

Apply the sharper `b=0` case (2.1) of the rank-two half-Riesz theorem to the original product coordinates `X_rest`, the orthonormal projection `V`, and the invertible matrix `S`:

`sup_t E |Y^T S Y-t|^(-1/2)
 <=16 sqrt(30) |det S|^(-1/4)`.                                      (3.6)

Using `det S=det Lambda/a`, (3.5)--(3.6) become exactly (3.4). QED.

### Consequence

The earlier B05 majority-sign coloop debt is eliminated. The result handles minority sign, majority sign, definite or indefinite Schur complement uniformly at every fixed nonzero `a`.

When the Schur complement happens to be definite, the compatible account04/B18 theorem (2.3) gives the strictly sharper source-valid bound

`||p_Q||_infinity <=2 sqrt(pi)(|a||det Lambda|)^(-1/4)`.               (3.7)

Thus account04/B18 is applied to the same actual inequality, while (3.4) removes its prior sign restriction.

The remaining local issue is now sharply identified: (3.4) deteriorates like `|a|^(-1/4)` as `a ->0`, whereas the previously proved exact-zero theorem has the finite bound

`3(2e)^(2/3)|det Lambda|^(-1/3) <9.276`

when `|det Lambda|>=1`. A full coloop closure needs a **translation-coherent near-isotropic estimate** joining these two endpoints; merely taking the better of the two existing bounds leaves a punctured neighborhood of zero unpaid.

The source of the loss is visible in (3.5): replacing the translated scalar density by its cap one before the `Y`-average forgets that the same fixed density of `X0` cannot independently track the moving critical translation `-a^(-1)b^T Y`. This is the exact analogue of the unnormalized-weight loss exposed by the preceding scalar-conditioning counterexample.

## 4. Full original-coordinate dimension `n=3`

Now let `A` itself be real symmetric `3 x 3` and assume all three eigenvalues have modulus at least one. Equivalently,

`sigma_min(A)>=1`, `|det A|>=1`.                                      (4.1)

Let `X_1,X_2,X_3` be arbitrary independent cap-one inputs.

### Theorem 4.1 — `QFORM-PHYSICAL-N3-ENDTOEND-v1`

The law of `Q=X^TAX` has an essentially bounded density. One explicit universal constant is

`C_3 = max{
  16 sqrt(30) 2^(1/4),
  3*400^(1/3) [128(sqrt(6)+2)]^(1/6)
}`.                                                                     (4.2)

Numerically the two displayed constants are approximately

`104.2168899892` and `63.6396743166`,

so `C_3<105`. The decimal comparison is not used in the proof; (4.2) is the exact bound.

#### Proof: branch I — a quantitative scalar pivot exists

Suppose some diagonal entry satisfies

`|a|=|A_ii|>=1/2`.                                                     (4.3)

After reordering coordinates, write

`A=[[a,v^T],[v,B]]`, `S=B-vv^T/a`.                                    (4.4)

Since `det A !=0`, `S` is invertible and

`det A=a det S`.                                                       (4.5)

Completing the square in the ORIGINAL independent coordinate `X_i` gives

`Q=a(X_i+a^(-1)v^T Y)^2+Y^T S Y`,                                    (4.6)

where `Y` consists of the other two original coordinates. Exactly as in (3.5),

`p_Q(t)<=|a|^(-1/2) E|Y^T S Y-t|^(-1/2)`.                             (4.7)

Apply (2.1) with `U=I_2`, `Lambda=S`, `b=0`:

`||p_Q||_infinity
 <=16sqrt(30)|a|^(-1/2)|det S|^(-1/4)
 =16sqrt(30)(|a||det A|)^(-1/4)
 <=16sqrt(30)2^(1/4)`.                                                (4.8)

This handles all signs of `a` and all signatures of `S`.

If `S` is definite, the completed account04/B18 theorem applies directly to (4.6) and sharpens this actual subcase to

`||p_Q||_infinity
 <=2sqrt(pi)(|a||det A|)^(-1/4)
 <=2sqrt(pi)2^(1/4)`.                                                  (4.9)

This is the required concrete account04 theorem application.

#### Proof: branch II — every diagonal pivot is small

Assume instead

`|A_11|,|A_22|,|A_33|<1/2`.                                           (4.10)

Since `sigma_min(A)>=1`, for every standard basis vector `e_i`,

`||Ae_i||_2>=1`.                                                       (4.11)

Fix any row `i`. Equation (4.11) and (4.10) imply

`sum_{j!=i} A_ij^2
 =||Ae_i||_2^2-A_ii^2
 >3/4`.                                                               (4.12)

There are only two off-diagonal terms in this sum, so at least one pair `i!=j` satisfies

`|d|:=|A_ij|>sqrt(3/8)`.                                               (4.13)

Take the corresponding ORIGINAL-coordinate principal pair

`B_2=[[alpha,d],[d,beta]]`,

where `|alpha|,|beta|<1/2`. Then

`det B_2=alpha beta-d^2<1/4-3/8=-1/8`,                                (4.14)

so `B_2` is invertible indefinite and

`D:=|det B_2|>1/8`.                                                    (4.15)

To lower-bound its smallest singular value, compare it with

`B_0=[[0,d],[d,0]]`.

The perturbation `diag(alpha,beta)` has operator norm below `1/2`, while the two singular values of `B_0` both equal `|d|`. The singular-value Lipschitz inequality therefore gives

`kappa:=sigma_min(B_2)
 > sqrt(3/8)-1/2
 = (sqrt(6)-2)/4`.                                                     (4.16)

Now apply the completed full-matrix indefinite-pair theorem (2.2) with `s=s_3(A)>=1`. Using (4.15)--(4.16),

`||p_Q||_infinity
 <3*400^(1/3)
   [ (1/8)^2 ((sqrt(6)-2)/4) ]^(-1/6)`

` =3*400^(1/3)[128(sqrt(6)+2)]^(1/6)`.                                (4.17)

This is the second exact constant in (4.2). Branches I and II are exhaustive, proving the theorem. QED.

### What the theorem closes

The account04/B18 report explicitly left open a fully coupled `3 x 3` inertia `(2,1)` or `(1,2)` block when every nonzero diagonal pivot has the majority sign (a Hadamard-type endpoint). Branch I above closes it whenever a diagonal has modulus at least `1/2`, without a sign restriction. Branch II closes the complementary all-small-diagonal regime by forcing a quantitatively indefinite original-coordinate pair and using (2.2). Hence **no sign or pivot geometry remains in physical dimension three**.

This is a true end-to-end theorem for the full owner quantifiers when `n=3`, but it is not a proof for arbitrary dimension.

## 5. The preceding scalar-fiber stress test is globally harmless by a product-preserving decomposition

The previous B05 counterexample to the scalar worst-conditioned-fiber bridge used

`A=I_4-2ww^T`, `w=(0,1,1,-2)/sqrt(6)`,

with a fragmented cap-one density in `X_1` and uniforms in `X_2,X_3,X_4`. The normalized spectral conditional core density grows like `log m`.

However `w_1=0`, so the full form splits in the ORIGINAL product coordinates as

`Q=X_1^2+R(X_2,X_3,X_4)`,                                             (5.1)

and the residual `3 x 3` matrix has eigenvalues `{1,1,-1}`. By Theorem 4.1,

`||p_R||_infinity<=C_3`.                                               (5.2)

Since `X_1^2` is independent of `R`, convolution with its probability law cannot increase an `L^infinity` density, hence

`||p_Q||_infinity<=C_3`,                                               (5.3)

uniformly in the fragmentation parameter `m`.

Thus the previous logarithmic normalized-fiber blowup is confirmed to be an **interface artifact**, not a QFORM counterexample: a product-preserving decomposition retains the compensating mass that the scalar conditional supremum discarded.

## 6. Exact remaining B05 factor

The two new theorems make the next coarea debt narrower.

1. The exact-rank-three coloop sign problem is gone. What remains there is only the **near-isotropic transition** `a ->0`: exact zero has a finite hyperbolic-square bound, every fixed nonzero `a` has (3.4), but the latter loses `|a|^(-1/4)`.
2. Physical dimension three is completely paid. Therefore a full proof must exploit how an arbitrary high-dimensional product source can be reduced or grouped to a paid three-coordinate / ridge / pair / coloop mechanism **without selecting one vanishing local minor first**.
3. The previous scalar-conditioning falsifier and the present near-zero coloop loss point to the same missing factor: **translation/weight coherence must be retained before taking a supremum or replacing a moving translated density by its pointwise cap**.

A precise next target is therefore:

`QFORM-COLOOP-NEARZERO-TRANSLATION-COHERENCE-v1` — in the coloop form (3.3), prove a bound uniform for `|a|<=a_0` by averaging the actual fixed scalar density through the moving critical translation, or route that region into an aggregate original-coordinate pair/ridge certificate. Any valid estimate must recover the finite `a=0` limit and cannot simply insert `||f_{X0}||_infinity` before the `Y`-integration.

For the unrestricted matrix, the corresponding structural target is an exhaustive product-preserving grouped-coordinate reduction to the now-paid physical three-coordinate endpoint or another completed diffuse/ridge mechanism.

## 7. Status and regularity

Proved in this report, using the complete source-pinned dependencies above:

- `QFORM-COLOOP-NONZERO-HALF-RIESZ-v1`: every nonzero exact-rank-three coloop pivot, all signs;
- `QFORM-PHYSICAL-N3-ENDTOEND-v1`: full physical dimension `n=3`, all admissible product laws and all symmetric matrices with three eigenvalues of modulus at least one, with explicit `C_3` in (4.2);
- the prior scalar-conditioned stress family has full density at most `C_3` by (5.1)--(5.3), despite unbounded normalized spectral conditional fibers.

Not proved:

- a uniform coloop estimate through `a=0` from the nonzero side;
- a reduction of arbitrary dimension to the paid branches;
- the full arbitrary-dimensional QFORM conjecture;
- continuity of the full density. The present arguments establish essential boundedness in their stated scopes only.

**Full QFORM: OPEN / NOT PROVED.**
