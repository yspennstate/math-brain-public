SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-24T15:18:25Z.
attacking: the fresh multiplicity-eight candidate by an independent end-to-end dependency audit, with B08 emphasis on the nonsymmetric interpolation ranks and the robust-pair terminal geometry.

# fleet03/B08 r59 — independent review of the multiplicity-eight candidate

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution/memory status: **WITHOUT_VERIFIED_BRAIN**.  
Review verdict: **PASS as one independent end-to-end mathematical review of `QFORM-FIXED-MULTIPLICITY-8-v1`; one further genuinely separate complete review is still required before independent-validation status.**  
The unrestricted three-large-eigenvalue conjecture remains **OPEN**. Global continuity is **not** proved by this candidate; the no-pivot Fourier branches are `C_0`, while the pivot branches only require essential boundedness.

## 1. Source boundary

Fresh control remained `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`. I read the complete latest standalone nine-eigenvalue source

- `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`,
- `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`,
- git blob `19fb119877426b640b2c0dae19ec2f78a399fe11`, SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`.

I also read the later multiplicity-eight assemblies

- fleet03/B07 `42decd5b0bac31666cbbc613bcd2d64194775063`, and
- fleet03/B01 `50a479407cc45f4fbcc87e70ac1846c049138c9f`,

and independently checked the exact dependencies they invoke:

1. terminal `s_8` no-pivot collar: `5dc3b183bf69c8ab69f725c4464d5073f5c803cd`;
2. robust physical two-anchor extraction: `0408c579bcda638e72c010ff99892a22b9049796`;
3. one-high leverage closure: `74542593cca87e76d83b07f98e2c895f76b90796`;
4. product-safe disjoint incident-volume receiver: `d44d368cd18a2590fc62d0aadd2cf2b7e9d0e83f`;
5. designated partner fleet04/B08 rank audit: `6b11fd000e12a6c279d736781d3f886e43a487fd`.

No Gaussianity, moment, compact-support, log-concavity, connected-support, diagonal-basis, post-rotation independence, arbitrary-joint coarea bound, conditional-density cap, or law-uniform pointwise quadratic-phase decay is used in the chain below.

## 2. Latest nine-eigenvalue source: audit verdict

I obtain **PASS** on the complete source, in particular on the B08-sensitive algebra.

For a sampled nonsingular disjoint seed `B=A[S,T]` of order `r`, the source uses

`P=A[:,T] B^{-1} A[S,:]`.

The interpolation identities are exact:

`P[S,:]=A[S,:]`, `P[:,T]=A[:,T]`.

With the manuscript completion `A=D+R+E`, `D` diagonal and zero on `S union T`, the two distinct rank facts are also correct:

`rank R <= 3r`,

while on the complement `L=(S union T)^c`,

`R[L,L]=P[L,L]`, hence `rank R[L,L] <= r`.

They are not interchangeable. The spectral-to-volume contradiction uses the global `3r` loss and the final diagonal-dominance contradiction uses the restricted `r` bound. This matches the independent fleet04/B08 review.

The grouped product-Fourier argument keeps all hub coordinates physical, obtains its light-bank estimate only after conditioning on original coordinates, and uses deterministic projection density bounds rather than independence after rotation. The order-three receiver is an actual `L^1`-Fourier endpoint; the order-two receiver is correctly used only as a negative-half-potential endpoint. The scalar, definite-pair and indefinite-pair branches retain their affine terms and use domination/Tonelli rather than false conditional independence. The scaling `Y=KX` gives exactly the factor `K^2/s`.

Thus the standalone theorem

` s_9(A)>=s > 0  =>  ||p_Q||_infinity <= 400 K^2/s`

survives this review. This report's main new review obligation is the later `s_8` assembly.

## 3. The multiplicity-eight candidate closes end to end

Normalize `K=s=1`. Use the later `eta=1/100` pivot split of the `s_8` reduction.

### 3.1 Scalar and pair pivots are already paid under `s_8`

If `|A_ii|>=eta`, the scalar-square profile gives

`||p_Q||_infinity <= eta^{-1/2} sup_a E|R-a|^{-1/2}`.

The Schur complement loses at most one spectral direction, so `s_7(R_quad)>=1`, hence in particular the proved five-direction full half-potential proposition applies. Its three bounds satisfy

`H_5 < max(70,80,1+4*(142/5)) = 573/5 = 114.6`,

so the scalar-pivot branch is `<1146`.

If a principal two-coordinate determinant has modulus at least `eta`, a definite pair gives `<40`. In the indefinite case the two-coordinate Schur complement retains at least six unit directions. The hyperbolic envelope plus the quarter-power logarithmic-potential bound gives, using `log 16<14/5`, `L_0<54/5` and `1/e<1/2`,

`||p_Q||_infinity < 10*(6+14/5+54/5)+1/2 = 393/2 <197`.

Therefore every pivot branch is far below the eventual constant `2400`.

### 3.2 Exact no-pivot terminal dichotomy

Assume no `eta`-pivot and `s_8(A)>=1`. The B04 theorem proves either

`V_3(A)>=kappa^3`, `kappa=1/6400`,

or the order-two terminal collar.

In the first branch, a fair literal coordinate cut carries crossing third volume at least `4^-3 kappa^3`; the completed marginal-free order-three receiver has constant `C_3<15`, hence

`||p_Q||_infinity < 15*(kappa^3/64)^(-1/6)=2400`,

and this branch has a continuous `C_0` density.

For the collar branch, the sampled-seed construction has good seeds with error norm

`epsilon <= epsilon_* = 3 sqrt(2)/80`.

Here the designated fleet04/B08 result is applied at an actual inequality. That partner independently verified the two completion ranks `rank R<=3r` and `rank R[L,L]<=r`. At `r=2`,

`rank R<=6`.

Consequently, for each good seed,

` s_8(D+R) >= 1-epsilon`

and the rank-shift inequality gives

`boxed: s_2(D) >= 1-epsilon`.

This is the exact quantitative step that creates the two large physical interpolation defects used by the collar and robust-anchor reductions.

### 3.3 Robust pair exists at dimension-free scale

The B17 aggregation argument converts the good-seed two-sided collar into one literal original-coordinate pair `H`, writing

`C=A[H,H^c]`,

such that

`g:=det(CC^T) >= delta_*^2/2`,

where

`delta_* = 97/100-(297 sqrt(2)+3 sqrt(202))/4000`.

The aggregation is valid: if `D_H=sum_U det A[H,U]^2`, then `sum_H D_H=V_2`; the assigned good-seed masses `w_H` satisfy `sum_H w_H>=V_2/2`; for one positive `D_H`, `w_H>=D_H/2`; and the two-sided collar gives `delta_*^2 w_H<=D_H^2`. Hence `D_H>=delta_*^2/2` without paying any individual tiny seed determinant.

For later exact arithmetic, `sqrt(2)<3/2` and `sqrt(202)<15` give

`delta_* > 6779/8000 > 4/5`,

so already

`boxed: g>8/25`.

### 3.4 One-high leverage states are paid

Let

`Q_C=C^T(CC^T)^(-1)C`, `q_i=(Q_C)_ii`, `P=I-Q_C`,

and let `J={i:q_i>2/3}`. Since `Q_C` is a rank-two projection, `|J|<=2`.

The B20 theorem proves that if `|J|<=1`, the product-usable disjoint incident third-volume satisfies

`W_dis > g/48`.

Its proof is sound. For low-leverage rows `p_i=P_ii>=1/3`, the exact anchored-minor identity gives an interpolation error `E` with

`||E||_F^2 <= 3 W_dis/g`.

Assuming `W_dis<=g/48` gives `||E||_F<=1/4`. The residual matrix has global rank at most `4+|J|<=5` and restricted low-row rank at most two. From `s_8(A)>=1`, rank perturbation forces at least three low diagonal coefficients of modulus at least `3/4`. On those three physical coordinates,

`|R_ii|>=0.74`,

while every off-diagonal entry is `<sqrt(eta^2+eta)+1/4`, so each two-entry off-diagonal row sum is `<0.701`. Strict diagonal dominance makes a rank-three restricted block, contradicting the restricted rank-two bound. Hence `W_dis>g/48`.

The fleet01/B19 product-safe receiver then gives

`||p_Q||_infinity <= C_inc W_dis^(-1/6)`,

`C_inc=3*2^(5/6)*e^(2/3)`,

with a continuous `C_0` density. Using the exact weaker bound `g>8/25`, already `W_dis>1/150`; the sharper source constant gives `<23.48`.

### 3.5 The apparent two-high endpoint is empty

It remains only to exclude `|J|=2`. Let `J={i,j}`. For each complement pair `{a,b}`, define

`w_ab = det(C_{ab})^2/g`.

After normalizing `C` by `(CC^T)^(-1/2)`, Cauchy--Binet gives

`sum_{a<b} w_ab=1`,

and the rank-two determinantal marginal identity gives

`q_i=sum_{b!=i} w_ib`.

Therefore

`w_ij >= q_i+q_j-1 >1/3`,

so

`det(C_{ij})^2 > g/3 > 8/75`.                                    (3.1)

But no `eta`-pivot implies for every distinct physical `u,v`

`|A_uv|^2 < eta^2+eta =101/10000`.

All four entries of `C_{ij}` are such off-diagonal physical coefficients, hence

`|det C_{ij}| < 2(101/10000)=101/5000`,

and therefore

`det(C_{ij})^2 < 10201/25000000`.                                (3.2)

The exact rational comparison

`8/75 > 10201/25000000`

contradicts (3.1)-(3.2) by a factor greater than 261. Thus the two-high branch is impossible. This version avoids relying on floating-point evaluation of `delta_*`.

### 3.6 Assembly and scaling

The normalized cases are exhaustive:

1. scalar pivot: `<1146`;
2. definite/indefinite pair pivot: `<197` (definite actually `<40`);
3. no pivot with large third volume: `<2400`, `C_0`;
4. no-pivot terminal collar: the robust pair exists, the two-high state is impossible, hence `|J|<=1`, so the incident-volume receiver gives `<23.48`, `C_0`.

Therefore the reviewed candidate proves

`boxed: s_8(A)>=s>0 => ||p_(X^TAX+b^TX+c)||_infinity < 2400 K^2/s.`

The usual scaling `Y=KX`, `A -> A/s` preserves the cap-one product structure and restores `K^2/s` exactly.

The candidate proves essential boundedness for all branches. It does **not** prove a globally continuous representative because the pivot branches are domination arguments; continuity is separately established on the two no-pivot Fourier branches.

## 4. Exact checker

A deterministic arithmetic checker for the rational margins used above was run. It returned:

- `delta_lower = 6779/8000 = 0.847375 > 4/5`;
- `g_lower = 8/25 = 0.32`;
- two-high determinant lower bound `8/75 = 0.106666...`;
- no-pivot cross-minor upper bound `10201/25000000 = 0.00040804`;
- contradiction margin ratio `>261.41`;
- five-direction half-potential safe bound `573/5 =114.6`, scalar outer bound `1146`;
- indefinite-pair safe bound `393/2 =196.5`;
- robust-pair disjoint-volume weaker exact bound `W_dis>1/150`.

These are checks of exact displayed arithmetic, not numerical evidence for the theorem.

## 5. Review status and next obligation

I found no missing sign case, affine-term restriction, support/moment hypothesis, post-rotation independence, or unproved density-cap transfer in the assembled `s_8` chain. The recent B20 theorem and the final two-high exclusion fit the B04/B17 hypotheses exactly.

Accordingly this run records **one independent end-to-end PASS review** of `QFORM-FIXED-MULTIPLICITY-8-v1`. I do not promote it to independently validated status here: under the owner protocol one further genuinely separate complete review of the same full chain is still required.

If that second review passes, the next fixed-multiplicity target is `s_7`. The current `s_8` proof spends two large interpolation defects after a rank-six completion; starting at seven removes exactly one unit of that diagonal-defect budget, so lowering to seven requires a genuinely new structural mechanism rather than another tightening of the same rank constants.

The unrestricted three-eigenvalue conjecture remains OPEN, and no counterexample was produced.
