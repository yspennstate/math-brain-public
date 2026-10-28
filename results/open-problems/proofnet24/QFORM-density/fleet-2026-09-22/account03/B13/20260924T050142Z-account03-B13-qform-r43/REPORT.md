SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-24T05:01:42Z.
attacking: optimize the low/high transverse split in the hard exact-rank-two survivor, improve the aggregate two-line/diffuse-bank exponents, and extract high-bank diagonal trace control.

# account03/B13 r43 — Pareto-optimized two-line split and high-bank diagonal trace

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T050142Z-account03-B13-qform-r43`  
Role: extremal product laws / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING STRUCTURAL THEOREMS IN THE HARD EXACT DIAGONAL+RANK-TWO CHAMBER / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

All random coordinates below remain the original independent physical coordinates. The only rotation is a deterministic change of basis in the two-dimensional coefficient space. No Gaussian, moment, log-concavity, compact-support, connected-support, single-interval extremality, bounded support diameter, uniform fragment count, post-rotation independence, law-uniform pointwise oscillatory decay, unrestricted joint coarea estimate, or deletion of a coefficient-small quadratic error is used.

## 1. Fresh source-pinned premises


### 1.1 Designated partner account04/B13 — diagonal fifth-order sparsification and optimizer-free reduction

Completed partner report:

`yspennstate/math-open-problems@635da12cb1c19b27c455c662be800eb1113dd845`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260924T031520Z-account04-B13-diagonal-sparsification-r2/REPORT.md`.

In the exact rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `rank(U Lambda U^T)<=2`, `s_3(A)>=1`,

if

`rho=P{X^T A X in J}/|J|`,

then, with `d_(j)` denoting the decreasing rearrangement of `|d_i|`,

`d_(5) <= C5/rho`,                                                  (1.1)

where

`C5=2 sqrt(30 pi)=19.41625912555699...`.                           (1.2)

Thus all but at most four physical diagonal coefficients obey `|d_i|<=C5/rho`.

The same partner report gives the safe optimizer-free product reduction: every strict cap-one product-law slab witness can, with arbitrarily small prescribed ratio loss and unchanged `A,J`, be replaced by a product of unit-measure bounded finite-union sets. It asserts equality of suprema, not optimizer attainment, interval extremality, bounded diameter, or a uniform fragment count.

This partner theorem is used below at the actual slope equation through the term `|d_i|+|d_j|`; it is not merely cited as status.

### 1.2 Hard diffuse exact-rank-two branch

The completed account04/B13 slab dichotomy at

`yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`

proves the following. In the diffuse exact-rank-two chamber `max_i c_i<=1/3`, where `c_i=||u_i||_2^2`, there is a physical coordinate `k` with `|d_k|>=1`. In the hard non-rank-one branch,

`|det Lambda| > H0 rho^(-2)`,                                     (1.3)

where

`H0=sqrt(1536 e^2)=106.534455308869...`.                          (1.4)

The complementary branch is already an operator-norm rank-one certificate and is not altered here.

### 1.3 Prior account03/B13 simultaneous tau control

The immediately preceding same-slot report is

`yspennstate/math-open-problems@f55c9f790ca64fcb3281c8833f8023519382444a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260924T033406Z-account03-B13-qform-r42/REPORT.md`.

Using the partner sparsification above together with the grouped three-leaf theorem of account01/B13, it selects at most ten original-coordinate centers `C`, containing `k`, so that every noncenter obeys

`c_i<=2/7`, `|d_i|<=C5/rho`,                                      (1.5)

and every two distinct positive-transverse noncenters obey

`|tau_ij| < Ktau rho^(-1)`,                                       (1.6)

with

`Ktau=3688.287088390375...`.                                      (1.7)

For completeness, (1.6) comes from the account01/B13 grouped three-leaf inequality

`Delta_ij (det Lambda)^2 |tau_ij| <= (759375/2) rho^(-5)`          (1.8)

combined with the noncenter complement determinant floor `Delta_ij>=(2/21)^2` and the hard determinant floor (1.3).

Rotate only the latent coefficient basis so

`u_k=(sqrt(c),0)`, `c=c_k`,
`u_i=(x_i,y_i)`, `s_i=y_i^2`, `t_i=x_i/y_i` when `s_i>0`.          (1.9)

Then exactly

`q_ki=c s_i`,
`q_ij=s_i s_j(t_i-t_j)^2`,                                       (1.10)

and

`tau_ij/(s_i s_j)
 =d_k(t_i-t_j)^2+c(d_i/s_i+d_j/s_j)`.                             (1.11)

The former r42 split fixed the threshold at `s_i=10.3 rho^(-1/3)`. The point of the present run is that the proof permits a one-parameter family of thresholds; choosing a different exponent improves both aggregate alternatives simultaneously.

## 2. New one-parameter theorem: the transverse split has a Pareto family

Fix

`a=10.3`                                                           (2.1)

and choose any

`1/3 < p < 1/2`.

Set

`q=1-2p>0`,                                                        (2.2)

`alpha_p=a rho^(-p)`,                                              (2.3)

and partition the noncenters into

`L_p={i notin C:s_i<alpha_p}`,
`R_p={i notin C:s_i>=alpha_p}`.                                   (2.4)

Indices with `s_i=0` belong to `L_p`; no slope is assigned to them.

Let

`ell_0=span(u_k)`.                                                  (2.5)

For every `i in L_p`,

`dist(u_i,ell_0)=|y_i|<sqrt(a) rho^(-p/2).`                        (2.6)

For `i,j in R_p`, use the exact identity (1.11), `|d_k|>=1`, `c<=1/3`, the simultaneous tau bound (1.6), and — at this exact equation — the designated partner estimate `|d_i|,|d_j|<=C5/rho`. We get

`|d_k|(t_i-t_j)^2`
` <= Ktau rho^(-1)/(s_i s_j)
`    +(C5/3)rho^(-1)(1/s_i+1/s_j)`
` <= [Ktau/a^2] rho^(2p-1)
`    +[2C5/(3a)] rho^(p-1).`                                      (2.7)

Since `rho>C5>1` and `p>0`, `rho^(p-1)<=rho^(2p-1)`. Define

`E_G=Ktau/a^2=34.76564321227613...`,                              (2.8)

`E_D=2C5/(3a)=1.256715801006925...`,                              (2.9)

`W2=E_G+E_D=36.02235901328306...`,                                (2.10)

`W=sqrt(W2)=6.001862961888005...`.                                (2.11)

Then

`boxed:
 |t_i-t_j| <= W |d_k|^(-1/2) rho^(-q/2).}`                        (2.12)

Thus all slopes in `R_p` lie in one interval, with no exceptional slope. If `R_p` is nonempty, choose one `t_0` from it and let

`ell_1=span((t_0,1))`;                                             (2.13)

if `R_p` is empty choose `ell_1` arbitrarily. For every `i in R_p`,

`dist(u_i,ell_1)
 <= |y_i||t_i-t_0|/sqrt(1+t_0^2)`
 <= sqrt(2/7) W |d_k|^(-1/2) rho^(-q/2).`                         (2.14)

This proves the rowwise part of the following theorem.

### Theorem 2.1 — `QFORM-TWOLINE-PARETO-SPLIT-v1`

Under the source-pinned hard exact-rank-two hypotheses above, for every `p in (1/3,1/2)` the same at-most-ten original-coordinate center set `C` admits two latent lines `ell_0,ell_1` so that every noncenter belongs to one of the two strips (2.6), (2.14). In addition, defining

`E0(p)=sum_{i in L_p}s_i`,                                         (2.15)

and letting `U^(0,p)` be obtained by orthogonally projecting each `L_p` row onto `ell_0` and each `R_p` row onto `ell_1`, one has

`boxed:
 ||U_{C^c}-U^(0,p)||_F^2
 <= E0(p)+W2 rho^(-q).}`                                           (2.16)

#### Proof of the aggregate estimate

The low-bank contribution is exactly

`sum_{i in L_p} dist(u_i,ell_0)^2=sum_{i in L_p}s_i=E0(p)`.        (2.17)

For the high bank, (2.12) gives

`sum_{i in R_p}dist(u_i,ell_1)^2`
` <=W2 |d_k|^(-1) rho^(-q) sum_{i in R_p}s_i`
` <=W2 rho^(-q)`,                                                  (2.18)

because `|d_k|>=1` and, after the orthogonal latent basis change, `sum_i y_i^2=1`. Adding (2.17) and (2.18) proves (2.16). QED.

Now the aggregate obstruction has an exact quantitative fork. If

`E0(p)<=rho^(-q)`,                                                  (2.19)

then

`boxed:
 ||U_{C^c}-U^(0,p)||_F
 <=sqrt(1+W2) rho^(-q/2)
 <6.085 rho^(-q/2).}`                                              (2.20)

If instead

`E0(p)>rho^(-q)`,                                                   (2.21)

define the original-coordinate normalized transverse vector

`b_i=y_i/sqrt(E0(p))` for `i in L_p`, and `b_i=0` otherwise.       (2.22)

Then

`sum_i b_i^2=1`,                                                   (2.23)

and, because `s_i<a rho^(-p)`,

`boxed:
 max_i b_i^2 < a rho^{-(3p-1)},}`                                  (2.24)

while

`boxed:
 |L_p|>rho^(3p-1)/a.}`                                             (2.25)

Indeed, `s_i/E0(p)<a rho^(-p+q)=a rho^{-(3p-1)}`, and `E0(p)<|L_p|a rho^(-p)` combined with (2.21) gives (2.25).

Equations (2.20) and (2.24)-(2.25) are a genuine Pareto family: moving `p` upward strengthens the diffuse-bank exponent `3p-1`, while moving it downward strengthens the aggregate two-line exponent `q/2=(1-2p)/2`. No random quadratic term has been discarded.

## 3. New high-bank diagonal trace theorem

The same calculation pays an additional quantity that r42 did not record.

For `i in R_p`, define

`a_i=c d_i/s_i`.                                                    (3.1)

For distinct `i,j in R_p`, set

`G_ij=tau_ij/(s_i s_j)`.                                           (3.2)

Because `s_i,s_j>=a rho^(-p)`, (1.6) gives

`|G_ij|<=E_G rho^(-q)`.                                            (3.3)

From (1.11) and (2.7),

`G_ij=d_k(t_i-t_j)^2+a_i+a_j`,                                    (3.4)

and

`|d_k|(t_i-t_j)^2<=W2 rho^(-q)`.                                  (3.5)

Hence every distinct high-bank pair satisfies

`boxed:
 |a_i+a_j| <= H rho^(-q),}`                                       (3.6)

where

`H=E_G+W2=70.78800222555918...`.                                  (3.7)

If `|R_p|>=3`, then for any three distinct `i,j,l`,

`2a_i=(a_i+a_j)+(a_i+a_l)-(a_j+a_l)`,                             (3.8)

so

`|a_i|<=(3/2)H rho^(-q)`.                                         (3.9)

Multiplying by `s_i` and summing gives

`c sum_{i in R_p}|d_i|`
` =sum_{i in R_p}|a_i|s_i`
` <=(3/2)H rho^(-q) sum_{i in R_p}s_i`
` <=Kdiag rho^(-q)`,                                               (3.10)

with

`Kdiag=(3/2)H=106.1820033383388...`.                              (3.11)

If `|R_p|<=2`, the partner diagonal-tail theorem gives directly

`c sum_{i in R_p}|d_i|<=2C5/(3rho)<Kdiag rho^(-q)`                 (3.12)

for `rho>1`. Thus there is no cardinality exception.

### Theorem 3.1 — `QFORM-HIGHBANK-DIAGONAL-TRACE-PARETO-v1`

For every `p in (1/3,1/2)` in the hard exact-rank-two chamber,

`boxed:
 c ||D_{R_p}||_{S_1}
 =c sum_{i in R_p}|d_i|
 <106.183 rho^{-(1-2p)}.}`                                        (3.13)

This is an actual trace-norm statement on the distributed physical diagonal curvature carried by the high-transverse bank. It follows from the all-pair tau equations plus the designated partner's `O(rho^-1)` diagonal tail; it does not treat `D_{R_p}` as a probabilistically small quadratic perturbation.

## 4. Concrete improved split: p=2/5

Take

`p=2/5`, `q=1/5`.                                                  (4.1)

This gives simple fifth-power scales and improves **both** r42 aggregate branches at once.

The threshold is

`alpha=10.3 rho^(-2/5)`.                                          (4.2)

Every low-bank row obeys

`boxed:
 dist(u_i,ell_0)<3.210 rho^(-1/5).}`                               (4.3)

Every high-bank row obeys

`boxed:
 dist(u_i,ell_1)
 <3.209 |d_k|^(-1/2) rho^(-1/10).}`                               (4.4)

More importantly, with `E0=sum_{L}s_i`, either

`E0<=rho^(-1/5)` and

`boxed:
 ||U_{C^c}-U^(0)||_F<6.085 rho^(-1/10),}`                         (4.5)

or `E0>rho^(-1/5)` and the normalized original-coordinate transverse vector `b` satisfies

`boxed:
 sum_i b_i^2=1,
 max_i b_i^2<10.3 rho^(-1/5),
 |supp b|>rho^(1/5)/10.3.}`                                       (4.6)

Simultaneously the high-transverse physical diagonal bank satisfies

`boxed:
 c ||D_R||_{S_1}<106.183 rho^(-1/5).}`                            (4.7)

### Comparison with r42

The r42 split `p=1/3` obtained a Frobenius-small branch of order `rho^(-1/12)` and a diffuse-bank coordinate-mass/cardinality exponent `1/6`. The present `p=2/5` split improves these simultaneously to

- aggregate two-line residual `O(rho^(-1/10))`; and
- diffuse-bank maximum squared coordinate `O(rho^(-1/5))` with support `Omega(rho^(1/5))`.

It also adds the new high-bank diagonal trace `O(rho^(-1/5))`.

This does not make the residual quadratic form probabilistically small for arbitrary fragmented or remotely translated supports. It gives stronger deterministic currency for a product-preserving receiver.

## 5. Extremal-product-law transfer at the actual inequalities

The designated account04/B13 optimizer-free theorem is used in its intended scope as follows. Let a cap-one product law be a strict slab witness for any putative violation of the structural conclusions above. For arbitrary `eta>0`, replace it by a bounded finite-union unit-product indicator witness with the same `A,J` and slab ratio at least `rho-eta`. Apply (1.1), the hard-branch tau inequality, and the arguments above at `rho-eta`. Let `eta downarrow0`. Every displayed structural inequality transfers back with zero limiting constant loss.

This is only a reduction of the extremal-product **supremum**. Nothing here says a centered interval or any interval is extremal; no optimizer is assumed to exist; no common support diameter or fixed fragment count is imposed.

## 6. What is and is not closed

The full QFORM conjecture is still **OPEN / not proved / not disproved**. Global continuity is separately **OPEN**.

The present run strengthens the exact-rank-two hard survivor to the following deterministic alternatives after at most ten original-coordinate centers:

1. the coefficient frame is `O(rho^-1/10)` in Frobenius norm from an exact two-line frame; or
2. there is a normalized original-coordinate transverse bank with maximum squared coordinate `O(rho^-1/5)` and at least `Omega(rho^1/5)` physical coordinates;

and in both cases the high-transverse bank's physical diagonal curvature has weighted trace `O(rho^-1/5)`.

The first unpaid implication is now

`QFORM-1P5-DIFFUSE-BANK-OR-1P10-TWOLINE-RECEIVER-v1`:

> retain the diagonal tail and the actual strip residual inside a product-preserving curved/Fourier receiver, using either the `rho^-1/5` diffuse transverse bank or the `rho^-1/10` aggregate two-line approximation, rather than deleting them as small random perturbations.

A successful receiver must remain affine-uniform after conditioning the finite original-coordinate center set. The existing corrections rule out replacing that task by post-rotation independence, a fiberwise density supremum, or a law-uniform pointwise quadratic-phase estimate.

## 7. Arithmetic checks

The deterministic constant check for this report verifies

`C5=19.41625912555699...`,
`E_G=34.76564321227613...`,
`E_D=1.256715801006925...`,
`W2=36.02235901328306...`,
`W=6.001862961888005...`,
`H=70.78800222555918...`,
`Kdiag=106.1820033383388...`,
`sqrt(1+W2)=6.084600152292922...`,
`sqrt(10.3)=3.209361307176243...`,
`sqrt(2/7)W=3.208130697964740...`.

The checker also verifies at `p=2/5` that `q=1/5`, the aggregate Frobenius exponent is `q/2=1/10`, and the diffuse-bank exponent is `3p-1=1/5`.

These are arithmetic checks of an analytic proof, not Monte Carlo evidence for the conjecture.
