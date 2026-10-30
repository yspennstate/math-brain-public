# fleet02/B04 early checkpoint — q=1 volume support and a double-hub stress matrix

Run: `fleet02-B04-20260923T094548Z-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: substantive partial result; full QFORM remains OPEN.

## First unpaid implication

The current hard branch should be sharpened from “soft-ridge double hub” to **support-deficient double hub**.  The reason is that a matrix may fail the partner soft-ridge gate in both orientations while the physical 3-minor support still has a perfectly balanced q=1 volume law.  The next structural theorem should therefore route only those double-hub survivors for which the nonzero 3-minor support itself cannot support a bounded-marginal fractional matching, or for which every such matching has prohibitive determinant/entropy cost.

## 1. Exact support criterion for q=1 third-volume reweighting

Let `M` be an original-coordinate cross block with rank at least 3.  Let `E` be its physical row set and let `mathcal B` be the bases of the rank-3 row matroid: triples `S subset E` for which some column triple `T` has `det M[S,T] != 0`.

A probability law on nonzero physical 3x3 minors induces a probability law `mu` on `mathcal B`; write `alpha_i=P_mu(i in S)`.

**Claim (QFORM-THIRDVOLUME-Q1-BASEPACKING-v1).** There exists a supported nonzero-minor law with every `alpha_i<=1/2` if and only if the row matroid contains two disjoint bases.

Proof.  If `B1,B2` are disjoint bases, choose for each `Bk` one column triple `Tk` with nonzero determinant and put weight 1/2 on `(Bk,Tk)`; then every row marginal is at most 1/2.

Conversely suppose such a law exists.  For every `A subset E`, each basis `B` obeys

`|B \ A| >= 3-r(A)`.

Averaging and using the marginal cap gives

`3-r(A) <= sum_{i in E\A} alpha_i <= |E\A|/2`,

hence

`|E\A| >= 2(3-r(A))` for every `A`.

By the matroid base-packing theorem (k=2), these inequalities are exactly the criterion for two disjoint bases.  QED.

Thus infeasibility of *every* q=1 admissible reweighting has a sharp support-level classification.  A violated base-packing inequality has `r(A)=2,1,0`, respectively forcing:

- `r(A)=2`: exactly one physical row lies outside a rank-2 flat, i.e. a genuine row coloop;
- `r(A)=1`: at most three physical rows lie outside a common rank-1 flat;
- `r(A)=0`: at most five nonzero physical rows.

This is only a support theorem: it does not yet control determinant magnitudes or the KL/entropy price of an admissible law.

## 2. Same-matrix stress family: double soft-ridge failure but globally optimal q=1 volume

Let

`S=(1/7)*[[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`.

Then `S^T S=I` and every entry of `S` is nonzero.  Define `U,V in R^{6x3}` by row pairs

`U_(2j-1)= e_j/sqrt(2),   U_(2j)= -e_j/sqrt(2)`,

`V_(2k-1)= s_k/sqrt(2),   V_(2k)= -s_k/sqrt(2)`,

where `s_k` is row k of S.  Then `U^T U=V^T V=I`.  Put

`D=diag(4,2,1)`,  `M=UDV^T`.

The singular values are exactly `(4,2,1)`.  In physical coordinates

`M = [[12/7,-12/7,-4/7,4/7,-6/7,6/7],
      [-12/7,12/7,4/7,-4/7,6/7,-6/7],
      [-2/7,2/7,3/7,-3/7,-6/7,6/7],
      [2/7,-2/7,-3/7,3/7,6/7,-6/7],
      [-3/14,3/14,-3/7,3/7,-1/7,1/7],
      [3/14,-3/14,3/7,-3/7,1/7,-1/7]]`,

so every one of the 36 cross coefficients is nonzero.

A nonzero physical 3x3 minor must choose exactly one row from each U-pair and one column from each V-pair.  There are `8*8=64` such minors and each has determinant magnitude exactly one:

`|det U_S|=|det V_T|=1/(2 sqrt(2))`, `det D=8`.

Hence

`E3(M)=64`.

The canonical squared-minor law is uniform on these 64 minors and every row/column marginal is exactly 1/2.  More strongly, because every supported minor has `det^2=1`, for every supported probability weight w,

`G(w)=exp(H(w)) <= 64`,

with equality only at the uniform law.  The sharp q-dependent coefficient

`C(q)=3e/[(3-2q)sqrt(q)]`

has derivative

`d log C/dq = 2/(3-2q)-1/(2q)>0` for `q>=1`.

Therefore the global optimum over *all* supported admissible weights and all `1<=q<3/2` is exactly uniform `w`, `q=1`, giving

`||p_Q||inf <= (3e)64^(-1/6)=3e/2`.

The older completed e5 Theorem D applies to this same inequality and gives

`||p_Q||inf <= 6 sqrt(e) 64^(-1/6)=3 sqrt(e)`.

## 3. Partner soft-ridge gate fails in both orientations on the same M

Apply fleet03/B04 `QFORM-SOFT-RIDGE-THIRDVOLUME-GATE-v1` at `theta=1/3`.  Here `T2=s3(M)^2=1`, and the singular-mode ridge eigenvalues are

`48/49, 12/13, 3/4`.

On the U side the six diagonal leverages are

`24/49,24/49,6/13,6/13,3/8,3/8`,

so `max diag K=24/49>1/3`.  On the V side the six diagonal values are approximately

`0.4664042,0.4664042,0.4002659,0.4002659,0.4596642,0.4596642`,

again all above 1/3.  Thus both fixed-scale soft-ridge exits fail and the partner theorem produces its aggregate row/column double-hub survivor.

But the q=1 volume law above is not merely admissible; it is globally optimal.  Hence **double-hub failure of the partner gate is not by itself a hard branch**.  The hard structural branch must additionally encode minor-support deficiency or determinant/entropy degeneration.

## 4. Target-valid indefinite embedding and direct ridge comparison

Put

`A=[[0,M],[M^T,0]]`.

Then A is a genuinely rotated indefinite 12x12 physical matrix with spectrum

`{+4,+2,+1,0,0,0,-4,-2,-1,0,0,0}`,

so six eigenvalues have modulus at least one.  For arbitrary independent cap-one inputs the sharp weighted-volume theorem therefore gives

`||p_(X^T A X)||inf <= 3e/2 = 4.077422742688568...`.

For comparison, apply the completed ridge density theorem to this same physical cut with `gamma=1/sqrt(2)`.  Its ridge trace is

`theta=16/(16+1/2)+4/(4+1/2)+1/(1+1/2)=250/99`,

and the U-side maximum diagonal is `16/33<1/2`.  Hence

`||p_(X^T A X)||inf <= (125/26)sqrt(e) = 7.926544570673695...`.

Thus on one explicit target-valid physical matrix the certified hierarchy is

`sharp balanced 3-volume 3e/2 < e5 Theorem D 3sqrt(e) < explicit ridge (125/26)sqrt(e)`,

while the newest partner fixed-scale soft-ridge gate fails in both orientations.

## Remaining gap

The support theorem removes one ambiguity: q=1 volume infeasibility is equivalent to absence of two disjoint physical row bases and therefore forces a finite-support/coloop rank defect.  The next unpaid implication is quantitative: combine that support defect with determinant/entropy scale and the target spectral hypothesis to enter an already-paid coloop/hub/grouped or physical-pair endpoint without paying a vanishing local coefficient.
