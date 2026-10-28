SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T05:05:09Z.
attacking: the newest account02/B07 incident-E2 branch by a sharp all-orders anchored compound-tail ladder; use adjacent anchored volumes to force either a rank-three low-tail state that the newest volume-stability theorem pays when its actual physical range is diffuse, or an anchored fourth-volume state that either localizes to a finite physical core or remains explicitly conditionally diffuse.

# account01/B07 r16 — anchored compound-tail ladder and rank3-stability / anchored-E4 alternative

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate-minor selection / aggregate before reciprocal inversion  
Status: `ESSENTIAL_STEP_APPLIED / NEW ANCHORED ALL-ORDER TAIL LADDER + PAID RANK3-DIFFUSE EXIT / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved or disproved here. The new work is a deterministic all-orders anchored-minor inequality, an equation-level application of the newest designated partner account02/B07 incident-E2 theorem, and a new split of that live survivor into a paid rank-three-stable branch or an anchored fourth-volume branch. In the latter, full concentration gives an actual <=8-coordinate physical spectral core; genuine conditional diffusion is retained rather than replaced by a fictitious uniformly good minor.

## 1. Fresh source boundary and inputs actually used


The designated partner result used at equations is the newest completed account02/B07 report visible in the mathematical archive:

`yspennstate/math-open-problems@4504338d5ee1d118c318423da067aadad75ade4b`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T043951Z-account02-B07-4c9e7a/REPORT.md`.

Its live incident branch starts from a physical cross block `M`, `F=||M||_F`, with

`T_2(M)=sum_{j>=3}s_j(M)^2 >= theta F^2`,                    (1.1)

and physical anchors `(i,a)` whose complete incident second-minor bank

`H_2 := sum_{k!=i,l!=a} det M[{i,k},{a,l}]^2`

satisfies

`sqrt(H_2) > (11 theta/7200)F^2`.                              (1.2)

The partner proves the sharp lift

`H_3 >= (1/2)T_2(M)H_2`,                                      (1.3)

where `H_3` is the complete third-minor mass through the same physical row and column anchors. Consequently

`H_3 > omega(theta)F^6`,                                      (1.4)

with

`omega(theta)=121 theta^3/(2*7200^2)`.                         (1.5)

At `theta=1/16`,

`omega=121/424673280000 = 2.8492491922260804e-10`.             (1.6)

The D5 payment from the newest-Claude Fourier package is already complete. Thus after removing that paid branch one may assume

`H_5 <= E_5(M) < eta_* F^10`,                                 (1.7)

where

`eta_* = theta^6/(120*3072^2)`.                               (1.8)

At `theta=1/16`, `eta_*=1/18999560927969280`.

The second source actually applied is the current volume-stability tail extension

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`.

For any original-coordinate cross block, if `P` is a physical row-space projection with `max_i P_ii<=1/2` and

`||(I-P)M||_op <= sqrt(T_2(M))/15`,                             (1.9)

then the full ambient form has a continuous density satisfying

`||p_Q||_inf <= (9 sqrt(3)e/2)[s_1(M)^2 s_2(M)^2 T_2(M)]^(-1/6)`. (1.10)

All self blocks, outside couplings, affine terms and remaining spectrum are retained in that theorem. Transposing the cross block gives the same exit when the corresponding right singular projection is diffuse.

No arbitrary-joint coarea bound, pointwise law-uniform stationary-phase estimate, spectral-coordinate independence, conditional-density positive moment, one-good-minor assertion, or small-random-perturbation argument is used below.

## 2. New theorem: the anchored compound-tail ladder

For a real `m x n` matrix `M`, fix one physical row `i` and one physical column `a`. For `k>=1` define

`H_k^(i,a)(M)
  = sum_{|R|=|C|=k, i in R, a in C} det M[R,C]^2`,             (2.1)

and write

`T_k(M)=dist_F(M,{rank<=k})^2=sum_{j>k}s_j(M)^2`.              (2.2)

### Theorem 2.1 — `QFORM-ANCHORED-COMPOUND-TAIL-LADDER-v1`

For every integer `k>=1`,

`boxed: H_(k+1)^(i,a)(M) >= [T_k(M)/k] H_k^(i,a)(M).`          (2.3)

The constant `1/k` is sharp for every `k`.

### Proof

First suppose the anchor entry `b=M_ia` is nonzero. Reorder indices only in notation and write

`M=[[b,r^T],[c,D]]`,
`S=D-c r^T/b`.                                                 (2.4)

For every residual `(k-1)x(k-1)` minor, scalar Schur expansion gives

`det M[{i} union R,{a} union C] = b det S[R,C]`.               (2.5)

Hence, with `E_j(S)=e_j(SS^T)` and `E_0=1`,

`H_k^(i,a)(M)=b^2 E_(k-1)(S)`.                                (2.6)

Let `S_(k-1)` be a best rank-`(k-1)` Frobenius approximation to `S`, and replace only the residual block `D` by

`D_(k)=c r^T/b + S_(k-1)`.                                    (2.7)

The resulting matrix has scalar Schur complement `S_(k-1)`, hence rank at most `k`, while the change in Frobenius norm is exactly `||S-S_(k-1)||_F`. Therefore

`T_k(M) <= T_(k-1)(S)`.                                       (2.8)

For squared singular values `lambda_1>=lambda_2>=...` of `S`, the elementary compound-tail inequality is

`T_(k-1)(S) E_(k-1)(S) <= k E_k(S)`.                          (2.9)

Indeed

`k E_k = sum_{|I|=k-1} prod_{r in I}lambda_r * sum_{j notin I}lambda_j`,

and for every `(k-1)`-set `I`, the complementary sum is at least the tail after the largest `k-1` singular values. Combining (2.6)-(2.9) gives (2.3).

If `b=0`, perturb only that one entry to `epsilon`. For every nonzero `epsilon` the proved inequality holds. Each `H_j` is a polynomial in the matrix entries and each `T_k` is continuous in the singular values, so `epsilon->0` proves (2.3) without an invertibility assumption.

For sharpness take `M=I_(k+1)` and anchor `(1,1)`. Then `H_k=k`, `H_(k+1)=1`, and `T_k=1`, so equality holds in (2.3). QED.

### Relation to the designated partner

At `k=2`, (2.3) is exactly the partner's sharp incident lift (1.3):

`H_3 >= (1/2)T_2 H_2`.                                        (2.10)

Thus the newest account02/B07 result is not merely cited: it is recovered as the first nontrivial member of an all-orders ladder and then its concrete lower bound (1.4) is used below.

Two immediate further members are

`H_4 >= (T_3/3)H_3`,                                          (2.11)
`H_5 >= (T_4/4)H_4`.                                          (2.12)

No individual determinant is inverted anywhere in this chain.

## 3. Adjacent anchored volumes are exact low-tail certificates

Whenever `H_k>0`, (2.3) can be read in the reverse direction as

`boxed: T_k(M) <= k H_(k+1)/H_k.`                              (3.1)

This is the first new implication needed in the current branch. It says that a small next anchored compound is not merely a failure of localization: it is a quantitative singular-tail certificate for the entire physical cross block.

For a nonzero scalar anchor `b`, (2.6) also gives the condition-number-free Schur form

`T_(k-1)(S) <= k H_(k+1)/H_k`,                                (3.2)

because the same compound-tail inequality applies directly to `S`. In particular

`T_2(S)<=3H_4/H_3`,
`T_3(S)<=4H_5/H_4`,
`T_3(S)^2<=12H_5/H_3`.                                        (3.3)

All factors of the possibly tiny physical entry `b` cancel. Equation (3.3) is retained as useful provenance currency for any future scalar-anchor receiver, but the main split below uses the pivot-free global version (3.1), so it also covers `b=0`.

## 4. A calibrated rank-three-stability versus anchored-fourth-volume split

Keep the live partner branch (1.1)-(1.8). Choose

`epsilon_3 := theta/225`.                                      (4.1)

There are two cases.

### Case A: small anchored fourth volume

Assume

`H_4 <= (epsilon_3/3) H_3 F^2`.                               (4.2)

Equation (3.1) with `k=3` gives immediately

`boxed: T_3(M) <= epsilon_3 F^2.`                              (4.3)

Thus the actual cross block is within Frobenius distance `sqrt(epsilon_3)F` of rank three. More importantly, this is strong enough to activate the new volume-stability tail theorem whenever the actual top-three singular frame is physically diffuse.

Indeed `T_2>=theta F^2` and

`s_3(M)^2 = T_2(M)-T_3(M) >= (theta-epsilon_3)F^2`.            (4.4)

Let `P_3^L` be the projection onto the top-three left singular vectors. Then

`||(I-P_3^L)M||_op=s_4(M)<=sqrt(T_3(M))
                              <=sqrt(epsilon_3)F
                              <=sqrt(T_2(M))/15`,              (4.5)

because `epsilon_3/theta=1/225`. Therefore, if

`max_i (P_3^L)_ii <=1/2`,                                     (4.6)

the newest volume-stability theorem (1.10) applies. The same is true after transposition if the right top-three projection satisfies the corresponding bound.

Using `s_1,s_2>=s_3`, (1.10) and (4.4) yield the explicit continuous-density estimate

`boxed:
 ||p_Q||_inf
 <= (9sqrt(3)e/2)
    [theta(theta-epsilon_3)^2]^(-1/6) F^(-1).
`                                                                    (4.7)

In the inherited no-large-star collar `CR<=Lambda`, `CRF>kappa`, so `F>kappa/Lambda` and (4.7) becomes the universal bound

`||p_Q||_inf
 < (9sqrt(3)e/2)[theta(theta-epsilon_3)^2]^(-1/6)
   (Lambda/kappa).`                                             (4.8)

At the current convenient constants

`theta=1/16`, `epsilon_3=1/3600`, `kappa=1/(256sqrt(3))`, `Lambda=1`,

this is

`boxed: ||p_Q||_inf < 37634.`                                  (4.9)

The density is continuous on this paid subbranch because the source theorem proves Fourier integrability.

Consequently the only survivor of Case A has BOTH top-three physical singular frames containing a coordinate of leverage `>1/2`, together with the strong actual low-tail estimate

`dist_F(M,rank<=3) <= F/60`.                                   (4.10)

This is substantially narrower than merely knowing that D5 failed.

### Case B: substantial anchored fourth volume

Otherwise

`H_4 > (epsilon_3/3)H_3F^2
     > (epsilon_3 omega(theta)/3)F^8`.                         (4.11)

This is a genuine original-coordinate fourth-volume bank through the SAME physical row/column anchors supplied by the partner incident compiler. It has been obtained without selecting a determinant.

The D5-failed state also gives, from (3.1) at `k=4`,

`T_4(M) <=4H_5/H_4
        < [12 eta_*/(epsilon_3 omega(theta))]F^2`.              (4.12)

At `theta=1/16`,

`epsilon_3=1/3600`,
`epsilon_3 omega/3 = 121/4586471424000000
                    =2.63819369650563e-14`,
`12eta_*/(epsilon_3 omega)=253125/31719424
                           =0.00798012599472172...`.            (4.13)

The partner's earlier global `E_3/E_5` argument gives an even smaller rank-four tail in this same branch; (4.12) is kept because it is generated entirely by the SAME anchored packet and therefore meshes with the physical-core tree below.

## 5. The high-H4 branch: finite physical core or explicit conditional diffusion

Normalize the anchored fourth-volume bank in (4.11):

`w(K,L)=det M[{i} union K,{a} union L]^2/H_4`,                 (5.1)

where `K,L` are residual triples. This is a probability law.

Run the following finite tree, always retaining determinant weights.

1. **Residual triples.** If one orientation has all inclusion marginals at most `2/3`, stop and record a level-1 conditional-diffuse packet. Otherwise choose one residual row and one residual column, each with marginal `>2/3`. Their joint event has mass `>1/3`.
2. **Residual pairs.** Condition on those two selected physical coordinates. If one orientation now has all pair-law inclusion marginals at most `2/3`, stop and record a level-2 conditional-diffuse packet. Otherwise choose another row/column pair with joint conditional mass `>1/3`.
3. **Residual singleton.** Condition again. If one orientation's singleton law has all marginals at most `2/3`, stop and record a level-3 conditional-diffuse packet. Otherwise choose the final row and column, whose joint conditional mass is `>1/3`.

If no diffuse stop occurs, one actual physical `4x4` cross minor `C` satisfies

`boxed: |det C|^2 > H_4/27.`                                  (5.2)

This is not a one-good-minor assertion from aggregate mass alone: the determinant is selected only after three proved concentration failures, while every diffuse alternative is kept explicitly.

### The terminal concentrated state is a paid physical core in N3

In the current sufficient no-pivot class `N3(tau)` with `tau=1/128`, every actual matrix entry obeys

`|A_uv|^2 < tau+tau^2`.                                        (5.3)

For `u=v` this follows from `|A_uu|<tau`; for `u!=v`,

`A_uv^2 <= |A_uu A_vv| + |A_uu A_vv-A_uv^2|
        < tau^2+tau`.

Hence the selected `4x4` cross submatrix obeys

`||C||_op <= ||C||_F <4sqrt(tau+tau^2).`                       (5.4)

If its singular values are `sigma_1>=...>=sigma_4`, then

`|det C|=sigma_1 sigma_2 sigma_3 sigma_4
        <= ||C||_op^2 sigma_3^2`,                              (5.5)

so

`sigma_3(C)
 > (H_4/27)^(1/4)/[4sqrt(tau+tau^2)].`                         (5.6)

Let `H` be the union of the involved original coordinates, so `|H|<=8`. Since `C` is a coordinate compression of the actual symmetric principal block `A[H,H]`, singular-value compression gives

`s_3(A[H,H]) >= s_3(C)`.                                      (5.7)

Because a symmetric matrix's singular values are the absolute values of its eigenvalues, `A[H,H]` has three actual eigenvalues of modulus at least the right side of (5.6). Conditioning only on the original coordinates outside `H`, the bounded-dimensional spectral theorem therefore gives an essentially bounded conditional density, uniformly in the induced affine term, and averaging preserves the bound.

Combining (4.11), (5.2), (5.6) gives

`s_3(A[H,H])
 > [(epsilon_3 omega(theta))/81]^(1/4)
   F^2/[4sqrt(tau+tau^2)].`                                   (5.8)

Thus the finite-dimensional receiver (`m<=8`) yields

`boxed:
 ||p_Q||_inf
 < 8 sqrt(48 pi (tau+tau^2))
   [81/(epsilon_3 omega(theta))]^(1/4) F^(-2).
`                                                                    (5.9)

On `F>kappa/Lambda`, this is a universal constant. At the current numerical collar `theta=1/16`, `tau=1/128`, `kappa=1/(256sqrt(3))`, `Lambda=1`, the unoptimized value is below `9.70e9`.

Only essential boundedness is asserted for this finite-core payment. I do not promote it to continuity here because the bounded-dimensional projected-gradient receiver is an interval-domination theorem rather than the Fourier-integrability conclusion used in Case A.

## 6. Why a diffuse high-H4 stop is genuine: a target-valid N3 stress family

The conditional-diffuse alternatives in Section 5 cannot be discarded. There is an explicit target-valid no-pivot family realizing them.

Let `N` be a power of two, let `U` be the first three columns of a normalized `N x N` Hadamard matrix, and put

`R=UU^T`,
`b=1/16`,
`M_N=diag(b,R)`,
`A_N=[[0,M_N],[M_N^T,0]]`.                                    (6.1)

Then `R` has singular values `1,1,1`; hence `M_N` has singular values

`1,1,1,1/16`,                                                  (6.2)

and `A_N` has `+1,+1,+1,-1,-1,-1` among its eigenvalues. Thus it satisfies the original three-large-eigenvalue target.

Every entry of `R` has magnitude at most `3/N`. For `N>=64`, every off-diagonal entry of `A_N` has square at most `1/256<1/128`, while all diagonals vanish. Hence every physical principal `2x2` determinant has magnitude `<tau=1/128`: this is an actual `N3(tau)` family.

Anchor the scalar row and column of `M_N`. Exact block structure gives

`H_2=b^2 E_1(R)=3b^2`,
`H_3=b^2 E_2(R)=3b^2`,
`H_4=b^2 E_3(R)=b^2`,
`H_5=0`.                                                       (6.3)

The conditional residual triple law in `H_4` is exactly the rank-three volume law of `R`. Its row and column marginals are the Hadamard-frame leverage scores

`3/N`,                                                         (6.4)

so Section 5 stops immediately in its level-1 conditional-diffuse branch.

Moreover each residual `3x3` determinant obeys

`|det R[K,L]|=|det U_K det U_L| <= (3/N)^3`,                   (6.5)

so every anchored physical `4x4` determinant is at most `27|b|/N^3` in magnitude. No bounded-cardinality core with a uniform determinant can be extracted from this branch as `N->infinity`.

For `N=64`, a direct regression gives singular values `(1,1,1,1/16,...)`, `F^2=3+1/256`, maximum cross entry `1/16`, maximum principal-pair determinant magnitude `1/256`, and residual inclusion marginal `3/64`. This family is a structural stress test, not a QFORM counterexample; other specialized low-rank/mixed-hub receivers may pay it.

## 7. What changed in the proof map

The newest designated partner left an incident-E2 branch with a quantitative anchored `H_3` packet but two genuinely conditional-diffuse survivors. This run adds two facts.

First, the partner lift is one member of the sharp all-orders identity (2.3). Therefore the next anchored volume is not merely extra combinatorics: the ratio `H_4/H_3` exactly controls the full rank-three tail `T_3(M)` up to factor three.

Second, calibrating the split at `epsilon_3=theta/225` makes the low-`H_4` side strong enough to trigger the newest physical-volume stability theorem. Thus:

- **low H4** -> `dist_F(M,rank<=3)<=F/60`; if either actual top-three physical singular frame has leverage at most `1/2`, the full form already has a **continuous** density with universal cap `<37634` on the inherited collar;
- **high H4** -> a quantitative same-anchor fourth-volume bank; if its finite concentration tree terminates, the full form is paid by an actual `<=8`-coordinate physical spectral core; otherwise one obtains one of three explicit `2/3`-conditional-diffuse anchored-fourth-volume states, while the D5 failure keeps the cross block in a rank-four low-tail regime.

This is an actual physical-core / low-tail alternative; no uniformly good local minor is asserted in the diffuse states.

## 8. First remaining implication

The first surviving B07 obligation is now

`QFORM-RANK3-BIHEAVY-OR-RANK4-CONDITIONAL-DIFFUSE-RECEIVER-v1`:

1. pay the low-H4 rank-three tube when BOTH top-three physical singular projections have a leverage `>1/2`; or
2. in the high-H4 branch, pay one of the three explicit conditional-diffuse anchored-fourth-volume packets while retaining arbitrary same-bank quadratic curvature and the true nonzero rank-four tail.

The Hadamard stress in Section 6 shows why item 2 cannot be replaced by a bounded physical-core assertion. The natural next mechanism is a mixed-hub / fractional-volume estimate that treats the fixed anchor(s) without demanding a false global marginal bound, while using the conditional `2/3` diffuse law on the residual determinant slots.

Full QFORM and full-target continuity remain OPEN. No independent end-to-end review of the new theorem is claimed.

## 9. Regression note

A private exact/numerical regression checked (2.3) on 630 `(matrix,k)` cases across rectangular integer matrices of sizes from `3x3` through `7x5`, including zero anchor entries; no violation occurred. The smallest nontrivial floating ratio `H_(k+1)/([T_k/k]H_k)` in that batch was `1.169199626...`. The identity matrices give exact ratio one and certify sharpness analytically. These checks are diagnostics only; the proof is Sections 2-5.
