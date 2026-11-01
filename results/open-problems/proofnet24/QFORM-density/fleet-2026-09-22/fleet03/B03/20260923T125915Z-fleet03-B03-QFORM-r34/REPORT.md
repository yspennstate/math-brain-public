SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T12:59:15Z.
attacking: dependence-safe time integration at the near-intersecting endpoint — first extend the physical-selector Plancherel compiler to finite-L^p coefficient laws, then close the r32 near-three-coordinate collar by a determinant-to-pivot lemma and the rank-two Schur half-Riesz receiver.

# fleet03/B03 r34 — L^p selector interpolation and uniform payment of the near-triangle collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREMS / NEAR-TRIANGLE COLLAR CLOSED IN THE EXACT ANGULAR PACKET / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


No step below uses a law-uniform pointwise van-der-Corput estimate, independence after a spectral rotation, a conditional density cap for one sum/difference variable given its conjugate, the false arbitrary-joint coarea bound, or the false single-Schur-rank-two structural implication. All stochastic selectors are genuine independent physical variables or source-proved product projections, and every Schur pivot is in an original physical coordinate.

## 1. Source-valid inputs

### 1.1 Immediate predecessor: bounded joint coefficient selector theorem

Canonical source:

`yspennstate/math-open-problems@0a2be76b2cba4f4d46b88682e196af8945db9ed1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T115729Z-fleet03-B03-QFORM-r33/REPORT.md`.

For genuine independent physical selectors `X_1,...,X_k`, independent of a background `W`, if the whole coefficient vector `C(W)` has joint density cap `M`, and

`Q=R(W)+sum_j[P_j(X_j)+2 beta_j X_j C_j(W)]`,

then

`|phi_Q(t)|^2 <= min(1, M pi^k (prod|beta_j|)^(-1) |t|^(-k)).`

The dependence among the `C_j` is retained. The present run first extends this endpoint from `L^infinity` coefficient densities to finite `L^p` coefficient densities.

### 1.2 r32 weighted-basis endpoint and stability theorem

Canonical source:

`yspennstate/math-open-problems@0ef1395ef5636eab3acb9e70130042e4dfcbb644`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T105601Z-fleet03-B03-QFORM-r32/REPORT.md`.

In the exact angular-cancellation packet

`Q = a^(-1) H^2 + 2 sigma U V`,                                      (1.1)

with disjoint original-coordinate banks and

`H=a X_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,
`h_R=beta v+m q`, `q perpendicular v`, `||v||=||q||=1`,             (1.2)

one has

`m=rho y`, `y^2>1/2`,
`(rho^2/|a|)|sigma| >= s_3(A)^2`.                                  (1.3)

For the right-bank rows `r_j=(h_j,v_j)`, let

`D_jk=det(r_j,r_k)`, `E2=sum_{j<k}D_jk^2=m^2`,
`p_jk=D_jk^2/E2`,                                                    (1.4)

and let `delta` be the probability that two iid edges under `p` are disjoint. If `delta>0`, r32 proves a continuous density bound

`||p_Q||_infinity <= 12 e^(1/3) s_3(A)^(-1) delta^(-1/3).`          (1.5)

It also proves the weighted intersection-stability alternative. Put

`c_*=(3/2)^(1/3)`,
`theta(delta)=1-delta-c_* delta^(1/3)`.                             (1.6)

Then either a row has volume-sampling incidence at least `theta(delta)` (near-coloop), or a physical triple `T` carries determinant energy

`sum_{ {j,k} subset T } D_jk^2 >= theta(delta) E2`.                 (1.7)

The near-triangle branch (1.7) was not paid uniformly in r32. It is paid below.

### 1.3 r27 physical-pivot Schur receiver

Canonical source:

`yspennstate/math-open-problems@b580b09027d8c20c3d3bbea0bea6cf8caa04d541`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T045638Z-fleet03-B03-QFORM-r27/REPORT.md`.

For any chosen right physical coordinate `j` in (1.1)-(1.2) with

`h_j=beta v_j+m q_j !=0`,
`eta_j=v_j^2+q_j^2`,                                                 (1.8)

completing the square in the actual physical coordinate `X_j` gives

`Q=d[X_j+c]^2+R`, `d=h_j^2/a`,                                     (1.9)

where the residual quadratic form has exact rank two and

`|pdet R_quad| >= sigma^2 m^2 eta_j/h_j^2`.                         (1.10)

The orientation-free rank-two half-Riesz theorem then gives

`sup_s E|R-s|^(-1/2)
 <=16 sqrt(30) sqrt( |h_j|/(|sigma|m sqrt(eta_j)) )`,               (1.11)

and, keeping an independent copy of the entire residual intact,

`int_R |t|^(-1/2)|phi_R(t)|^2 dt
 <=16 sqrt(60 pi) sqrt( |h_j|/(|sigma|m sqrt(eta_j)) ).`             (1.12)

Finally the same genuine square (1.9) yields

`||p_Q||_infinity
 <=16 sqrt(30)
   sqrt( |a|/(|sigma|m sqrt(eta_j)|h_j|) ).`                         (1.13)

This source was originally motivated by a heavy row, but the algebra (physical completion, transverse coefficient identity, and rank-two determinant identity) uses only `h_j!=0`; no lower leverage threshold is needed for (1.10)-(1.13).

### 1.4 Designated partner fleet04/B03

Canonical source:

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`.

Only its valid elementary collision lemma is used:

`P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`.                              (1.14)

Its historically stronger weighted-`L^2` compiler is not used.

## 2. First theorem: finite-L^p dependent coefficient selector compiler

The initial mechanism of this run was to weaken the `L^infinity` density hypothesis in r33. This produces a clean integrated-time ladder and is useful whenever a coefficient projection is controlled only in a finite Renyi class.

### Theorem 2.1 — `QFORM-LP-COEFFICIENT-SELECTOR-PLANCHEREL-v1`

Let `X_1,...,X_k` be independent real variables with densities `0<=f_j<=1`. Let `W` be independent of the whole selector bank. Let

`C(W)=(C_1(W),...,C_k(W))`

have a JOINT probability density `g` in `L^p(R^k)` for some `1<p<=infinity`, and write

`G=||g||_p`,
`vartheta=1-1/p` (with `vartheta=1` when `p=infinity`),
`alpha=k vartheta`,
`B=prod_j |beta_j|`.                                                (2.1)

No independence among the coordinates of `C` is assumed. Let `R(W)` be arbitrary measurable, let `beta_j!=0`, and let `P_j:R->R` be arbitrary measurable. Define

`Q=R(W)+sum_{j=1}^k [P_j(X_j)+2 beta_j X_j C_j(W)].`                (2.2)

Then for all `t!=0`,

`boxed:
 |phi_Q(t)|^2
 <= min{1, A |t|^(-alpha)},
 A=G pi^alpha B^(-vartheta).
}`                                                                  (2.3)

#### Proof

For fixed `t`, let

`F_{j,t}(xi)=int f_j(x) exp(i t P_j(x)+i xi x) dx`.                 (2.4)

Conditioning only on the whole background `W` preserves the genuine independence of the physical selectors:

`phi_Q(t)=E_W exp(itR(W)) prod_j F_{j,t}(2 beta_j t C_j(W)).`       (2.5)

Cauchy-Schwarz over the WHOLE background gives

`|phi_Q(t)|^2
 <=int g(c) prod_j |F_{j,t}(2 beta_j t c_j)|^2 dc`.                 (2.6)

Let `p'=p/(p-1)`, so `1/p'=vartheta`. Holder in the joint coefficient variable gives

`(2.6)
 <=G || prod_j |F_{j,t}(2 beta_j t c_j)|^2 ||_{p'}`.                (2.7)

The deterministic `c` integration factorizes. Since `|F_{j,t}|<=1` and, by Plancherel and `f_j<=1`,

`int |F_{j,t}(xi)|^2 dxi
 =2pi int f_j(x)^2 dx <=2pi`,                                      (2.8)

we have for `2p'>=2`

`int |F_{j,t}|^(2p') <=2pi`.                                       (2.9)

Therefore

`|| prod_j |F_{j,t}(2 beta_j t c_j)|^2 ||_{p'}
 =prod_j [ (2|beta_j t|)^(-1)
            int |F_{j,t}(xi)|^(2p') dxi ]^(1/p')`

`<=prod_j [pi/(|beta_j t|)]^vartheta
 =pi^alpha B^(-vartheta)|t|^(-alpha).`                             (2.10)

Together with `|phi_Q|<=1`, this proves (2.3). QED.

The proof never conditions on a conjugate sum/difference coordinate. Equivalently, when one reads `|phi_Q(t)|^2=E exp(it(Q-Q'))`, the **whole copy difference** is retained; the estimate is obtained by a joint coefficient-space Holder step, not by falsely splitting dependent coordinates of one pair.

### 2.2 Exact weighted independent-copy integral

For every `0<gamma<alpha`, split (2.3) at

`T=A^(1/alpha)=pi G^(1/alpha) B^(-1/k)`.                            (2.11)

Then

`boxed:
 int_R |t|^(gamma-1)|phi_Q(t)|^2 dt
 <= [2 alpha/(gamma(alpha-gamma))]
    A^(gamma/alpha).
}`                                                                  (2.12)

Indeed the two pieces are

`2 int_0^T t^(gamma-1)dt`

and

`2A int_T^infinity t^(gamma-alpha-1)dt`,

which combine exactly to (2.12). This is a full-time integrated estimate, not a truncated or pointwise stationary-phase assertion.

At `gamma=1/2` it is available whenever `alpha>1/2`.

### 2.3 L^2 and partner collision threshold

If `alpha>1`, then integrating (2.3) without a weight gives

`int |phi_Q|^2
 <=2 alpha/(alpha-1) A^(1/alpha)`.                                 (2.13)

By Plancherel, `Q` has an `L^2` density and

`boxed:
 ||p_Q||_2^2
 <= [alpha/(alpha-1)]
    G^(1/alpha) B^(-1/k).
}`                                                                  (2.14)

Applying the designated fleet04/B03 lemma (1.14) gives the actual inequality

`boxed:
 P(|Q-Q'|<=eps)
 <= [2 alpha/(alpha-1)]
    G^(1/alpha) B^(-1/k) eps.
}`                                                                  (2.15)

For `k=2`, the threshold `alpha>1` is exactly `p>2`.

### 2.4 One-copy half-Riesz receiver from the squared envelope

Taking square roots in (2.3),

`|phi_Q(t)|<=min(1,A^(1/2)|t|^(-alpha/2)).`                         (2.16)

If `alpha>1`, then

`int_R |t|^(-1/2)|phi_Q(t)|dt
 <=[4 alpha/(alpha-1)] A^(1/(2alpha)).`                             (2.17)

Using

`int_R |t|^(-1/2)e^(itx)dt=sqrt(2pi)|x|^(-1/2)`                    (2.18)

in the standard truncated Riesz representation yields, uniformly in every translate `s`,

`boxed:
 sup_s E|Q-s|^(-1/2)
 <=[2 sqrt(2) alpha/(alpha-1)]
    G^(1/(2alpha)) B^(-1/(2k)).
}`                                                                  (2.19)

This is the key output-side receiver derived from the dependence-safe **squared-characteristic envelope** (2.3).

### 2.5 Linear one-copy small-ball after one genuine physical square

Let `Z` be one additional original cap-one coordinate, independent of every variable used in `Q`, let `h` be arbitrary measurable in the other variables, and put

`T=d[Z+h]^2+Q`, `d!=0`.                                             (2.20)

The conditional square pushforward obeys

`p_{d[Z+h]^2}(u | others) <= |d|^(-1/2)|u|^(-1/2)`.                (2.21)

Combining with (2.19), for `alpha>1`,

`boxed:
 ||p_T||_infinity
 <=[2 sqrt(2) alpha/(alpha-1)]
   |d|^(-1/2) G^(1/(2alpha)) B^(-1/(2k)).
}`                                                                  (2.22)

Hence for every interval `I`,

`P(T in I) <= RHS(2.22) |I|`.                                      (2.23)

Thus the finite-`L^p` squared-characteristic estimate recovers the assignment's **linear one-copy small-ball scaling** without any sum/difference independence. For two selectors this works for every coefficient density in `L^p`, `p>2`.

### 2.6 Direct bounded continuous density threshold

If `alpha>2`, then `phi_Q in L^1`, and direct integration of (2.16) gives

`boxed:
 ||p_Q||_infinity
 <=[alpha/(alpha-2)] G^(1/alpha) B^(-1/k).
}`                                                                  (2.24)

The density is continuous and vanishes at infinity. For three selectors, the finite-`L^p` threshold is `p>3`. At `p=infinity`, (2.24) becomes the r33 constant `3(M/B)^(1/3)`.

The finite-`L^p` extension is rigorous but, by itself, does not solve the r32 `delta->0` structural collar. In particular, merely weakening `L^infinity` to finite `L^p` does not manufacture a uniformly nondegenerate coefficient map from the spectral hypothesis. I therefore changed mechanism on the same target and attacked the near-triangle collar directly.

## 3. Determinant energy of a physical triple forces a usable pivot

The following deterministic lemma is the new structural bridge.

### Lemma 3.1 — `QFORM-TRIPLE-ENERGY-TO-PIVOT-v1`

In the exact packet (1.1)-(1.4), define the two-plane physical rows

`z_j=(v_j,q_j) in R^2`,
`eta_j=||z_j||^2=v_j^2+q_j^2`.                                     (3.1)

Because `v,q` are orthonormal,

`sum_j z_j z_j^T=I_2`.                                             (3.2)

Also, with `c=(beta,m)`,

`h_j=c.z_j`, `||c||=S=sqrt(beta^2+m^2)>=m`.                        (3.3)

Suppose a physical triple `T` satisfies

`sum_{ {j,k} subset T} D_jk^2 >= theta m^2`                        (3.4)

for some `theta>0`. Then there exists `j in T` such that

`boxed:
 |h_j| >= sqrt(theta/3) S,
 eta_j >= theta/3,
 m sqrt(eta_j)|h_j| >= (theta/3)m^2.
}`                                                                  (3.5)

#### Proof

Since `h_j=beta v_j+m q_j`,

`D_jk=h_j v_k-h_k v_j
     =m(q_j v_k-q_k v_j)`,                                         (3.6)

so (3.4) is equivalent to

`sum_{ {j,k} subset T} det(z_j,z_k)^2 >= theta`.                   (3.7)

Let

`G_T=sum_{j in T} z_j z_j^T`.                                      (3.8)

By the two-dimensional Cauchy-Binet identity,

`det G_T=sum_{ {j,k} subset T}det(z_j,z_k)^2 >=theta`.             (3.9)

From (3.2), `0<=G_T<=I_2`. If its eigenvalues are `lambda_1<=lambda_2<=1`, then

`lambda_1=det(G_T)/lambda_2 >=theta`.                               (3.10)

Therefore

`G_T>=theta I_2`.                                                   (3.11)

Using (3.3),

`sum_{j in T} h_j^2=c^T G_T c >=theta S^2`.                        (3.12)

Some `j in T` has

`|h_j|>=sqrt(theta/3)S`.                                            (3.13)

For the same `j`, Cauchy-Schwarz gives

`h_j^2=(c.z_j)^2<=S^2 eta_j`,                                      (3.14)

hence `eta_j>=theta/3`. Multiplying the two lower bounds and using `S>=m` gives

`m sqrt(eta_j)|h_j|
 >=m sqrt(theta/3) sqrt(theta/3) S
 =(theta/3)mS
 >=(theta/3)m^2`.                                                   (3.15)

QED.

This lemma is important because it converts an **aggregate three-coordinate determinant certificate** into exactly the product `m sqrt(eta_j)|h_j|` needed by the physical Schur half-Riesz receiver. No inverse of a tiny individual determinant is paid.

## 4. Uniform density payment of the near-triangle collar

### Theorem 4.1 — `QFORM-NEAR-TRIANGLE-SCHUR-HALFRIESZ-v1`

Assume the exact angular packet (1.1)-(1.3) and suppose a physical triple satisfies (3.4). Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=96 sqrt(5) theta^(-1/2) s_3(A)^(-1).
}`                                                                  (4.1)

No continuity assertion is made by this square-transducer proof.

#### Proof

Lemma 3.1 supplies `j` with `h_j!=0` and

`m sqrt(eta_j)|h_j| >=(theta/3)m^2`.                               (4.2)

Apply the r27 physical-pivot receiver (1.13):

`||p_Q||_infinity
 <=16 sqrt(30)
   sqrt( |a|/(|sigma|m sqrt(eta_j)|h_j|) )`

`<=16 sqrt(30)
   sqrt( 3|a|/(theta |sigma|m^2) ).`                               (4.3)

Now (1.3) and `m^2=rho^2 y^2>rho^2/2` imply

`|sigma|m^2/|a|
 > (1/2) s_3(A)^2`,                                                 (4.4)

or

`|a|/(|sigma|m^2) <2 s_3(A)^(-2)`.                                (4.5)

Insert this in (4.3):

`||p_Q||_infinity
 <=16 sqrt(180) theta^(-1/2) s_3(A)^(-1)
 =96 sqrt(5) theta^(-1/2) s_3(A)^(-1).`                            (4.6)

QED.

Numerically the base coefficient is

`96 sqrt(5)=214.66252583997982...`.                                (4.7)

### 4.2 Dependence-safe time integral in the pivoted residual

The same selected physical coordinate `j` has the r27 residual estimate (1.12):

`boxed:
 int_R |t|^(-1/2)|phi_R(t)|^2 dt
 <=16 sqrt(60 pi)
    sqrt( |h_j|/(|sigma|m sqrt(eta_j)) ).
}`                                                                  (4.8)

The identity used here is only

`|phi_R(t)|^2=E exp(it(R-R'))`                                     (4.9)

for an independent copy of the **whole residual**. There is no operation that treats a coordinate difference and its conjugate sum as independent.

The residual half-Riesz receiver and the genuine physical square in (1.9) are what convert this decoupled-time geometry into the linear output small-ball statement (4.1). The causal proof of (4.1) uses the translation-uniform one-copy potential (1.11); (4.8) is the assignment's independent-copy integrated certificate for exactly the same pivoted residual.

Once (4.1) is known, the complete output itself also has a dependence-safe half-Riesz copy-energy bound. Since `p_{Q-Q'}=p_Q*tilde p_Q` has density cap at most `C=||p_Q||_infinity`, any probability density `r<=C` obeys

`int |x|^(-1/2)r(x)dx <=4 sqrt(C)`                                 (4.10)

(split at `R=1/(4C)`). Hence

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <=4 sqrt(2pi C)
 <=4 sqrt(192 pi sqrt(5))
    theta^(-1/4)s_3(A)^(-1/2).
}`                                                                  (4.11)

The outside numerical coefficient in the last line is

`146.90211316981492...`.                                           (4.12)

This last estimate is a consequence, not the proof, of the density bound; it is recorded to give the whole-output time scale explicitly.

### 4.3 Designated partner applied to an actual new inequality

By (1.14) and `||p_Q||_2^2<=||p_Q||_infinity`, Theorem 4.1 gives

`boxed:
 P(|Q-Q'|<=eps)
 <=192 sqrt(5) theta^(-1/2)s_3(A)^(-1) eps.
}`                                                                  (4.13)

This is a genuine new partner-consumed linear collision estimate in the near-triangle collar. No challenged partner compiler is used.

## 5. Combined compiler: the entire non-coloop part of the r32 collar is now uniform

The r32 positive-`delta` Fourier theorem and Theorem 4.1 splice cleanly.

### Theorem 5.1 — `QFORM-ANGULAR-PACKET-NONCOLOOP-COMPILER-v1`

In the exact angular packet (1.1)-(1.4), one of the following holds:

1. `delta>=1/64`, in which case

   `||p_Q||_infinity
    <=48 e^(1/3) s_3(A)^(-1)
    =66.98939640413229... s_3(A)^(-1)`;                             (5.1)

2. `delta<1/64` and the r32 stability theorem selects the near-triangle alternative, in which case

   `||p_Q||_infinity
    <96 sqrt(15/2) s_3(A)^(-1)
    =262.9068276024797... s_3(A)^(-1)`;                             (5.2)

3. `delta<1/64` and the r32 stability theorem selects a near-coloop row.

Consequently, **outside the near-coloop alternative, the entire exact angular-cancellation packet is paid by the universal constant `<263/s_3(A)`**.

#### Proof

Case 1 is immediate from r32 (1.5), since `(1/64)^(-1/3)=4`.

For case 2, if `delta<1/64`, then `delta^(1/3)<1/4`. Since

`c_*=(3/2)^(1/3)<6/5`,                                             (5.3)

we have

`theta(delta)
 >1-1/64-(6/5)(1/4)
 =1-1/64-3/10
 >2/3`.                                                             (5.4)

The r32 near-triangle alternative is precisely (3.4) with `theta=theta(delta)`. Theorem 4.1 therefore gives

`||p_Q||_infinity
 <96 sqrt(5) (2/3)^(-1/2)s_3(A)^(-1)
 =96 sqrt(15/2)s_3(A)^(-1)`.                                      (5.5)

The only remaining case is the near-coloop alternative. QED.

At the same `theta>=2/3` scale, the partner collision estimate (4.13) is

`P(|Q-Q'|<=eps)
 <192 sqrt(15/2)s_3(A)^(-1) eps
 =525.8136552049594... s_3(A)^(-1) eps.`                            (5.6)

## 6. Exact meaning of the remaining near-coloop case

There is a useful simplification that should be retained by the next run. The r32 incidence leverage for row `r_j=(h_j,v_j)` is actually the physical two-plane leverage `eta_j`.

Indeed, with

`z_j=(v_j,q_j)`,
`T=[[beta,m],[1,0]]`,
`r_j=T z_j`,                                                        (6.1)

we have

`G=sum_j r_j r_j^T=T T^T`                                         (6.2)

because `sum z_j z_j^T=I_2`. Since `m>0`, `T` is invertible, and

`r_j^T G^(-1)r_j
 =z_j^T T^T(TT^T)^(-1)Tz_j
 =||z_j||^2
 =eta_j.`                                                           (6.3)

Thus after the present near-triangle payment, the **only** r32 collar left is a genuine original-coordinate physical row with

`eta_j >= theta(delta) >2/3`                                       (6.4)

and, if r27 does not already pay it, simultaneous angular cancellation

`|h_j|=|beta v_j+m q_j| << sqrt(beta^2+m^2)`.                      (6.5)

This is much narrower than the previous `delta->0` statement. It is the exact high-leverage / near-orthogonality endpoint to attack next. The complement two-plane covariance is `I-z_j z_j^T`; in the exact-coloop limit `eta_j=1`, every remaining row is collinear with the line orthogonal to `z_j`. Any next proof must aggregate that complementary one-dimensional product bank rather than invert one small residual coordinate.

## 7. Why the finite-L^p attempt was not declared closure

Theorem 2.1 is a genuine strengthening of r33, but it does not by itself imply that a bare three-large-eigenvalue matrix produces the required selector/coefficient geometry. In a full-rank linear coefficient map, replacing an `L^infinity` projection density by `L^p` changes the time exponent and Renyi norm together; it does not automatically remove determinant or near-coloop degeneracy. Claiming otherwise would repeat the source's warning against paying a fragile local minor before aggregation.

The run therefore preserved the finite-`L^p` theorem as a reusable analytic tool and changed mechanism to the aggregate triple-energy certificate (Lemma 3.1), which directly closes one of the two structural collars from r32.

## 8. Status and next implication

What is proved here:

- `QFORM-LP-COEFFICIENT-SELECTOR-PLANCHEREL-v1`, including a full weighted independent-copy time estimate, exact `L^2`, one-copy half-Riesz, square-transduced linear small-ball, and direct-continuity thresholds;
- `QFORM-TRIPLE-ENERGY-TO-PIVOT-v1`;
- `QFORM-NEAR-TRIANGLE-SCHUR-HALFRIESZ-v1`;
- `QFORM-ANGULAR-PACKET-NONCOLOOP-COMPILER-v1`: within the exact r32 angular-cancellation packet, every branch except near-coloop is uniformly paid by `<263/s_3(A)`.

What is NOT proved:

- the unrestricted QFORM density conjecture;
- full-target continuity;
- a universal structural reduction of every matrix under the target assumptions to the exact angular packet;
- the remaining near-coloop / angular-cancellation endpoint.

The next B03 implication is now sharply stated:

> Assume an actual physical right-bank row has `eta_j>2/3` while `h_j=beta v_j+m q_j` is small or zero. Aggregate the complementary original-coordinate bank (which becomes nearly one-dimensional in the `(v,q)` plane as `eta_j->1`) together with the hub square and bilinear term, and prove a half-Riesz or direct small-ball bound stable as `h_j->0`, without deleting the transverse term or imposing a conditional sum/difference density cap.

The full conjecture remains **OPEN**. Continuity is proved by r32 on the positive-disjoint-basis branch and by Theorem 2.1 when `alpha>2`; Theorem 4.1 itself establishes essential boundedness only.
