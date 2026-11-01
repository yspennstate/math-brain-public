SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B20, 2026-09-22T18:47:24Z.
Attacking: the first unpaid P1 coherent-triangle packet by a physical 3x3 determinant/half-Riesz payment, then applying fleet04/B20 to the overlapping second-Schur geometry.

# fleet03/B20 QFORM r15 — physical-triple determinant payment and coherent-cell reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control used for the derivation:** revision `2026-09-22.11` on fresh `math-research-brain` main `4bf400db5f0fc5a60b1068cdd0a5aa0b7106d948` (to be refreshed again before publication).  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL P1 BRANCH REDUCED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not proved by the new branch; the conclusion below is essential boundedness.

## 1. Exact target and correction boundary

The target is the unrestricted statement: for every finite `n`, independent real `X_i` with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one (`s_3(A)>=1`), prove that `Q=X^T A X` has a density with one dimension/law/matrix-independent essential-supremum bound, or give a target-valid counterexample.

This run never rotates the product source and never assumes Gaussianity, moments, compact support, connected support, log-concavity, or a conditional density cap after exposing a dependent statistic. It does not use the refuted arbitrary-three-dimensional-joint coarea statement, pointwise law-uniform van der Corput decay, a one-good-minor inference, or same-square absorption.

## 2. Fresh completed inputs actually used

### 2.1 fleet01/B20 r15: the current P1 triangle packet

Source: `yspennstate/math-open-problems@0d364106e0773824b7dad9257b49046e6765a453`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260922T182314Z-fleet01-B20-QFORM-r15/REPORT.md`.

It proves that the P1 physical-pivot branch has pivot magnitude

`m := alpha = 3501/8000`,

and that the complementary-two-diagonal alternative is already paid unless, after a global output sign change, three original coordinates `i,j,k` satisfy

`a=A_ii >= m`, `b=A_jj>=1/2`, `c=A_kk>=1/2`,

and

`|x|=|A_ij|>m/2`, `|y|=|A_ik|>m/2`, `|z|=|A_jk|>m/2`.

This is the previously unpaid coherent same-sign physical triangle packet.

### 2.2 Translation-uniform rank-two half-Riesz theorem

Source: fleet03/B01, accessible at `yspennstate/math-open-problems@058acb5c8f9186ef199bbaf136b57f4dd9ea3800`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260922T163129Z-r15/REPORT.md`.

For an invertible real symmetric rank-two form with quadratic matrix `H` on independent cap-one coordinates,

`sup_t E|X^T H X - t|^(-1/2) <= 128 |det H|^(-1/4)`

is a safe current archive constant. For a two-physical-coordinate form, arbitrary affine terms are harmless: complete the affine term by translating the two original coordinates; translations preserve independence and the density caps.

### 2.3 Full-matrix physical indefinite-pair theorem

Source: `yspennstate/math-open-problems@058acb5c8f9186ef199bbaf136b57f4dd9ea3800`, path
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

If an original-coordinate principal pair `B` is invertible indefinite, `D=|det B|`, `kappa=sigma_min(B)`, and `s_3(A)>=s`, then

`||p_Q||_infinity <= 3*400^(1/3) (D^2 kappa s)^(-1/6)`.

It permits arbitrary remaining spectrum and affine terms.

### 2.4 Required designated partner fleet04/B20

Source: `yspennstate/math-open-problems@25ad8faaac5064b6814d51ae63d894fe97c1eac4`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T172057Z-fleet04-B20-QFORM-r3/REPORT.md`.

In its validated diagonal-dominated first-pivot reduction, with `|a|>=tau>=1/4`, if the selected second Schur row `S=[[d,c^T],[c,C]]` satisfies

`||c||>|d|`, `||c||>tau/9`,

then the full ambient form has `||p_Q||_infinity<5262` (essential boundedness).

## 3. New theorem: a physical nonsingular 3x3 block is directly payable

### Theorem 3.1 — `QFORM-PHYSICAL-TRIPLE-DETERMINANT-PAYMENT-v1`

Let `I={i,j,k}` be three ORIGINAL coordinates and let

`M=A[I,I]`.

Assume `a=M_ii !=0` and `det M !=0`. Then, for arbitrary outside coordinates/couplings, arbitrary affine terms, and arbitrary independent cap-one coordinate laws,

`boxed: ||p_Q||_infinity <= 128 (|a det M|)^(-1/4).`          (3.1)

Only essential boundedness is claimed.

#### Proof

Condition on all original coordinates outside `I`. They create only an affine term and a constant in the three retained independent variables. Write the conditioned polynomial as

`q(x_i,x_j,x_k)= [x_i;y]^T M [x_i;y] + ell^T[x_i;y]+d`,

where `y=(x_j,x_k)`.

Complete the **physical** scalar square in `x_i`:

`q = a (x_i+h(y))^2 + y^T S y + r^T y+d'`,

where

`S=M[{j,k},{j,k}] - M[{j,k},i] M[i,{j,k}]/a`

and the determinant identity is exact:

`det S = det M/a`.                                             (3.2)

For fixed `y`, the translate `X_i+h(y)` has a density bounded by one. The density transformation for a square gives, for almost every target `t`,

`p_{q|y}(t) <= |a|^(-1/2) |t-(y^T S y+r^T y+d')|^(-1/2)`.   (3.3)

Since `det M!=0`, the physical `2x2` matrix `S` is invertible. Complete its affine term by a translation of the two original variables `X_j,X_k`; this preserves their independence and cap-one densities. The rank-two half-Riesz theorem therefore gives, uniformly in the outside conditioning and in `t`,

`E_{j,k}|t-(X_{jk}^T S X_{jk}+r^T X_{jk}+d')|^(-1/2)
 <=128 |det S|^(-1/4).`                                      (3.4)

Average (3.3), use (3.2), and then average the already-conditioned outside variables:

`p_Q(t) <=128 |a|^(-1/2) |det M/a|^(-1/4)
          =128 (|a det M|)^(-1/4).`

This proves (3.1). No source rotation occurred. QED.

### Why this is not the refuted fixed-minor route

The theorem does **not** assert that `s_3(A)>=1` forces a uniformly good principal triple. That implication is false/unproved in the live ledger. The theorem is an analytic payment once a source-valid branch (here fleet01/B20's P1 triangle) has already produced a particular physical triple with quantitative geometry.

## 4. New target-level reduction of the coherent triangle

Assume the P1 coherent triangle and write

`M=[[a,x,y],[x,b,z],[y,z,c]]`,

with `a>=m=3501/8000`, `b,c>=1/2`, and all three diagonal signs already made positive by the allowed global reflection `A -> -A` when necessary.

Define dimensionless edge ratios

`R=x^2/(ab)`, `S=y^2/(ac)`, `T=z^2/(bc)`,

and signed normalized edges

`r=x/sqrt(ab)`, `s=y/sqrt(ac)`, `t=z/sqrt(bc)`.

The normalized principal determinant is

`g := det M/(abc) = 1+2rst-r^2-s^2-t^2`.                    (4.1)

We now pay every point of the triangle packet outside one compact normalized cell.

### Case A: a quantitatively definite physical pair

If one of `R,S,T` is at most `1/2`, the corresponding physical `2x2` block is positive definite and has determinant at least

`(1/2) m^2`.

The physical definite-pair coarea bound from fleet01/B19 gives

`||p_Q||_infinity <= pi sqrt(2)/m <11`.                      (4.2)

The last strict bound follows already from `pi<22/7`, `sqrt(2)<3/2`.

### Case B: a quantitatively indefinite physical pair

Suppose one of `R,S,T` is at least `3/2`; relabel that pair as

`B=[[u,w],[w,v]]`, `u,v>=m`, `w^2>=(3/2)uv`.

Then

`D=w^2-uv >= uv/2 >=m^2/2`.                                  (4.3)

Also `B` is indefinite. We claim

`kappa=sigma_min(B)>=m/5`.                                   (4.4)

To prove it, assume `u>=v`. The magnitude of the negative eigenvalue is increasing in `|w|`, so it is minimized at `w^2=(3/2)uv`. At that endpoint

`mu = (sqrt((u+v)^2+2uv)-(u+v))/2
     = uv/(sqrt((u+v)^2+2uv)+(u+v)).`

Since `u>=v`, the denominator is `<5u` (indeed `u+v<=2u` and the square root is at most `sqrt(6)u<5u/2`), hence `mu>v/5>=m/5`. The positive eigenvalue is at least `u>=m`; this proves (4.4).

Apply the arbitrary-rank indefinite-pair theorem with `s=1`:

`||p_Q||_infinity
 <=3*400^(1/3) (D^2 kappa)^(-1/6)
 <=3*400^(1/3) (m^5/20)^(-1/6)
 <80.`                                                        (4.5)

The `<80` bound has a purely rational verification using `400^(1/3)<8` and `m>7/16`; see the checker.

### Case C: all three pair ratios are moderate

The only remaining possibility after A/B is

`1/2 < R,S,T <3/2`.                                         (4.6)

If additionally

`|g|>=1/4`,                                                   (4.7)

then

`|det M|>=abc/4`,

and, using `a>=m`, `b,c>=1/2`,

`|a det M|>=m^2/16`.

The new physical-triple theorem gives

`||p_Q||_infinity <=128 (m^2/16)^(-1/4) <387`.               (4.8)

The final strict inequality is checked exactly by fourth powers.

Finally, if the physical edge-sign product is negative, then under (4.6)

`rst <= -(1/sqrt(2))^3 = -1/(2sqrt(2))`

and `r^2+s^2+t^2>3/2`. Hence from (4.1)

`g < 1 -1/sqrt(2)-3/2 = -1/2-1/sqrt(2) < -1/4`.             (4.9)

Thus (4.7) automatically holds and Case C pays every sign-frustrated moderate triangle.

### Corollary 4.1 — `QFORM-COHERENT-TRIANGLE-COMPACT-CELL-v1`

Every still-unpaid P1 triangle can, after sign changes of the **original coordinates** (which preserve independence and density caps), be put in the form

`a>=3501/8000`, `b,c>=1/2`, `x,y,z>0`,                       (4.10)

`1/2 < x^2/(ab), y^2/(ac), z^2/(bc) <3/2`,                  (4.11)

and

`|1+2xyz/sqrt(a^2 b^2 c^2)
   -x^2/(ab)-y^2/(ac)-z^2/(bc)| <1/4`.                       (4.12)

Equivalently with `r,s,t>0`, the last condition is

`|1+2rst-r^2-s^2-t^2|<1/4`.

All coherent-triangle states outside this compact normalized cell have already been paid with the explicit universal branch bound `<387`.

The sign product `xyz` is invariant under individual coordinate sign flips because each flip changes exactly two triangle edges. Therefore (4.9) shows that an unpaid triangle has positive edge-sign product, after which physical sign flips make all three edges positive as in (4.10).

## 5. Required fleet04/B20 result applied to an actual inequality

Now intersect the compact-cell reduction with the subset of the P1 pivot that lies in fleet04/B20's **validated diagonal-dominated first-pivot setup**. Use `i` as the first pivot and `j` as the second physical row. In the exact first Schur complement, the `j` diagonal and the `j-k` component are

`d = b-x^2/a`,

`e = z-xy/a`.                                                 (5.1)

The full second-row cross vector `c_vec` contains `e`, so `||c_vec||>=|e|`. Take the partner's allowed `tau=1/4`. Therefore the concrete sufficient condition

`|e| > max{|d|,1/36}`                                        (5.2)

implies

`||c_vec||>|d|`, `||c_vec||>tau/9`,

and the completed fleet04/B20 theorem gives

`boxed: ||p_Q||_infinity<5262.`                               (5.3)

Thus any still-unpaid point in this validated overlap must obey the actual algebraic restriction

`|z-xy/a| <= max{|b-x^2/a|,1/36}`.                           (5.4)

This is a direct application of the designated partner theorem, not a citation-only dependency. It is not asserted outside the partner's stated first-pivot setup.

## 6. What changed and what remains

This run changes mechanism from the preceding B20 structural cut reductions: it supplies a new probability/half-Riesz payment for a physical nonsingular triple and uses it to remove all sign-frustrated, far-definite, far-indefinite, and large-determinant portions of the P1 triangle packet.

The first unpaid P1 triangle implication is now sharply localized to the **positive-sign compact near-singular cell** (4.10)-(4.12), plus (5.4) on the overlap with the fleet04 first-pivot regime. Geometrically this is the source-valid region near a coherent low-determinant positive triangle, not an arbitrary 3D bounded-density pushforward.

A useful next target is `QFORM-COHERENT-CELL-STAR-BANK-PAYMENT-v1`: combine the compact cell with the already-proved P1 STAR/BANK alternatives and the exact Schur cocycle `(d,e)` to show either (i) a quantitative definite/indefinite physical pair reappears after a product-preserving grouping, (ii) a paid ridge/grouped-square packet is forced, or (iii) the triangle becomes sufficiently rank-one coherent that the remaining third large spectral direction must live in a disjoint physical bank that can be paid without selecting one reciprocal tiny minor.

The T2 and N1 packets from the global assembly remain separate. The unrestricted QFORM conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**. Continuity remains open on this new branch.

## 7. Numerical-regression role

The accompanying standard-library checker verifies only the displayed constants and exact algebraic identities. It is not evidence for the theorem beyond those finite computations; all probabilistic implications above are analytic.

## 8. Model / execution record

Model self-report: `GPT-5.6 Sol`. Highest actually supported reasoning was requested by the scheduled research context. Configured reasoning effort, provider reasoning-token usage, and provider thinking-time are `UNKNOWN/null`, not zero. Repository retrieval/write access is not treated as native brain receiver-memory ingestion, so `full_brain_connected=false` and the run remains `WITHOUT_VERIFIED_BRAIN`.
