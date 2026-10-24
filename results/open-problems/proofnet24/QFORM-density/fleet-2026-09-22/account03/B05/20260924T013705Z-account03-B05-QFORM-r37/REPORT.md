SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T01:37:05Z.
attacking: QFORM-INDEFINITE-PAIR-OUTSIDE-COLLAR-COMPILER-v1 — replace the collar/condition-number split by a global product-preserving one-third coarea kernel for every invertible indefinite scalar pair.

# account03/B05 r37 — a determinant-only one-third hyperbolic coarea kernel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: quadratic coarea / equivalent interval bound preserving arbitrary original-coordinate product densities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING PRODUCT-PRESERVING THEOREM / ENTIRE INDEFINITE RATIO-PAIR BRANCH CLOSED / FULL QFORM OPEN**  
Full-target continuity: **OPEN**. The new result proves absolute continuity and essential boundedness in its scope; continuity is not claimed.

## 1. First missing implication and what changes

The immediate predecessor proved a uniform one-third receiver only on the fixed near-double-zero collar

`max(|a|,|d|) <= sqrt(|det B|)/5`

for the indefinite scalar block `B=[[a,c],[c,d]]`. Outside that collar the older raw-diagonal receiver gave a fourth-root loss, so the unpaid question was whether condition number or a raw diagonal is genuinely needed.

It is not needed at the scalar-pair level. The missing operation is to aggregate the two original independent scalar densities **before** paying the reciprocal gradient. The key observation is that a level branch of a nondegenerate indefinite quadratic has second derivative

`|y''| = D |t| / s^3`,

while the coarea denominator is `2s`, where `D=|det B|`. A dyadic decomposition in the *same* variable `s` lets one interpolate a mass bound against this curvature bound. The crossover exponent is exactly one third.

The result is a translation-uniform, condition-number-free bound

`p_pair(t) <= 8(3+sqrt(2)) (L_1 L_2)^(2/3) D^(-1/3) |t|^(-1/3)`.

Splicing this directly to the already-proved rank-one affine square-root small-ball estimate closes **every invertible indefinite scalar block** in the live ratio packet, including all nonzero-diagonal cases outside the previous collar.

This does not use arbitrary-joint coarea, post-rotation independence, conditional projection-density caps, fiber suprema, pointwise van-der-Corput decay, compact support, or moments.

## 2. A one-dimensional curvature-composition lemma

### Lemma 2.1 — monotone-derivative composition

Let `g` be a probability density on the line with `||g||_infinity <= L`. Let `phi` be `C^2` on an interval `J`, with `phi''` of fixed sign and

`|phi''(x)| >= lambda >0` on `J`.

Then

`boxed:
 integral_J g(phi(x)) dx <= 4 sqrt(L/lambda).
`

#### Proof

Since `phi'` is monotone, for every `u>0` the set

`E_u={x in J: |phi'(x)|<=u}`

has length at most `2u/lambda`. Hence

`integral_(E_u) g(phi(x)) dx <= 2 L u/lambda`.

The complement has at most two intervals on each of which `phi` is monotone and `|phi'|>=u`. On each such component, change variables `v=phi(x)` to get an integral at most `1/u`, so the two components contribute at most `2/u`. Therefore

`integral_J g(phi(x)) dx <= 2Lu/lambda+2/u`.

Taking `u=sqrt(lambda/L)` gives the claim. QED.

This elementary lemma is the only nonlinear one-dimensional input below.

## 3. Main scalar-pair theorem

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-ONE-THIRD-COAREA-v1`

Let `X,Y` be independent real random variables with probability densities `f,g` satisfying

`||f||_infinity <= L_X`, `||g||_infinity <= L_Y`.

Let

`B=[[a,c],[c,d]]`

be real symmetric and indefinite, and put

`D=|det B|=c^2-ad>0`.

For arbitrary deterministic translations `x_0,y_0`, define

`R=(X+x_0,Y+y_0)^T B (X+x_0,Y+y_0)`.

Then `R` is absolutely continuous and for almost every `t!=0`,

`boxed:
 p_R(t)
 <= C_H (L_X L_Y)^(2/3) (D |t|)^(-1/3),
 C_H=8(3+sqrt(2))<35.314.
`

At `t=0` the right side is infinite, so no pointwise assertion there is needed. The estimate is uniform in the translations and in the condition number of `B`.

### Proof, case `d!=0`

Translations preserve independence and the density caps, so absorb `x_0,y_0` into the laws and write

`q(x,y)=a x^2+2cxy+d y^2`.

Fix `t!=0`. Put

`s(x)=sqrt(D x^2+d t)`

on the open domain `Omega_t={x: D x^2+d t>0}`. The two roots of `q(x,y)=t` in the `y` variable are

`y_sigma(x)=(-c x+sigma s(x))/d`, `sigma in {+1,-1}`.

Moreover

`partial_y q(x,y_sigma(x)) = 2 sigma s(x)`.

Thus the standard one-dimensional coarea/root formula gives, for almost every `t!=0`,

`p_R(t)
 = sum_sigma integral_(Omega_t)
   f(x) g(y_sigma(x)) [2s(x)]^(-1) dx.                 (3.1)`

A direct differentiation gives the exact identity

`boxed:
 y_sigma''(x)=sigma D t / s(x)^3.                    (3.2)
`

This is the decisive cancellation: no entry of `B` other than its determinant remains.

Choose a scale `R_0>0`, to be optimized below, and put

`R_k=2^k R_0`,
`E_k={x in Omega_t: R_k <= s(x)<2R_k}`, `k in Z`.

Because `s(x)^2=D x^2+d t`, each `E_k` is a union of at most two intervals. On every component and for each fixed `sigma`, (3.2) has fixed sign and

`|y_sigma''(x)|
 >= D|t|/(8R_k^3).                                      (3.3)`

There are two complementary estimates for the contribution of `E_k`.

**Mass estimate.** Since `g<=L_Y`, `s>=R_k`, and `f` has total mass one,

`sum_sigma integral_(E_k)
 f(x)g(y_sigma(x))[2s(x)]^(-1) dx
 <= L_Y/R_k.                                             (3.4)`

**Curvature estimate.** Apply Lemma 2.1 on each of at most two interval components of `E_k`, use `f<=L_X`, and then `s>=R_k`. For one root branch,

`integral_(E_k) f(x)g(y_sigma(x))[2s(x)]^(-1) dx
 <= 8 sqrt(2) L_X L_Y^(1/2)
    R_k^(1/2) (D|t|)^(-1/2).                            (3.5)`

Summing the two root branches gives

`<=16 sqrt(2) L_X L_Y^(1/2)
   R_k^(1/2)(D|t|)^(-1/2).                              (3.6)`

Therefore the full shell contribution `A_k` obeys

`A_k <= min{
 L_Y/R_k,
 16 sqrt(2) L_X L_Y^(1/2) R_k^(1/2)(D|t|)^(-1/2)
}.                                                       (3.7)`

Choose `R_0` so the two entries in (3.7) are equal at `k=0`. Their common value is

`T=(16sqrt(2))^(2/3)
   (L_XL_Y)^(2/3)(D|t|)^(-1/3)
 =8 (L_XL_Y)^(2/3)(D|t|)^(-1/3).                       (3.8)`

For `k>=0`, sum the mass bound:

`sum_(k>=0) A_k <= T sum_(k>=0)2^(-k)=2T`.             (3.9)

For `k<0`, sum the curvature bound:

`sum_(k<0) A_k
 <=T sum_(j>=1)2^(-j/2)
 =(1+sqrt(2))T`.                                        (3.10)`

Combining (3.8)--(3.10) yields

`p_R(t)
 <=(3+sqrt(2))T
 =8(3+sqrt(2))(L_XL_Y)^(2/3)(D|t|)^(-1/3)`,

as claimed.

### Proof, case `d=0`

Then `c!=0`, `D=c^2`, and for `x!=0` the level equation has the unique root

`y(x)=(t-a x^2)/(2cx)`.

The coarea denominator is

`|partial_y q|=2|cx|=2s`, `s=|c x|`,

and a direct differentiation gives

`|y''(x)|=D|t|/s^3`.

Dyadically decompose in `s` exactly as above. There is now only one root branch, so the previous estimates apply with no larger constant. This proves Theorem 3.1 in all cases. QED.

### Absolute continuity

The root formula above constructs a density on every `t!=0`. The only critical point of the nondegenerate quadratic is the origin, which has zero probability under an absolutely continuous product law. Equivalently one may apply coarea away from the origin and let the deleted ball shrink. Hence the pushforward has no singular mass at the critical value, so the law is absolutely continuous.

## 4. Environment splice: square-root small ball plus the one-third pair kernel

### Corollary 4.1 — `QFORM-INDEFINITE-PAIR-ONE-THIRD-SCHUR-v1`

Let `E` be an arbitrary environment. Let `Y,Z` be independent of each other and of `E`, with density caps `L_Y,L_Z`. Let `B` be any fixed invertible indefinite symmetric `2x2` matrix with `D=|det B|`. Let `h(E) in R^2` be arbitrary measurable and let `T(E)` be a real random variable satisfying, uniformly in `u` and `rho>0`,

`P(|T-u|<rho) <= min(1,H sqrt(rho)).                    (4.1)`

Then

`Q=T(E)+[Y,Z+h(E)]^T B [Y,Z+h(E)]`

(with the evident vector notation, i.e. independent coordinatewise translations) has an essentially bounded density satisfying

`boxed:
 ||p_Q||_(infinity,ess)
 <= 3 C_H (L_YL_Z)^(2/3) D^(-1/3) H^(2/3).             (4.2)`

#### Proof

Condition on `E`. Theorem 3.1, uniformly in the resulting deterministic translations, gives the conditional density envelope

`p_(Q|E)(u)
 <=C_H(L_YL_Z)^(2/3)D^(-1/3)|u-T(E)|^(-1/3).`

The already-used layer-cake lemma says that (4.1) implies

`sup_u E|T-u|^(-1/3) <=3H^(2/3).`

Average the conditional envelope. QED.

This is exactly the aggregate-before-inversion statement that the previous collar proof lacked globally.

## 5. Application to the live ratio packet: all indefinite `B`

Use the live affine ratio packet

`Q=V^T C V+2V^T P W+W^T B W
   +ell_V^T V+ell_W^T W+q_0`,

where `V=(S,R)` is an orthonormal two-dimensional projection of one original-coordinate product bank and `W=(Y,Z)` consists of two mutually independent normalized scalar projections on disjoint original-coordinate banks. The scalar caps satisfy

`L_Y,L_Z <=sqrt(2)`.

Assume `B` is invertible and indefinite, and

`C-PB^(-1)P^T=lambda m e_1e_1^T`,
`mu=|det B| |lambda|`.

Complete the scalar pair:

`h(V)=B^(-1)(P^T V+ell_W/2)`,

`Q=[W+h(V)]^T B[W+h(V)]+T(V)`,

where exactly

`T(V)=lambda m S^2+b^T V+q_1`.                       (5.1)`

No conditioning of the dependent coordinate `R` is performed. The rank-one affine small-ball theorem already source-pinned in the programme gives

`P(|T-u|<rho)
 <=min(1,10 sqrt(rho/(|lambda|m))).                    (5.2)`

Thus in Corollary 4.1

`H=10/sqrt(|lambda|m)`,
`D=|det B|`,
`(L_YL_Z)^(2/3)<=2^(2/3)`.

Consequently

`boxed:
 ||p_Q||_(infinity,ess)
 <= C_RP (mu m)^(-1/3),
 C_RP=3*20^(2/3)*8(3+sqrt(2))
     =780.5808866... <781.
}                                                        (5.3)`

This bound is independent of

- the condition number of `B`;
- both raw diagonals `a,d`;
- the ratio residual `sigma` in the first product bank;
- the translations generated by the dependent residual coordinate;
- the support locations, fragment counts, or moments of any input law.

For the standard ratio packet `m>=3/20`,

`boxed:
 ||p_Q||_(infinity,ess)
 <1470 mu^(-1/3).
}                                                        (5.4)`

Therefore every standard ratio packet with `mu>=1` and **any invertible indefinite scalar pair** has the numerical universal branch bound `<1470`.

This supersedes the previous distinction between the near-double-zero collar and its outside-collar complement for the indefinite scalar pair. The previous collar theorem remains a sharper constant in its scope, but is no longer structurally necessary.

## 6. Designated partner account04/B05 applied to an actual complementary inequality

Fresh designated-partner source consumed:

- `yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260924T011830Z-account04-B05-convex-pair-r3/REPORT.md`
- theorem `QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`.

For an actual original-coordinate definite physical pair with coordinate density caps `m_i,m_j`, it proves

`P(Q in I)<=pi m_i m_j |det C|^(-1/2)|I|`.

Apply it to the literal-scalar endpoint of the present packet: if `q_Y=q_Z=1`, the normalized scalar projections `Y,Z` are literal original coordinates up to signs. If their physical block `B` is definite, then `m_i=m_j=1` and

`boxed:
 ||p_Q||_(infinity,ess)<=pi |det B|^(-1/2).
}                                                        (6.1)`

In the actual quantitative branch `|det B|>=1/4`, this gives

`boxed: ||p_Q||_(infinity,ess)<=2pi<6.284.`             (6.2)`

Thus the fresh partner closes the convex literal-pair side, while Theorem 5.1 closes the full hyperbolic/indefinite scalar-pair side of the ratio packet.

## 7. What remains

The new theorem closes the predecessor debt

`QFORM-INDEFINITE-PAIR-OUTSIDE-COLLAR-COMPILER-v1`

for the entire invertible-indefinite scalar-pair regime. The next B05 debt is no longer a condition-number or raw-diagonal problem.

The remaining geometric assembly issue is:

`QFORM-RATIOPACKET-TO-GLOBAL-COMPILER-v1`:

> verify, in the current global reduction, that every hard three-eigenvalue configuration is routed either to an invertible-indefinite ratio packet covered by (5.3), to a completed definite/literal or exact-slope/crossing branch, or to a separately identified zero-pivot/isotropic-shear survivor; then quantify any remaining loss in `mu` rather than re-opening scalar-pair conditioning.

In particular, a future proof should not reintroduce `sigma_min(B)`, a raw diagonal, or a collar assumption inside the indefinite ratio packet: (5.3) has removed those factors.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. The new theorem establishes absolute continuity and essential boundedness only in its stated branch.
