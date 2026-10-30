SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-24T02:33:49Z.
attacking: turn the exact-rank-two hard survivor into a uniform all-pairs cancellation law after finitely many physical deletions, then force a two-projective-line normal form without selecting a tiny minor.

# fleet03/B13 r41 — low-leverage all-pair tau control and a ten-center two-line normal form

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T023349Z-fleet03-B13-qform-r41`  
Role: extremal product laws / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW TARGET-LEVEL STRUCTURAL THEOREMS IN THE EXACT DIAGONAL+RANK-TWO HARD CHAMBER / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation independence, interval extremality, bounded support diameter, fixed fragment count, or deletion of a coefficient-small quadratic tail is used. The only basis rotation is a deterministic rotation in the two-dimensional coefficient factorization of a rank-two matrix; the independent physical variables are never rotated.

## 1. Source-pinned premises actually used


### Designated partner fleet04/B13

Canonical source:

`yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260923T201653Z-fleet04-B13-extremal-slab-dichotomy-r1/REPORT.md`.

It proves the optimizer-free cap-one product reduction and, in the diffuse exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i c_i<=1/3`, `c_i=||u_i||_2^2`, `s_3(A)>=1`,

selects a physical coordinate `k` with `|d_k|>=1` and proves for every slab ratio

`rho=P{X^T A X in J}/|J|`

that

`|A_kk det Lambda| <=1536 e^2 rho^(-4)`.                         (1.1)

Put

`H0=sqrt(1536 e^2)=106.534455308869...`.                          (1.2)

Hence either

`dist_op(U Lambda U^T, SymRank_{<=1}) <=10.321552951 rho^(-1)`,   (1.3)

or in the hard non-rank-one branch

`|det Lambda|>H0 rho^(-2)`, `|A_kk|<=H0 rho^(-2)`.                (1.4)

The present run applies (1.4) to an actual inequality in Section 3.

### Grouped three-leaf receiver

Canonical source:

`yspennstate/math-open-problems@38a8a2ae1cb319211ab4be60f6f8d6f7f03f85f9`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T223205Z-fleet01-B13-qform-auto11/REPORT.md`.

For a physical triple `L={k,i,j}` and complement `I`, define

`q_ab=det(u_a,u_b)^2`,
`Delta_ij=det(U_I^T U_I)`,
`tau_ij=d_k q_ij+d_i q_kj+d_j q_ki`.                              (1.5)

When the triple and complement span the latent two-space, its grouped theorem gives

`Delta_ij (det Lambda)^2 |tau_ij| <= C_T rho^(-5)`,               (1.6)

where

`C_T=759375/2=379687.5`.                                          (1.7)

This is an aggregate complement-volume theorem. No individual physical minor is inverted.

## 2. Extremal product-law reduction retained exactly

The designated fleet04/B13 theorem proves, for every nonnegative measurable kernel `K`,

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i
 =sup_{|E_i|=1} int_{prod_i E_i} K`.                              (2.1)

Thus for the slab kernel `K=1_{x^T A x in J}`, every strict cap-one product-law violation transfers, with arbitrarily small prescribed loss if needed, to arbitrary unit-measure product indicators. Bounded finite-union epsilon-witnesses are available, but there is no centered-interval, common-diameter, or uniform-fragment-count conclusion.

All new results below are coefficient inequalities depending only on `A`, so they pass unchanged through this optimizer-free reduction.

## 3. New theorem: uniform all-pair cancellation after finitely many high-leverage rows

Assume the hard branch (1.4). If `c_k=0`, then `A_kk=d_k`, so `|d_k|>=1` and (1.4) imply

`rho<=sqrt(H0)=10.321552951...`.                                  (3.1)

Hence every putative large-ratio hard survivor has `c_k>0`.

Rotate only the latent coefficient basis so

`u_k=(sqrt(c),0)`, `c=c_k>0`.                                     (3.2)

For `i!=k`, write

`u_i=(x_i,y_i)`, `s_i=y_i^2`.                                    (3.3)

When `s_i>0`, put `t_i=x_i/y_i`. Then

`q_ki=c s_i`,
`q_ij=s_i s_j (t_i-t_j)^2`.                                      (3.4)

### Theorem 3.1 — `QFORM-LOWLEVERAGE-ALLPAIR-TAU-v1`

Fix `0<eta<1/3`. For any two distinct physical indices `i,j!=k` satisfying

`c_i<=eta`, `c_j<=eta`, `s_i s_j>0`,                              (3.5)

one has

`boxed:
 |tau_ij|
 < [C_T/(H0^2(2/3-2eta)^2)] rho^(-1).}`                          (3.6)

In particular, with `eta=1/4`,

`boxed: |tau_ij| < C_* rho^(-1)}`,                                (3.7)

where

`C_* =36 C_T/H0^2
     =2278125/(256 e^2)
     =1204.338641107064...`.                                      (3.8)

Moreover there are at most seven indices `i!=k` with `c_i>1/4`.

#### Proof

Let

`I=[n]\{k,i,j}`.

Parseval gives

`U_I^T U_I=I_2-u_k u_k^T-u_i u_i^T-u_j u_j^T`.                   (3.9)

For every unit vector `v in R^2`,

`v^T U_I^T U_I v
 >=1-||u_k||^2-||u_i||^2-||u_j||^2
 >=2/3-2eta`.                                                     (3.10)

Therefore

`Delta_ij=det(U_I^T U_I)>=(2/3-2eta)^2`.                          (3.11)

Because `s_i,s_j>0` and `u_k` is nonzero on the first latent axis, the triple `{k,i,j}` spans the latent two-space; (3.11) also makes the complement span it. Thus the grouped receiver (1.6) applies. The partner hard determinant floor (1.4) gives

`(det Lambda)^2>H0^2 rho^(-4)`.                                  (3.12)

Substituting (3.11)-(3.12) into (1.6) yields (3.6). At `eta=1/4`, `(2/3-2eta)^2=(1/6)^2=1/36`, proving (3.7)-(3.8).

Finally `sum_i c_i=tr(U^T U)=2`. If eight indices had `c_i>1/4`, their leverage sum would exceed two. Hence at most seven such indices exist. QED.

### Why this is stronger than selecting a good pair

The conclusion is simultaneous for **every** pair outside a fixed finite high-leverage set. No pair-volume `q_ij`, no complement determinant depending on dimension, and no selected reciprocal minor appears in (3.7). The only payment is deletion of at most seven physical high-leverage coordinates.

## 4. Exact four-point cancellation identity

For positive `s_i,s_j`, define

`G_ij=tau_ij/(s_i s_j)`.                                         (4.1)

Then exactly

`G_ij=d_k(t_i-t_j)^2+c(d_i/s_i+d_j/s_j)`.                         (4.2)

For four distinct physical indices `i,j,l,m` away from `k`, all with positive `s`,

`boxed:
 G_ij+G_lm-G_il-G_jm
 =-2 d_k(t_i-t_m)(t_j-t_l).}`                                    (4.3)

Every arbitrary one-vertex diagonal term cancels. This identity was proved in r40 and is repeated here only as the algebraic input to the new global all-pair consequence.

## 5. New theorem: at most ten physical centers and two projective lines at scale rho^{-1/6}

Assume `rho>sqrt(H0)` so `c_k>0`, and remain in the hard branch. Let

`H={i!=k:c_i>1/4}`.                                               (5.1)

By Theorem 3.1, `|H|<=7`. Put

`L=[n]\(H union {k})`,
`alpha=rho^(-1/3)`,
`L_0={i in L:s_i<alpha}`,
`L_1={i in L:s_i>=alpha}`.                                       (5.2)

Every `i in L_0` is physically close in coefficient space to the hub line

`ell_0=span(u_k)`:

`boxed: dist(u_i,ell_0)=|y_i|<rho^(-1/6).}`                       (5.3)

For `i,j in L_1`, (3.7) gives

`|G_ij| <= C_* rho^(-1) alpha^(-2)
          =C_* rho^(-1/3).`                                      (5.4)

### Theorem 5.1 — `QFORM-NINEEXCEPTION-TWOLINE-ONESIXTH-v1`

There is a second latent line `ell_1` and a set `Z subset [n]\{k}` with

`boxed: |Z|<=9}`                                                   (5.5)

such that every physical row outside `Z union {k}` satisfies

`boxed:
 dist(u_i,ell_0)<rho^(-1/6)
 or
 dist(u_i,ell_1)<24.540 rho^(-1/6).}`                             (5.6)

Equivalently, including the distinguished coordinate `k`, a hard high-density exact-rank-two survivor has at most ten named physical centers outside a two-projective-line strip of width `O(rho^(-1/6))`.

#### Proof

Write `M=|L_1|` and order the slopes of `L_1`:

`t_1<=t_2<=...<=t_M`.                                             (5.7)

If `M>=4`, apply (4.3) with the four distinct positions

`i=1`, `m=M-1`, `j=M`, `l=2`.                                    (5.8)

By (5.4), the absolute value of the left side of (4.3) is at most

`4 C_* rho^(-1/3)`.                                               (5.9)

Since `|d_k|>=1`,

`2 (t_{M-1}-t_1)(t_M-t_2)
 <=4 C_* rho^(-1/3)`,                                             (5.10)

hence

`(t_{M-1}-t_1)(t_M-t_2)
 <=2 C_* rho^(-1/3).`                                             (5.11)

Therefore one of the two factors is at most

`W:=sqrt(2C_*) rho^(-1/6)
  =49.078277090930... rho^(-1/6).`                               (5.12)

So either `t_1,...,t_{M-1}` or `t_2,...,t_M` lies in an interval of length `W`. Remove the one possible extreme outlier and choose `t_0` inside the surviving interval. Let

`ell_1=span((t_0,1))`.                                            (5.13)

For every surviving transverse row,

`u_i=y_i(t_i,1)`, so

`dist(u_i,ell_1)
 = |y_i||t_i-t_0|/sqrt(1+t_0^2)
 <=sqrt(c_i) W
 <=W/2
 <24.540 rho^(-1/6)`,                                            (5.14)

because `c_i<=1/4` on `L`.

If `M<=3`, choose `ell_1` through any one nonzero row in `L_1` and mark the remaining at most two rows as exceptions. Thus in all cases at most two low-leverage transverse rows need be exceptional.

Take `Z` to be the union of the at most seven high-leverage rows `H` and those at most two transverse exceptions. Then `|Z|<=9`; (5.3) pays `L_0` and (5.14) pays the surviving `L_1`. QED.

### Optimal exponent within this simple truncation mechanism

If the transverse threshold is `alpha=rho^(-a)`, the hub-strip distance is `rho^(-a/2)`, while the normalized all-pair bound gives slope width `rho^{-(1-2a)/2}`. Balancing the exponents gives

`a/2=(1-2a)/2`, hence `a=1/3` and exponent `1/6`.                  (5.15)

Thus the `rho^-1/6` scale is the balanced output of the present leverage-truncation + exact four-point mechanism.

## 6. Actual equation-level application of fleet04/B13

The designated partner is not used only as a status citation. Its hard-branch determinant floor

`(det Lambda)^2>1536e^2 rho^(-4)`                                (6.1)

is inserted into the grouped physical-triple inequality

`Delta_ij (det Lambda)^2 |tau_ij|<=379687.5 rho^(-5)`.            (6.2)

The low-leverage complement estimate `Delta_ij>=1/36` then gives the concrete target-level inequality

`boxed:
 |tau_ij|<1204.338641108 rho^(-1)}`                               (6.3)

simultaneously for every low-leverage transverse pair. This is the essential new bridge that makes the global two-line theorem possible.

The partner's optimizer-free bathtub theorem is also used to retain full arbitrary cap-one product-law scope; no interval optimizer is introduced.

## 7. Relation to the previous projective-packet results

The earlier packet arguments forced a fixed positive **weighted packet mass** to become projectively degenerate, at scales such as `rho^-1/10`, but did not control every low-leverage physical pair simultaneously. Theorem 3.1 instead pays the complement determinant uniformly after deleting finitely many high-leverage rows. The result is a **global rowwise organization**: apart from at most nine additional physical coordinates, every rank-two coefficient row lies near one of two projective lines, at the faster `rho^-1/6` scale.

This does not say the entire coefficient matrix is close in Frobenius norm to two exact line-banks: arbitrarily many individually small row errors can carry non-negligible aggregate energy. That distinction is essential under the live corrections and is why the residual strip cannot simply be deleted.

## 8. New remaining implication

The next B13 obligation is

`QFORM-TWOLINE-BANK-PRODUCT-RECEIVER-v1`.

Starting from Theorem 5.1, consume the two physical projective banks plus at most ten named centers in a product-preserving density/small-ball receiver. The receiver must:

1. aggregate each original-coordinate bank before taking reciprocal coefficients;
2. retain the `O(rho^-1/6)` rowwise strip errors inside the actual quadratic phase rather than deleting them on unbounded fragmented supports;
3. retain arbitrary diagonal curvature and outside couplings;
4. interface with the already-proved every-cut transverse-mode bounds in the non-exact-rank-two survivor.

An exact two-line endpoint has a diagonal plus two disjoint rank-one physical banks and their rank-one cross coupling; this includes the known singleton-plus-two-bank control family, so a bank receiver rather than another local-minor selection is the appropriate next mechanism.

## 9. Status

**Full QFORM remains OPEN / not proved / not disproved. Global continuity remains OPEN.** The present theorem is a quantitative structural theorem inside the exact diagonal-plus-rank-two diffuse hard chamber. It matches all product-law quantifiers in that scope and does not assert that the rowwise `rho^-1/6` strip is probabilistically negligible.
