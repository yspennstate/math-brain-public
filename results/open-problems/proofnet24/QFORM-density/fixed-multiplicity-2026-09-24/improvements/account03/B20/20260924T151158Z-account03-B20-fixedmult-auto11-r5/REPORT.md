SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-24T15:11:58Z.

attacking: multiplicity-eight robust-pair endpoint — close every state with at most one high-leverage complement coordinate, leaving only a two-high finite physical core.

# account03/B20 r5 — release gate and one-high-leverage closure at multiplicity eight

Run: `20260924T151158Z-account03-B20-fixedmult-auto11-r5`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 0. Release-gate state

The pinned seventeen-direction manuscript remains mathematically PASS in this B20 review. The singular-Schur regularization paragraph is sound: if `m=N_A(t)-k`, the regularized Schur complements obey `s_m(S_eps)>=t-|eps|`, and operator-norm continuity yields `s_m(S)>=t`; there is no invalid moving-threshold passage. The zero-weight Brascamp--Lieb wording remains editorial only.

The lowest release-grade fixed multiplicity currently backed by two separate complete reconstructions remains **9**. B20 retains the common safe independently reconstructed bound

`||p_Q||_infinity < 5338 K^2/s`

under `s_9(A)>=s>0`. Global continuity is not part of this release certificate; the theorem is an essential-density statement. The multiplicity-eight theorem remains open.

Source pins used for the present improvement:

- account01/B09 robust-pair low-leverage closure: `61ecd9c1e33bb2895ec1d184c77b9f1e76064449`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account01/B09/20260924T144758Z-account01-B09-FIXMULT-auto11-r12/LOW_LEVERAGE_ROBUST_PAIR.md`;
- account01/B19 incident-volume reduction/receiver: `d44d368cd18a2590fc62d0aadd2cf2b7e9d0e83f`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account01/B19/20260924T144921Z-account01-B19-fixed-mult-audit-r11/S8_INCIDENT_VOLUME_REDUCTION.md`;
- account02/B17 robust-pair-only shortcut counterexample: `85fa658e5ef8c1227cfbac3a05145bde9e3db5e0`.

All mathematics below is in literal original coordinates. Orthogonal projections are deterministic row-space devices only; no independence after rotation is used.

## 1. Setup: the current robust-pair `s_8` collar

Work in the normalized no-pivot chamber with

`eta=1/100`, `s_8(A)>=1`.

The current robust-anchor reduction supplies a literal two-coordinate set `H`, complement `L=H^c`, and block form

`A=[[B,C],[C^T,D]]`

with

`g:=det(CC^T)>=d0:=0.3649442658827020...`.

Let

`Q_C=C^T(CC^T)^(-1)C`, `P=I_L-Q_C`,

and write

`q_i=(Q_C)_{ii}`, `p_i=P_{ii}=1-q_i`.

Because `Q_C` is a rank-two orthogonal projection,

`sum_{i in L} q_i=2`.

Define the high-leverage set

`J={i in L: q_i>2/3}`

and `U=L\J`. Then necessarily

`h:=|J|<=2`,

and `p_i>=1/3` for every `i in U`.

The B09 theorem already closes the case `h=0`. The point of this note is to close `h=1` as well without any new probabilistic assumption.

## 2. Anchored disjoint third-minor identity

For `i in L`, let `d_i` be row `i` of `D` and set

`r_i=d_iP`.

For each `i`, define the product-usable anchored third-minor energy

`W_i=sum_{T subset L\{i}, |T|=3} det A[H union {i},T]^2`.

The exact B09 Gram/Cauchy--Binet identity is

`W_i=g(p_i ||r_i||_2^2-r_{ii}^2)`.                                      (2.1)

Let

`W_dis=sum_{i in L} W_i`.

This is exactly the incident three-volume in which the distinguished row coordinate does not also appear among the three column coordinates.

For each low-leverage `i in U`, define

`lambda_i=r_{ii}/p_i`

and

`e_i^T E=(d_i-lambda_i e_i^T)P`.

For high-leverage `i in J`, set `lambda_i=0` and `e_i^T E=0`.

Then `E_ii=0` for every `i`, and for `i in U`,

`||e_i^T E||_2^2=||r_i-(r_{ii}/p_i)e_i^TP||_2^2
                 =||r_i||_2^2-r_{ii}^2/p_i
                 =W_i/(g p_i)`.

Since `p_i>=1/3` on `U`,

`||E||_F^2
 =sum_{i in U} W_i/(g p_i)
 <=(3/g) sum_{i in U}W_i
 <=3 W_dis/g`.                                                        (2.2)

## 3. New theorem: at most one high leverage forces macroscopic disjoint volume

### Theorem `QFORM-S8-ROBUSTPAIR-ONEHIGH-CLOSURE-v1`

Under the setup above, if `h=|J|<=1`, then

`W_dis>g/48`.                                                         (3.1)

Consequently the full quadratic polynomial with arbitrary affine terms and arbitrary independent cap-one coordinate laws has a bounded continuous density satisfying

`||p_Q||_infinity
 < C_inc (g/48)^(-1/6)
 <= C_inc (d0/48)^(-1/6)
 =23.478932894359914... <23.48`,                                    (3.2)

where

`C_inc=3*2^(5/6)*e^(2/3)=10.411402562723481...`.

#### Proof

Assume for contradiction that

`W_dis<=g/48`.

By (2.2),

`||E||_F<=1/4`.                                                       (3.3)

Extend `lambda` by zero on `H` and put

`D0=0_H directsum diag(lambda)`

and

`R=A-D0-(0_H directsum E)`.

For a low row `i in U`, the `L`-part of the row of `R` is

`d_i-lambda_i e_i^T-(d_i-lambda_i e_i^T)P
 =(d_i-lambda_i e_i^T)Q_C`,

which lies in the two-dimensional row space of `C`. Its `H`-part lies in the two physical coordinates `H`. The anchor rows have the same four-dimensional support description. Each exceptional high row in `J` can add at most one further row direction. Therefore

`rank R<=4+h<=5`.                                                     (3.4)

More importantly, after restricting both rows and columns to `U`, every row belongs to the restriction of `row(C)`, so

`rank R[U,U]<=2`.                                                     (3.5)

From `s_8(A)>=1` and (3.3),

`s_8(D0+R)=s_8(A-(0_H directsum E))>=3/4`.                           (3.6)

Since `rank R<=4+h`, the rank-perturbation inequality gives

`s_{4-h}(D0)>=3/4`.                                                   (3.7)

When `h<=1`, (3.7) implies that at least three low coordinates `I subset U` satisfy

`|lambda_i|>=3/4`.

The no-pivot chamber gives

`|A_ii|<eta=1/100`

and for `i!=j`,

`|A_ij|<a0:=sqrt(eta^2+eta)=0.1004987562112089...`.

Because `E_ii=0`, for `i in I`,

`|R_ii|=|A_ii-lambda_i|>=3/4-1/100=0.74`.                           (3.8)

For distinct `i,j in I`,

`|R_ij|<=|A_ij|+|E_ij|
        <a0+1/4
        =0.3504987562112089...`.                                    (3.9)

Hence the sum of the two off-diagonal absolute values in any row of the `3 x 3` matrix `R[I,I]` is strictly less than

`2(a0+1/4)=0.7009975124224178...<0.74`.                             (3.10)

Thus `R[I,I]` is strictly row-diagonally dominant and therefore invertible. It has rank three. This contradicts (3.5), because `I subset U` and `rank R[U,U]<=2`.

The contradiction proves (3.1).

Now invoke the completed account01/B19 disjoint incident-volume receiver, which is product-law safe and retains all self-curvature and affine terms:

`||p_Q||_infinity<=C_inc W_dis^(-1/6)`.

Substituting (3.1) and `g>=d0` proves (3.2). The receiver has an integrable characteristic-function majorant, so this branch has a continuous `C_0` density. QED.

## 4. Exact remaining robust-pair geometry: two high coordinates

The preceding theorem plus `sum q_i=2` leaves only

`|J|=2`.

Write `J={i,j}`. The exact two-dimensional determinantal weights

`w_ab=det(C_{\{a,b\}})^2/g`, `a<b`,

satisfy

`sum_{a<b}w_ab=1`,

and the determinantal inclusion identity gives

`q_i=sum_{b!=i}w_{ib}`.

Therefore, because both `q_i,q_j>2/3`,

`w_ij>=q_i+q_j-1>1/3`.

Equivalently,

`det(C_{\{i,j\}})^2>g/3>=d0/3
 =0.12164808862756733...`.                                          (4.1)

Thus the entire unpaid robust-pair endpoint has been localized to a literal four-coordinate core: the original physical anchor pair `H` plus exactly two complement coordinates `i,j`, with a quantitatively nondegenerate `2 x 2` anchor-to-core cross minor.

This is stronger than the previous statement “there are at most two high coordinates”: **one-high is now paid**, so two-high is necessary for nonpayment.

## 5. Why this does not yet prove multiplicity eight

The account02/B17 rank-two construction shows that robust order-two crossing data alone, even with no physical pivot and `CC^T=I_2`, can coexist with a logarithmically unbounded output density when the ambient Schur/spectral currency is discarded. Therefore (4.1) must not be promoted to a generic order-two density theorem.

The multiplicity-eight hypothesis supplies additional spectral information that this local counterexample lacks. The next exact implication is therefore

`QFORM-S8-TWOHIGH-FOURCOORD-CORE-SCHUR-ENDPOINT-v1`:

> Starting from the four-coordinate physical core in (4.1) and the remaining spectral/Schur directions forced by `s_8(A)>=1`, prove a product-preserving `L^infinity` endpoint or force an already-paid disjoint third-volume receiver.

Promising routes are the six/four exterior directions already present in concurrent fixed-multiplicity work, but any proof must retain them quantitatively rather than replace the full state by the robust pair alone.

## 6. Threshold and regularity accounting

- pinned 17-direction manuscript: mathematical PASS in this B20 review; global result is essential boundedness, not a global continuity theorem;
- release-grade fixed multiplicity: `9`, with common safe two-review bound `<5338 K^2/s`;
- multiplicity 8: **OPEN**; this run closes all robust-pair states with zero or one leverage score above `2/3` and localizes the unpaid robust-pair survivor to exactly two such coordinates;
- unrestricted multiplicity 3 conjecture: **OPEN / not proved / not disproved**;
- continuity: proved on the new disjoint-third-volume branch through the B19 product-Fourier receiver; not claimed globally at multiplicity 9, 8, or 3.

## 7. Self-audit / dependency discipline

The new theorem uses only:

1. the source-valid no-pivot entry bound;
2. the B09 exact anchored-minor and determinantal inclusion identities;
3. rank perturbation for singular values of the possibly nonsymmetric `A-(0 directsum E)`;
4. strict diagonal dominance;
5. the B19 product-safe disjoint incident-volume receiver.

It introduces no Gaussianity, moments, compact support, log-concavity, connected support, diagonal basis, post-rotation independence, arbitrary-joint coarea bound, or law-uniform pointwise quadratic-phase decay.

This is a B20 self-audit of the new implication, not an independent peer review. Multiplicity eight is not promoted until a complete closed argument and the required separate reviews exist.
