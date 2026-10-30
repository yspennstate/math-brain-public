# fleet03/B08 r59 — full independent review of `QFORM-FIXED-MULTIPLICITY-8-v1`

Source control objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.  
Verdict: **PASS as one genuinely separate end-to-end mathematical review.** A second separate full review is still required before independent-validation status.

The reviewed candidate is the later multiplicity-eight assembly at `yspennstate/math-open-problems@42decd5b0bac31666cbbc613bcd2d64194775063`, independently reassembled at `50a479407cc45f4fbcc87e70ac1846c049138c9f`. The complete latest nine-eigenvalue source used underneath is `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`, SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`.

## Reviewed theorem

For arbitrary independent real coordinates with probability densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_8(A)>=s>0`, the candidate proves

`||p_(X^TAX+b^TX+c)||_infinity < 2400 K^2/s`.

The theorem is an essential-density statement. The no-pivot Fourier branches have `C_0` densities; global continuity is not established by the pivot branches.

## Dependency-by-dependency review

### A. Nine-eigenvalue analytic base — PASS

I read the complete self-contained nine/400 source. The nonsymmetric interpolation is used correctly: for a disjoint nonsingular `r x r` seed `B=A[S,T]`,

`P=A[:,T]B^{-1}A[S,:]`

satisfies `P[S,:]=A[S,:]`, `P[:,T]=A[:,T]`. In the completion `A=D+R+E`, `D` is diagonal and zero on `S union T`; globally `rank R<=3r`, while on `L=(S union T)^c`, `R[L,L]=P[L,L]` and `rank R[L,L]<=r`. The proof never substitutes one rank bound for the other.

The grouped Fourier compiler uses original-coordinate conditioning and deterministic projection-density estimates, not independence after rotation. The order-three receiver is an integrable Fourier endpoint; the order-two receiver is used only as a full negative-half-potential endpoint. Scalar and pair pivots retain arbitrary affine terms. Scaling restores `K^2/s` correctly.

### B. Pivot branches under only eight directions — PASS

Use the `s_8` reduction's `eta=1/100`.

A scalar pivot leaves at least seven unit Schur directions, hence the proved five-direction full half-potential applies. Its safe bound is

`max(70,80,1+4*(142/5))=573/5=114.6`,

so the outer scalar square profile gives `<1146`.

A definite two-coordinate pivot gives `<40`. An indefinite pair retains at least six unit Schur directions; using `log16<14/5`, `L_0<54/5`, `1/e<1/2`, its bound is `<393/2=196.5`. All pivot branches are therefore below `2400`.

### C. B04 terminal no-pivot dichotomy — PASS

Dependency: `5dc3b183bf69c8ab69f725c4464d5073f5c803cd`.

If `V_3>=kappa^3`, `kappa=1/6400`, a fair physical cut has third crossing volume at least `4^-3 kappa^3`; the marginal-free order-three receiver with `C_3<15` gives `<2400`, with a `C_0` density.

Otherwise the sampled order-two seed construction has good seeds with `epsilon<=3 sqrt(2)/80`. The completion has global rank at most six and restricted complement rank at most two. The designated fleet04/B08 audit at `6b11fd000e12a6c279d736781d3f886e43a487fd` independently verifies these two rank facts. Applying its global rank result at `r=2` gives the live inequality

` s_2(D) >= s_8(D+R) >= 1-epsilon`.

That is exactly the two-large-defect step required by the collar.

### D. B17 robust-anchor extraction — PASS

Dependency: `0408c579bcda638e72c010ff99892a22b9049796`.

The assigned good-seed masses `w_H` and physical pair volumes `D_H=det(A[H,H^c]A[H,H^c]^T)` satisfy

`sum_H w_H >= V_2/2 = (1/2) sum_H D_H`.

Hence some positive `D_H` has `w_H>=D_H/2`. The two-sided interpolation collar gives `delta_*^2 w_H<=D_H^2`, so

`D_H>=delta_*^2/2`,

where

`delta_*=97/100-(297 sqrt(2)+3 sqrt(202))/4000`.

No reciprocal of an individual tiny seed is paid. The exact rational lower estimate

`sqrt(2)<3/2`, `sqrt(202)<15`

implies `delta_*>6779/8000>4/5`, hence for the selected literal anchor pair

`g:=det(CC^T)>8/25`.

### E. B20 one-high leverage closure — PASS

Dependency: `74542593cca87e76d83b07f98e2c895f76b90796`.

For `Q_C=C^T(CC^T)^(-1)C`, let `q_i=(Q_C)_ii` and `J={i:q_i>2/3}`. Since `Q_C` is a rank-two projection, `|J|<=2`.

For `|J|<=1`, the anchored disjoint-minor identities produce an interpolation error `E` with

`||E||_F^2 <=3 W_dis/g`.

If `W_dis<=g/48`, then `||E||_F<=1/4`. The residual matrix has global rank at most `4+|J|<=5` and restricted low-coordinate rank at most two. Rank perturbation from `s_8(A)>=1` forces at least three low diagonal coefficients of modulus at least `3/4`. On those three physical coordinates, diagonal entries of the residual are at least `0.74` in modulus while the sum of the two off-diagonal magnitudes in any row is `<0.701`. Strict diagonal dominance forces restricted rank three, contradiction. Thus

`W_dis>g/48`.

### F. Two-high leverage endpoint — PASS and empty

If `J={i,j}`, normalize the rank-two row map and define

`w_ab=det(C_{ab})^2/g`.

Cauchy--Binet gives `sum w_ab=1`, while the rank-two determinantal marginal identity gives

`q_i=sum_{b!=i}w_ib`.

Thus `w_ij>=q_i+q_j-1>1/3`, so

`det(C_{ij})^2>g/3>8/75`.

But the no-`eta`-pivot condition gives every off-diagonal physical coefficient

`|A_uv|^2<eta^2+eta=101/10000`.

All four entries of `C_{ij}` are off-diagonal, hence

`|det C_{ij}|<2(101/10000)=101/5000`,

so

`det(C_{ij})^2<10201/25000000`.

The exact rational inequality

`8/75 > 10201/25000000`

is a contradiction. Therefore the only endpoint left by B20 is actually empty.

### G. Product-safe incident-volume receiver — PASS

Dependency: `d44d368cd18a2590fc62d0aadd2cf2b7e9d0e83f`.

For `W_dis>0`, a fair cut of the complement keeps one distinguished row coordinate opposite its three column coordinates with probability `1/16`. The resulting physical crossing has exact currency `W=S^2 Z_1`. If residual row volume is diffuse, the `(k,ell)=(2,1)` grouped product-Fourier compiler applies; if one residual row is heavy, that literal physical coordinate is promoted to a third hub. Both cases give

`||p_Q||_infinity <= C_inc W_dis^(-1/6)`,

`C_inc=3*2^(5/6)*e^(2/3)`,

with an integrable characteristic-function envelope and hence a continuous `C_0` density.

Since the two-high case is impossible, every robust-pair terminal state has `|J|<=1`, so `W_dis>g/48` and this receiver closes the branch. The sharper source constants yield `<23.48`; the exact weaker rational bound `g>8/25` already gives `W_dis>1/150`.

## Assembly verdict

The normalized exhaustive bounds are:

- scalar pivot: `<1146`;
- definite pair: `<40`;
- indefinite pair: `<197`;
- no pivot, large `V_3`: `<2400`, `C_0`;
- no-pivot robust terminal state: `<23.48`, `C_0`.

Thus the dependency chain proves the stated `s_8` candidate with universal constant `2400`. Scaling by `Y=KX` and `A/s` gives `2400 K^2/s`.

I found no missing sign case, hidden moment/support assumption, rotated-independence use, affine-term loss, or incorrect rank transfer. The full unrestricted three-eigenvalue conjecture remains open.

## Review gate

This file is **one independent complete PASS review**. It is not a self-awarded release certificate. One additional genuinely separate end-to-end review of the same full `s_8` chain is still required by the owner protocol before independent-validation status.

If that review also passes, the next fixed threshold is seven. The present rank-six completion mechanism loses exactly the second large diagonal defect when starting from `s_7`; reducing further therefore requires a new structural mechanism rather than a cosmetic constant tightening.
