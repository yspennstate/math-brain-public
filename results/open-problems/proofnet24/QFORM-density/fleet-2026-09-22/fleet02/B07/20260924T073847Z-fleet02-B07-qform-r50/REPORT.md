SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B07, 2026-09-24T07:38:47Z.
attacking: fleet03/B07 r49 pair-block normal form — close the bounded-support block-diagonal-plus-rank24 spectral subproblem without selecting a minor, then sharpen the unpaid matched-bank receiver.

# fleet02/B07 r50 — pair-block rank cancellation, H62/rank4 compression, and a sharp target-valid regression

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW PAIR-BLOCK LOW-RANK-CANCELLATION CORE / NEW H62+RANK4 OPERATOR-TAIL COMPILER / SHARP TARGET-VALID 26-DIRECTION REGRESSION / PINNED e5 THEOREM F APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN.**

No moment, support, log-concavity, iid, diagonal-basis, post-rotation independence, arbitrary-joint coarea, pointwise quadratic-phase decay, deletion of a nonzero coefficient tail, or universally good single coordinate minor is used. All SVD/singular-subspace operations below are deterministic coefficient algebra only. Conditioning, when used, is only on original coordinates.

## 0. First unpaid implication

The sharpened debt is

`QFORM-R49-H62-R4-OPTAIL-RECEIVER-v1`.

On the fleet03/B07 r49 survivor after its physical-E3 payment and in its moderate same-bank-star-energy branch, either a bounded original-coordinate principal block already gives a universal essential-density bound, or there is a literal physical set `H subset S`, `|H|<=62`, such that for `L=S\H`,

`boxed: dist_op(A[L,L], {symmetric matrices of rank <=4})`
`       < 0.001631502080283948.`                                  (0.1)

A valid receiver for (0.1) must retain the live r49 global `T|S` crossing with its true nonzero `2^-16` Frobenius tail, arbitrary `A[T,T]`, all couplings involving `H`, all outside couplings, and every additional spectral direction. The separate r49 branch

`sum_{K good} ||A[K,S\K]||_F^2 > 1`                              (0.2)

remains an explicit alternative. In particular, neither (0.1) nor the bounded-core payment below licenses replacing the whole matrix by one selected minor or by an exact rotated low-rank random model.

## 1. Fresh source state and incoming r49 branch

Fresh owner control and the live correction inbox were reread immediately before this report. Owner control remains revision `2026-09-22.15`, the sole target remains the unrestricted three-large-eigenvalue QFORM conjecture, fleet02/B07 remains `Coordinate minor selection`, and there is no later stop or reassignment for this slot. The unrestricted theorem and full-target continuity remain OPEN.

The latest compatible completed fleet03/B07 source is r49, `20260924T064126Z-fleet03-B07-qform-r49`. Its input is a literal physical cut `T|S`, with `S` partitioned into disjoint physical pairs, and

`M=A[T,S]`,                                                       (1.1)

`dist_F(M,rank<=2)<eps`, `eps=2^-16`,                            (1.2)

`s2(M)>d_*=0.10429071727552326290...`,                            (1.3)

`s1(M)s2(M)>p_*=1.19876993884320...`.                             (1.4)

All but at most two matched pairs are determinant-stable under pair deletion, and all but at most three have top-two right-plane leverage at most `1/2`, so there are at most five non-good pairs. For each good pair r49 constructs a determinant-transfer packet and a random cut. If the resulting crossing has

`e3(CC^T)>=tau`, `tau=2^-30`,                                    (1.5)

then the completed marginal-free physical-E3 theorem pays the full ambient law continuously by

`||p_Q||_infinity <= 337.605402598...`.                           (1.6)

If (1.5) does not pay and the same-bank star energy is at most one, r49 proves the exact original-coordinate normal form

`boxed: A[S,S] = B_pair + R_24 + E_S,`                            (1.7)

where

* `B_pair` is block diagonal on the good literal physical `2x2` matched pairs;
* `rank R_24<=24`;
* `||E_S||_F < D0`, with

`D0=5.438340267613160e-4`;                                       (1.8)

* more precisely, `R_24=R_4+R_exc`, where `rank R_4<=4`, while `R_exc` is supported on the rows/columns of at most ten exceptional physical coordinates and has rank at most twenty.

The r49 report already paid 27 pair blocks carrying large **diagonal** pivots by a diagonal-plus-rank24 theorem. The point of the next section is to remove the diagonal restriction completely: arbitrary symmetric `2x2` pair blocks are enough, and their singular directions—not coordinate pivots—are the right currency.

## 2. Pair-block low-rank-cancellation theorem

### Theorem 2.1 — `QFORM-PAIRBLOCK-RANK-CANCELLATION-CORE-v1`

Let `C` be a union of disjoint literal original-coordinate pairs. Suppose

`A[C,C]=B+R+E`,                                                   (2.1)

where

* `B=direct_sum_K B_K` is symmetric and block diagonal on those physical `2x2` pairs;
* `rank R<=r`, with no norm or sign restriction on `R`;
* `E=E^T` and `||E||_op<=eta`.

For `d>0` define the block singular-direction count

`nu_d(B):=sum_K #{j in {1,2}: s_j(B_K)>=d}`.                     (2.2)

If

`nu_d(B)>=r+3`,                                                   (2.3)

then there is a union `C0` of at most `r+3` of the original physical pair blocks, hence

`|C0|<=2(r+3)`,                                                   (2.4)

such that

`boxed: s3(A[C0,C0]) >= d-eta.`                                  (2.5)

Consequently, if `d>eta`, the completed physical-fiber receiver gives the full ambient essential-density bound

`boxed: ||p_{X^TAX}||_infinity`
`       <= 2 sqrt(6 pi |C0|)/(d-eta)`
`       <= 2 sqrt(12 pi (r+3))/(d-eta).`                          (2.6)

All variables outside `C0`, all outside quadratic curvature, and every conditioning-generated affine term are retained by that receiver.

### Proof

Choose a minimal collection of physical pair blocks for which the cumulative count in (2.2) is at least `r+3`, and call their union `C0`. Every chosen block contributes at least one counted singular direction, so at most `r+3` blocks are selected; this proves (2.4).

Let `U` be the direct sum, inside `R^{C0}`, of all singular/eigenvector directions of the symmetric block diagonal matrix `B0=B[C0,C0]` whose singular values are at least `d`. Then

`dim U>=r+3`,                                                     (2.7)

and, because `B0` is block diagonal and `U` is its spectral singular subspace,

`||B0 x||_2 >= d ||x||_2` for every `x in U`.                    (2.8)

Put `R0=R[C0,C0]`. Since `rank R0<=r`,

`dim ker R0 >= |C0|-r`.                                          (2.9)

The elementary dimension inequality now gives

`dim(U intersect ker R0)`
` >= dim U + dim ker R0 - |C0|`
` >= (r+3)+(|C0|-r)-|C0|=3`.                                    (2.10)

For `x in U intersect ker R0`,

`(B0+R0)x=B0x`,                                                   (2.11)

so (2.8) gives a three-dimensional subspace on which `B0+R0` is bounded below by `d`. The max-min characterization of singular values therefore yields

`s3(B0+R0)>=d`.                                                   (2.12)

Finally `||E[C0,C0]||_op<=eta`, hence singular-value perturbation gives (2.5). Equation (2.6) is the completed physical-fiber theorem applied after conditioning only outside the literal original-coordinate set `C0`. QED.

### Why this is the relevant bounded-dimensional closure

The theorem spends aggregate pair-block singular directions before any reciprocal localization. A rank-`r` cancellation can erase at most `r` independent directions; `r+3` surviving directions force a true three-dimensional lower singular space on one bounded physical union. No claim is made that one good `2x2`, `3x3`, or other individual coordinate minor must exist.

At the natural r49 scale `d=1/64`, Theorem 2.1 with `r=24`, `eta=D0` gives

`s3(A[C0,C0]) > 1/64-D0`
`=0.015081165973238684...`,                                      (2.13)

on at most 54 physical coordinates and therefore

`||p_Q||_infinity < 4230.996`.                                   (2.14)

For structural compression it is better to lower the cutoff to `d=2D0`; the price is a larger but still universal paid constant, while the unpaid operator tail becomes two orders of magnitude smaller.

## 3. r49 specialization: pair blocks collapse to H62 plus rank four

Take

`d=2D0=0.001087668053522632`.                                    (3.1)

If

`nu_d(B_pair)>=27`,                                               (3.2)

Theorem 2.1 with `r=24` produces an actual principal block on at most 54 original coordinates satisfying

`s3>=d-D0=D0`,                                                    (3.3)

so the full ambient law obeys

`boxed: ||p_Q||_infinity <117330.53743.`                          (3.4)

Continuity is not asserted by this physical-core gate.

Suppose instead that (3.2) fails. Then

`nu_d(B_pair)<=26`.                                               (3.5)

Any good physical pair block with operator norm at least `d` contributes at least one singular value to `nu_d`, so there are at most 26 such blocks. Let `H_good` be the union of all of them. Then

`|H_good|<=52`.                                                   (3.6)

Let `H_exc` be the at most ten exceptional physical coordinates supporting `R_exc`, and put

`H=H_good union H_exc`, `L=S\H`.                                 (3.7)

Thus

`boxed: |H|<=62.`                                                 (3.8)

On `L`, every surviving pair block has operator norm `<d`, so because the blocks are disjoint,

`||B_pair[L,L]||_op<d`.                                          (3.9)

Also `R_exc[L,L]=0`, while `rank R_4[L,L]<=4`; finally

`||E_S[L,L]||_op<=||E_S||_F<D0`.                                 (3.10)

Hence

`A[L,L]=R_4[L,L] + (B_pair[L,L]+E_S[L,L])`,                      (3.11)

and therefore

`boxed: dist_op(A[L,L],rank<=4)`
`       < d+D0=3D0`
`       =0.001631502080283948.`                                  (3.12)

This is `QFORM-R49-H62-R4-OPTAIL-COMPILER-v1`. It is a deterministic physical-coordinate statement. It does not rotate the product law, discard the r49 `T|S` crossing, or promote the small operator tail to a probabilistically harmless quadratic error. Those are exactly the restrictions encoded in the unpaid implication (0.1).

## 4. The threshold `r+3=27` is sharp under only rank-24 cancellation

The preceding theorem cannot replace `27` by `26`. More importantly, the failure can occur inside the exact owner target and inside the displayed r49 separator/stability regime.

### Construction — `QFORM-R49-26-DIRECTIONS-SHARP-TARGET-REGRESSION`

Fix even `N>=8`. Take two physical coordinate banks `T` and `S0`, each of size `N`, and another bank `P` consisting of 26 disjoint physical pairs

`K_j={a_j,b_j}`, `j=1,...,26`.                                   (4.1)

Let `sigma_i in {+1,-1}` be balanced. Define flat orthonormal `N x 2` frames `U,V` by rows

`U_i=(1,sigma_i)/sqrt(N)`,
`V_i=(1,sigma_i)/sqrt(N)`,                                       (4.2)

with the signs on `S0` paired so that each matched `S0` pair contains one `+` row and one `-` row. Put

`c=sqrt(2)`,
`M=c U V^T`,                                                      (4.3)

and extend `M` by zero columns on `P`. Thus `M:T -> S0 union P` has exactly two singular values, both equal to `c`.

Choose any `d>0` (in particular `d=2D0`) and define the pair-block bookkeeping matrix on `S=S0 union P` by

`B_pair[K_j,K_j]=diag(d,0)` for `j=1,...,26`,                    (4.4)

with zero blocks on the matched `S0` pairs. Define

`R_24=-d sum_{j=1}^{24} e_{a_j}e_{a_j}^T`,                       (4.5)

and `E_S=0`. Then

`rank R_24=24`,                                                   (4.6)

while

`nu_d(B_pair)=26`.                                                (4.7)

The actual same-side matrix is

`A[S,S]=B_pair+R_24`,                                             (4.8)

so the first 24 block directions are cancelled exactly and only the two diagonal entries at `a_25,a_26` remain. Let `A[T,T]=0` and set the cross blocks to `M,M^T`.

### r49 displayed inequalities hold

Because `M` is exact rank two,

`dist_F(M,rank<=2)=0<2^-16`.                                     (4.9)

Moreover

`s2(M)=sqrt(2)>d_*`,
`s1(M)s2(M)=2>p_*`.                                               (4.10)

Deleting any `P` pair does not change `M`, so its stability volume is

`Z_K=e2(MM^T)=c^4=4`.                                             (4.11)

For a matched `S0` pair, the two opposite-sign rows in (4.2) contribute `(2/N)I_2` to `V^T V`, hence after pair deletion

`V_{-K}^T V_{-K}=(1-2/N)I_2`,                                   (4.12)

and therefore

`Z_K=4(1-2/N)^2>z0` for `N>=8`.                                  (4.13)

Each `S0` pair has top-two right-plane leverage exactly `4/N<=1/2`, and each `P` pair has leverage zero, so every pair is good in the displayed r49 sense. Finally there are no off-pair `SxS` entries at all. Hence for every matched pair

`R_K=A[K,S\K]=0`,                                                 (4.14)

so the r49 same-bank star energy is exactly zero and all pair-transfer residuals vanish. The normal form is exact here.

### Exact target spectrum

The bipartite block

`[[0,M],[M^T,0]]`                                                 (4.15)

has nonzero eigenvalues

`+c,+c,-c,-c`.                                                    (4.16)

The two uncancelled coordinates contribute two additional eigenvalues `d,d`. Consequently the full matrix has at least four eigenvalues of modulus `sqrt(2)>1`; it lies in the exact owner target for every `N`.

### No bounded-cardinality three-eigenvalue physical core

Fix a cardinality `L0` independent of `N`, and let `C` be any literal physical principal set with `|C|<=L0`. The actual diagonal part of `A[C,C]` has rank at most two, since only `a_25,a_26` survive the cancellation. Every entry of `M` has magnitude at most `2c/N`. If `p=|C intersect T|` and `q=|C intersect S0|`, then

`||M[C intersect T,C intersect S0]||_op`
` <= ||.||_F <= (2c/N)sqrt(pq)`
` <= c L0/N`.                                                     (4.17)

The symmetric crossing in the principal block has the same operator norm. A rank-two matrix plus a perturbation of norm at most `cL0/N` has third singular value at most that perturbation norm. Therefore

`boxed: sup_{|C|<=L0} s3(A[C,C]) <= c L0/N ->0.`                 (4.18)

Thus even the exact target, exact rank-two crossing, all displayed r49 stability inequalities, zero same-bank star residual, and 26 physical pair singular directions do **not** force a uniformly spectral bounded physical core. The count `r+3=27` in Theorem 2.1 is sharp under only a rank-24 cancellation hypothesis. This family is an intermediate-mechanism obstruction, not a QFORM counterexample.

## 5. Mandatory pinned `e5f71d79...` result applied to the obstruction

The pinned source proves the general-rank Fresnel–Brascamp–Lieb theorem: if

`A=D+sum_{k=1}^r lambda_k v_k v_k^T`,                             (5.1)

where `D` is any diagonal matrix, the `v_k` are orthonormal, and every original coordinate has leverage at most `1/2` in their span, then for `r>=3`

`||p_Q||_infinity <= (4r/(r-2))`
`                     (prod_k |lambda_k|)^(-1/r)`.               (5.2)

It retains arbitrary diagonal twists and linear terms and uses the original product coordinates; no post-rotation independence is assumed.

Apply (5.2) to the exact family of Section 4. Put the two residual `d` entries into `D`. The remaining rank-four bipartite term has eigenvalues

`lambda=(c,c,-c,-c)`,                                            (5.3)

so

`prod |lambda_k|=c^4=4`.                                         (5.4)

Its rank-four spectral subspace has physical coordinate leverage `2/N` on every coordinate of `T` and `S0`, and zero on `P`; for `N>=8` this is at most `1/2`. Therefore pinned Theorem F gives a continuous density satisfying

`boxed: ||p_Q||_infinity <= 8 * 4^(-1/4)`
`       = 4 sqrt(2)`
`       = 5.65685424949... .`                                    (5.5)

This is a direct completed-source payment on the new target-valid obstruction. It also identifies why (4.18) is not dangerous for the conjecture: diffuse product-law Fresnel smoothing can pay a family for which every fixed coordinate core degenerates. A structural proof must preserve that diffuse mechanism rather than insist on a hidden good minor.

## 6. What is now closed and what remains

The actual bounded-dimensional spectral subproblem for r49's pair-block normal form is closed at the correct level: `r+3` pair-block singular directions defeat arbitrary rank-`r` cancellation on a bounded physical union, with no need to find one good minor. For the concrete r49 constants, either the full ambient law is paid by a core on at most 54 original coordinates, or after deleting at most 62 original coordinates the matched-bank principal block is within `1.632e-3` in operator norm of rank four.

The exact next debt is not “find a better coordinate minor.” It is the robust analytic/structural receiver (0.1), with all of the following retained simultaneously:

1. the near-rank-two physical crossing `M=A[T,S]`, including its nonzero `2^-16` tail and robust second singular direction/product;
2. the rank-four carrier and its `0.001632` same-bank operator tail on `S\H`;
3. the at most 62 exceptional physical coordinates and all of their couplings;
4. arbitrary `A[T,T]`, outside couplings, and extra spectrum;
5. the separate `E_star>1` same-bank-star-energy branch.

The Section 4 regression is mandatory for any proposed closure: a method that tries to convert the state into one bounded principal core fails even in an exact target family, while the pinned product-law Fresnel theorem succeeds immediately.

Full unrestricted QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**. Continuity is available on the r49 physical-E3 payment and on the pinned Theorem-F regression (5.5), but is not claimed for the physical-core gate (2.6).
