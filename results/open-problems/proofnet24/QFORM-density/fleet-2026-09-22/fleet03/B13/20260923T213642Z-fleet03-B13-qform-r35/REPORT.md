# fleet03/B13 r35 — constructive cellular purification and exact-rank-two endpoint consequences

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws  
Run: `20260923T213642Z-fleet03-B13-qform-r35`  
Status: **PROVED SUPPORTING REDUCTION / FULL QFORM OPEN**  
Continuity: **not proved globally in this run**.

## 1. Scope and source-pinned inputs

The target is unchanged. The coordinates are independent ORIGINAL real coordinates, each marginal has a probability density `0<=f_i<=1`, and `A=A^T` has at least three eigenvalues of absolute value at least one. No moment, compact-support, connected-support, Gaussian, log-concave, iid, or rotated-coordinate independence assumption is used.


The designated partner input is fleet04/B13:

- underlying report `yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`.

In its diffuse exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`, `s_3(A)>=1`,

it selects an original coordinate `k` with `|d_k|>=1` and proves, for slab ratio `rho`,

`|A_kk det Lambda| <= 1536 e^2 rho^(-4)`,                                      (1.1)

hence the quantitative alternative

`|A_kk| <= C0 rho^(-2)`, `C0=106.534456`,                                      (1.2a)

or

`dist_op(U Lambda U^T,{rank<=1}) <= C1 rho^(-1)`, `C1=10.321553`.                (1.2b)

The previous B13 local compiler is also used below: if an ORIGINAL-coordinate `3x3` principal block `B` has `sigma_min(B)>=s>0`, then the full ambient quadratic law has density cap

`||p_Q||_infty <= K3/s`, `K3=128*2^(1/4)=152.218510720348...`.                  (1.3)

The one-dimensional bounded-density projection theorem used in the programme gives `||p_{a dot X}||_infty <= sqrt(2)/||a||_2` for independent cap-one coordinates.

## 2. Constructive equal-cell purification

The earlier bathtub theorem identifies product indicators as the right extremal class. The result below strengthens that reduction in a way useful for geometry: one may restrict further to unit-measure sets made from finitely many **equal cells of one lattice grid**. No optimizer, threshold level, interval extremality, support diameter, or fixed fragment count is assumed.

For an integer `m>=1`, define

`I_{m,j}=[j/m,(j+1)/m)`, `j in Z`,

and let `C_m` be the class of all sets

`E=union_{j in S} I_{m,j}` with `S subset Z`, `|S|=m`.                            (2.1)

Every `E in C_m` has Lebesgue measure one.

### Theorem 2.1 — `QFORM-SYSTEMATIC-CELLULAR-EXTREMAL-MIXTURE-v1`

Let `n<infinity` and let `0<=K(x)<=1` be any measurable kernel on `R^n`. Let

`P={f:R-> [0,1] measurable : integral f=1}`.

Then

`boxed:
 sup_{f_1,...,f_n in P} integral K(x) prod_i f_i(x_i) dx
 = sup_{m>=1} sup_{E_1,...,E_n in C_m}
     integral K(x) prod_i 1_{E_i}(x_i) dx.`                       (2.2)

In particular, for `K=1_{x^T A x in J}`, the full cap-one product slab supremum equals the supremum over products of equal-cell unit sets. The cells may be arbitrarily far apart and `m` is not bounded.

### Proof

Fix one `f in P`. For integer `m>=1`, let `P_m f` be its average on each grid cell:

`(P_m f)(x)=m integral_{I_{m,j}} f(t)dt`, `x in I_{m,j}`.                         (2.3)

Write

`p_j=m integral_{I_{m,j}} f(t)dt`.                                                (2.4)

Then `0<=p_j<=1` and `sum_{j in Z} p_j=m`.

We first realize `P_m f` as an **exact barycenter** of indicators from `C_m`. Enumerate `Z` as `j_1,j_2,...`, put `a_0=0`, `a_r=sum_{q<=r}p_{j_q}`, and form half-open intervals

`J_r=[a_{r-1},a_r) subset [0,m)`.                                                  (2.5)

They partition `[0,m)` modulo endpoints and each has length at most one. Let `U` be uniform on `[0,1)`. Select index `j_r` iff `J_r` contains one of

`U,U+1,...,U+m-1`.                                                               (2.6)

Because `|J_r|<=1`, one `J_r` cannot contain two of these points. Every one of the `m` points belongs to exactly one `J_r`. Hence exactly `m` distinct indices are selected almost surely. Call the resulting set of integers `S_m(U)` and put

`E_m(U)=union_{j in S_m(U)} I_{m,j} in C_m`.                                      (2.7)

For a fixed `r`, the sets `(J_r-l) cap [0,1)`, `l=0,...,m-1`, are disjoint modulo endpoints and have total length `|J_r|=p_{j_r}`. Therefore

`P(j_r in S_m(U))=p_{j_r}`.                                                       (2.8)

Consequently, pointwise off grid boundaries,

`E_U[1_{E_m(U)}(x)] = P_m f(x)`.                                                  (2.9)

This is the promised exact systematic-sampling barycenter.

Next, `P_m f -> f` in `L^1(R)`. Indeed `P_m` is an `L^1` contraction: on each cell, Jensen/triangle gives

`integral_{I_{m,j}} |P_m h| <= integral_{I_{m,j}} |h|`,                          (2.10)

hence `||P_m h||_1<=||h||_1`. Approximate `f` in `L^1` by `g in C_c(R)`. Uniform continuity of `g` gives `||P_m g-g||_1->0`; therefore

`||P_m f-f||_1 <= 2||f-g||_1+||P_m g-g||_1 ->0`.                                (2.11)

Now take `f_1,...,f_n in P`, and use the same `m` for all coordinates. Since every factor is a probability density,

`||prod_i P_m f_i - prod_i f_i||_{L^1(R^n)}
 <= sum_i ||P_m f_i-f_i||_1 ->0`,                                                 (2.12)

by the usual telescoping expansion. Let the systematic-sampling variables `U_1,...,U_n` be independent. From (2.9) and Tonelli,

`integral K prod_i P_m f_i
 = E_U[ integral K prod_i 1_{E_{i,m}(U_i)} ].`                                    (2.13)

The right side is an average of cellular product-indicator values, hence is at most the right side of (2.2). Passing `m->infinity` using (2.12) proves `<=` in (2.2). The reverse inequality is immediate because every `1_E`, `E in C_m`, itself belongs to `P`. QED.

### Corollary 2.2 — exact lattice-box form of the geometric problem

For `E_i in C_m`, write its selected integer set as `S_i`, `|S_i|=m`. Under density `1_{E_i}`, one may write exactly

`X_i=(K_i+V_i)/m`,                                                               (2.14)

where the `K_i` are independent and uniform on `S_i`, the `V_i` are iid uniform on `[0,1)`, and `K,V` are independent. Hence for an interval `J`,

`P(X^T A X in J)
 = m^{-n} sum_{k in S_1 x ... x S_n}
   |{v in [0,1)^n : (k+v)^T A (k+v) in m^2 J}|.`                                (2.15)

Thus the unresolved geometric inequality can be posed as a discrete-continuous sublevel-set bound on arbitrary finite integer sets `S_i`, each of cardinality `m`. Equation (2.15) is an exact identity, not a Monte Carlo or interval-extremality assertion.

## 3. Partner theorem applied to an actual inequality

The partner dichotomy (1.2) becomes more informative after a deterministic row-energy computation. Put

`R=U Lambda U^T`, `u=u_k`, `c=||u||_2^2<=1/3`, `a=A_kk`, `d=d_k`, `r=R_kk=a-d`.

The off-diagonal part of row `k` of the rank-two carrier obeys the exact identity

`||R_{k,-k}||_2^2
 = u^T Lambda (I-u u^T) Lambda u
 = ||Lambda u||_2^2-r^2`.                                                        (3.1)

By Cauchy,

`r^2=(u^T Lambda u)^2 <= c ||Lambda u||_2^2`,                                   (3.2)

so

`boxed:
 ||R_{k,-k}||_2^2 >= (1/c-1) r^2 >= 2 (|d|-|a|)_+^2.`                           (3.3)

Since the partner chooses `|d|>=1`, its near-null branch (1.2a) yields the actual target-level inequality

`boxed:
 ||R_{k,-k}||_2^2
 >= 2(1-C0 rho^{-2})_+^2.`                                                       (3.4)

Thus near cancellation of a large physical diagonal by a diffuse rank-two carrier cannot be isolated: it forces order-one aggregate crossing out of that same original coordinate.

Let

`W_k=sum_{j != k} R_{kj} X_j`.                                                    (3.5)

`W_k` is independent of `X_k`. The one-dimensional bounded-density projection theorem and (3.4) give, whenever `C0 rho^{-2}<1`,

`boxed:
 ||p_{W_k}||_infty
 <= sqrt(2)/||R_{k,-k}||_2
 <= 1/(1-C0 rho^{-2}).`                                                          (3.6)

For the safe numerical threshold `rho>=20.644`, one has

`C0 rho^{-2}<1/4`, `||R_{k,-k}||_2^2>9/8`, and `||p_{W_k}||_infty<4/3`.          (3.7)

This does **not** by itself bound the indefinite quadratic pushforward: the correction forbidding that inference remains in force. It does identify a genuinely bounded-density transverse linear form in the near-null branch.

### Lemma 3.2 — the near-rank-one branch forces two large diagonal sites

Assume instead (1.2b), and put `beta=C1/rho`. Since `R` is symmetric, spectral truncation supplies a symmetric rank-at-most-one `S` with

`||R-S||_op<=beta`.                                                              (3.8)

Weyl's inequality gives

`s_3(D+S) >= s_3(A)-beta >= 1-beta`.                                             (3.9)

For a rank-one perturbation, the singular-value rank inequality gives

`s_3(D+S) <= s_2(D)`.                                                            (3.10)

Therefore

`boxed: s_2(D)>=1-C1/rho.`                                                       (3.11)

Equivalently, at least two ORIGINAL diagonal coefficients satisfy

`|d_i|>=1-C1/rho`.                                                               (3.12)

At `rho>=20.644`, `C1/rho<1/2`, so the near-rank-one branch contains at least two physical diagonal coefficients of modulus `>1/2` while the full rank-two carrier lies within `0.5000...` (and asymptotically `O(rho^-1)`) in operator norm of a rank-one carrier.

### Corollary 3.3 — cellular exact-rank-two endpoint

By Theorem 2.1, any strict cap-one product slab witness may be replaced, with arbitrarily small loss in slab ratio and unchanged `A,J`, by a cellular product witness. Applying fleet04/B13's completed exact-rank-two theorem to that **actual cellular slab inequality**, then (3.4)-(3.12), and finally sending the approximation loss to zero, yields the following optimizer-free alternative in the diffuse exact-rank-two chamber, for `rho>=20.644`:

1. **near-null/crossing branch:** an original coordinate `k` has `|d_k|>=1`, `|A_kk|<=C0 rho^-2`, and its off-diagonal rank-two crossing satisfies `||R_{k,-k}||_2^2>9/8`; the transverse linear form `W_k` has density cap `<4/3`; or
2. **near-rank-one/two-diagonal branch:** the carrier is within `C1/rho` of symmetric rank one and at least two original diagonal coefficients have modulus at least `1-C1/rho>1/2`.

This is the requested application of a completed partner result to explicit inequalities. It does not claim either branch alone settles QFORM.

## 4. Support-free local absorption of the r33 small twist

The r33 normal form gives, after at most four physical hubs and for `rho>=12 sqrt(pi)`, a complement `K` with

`A[K,K]=A0+E`, `A0=D+R`, `R=R^T`, `rank R<=2`,

`||E||_F <= 671.513466699972 rho^(-3/2)`.                                         (4.1)

A global perturbative deletion of `E` is invalid on arbitrarily translated/fragmented supports. Nevertheless **local coefficient tests are stable without any support radius**. For every physical triple `I subset K`, Weyl gives

`sigma_min(A0[I,I])
 <= sigma_min(A[I,I])+||E[I,I]||_op
 <= sigma_min(A[I,I])+||E||_F`.                                                   (4.2)

If the slab ratio is `rho`, the local principal compiler (1.3) forbids `sigma_min(A[I,I])>K3/rho`. Hence every such model triple satisfies

`boxed:
 sigma_min((D+R)[I,I])
 <= 128*2^(1/4) rho^(-1)+||E||_F.`                                                (4.3)

Using (4.1),

`boxed:
 sigma_min((D+R)[I,I])
 <= 152.218510721 rho^(-1)+671.513466700 rho^(-3/2).}`                            (4.4)

This is a legitimate way to absorb the twist in a **finite physical coefficient certificate**; it never replaces the random quadratic term `X^T E X` by zero. The distinction matters because tiny remote support fragments can make support-weighted perturbation errors arbitrarily large.

## 5. What changed and what remains

This run changes mechanism from repeated global small-tail perturbation attempts to a constructive extremal-law discretization plus exact endpoint algebra.

The new durable facts are:

- arbitrary cap-one product slab optimization is exactly reducible to products of unit sets made of exactly `m` equal lattice cells, with common `m` allowed to tend to infinity;
- in the partner's diffuse exact-rank-two near-null branch, the cancelling physical coordinate exports order-one `l^2` crossing and hence a uniformly bounded-density linear projection;
- in its near-rank-one branch, the spectral three-mode condition forces at least two large original diagonal sites;
- the r33 `o(1/rho)` Frobenius twist may be safely absorbed in any already-finite principal-block certificate via (4.3), without a support diameter.

The exact cellular representation also shows why interval extremality cannot be inserted: the selected integer cells in (2.15) may be arbitrarily separated, and different coordinates may use unrelated sets.

The next B13 target is

`QFORM-CELLULAR-CROSS-OR-TWO-DIAGONAL-GLUE-v1`:

turn either (i) the near-null branch's bounded-density transverse linear form plus the remaining rank-two structure, or (ii) the near-rank-one branch's two large physical diagonal sites plus its retained second mode, into a third independent smoothing direction. The receiver must remain uniform under arbitrary affine translations/cell centers and may not delete the `O(rho^-3/2)` twist on unbounded inputs.

**Full QFORM remains OPEN / not proved / not disproved. Global continuity remains OPEN.**
