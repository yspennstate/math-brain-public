SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T19:52:34Z.
attacking: the punctured near-coloop survivor by changing mechanism from one-hub third-compound currency to a grouped original-coordinate second-compound crossing; determine exactly which crossing directions remain uniformly nondegenerate as the leakage tends to zero.

# account01/B10 — robust grouped second-compound backbone in the near-coloop collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Classification: `NEW STRUCTURAL THEOREM / NEW PAID SUBBRANCH / PARTNER BARRIER APPLIED / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source boundary and live state


The completed account03/B10 reduction

`yspennstate/math-open-problems@master:proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T181522Z-account03-B10-QFORM-r26/REPORT.md`

establishes that every still-unpaid positive-leakage near-coloop state may be written

`A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`, `D=|det M|>=1`,             (1.1)

with one ORIGINAL hub row

`u_0=sqrt(h) r`, `h>63/64`,                                             (1.2)

and leaf rows

`u_i=t_i r+p_i`, `p_i perpendicular r`,                                (1.3)

obeying the exact Parseval ledger

`sum_i t_i^2=rho:=1-h`, `sum_i t_i p_i=0`, `sum_i p_i p_i^T=I_2`,       (1.4)

and, after the completed physical-pivot/pair exits,

`tau_i:=||p_i||^2<1/61` for every leaf.                                 (1.5)

No variable in the spectral coordinates is declared independent. Every partition below is a partition of the ORIGINAL scalar coordinates.

The fresh arbitrary-rank projected-crossing theorem used later is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For a disjoint original-coordinate crossing block `B` of rank three with singular values `s_1>=s_2>=s_3>0`, it gives a continuous density and

`||p_Q||_infinity <= 6 (s_1 s_2 s_3)^(-1/3)`.                          (1.6)

Internal quadratic terms on both sides are arbitrary.

## 2. Pair-volume law and a balanced original-coordinate split

Put

`w_ij=det(p_i,p_j)^2`, `i<j`.                                          (2.1)

Two-dimensional Cauchy--Binet and the Parseval identity in (1.4) give

`sum_(i<j) w_ij=1`,                                                     (2.2)

and the exact coordinate marginal identity

`sum_(j!=i) w_ij=tau_i`.                                                (2.3)

Thus `w` is a probability law on unordered leaf pairs. Let `B,B'` be independent pair samples from this law. By a union bound over common coordinates,

`P(B intersects B') <= sum_i tau_i^2
                     <= (max_i tau_i) sum_i tau_i
                     < (1/61)*2=2/61`.                                 (2.4)

Hence the disjoint-pair probability satisfies

`delta:=P(B cap B'=empty)>59/61`.                                      (2.5)

Now colour every leaf independently into `I` or `J`, each with probability `1/2`, and define the transverse Grams

`S_I=sum_(i in I)p_i p_i^T`, `S_J=sum_(j in J)p_j p_j^T`.              (2.6)

Cauchy--Binet gives

`det S_I=sum_(B subset I)w_B`, `det S_J=sum_(B' subset J)w_B'`.         (2.7)

For fixed pair samples `B,B'`, the event `B subset I` and `B' subset J` has probability `1/16` when the pairs are disjoint and zero otherwise. Therefore

`E[det S_I det S_J]=delta/16>59/976`.                                  (2.8)

Consequently some deterministic ORIGINAL-coordinate partition `L=I sqcup J` satisfies

`boxed: det S_I det S_J>59/976.`                                      (2.9)

Since `0<=S_I,S_J<=I_2`, each determinant is at most one, so the same split has separately

`boxed: det S_I>59/976,   det S_J>59/976.`                             (2.10)

This is a stronger two-sided product-frame certificate than the earlier hub-versus-leaf triple split: it does not lose a factor `rho=1-h`.

## 3. Main theorem: uniform second-compound crossing survives the coloop limit

Let

`H={0} union I`,

`P=R_H` (the spectral-row matrix on the hub plus bank `I`),

`Q=R_J`,

and let the physical grouped crossing be

`B=A[H,J]=P M Q^T`.                                                     (3.1)

### Theorem — `QFORM-NEARCOLOOP-ROBUST-SECOND-COMPOUND-v1`

For the deterministic split furnished by Section 2,

`boxed: e_2(BB^T)>205379/3718856704>5.5226e-5.`                         (3.2)

Equivalently, if `s_1>=s_2>=s_3>=0` are the singular values of `B`, then

`boxed: s_1 s_2>sqrt((205379/3718856704)/3)>0.00429054.`                (3.3)

In particular two crossing singular directions remain uniformly nondegenerate as `rho ->0`.

### Proof

Write an arbitrary spectral vector as `z=xr+y`, `y perpendicular r`. Then

`z^T(P^T P)z
 =h x^2+sum_(i in I)(t_i x+p_i.y)^2`.                                  (3.4)

For real `a,b`,

`(a+b)^2 >= (1/2)b^2-a^2`                                              (3.5)

because the difference is `2(a+b/2)^2`. Hence, with `rho_I=sum_(i in I)t_i^2<=rho`,

`z^T(P^T P)z
 >=(h-rho_I)x^2+(1/2)y^T S_I y`.                                      (3.6)

Since `h>63/64`,

`h-rho_I>=h-rho=2h-1>31/32`.                                          (3.7)

Also `S_I<=I_2`, so in dimension two

`lambda_min(S_I)=det(S_I)/lambda_max(S_I)>=det(S_I)>59/976`.           (3.8)

Therefore

`lambda_min(P^T P)>59/1952=:gamma`.                                   (3.9)

The least singular value of the second exterior power `wedge^2 P` is therefore at least `gamma`.

On the right bank, put `G_J=Q^T Q`. In the orthogonal splitting `R r direct-sum r^perp`, the transverse principal block of `G_J` is exactly `S_J`. Hence the second elementary symmetric polynomial satisfies

`e_2(G_J)>=det S_J>59/976=:eta`.                                      (3.10)

Equivalently,

`||wedge^2 Q^T||_F^2=e_2(G_J)>eta`.                                   (3.11)

Now use the exact factorization

`wedge^2 B=(wedge^2 P)(wedge^2 M)(wedge^2 Q^T)`.                       (3.12)

Because every singular value of `M` is at least one,

`sigma_min(wedge^2 M)>=1`.                                             (3.13)

Thus the Frobenius norm obeys

`||wedge^2 B||_F
 >=sigma_min(wedge^2 P) sigma_min(wedge^2 M)||wedge^2 Q^T||_F
 >gamma sqrt(eta)`.                                                     (3.14)

Squaring and using `e_2(BB^T)=||wedge^2 B||_F^2` gives

`e_2(BB^T)>gamma^2 eta
 =(59/1952)^2(59/976)
 =205379/3718856704`,                                                   (3.15)

proving (3.2). Finally

`e_2(BB^T)=(s_1s_2)^2+(s_1s_3)^2+(s_2s_3)^2<=3(s_1s_2)^2`,            (3.16)

which proves (3.3). QED.

The proof uses only original-coordinate partitions and exact coefficient geometry. It does not assume the spectral projections are independent and does not use moment, support, Gaussian, log-concavity, or perturbative hypotheses.

## 4. Actual analytic consequence: a new paid rank-three-crossing subbranch

Whenever the third singular value of the same grouped crossing satisfies `s_3>0`, the completed rank-three projected-crossing theorem (1.6) and (3.3) give

`||p_Q||_infinity
 <6[0.00429054 s_3]^(-1/3)
 <36.925 s_3^(-1/3)`.                                                   (4.1)

The resulting density is continuous and vanishes at infinity.

In particular the explicit subbranch

`s_3>=2^(-10)`                                                         (4.2)

is completely paid with

`boxed: ||p_Q||_infinity<372.175`,                                     (4.3)

and a continuous density.

Thus the punctured near-coloop problem is no longer a question of producing the first two crossing directions: those are now uniformly present. The unpaid grouped-crossing survivor may be restricted to

`boxed: s_3<2^(-10) while s_1s_2>0.00429054.`                          (4.4)

The missing analytic mechanism is to obtain the last half-power of Fourier decay (or its direct small-ball analogue) by spending the shared heavy-hub / third-rank phase without paying a negative power of `rho`, `A_00`, or `s_3`.

## 5. Designated partner account02/B10 applied to an actual inequality

The latest completed designated-partner theorem used here is

`QFORM-NEARCOLOOP-ONEHUB-CURRENCY-BARRIER-v1`,

`yspennstate/math-open-problems@bf1ec1482020bc1da89f7f888057b70269df650d`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T170933Z-account02-B10-QFORM-r11/REPORT.md`.

It proves for every leaf-only one-hub projected-crossing split

`V_3(I,J)<=h D^2(1-h)`.                                                (5.1)

Apply it to the already isolated ultra-collar from the preceding account01/B10 run, where

`D^2(1-h)<2^(-12)`.                                                     (5.2)

Then for every such one-hub projected-crossing split,

`boxed: V_3(I,J)<2^(-12).`                                             (5.3)

This is an actual inequality-level use of the completed partner result. In contrast, Theorem (3.2) gives an order-one-in-`rho`-scale second-compound lower bound for a grouped crossing on the same survivor. Therefore the partner barrier and the new theorem together locate the obstruction precisely: **the first two grouped crossing singular directions do not collapse; only the third-direction payment collapses in the old one-hub topology.**

A newer account02/B10 artifact at `account02-B10-20260923T194407Z-auto11-hybrid-nearnull/` was only an early checkpoint when consumed, so it is not cited as a completed partner theorem.

## 6. Endpoint geometry and next implication

The completed account03/B10 null-hub theorem pays the exact `A_00=0` diffuse-transverse boundary by a mixed-Fresnel shear. The current theorem is complementary: it shows a robust rank-two crossing persists through the positive-leakage collar, including as the coloop leakage tends to zero.

The first unpaid implication is now

`QFORM-NEARCOLOOP-RANK2-CROSSING-PLUS-SHARED-HUB-HALFPOWER-v1`:

> Given a disjoint original-coordinate grouped crossing with `s_1s_2>=0.00429`, prove a universal density bound in the exact-rank-three near-coloop geometry even when `s_3` is arbitrarily small, by coupling the critical rank-two crossing decay with the shared-hub third-rank phase before taking absolute values.

This formulation is deliberately phase-sensitive. A bare rank-two crossing supplies only critical `|t|^{-1}` decay; taking absolute values and then asking for the third singular value reproduces the known coloop loss.

Full arbitrary exact rank three: `OPEN / NOT PROVED`.  
Full owner QFORM conjecture: `OPEN / NOT PROVED / NOT DISPROVED`.  
Continuity: proved on the paid subbranch (4.2), open globally.

## 7. Deterministic arithmetic check

The exact constants used above are

`eta=59/976=0.0604508196721...`,

`gamma=59/1952=0.0302254098361...`,

`gamma^2 eta=205379/3718856704=5.52263817477e-5`,

`sqrt((gamma^2 eta)/3)=0.00429054704156...`,

and the `s_3>=2^-10` projected-crossing consequence is `372.1748425...`.

These are arithmetic checks only; the proof is the exact exterior-power argument above.
