SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T01:20:49Z.
attacking: the slope-dominant punctured near-coloop by locating its third projection direction exactly; convert the partner's normalized slope collar into mixed two-bank Pluecker volume, and test whether that volume is visible to the existing per-bank 3D punctured TT* receiver.

# account03/B16 current run — mixed-volume compiler for the slope collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T012049Z-account03-B16-QFORM-r38`  
**Role:** Projection-product interaction  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `NEW EXACT MIXED-VOLUME CERTIFICATE + NEW PER-BANK PUNCTURE BARRIER + TRUE-DENSITY CONTROL OF THE PREVIOUS TRACE-OBSTRUCTION FAMILY / FULL QFORM OPEN`  
**Regularity:** the new structural theorem is algebraic. The source-valid control family in Section 7 obtains an essentially bounded density; continuity is not proved there. Global continuity remains open.

## 1. Source boundary

The unrestricted owner target remains OPEN: independent real original coordinates with scalar probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concave, iid, connected-support, centering, or post-rotation independence hypothesis is added.


The live corrections are retained throughout. In particular, no arbitrary-joint indefinite coarea estimate, conditional projection-height moment, pointwise law-uniform quadratic stationary-phase estimate, worst-fiber supremum, or independence after rotation is used.

The completed mathematical inputs actually used are:

1. **Designated partner account04/B16 r3**, `yspennstate/math-open-problems@c47c53d4ef3e255431a6fb13960de1794bf2698f`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260923T211939Z-account04-B16-QFORM-r3/REPORT.md`.
   Its balanced near-coloop packet supplies the exact innovation/slope identity and, on the slope-dominant branch,
   `delta_J^2+delta_K^2<epsilon/2` and `d^T G_JG_K d>epsilon/2`.
2. **Two-bank exact identity**, account01/B16 at `yspennstate/math-open-problems@178419f09a3e2c7629d4e7ccc203b63a433916a5`, which supplies the least-squares coordinates used below.
3. **Zero-pivot conditional trace theorem**, account01/B16 at `yspennstate/math-open-problems@1bbe7c7c194bc92e10fc9c3cb3eb548d65e7043d`, used in Section 7 on the authentic family from the preceding B16 run.
4. The preceding same-slot mechanism obstruction, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260924T005411Z-account03-B16-QFORM-r38/REPORT.md`, which showed that the hub-first positive scalar-root half-potential diverges logarithmically along an authentic target family. The present run changes mechanism rather than repeating that positive-root trace.

## 2. Balanced two-bank notation

Work in the exact-rank-three near-coloop packet. In spectral coordinates write the physical leaf rows as

`r_i=(alpha_i,z_i) in R x R^2`,

and split the leaves into disjoint original-source banks `J,K`. Let `Z_B` be the `2 x |B|` matrix whose columns are the `z_i`, and put

`G_B=Z_B Z_B^T`, `B in {J,K}`.

The balanced packet satisfies

`G_J+G_K=I_2`,
`(1/4)I_2 <= G_J,G_K <= (3/4)I_2`.                              (2.1)

Write the bank longitudinal coefficient vector in its least-squares decomposition

`alpha_B=Z_B^T q_B+eta_B`,
`Z_B eta_B=0`,
`delta_B=||eta_B||_2`.                                          (2.2)

Let

`d=q_J-q_K`, `epsilon=1-h`.                                    (2.3)

The exact coupled identity is

`q_J=G_K d`, `q_K=-G_J d`,                                      (2.4)

and

`epsilon=delta_J^2+delta_K^2+d^T G_JG_K d`.                    (2.5)

The account04/B16 r3 slope-dominant branch is

`delta_J^2+delta_K^2<epsilon/2`,                                (2.6)
`d^T G_JG_K d>epsilon/2`.                                      (2.7)

It also implies `2epsilon<||d||^2<=(16/3)epsilon`, but the sharper currency for the present calculation is (2.7).

## 3. Exact result 1 — the normalized slope is invisible to each bank's 3D determinant

For one bank define its three-row coefficient matrix by taking the two transverse rows of `Z_B` together with the normalized longitudinal row `alpha_B/sqrt(epsilon)`. Its row Gram is

`T_B = [[G_B, G_B q_B/sqrt(epsilon)],
        [q_B^T G_B/sqrt(epsilon),
         (q_B^T G_B q_B+delta_B^2)/epsilon]]`,                  (3.1)

up to the harmless ordering of the scalar row.

### Theorem `QFORM-SLOPE-INVISIBLE-PERBANK-VOLUME-v1`

For both banks,

`boxed: det T_B=(delta_B^2/epsilon) det G_B.`                    (3.2)

In particular the whole least-squares slope `q_B`, including the order-`sqrt(epsilon)` slope separation forced by the partner collar, cancels exactly from the per-bank three-dimensional projection volume.

### Proof

Take the Schur complement of the positive definite block `G_B` in (3.1):

`(q_B^T G_B q_B+delta_B^2)/epsilon
 -(q_B^T G_B)G_B^(-1)(G_B q_B)/epsilon
 =delta_B^2/epsilon`.

Multiplication by `det G_B` proves (3.2). QED.

This is the first essential implication attempted in this run. It shows that the fresh completed punctured receiver that asks each bank for a genuine 3D projection density cannot simply be fed the normalized slope. If `delta_B->0`, the bank becomes rank two even though `||d||/sqrt(epsilon)` stays bounded away from zero.

## 4. Exact result 2 — resolve the third volume into the two mixed orientations

Let

`S_B=sum_(i in B) r_i r_i^T`.                                    (4.1)

Define the two mixed squared-volume masses

`M_JJK = sum_(i<j in J, k in K) det(r_i,r_j,r_k)^2`,            (4.2)

`M_JKK = sum_(i in J, j<k in K) det(r_i,r_j,r_k)^2`.            (4.3)

### Theorem `QFORM-TWOBANK-MIXED-PLUCKER-RESOLUTION-v1`

The two orientations have the exact formulas

`boxed:
M_JJK
 = det(G_J)[delta_K^2+d^T G_K d]
   +delta_J^2 tr(adj(G_J)G_K),`                                  (4.4)

`boxed:
M_JKK
 = det(G_K)[delta_J^2+d^T G_J d]
   +delta_K^2 tr(adj(G_K)G_J).`                                  (4.5)

Consequently

`M_JJK+M_JKK
 =d^T G_JG_K d
  +delta_J^2(1-det G_J)
  +delta_K^2(1-det G_K).`                                       (4.6)

### Proof

Cauchy--Binet gives a convenient generating polynomial. Since

`S_J+tS_K = R_J^T R_J + (sqrt(t)R_K)^T(sqrt(t)R_K)`,

where `R_B` is the row matrix of the bank, every triple containing exactly `m` rows from `K` receives the factor `t^m`. Hence

`det(S_J+tS_K)
 =det S_J + t M_JJK + t^2 M_JKK + t^3 det S_K`.                 (4.7)

Now make the determinant-one shear of the three spectral coefficient rows which replaces the longitudinal coordinate `alpha` by `alpha-q_J^T z`. On bank `J`, (2.2) becomes just `eta_J`; hence

`S_J -> diag(delta_J^2,G_J)`.                                   (4.8)

On bank `K`, the new longitudinal row is

`alpha_K-Z_K^T q_J
 =eta_K+Z_K^T(q_K-q_J)
 =eta_K-Z_K^T d`,                                                (4.9)

so its Gram becomes

`S_K -> [[delta_K^2+d^T G_K d, -d^T G_K],
          [-G_K d, G_K]]`.                                      (4.10)

The coefficient of `t` in (4.7) is `tr(adj(S_J)S_K)`. Because (4.8) is block diagonal,

`adj(S_J)=diag(det G_J, delta_J^2 adj(G_J))`,                    (4.11)

and (4.4) follows. Interchanging `J,K` gives (4.5).

To obtain (4.6), either add (4.4)-(4.5) and diagonalize the commuting pair `G_K=I-G_J`, or subtract the pure-bank masses `det S_B=delta_B^2 detG_B` from

`det(S_J+S_K)=det diag(epsilon,I_2)=epsilon`                     (4.12)

and then use (2.5). QED.

## 5. Partner r3 applied: BOTH mixed orientations carry universal normalized volume

This is the required designated-partner-to-actual-inequality application.

Because `G_K=I-G_J`, the matrices commute. Let the eigenvalues of `G_J` be `x_1,x_2 in [1/4,3/4]`. In their common eigenbasis, for coordinate `k`,

`det(G_J)(G_K)_(kk)
 =x_1x_2(1-x_k)
 =x_(3-k)[x_k(1-x_k)]
 >=(1/4)[G_JG_K]_(kk)`.                                         (5.1)

Thus, as a matrix inequality,

`det(G_J)G_K >=(1/4)G_JG_K`.                                    (5.2)

Similarly

`det(G_K)G_J >=(1/4)G_JG_K`.                                    (5.3)

All other terms in (4.4)-(4.5) are nonnegative. Insert the **completed account04/B16 r3 slope inequality** (2.7):

`M_JJK >= det(G_J)d^T G_Kd
         >=(1/4)d^T G_JG_Kd
         >epsilon/8`,                                            (5.4)

and likewise

`boxed: M_JKK>epsilon/8.`                                        (5.5)

Normalize the longitudinal coordinate by `sqrt(epsilon)`. Every three-by-three determinant is linear in that row, hence every squared three-volume is divided by `epsilon`. Therefore the normalized mixed masses satisfy

`boxed: Mtilde_JJK>1/8,  Mtilde_JKK>1/8.`                        (5.6)

There is a stronger total statement. By (3.2), the normalized pure-bank masses are

`Ptilde_J=(delta_J^2/epsilon)det G_J`,
`Ptilde_K=(delta_K^2/epsilon)det G_K`.                            (5.7)

Since `det G_B<=9/16` and the partner slope branch has (2.6),

`Ptilde_J+Ptilde_K<9/32`.                                       (5.8)

The global normalized leaf frame has Gram `I_3`, so its total squared three-volume is one. Hence

`boxed: Mtilde_JJK+Mtilde_JKK>23/32.`                            (5.9)

Thus more than `71.875%` of the normalized rank-three volume is forced to be genuinely **mixed-bank** in the slope-dominant collar, and each mixed orientation alone carries more than `1/8`.

This is the precise geometric resource that the previous per-bank 3D punctured theorem does not see.

## 6. Sharp innovation-free model: every pure-bank 3-volume is zero while both mixed orientations equal 1/2

For any `0<epsilon<1`, take five spectral-frame rows

`r_0=(sqrt(1-epsilon),0,0)`,

`r_1=( sqrt(epsilon/2), 1/sqrt(2), 0)`,
`r_2=( 0,               0,         1/sqrt(2))`,

`r_3=(-sqrt(epsilon/2), 1/sqrt(2), 0)`,
`r_4=( 0,               0,         1/sqrt(2))`.                 (6.1)

Let `J={1,2}`, `K={3,4}`. Directly,

`sum_(i=0)^4 r_i r_i^T=I_3`,                                    (6.2)

so this is a Parseval frame with near-coloop leverage `1-epsilon`.

Here

`G_J=G_K=(1/2)I_2`,
`q_J=(sqrt(epsilon),0)`,
`q_K=(-sqrt(epsilon),0)`,
`delta_J=delta_K=0`,
`d=(2sqrt(epsilon),0)`.                                         (6.3)

Therefore

`d^T G_JG_K d=epsilon`;                                         (6.4)

the partner's slope mechanism carries the entire defect. Equations (4.4)-(4.5) give exactly

`M_JJK=M_JKK=epsilon/2`.                                        (6.5)

After normalization by `sqrt(epsilon)`,

`Mtilde_JJK=Mtilde_JKK=1/2`,                                    (6.6)

while

`det T_J=det T_K=0`.                                            (6.7)

The global normalized leaf coefficient rows are explicitly

`(1/sqrt(2),0,-1/sqrt(2),0)`,
`(1/sqrt(2),0, 1/sqrt(2),0)`,
`(0,1/sqrt(2),0,1/sqrt(2))`,                                    (6.8)

which are orthonormal. Hence the actual three-dimensional bounded-density projection theorem gives the **global** normalized leaf projection a joint density cap `2^(3/2)`, even though each individual bank's three-row projection is rank two.

This does not by itself bound an indefinite quadratic pushforward; the current corrections explicitly forbid that inference. It identifies exactly where a future nonlinear projection-product theorem must spend the curvature: across the two independent banks, not inside either bank separately.

## 7. The previous authentic hub-first trace obstruction has a uniformly bounded TRUE density

The preceding same-slot run constructed the authentic target family

`Q_a=aY^2+4YU+V^2`,                                               (7.1)

with

`Y=sqrt(c)X_0+S`, `c=127/128`,                                  (7.2)

where `X_0,S,U,V` are generated by four disjoint original-source blocks, all physical source densities are at most one, and the matrix has three eigenvalues of modulus at least one throughout the punctured collar. That run proved that the positive hub-first root majorant

`E(4U^2-aV^2)_+^(-1/2)`                                        (7.3)

diverges at least logarithmically as `a downarrow0`.

The true density does **not** share this divergence. This run can pay the same family uniformly by changing the scalar variable rather than taking the positive hub-root trace.

Order the variables as `(U,Y,V)`. The coefficient matrix is

`B_a=[[0,2,0],[2,a,0],[0,0,1]]`,
`det B_a=-4`,                                                     (7.4)

so its first diagonal is exactly zero for every `a`.

The one-dimensional projection theorem gives

`||p_U||_infinity<=sqrt(2)`,
`||p_V||_infinity<=sqrt(2)`.                                    (7.5)

Because `sqrt(c)X_0` has density cap `1/sqrt(c)` and convolution cannot increase an `L^infinity` cap,

`||p_Y||_infinity<=1/sqrt(c)`.                                  (7.6)

Moreover `U` is independent of `(Y,V)`, and `Y,V` are independent, so

`||p_(Y,V)||_infinity<=sqrt(2/c)`.                              (7.7)

Apply the completed `QFORM-ZERO-PIVOT-CONDITIONAL-TRACE-v1` theorem with scalar conditional cap

`K=sqrt(2)`

and pair cap

`M=sqrt(2/c)`.

Using `|det B_a|=4`, uniformly in every real `a`,

`||p_(Q_a)||_infinity
 <=3*2^(2/3)(K M)^(2/3)4^(-1/3)`
` =3*2^(2/3)c^(-1/3)`
` =4.7746697131...`.                                             (7.8)

Thus

`boxed: ||p_(Q_a)||_infinity<4.775 for every a in the authentic family.}` (7.9)

This is a useful control on the mechanism discovered in the preceding run: the scalar-root positive trace can diverge while the actual output density remains uniformly bounded. The cancellation is not cosmetic; it is mathematically essential.

No continuity conclusion is imported from the zero-pivot theorem, so (7.9) is only an essential density bound.

## 8. What this run rules out, and the precise successor

The account04/B16 slope collar has now been converted into a strong dimension-free rank-three certificate, but it is a **mixed-bank** certificate:

- both mixed orientations have normalized Pluecker mass `>1/8`;
- the total mixed normalized mass is `>23/32`;
- the normalized slope cancels completely from each individual bank's 3D determinant;
- at the exact innovation-free endpoint both per-bank 3D determinants can be zero while the global normalized three-volume is exactly one.

Therefore the fresh phase-weighted theorem `QFORM-HUBPHASE-PUNCTURED-TWOBANK-v1`, when invoked through separate finite 3D density caps for both banks, cannot close this slope endpoint by merely renaming the order-one normalized slope as a third bank coordinate. The missing third dimension is created by **transversality between the two bank planes**.

The next B16 implication is consequently

**`QFORM-MIXED-VOLUME-OVERLAP-TTSTAR-v1` (OPEN):**

> Build a two-bank Fourier/TT* receiver whose quantitative input is the mixed volume pair `(Mtilde_JJK,Mtilde_JKK)` rather than separate three-dimensional bank density caps. It must remain finite when `delta_J=delta_K=0`, use the bank independence before absolute values, and couple the nonzero hub phase to the same common frequency. The structural packet available to it is `Mtilde_JJK,Mtilde_JKK>1/8` and total mixed mass `>23/32` in the partner slope collar.

This successor is genuinely different from the mechanisms already ruled out: it does not freeze a physical `P` slice and use Minkowski, does not perturbatively compare the punctured characteristic function to the zero-coupling form, does not take the hub scalar roots and then a positive indefinite half-potential, and does not demand a 3D density from either rank-two bank separately.

Arbitrary additional spectrum remains a separate full-target interface after the exact-rank-three endpoint. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED; global continuity remains OPEN.
