SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B01, 2026-09-24T07:00:34Z.
attacking: the exact single-leaf endpoint left by the grouped rank-one arrowhead theorem; spend the third spectral direction before any reciprocal vanishing tail is paid.

# account02/B01 — exact single-leaf third-curvature compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T070034Z-account02-B01-QFORM-auto11`  
Role: Oscillatory replacement / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW EXACT-ENDPOINT COMPILER / FULL QFORM OPEN**

## 1. Scope and correction boundary

Throughout, all random scalar coordinates are ORIGINAL independent coordinates with probability densities bounded by one. There are no moment, compact-support, connected-support, Gaussian, iid, log-concavity or smoothness assumptions. Deterministic diagonalizations are used only inside already-proved coefficient theorems; no rotated random coordinates are declared independent. Essential boundedness is the target; continuity is not asserted unless a cited theorem separately supplies it.

The phase-aligned-density obstruction remains in force. For every nonzero frequency `s` and every small `eta>0`, one can choose a cap-one probability density supported on a finite union of intervals in `{x:dist(sx^2,2pi Z)<=eta}` and obtain `Re E exp(isX^2)>=cos eta`. Hence no positive law-uniform pointwise power decay for a scalar quadratic phase is used below.

The live correction ledger was refreshed. In particular this report does not use arbitrary-joint coarea, conditional projection-density caps, post-rotation independence, a uniformly well-conditioned fixed physical minor, or the false assertion that a small coefficient matrix is a small random quadratic perturbation on arbitrary unbounded product inputs.

The full QFORM conjecture remains OPEN.

## 2. Source-pinned inputs actually spent

### 2.1 Required 20260922T211500Z Fourier report

Required source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

I use the following proved statements at explicit equations below.

1. Fractional potentials from Fourier/rearrangement: for `0<alpha<1`,

`H_alpha(Z):=sup_s E|Z-s|^(-alpha)`
` <= c_alpha integral |t|^(alpha-1)|phi_Z(t)| dt`.             (2.1)

2. Scalar-square peel: if a literal original coordinate has nonzero coefficient `a` and exact completion

`Q=a(X+h)^2+S`,                                                   (2.2)

then

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(S)`,                    (2.3)

and, for `alpha<1/2`,

`H_alpha(Q)<=M_alpha |a|^(-alpha)`, with `M_(1/4)<=4`.           (2.4)

3. The two-square logarithmic half-potential estimate in Corollary 4.4(iv): after a literal scalar completion,

`H_(1/2)(a(V+h)^2+T)`
` <= |a|^(-1/2)[8+2 sup_s E log_+(|a|/(4|s-T|))].`              (2.5)

4. Scalar Schur persistence from `RESULTS.md`, Lemma 4: if a symmetric coefficient matrix has `k` eigenvalues of modulus at least one and a literal scalar pivot is nonzero, the scalar Schur complement retains at least `k-1` such eigenvalues. This is used at (4.8) and (5.3).

The same pinned source's D/D'/D5 cross-volume results are tested on an actual target obstruction in Section 7.

### 2.2 Orientation-free rank-two half-Riesz theorem

Source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an exact rank-two quadratic coefficient with nonzero eigenvalues represented by an invertible symmetric `2x2` matrix `Lambda`, and for an arbitrary original-coordinate affine term,

`H_(1/2) <= 128 |det Lambda|^(-1/4).`                           (2.6)

There is no leverage assumption and no affine-in-range assumption. I use (2.6) only after conditioning to an actual two-coordinate product block.

### 2.3 Earlier B01 generic-edge quarter-potential

Source:

`yspennstate/math-open-problems@25a695084d9acb02a3c81da41ef3e23953fb1a34`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T050513Z-account02-B01-qform-auto11/REPORT.md`.

If an arbitrary ambient quadratic polynomial contains a literal physical edge `mu!=0`, then

`H_(1/4) <= C_edge |mu|^(-1/4)`,
`C_edge=3.179662567631707...`.                                  (2.7)

The proof is an averaged-frequency argument: conditional Cauchy-Schwarz plus Plancherel gives `|phi(t)|<=min(1,sqrt(pi/(|mu t|)))`, and (2.1) at `alpha=1/4` pays the quarter-potential. It does not assert scalar Fresnel decay.

### 2.4 Previous B01 endpoint and newest partner

The immediately preceding B01 result is

`yspennstate/math-open-problems@fb7b0f71ead32ea608ff9ec45370edc246f7239e`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T063552Z-account02-B01-qform-auto11-r46/REPORT.md`.

It pays every rank-one two-hub arrowhead with at least two nonzero leaf slopes by half-Riesz, but its heavy-leaf estimate deteriorates like `theta^(-1/4)` as the tail slope tends to zero. It also proves by the example `(S+Y)^2` that a shape-free half-Riesz bound depending only on the aggregate arrowhead slope is false at a single leaf. Thus the first unpaid implication is the exact/almost-single-leaf endpoint, and the third spectral direction has to be spent structurally.

The newest compatible designated-partner account03/B01 theorem is

`yspennstate/math-open-problems@17d8c84cf1b4bf67dab6340ffa0ea432c6feb8f6`

with source addendum `7b617d334690a672477a5cd834bf27731d262ef4`, report

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260924T063007Z-account03-B01-qform-auto11-r46/REPORT.md`.

It proves, for an invertible indefinite physical pair `P`,

`||p_Q||_infinity <=14.180833 D^(-3/10)(kappa lambda)^(-1/5)`,  (2.8)

where `D=|det P|`, `kappa=sigma_min(P)`, and `lambda=s_3(A)>0`. It also proves universal square-root-log concentration for every nonzero quadratic coefficient. Section 8 below spends (2.8) at an actual target inequality.

## 3. A simple log-to-quarter conversion

For every `z>0`,

`log_+ z <= 4 z^(1/4)`.                                         (3.1)

Indeed the left side vanishes for `z<=1`, while for `z>=1` the standard inequality `log z<=z^alpha/alpha` with `alpha=1/4` applies. Hence if `H_(1/4)(T)<=H`, then for every `A>0`,

`sup_s E log_+(A/|s-T|) <=4 A^(1/4) H`.                        (3.2)

Combining (3.2) with the required source's two-square estimate (2.5) gives

`H_(1/2)(a(V+h)^2+T)`
` <=8|a|^(-1/2)+8*4^(-1/4) H |a|^(-1/4).`                      (3.3)

This is the bridge used below. It spends an averaged quarter-potential to pay the logarithmic singularity of a physical square; no pointwise oscillatory estimate appears.

## 4. Main supporting lemma: any 3-variable coefficient with two large singular directions has bounded half-potential

### Theorem 4.1 — `QFORM-3D-S2-HALFRIESZ-v1`

Let `C` be a real symmetric `3x3` matrix with at least two eigenvalues of modulus at least one. Let `Z=(Z_1,Z_2,Z_3)` have independent cap-one densities, and let arbitrary affine terms be added. Then

`boxed: H_(1/2)(Z^T C Z + affine) < 169.`                       (4.1)

No sign or nonzero-principal-minor hypothesis is imposed.

### Proof

Fix

`delta=1/100`.                                                   (4.2)

There are two exhaustive ORIGINAL-coordinate cases.

#### Case A: every physical diagonal is small

Assume

`max_i |C_ii| < delta`.                                         (4.3)

Because at least two singular values of `C` are at least one,

`||C||_F^2 >=2`.                                                (4.4)

Therefore

`2 sum_(i<j) C_ij^2
 =||C||_F^2-sum_i C_ii^2
 >2-3delta^2`.                                                  (4.5)

Some physical edge `mu=C_ij` consequently satisfies

`mu^2 >(2-3delta^2)/6`.                                         (4.6)

For the literal two-coordinate principal block

`B=[[C_ii,mu],[mu,C_jj]]`,

we have

`det B=C_ii C_jj-mu^2<0`, and

`|det B|
 =mu^2-C_ii C_jj
 >=mu^2-|C_ii C_jj|
 >1/3-(3/2)delta^2
 =0.3331833333... .`                                            (4.7)

Condition on the third ORIGINAL coordinate. The conditional quadratic polynomial in the remaining two independent coordinates has exact invertible rank-two coefficient `B` and an arbitrary affine term. The orientation-free theorem (2.6) gives

`H_(1/2)
 <=128 [1/3-(3/2)delta^2]^(-1/4)
 =168.4764304556... <169.`                                      (4.8)

Averaging the conditioning and taking the supremum over the target shift preserves this bound.

#### Case B: a physical diagonal is not small

Assume some literal pivot `a=C_ii` satisfies

`|a|>=delta`.                                                    (4.9)

Complete this ORIGINAL coordinate exactly:

`Z^T C Z + affine = a(Z_i+h)^2+T`,                              (4.10)

where `T` is a quadratic-plus-affine polynomial in the two remaining independent original coordinates. By scalar Schur persistence from the required pinned source, the `2x2` quadratic coefficient of `T` has at least one eigenvalue of modulus at least one, hence operator norm at least one.

For a symmetric `2x2` matrix `[[p,q],[q,r]]`,

`||.||_op <= max row-sum <=2 max(|p|,|q|,|r|)`.                 (4.11)

Thus one physical coefficient of `T` has magnitude at least `1/2`.

If that coefficient is a diagonal, the required source's universal square quarter-potential (2.4) gives

`H_(1/4)(T)<=4(1/2)^(-1/4)=4*2^(1/4).`                         (4.12)

If it is an off-diagonal edge, (2.7) gives the even smaller bound

`H_(1/4)(T)<=C_edge(1/2)^(-1/4)<4*2^(1/4).`                    (4.13)

Hence in all cases

`H_(1/4)(T)<=H_0:=4*2^(1/4).`                                  (4.14)

Insert (4.14) into the averaged log bridge (3.3). Since `|a|>=delta`,

`H_(1/2)
 <=8 delta^(-1/2)+32*2^(-1/4)delta^(-1/4)
 =165.0927343511... <169.`                                     (4.15)

Cases A and B prove (4.1). QED.

The key feature is that the proof never asks for one uniformly good physical principal pair. If all diagonals are tiny, the **aggregate Frobenius mass forced by two large singular directions** creates one good indefinite pair. If a diagonal is visible, the second singular direction is spent after scalar Schur completion through a quarter-potential and the logarithmic half-potential interface.

## 5. Exact single-leaf arrowhead compiler

Return to the finite-leak rank-one two-hub arrowhead state from the preceding B01 run. After one literal outer completion,

`Q=a_0(X_0+h)^2+R`, `a_0!=0`.                                  (5.1)

At the exact single-leaf endpoint, the Schur remainder has only one nonzero hub-to-leaf slope. Thus, after relabelling ORIGINAL coordinates, its quadratic coefficient is block diagonal

`S = C direct_sum diag(d_1,...,d_m)`,                           (5.2)

where `C` is a symmetric `3x3` coefficient on the two literal hubs and the single active literal leaf; the remaining zero-slope leaves have arbitrary diagonal twists. Affine terms are arbitrary.

Because the full target has `s_3(A)>=1`, scalar Schur persistence at the outer pivot gives

`S has at least two eigenvalues of modulus >=1.`                (5.3)

### Theorem 5.1 — `QFORM-EXACT-SINGLELEAF-THIRDCURVATURE-v1`

Under (5.1)-(5.3),

`boxed: H_(1/2)(R) <169`,                                       (5.4)

and therefore, by the required source's square peel,

`boxed: ||p_Q||_infinity <169 |a_0|^(-1/2).`                   (5.5)

In particular, in a high-pivot chamber `|a_0|>=1/64`,

`boxed: ||p_Q||_infinity <1352.`                                (5.6)

### Proof

Because (5.2) is block diagonal, the large singular values of `S` are exactly the multiset union of those of `C` and the numbers `|d_j|`. There are three exhaustive spectral allocations.

**(i) The 3-variable core has two large directions.** If `s_2(C)>=1`, Theorem 4.1 gives `H_(1/2)(core)<169`. The diagonal zero-slope tail is independent and additive. Conditioning on its value merely translates the target in the definition of `H_(1/2)`, hence cannot increase the supremum. Thus (5.4) follows.

**(ii) Two diagonal tail coefficients are large.** If distinct `j,k` satisfy `|d_j|,|d_k|>=1`, condition on every coordinate except these two. Their conditional quadratic coefficient is `diag(d_j,d_k)`, while all induced linear terms are arbitrary. The orientation-free rank-two theorem (2.6) gives

`H_(1/2)(R)<=128 |d_jd_k|^(-1/4)<=128<169.`                    (5.7)

**(iii) One large tail square and one large core direction.** The only remaining possibility compatible with (5.3) is: exactly one tail coefficient satisfies `|d|>=1`, the core has `s_1(C)>=1` but `s_2(C)<1`.

Since `||C||_op>=1` and a `3x3` row sum is at most three times the largest absolute matrix entry, some physical coefficient of `C` has magnitude at least `1/3`. If it is a diagonal, (2.4) gives `H_(1/4)(core)<=4*3^(1/4)`; if it is an edge, (2.7) gives a smaller constant. Therefore

`H_(1/4)(core)<=4*3^(1/4).`                                    (5.8)

Conditioning on all additional diagonal-tail coordinates preserves (5.8). Apply the log-square bridge (3.3) to the one large independent tail square `dY^2+affine`, with `|d|>=1`. This yields

`H_(1/2)(R)
 <=8+16sqrt(2)*3^(1/4)
 =37.7793554913... <169.`                                      (5.9)

The three cases are exhaustive, proving (5.4); (5.5) is exactly (2.3). QED.

This closes the **exact** `theta=0` endpoint that the preceding grouped-arrowhead half-Riesz theorem necessarily left open. It does so by spending the target's third spectral direction before paying any reciprocal tail coefficient.

## 6. Why this does not contradict the exact single-leaf half-Riesz obstruction

The preceding run's obstruction

`R=(S+Y)^2`

can indeed have `H_(1/2)(R)=infinity` for admissible independent laws. Its coefficient has only one large singular direction. Theorem 5.1 assumes the exact single-leaf state arises as a Schur remainder of a target with three large directions, so (5.3) forces **two** large directions in the remainder. That additional curvature is exactly what the obstruction lacks.

Thus the new theorem does not assert a false shape-free arrowhead half-potential; it identifies and spends the missing target-level spectral resource.

## 7. Concrete full-target stress family and required-source obstruction

Consider four independent cap-one coordinates `(X_0,H_1,H_2,Y)` and

`Q_sharp = X_0^2 + H_1^2+H_2^2+Y^2`
`          +2H_1H_2+2H_1Y-2H_2Y`.                              (7.1)

The residual `3x3` coefficient is

`C_sharp=[[1,1,1],[1,1,-1],[1,-1,1]]`,                         (7.2)

whose eigenvalues are `{-1,2,2}`. Hence the full matrix has spectrum

`{-1,1,2,2}`,                                                   (7.3)

so it is an exact owner-target example. It is also an exact single-leaf rank-one two-hub arrowhead: the sole leaf `Y` sees the hub slope `(1,-1)`.

Every physical `2x2` principal determinant **inside the residual core** is zero, because each is `1*1-(+/-1)^2`. Thus a strategy requiring an invertible residual physical pair fails maximally on this example.

Nevertheless, complete the literal hub coordinate `H_1`, whose pivot is `a=1`. Its scalar Schur complement on `(H_2,Y)` is

`T=[[0,-2],[-2,0]]`.                                             (7.4)

The actual edge `mu=-2` and the averaged-frequency theorem (2.7) give

`H_(1/4)(T)<=C_edge 2^(-1/4)=2.67376685484...`.                 (7.5)

Spend the required source's logarithmic square estimate through (3.3):

`H_(1/2)(residual core)
 <=8+(8/sqrt(2))*2.67376685484...
 =23.1251093949... .`                                           (7.6)

The outer literal square `X_0^2` and the required source's square peel therefore give the concrete target-level inequality

`boxed: ||p_(Q_sharp)||_infinity <=23.126.`                      (7.7)

This also supplies an actual obstruction/application of the pinned D/D'/D5 results. In dimension four every disjoint original-coordinate cross block has rank at most two. Therefore for every physical cut

`e_3(M^T M)=e_5(M^T M)=0`.                                     (7.8)

The pinned third- and fifth-volume currencies are identically zero on this target family, while the averaged quarter-potential + logarithmic square route gives (7.7).

## 8. Newest designated-partner theorem spent at an actual target inequality

Take three independent cap-one coordinates `(X_0,U,V)` and

`Q_pair=X_0^2+2UV`.                                              (8.1)

Its coefficient spectrum is `{1,1,-1}`, so `s_3(A)=1`. The physical pair `(U,V)` is

`P=[[0,1],[1,0]]`,                                               (8.2)

hence `D=|det P|=1`, `kappa=1`, and `lambda=s_3(A)=1`. The newest account03/B01 theorem (2.8) gives the actual full-target estimate

`boxed: ||p_(Q_pair)||_infinity <=14.180833.`                    (8.3)

This application is deliberately separate from the singular-pair stress family (7.1): every residual physical pair of (7.2) is singular, so the partner's invertible-pair receiver cannot by itself pay that exact core. The present theorem supplies the complementary mechanism.

## 9. First unpaid implication

The exact endpoint is now paid, while the preceding grouped-arrowhead theorem pays every fixed nonzero tail with a cost proportional to `theta^(-1/4)`. The remaining sharp debt is therefore

`QFORM-ALMOST-SINGLELEAF-ENDPOINT-STABILITY-v1`:

> In the rank-one two-hub finite-leak Schur state, obtain a bound uniform as the nonzero tail norm tends to zero. The proof must allocate the two large Schur singular directions from `s_3(A)>=1` before using the weak tail, and must not treat the small tail coefficient matrix as a small random perturbation on arbitrary unbounded product inputs.

A promising next mechanism is to combine the exact-endpoint spectral allocation above with the newest account03/B01 square-root-log concentration theorem, so that the weak tail is used only through a distribution-function average rather than through `theta^(-1/4)` inversion. If that leaves the same quantitative loss for three attempts, the mechanism should change to a literal 3-variable/physical-pair partition.

Full unrestricted QFORM remains OPEN.
