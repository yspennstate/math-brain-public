SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-22T23:39:48Z.
attacking: the small-positive disjoint-Pluecker-mass null-frame chamber by converting partner D0 into an actual original-coordinate rank-three cut, and falsifying a finite-ray stability shortcut.

# account02/B11 QFORM — disjoint-basis mass to a physical rank-three cut

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: **Indefinite signatures**  
Method: complementary constructions / source-valid counterexamples  
Run: `20260922T233948Z-account02-B11-QFORM-b35bb6c3`  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The full conjecture is not proved here. The new step is a deterministic bridge in the exact-rank-three zero-diagonal indefinite chamber: the assigned partner's disjoint Pluecker mass `D0` is exactly an average of two-sided spectral volumes over product-preserving original-coordinate half-cuts. Consequently, every `D0>0` forces an actual original-coordinate cross block whose third singular value is at least `s sqrt(D0)/8`, where `s` is the least nonzero spectral magnitude. A second exact identity shows that small `D0` forces a heavy physical spectral row. Together with the completed account03/B11 pair/ridge compiler, this reduces the partner's small-positive-`D0` stability problem to one sharply stated simultaneous heavy-star / nondiffuse-cross-cut residual.

## 1. First unpaid implication

The first unpaid implication after this run is

`QFORM-NULL-D0-HEAVY-CROSS-OVERLAP-v1`:

> In an exact-rank-three zero-diagonal indefinite form, assume `0<D0<<1`, every physical pair is below the quantitative pair threshold, and the cross cut forced by Theorem 3.1 fails the completed diffuse-ridge leverage condition. Use simultaneously (i) the heavy null row forced by `D0`, (ii) its many-small physical star, and (iii) the rank-three cross cut forced by the same `D0`, to obtain a product-preserving grouped hub/Fresnel or cone-trace bound uniform as `D0 -> 0`; or produce a genuine QFORM counterexample.

This is strictly narrower than the previous vague request for a stability theorem. The exact endpoint `D0=0` is already paid by the newest assigned partner result. A finite-ray-count stability statement for positive `D0` is false; Section 6 gives an exact target family proving that.

## 2. Source-pinned inputs and correction status

### 2.1 Assigned partner account03/B11 r18 — actually applied

Completed partner source:

`yspennstate/math-open-problems@6f501dcdf1db12adaa34b54c10c5fa75c1688e69`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T221034Z-account03-B11-QFORM-r18/REPORT.md`

and its `STABILITY_ADDENDUM.md` at the same commit.

For exact rank three `A=R Lambda R^T`, `R^T R=I_3`, with signature `(2,1)` or `(1,2)`, all three nonzero eigenvalue magnitudes at least `s`, and zero physical diagonal, the partner defines

`w_B=det(R_B)^2`, `sum_B w_B=1`,

and

`D0=sum_{B cap T=empty} w_B w_T`.

It proves the endpoint theorem

`D0=0  ==>  at most five projective null-ray banks`

and hence, at `s=1`, `||p_Q||_infinity <=449.0569661600281...`. Its addendum also proves `D0=sum_B w_B det S_B`, where `S_B` is the complement covariance. The present report uses exactly this `D0` and extends it to an original-coordinate cross-cut identity.

### 2.2 Assigned partner account03/B11 r17 — quantitative exits

Completed source:

`yspennstate/math-open-problems@c869a82e52e46664d5bf299c3b210de02a02fc50`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T215136Z-account03-B11-QFORM-r17/REPORT.md`.

If `s_3(A)>=s` and an original-coordinate zero-diagonal physical pair has `|A_ij|>=delta s`, its pair branch gives

`||p_Q||_infinity <= 3*400^(1/3) delta^(-5/6) s^(-1)`

with coefficient `22.1041889918423...`.

If an original-coordinate cross block has third singular value `tau>=sigma s` and one orientation has all row norms at most `tau/sqrt(12)`, the ridge branch gives a continuous density with

`||p_Q||_infinity <= (9/2)sqrt(3e)/(sigma s)`.

The present theorem supplies such a cross block with `sigma=sqrt(D0)/8`; thus this partner theorem is applied quantitatively below, not merely cited.

### 2.3 Binding corrections

No step assumes independence after spectral rotation, a conditional density cap for conjugate variables, an arbitrary-joint rank-three coarea bound, a fixed good physical minor, pointwise law-uniform oscillatory decay, moments/support bounds, or perturbative deletion of small coefficients. The argument is deterministic in the spectral frame until the cited product-law density exits are invoked. It does not claim that an arbitrary full-rank matrix is controlled by its chosen three-eigenspace component: additional spectrum can alter physical cross blocks and remains a separate debt.

## 3. Main theorem: `D0` forces a rank-three original-coordinate cross cut

Let `A=R Lambda R^T`, `R^T R=I_3`, be exact rank three. Order the absolute eigenvalues of `Lambda` as `ell_1>=ell_2>=ell_3=s>0`. For a physical subset `S`, write

`G_S=R_S^T R_S=sum_{i in S} r_i r_i^T`,

so `G_{S^c}=I_3-G_S`, and let

`C_S=A[S,S^c]=R_S Lambda R_{S^c}^T`.

### Theorem 3.1 — `QFORM-D0-HALFCUT-CROSS-S3-v1`

For a fair Bernoulli half-partition `S` of the original coordinates,

`boxed: E_S[det(G_S) det(I-G_S)] = D0/64.`                       (3.1)

For every deterministic `S`, if `sigma_1(C_S)>=sigma_2(C_S)>=sigma_3(C_S)` are its first three singular values, then

`boxed: product_{k=1}^3 sigma_k(C_S)
       = |det Lambda| sqrt(det(G_S)det(I-G_S)).}`                 (3.2)

Moreover

`boxed: sigma_3(C_S)
       >= s sqrt(det(G_S)det(I-G_S)).}`                           (3.3)

Consequently there exists an original-coordinate cut `S,S^c` with

`boxed: sigma_3(A[S,S^c]) >= (s/8) sqrt(D0).}`                   (3.4)

This statement is sign-independent and therefore applies equally to `(2,1)` and `(1,2)` signatures.

### Proof of (3.1)

By Cauchy--Binet,

`det(G_S)=sum_{B subset S, |B|=3} det(R_B)^2=sum_{B subset S} w_B`,

and similarly `det(I-G_S)=sum_{T subset S^c} w_T`. Hence

`det(G_S)det(I-G_S)
 =sum_{B,T} w_B w_T 1_{B subset S}1_{T subset S^c}`.

The indicator vanishes unless `B cap T=empty`. For two disjoint triples, the fair half-partition places all three elements of `B` in `S` and all three elements of `T` in `S^c` with probability `2^-6`. Therefore

`E det(G_S)det(I-G_S)=2^-6 sum_{B cap T=empty}w_Bw_T=D0/64`.

### Proof of (3.2)

If either covariance is singular, both sides are zero. Otherwise `C_S` has rank three. Since

`C_S C_S^T=R_S Lambda (I-G_S) Lambda R_S^T`,

the product of its three nonzero squared singular values is

`det(G_S) det(Lambda(I-G_S)Lambda)
 =det(G_S)det(I-G_S)det(Lambda)^2`.

Taking square roots gives (3.2).

### Proof of (3.3)

Both `R_S` and `R_{S^c}` are contractions because their Gram matrices are bounded above by the identity. The singular-value ideal inequality therefore gives `sigma_k(C_S)<=ell_k`, `k=1,2,3`. Divide (3.2) by `sigma_1 sigma_2` and use `sigma_1 sigma_2<=ell_1ell_2`:

`sigma_3(C_S)
 >= (ell_1ell_2ell_3)/(ell_1ell_2)
    sqrt(det(G_S)det(I-G_S))
 =s sqrt(det(G_S)det(I-G_S))`.

Finally (3.1) gives a cut with determinant product at least `D0/64`, proving (3.4). QED.

### Interpretation

`D0` is not merely an abstract Pluecker overlap statistic. It is exactly sixty-four times the average squared three-volume available simultaneously on both sides of an original-coordinate product partition. Positive `D0` therefore means a genuine third cross direction exists somewhere in the original independent coordinates. This does not by itself meet the ridge leverage condition, but it removes the possibility that positive `D0` is geometrically invisible to every original-coordinate cut.

## 4. Small `D0` also forces a heavy original spectral row

Put `c_i=||r_i||_2^2`, `c_*=max_i c_i`. Since `R^T R=I_3`, `sum_i c_i=3`.

### Theorem 4.1 — `QFORM-D0-HEAVY-ROW-v1`

For the same volume weights,

`sum_{B: i in B} w_B = c_i`.                                    (4.1)

Consequently

`boxed: c_* >= (1-D0)/3.`                                       (4.2)

If, in addition, the physical diagonal is zero and `min |lambda(Lambda)|>=s`, then for an index `i_*` attaining `c_*`,

`sum_{j != i_*} A_{i_*j}^2 >= s^2 c_*`.                         (4.3)

Thus, if every physical pair satisfies `|A_ij|<delta s`, the heavy row has effective support

`boxed:
 [sum_{j != i_*}A_{i_*j}^2]/[max_{j != i_*}|A_{i_*j}|^2]
 > (1-D0)/(3 delta^2).}`                                        (4.4)

### Proof

Scale only physical row `i` of `R` by `sqrt(t)`. Cauchy--Binet gives

`det(I+(t-1)r_i r_i^T)
 =sum_{B:not i}w_B+t sum_{B:i in B}w_B`.

The matrix determinant lemma gives the left side as `1+(t-1)c_i`. Comparing the coefficient of `t` proves (4.1).

Now sample two independent volume-law triples `B,T` with probabilities `w_B,w_T`. Then `D0=P(B cap T=empty)`. By the union bound,

`1-D0=P(B cap T != empty)
 <=sum_i P(i in B and i in T)
 =sum_i c_i^2
 <=c_* sum_i c_i=3c_*`,

proving (4.2).

If `A_ii=0`, then

`sum_{j != i}A_ij^2=(A^2)_ii=r_i^T Lambda^2 r_i>=s^2 c_i`,

which gives (4.3), and division by the assumed entry bound gives (4.4). QED.

This is the promised quantitative complement to the partner's endpoint: as `D0 ->0`, the frame cannot remain uniformly diffuse in physical leverage. It must carry a row of leverage asymptotically at least `1/3`.

## 5. Conditional end-to-end reduction in the zero-diagonal exact-rank-three chamber

Combine the newest partner r18 endpoint, Theorems 3.1 and 4.1, and partner r17. Fix `delta>0`.

1. **Endpoint.** If `D0=0`, partner r18 gives the five-ray bank reduction and the universal bound `449.056966.../s` after scaling.
2. **Physical-pair exit.** If some `|A_ij|>=delta s`, zero diagonal makes the pair exactly indefinite, and partner r17 gives `||p_Q||_infinity <=22.104189 delta^(-5/6)/s`.
3. **Positive-D0 cross cut.** If `D0>0`, Theorem 3.1 gives a cut with `tau=sigma_3(A[S,S^c]) >= s sqrt(D0)/8`. If one orientation of that cut has every row norm at most `tau/sqrt(12)`, partner r17 applies with `sigma=sqrt(D0)/8` and gives

   `boxed: ||p_Q||_infinity <=36 sqrt(3e)/(s sqrt(D0))
          =102.804084301397.../(s sqrt(D0)).}`                   (5.1)
4. **Only residual.** If the pair exit fails and the guaranteed cut fails the ridge diffusion condition in both orientations, then two simultaneous many-small structures are forced. The global heavy row obeys (4.2)--(4.4). In addition, on at least one side of the guaranteed cut there is a cross row `u` with `||u||_2>tau/sqrt(12)`. Since each of its entries is below `delta s`,

   `boxed: ||u||_2^2/||u||_infinity^2
          > D0/(768 delta^2).}`                                 (5.2)

No case is silently dropped. The full conjecture remains open precisely because no current source supplies a uniform product-law estimate for this last simultaneous heavy-row / many-small cross-row chamber as `D0 ->0`.

For example, choosing `delta=D0` makes the residual effective supports at least `(1-D0)/(3D0^2)` and `1/(768D0)`, respectively. This quantifies the aggregation available to the next hub/Fresnel or cone-trace attempt, but is not itself a density bound.

## 6. Exact counterexample to finite-ray stability for small positive `D0`

A tempting continuation of partner r18 would be: if `D0` is sufficiently small, then the null frame lies on a uniformly bounded number of projective rays. That statement is false, even for exact target spectrum and zero physical diagonal.

Take `Lambda=diag(1,1,-2)` and define the null vector

`v(phi)=(sqrt(2) cos phi, sqrt(2) sin phi, 1)`.

Then

`v(phi)^T Lambda v(phi)=0`,

and

`v(phi)^T Lambda v(psi)=2(cos(phi-psi)-1)
                      =-4 sin^2((phi-psi)/2)`.                  (6.1)

For `0<epsilon<=1/2`, take three base rows at angles `0,2pi/3,4pi/3` with

`r_k=sqrt((1-epsilon)/3) v(phi_k)`.

For any `N>=3`, add `N` tail rows at the distinct shifted angles

`psi_j=2pi(j+1/7)/N`

with

`r_{3+j}=sqrt(epsilon/N) v(psi_j)`.

The standard first- and second-harmonic sums of equally spaced angles give

`R^T R=(1-epsilon)I_3+epsilon I_3=I_3`.                         (6.2)

Thus `A=R Lambda R^T` has exactly the three nonzero eigenvalues `1,1,-2`, while every physical diagonal is zero. The frame has `N+3` distinct projective null rays.

The three base rows are mutually Euclidean-orthogonal and each has leverage `1-epsilon`. For a subset `J` of these three base coordinates, Cauchy--Binet on the complement gives

`P_volume(B avoids J)
 =det(I-sum_{j in J}r_jr_j^T)
 =epsilon^{|J|}.`                                                (6.3)

If two independently volume-sampled triples `B,T` are disjoint, then for each of the three base coordinates at least one of `B,T` omits that coordinate. Union over the `2^3` assignments of these omissions. Each assignment has probability exactly `epsilon^3` by (6.3) and independence. Hence

`boxed: 0<D0<=8 epsilon^3.}`                                    (6.4)

The strict positivity follows because the construction has at least six distinct null rays and any three distinct rays in this parametrization span spectral space, so disjoint positive-weight basis triples exist.

Therefore `D0` can be arbitrarily small while the number of exact projective rays is arbitrarily large. This refutes finite-ray stability for positive `D0`.

It does **not** refute QFORM. From (6.1), every pair of distinct base coordinates has `|A_ij|=1-epsilon>=1/2`. So the completed partner physical-pair theorem pays the family uniformly; with `delta=1/2` and `s=1` its bound is below `39.386`. This example shows exactly why the correct stability theorem must include a quantitative pair exit rather than try to perturb the five-ray endpoint directly.

## 7. Rank-two logarithmic singularity and the role of the third direction

The mandatory control remains intact. A zero-diagonal physical pair is `[[0,a],[a,0]]`, so on two independent centered unit-uniform coordinates it produces `2aXY`, whose density has the usual logarithmic divergence at zero. Nothing in Theorem 3.1 claims that pair density is bounded.

The third direction appears in two correction-safe ways.

- In the partner pair theorem, the logarithmic pair envelope is retained and its moving critical value is averaged against the remaining third singular direction.
- In the new half-cut identity, positive `D0` forces a literal third singular direction across an original-coordinate product partition: `sigma_3>=s sqrt(D0)/8`. If that direction is sufficiently diffuse, the completed ridge theorem makes the time exponent integrable. At the singular endpoint `D0=0`, partner r18 instead uses null-matroid structure to compress the product source into at most five line banks; true rank-three spanning then supplies a third independent bank absent from the two-ray saddle.

Thus this run identifies where the third direction lives in both the positive-`D0` and endpoint regimes without invoking post-rotation independence.

## 8. Exact verification

The accompanying checker constructs the family in Section 6 with `N=5`, `epsilon=0.1`, enumerates all basis triples and all original-coordinate cuts, and verifies `R^T R=I_3`, target spectrum, zero diagonal, `sum_B w_B=1`, the one-coordinate inclusion identity, (3.1), (3.2), (3.3), `D0<=8epsilon^3`, and `|A_01|=0.9`.

It terminates `QFORM_D0_HALFCUT_CHECK_PASS`.

Checker SHA-256: `ef32e7998626682e5bac296e875958211211a92d51263ed58dec5b6325c830e7`.  
Captured-output SHA-256: `49c6ca4f412781ccb30c5fc2d6955aa1f8b883a71d16905e978d942a39cdf6e8`.

The computation is regression evidence only; the theorems above are algebraic and do not use finite census closure.

## 9. Scope and next action

**Proved here:** a deterministic `D0 -> original cross s_3` theorem, a `D0 -> heavy row` theorem, their explicit quantitative integration with the completed account03/B11 pair/ridge exits, and an exact target family refuting positive-`D0` finite-ray-count stability.

**Not proved here:** a density bound uniform through the final simultaneous heavy-star/nondiffuse-cross-cut residual, arbitrary additional spectrum, or a full end-to-end universal theorem. Essential boundedness of QFORM therefore remains OPEN. Continuity is not claimed beyond the already cited ridge-certified branches.

The next mechanism should use the two simultaneous many-small structures before inversion, rather than attempt another fixed minor, conditional cap, or perturbative deletion.
