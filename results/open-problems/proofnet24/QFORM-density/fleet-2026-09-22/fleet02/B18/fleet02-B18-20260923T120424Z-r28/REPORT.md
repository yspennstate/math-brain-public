SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-23T12:04:24Z.
attacking: the nonplanar Schur-isotropic two-sheet zero-pivot survivor, applying the latest fleet03/B18 three-disjoint-bank theorem only where its exact original-coordinate hypotheses are available.

# fleet02/B18 r28 — circular scalar-bank compiler barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Literature-to-proof transfer; complementary constructions / source-valid counterexamples  
**Designated partner:** fleet03/B18  
**Status:** `PROVED SUPPORTING METHOD OBSTRUCTION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full target remains open: for arbitrary independent real inputs with one-dimensional probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X`, or give a genuine target counterexample. No moment, support, log-concavity, iid, smoothness, diagonal-basis, or post-rotation independence assumption is used here.

## 1. First unpaid implication

The preceding B18 run isolated an exact target-valid circular Schur-isotropic family whose positive / one-sheet half-line is already paid by the pinned ruled-surface theorem, while the negative / two-sheet half-line remains open.

The latest designated partner, fleet03/B18 r27, closes every case in which the active form can be represented by **three pairwise disjoint ORIGINAL-coordinate scalar banks** with a uniformly nonsingular effective `3 x 3` matrix. The first question this run is therefore structural and source-matching:

> Can the circular nonplanar survivor be compiled into those three scalar banks with `sigma_min(K)` bounded below independently of dimension?

The answer is **no**. The new theorem below proves that every exact three-disjoint-scalar-bank representation on this family has `sigma_min(K)=O(1/m)`. In fact, no exact scalar bank can contain three residual coordinates at all. Thus the partner theorem is a genuine closure theorem for its subclass, but it cannot be promoted to the current nonplanar survivor by silently replacing a three-dimensional product projection with three independent scalar aggregates.

The sharpened unpaid implication after this run is:

**`QFORM-CIRCULAR-THREEDIM-PROVENANCE-TWOSHEET-v1`.** Uniformly bound the negative / two-sheet density of the circular family by retaining a genuinely three-dimensional residual statistic (or an equivalent joint oscillatory/product-preserving mechanism) before nonlinear conditioning destroys the original product provenance. Generic joint-density caps, coordinate marginal caps, X-ray caps, exact scalar banks, and exact two-dimensional banks are insufficient proof interfaces.

## 2. Source-valid inputs actually applied

### 2.1 Latest designated partner: three disjoint scalar banks, all pivots

Source:

`yspennstate/math-open-problems@602d508c11f3bb5848b65581a750b4497708bd5f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T112422Z-fleet03-B18-QFORM-r27/REPORT.md`.

Its theorem `QFORM-THREE-DISJOINT-BANKS-ALLPIVOTS-v1` is:

Let `I_1,I_2,I_3` be pairwise disjoint sets of original coordinates, let `u_k` be unit vectors supported on `I_k`, and put

`S_k=<u_k,X_{I_k}>`, `S=(S_1,S_2,S_3)`.

Because the banks are disjoint sets of ORIGINAL independent coordinates, the three `S_k` are genuinely independent. If after conditioning any other original coordinates the active dependence is exactly

`Q=S^T K S+ell^T S+c`

with fixed symmetric `K` satisfying `sigma_min(K)>=s>0`, then

`||p_Q||_infinity < 296/s`.                                         (2.1)

No scalar-pivot lower bound is required. The exact zero-pivot subcase has the sharper source-pinned estimate

`||p_Q||_infinity <=12 |det K|^(-1/3)`                               (2.2)

with continuity.

The partner explicitly does **not** prove that the bare three-large-eigenvalue hypothesis supplies such a scalar-bank representation.

### 2.2 Primary source: Livshyts--Paouris--Pivovarov

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, Theorem 1.1.

For a genuine product probability density `f=prod_i f_i`, with each `f_i` bounded, every `k`-dimensional orthogonal marginal satisfies

`||pi_E f||_infinity`
` <= min{ (n/(n-k))^((n-k)/2), 2^(k/2) } prod_i ||f_i||_infinity^(gamma_i)`,

for suitable `gamma_i in [0,1]` with `sum gamma_i=k`. Hence cap-one factors give

`||pi_E f||_infinity <=2^(k/2)`.                                    (2.3)

The theorem assumes no moments, compact support, log-concavity, smoothness, identical laws, symmetry, or centering. It controls marginal density; it does **not** assert independence among projected coordinates. Fleet03/B18 uses the `k=1` case only after the three banks are genuinely disjoint in original coordinates.

### 2.3 Required pinned completed result applied to a real inequality

The required `e5f71d79...` package proves in `COUNTEREXAMPLE_SEARCH.md`, Theorem C, that for an exact rank-three signature `(+,+,-)` target the one-sheet side has

`p_Q(t) <= pi sqrt(2)`                                               (2.4)

for a.e. `t>=0` after the stated coefficient normalization. This uses line integrals that are actual two-dimensional marginals of the original product projection, not independence after rotation.

We apply (2.4) below to the exact circular family. Thus the structural obstruction proved here concerns only the still-unpaid two-sheet side, not the whole line.

## 3. The exact circular target family

For integer `m>=3`, put

`theta_j=2 pi j/m`,

`v_j=m^(-1/2)(1, sqrt(2) cos theta_j, sqrt(2) sin theta_j)`,

for the `m` residual original coordinates. The rows form a Parseval frame:

`sum_j v_j v_j^T=I_3`.                                               (3.1)

Take the original-coordinate hub row

`u_0=m e_1`,                                                         (3.2)

and put

`s=sqrt(1+m^2)`,

`D_m=[[0,s^(-1),0],[s^(-1),0,0],[0,0,1]]`.                          (3.3)

Let `U` have rows `u_0,v_1,...,v_m` and define

`A_m=U D_m U^T`.                                                     (3.4)

Then

`U^T U=diag(1+m^2,1,1)`.                                             (3.5)

Hence the nonzero spectrum of `A_m` equals the spectrum of

`(U^TU)^(1/2) D_m (U^TU)^(1/2)
 =[[0,1,0],[1,0,0],[0,0,1]]`,

namely

`boxed: spec_nonzero(A_m)={-1,1,1}.`                                 (3.6)

So this is a genuine target family for every `m`, with no limiting relaxation of the spectral hypothesis.

Writing `Y=V^T X_R`, its quadratic form is

`Q_m=(2/s)(Y_1+m X_0)Y_2+Y_3^2`.                                    (3.7)

By the pinned ruled-surface theorem (2.4),

`boxed: p_(Q_m)(t)<=pi sqrt(2) for a.e. t>=0.`                        (3.8)

The remaining issue is the negative / two-sheet half-line.

The following exact physical identities will be used. First,

`det D_m=-1/(1+m^2) !=0`, `||D_m||_op=1`,                            (3.9)

and every residual row has

`||v_j||^2=3/m`.                                                     (3.10)

Therefore for residual indices `i,j`,

`|A_ij|=|v_i^T D_m v_j|<=3/m`.                                      (3.11)

The hub is an exact zero pivot:

`A_00=0`.                                                            (3.12)

Moreover

`A_0j=(sqrt(2m)/sqrt(1+m^2)) cos theta_j`.                           (3.13)

A direct substitution in `v_j^T D_m v_j` gives

`A_jj=(1/m)[(2 sqrt(2)/s) cos theta_j+2 sin^2 theta_j]`.              (3.14)

In particular,

`A_0j=0  =>  cos theta_j=0  =>  A_jj=2/m !=0`.                        (3.15)

## 4. Main theorem: every exact three-scalar-bank compiler degenerates

### Theorem `QFORM-CIRCULAR-SCALAR-BANK-COMPILER-BARRIER-v1`

Consider the family `A_m` above. Suppose an exact application of the fleet03/B18 theorem uses three pairwise disjoint original-coordinate scalar banks. After deleting zero aggregate coefficients from their nominal supports, let `a_1,a_2,a_3` be the three unit coefficient vectors, with disjoint supports, and put

`T=[a_1,a_2,a_3]`.                                                   (4.1)

Conditioning every original coordinate outside their union `B`, assume the active quadratic Hessian factors exactly through the three scalar bank variables:

`A_m[B,B]=T K T^T`                                                   (4.2)

for a symmetric `3 x 3` matrix `K`.

Then:

1. if all three banks are residual, `sigma_min(K)<=18/m`;
2. if the hub coordinate is active, its bank is necessarily the singleton hub and `sigma_min(K)<=12/m`.

Consequently the partner estimate (2.1), when applicable, has a nominal right-hand-side coefficient at least

`(296/18)m=(148/9)m`                                                 (4.3)

in the all-residual case, and at least

`(296/12)m=(74/3)m`                                                  (4.4)

when the hub is active. Thus this exact scalar-bank compiler cannot yield a dimension-free certificate on the circular family.

### Proof

Because the bank supports are disjoint and the `a_r` are normalized,

`T^T T=I_3`.                                                         (4.5)

For each scalar bank `B_r`, the corresponding within-bank principal block of (4.2) is

`A_m[B_r,B_r]=K_rr a_r a_r^T`,                                      (4.6)

and therefore has rank at most one.

#### Step 1: a bank containing the hub contains no residual coordinate

Suppose the hub belongs to bank `B_r`. Its aggregate coefficient is nonzero after the support cleanup. By (3.12) and (4.6),

`0=A_00=K_rr a_r(0)^2`,

so

`K_rr=0`.                                                            (4.7)

Equation (4.6) would then force the **entire** within-bank block to vanish. If a residual coordinate `j` were also in that bank, we would need both `A_0j=0` and `A_jj=0`. But (3.15) shows these two conditions can never occur simultaneously. Contradiction.

Hence any active hub bank is exactly the singleton `{0}`.             (4.8)

#### Step 2: every residual-only scalar bank contains at most two coordinates

Take any three distinct residual indices `i,j,k` and let `V_J` be the `3 x 3` matrix with rows `v_i,v_j,v_k`. The rows are invertible. Indeed, after removing the harmless common scaling and common first coordinate, a linear dependence is equivalent to the three distinct points

`(cos theta_i,sin theta_i)`, `(cos theta_j,sin theta_j)`, `(cos theta_k,sin theta_k)`

being collinear in the plane. A line meets the unit circle in at most two distinct points. Hence

`det V_J !=0`.                                                       (4.9)

Since `D_m` is invertible,

`det A_m[J,J]
 =det(V_J D_m V_J^T)
 =(det V_J)^2 det D_m
 !=0`.                                                               (4.10)

Thus every residual principal triple has rank three. But (4.6) says every triple lying inside one scalar bank would have rank at most one. Therefore

`boxed: every residual scalar bank has support size at most two.`    (4.11)

#### Step 3: all three banks residual

By (4.11), their union contains at most six residual coordinates. By (3.11), every entry of `A_m[B,B]` has modulus at most `3/m`, so the row-sum bound gives

`||A_m[B,B]||_op<=18/m`.                                             (4.12)

From (4.2) and (4.5),

`K=T^T A_m[B,B] T`,                                                  (4.13)

and hence

`||K||_op<=18/m`.                                                     (4.14)

Therefore

`boxed: sigma_min(K)<=18/m.`                                         (4.15)

If `K` is singular the partner theorem is unavailable. If it is nonsingular, no valid lower parameter `s<=sigma_min(K)` can make `296/s` dimension-free, and (4.3) follows.

#### Step 4: the hub is active

By Step 1, the hub is its own scalar bank. The other two banks contain at most four residual coordinates in total. In the bank basis write

`K=[[0,b^T],[b,C]]`,                                                 (4.16)

where the `2 x 2` block `C` is the compression of the residual principal block to the two residual aggregate directions. The residual union has cardinality at most four, so (3.11) gives

`||C||_op<=12/m`.                                                     (4.17)

Choose a unit `z in R^2` perpendicular to `b` (if `b=0`, choose any unit `z`) and put `w=(0,z)`. Then

`K w=(0,Cz)`,                                                        (4.18)

so

`boxed: sigma_min(K)<=||Kw||<=12/m.`                                 (4.19)

This proves (4.4) and completes the theorem. QED.

## 5. Stronger structural corollary: exact 1D/2D bank statistics cannot aggregate the circular residual source

The preceding rank argument is not special to scalar banks. Suppose a residual original-coordinate bank is represented exactly through a `d`-dimensional linear statistic `L^T X_B`, so its within-bank Hessian factors through a matrix of rank at most `d`. Then

`rank A_m[B,B]<=d`.                                                   (5.1)

But by (4.10), every three distinct residual coordinates already form a rank-three principal block. Hence:

`boxed: if d<=2, the support of an exact residual bank contains at most two circular residual coordinates.` (5.2)

Therefore any exact high-cardinality bank compression for this family must retain **all three residual spectral dimensions somewhere**. This is the structural reason the newest partner's three-independent-scalar theorem, powerful on genuinely separable original-coordinate banks, cannot pay the nonplanar circular survivor.

No independence statement about the three spectral coordinates of `Y=V^T X_R` follows from their being a three-dimensional projection. LPP supplies a bounded joint density, but the live two-sheet correction proves that generic bounded projection/X-ray information is not enough for the negative hyperboloid trace.

## 6. Relation to live corrections and source scope

The new theorem is only a proof-method obstruction. It is **not** a counterexample to QFORM and not a lower bound on the true density. Indeed (3.8) gives a uniform bound on half the line for the same exact target family.

The following tempting transfers remain invalid:

- treating `Y_1,Y_2,Y_3` as independent after the circular orthogonal projection;
- replacing simultaneous product provenance by only `||p_Y||_infinity`, coordinate marginal caps, or X-ray caps on the two-sheet side;
- perturbing the exact hub zero pivot into a nonzero-pivot argument on arbitrary unbounded input supports;
- inferring a uniformly conditioned fixed scalar-bank or physical-minor certificate from the three-large-eigenvalue hypothesis.

A later source-valid correction strengthens the second point: even an independent cap-one hub scalar together with a residual three-dimensional vector whose full joint density and all coordinate one-/two-dimensional marginals are bounded can still be straightened by a nonlinear reciprocal shear into a logarithmically singular output. Thus the remaining mechanism must retain **simultaneous linear-product provenance**, not merely a collection of marginal-density estimates.

## 7. Honest status

`QFORM-CIRCULAR-SCALAR-BANK-COMPILER-BARRIER-v1` is proved. It closes a specific structural question raised by the newest designated-partner theorem and narrows the circular two-sheet debt to a genuinely three-dimensional product-preserving aggregation problem.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity for the unrestricted target is separate and is not claimed here.

No literature search miss is used as evidence of novelty. The external theorem actually used is the exact Livshyts--Paouris--Pivovarov marginal-density theorem at its published hypotheses; the required pinned e5f ruled-surface theorem is applied only on its one-sheet half-line; and the fleet03/B18 theorem is applied only to exact disjoint original-coordinate scalar banks.
