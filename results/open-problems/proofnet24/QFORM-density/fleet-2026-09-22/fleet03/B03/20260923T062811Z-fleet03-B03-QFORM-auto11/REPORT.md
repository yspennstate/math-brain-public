SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T06:28:11Z.
attacking: decoupled time integral at the angular-cancellation endpoint; derive an integrated half-Riesz/collision estimate that stays finite when a heavy physical row has h_r=0, without separating sum/difference pairs.

# fleet03/B03 auto11 — angular-cancellation integrated L2 compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T062811Z-fleet03-B03-QFORM-auto11`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREM / EXACT ANGULAR-CANCEL COLLISION ENDPOINT PAID / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


The unrestricted owner conjecture and the unrestricted continuity claim remain OPEN.

## 1. Inputs and the exact endpoint

The immediate B03 predecessor is

`yspennstate/math-open-problems@b580b09027d8c20c3d3bbea0bea6cf8caa04d541`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T045638Z-fleet03-B03-QFORM-r27/REPORT.md`.

In its exact-rank-three one-sided-overlap packet, after a genuine original-coordinate nonzero pivot `i`, the quadratic has

`Q = a^(-1) H^2 + 2 sigma U V`,                                    (1.1)

where

`H=a X_i + h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,                                              (1.2)

`u,v` are unit vectors on disjoint original-coordinate banks, and

`h_R=beta v + m q`, `q perpendicular v`, `||q||=1`, `m=rho y`,
`rho^2=a^2+||k||^2`, `y^2>1/2`.                                  (1.3)

The preceding diffuse-plane payment leaves a physical coordinate `r in R` with

`eta_r:=v_r^2+q_r^2>1/2`.                                        (1.4)

Run r27 pays every `h_r:=beta v_r+m q_r !=0` through a Schur-complement half-Riesz estimate, but its coefficient degenerates as `h_r ->0`. This run attacks the exact angular-cancellation endpoint

`h_r=0`.                                                          (1.5)

The designated partner `fleet04/B03` has one completed handoff, canonical mathematics

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`.

Its advertised weighted-L2 compiler is not used: a previous B03 run found the missing time-weight factor and wrong coefficient homogeneity. I use only the elementary valid lemma from that handoff,

`P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`.                            (1.6)

## 2. A random-slope square-times-linear integrated theorem

### Theorem 2.1 — `QFORM-RANDOM-LINEAR-RECEIVER-L2-v1`

Let `X,Z` be independent real variables with probability densities bounded by one. Let `Omega` be independent of `(X,Z)`. Let `c(Omega),d(Omega),b(Omega)` be arbitrary real measurable functions and let `a!=0`. Assume

`E |b(Omega)|^(-1/3) < infinity`.                                  (2.1)

Put

`T=a(X+c(Omega))^2 + b(Omega) Z + d(Omega)`.                       (2.2)

Then the characteristic function of `T` satisfies

`boxed:
 int_R |phi_T(t)|^2 dt
 <= 8 pi |a|^(-2/3) E|b|^(-1/3).`                                 (2.3)

Consequently `T` has an `L^2` density and

`boxed:
 ||p_T||_2^2 <=4 |a|^(-2/3) E|b|^(-1/3).`                         (2.4)

Also, without any new hypothesis,

`boxed:
 int_R |t|^(-1/2)|phi_T(t)|^2 dt
 <=4 [8pi |a|^(-2/3)E|b|^(-1/3)]^(1/2).`                          (2.5)

This is an integrated theorem; no pointwise power decay of either quadratic or linear phase is asserted.

### Proof

For fixed `omega`, write

`g_omega(t)=E_X exp(i t a(X+c(omega))^2)`,
`psi(s)=E_Z exp(i s Z)`.                                          (2.6)

Conditioning on `Omega`, then Jensen,

`|phi_T(t)|^2 <= E_Omega [ |g_Omega(t)|^2 |psi(b(Omega)t)|^2 ].`   (2.7)

We need two uniform integrated norms.

#### 2.1 Uniform L3 norm of a translated square characteristic function

Let `f<=1`, `int f=1`, and `W=(X+c)^2`. Its density for `w>0` is

`h(w)=[f(-c+sqrt(w))+f(-c-sqrt(w))]/[2sqrt(w)]`.                  (2.8)

Using `(r+s)^(3/2)<=sqrt(2)(r^(3/2)+s^(3/2))`, changing `w=y^2`, and `f^(3/2)<=f`,

`int_0^infinity h(w)^(3/2)dw
 <= int_R f(x) |x+c|^(-1/2) dx`.                                 (2.9)

Among probability densities capped by one, the last integral is maximized by filling the unit interval centered at the singularity; therefore

`int h^(3/2) <= int_(-1/2)^(1/2)|u|^(-1/2)du=2sqrt(2)`.           (2.10)

Hence

`||h||_(3/2) <=2`.                                                (2.11)

For `aW`, scaling gives `||h_a||_(3/2)<=2|a|^(-1/3)`. Interpolating the elementary Fourier bounds `L1->Linfinity` with norm one and Plancherel `L2->L2` with norm `sqrt(2pi)` gives Hausdorff--Young at `(3/2,3)` with constant `(2pi)^(1/3)`. Therefore, uniformly in the translation `c`,

`boxed: ||g_omega||_3 <=2(2pi)^(1/3)|a|^(-1/3).`                  (2.12)

#### 2.2 Uniform L6 norm of the linear characteristic function

Plancherel and `f_Z<=1` give

`int |psi(s)|^2 ds=2pi int f_Z^2 <=2pi`.                          (2.13)

Since `|psi|<=1`,

`int |psi|^6 <=2pi`, so
`||psi||_6^2 <=(2pi)^(1/3)`.                                     (2.14)

By scaling,

`||psi(b .)||_6^2 <=(2pi)^(1/3)|b|^(-1/3)`.                      (2.15)

#### 2.3 Time integration

Apply Holder to `|g|^2 |psi_b|^2` with exponents `3/2` and `3`:

`int |g_omega(t)|^2 |psi(b t)|^2 dt
 <= ||g_omega||_3^2 ||psi(b .)||_6^2
 <=8pi |a|^(-2/3)|b|^(-1/3).`                                   (2.16)

Integrating (2.7) over `t` and using Tonelli proves (2.3). Plancherel gives (2.4).

For (2.5), put `L=int|phi_T|^2`. For every `R>0`, using `|phi_T|<=1`,

`int |t|^(-1/2)|phi_T|^2
 <=4 sqrt(R)+R^(-1/2)L`.                                         (2.17)

The optimizer is `R=L/4`, giving `<=4sqrt(L)` and hence (2.5). QED.

### Why this respects the sum/difference correction

The proof never conditions on `X-X'` given `X+X'` or conversely. The only factorization is between two **genuine disjoint original coordinates** `X,Z` after conditioning the remaining original coordinates. The independent-copy identity enters only after the complete one-copy `L^2` estimate, through Plancherel/collision; all dependence internal to a duplicated coordinate pair remains untouched.

## 3. Specialization to the exact angular-cancellation endpoint

At (1.5), write

`V=v_r X_r+V_0`,                                                   (3.1)

where `V_0` does not involve `X_r`. Because `h_r=0`, the square `H` also does not involve `X_r`. Let

`H=a X_i+C`,                                                       (3.2)

where `C` involves neither `X_i` nor `X_r`. Conditional on every original coordinate except `X_i,X_r`, (1.1) becomes exactly

`Q=a(X_i+C/a)^2 + [2 sigma v_r U] X_r + 2sigma U V_0`.            (3.3)

Thus Theorem 2.1 applies with

`X=X_i`, `Z=X_r`, `b=2sigma v_r U`.                               (3.4)

The one-dimensional product-projection theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

implies for the unit projection `U=u.X_L`

`||p_U||_infinity <=sqrt(e)`.                                     (3.5)

For any density `p<=M`, probability normalization and rearrangement give

`E|Y|^(-1/3)
 <= M int_(-1/(2M))^(1/(2M)) |y|^(-1/3)dy
 =3*2^(-2/3) M^(1/3).`                                           (3.6)

With `M=sqrt(e)` and (3.4),

`E|b|^(-1/3)
 <=(2|sigma v_r|)^(-1/3) 3*2^(-2/3)e^(1/6)
 =(3/2)e^(1/6)|sigma v_r|^(-1/3).`                               (3.7)

Therefore

`boxed:
 int_R |phi_Q(t)|^2dt
 <=12pi e^(1/6)|a|^(-2/3)|sigma v_r|^(-1/3).`                    (3.8)

Numerically the outer coefficient is

`12pi e^(1/6)=44.536238331606214...`.                             (3.9)

Equivalently,

`boxed:
 ||p_Q||_2^2
 <=6 e^(1/6)|a|^(-2/3)|sigma v_r|^(-1/3).`                       (3.10)

The weighted independent-copy time integral is also finite:

`boxed:
 int |t|^(-1/2)|phi_Q(t)|^2dt
 <=8sqrt(3pi)e^(1/12)|a|^(-1/3)|sigma v_r|^(-1/6).`              (3.11)

The numerical prefactor in (3.11) is `26.69419062840639...` before the displayed coefficient powers.

## 4. New structural identity: exact angular cancellation is a heavy physical null hub

There is a useful target-level geometric fact at (1.5).

Embed the rank-two Schur vectors into the full physical space as

`u_tilde=(0,u)`, `v_tilde=(0,v)`.                                 (4.1)

Write `h=alpha u+beta v+k`, with `k perpendicular u,v`, and recall

`rho^2=a^2+||k||^2`.                                              (4.2)

Then

`w=(a,k)/rho`                                                     (4.3)

is a unit vector orthogonal to `u_tilde,v_tilde`. Since the completed-square vector `(a,h)` equals

`rho w+alpha u_tilde+beta v_tilde`,                               (4.4)

the exact rank-three range of `A` is spanned by the orthonormal triple

`{u_tilde,v_tilde,w}`.                                            (4.5)

For `r in R`, `u_r=0` and `k_r=m q_r=rho y q_r`. Hence the spectral leverage of the ORIGINAL physical coordinate `r` is exactly

`boxed:
 c_r=||P_range(A)e_r||^2=v_r^2+y^2 q_r^2.`                        (4.6)

Since `y^2>1/2` and `eta_r=v_r^2+q_r^2>1/2`,

`boxed: c_r >= y^2 eta_r >1/4.`                                  (4.7)

At the exact cancellation `h_r=0`, the physical diagonal is

`A_rr=h_r^2/a+2sigma u_rv_r=0`,                                  (4.8)

and its whole physical row is the pure star

`A_{r,L}=sigma v_r u^T`,
`A_{r,j}=0` for `j notin L`.                                     (4.9)

In particular `v_r!=0`: otherwise `h_r=m q_r=0` would force `q_r=0`, contradicting `eta_r>1/2`.

If `s_3(A)` denotes the smallest modulus among the three nonzero eigenvalues in this exact-rank-three packet, then on the range of `A`, `||Az||>=s_3(A)||z||`. Therefore

`|sigma v_r|=||Ae_r||
 >=s_3(A)||P_range(A)e_r||
 =s_3(A)sqrt(c_r)
 >s_3(A)/2.`                                                      (4.10)

Combining (4.10) with (3.8)--(3.10) removes every `v_r ->0` concern:

`int |phi_Q|^2
 <12pi 2^(1/3)e^(1/6) s_3(A)^(-1/3)|a|^(-2/3),`                  (4.11)

`||p_Q||_2^2
 <6 2^(1/3)e^(1/6) s_3(A)^(-1/3)|a|^(-2/3).`                    (4.12)

Under the target normalization `s_3(A)>=1`, the numerical constants are respectively

`56.1121441571256...` and `8.930525110091553...`.                 (4.13)

This exact identity also places the angular-cancelled row inside the fleet's heavy-null-hub geometry: it is a genuine original null coordinate of spectral leverage strictly above `1/4`, not an arbitrary small local pivot. It does **not** by itself close the true near-coloop collar, because the remaining product-provenance issue at leverage approaching one is real.

## 5. Designated partner applied: linear collision small-ball

Apply the valid `fleet04/B03` lemma (1.6) to (3.10). For an independent copy `Q'`,

`boxed:
 P(|Q-Q'|<=eps)
 <=12 e^(1/6)|a|^(-2/3)|sigma v_r|^(-1/3) eps.`                  (5.1)

Using (4.10),

`boxed:
 P(|Q-Q'|<=eps)
 <12 2^(1/3)e^(1/6)
 s_3(A)^(-1/3)|a|^(-2/3) eps.`                                  (5.2)

The normalized numerical coefficient is

`12 2^(1/3)e^(1/6)=17.861050220183106...`.                       (5.3)

Thus the exact `h_r=0` endpoint now has a dependence-safe **linear collision small-ball estimate**. This is precisely an `L^2` density certificate, not yet the one-copy `L^infinity` certificate required by the owner target.

## 6. A literal L2-to-Linfinity receiver when a genuine independent linear direction exists

For later compilation, if `W` is an additional original coordinate independent of `Q`, with density cap one, and `lambda!=0`, then

`||p_(lambda W)||_2 <= |lambda|^(-1/2)`.                          (6.1)

Therefore Young/Cauchy--Schwarz gives

`||p_(Q+lambda W)||_infinity
 <= ||p_Q||_2 ||p_(lambda W)||_2`                                (6.2)

and hence from (3.10)

`boxed:
 ||p_(Q+lambda W)||_infinity
 <= sqrt(6)e^(1/12)|lambda|^(-1/2)
    |a|^(-1/3)|sigma v_r|^(-1/6).`                               (6.3)

This shows concretely how the integrated estimate recovers one-copy linear small-ball scaling when a genuinely independent linear receiver is available. No such receiver is assumed in the bare exact-rank-three target, so (6.3) is a scoped transducer, not a full proof.

## 7. What changed and what remains

The r27 endpoint loss `|h_r|^(-1/2)` was an artifact of using a nonzero scalar Schur pivot. At the exact angular cancellation `h_r=0`, the correct mechanism is different: retain the original pivot square and use the cancelled physical coordinate as a random linear receiver. The resulting time estimate (3.8) remains finite at `h_r=0`, and the star/spectral identity (4.10) makes the linear coefficient quantitatively nondegenerate at target scale.

The exact angular-cancellation collision problem is therefore paid. The remaining target-level obstruction on this route is sharper:

`QFORM-ANGULAR-CANCEL-L2-TO-LINF-AT-NEARNULL-OUTER-PIVOT-v1` — upgrade the exact packet from (4.12) to a one-copy universal `L^infinity` bound uniformly as the outer original pivot `a ->0`, retaining the full product provenance of the rank-one square and the null-star receiver. An argument may not replace an effective scalar by a merely conditionally capped variable, delete the small nonzero pivot, or take a worst spectral-fiber supremum.

The fresh fleet03/B10 near-coloop results are consistent with this diagnosis: the hard null-hub collar is exactly where same-bank longitudinal/transverse contamination survives after all easy local pivots disappear.

**Continuity:** Theorem 2.1 yields an `L^2` density, not continuity. No continuity claim is made for this branch.  
**Full QFORM:** OPEN.  
**Independent end-to-end reviews:** none claimed; this is a supporting theorem, not a full candidate proof.

No scheduler/task state, notification/email setting, permission, public-release state, paid model/API/Codex action, installation, or cross-account authentication was changed.