SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-22T23:46:22Z.
attacking: N3 no-pivot hybrid: source-coordinate hub plus dense nonseparable light block; derive a bilinear/square-lift payment retaining all curvature.

# fleet01/B09 QFORM r19 — two-pivot product closure and a no-pivot grouped-bank routing simplification

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B09-20260922T234622Z-r19`  
Classification: **ESSENTIAL_STEP_APPLIED / ROUTE_NODE_CLOSED / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **not proved by the new pair endpoint; essential boundedness and linear interval anti-concentration are proved on the stated branches.**

## 1. Exact target, fresh control, and correction boundary

The target is unchanged: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one dimension/law/matrix-independent constant `C` such that `X^T A X` has an essentially bounded density `<=C`, or give a valid counterexample. The stronger request for a continuous density is tracked separately.

Fresh control was read on `yspennstate/math-research-brain` main. The prewrite control commit was

`d3cdecfa1c922008cf324d5755de69578cebfa74`,


`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`

at

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`.

The following live corrections are respected throughout: no law-uniform pointwise quadratic-phase decay; no post-rotation independence; no arbitrary-joint rank-three coarea bound; no worst conditional projection-density moment/supremum; no universal single physical minor or rank-three cross-cut extraction. No moments, Gaussianity, log-concavity, compact support, connected support, identical laws, or centeredness are used.

## 2. Newest completed designated partner input

The newest completed `fleet02/B09` result available before publication is run

`20260922T234138Z-fleet02-B09-QFORM-r12`,

canonical proof

`yspennstate/math-open-problems@0cb1fed576ea640d3458dce48470f09346c6e216`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T234138Z-fleet02-B09-QFORM-r12/REPORT.md`.

Its theorem `QFORM-HYPERBOLIC-EXTERNAL-SQUARE-v1` states that for mutually independent scalar variables `U,V,W` with density caps `N_U,N_V,N_W`,

`F=2aUV+bU+cV+d(W+alpha U+beta V+gamma)^2+e`, `ad!=0`,

has

`||p_F||_infinity <= 4 sqrt(2) N_W sqrt(N_U N_V) / sqrt(|ad|)`.      (2.1)

It also proves the exact algebraic bridge: if the corresponding scalar `3x3` quadratic matrix `G` has Schur complement `[[0,a],[a,0]]` across the `W` pivot and `sigma_min(G)>=s`, then

`|ad|>=s^2`.                                                        (2.2)

For three pairwise-disjoint original-coordinate **unit-projection banks**, projection-density caps give the target-level consequence

`||p_F||_infinity <= 8 sqrt(2)/s`,                                  (2.3)

with arbitrary outside conditioning that only changes affine terms. This is a genuine linear interval bound; no probability squaring or square-root interval loss is used.

I apply (2.3) below to an actual no-pivot target family.

## 3. New theorem: any quantitative two-scalar-pivot state is already a physical-pair state

### Theorem `QFORM-TWO-PIVOT-PRODUCT-CLOSURE-v1`

Let `A` be real symmetric with `s_3(A)>=s>0`. Let `i!=p` be two ORIGINAL coordinates. Suppose the first scalar physical Schur pivot is

`a=A_ii !=0`,

and, after eliminating coordinate `i`, the second physical scalar pivot at `p` is

`d=A_pp-A_pi^2/a !=0`.                                              (3.1)

Let

`B=A[{i,p},{i,p}]`.

Then the exact physical determinant identity is

`boxed: det B = a d.`                                               (3.2)

Consequently:

1. if `ad>0`, the physical pair `B` is definite and

`boxed: ||p_{X^TAX}||_infinity <= pi / sqrt(|ad|);`                 (3.3)

2. if `ad<0`, the physical pair `B` is indefinite and the newest determinant-only pair theorem gives

`boxed: ||p_{X^TAX}||_infinity
       <= |ad|^(-1/2) [9.2+log_+(10000 sqrt(|ad|)/s)].`              (3.4)

All remaining coordinates, same-side curvature, couplings, signs, extra eigenvalues, and affine terms are arbitrary.

### Proof

After merely permuting original coordinates, write the physical principal pair as

`B=[[a,q],[q,c]]`.

The scalar Schur complement of `a` is `d=c-q^2/a`. Hence

`det B=ac-q^2=a(c-q^2/a)=ad`, proving (3.2).

If `ad>0`, then `det B>0`; since `B` is a real symmetric invertible `2x2` matrix, its two eigenvalues have the same sign. Condition on all coordinates outside `{i,p}`. The two remaining variables are still independent with density caps one. Completing the square only translates them. The standard two-dimensional definite quadratic change of variables gives conditional density cap `pi/sqrt(det B)` (and reflection handles the negative-definite case). The cap is uniform in the conditioning, so averaging proves (3.3).

If `ad<0`, then `B` is an actual indefinite nonsingular original-coordinate principal block with determinant magnitude `D=|ad|`. The newest Claude synthesis, Theorem 3.1 in `GEOMETRIC_SYNTHESIS.md`, applies directly under `s_3(A)>=s` and yields

`||p_Q||_infinity <= D^(-1/2)[9.2+log_+(10000 sqrt(D)/s)]`,

which is (3.4). This theorem already retains arbitrary ambient spectrum, curvature and affine terms, so no additional conditioning interface is introduced. QED.

## 4. The previously unpaid opposite-sign two-pivot route is closed

A prior proof-assembly branch, recorded in `fleet02/B20` run

`20260922T210111Z-fleet02-B20-QFORM-r19`,

had already produced two successive physical pivots satisfying

`a d<0`,

`|a| >= m :=3501/8000`,

`|d| >1/8`.                                                        (4.1)

That report then spent the third spectral direction to obtain either a physical triple or a residual cross bank and left `QFORM-OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAYMENT-v1` unpaid.

The new determinant-only pair theorem makes that extra routing unnecessary. By (3.2) and (4.1), the ORIGINAL physical pair `{i,p}` already has

`D=|det B|=|ad| > (3501/8000)(1/8)=3501/64000`.                    (4.2)

Since the pair is indefinite, (3.4) at `s=1` gives

`||p_Q||_infinity
 < (3501/64000)^(-1/2)
   [9.2+log(10000 sqrt(3501/64000))]
 =72.5026347572... <73`.                                           (4.3)

Thus

`boxed: P{X^TAX in I} <73 |I|`                                    (4.4)

on the entire former opposite-sign two-pivot survivor, with no need to expose or pay the later residual Schur cross bank.

For comparison, if the same pivot magnitudes occur with `ad>0`, (3.3) gives the much smaller bound

`pi / sqrt(3501/64000)=13.4320965330...`.                          (4.5)

Therefore **every** two-pivot state with the magnitudes in (4.1), regardless of sign, is paid by `<73` before any third-resource routing.

This closes a concrete previously named unpaid node; it does not prove that every target matrix admits such two pivots.

## 5. Fixing the no-pivot reduction at tau=1/128 removes the heavy-edge packet

The newest Claude synthesis proves that it suffices to establish `N3(tau,C0)` for any one fixed `tau in (0,1]`, where `N3` is the full target restricted to matrices satisfying

`|A_ii|<tau`,

`|det A[{i,j},{i,j}]|<tau` for every `i!=j`.                       (5.1)

Fix once and for all

`tau_0=1/128`.                                                     (5.2)

Then every no-`tau_0`-pivot matrix obeys an entrywise off-diagonal bound. Indeed, for `i!=j`,

`A_ij^2
 =A_ii A_jj-det A[{i,j},{i,j}]
 <=|A_ii A_jj|+|det A[{i,j},{i,j}]|
 <tau_0^2+tau_0
 <2 tau_0=1/64`.

Hence

`boxed: |A_ij|<1/8 for every i!=j.`                                (5.3)

This immediately interacts with the fresh `fleet02/B20` r22 physical-packet reduction. That result says its O0 anchored survivor is forced, after the already-paid high-`E_5` branch, into one of

`H: |b|>1/8`,

`P: ||c||_2 ||r||_2 ||D||_F >1/(32 sqrt(3))`,

`R: E_2(D)>1/48 and E_5(D)<1/1024`,                               (5.4)

where `b` is an actual physical cross-block entry. Inside `N3(1/128)`, (5.3) makes `H` **impossible**. Thus the O0 packet obligation inside the sufficient no-pivot class reduces to only `P` or `R` (plus the already-paid `D5` branch).

There is a second exact simplification. For any two successive scalar physical pivots `a,d`, (3.2) gives

`|ad|=|det A[{i,p},{i,p}]|<1/128`                                 (5.5)

inside `N3(1/128)`. Therefore the quantitative two-pivot state (4.1) is not merely paid; it cannot occur in the no-pivot core at all.

This is useful proof bookkeeping: the full reduction should not keep asking N3 to pay a branch that the determinant identity has already routed outside N3.

## 6. Required designated-partner application: a genuine N3 family is paid at grouped scale

The no-pivot restrictions do **not** mean that all useful bilinear/square resources are small. The designated partner theorem r12 makes this precise.

For an integer `m>=129`, split `3m` original coordinates into three disjoint banks `I,J,K`, each of size `m`, and define normalized original-product projections

`U=m^(-1/2) sum_{i in I} X_i`,

`V=m^(-1/2) sum_{j in J} X_j`,

`W=m^(-1/2) sum_{k in K} X_k`.

Consider

`Q_m=2UV+W^2`.                                                    (6.1)

The active compressed matrix in `(U,V,W)` coordinates is

`G=[[0,1,0],[1,0,0],[0,0,1]]`,                                  (6.2)

so its eigenvalues are `{-1,1,1}` and `sigma_min(G)=1`. Thus the full physical matrix satisfies the target hypothesis `s_3(A)=1`.

At the physical-coordinate level, every diagonal coefficient is either `0` or `1/m`; every nonzero physical `2x2` principal determinant is `-1/m^2` (an `I-J` pair), while all other physical pair determinants vanish. Therefore, for `m>=129`,

`|A_ii|<=1/m<1/128`,

`|det A[{i,j},{i,j}]|<=1/m^2<1/128`.                              (6.3)

Hence `Q_m` is a genuine member of `N3(1/128)` despite every fixed physical coefficient tending to zero.

Now apply fleet02/B09 r12, equation (2.3), with the three unit-projection banks and `s=1`. It gives the actual target-level inequality

`boxed: ||p_{Q_m}||_infinity <=8 sqrt(2)<11.314`,                  (6.4)

and hence

`boxed: P{Q_m in I} <=8 sqrt(2) |I|`                              (6.5)

for every interval `I`, every `m>=129`, and every admissible product input law.

This is the required equation-level use of the designated partner. It also shows exactly why N3 must be attacked at **grouped original-coordinate scale**: its physical pivots can all vanish while an aggregate three-bank Schur-gap product remains order one.

## 7. What remains after this run

The full conjecture remains open. The useful first unpaid B09 implication is now narrower:

### `QFORM-N3-PACKET-P-OR-R-GROUPED-ROUTING-v1`

Work inside `N3(1/128)`. After the already-paid `D5` branch and the elimination of the heavy physical edge `H`, the fresh physical O0 packet reduction leaves only

`P: ||c||_2 ||r||_2 ||D||_F >1/(32 sqrt(3))`,                    (7.1)

or

`R: E_2(D)>1/48, E_5(D)<1/1024`.                                 (7.2)

Product-preservingly prove that either

1. these resources yield a three-bank hyperbolic-Schur compression with a fixed scalar singular gap, so fleet02/B09 r12 gives an `O(|I|)` bound;
2. they yield two disjoint hyperbolic packets, so the existing four-bank hyperbolic-convolution theorem pays them;
3. they trigger an already-paid `D'`, ridge, definite, pair, or grouped-square branch;
4. or identify a genuinely new overlapping-operator obstruction and estimate it without conditioning away the third source direction.

The critical constraint is source provenance: `P` contains aggregate norms on actual physical banks but does not by itself align the star vectors with a singular direction of `D`. Replacing it by a rotated scalar triple without proving a product-preserving bank construction would repeat the prohibited post-rotation-independence error.

## 8. Status and exact mathematical change

- **New proved structural identity/payment:** two successive physical scalar Schur pivots are exactly one original physical pair with determinant `ad`; the newest determinant-only pair theorem closes every quantitative opposite-sign two-pivot branch directly.
- **Closed old unpaid node:** `QFORM-OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAYMENT-v1` is no longer needed on the source branch (4.1); bound `<73` already holds.
- **No-pivot specialization:** fixing the sufficient reduction at `tau=1/128` gives `|A_ij|<1/8`, eliminating the fresh r22 heavy-edge packet `H` and excluding the old moderate two-pivot state from N3.
- **Designated partner applied:** the newest fleet02/B09 r12 theorem pays the genuine no-pivot family `2UV+W^2` by `8sqrt(2)` uniformly in bank size and input laws.
- **Full target:** OPEN / NOT PROVED / NOT DISPROVED.
- **Continuity:** no new unrestricted continuity theorem is claimed; the new pair endpoint is used only for essential boundedness and linear interval anti-concentration.
