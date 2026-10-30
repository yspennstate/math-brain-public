SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B20, 2026-09-22T21:01:11Z.
attacking: the newest designated-partner opposite-sign two-pivot survivor, with the goal of forcing and quantifying the third source-valid resource without rotating the product law.

# fleet02/B20 QFORM r19 — exact third-resource extraction after two physical Schur pivots

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `ESSENTIAL_STEP_APPLIED / THIRD-SPECTRAL-RESOURCE-QUANTIZED / FULL_TARGET_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Continuity:** not proved by this argument; the new paid branch concerns essential boundedness only.

## 1. Target and correction boundary

The parent target is unchanged: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with `s_3(A)>=1`, prove a dimension/law/matrix-independent bound on the essential supremum of the density of `Q=X^T A X`, or give a target-valid counterexample.

No Gaussianity, log-concavity, moments, compact/connected support, diagonal-basis hypothesis, or post-rotation independence is used. In particular, this report does not use law-uniform pointwise quadratic-phase decay, unrestricted fiber suprema, arbitrary-joint 3D coarea, or conditional-density caps after exposing a dependent statistic.

## 2. Fresh designated partner actually consumed

The newest completed compatible `fleet03/B20` result is run

`20260922T204947Z-fleet03-B20-QFORM-r17`, canonical mathematics

`yspennstate/math-open-problems@56f7a951d545e6639d4b89fbfa18b0a1158ffe44`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260922T204947Z-fleet03-B20-QFORM-r17/REPORT.md`.

On its validated low-leverage two-arm overlap it proves that every still-unpaid state has two successive **physical** scalar pivots of opposite sign. In the original-coordinate order `i,p,R`, put

`a=A_ii`,

`S=A_{-i,-i}-A_{-i,i}A_{i,-i}/a`,

`d=S_pp`,

and let `T` be the exact second Schur complement after pivoting `p` in `S`. The partner gives the exact inequalities

`a d<0`,

`|a| >= m :=3501/8000`,

`|d| >1/8`.                                                   (2.1)

Its first unpaid implication is to use the full target hypothesis `s_3(A)>=1` to force a third source-valid curvature/small-ball resource, or to pay the indefinite pair by a residual smoother.

I use (2.1) exactly below.

A second completed theorem from the same designated partner, run `20260922T184724Z-fleet03-B20-QFORM-r15`, is the physical-triple determinant payment:

> If `M=A[I,I]` is an ORIGINAL-coordinate principal `3x3` block, `a=M_ii!=0`, and `det M!=0`, then with arbitrary outside coordinates/couplings and affine terms,
>
> `||p_Q||_infinity <=128 (|a det M|)^(-1/4)`.                (2.2)

This is source-valid because its proof conditions only on outside original coordinates and uses a physical scalar square plus a translation-uniform rank-two half-Riesz estimate.

## 3. New structural lemma: spectral tail survives successive physical Schur elimination

### Lemma 3.1 — `QFORM-SCHUR-TAIL-SINGULAR-PRESERVATION-v1`

Let `A` be real symmetric. Perform `k` successive nonzero **scalar physical-coordinate Schur pivots**, obtaining the final Schur complement `T_k` on the untouched original coordinates. Then

`boxed: s_{k+1}(A) <= ||T_k||_op.`                            (3.1)

In particular, after the two partner pivots,

`boxed: ||T||_op >= s_3(A) >=1.`                             (3.2)

#### Proof

For one pivot, after merely permuting original coordinates so the pivot is first,

`A = a vv^T + diag(0,S)`,                                    (3.3)

where `v=(1,A_{i,-i}/a)^T` and `S` is the physical Schur complement. The first term has rank one.

Apply the same identity inside `S` at the second physical pivot:

`S = d ww^T + diag(0,T)`.                                    (3.4)

After extending `w` by a zero in the first pivot coordinate,

`A = R_2 + diag(0,0,T)`                                      (3.5)

with `rank(R_2)<=2`. Iterating gives

`A=R_k+E T_k E^T`, `rank(R_k)<=k`,                            (3.6)

where `E` is the coordinate embedding of the untouched original coordinates, hence `||E T_k E^T||_op=||T_k||_op`.

By the Eckart-Young characterization of singular values,

`s_{k+1}(A)=inf_{rank B<=k} ||A-B||_op <=||A-R_k||_op=||T_k||_op`.

This proves (3.1)-(3.2). No probabilistic transformation is involved. QED.

This is stronger than an inertia statement: it quantitatively retains the `(k+1)`-st singular value after arbitrary-size couplings to the eliminated physical pivots.

## 4. New theorem: either a paid physical triple or a strong residual cross bank

### Theorem 4.1 — `QFORM-TWO-PIVOT-THIRD-RESOURCE-DICHOTOMY-v1`

Assume the full target hypotheses and the designated-partner two-pivot state (2.1). Then exactly one of the following payments/resources is available (the alternatives need not be exclusive):

1. **Physical-third-diagonal branch.** There is an untouched original coordinate `j` with

   `|T_jj|>=1/2`.                                             (4.1)

   Then the full ambient quadratic form is already paid by

   `boxed: ||p_Q||_infinity <256/sqrt(m)<386.981.`            (4.2)

2. **Strong residual cross-bank branch.** There is a nontrivial partition of the untouched original coordinates `R=L disjoint_union K` such that

   `boxed: s_1(T[L,K])>1/4.`                                 (4.3)

   Moreover this is an aggregate ORIGINAL-matrix minor packet. If

   `Delta_jk := det A[{i,p,j},{i,p,k}]`                       (4.4)

   with the row/column orders shown, then

   `Delta[L,K]=a d T[L,K]`,                                  (4.5)

   hence

   `boxed: s_1(Delta[L,K]) > |a d|/4 > m/32
           =3501/256000.`                                    (4.6)

Thus the vague request to “use the third eigenvalue” is replaced by a fixed-scale, source-indexed dichotomy with no dimension loss.

#### Proof: diagonal branch and its density payment

By Lemma 3.1, `||T||_op>=1`. Let `D=diag(T)` and `H=T-D`.

If `||D||_op=max_j |T_jj|>=1/2`, choose such a physical coordinate `j`. Let

`M=A[{i,p,j},{i,p,j}]`.

Successive scalar Schur determinant factorization gives the exact identity

`det M = a d T_jj`.                                          (4.7)

Indeed pivoting `i` in this `3x3` block contributes the factor `a`, pivoting `p` in the resulting `2x2` block contributes `d`, and its remaining scalar is exactly `T_jj`.

Therefore, using (2.1) and (4.1),

`|a det M|=|a|^2 |d| |T_jj|
           > m^2 (1/8)(1/2)
           =m^2/16`.                                         (4.8)

Apply the designated-partner physical-triple theorem (2.2):

`||p_Q||_infinity
 <=128 (|a det M|)^(-1/4)
 <128 (m^2/16)^(-1/4)
 =256/sqrt(m)
 =386.9803414...<386.981`.                                   (4.9)

This closes the entire physical-third-diagonal alternative with arbitrary self blocks and outside couplings retained.

#### Proof: cross-bank branch

Suppose instead `||D||_op<1/2`. Since `T=D+H` and `||T||_op>=1`,

`||H||_op >= ||T||_op-||D||_op >1/2`.                        (4.10)

Choose a unit real eigenvector `z` of the symmetric zero-diagonal matrix `H` with

`|z^T H z|=||H||_op`.

Independently put every residual physical coordinate into `L` with probability `1/2` and into `K` otherwise. Let

`H_cross(L)=P_L H P_K+P_K H P_L`.

Because `H` has zero diagonal, each off-diagonal entry survives in `H_cross` with probability `1/2`, so

`E H_cross(L)=H/2`,

and hence

`E[z^T H_cross(L) z]=(1/2)z^T H z`.                          (4.11)

If `z^T H z>0`, some cut has `z^T H_cross z >= (1/2)z^T H z`; if it is negative, apply the same statement to the negative scalar. Thus for some cut,

`||H_cross(L)||_op >= |z^T H_cross(L)z|
                     >= ||H||_op/2
                     >1/4`.                                  (4.12)

In the decomposition `L union K`,

`H_cross(L)=[[0,H[L,K]],[H[K,L],0]]`,

whose operator norm is exactly `s_1(H[L,K])`. Since the diagonal matrix `D` has no cross entries,

`H[L,K]=T[L,K]`.

This proves (4.3). The cut is automatically nontrivial because the block is nonzero.

Finally, for every `j in L`, `k in K`, the bordered-minor Schur determinant formula with the invertible physical `2x2` pivot block `{i,p}` gives

`det A[{i,p,j},{i,p,k}]
 = det A[{i,p},{i,p}] * T_jk
 = (a d) T_jk`.                                               (4.13)

This proves the matrix identity (4.5). Multiplying singular values and using (2.1),(4.3) gives

`s_1(Delta[L,K])=|a d| s_1(T[L,K])
                 > (m/8)(1/4)=m/32`,

which is (4.6). QED.

## 5. What this pays in the conditional end-to-end route

The strongest current low-leverage two-arm route is now:

1. the prior synthesis produces the physical first pivot and balanced hub packet;
2. fleet03/B20 r17 plus the cross-dominated second-Schur theorem pays the cross-dominated hub row, obtains `|d|>1/8`, pays the same-sign pair, and leaves only the quantitative opposite-sign state (2.1);
3. Theorem 4.1 **fully pays** every such state whose second residual has a physical diagonal of magnitude at least `1/2`;
4. every remaining opposite-sign two-pivot state has an untouched-original-coordinate Schur cross cut with singular value `>1/4`, equivalently an aggregate `3x3` original-matrix cross-minor packet of singular value `>3501/256000`.

Therefore the designated partner's first unpaid “third source” request is no longer qualitative: the third spectral direction has been converted into either a closed physical-triple branch or a fixed-scale cross-bank packet.

The broader synthesis still has the separately tracked high-leverage augmented-bank and pivot-star/heavy-edge debts. Thus this is not a full proof.

## 6. First unpaid implication after this run

The first unpaid implication on the partner branch is now the concrete statement

### `QFORM-OPPOSITE-PAIR-STRONG-SCHUR-CROSS-PAYMENT-v1`

For independent original-coordinate inputs with densities at most one, suppose `A` has `s_3(A)>=1` and admits successive physical pivots `i,p` with

`a d<0`, `|a|>=3501/8000`, `|d|>1/8`,

and the exact second Schur complement `T` has an original-coordinate cut `L|K` satisfying

`s_1(T[L,K])>1/4`.

Prove a universal linear small-ball/density bound for the **full ambient form**, retaining arbitrary within-bank self curvature and all outside couplings; or source-preservingly reduce this packet to a currently paid physical-pair, physical-triple, ridge/grouped-square, or two-bank transverse-curvature theorem.

The exact obstruction is dependence created by completing the two pivots: although `L,K` remain disjoint original-coordinate banks, one may not treat the shifted pivot variables as independent of `(X_L,X_K)`, and one may not drop arbitrary same-bank curvature. The next mechanism should therefore use the original-coordinate minor identity (4.5) or aggregate-before-inversion, rather than conditioning on a rotated residual coordinate.

## 7. Status

Classification: `ESSENTIAL_STEP_APPLIED / THIRD-SPECTRAL-RESOURCE-QUANTIZED / FULL_TARGET_OPEN`.

Target-level change: the physical-third-diagonal subbranch of the partner's opposite-sign two-pivot survivor is closed with explicit constant `<386.981`.

Mechanism-level change: every remaining state has a fixed-scale source-indexed residual cross bank `s_1>1/4` and an equivalent aggregate original-matrix `3x3` cross-minor packet `s_1>3501/256000`.

Full QFORM is **OPEN / NOT PROVED / NOT DISPROVED**. No new continuity conclusion is claimed.
