# account01/B06 r49 — exact singular-P1 row compiler

**Run:** `20260924T063803Z-account01-B06-QFORM-r49`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`, OWNER CONTROL `2026-09-22.15`  
**Assignment:** curved fiber integration  
**Status:** new supporting analytic theorem and direct designated-partner application; full unrestricted QFORM remains OPEN; global continuity remains OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (repository retrieval/publication occurred, but no native learned-memory receiver use was verified)

## 0. Exact target and source discipline

The target remains: for every `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with a universal `L^infinity` bound, or give a valid counterexample. No moment, support, Gaussian, log-concavity, compactness, connected-support, or diagonal-basis assumption is introduced. Rotating the input coordinates is never used as an independence-preserving operation.

Fresh control was read from `yspennstate/math-research-brain` main. The protected `scheduled_tasks/README.md` blob remained `14046b5138615be52bb1c49a998122a7c84e200e`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only. The live `CLAIMS.json` still marks both the full bounded-density theorem and the global continuous-density conclusion OPEN. The live correction inbox was refreshed before publication. In particular, this run does not use pointwise van-der-Corput decay, arbitrary-joint coarea, post-rotation independence, or unrestricted fiber suprema.

Immediate predecessor: account01/B06 r48, canonical mathematics `yspennstate/math-open-problems@abcdb34fb8b6994835f829536f058701b2a65fea`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260924T060138Z-account01-B06-QFORM-r48/REPORT.md`. Its theorem `QFORM-RANK1-PHYSICAL-PAIR-TRANSVERSE-SLOPE-v1` states that for a literal original-coordinate physical pair with rank-one quadratic block `P=theta vv^T`, null unit vector `w`, and complete complement cross vector `q=A[J,J^c]^T w`, one has

`||p_Q||_infinity <= C_par (|theta| ||q||_2)^(-1/2)`,

where

`C_par = 2^(13/4) e^(1/4) = 12.215777290955165...`,

with completely arbitrary same-complement quadratic curvature retained.

Designated partner actually applied below: account02/B06 r13, canonical mathematics `yspennstate/math-open-problems@bc7c60dbcb335ba3b18748816a62b026dc8ef4ab`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/account02-B06-20260924T052646Z-auto11-r13/REPORT.md`. In its three-hub normal form it proves the complete P1 mixed-minor aggregate

`Lambda_1 = sum_h ||R_h||_2^2 = beta^2 tr(adj(N) G adj(N)^T)`

and, with `mu=sigma_min(N)`, the quantitative inequality

`Lambda_1 >= |beta| mu^4 P_1`.

On its live branch `P_1>5P/16`, therefore

`Lambda_1 > (5/16)|beta| mu^4 P`.                                            (0.1)

The same partner report shows that P1 can be large while every literal two-hub principal pair is singular. This run pays that exact-singular endpoint rather than trying to infer an invertible pair.

## 1. Setup: one P1 row and a singular physical pair

Let the three literal hub coordinates be `H={1,2,3}` and let `T` be the disjoint original-coordinate tail bank. Write

`K=A[H,H]`.

Fix `h in H`, set `J=H\{h}`, and define the literal physical pair block

`P_h=K[J,J]`.

For every tail coordinate `p in T`, let `R_h(p)` denote the oriented `3x3` mixed minor using the two hub columns in `J` and the tail column `p`, with all three hub rows. Up to one fixed sign depending only on the column order,

`R_h(p)=det A[H, J union {p}]`.

Let

`R_h=(R_h(p))_{p in T}`,  `rho_h=||R_h||_2`.

Assume in this section that `P_h` has rank exactly one. Let its nonzero eigenvalue be `theta_h` and choose orthonormal vectors `v_h,w_h` in `R^2` so that

`P_h=theta_h v_h v_h^T`,   `P_h w_h=0`.

Write

`c_h=K[J,h] in R^2`,
`M_h=A[J,T] in R^{2 x |T|}`,
`a_h=w_h^T c_h`,
`n_h=M_h^T w_h in R^{|T|}`.

The complete complement cross vector from the physical-pair null direction is

`q_h=A[J,J^c]^T w_h = (a_h,n_h)`,

where `J^c={h} union T`, hence

`||q_h||_2^2 = a_h^2+||n_h||_2^2`.                              (1.1)

All variables in `J` and `J^c` are still literal disjoint banks of original independent coordinates.

## 2. Exact singular-row factorization

### Theorem 2.1 — `QFORM-P1-SINGULAR-ROW-FACTORIZATION-v1`

If `rank P_h=1`, then for every tail coordinate `p`,

`boxed: R_h(p) = +/- theta_h a_h (n_h)_p`,                       (2.1)

and therefore

`boxed: rho_h = |theta_h| |a_h| ||n_h||_2`.                     (2.2)

Moreover the full literal hub determinant satisfies

`boxed: det K = -theta_h a_h^2`.                                (2.3)

Consequently, whenever `rho_h>0`, the hub triple is automatically nonsingular and

`boxed:
 (|theta_h| ||q_h||_2)^2
 = |theta_h| [ |det K| + rho_h^2/|det K| ].`                    (2.4)

In particular, by AM-GM,

`boxed: |theta_h| ||q_h||_2 >= sqrt(2 |theta_h| rho_h).`         (2.5)

#### Proof

Order the two rows indexed by `J` first and the remaining hub row `h` last; order the two columns `J` first and the tail column `p` last. The mixed `3x3` block is

`[[ P_h,             M_h[:,p] ],
  [ c_h^T,           A[h,p]    ]]`.

For every `2x2` matrix `P`, vector columns `m,c`, and scalar `t`,

`det [[P,m],[c^T,t]] = t det P - c^T adj(P)m`.                  (2.6)

Because `P_h` has eigenvalues `theta_h,0`, its adjugate is exactly

`adj(P_h)=theta_h w_h w_h^T`.                                  (2.7)

Since `det P_h=0`, (2.6)-(2.7) give

`R_h(p)=+/-[-theta_h (c_h^T w_h)(w_h^T M_h[:,p])]`,

which is (2.1); squaring and summing over `p` proves (2.2).

Apply the same block determinant identity to the literal hub block

`K=[[P_h,c_h],[c_h^T,K_hh]]`.

Again `det P_h=0`, hence

`det K = -c_h^T adj(P_h)c_h = -theta_h a_h^2`,

which is (2.3).

When `rho_h>0`, both `a_h` and `||n_h||` are nonzero, so `det K!=0`. Put `d=|det K|=|theta_h|a_h^2`. From (2.2),

`rho_h^2 = |theta_h|^2 a_h^2 ||n_h||^2 = d |theta_h| ||n_h||^2`.

Thus

`|theta_h|^2 ||q_h||^2
 = |theta_h|^2 a_h^2 + |theta_h|^2||n_h||^2
 = |theta_h| d + |theta_h| rho_h^2/d`,

which is (2.4). Finally `d+rho_h^2/d >=2rho_h`, yielding (2.5). QED.

### Interpretation

Equation (2.1) is the singular analogue of account02/B06 r13's invertible-pair Schur identity `||R_h||=|det P_h| ||n_h||`. At rank loss, the Schur denominator disappears and is replaced by the exact product of two genuine null-direction cross slopes: one into the remaining hub and one into the complete tail bank. No inverse physical minor appears.

Equation (2.4) is a balanced curved-fiber identity: the complete null-direction cross norm is the geometric mean-compatible combination of the hub determinant and the full tail mixed-minor row. Taking a worst individual tail coefficient would lose this structure; summing `rho_h` first is essential.

## 3. Density payment of an exact singular P1 row

### Theorem 3.1 — `QFORM-P1-SINGULAR-PAIR-CURVED-RECEIVER-v1`

Under the preceding hypotheses, if `rho_h>0`, then the full ambient quadratic form has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_par [2 |theta_h| rho_h]^(-1/4).`                          (3.1)

Equivalently, retaining the exact hub determinant rather than AM-GM,

`boxed:
 ||p_Q||_infinity
 <= C_par
    { |theta_h| [ |det K| + rho_h^2/|det K| ] }^(-1/4).`        (3.2)

No assumption is made on any quadratic coefficient entirely inside the complement bank `J^c`; all same-bank curvature is retained.

#### Proof

Use the two literal original coordinates in `J` as the physical pair and all original coordinates in `J^c` as the disjoint complement bank. The pair block is rank one with nonzero eigenvalue `theta_h` and null direction `w_h`. Its complete null-direction cross vector is exactly `q_h` from (1.1).

Account01/B06 r48 `QFORM-RANK1-PHYSICAL-PAIR-TRANSVERSE-SLOPE-v1` therefore applies directly:

`||p_Q||_infinity <= C_par (|theta_h| ||q_h||)^(-1/2)`.          (3.3)

Insert the exact identity (2.4) to obtain (3.2), or the lower bound (2.5) to obtain (3.1). QED.

This is the missing exact-singularity endpoint for the P1 packet. The singularity of `P_h` is not treated as a limit of the logarithmic invertible-pair theorem; the proof changes geometry at rank loss and keeps the parabola/null-cross fiber exactly.

## 4. Direct application of the designated account02/B06 aggregate

Define the quantitative singular-row set

`S_kappa={ h : rank(P_h)=1 and |theta_h|>=kappa }`.

Let

`Lambda_sing(kappa)=sum_{h in S_kappa} rho_h^2`.

### Corollary 4.1 — aggregate exact-singular P1 payment

If `Lambda_sing(kappa)>0`, then

`boxed:
 ||p_Q||_infinity
 <= C_par 2^(-1/4) 3^(1/8)
    kappa^(-1/4) Lambda_sing(kappa)^(-1/8).`                    (4.1)

More generally, if `Lambda_sing(kappa)>=eta Lambda_1` for some `eta in (0,1]`, then

`boxed:
 ||p_Q||_infinity
 <= C_par 2^(-1/4) 3^(1/8)
    eta^(-1/8) kappa^(-1/4) Lambda_1^(-1/8).`                   (4.2)

The numerical front constant in (4.2), before `eta,kappa,Lambda_1`, is

`C_par 2^(-1/4)3^(1/8)=11.784299300938887...`.

#### Proof

There are at most three rows. Choose `h in S_kappa` with

`rho_h >= sqrt(Lambda_sing(kappa)/3)`.

Apply (3.1):

`||p_Q|| <= C_par [2 kappa rho_h]^(-1/4)
            <= C_par 2^(-1/4) 3^(1/8)
               kappa^(-1/4)Lambda_sing(kappa)^(-1/8)`.

This is (4.1); (4.2) follows immediately. QED.

Now apply the designated account02/B06 r13 inequality (0.1) at the actual P1-large equation. If the row carrying the maximal P1 energy is an exact rank-one physical pair with `|theta_h|>=kappa`, then `Lambda_sing(kappa)>=Lambda_1/3` is not needed: simply choose the maximal row, for which `rho_h>=sqrt(Lambda_1/3)`, and (3.1) gives

`||p_Q||_infinity
 <= C_par (2 kappa)^(-1/4)(Lambda_1/3)^(-1/8)`.

Using (0.1),

`boxed:
 ||p_Q||_infinity
 < C_par [ 12/(5 kappa^2 |beta| mu^4 P) ]^(1/8).`              (4.3)

Equivalently the numerical front constant after extracting the product currency is

`C_par (12/5)^(1/8)=13.628482837559169...`.

Thus **the account02/B06 P1 packet is now paid even when its selected literal pair is exactly singular**, provided the pair still carries a quantitative nonzero rank-one curvature. The former `sigma_min(P_h)>0` gate is no longer necessary at the singular endpoint.

## 5. The partner's exact counterexample is now paid by the singular receiver

Account02/B06 r13 exhibits

`K=[[1,1,1],[1,1,-1],[1,-1,1]]`,

with one tail column `z=e_1`, for which every literal `2x2` hub principal block is singular while

`P_1=4`, `Lambda_1=16`,

and the entire mixed-row energy is `rho_1=4`, `rho_2=rho_3=0`.

For `h=1`, the physical pair on hubs `{2,3}` is

`P_1=[[1,-1],[-1,1]]`,

whose nonzero eigenvalue is `theta_1=2`. Therefore Theorem 3.1 gives directly

`||p_Q||_infinity
 <= C_par [2*2*4]^(-1/4)
 = C_par/2
 = 6.1078886454775825... .`                                    (5.1)

This is a real target-level bound for the same ambient matrix that refuted the stronger claim `large P1 => some invertible physical pair`. No localized-triple rescue is required for this example: the exact singular pair itself carries the correct curved product geometry.

## 6. What remains unpaid

This run does **not** close the full P1 branch or the unrestricted QFORM conjecture.

The new exact-singular receiver plus account02/B06 r13 now covers:

1. quantitatively conditioned invertible physical pairs through r13's pair/logarithmic receiver;
2. exact rank-one singular physical pairs through Theorem 3.1 above;
3. the explicit all-pairs-singular P1 counterexample from r13.

The first local debt is now the **near-singular transition with vanishing rank-one curvature scale**, together with finite hub-metric degeneration:

`QFORM-P1-NEARSINGULAR-OR-SMALL-RANK1-CURVATURE-ROUTING-v1`.

Concretely, if the row carrying substantial `rho_h` has an invertible pair with very small `sigma_min(P_h)`, r13's current bound still deteriorates; if it is exactly rank one but `|theta_h|` is very small, (3.1) also deteriorates. A correct next step must use the other complement cross direction, a localized three-hub block, or a grouped higher-rank product receiver. It cannot infer a uniformly good physical pair from P1 alone, because r13 already supplied a valid counterexample to that structural shortcut.

The full arbitrary-dimensional QFORM conjecture remains OPEN. Global continuity remains OPEN; this run establishes essential boundedness only in the stated branch and makes no continuity claim.

## 7. Algebra check

A finite diagnostic script in this run directory samples random rank-one physical pairs and verifies the identities

`R_h(p)=-theta_h a_h (n_h)_p`,
`det K=-theta_h a_h^2`,

and the exact balance (2.4). The maximum discrepancies in 10,000 random trials were approximately `5.4e-15` for the mixed-minor factorization and `1.5e-14` for the hub determinant identity. The proof above is algebraic; the finite check is not evidence for the full conjecture.

## 8. Status

New theorem IDs:

- `QFORM-P1-SINGULAR-ROW-FACTORIZATION-v1`;
- `QFORM-P1-SINGULAR-PAIR-CURVED-RECEIVER-v1`;
- `QFORM-P1-EXACT-SINGULAR-AGGREGATE-PAYMENT-v1`.

Partner actually applied: account02/B06 r13, `QFORM-P1-MIXED-CROSSMINOR-AGGREGATE-v1` / `QFORM-P1-AGGREGATE-SURVIVAL-v1`, source `yspennstate/math-open-problems@bc7c60dbcb335ba3b18748816a62b026dc8ef4ab`.

Full target: **OPEN**.  
Continuous-density conclusion: **OPEN globally**.  
Execution: **WITHOUT_VERIFIED_BRAIN**.
