SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T14:23:18Z.
attacking: decoupled time integral at the near-coloop angular-cancellation endpoint; aggregate the complementary one-dimensional product bank and derive a dependence-safe half-Riesz receiver.

# account03/B03 r35 — heavy-row pair aggregation and endpoint Fresnel-Plancherel compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** decoupled time integral  
**Status:** `NEW SUPPORTING THEOREMS / ANGULAR-CANCELLATION L2-TIME ENDPOINT STABILIZED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full owner target remains open and the full continuity conclusion remains open. This report proves a new source-preserving aggregation lemma and a dependence-safe time-integral theorem in the exact one-sided-overlap packet. It does not infer independence after spectral rotation, does not condition a sum/difference variable and reuse its marginal cap, and does not use law-uniform pointwise quadratic-phase decay.


## 1. Source-valid inputs actually used

1. **Weighted product projection.** `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, account02/B06, canonical
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.
   A unit scalar projection of an original-coordinate cap-one product law has density at most `sqrt(e)`; a two-dimensional orthogonal projection has density at most `e`. This is a weighted physical-fiber theorem, not the refuted unrestricted fiber supremum.

2. **Fresnel linearization.** The damped Fresnel identity and limiting argument from
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   used previously in account01/B06 r24. The present proof uses Fresnel only to expose original-coordinate Fourier transforms; no pointwise van-der-Corput estimate is used.

3. **Incoming exact packet.** account03/B03 r27 and r34, canonical reports
   `yspennstate/math-open-problems@b580b09027d8c20c3d3bbea0bea6cf8caa04d541` and
   `yspennstate/math-open-problems@926549e6ace81816d0533164f35f548a4f84d508`.

4. **Designated partner account04/B03.** Only the valid collision lemma from
   `yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38` is used:
   `P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`.
   The partner's subsequently challenged weighted-L2 compiler is not used.

## 2. Heavy physical row gives a uniform joint cap after aggregating the complement

Let `X_R=(X_j)_{j in R}` have independent densities at most one. Let `v,q in R^R` be orthonormal, let

`V=v.X_R`, `H=(beta v+m q).X_R`, `m>0`,                              (2.1)

and fix an actual original-coordinate row `r`. Put

`c=v_r^2+q_r^2`, `0<c<=1`.                                          (2.2)

### Theorem 2.1 — `QFORM-HEAVY-ROW-PAIR-CAP-v1`

The pair `(V,H)` has a joint density and

`boxed: ||p_(V,H)||_infinity <= sqrt(e)/(m sqrt(c)).`                (2.3)

This remains valid at the exact coloop endpoint `c=1` and is completely independent of the angular coefficient `h_r=beta v_r+m q_r`.

### Proof

Write `z_r=(v_r,q_r)` and choose an orthonormal basis `(e_1,e_2)` of the spectral `(v,q)` plane with

`e_1=z_r/sqrt(c)`.                                                    (2.4)

For `j != r`, put

`a_j=< (v_j,q_j),e_1>`, `b_j=< (v_j,q_j),e_2>`.                     (2.5)

Because the row frame of `(v,q)` is Parseval,

`sum_{j!=r} a_j^2=1-c`, `sum_{j!=r} b_j^2=1`, `sum_{j!=r}a_jb_j=0`. (2.6)

When `c<1`, define the complement projections

`Y=(1/sqrt(1-c)) sum_{j!=r} a_j X_j`,
`Z=sum_{j!=r} b_j X_j`.                                              (2.7)

The coefficient vectors of `Y,Z` are orthonormal on the original-coordinate complement bank. In particular, the weighted product-projection theorem gives

`||p_Z||_infinity <= sqrt(e)`.                                      (2.8)

Let

`S=sqrt(c) X_r+sqrt(1-c)Y`.                                         (2.9)

Although `Y,Z` may be dependent, `X_r` is genuinely independent of the complement bank. Therefore

`p_(S,Z)(s,z)
 =c^(-1/2) int f_r((s-sqrt(1-c)y)/sqrt(c)) p_(Y,Z)(y,z)dy`

`<=c^(-1/2) int p_(Y,Z)(y,z)dy
 =c^(-1/2)p_Z(z)
 <=sqrt(e/c).`                                                       (2.10)

At `c=1`, the same conclusion is simply `p_(S,Z)=f_r p_Z`.

Write the physical spectral vectors `e_v=(1,0)` and `w=(beta,m)` in the `(e_1,e_2)` basis:

`e_v=alpha e_1+gamma e_2`, `w=w_1e_1+w_2e_2`.                     (2.11)

Then

`V=alpha S+gamma Z`, `H=w_1S+w_2Z`,                                (2.12)

and the Jacobian determinant is

`|alpha w_2-gamma w_1|=|det(e_v,w)|=m`.                             (2.13)

Changing variables in (2.10) proves (2.3). QED.

**Structural point.** The narrow `sqrt(1-c)` complement direction is not discarded. It is aggregated into `Y`, while the transverse complement direction `Z` keeps a true scalar product-projection cap. The heavy original coordinate then smooths the narrow direction. This is stable as `c->1` and uses no conditional projected-density claim.

## 3. Fresnel-Plancherel theorem for the exact square-plus-hyperbola packet

Let the original coordinates split into a physical pivot `i`, left bank `L`, right bank `R`, and residual bank `K`, all mutually independent. Consider

`Q=a^(-1)H^2+2 sigma U V`,                                          (3.1)

`H=a X_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`,                                                         (3.2)

where `a sigma !=0`, `u` is unit, and assume only that the right pair

`(H_R,V):=(h_R.X_R,v.X_R)`                                          (3.3)

has a joint density cap

`M=||p_(H_R,V)||_infinity<infinity`.                                (3.4)

Let

`L=||p_U||_infinity`.                                                (3.5)

No independence between `U` and `h_L.X_L` is assumed.

### Theorem 3.1 — `QFORM-PAIRCAP-FRESNEL-L2-v1`

For every real `t !=0`,

`boxed:
 |phi_Q(t)| <= min{1, D/|t|},
 D=pi sqrt(L M/|sigma|).
}`                                                                    (3.6)

Consequently

`boxed: int_R |phi_Q(t)|^2 dt <=4D,`                                (3.7)

`boxed: ||p_Q||_2^2 <=2 sqrt(LM/|sigma|),`                          (3.8)

and

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <=(16/3)sqrt(pi)(LM/|sigma|)^(1/4).
}`                                                                    (3.9)

The independent-copy identity is kept at the level of the whole variable: `(3.9)` is equivalently a half-Riesz energy of `Q-Q'`; no coordinate sum is separated from its conjugate difference.

### Proof

Use Fourier convention `f_hat(xi)=int exp(i xi x)f(x)dx`. The damped Fresnel identity, followed by the source limiting argument, gives

`phi_Q(t)=C_(a,t) int exp(-i a s^2/(4t)) chi_i(as) chi_K(s)
 [int g_s(u) F_R(s,2t sigma u)du] ds`,                              (3.10)

where

`|C_(a,t)|=sqrt(|a|/(4pi|t|))`,                                    (3.11)

`chi_i` is the characteristic function of `X_i`, `|chi_K|<=1`,

`F_R(s,xi)=E exp(i s H_R+i xi V)`,                                  (3.12)

and `g_s` is the complex density obtained by pushing
`exp(i s h_L.X_L)` through `U=u.X_L`.

The crucial dependence-preserving fact is

`|g_s(u)|<=p_U(u)` a.e.                                               (3.13)

because the Radon--Nikodym derivative is the conditional expectation of a unit-modulus phase. Hence

`||g_s||_2^2 <= int p_U(u)^2du <=L`.                                (3.14)

For fixed `s`, Cauchy--Schwarz and `xi=2t sigma u` give

`|int g_s(u)F_R(s,2t sigma u)du|
 <=[L/(2|t sigma|)]^(1/2)
   [int |F_R(s,xi)|^2 dxi]^(1/2).`                                  (3.15)

Now apply Cauchy--Schwarz in `s`. Since `f_i<=1` is a probability density,

`int |chi_i(as)|^2 ds
 =(2pi/|a|) int f_i^2 <=2pi/|a|`.                                   (3.16)

Two-dimensional Plancherel and `p_(H_R,V)<=M` give

`int_R2 |F_R(s,xi)|^2 ds dxi
 =(2pi)^2 ||p_(H_R,V)||_2^2
 <=(2pi)^2 M`.                                                       (3.17)

Multiplying (3.11), (3.15), (3.16), and (3.17) yields exactly

`|phi_Q(t)| <= pi sqrt(LM/|sigma|)|t|^(-1)`.                        (3.18)

Adjoin `|phi_Q|<=1` to get (3.6).

If `T=D` is the crossover, direct integration gives

`int min(1,D^2/t^2)dt=4D`,                                         (3.19)

and Plancherel proves (3.8). Likewise

`int |t|^(-1/2)min(1,D^2/t^2)dt=(16/3)sqrt(D)`,                    (3.20)

which is (3.9). QED.

## 4. All finite Lp norms and a translation-uniform half-Riesz receiver

The borderline `1/|t|` one-copy decay is not integrable, so Theorem 3.1 alone does **not** prove `L^infinity`. It does, however, give every finite density norm.

For `p>=2`, set `q=p/(p-1)`. From (3.6),

`int |phi_Q|^q <=2D q/(q-1)=2Dp`.                                  (4.1)

Interpolating the inverse-Fourier `L^1->L^infinity` and Plancherel bounds gives

`boxed:
 ||p_Q||_p <=[p sqrt(LM/|sigma|)]^(1-1/p),  2<=p<infinity.
}`                                                                    (4.2)

At `p=4`, put

`S=sqrt(LM/|sigma|)`.                                                (4.3)

Then `||p_Q||_4<=(4S)^(3/4)`. For every shift `z` and every `R>0`, Holder near `z` and probability mass outside give

`E|Q-z|^(-1/2)
 <=6^(3/4)||p_Q||_4 R^(1/4)+R^(-1/2)`.                              (4.4)

Optimizing in `R` yields the explicit translation-uniform potential bound

`boxed:
 sup_z E|Q-z|^(-1/2)
 <= C_H (LM/|sigma|)^(1/4),
 C_H=6sqrt(6)/2^(2/3)=9.2584910653...
}`                                                                    (4.5)

Therefore, whenever an additional **genuine disjoint original coordinate** `Z` is available with density cap one and

`T=d[Z+h]^2+Q`, `d!=0`,                                               (4.6)

where `Z` is independent of the whole state `(h,Q)`, conditional square smoothing gives the actual linear output small-ball bound

`boxed:
 ||p_T||_infinity
 <= C_H |d|^(-1/2)(LM/|sigma|)^(1/4).
}`                                                                    (4.7)

Thus the new time estimate is not merely a collision certificate: it supplies a translation-uniform half-Riesz receiver that converts one further true physical square into one-copy `L^infinity` scaling. The current exact rank-three packet does not automatically provide such an unused fourth square, so (4.7) is a supporting compiler rather than a full-target closure.

## 5. Application to the r34 near-coloop angular-cancellation collar

Return to the exact r27/r34 packet

`h_R=beta v+m q`, `v perp q`, `||v||=||q||=1`, `m>0`,               (5.1)

and let the r34 near-coloop row `r` have

`c=eta_r=v_r^2+q_r^2>2/3`.                                         (5.2)

Theorem 2.1 gives

`M<=sqrt(e)/(m sqrt(c))`,                                           (5.3)

while the scalar product-projection bound on the independent left bank gives

`L<=sqrt(e)`.                                                        (5.4)

Hence Theorem 3.1 yields the **angular-cancellation-stable** envelope

`boxed:
 |phi_Q(t)|
 <=min{1,
 pi sqrt(e) (|sigma|m sqrt(c))^(-1/2)|t|^(-1)}.
}`                                                                    (5.5)

Unlike the physical-pivot r27 estimate, every bound in this section is independent of

`h_r=beta v_r+m q_r`;                                                (5.6)

it stays finite as the angular cancellation becomes exact.

The explicit integrated consequences are

`boxed:
 ||p_Q||_2^2
 <=2sqrt(e)(|sigma|m sqrt(c))^(-1/2),
}`                                                                    (5.7)

`boxed:
 int |t|^(-1/2)|phi_Q(t)|^2dt
 <=(16/3)sqrt(pi)e^(1/4)(|sigma|m sqrt(c))^(-1/4),
}`                                                                    (5.8)

and

`boxed:
 sup_z E|Q-z|^(-1/2)
 <= C_H e^(1/4)(|sigma|m sqrt(c))^(-1/4).
}`                                                                    (5.9)

Numerically, the outside constants in (5.7), (5.8), (5.9) are respectively

`2sqrt(e)=3.2974425414...`,
`(16/3)sqrt(pi)e^(1/4)=12.1380042372...`,
`C_H e^(1/4)=11.888...` (the exact symbolic form is authoritative). (5.9) is only used as a supporting receiver; the exact rank-three endpoint still lacks the additional unused square required by (4.7).

This is a genuine advance on the r34 near-coloop debt: the singular factor `|h_r|^(-1/2)` has disappeared completely at the level of all finite `L^p`, collision small-ball, and the translation-uniform half-Riesz potential. The remaining gap is now specifically the borderline `L^p for every finite p` -> `L^infinity` upgrade at the exact three-direction level.

## 6. Designated account04/B03 partner applied to an actual inequality

From (3.8), the valid account04/B03 collision lemma gives

`P(|Q-Q'|<=eps)
 <=2 eps ||p_Q||_2^2
 <=4 eps sqrt(LM/|sigma|).`                                         (6.1)

In the near-coloop packet this is

`boxed:
 P(|Q-Q'|<=eps)
 <=4sqrt(e)(|sigma|m sqrt(c))^(-1/2) eps.
}`                                                                    (6.2)

The numerical outside coefficient is `4sqrt(e)=6.5948850828...`. This is linear collision small-ball scaling with no angular-cancellation denominator. No challenged partner statement is used.

## 7. Deterministic algebra and constant checks

Random orthonormal pairs `(v,q)` in dimensions `3,5,10,25` were checked. After rotating the spectral plane so the selected row is `(sqrt(c),0)`, the complement identities

`sum a_j^2=1-c`, `sum b_j^2=1`, `sum a_jb_j=0`

held to errors below `7e-16`, and the Jacobian from `(S,Z)` to `(V,H)` agreed with `m` to errors below `2e-16` in all trials. Independent arithmetic checks give

`pi sqrt(e)=5.17961063185...`,
`2sqrt(e)=3.29744254140...`,
`4sqrt(e)=6.59488508280...`,
`(16/3)sqrt(pi)e^(1/4)=12.13800423717...`,
`C_H=9.25849106530...`.

The displayed identities, not the finite checks, are the proof.

## 8. Exact remaining implication

The unrestricted three-large-eigenvalue conjecture remains **OPEN** and full-target continuity remains **OPEN**.

Within the r34 exact angular packet, every non-coloop branch was already paid in `L^infinity`; this run now stabilizes the near-coloop branch at every finite `L^p` and at the half-Riesz-potential level even when `h_r=0`. The first unpaid B03 implication is therefore sharpened to

`QFORM-NEARCOLOOP-BORDERLINE-LP-TO-LINF-v1`:

> exploit the original product provenance that produced Theorem 2.1 to upgrade the endpoint envelope `|phi(t)|<=min(1,D/|t|)` to a one-copy `L^infinity` estimate without perturbatively deleting the narrow complement direction. A merely abstract pair-density argument is insufficient; the required extra half power must come from source-level curvature/aggregation or a true additional physical square.

This agrees with the newer source-plane/source-line near-coloop work: atom-by-atom reciprocal-minor payment can lose with dimension, while whole original-coordinate bank aggregation remains stable. No easy subclass is being substituted for the full target.
