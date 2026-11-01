SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-23T09:50:10Z.
attacking: remove the remaining Schur-sign restriction in the dependent-pair/fresh-square transducer by integrating the opposite-sign logarithmic root collar before averaging the source marginal.

# fleet03/B16 — sign-free dependent-pair / fresh-square Schur transducer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Run:** `20260923T095010Z-fleet03-B16-QFORM-r27`  
**Status:** `NEW SUPPORTING THEOREM / PARTNER RESULT APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** absolute continuity and an essential `L^infinity` bound are proved in the stated scope. Continuity is not proved by this argument; global continuity remains open.

## 1. Target and source discipline

The owner target remains: for every `n`, independent real original-coordinate variables `X_i` with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `X^T A X` has a density with universally bounded essential supremum, or give a valid counterexample.


The immediate predecessor is fleet03/B16 run `20260923T092201Z-fleet03-B16-QFORM-r26`, canonical report commit `1b0efed8d90194030e144c6f2678ed31d5684f6e`. It proved the same receiver below under the extra **same-sign Schur gate** `b delta >=0`, with constant `8`, and isolated the opposite-sign gate as a remaining analytic restriction. The present run removes that restriction completely.

The designated partner input is fleet04/B16 run `20260922T161909Z-fleet04-B16-QFORM-r2`,

`yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260922T161909Z-fleet04-B16-QFORM-r2/REPORT.md`.

Its exact nested-heavy identity is used quantitatively in Section 6.

## 2. Main theorem

### Theorem `QFORM-DEPENDENT-PAIR-FRESH-SQUARE-SIGNFREE-v1`

Let `(H,U)` be an arbitrary real random pair; no independence between `H` and `U` is assumed. Let `X` and `V` be real random variables such that the three source objects

`X`, `(H,U)`, `V`

are mutually independent. Assume

`||p_X||_infinity <= L_X`,  `||p_U||_infinity <= L_U`,  `||p_V||_infinity <= L_V`.

Let `gamma !=0`, put

`Y=gamma X+H`,

and let

`B=[[a,k,m],[k,l,n],[m,n,b]]`

be any real symmetric invertible `3 x 3` matrix with `b!=0`. Add arbitrary deterministic affine terms

`r_1 Y+r_2 U+r_3 V+r_0`.

Then, with no sign restriction on any Schur coefficient,

`Q=(Y,U,V)^T B (Y,U,V)+r_1Y+r_2U+r_3V+r_0`

is absolutely continuous and has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= 2^(13/4) L_V sqrt(L_X L_U/|gamma|)
    (|b det B|)^(-1/4).
`

Numerically `2^(13/4)=9.513656920021768...`.

At the exact Schur-null endpoint identified in the predecessor (`delta=0` below), the sharper predecessor constant `4` remains valid. The point of the present theorem is that **the opposite-sign side is no longer exceptional**.

## 3. Exact Schur reduction

Multiplying the whole output by `-1` preserves density height, so assume `b>0`.

Complete the square only in the genuinely independent source scalar `V`. Put

`delta=a-m^2/b`,
`kappa=k-mn/b`,
`lambda=l-n^2/b`,
`p=r_1-mr_3/b`,
`q=r_2-nr_3/b`,
`c=r_0-r_3^2/(4b)`.

Then the conditional square pushforward of `V` gives, for almost every `t`,

`p_Q(t) <= L_V b^(-1/2) E [t-F(Y,U)]_+^(-1/2)`,            (3.1)

where

`F(y,u)=delta y^2+2 kappa u y+lambda u^2+p y+q u+c`.       (3.2)

Conditional on `(H,U)`, the variable `Y=gamma X+H` is a translate of `gamma X`, hence has density cap

`L_Y=L_X/|gamma|`.                                             (3.3)

No conditional density of `U|H` is used.

For fixed `u`, write

`s(u)=kappa u+p/2`,
`r(u)=lambda u^2+q u+c`,
`D_t(u)=delta(t-r(u))+s(u)^2`.                                 (3.4)

When `delta!=0`, completing the square in the deterministic variable `y` gives the exact identity

`t-F(y,u)=D_t(u)/delta-delta (y+s(u)/delta)^2`.                (3.5)

The coefficient of `u^2` in `D_t` is

`theta=kappa^2-delta lambda`.                                  (3.6)

The Schur determinant identity is

`det B=b(delta lambda-kappa^2)=-b theta`,                      (3.7)

so, since `B` is invertible,

`theta!=0`,  `|theta|=|det B|/b`.                              (3.8)

## 4. New opposite-sign kernel estimate

The predecessor paid `delta>0`. The missing case is `delta<0`; write `alpha=-delta>0`.

### Lemma 4.1 — conditional root-collar bound

For every fixed `u` with `D=D_t(u)!=0`,

`E([t-F(Y,u)]_+^(-1/2) | H,U=u)
 <= 2 sqrt(2 L_Y) |D|^(-1/4)`.                                (4.1)

This bound is uniform in the conditional value of `H`.

#### Case A: `delta>0`

If `D<=0`, the positive set is empty up to a null point. If `D>0`, (3.5) is a concave quadratic. For `z>0`, the superlevel set of the kernel is the pair of root collars

`{y: 0<t-F(y,u)<z^(-2)}`.

Its total length is at most

`2/(sqrt(D) z^2)`.                                             (4.2)

Using the density cap `L_Y` and probability normalization,

`P(K>z) <= min(1, 2L_Y/(sqrt(D) z^2))`,

hence layer cake gives

`E K <= integral_0^infinity min(1,2L_Y D^(-1/2)z^(-2)) dz
      =2 sqrt(2L_Y) D^(-1/4)`.                                 (4.3)

#### Case B: `delta<0`, `D>0`

Now

`t-F=alpha x^2-D/alpha`

after translation. The positive set lies outside two roots. The same root-collar computation is even slightly better: the total length of

`{0<alpha x^2-D/alpha<z^(-2)}`

is at most `1/(sqrt(D)z^2)`, so (4.1) follows from the same safe constant as in (4.3).

#### Case C: `delta<0`, `D<0`

Now

`t-F=alpha x^2+|D|/alpha`,

so the kernel has finite maximum

`Z=sqrt(alpha/|D|)`.

For `0<z<Z`, its superlevel set has length at most

`2/(sqrt(alpha) z)`.                                           (4.4)

Put `A=2L_Y/sqrt(alpha)`. Layer cake yields

`E K <= integral_0^Z min(1,A/z) dz`.                           (4.5)

If `Z<=A`, the right side is at most `Z<=sqrt(AZ)`. If `Z>A`, it equals

`A(1+log(Z/A))`.

For `r>=1`,

`1+log r <=2 sqrt(r)`                                          (4.6)

because `2sqrt(r)-1-log r` is increasing and positive at `r=1`. Therefore both subcases give

`E K <=2 sqrt(AZ)
     =2 sqrt(2L_Y)|D|^(-1/4)`,                                 (4.7)

which is (4.1).

At `D=0` the fixed-`u` kernel may have a logarithmic divergence in the opposite-sign case, but `D_t(U)=0` occurs with probability zero because `U` has a density and `D_t` is a nonzero quadratic polynomial by (3.8). Thus this null slice causes no problem in the subsequent Tonelli integral.

For `delta=0`, the affine-in-`y` predecessor calculation gives an even smaller conditional bound and is included in the final theorem.

## 5. Average the singular collar before any conditional supremum

We need one elementary quadratic sublevel estimate.

### Lemma 5.1 — absolute quadratic band

For every real quadratic polynomial

`D(u)=theta u^2+beta u+eta`, `theta!=0`,

and every `s>0`,

`|{u: |D(u)|<s}| <= 2 sqrt(2s/|theta|)`.                        (5.1)

Proof: complete the square and scale by `sqrt(|theta|)`. The problem reduces to `|x^2-a|<s`. If `a>=s`, the total length is

`2(sqrt(a+s)-sqrt(a-s)) <=2sqrt(2s)`;

if `-s<a<s`, the set is a centered interval of length at most `2sqrt(2s)`; if `a<=-s` it is empty.

Since `p_U<=L_U`,

`P(|D_t(U)|<s)
 <= min(1, 2sqrt(2)L_U sqrt(s/|theta|))`.                       (5.2)

Layer cake with exponent `1/4` gives

`E |D_t(U)|^(-1/4)
 <= integral_0^infinity min(1,A z^(-2)) dz
 =2 sqrt(A)`,                                                   (5.3)

where

`A=2sqrt(2)L_U/ sqrt(|theta|)`.

Therefore

`E |D_t(U)|^(-1/4)
 <=2^(7/4) sqrt(L_U)|theta|^(-1/4)`.                           (5.4)

Combining (3.1), Lemma 4.1, (5.4), (3.3), and (3.8),

`p_Q(t)
 <=L_V b^(-1/2)
   [2sqrt(2)sqrt(L_Y)]
   [2^(7/4)sqrt(L_U)|theta|^(-1/4)]`

`=2^(13/4)L_V sqrt(L_XL_U/|gamma|)
  b^(-1/2)(|det B|/b)^(-1/4)`

`=2^(13/4)L_V sqrt(L_XL_U/|gamma|)
  (b|det B|)^(-1/4)`.                                          (5.5)

Restoring the original sign of `b` gives the theorem with `|b|`.

This proof is exactly the dependence-preserving operation required by the assignment: the singular opposite-sign slice is **integrated against the original unconditional source marginal before any projection-height supremum is taken**.

## 6. Designated partner result applied to an actual target inequality

Fleet04/B16 r2 proves, for an exact-rank-three frame `A=R Lambda R^T` and a nested-heavy physical pair `(i,j)` with

`c=||r_i||^2>1/2`,
`h=||(I-ee^T)r_j||^2>1/2`,

that

`G_ij=ch>1/4`,                                                   (6.1)

and that there are normalized bank weights `w_k>=0`, `sum_k w_k=1`, with

`|det A_{\{i,j,k\}}|=|det Lambda| G_ij w_k`.                    (6.2)

Since all three nonzero eigenvalues have modulus at least one,

`|det A_{\{i,j,k\}}| > w_k/4`.                                 (6.3)

This partner identity is now inserted into the sign-free theorem rather than merely cited.

### Corollary `QFORM-NESTED-HEAVY-NONZERO-DIAGONAL-ATOM-v1`

In the nested-heavy exact-rank-three state, if one bank atom satisfies

`w_k>=1/8` and `|A_kk|>=1/64`,                                  (6.4)

then the full ambient quadratic form, with arbitrary outside original coordinates, arbitrary outside quadratic terms, and arbitrary couplings, has

`boxed: ||p_Q||_infinity <64`.                                  (6.5)

Proof: condition on every original coordinate outside `{i,j,k}`. The remaining three original variables are still independent with density caps one; all outside interactions become arbitrary affine terms. Set

`X=X_i`, `H=0`, `U=X_j`, `V=X_k`, `gamma=1`, `B=A_{\{i,j,k\}}`.

By (6.3)-(6.4),

`|det B|>1/32`, `|b|=|A_kk|>=1/64`,

hence

`|b det B|>1/2048=2^(-11)`.                                    (6.6)

Theorem 2 gives

`||p_Q||_infinity
 <=2^(13/4)(2^11)^(1/4)
 =2^6
 =64`.                                                         (6.7)

Averaging the conditional densities preserves the same bound. No Schur-sign condition is required. This extends the partner's exact zero-diagonal atom endpoint to a quantitative nonzero-diagonal atom branch.

The partner's r3 correction also explains why this source-first route is necessary: in its diffuse-block family the conditional projection-height variable satisfies `E M_m=m`, while the actual rank-three output remains uniformly bounded. A receiver-only inequality of the form `||p_Q||_infinity <= C E M_m` would therefore lose a factor `m`; the present proof never introduces that quantity.

## 7. What remains

The new theorem removes the **entire Schur-sign obstruction** from the fresh-square branch. The near-coloop compiler no longer needs separate same-sign and opposite-sign cases once it has three genuine source objects `X`, `(H,U)`, `V` with quantitative `|b det B|`.

The first unpaid B16 implication is now purely structural:

`QFORM-NEAR-COLOOP-FRESH-SQUARE-OR-SHARED-BANK-v2`.

In the exact-rank-three near-coloop collar `c>63/64`, after the already-paid transverse and two-bank exits, either

1. extract a disjoint fresh scalar source `V` with `|b det B|` bounded below at a universal scale, in which case Theorem 2 closes the branch with **no sign test**, or
2. prove a product-preserving receiver for the genuinely shared-bank endpoint where every usable transverse square shares original-coordinate sources with `(H,U)`.

Arbitrary additional spectrum remains a separate full-target interface after exact rank three. The full conjecture and the global continuity conclusion are not proved here.

## 8. Verification notes

A finite checker accompanying this report verifies:

1. `2^(13/4)=9.513656920021768...`;
2. the nested-heavy threshold calculation gives exactly `64` at `w_k=1/8`, `|A_kk|=1/64`;
3. `1+log r <=2sqrt(r)` on a wide deterministic grid `r>=1`;
4. randomized numerical checks of the absolute quadratic-band estimate (5.1) remain below its analytic constant.

The checker is supplementary only; the proof above is analytic.

**Full QFORM conjecture: OPEN / NOT PROVED.**
