SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T18:48:04Z.
attacking: the exact diagonal-plus-rank-at-most-four carrier endpoint left by r38, using a random ORIGINAL-coordinate cut and aggregate third-volume bilinear smoothing before any individual-minor inversion.

# fleet03/B09 r39 — diffuse finite-rank carrier smoothing and a 256-coordinate localization fork

## Status

**NEW SUPPORTING THEOREM / FIRST EXACT r38 CARRIER ENDPOINT PAID / FULL QFORM OPEN.**

The unrestricted quadratic-form bounded-density conjecture remains **OPEN**. This run solves a substantial part of the first endpoint left by fleet03/B09 r38. If an original-coordinate diagonal plus rank-three/rank-four carrier is diffuse in physical coordinates, a literal physical cut has enough aggregate third cross-volume to give a continuous bounded density. Without a global diffuseness assumption, either the same payment is available or one carrier direction is quantitatively localized on at most 256 original coordinates.

No random variable is rotated. All cuts are partitions of the original independent coordinates. No pointwise scalar van-der-Corput bound, arbitrary-joint coarea estimate, moment/support assumption, square-root small-ball conversion, or deletion of a small quadratic term is used.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source-pinned premises

Fresh owner control was resolved from `yspennstate/math-research-brain` main at source commit

`40024d459ee9559e24841ef53535df834761c6d9`.


The relevant mathematical inputs are:

1. **fleet03/B09 r38 dual aggregate collapse.** Canonical source
   `yspennstate/math-open-problems@b2a0ccad9d4f4d654e0fc84dd0323ce84230ebc4`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T175610Z-fleet03-B09-QFORM-r38/REPORT.md`.
   At exact two-sided singleton aggregate zero it gives
   `A=D_0+S`, where `D_0` is diagonal in the original physical coordinates and `rank S<=4`. If `s_3(A)>=1` and `||D_0||op<=tau`, then
   `s_3(S)>=1-tau`.

2. **Independently checked weighted-subset / projected-crossing theorem.** Canonical source
   `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
   `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.
   I use its weighted-subset Fourier lemma at `k=0, ell=3`; Section 2 below derives this empty-hub specialization explicitly from that source, so no unspoken convention about a zero-dimensional hub is needed.

3. **Designated partner fleet04/B09.** Canonical source
   `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.
   For a literal invertible physical `3x3` cross block `K`, with arbitrary same-side curvature,
   `||p_Q||inf <=3 |det K|^(-1/3)`, with a continuous density.

All live corrections are respected: bounded density does not imply law-uniform pointwise quadratic-phase decay; spectral rotation does not preserve independence; a bounded projection density alone does not control an indefinite quadratic pushforward; the arbitrary-joint rank-three coarea lemma is false; and a single uniformly good physical minor is not forced by the target hypothesis.

## 2. Aggregate physical third-volume smoothing

This section records the exact bilinear receiver used below.

Let `J,I` be disjoint original-coordinate banks. After conditioning on all coordinates outside `I union J`, write the surviving form as

`Q=F(X_J)+2 X_J^T B X_I+G(X_I)`,                         (2.1)

where `F,G` may be arbitrary quadratic-plus-affine functions (depending on the conditioned outside coordinates) and

`B=A[J,I]`                                                        (2.2)

is the literal physical cross block.

Define

`Z_3(B)=e_3(BB^T)=sum_{R subset J, |R|=3} det(B_R B_R^T)`.       (2.3)

When `Z_3>0`, put

`w_R=det(B_R B_R^T)/Z_3`,
`alpha_j=sum_{R containing j} w_R`.                              (2.4)

### Lemma 2.1 — `QFORM-E3-PHYSICAL-CROSS-SMOOTHING-v1`

If

`alpha_j<=1/2` for every `j in J`,                               (2.5)

then the law of `Q` has a continuous density and

`boxed: ||p_Q||inf <= 6 sqrt(2e) Z_3(B)^(-1/6).`                 (2.6)

Consequently every interval `L` satisfies

`boxed: P{Q in L} <= 6 sqrt(2e) Z_3(B)^(-1/6) |L|.`             (2.7)

#### Proof

Let `Y=X_J`, `Z=X_I`. Cauchy--Schwarz in the probability measure of `Y`, followed by an independent copy `Z'`, gives

`|phi_Q(t)|^2
 <= E_D product_{j in J} |psi_j(2t <b_j,D>)|`,                  (2.8)

where `D=Z-Z'`, the coordinates of `D` are independent and each has a probability density at most one, `b_j` is row `j` of `B`, and the internal phases `F,G` have disappeared only through modulus one. This is exactly the checked weighted-subset Fourier lemma with `k=0`, `ell=3`, `M` the unique zero-row matrix, and `kappa=1`. It yields

`|phi_Q(t)|^2
 <= 2^(3/2) (2pi)^3 e^(3/2)
    Z_3(B)^(-1/2) |t|^(-3).`                                    (2.9)

Hence

`|phi_Q(t)|
 <= min{1,
        2^(9/4) pi^(3/2) e^(3/4)
        Z_3(B)^(-1/4) |t|^(-3/2)}.`                              (2.10)

The right side is integrable. If `K` denotes the coefficient of `|t|^(-3/2)` in (2.10), then

`(1/(2pi)) integral_R min(1,K|t|^(-3/2)) dt
 = (3/pi) K^(2/3)
 = 6 sqrt(2e) Z_3(B)^(-1/6).`                                   (2.11)

Fourier inversion proves continuity and (2.6); (2.7) follows by integrating the density. QED.

This is a direct `O(|L|)` bilinear-block estimate. It spends aggregate squared physical minors before any reciprocal individual-minor selection.

## 3. Volume marginals never exceed range leverage

The next deterministic lemma converts a diffuse carrier frame into the marginal gate (2.5).

### Lemma 3.1

Let `B` be any real matrix of rank `r>=3`, with thin SVD

`B=U Sigma W^T`, `U^T U=I_r`.                                   (3.1)

Let `alpha_i` be the size-three volume marginals (2.4). Then

`boxed: alpha_i <= sum_{a=1}^r U_{ia}^2
                 = (P_range(B))_{ii}.`                           (3.2)

#### Proof

For a row triple `R`, Cauchy--Binet in the singular directions gives

`det(B_R B_R^T)
 =sum_{T subset [r], |T|=3}
   det(U_{R,T})^2 product_{a in T} sigma_a^2.`                    (3.3)

Also

`Z_3(B)=e_3(sigma_1^2,...,sigma_r^2)
       =sum_{|T|=3} product_{a in T} sigma_a^2.`                  (3.4)

Thus the row-volume law is a convex mixture over three-element singular-direction sets `T`, with mixture weight proportional to `product_{a in T}sigma_a^2`, of the projection-DPP law

`P_T(R)=det(U_{R,T})^2`.                                         (3.5)

For fixed `T`, Cauchy--Binet gives total mass one, and its one-row marginal is

`sum_{R containing i} det(U_{R,T})^2
 =sum_{a in T} U_{ia}^2`.                                       (3.6)

Averaging (3.6) over `T` gives

`alpha_i<=sum_{a=1}^r U_{ia}^2`. QED.

The inequality is useful because the right side depends only on a range projection, not on the smallest nonzero singular value of `B`.

## 4. Diffuse diagonal-plus-rank-four carrier is paid

Let

`A=D+S`,
`S=V K V^T`,                                                     (4.1)

where

- `D` is diagonal in the original physical coordinates;
- `V in R^(n x r)` has orthonormal columns;
- `r in {3,4}`;
- `K=K^T` is invertible;
- `s_3(K)>=gamma>0`.

Let the physical row of `V` at coordinate `i` be `v_i^T`, and define its carrier leverage

`ell_i=||v_i||_2^2`, `q=max_i ell_i`.                            (4.2)

### Theorem 4.1 — `QFORM-DIAGONAL-PLUS-R4-DIFFUSE-CARRIER-v1`

If

`q<=1/16`,                                                       (4.3)

then for every admissible independent cap-one product law,

`boxed:
 ||p_{X^TAX}||inf
 <=24 sqrt(2e) gamma^(-1)
 <55.960 gamma^(-1).`                                            (4.4)

The density is continuous and the same coefficient multiplies interval length.

#### Proof

Choose a random physical partition `I disjoint J=[n]` by putting each coordinate into `J` independently with probability `1/2`. Put

`G_J=V_J^T V_J=sum_{j in J} v_j v_j^T`,
`G_I=I_r-G_J`.                                                   (4.5)

Since `E G_J=I_r/2` and the Bernoulli fluctuations are independent with mean zero,

`E ||G_J-I_r/2||_F^2
 = (1/4) sum_i ||v_i v_i^T||_F^2
 = (1/4) sum_i ell_i^2
 <= (q/4) sum_i ell_i
 = qr/4
 <=q.`                                                           (4.6)

Therefore some literal partition satisfies

`||G_J-I_r/2||op
 <=||G_J-I_r/2||F
 <=sqrt(q)<=1/4`.                                                 (4.7)

Hence

`G_I,G_J >=(1/4) I_r`.                                           (4.8)

Because `D` is physically diagonal, its cross block vanishes, and

`B:=A[J,I]=V_J K V_I^T`.                                        (4.9)

Write

`U_J=V_J G_J^(-1/2)`, `U_I=V_I G_I^(-1/2)`.                     (4.10)

Both have orthonormal columns, and the nonzero singular values of `B` are those of

`T=G_J^(1/2) K G_I^(1/2)`.                                      (4.11)

Thus

`s_3(B)=s_3(T)
 >=sqrt(lambda_min G_J) s_3(K) sqrt(lambda_min G_I)
 >=gamma/4`.                                                     (4.12)

Consequently

`Z_3(B)>=s_1(B)^2 s_2(B)^2 s_3(B)^2
       >=(gamma/4)^6`.                                           (4.13)

Since `K` and `G_I` are invertible,

`range(B)=range(V_J)`.                                           (4.14)

For `j in J`, its range leverage is

`(P_range(B))_{jj}
 =v_j^T G_J^(-1)v_j
 <=4 ell_j
 <=1/4`.                                                         (4.15)

Lemma 3.1 gives every third-volume marginal `alpha_j<=1/4<1/2`. Lemma 2.1 and (4.13) now yield

`||p_Q||inf
 <=6sqrt(2e) * (4/gamma)
 =24sqrt(2e) gamma^(-1).` QED.

This is uniform in all four-dimensional carrier anisotropy beyond the third singular value: when `r=4`, the fourth singular value of `K` may be arbitrarily small.

## 5. No global diffuseness: paid cross cut or a finite physical localization certificate

The previous theorem assumes `q<=1/16`. A second random-cut argument yields a useful unconditional structural fork for every rank-three/rank-four carrier.

### Theorem 5.1 — `QFORM-R4-CARRIER-DIFFUSE-OR-256-LOCALIZED-v1`

Under (4.1), without assuming (4.3), at least one of the following holds:

**(A) paid bilinear exit.** `Q=X^TAX` has a continuous density and

`boxed:
 ||p_Q||inf
 <= (48 sqrt(2e)/sqrt(3)) gamma^(-1)
 <64.617 gamma^(-1),`                                            (5.1)

with the same coefficient multiplying interval length;

or

**(B) finite physical localization.** There is a set `H` of at most `256` original coordinates and a unit vector `u in R^r` such that the unit carrier vector `Vu` obeys

`boxed: ||(Vu)_H||_2^2>1/2.`                                    (5.2)

#### Proof

Define the heavy physical set

`H={i: ell_i>1/64}`, `L=H^c`.                                   (5.3)

Since `sum_i ell_i=r<=4`,

`|H|<=64r<=256`.                                                 (5.4)

Put

`G_L=V_L^T V_L`, `G_H=I_r-G_L`.                                 (5.5)

If `lambda_min(G_L)<1/2`, choose a unit `u` realizing that minimum. Then

`||(Vu)_H||_2^2
 =u^T G_H u
 =1-u^T G_Lu
 >1/2`,                                                         (5.6)

which is alternative (B).

Assume instead

`G_L >=(1/2)I_r`.                                                (5.7)

Randomly put each light coordinate independently into `J` with probability `1/2`, and put every heavy coordinate into the other bank `I`. Then

`G_J=sum_{j in J}v_jv_j^T`,
`G_I=I_r-G_J`.                                                   (5.8)

Now

`E||G_J-G_L/2||_F^2
 =(1/4)sum_{j in L}ell_j^2
 <=(1/4)(1/64)sum_{j in L}ell_j
 <=1/64`.                                                        (5.9)

Hence some physical split has

`||G_J-G_L/2||op<=1/8`.                                         (5.10)

Using `G_L>=I/2` and `G_L<=I`,

`G_J >=(1/8)I_r`,
`G_J <=(5/8)I_r`,
`G_I=I-G_J >=(3/8)I_r`.                                         (5.11)

Orient the physical cross block with the **light selected bank as the row side**:

`B=A[J,I]=V_J K V_I^T`.                                         (5.12)

Exactly as in (4.11),

`s_3(B)
 >=sqrt(1/8) gamma sqrt(3/8)
 =sqrt(3) gamma/8`,                                              (5.13)

so

`Z_3(B)>=(sqrt(3)gamma/8)^6`.                                   (5.14)

Every row `j in J` is light. Since `range(B)=range(V_J)`,

`(P_range(B))_{jj}
 =v_j^T G_J^(-1)v_j
 <=8 ell_j
 <=1/8`.                                                        (5.15)

Lemma 3.1 supplies `alpha_j<=1/8`, so Lemma 2.1 gives

`||p_Q||inf
 <=6sqrt(2e) * 8/(sqrt(3)gamma)
 =48sqrt(2e)/(sqrt(3)gamma)`.                                    (5.16)

This is alternative (A). QED.

The orientation in (5.12) is essential: all heavy coordinates were deliberately placed on the opposite bank, so they do not enter the row-marginal gate.

## 6. Actual closure of the diffuse exact r38 carrier endpoint

Apply Theorem 5.1 to the exact-zero case of r38. Suppose r38 yields

`A=D_0+S`, `rank S<=4`,                                         (6.1)

and the target spectral condition gives `s_3(A)>=1`. If

`||D_0||op<=tau<1`,                                              (6.2)

then r38 gives

`gamma:=s_3(S)>=1-tau>0`.                                       (6.3)

Choose an orthonormal frame `V` for `range(S)` and write `S=VKV^T`. Its rank is three or four. Theorem 5.1 therefore gives the concrete dichotomy

`boxed:
 ||p_Q||inf<64.617/(1-tau)`                                      (6.4)

with a continuous density, **or** a unit vector in `range(S)` has more than half of its squared mass on at most 256 original coordinates.

If, more strongly, the carrier range leverage satisfies

`max_i (P_range(S))_ii<=1/16`,                                  (6.5)

Theorem 4.1 improves the paid branch to

`boxed: ||p_Q||inf<55.960/(1-tau).`                              (6.6)

For example, at `tau=1/4` the latter coefficient is

`74.6126074112`.                                                 (6.7)

This is the first analytic payment of the exact diagonal-plus-rank-at-most-four carrier endpoint produced by r38. It does **not** yet pay the finite-localization alternative or a nonzero retained residual `E` from r38's quantitative version.

## 7. Target-valid Walsh regression and aggregate-vs-single-minor comparison

Take `N=64`. Let `chi_1,chi_2,chi_3` be three independent Walsh characters on the 64 physical coordinates and define

`V_i=(1,chi_1(i),chi_2(i))/sqrt(N)`,
`A=VV^T`.                                                        (7.1)

Then `V^TV=I_3`, so the spectrum of `A` is exactly

`{1,1,1,0,...,0}`.                                               (7.2)

Thus this is a genuine target instance. Every physical carrier leverage is

`ell_i=3/64<1/16`.                                               (7.3)

Split the physical coordinates by the independent character `chi_3`. Orthogonality of Walsh characters gives exactly

`G_I=G_J=(1/2)I_3`.                                              (7.4)

Therefore the literal cross block `B=A[J,I]` has exactly three nonzero singular values

`1/2,1/2,1/2`,                                                   (7.5)

and

`Z_3(B)=1/64`.                                                   (7.6)

Every third-volume row marginal is exactly the range leverage

`alpha_j=6/64=3/32`.                                             (7.7)

Lemma 2.1 gives the concrete continuous-density estimate

`boxed:
 ||p_{X^TAX}||inf
 <=12 sqrt(2e)
 =27.9797277792... .`                                            (7.8)

This is dimension-free aggregate smoothing on an actual physical cut.

## 8. Required fleet04/B09 partner application at an actual inequality

Use the same target-valid Walsh family (7.1). Choose three distinct physical rows with sign patterns

`(chi_1,chi_2)=(1,1),(1,-1),(-1,1)`                              (8.1)

and three **different** physical columns with the same three patterns. Such disjoint choices exist because every pattern occurs 16 times.

For each selected row triple,

`|det V_R|=4/N^(3/2)`.                                           (8.2)

Hence the literal disjoint physical `3x3` cross block

`K=A[R,C]=V_R V_C^T`                                            (8.3)

satisfies

`|det K|=16/N^3=1/16384`.                                       (8.4)

The designated fleet04/B09 theorem therefore gives the actual inequality

`boxed:
 ||p_Q||inf
 <=3 |det K|^(-1/3)
 =3N/16^(1/3)
 =76.1952504945...`                                              (8.5)

for `N=64`, with a continuous density and direct interval bound.

The partner inequality is valid and is applied exactly at its stated physical-cross hypotheses. The aggregate third-volume cut (7.8) is substantially sharper on the same diffuse family because it pays all physical minors before taking a reciprocal power.

## 9. What remains

This run closes the **diffuse exact** diagonal-plus-rank-three/rank-four carrier branch and converts the general exact carrier into a two-way endpoint:

1. aggregate physical cross-volume smoothing with a universal `O(|L|)` bound; or
2. one carrier direction has more than half of its mass on a fixed set of at most 256 original coordinates.

The next B09 debt is

`QFORM-R4-CARRIER-256-LOCALIZED-OR-RESIDUAL-CROSSING-v1`:

> Route the finite-localization alternative into an already-paid physical pivot/hub/fixed-pair receiver, or iterate a product-preserving quotient split until three smoothing directions are paid. In parallel, extend the exact-carrier argument to r38's nonzero block-diagonal residual `E` without treating `E` as a small random quadratic error.

A small operator/Frobenius residual cannot simply be dropped because the admissible source laws have no support or moment bounds. Any robust extension must keep the residual in the phase or compile its physical cross-volume explicitly.

Full-target essential boundedness: **OPEN**.  
Full-target continuous density: **OPEN**.  
Continuity is proved for the paid branches in this report.

## 10. Finite checks

`CHECK.py` beside this report verifies:

- the Walsh frame is exactly orthonormal;
- the target matrix has three unit eigenvalues;
- the `chi_3` split has `G_I=G_J=I_3/2`;
- the cross singular values are `1/2,1/2,1/2`;
- `Z_3=1/64` and row marginals are `3/32`;
- the aggregate constant is `27.9797277792...`;
- a literal disjoint `3x3` partner block has determinant `16/N^3` and partner bound `76.1952504945...`;
- the theorem constants `24sqrt(2e)` and `48sqrt(2e)/sqrt(3)` are as displayed.

No histogram or Monte Carlo density estimate is used as proof evidence.
