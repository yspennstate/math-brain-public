# fleet01/B20 QFORM r11 — physical rank-one × rank-two cascade from the O0 heavy packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T171840Z-fleet01-B20-QFORM-r11`  
**Owner control:** revision `2026-09-22.8`  
**Assignment:** Proof closure and keeper  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL IMPLICATION PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The target remains the full arbitrary-law statement: for every finite dimension, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric matrix `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal finite constant, or give a target-valid counterexample. Continuity is tracked separately.

No Gaussian, moment, iid, compact-support, log-concavity, or post-rotation independence assumption is introduced. The live corrections are retained, in particular: there is no law-uniform pointwise quadratic Fresnel decay; a generic conditional three-dimensional spectral density cap is false; one good physical minor cannot be extracted with a dimension-free reciprocal-minor payment; and rotating a bank does not preserve independence of its coordinates.

## 2. Completed fleet02/B20 result actually consumed

The required partner source is fleet02/B20 run `20260922T165822Z-fleet02-B20-QFORM-r13`, canonical report

`yspennstate/math-open-problems@ccd703b260df4eca8b539b6614e2cecdad3e7465`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260922T165822Z-fleet02-B20-QFORM-r13/REPORT.md`.

In the O0 cross-cut branch it has a physical cross block `B=A[L,R]`, `M=BB^T`, and `E_3=e_3(M)>=1/256`. At the calibrated ridge scale `tr K=8/3`, if a physical row `i in L` is heavy, `K_ii>1/2`, its theorem `QFORM-O0-DPP-HEAVY-THIRD-MASS-v1` proves

`E_3(i)/E_3>1/48`, hence

`E_3(i)>1/12288`.                                                    (2.1)

Its second theorem colors `L\{i}` into `L1,L2` and `R` into `R1,R2,R3`, preserving one ninth of the relevant third-minor mass. Thus there is a source-realizable six-block packet

`P := sum_{j in L1,k in L2}`
`     sum_{a in R1,b in R2,c in R3}`
`     det B[{i,j,k},{a,b,c}]^2`

with

`P>1/110592`.                                                        (2.2)

The partner identified the next method as an aggregate expansion relative to the singleton row. The present run carries that expansion out and converts (2.2) into a scale-invariant physical rank-one × rank-two reserve without selecting a coordinate or rotating a random-variable bank.

## 3. Exact algebraic Schur–Gram contraction

Before physicalizing the packet, it is useful to record the exact exterior identity behind (2.1).

Let `r=B[i,R]` be the heavy physical row, `s=||r||_2^2`, and for every other row `u_j=B[j,R]` let

`u_j^perp = u_j - <u_j,r> r/s`

when `s>0`. Equation (2.1) already implies `s>0`. Let `C_perp` be the matrix with rows `u_j^perp`, `j in L\{i}`. Then

`boxed( E_3(i) = s e_2(C_perp C_perp^T). )`                         (3.1)

Indeed, by Cauchy--Binet,

`E_3(i)=sum_{j<k} sum_{|T|=3} det B[{i,j,k},T]^2`
`      =sum_{j<k} ||r wedge u_j wedge u_k||_2^2`.

Orthogonal projection onto `r^perp` does not change `r wedge u_j wedge u_k`, and

`||r wedge u_j^perp wedge u_k^perp||_2^2`
` = ||r||_2^2 ||u_j^perp wedge u_k^perp||_2^2`.

Summing over row pairs gives (3.1), since the sum of squared two-row wedge norms is exactly `e_2(C_perp C_perp^T)`. Combining with (2.1),

`boxed( ||r||_2^2 e_2(C_perp C_perp^T) > 1/12288. )`               (3.2)

This is an exact algebraic rank-one × rank-two reserve. It is **not yet an analytic product-coordinate certificate**, because `C_perp` uses an orthogonal projection in the right-bank coordinate space. The next theorem obtains a weaker but completely physical version directly from the six-block packet.

## 4. Main new theorem — physical Laplace cascade

### Theorem `QFORM-O0-FIVEBANK-LAPLACE-CASCADE-v1`

Assume the six-block packet (2.2). For `q=1,2,3`, define the singleton-row bank energies

`s_q := sum_{a in R_q} B_{ia}^2`.                                  (4.1)

For distinct `p,r in {1,2,3}`, define the bank-separated two-minor mass

`T_{pr} := sum_{j in L1,k in L2}`
`          sum_{b in R_p,c in R_r}`
`          (B_{jb}B_{kc}-B_{jc}B_{kb})^2`.                         (4.2)

Then for some permutation `(q,p,r)` of `(1,2,3)`,

`boxed( s_q T_{pr} > 1/995328. )`                                  (4.3)

Consequently, if

`C_{pr}=B[L1 union L2, R_p union R_r]`,                             (4.4)

then all coordinate sets underlying `B[i,R_q]` and `C_{pr}` are disjoint original-coordinate banks and

`boxed( ||B[i,R_q]||_2^2 e_2(C_{pr}C_{pr}^T) > 1/995328. )`        (4.5)

In particular `C_{pr}` has rank at least two. No spectral rotation, no conditional projection, and no one-minor selection occurs.

### Proof

For fixed `j,k,a,b,c`, abbreviate

`D=det B[{i,j,k},{a,b,c}]`.

Laplace expansion along the singleton row gives

`D = B_{ia}(B_{jb}B_{kc}-B_{jc}B_{kb})`
`    -B_{ib}(B_{ja}B_{kc}-B_{jc}B_{ka})`
`    +B_{ic}(B_{ja}B_{kb}-B_{jb}B_{ka}).`                          (4.6)

By `(x+y+z)^2<=3(x^2+y^2+z^2)`,

`D^2 <= 3(X^2+Y^2+Z^2)`,                                           (4.7)

with the three terms corresponding to the three displayed cofactors. Sum (4.7) over `j in L1`, `k in L2`, `a in R1`, `b in R2`, `c in R3`. Because the index sets factor, the first total is exactly `s_1 T_23`, the second `s_2 T_13`, and the third `s_3 T_12`. Therefore

`P <= 3(s_1T_23+s_2T_13+s_3T_12)`.                                (4.8)

Since `P>1/110592`,

`s_1T_23+s_2T_13+s_3T_12 > 1/331776`.

At least one of the three terms is therefore greater than

`1/(3*331776)=1/995328`,

which proves (4.3).

Finally, by Cauchy--Binet,

`e_2(C_{pr}C_{pr}^T)`

is the sum of the squares of **all** `2x2` minors of `C_{pr}`. The quantity `T_{pr}` is only the sub-sum using one row from each of `L1,L2` and one column from each of `R_p,R_r`; hence

`e_2(C_{pr}C_{pr}^T)>=T_{pr}`.                                    (4.9)

Equations (4.3) and (4.9) give (4.5). QED.

## 5. A still more concrete disjoint matching-energy corollary

Put

`E_{alpha,beta}=||B[L_alpha,R_beta]||_F^2`,

for `alpha in {1,2}` and `beta in {1,2,3}`. For the permutation from Theorem 4,

`T_{pr}`
` <=2(E_{1p}E_{2r}+E_{1r}E_{2p})`,                                (5.1)

because `(xy-zw)^2<=2x^2y^2+2z^2w^2`, followed by summation and factorization. Combining (4.3) and (5.1), at least one of the two orientations satisfies

`boxed( s_q E_{1p}E_{2r} > 1/3981312 )`                            (5.2)

or the same statement with `p,r` interchanged. Thus the heavy O0 packet contains three pairwise-disjoint physical cross-energy banks whose **product**, rather than any individual coefficient, is dimension-free.

This is weaker than the determinant packet and is recorded only as a concrete interface. The stronger source-valid object is (4.5).

## 6. Why the aggregate product is the correct currency: a source-valid obstruction to one-edge extraction

The cascade cannot in general be sharpened to a fixed lower bound on one physical singleton edge or one physical `3x3` minor.

For any `m>=1`, take a `3 x (m+2)` cross matrix `B_m` with rows `i,j,k` and right banks

`R1={a_1,...,a_m}`, `R2={b}`, `R3={c}`,

such that

`B_m[i,a_l]=m^(-1/2)` for every `l`,
`B_m[j,b]=1`,
`B_m[k,c]=1`,

and every other entry is zero. Then the three rows are orthonormal, so the nonzero singular values of `B_m` are exactly `1,1,1`. For every `l`,

`det B_m[{i,j,k},{a_l,b,c}] = m^(-1/2)`,

and therefore

`P_m=sum_l det(...)^2=1`.                                          (6.1)

Yet

`max_l |B_m[i,a_l]|=m^(-1/2)->0`,
`max_l det(...)^2=1/m->0`.                                        (6.2)

The symmetric cross form

`A_m=[[0,B_m],[B_m^T,0]]`

has eigenvalues `+1,+1,+1,-1,-1,-1` (and zeros if padded), so this coefficient geometry lies squarely inside the target spectral regime. It is not a counterexample to QFORM; it is a counterexample to any reduction that tries to replace the aggregate O0 packet by one uniformly large singleton edge or one uniformly large physical third minor.

For this family the physical cascade is exact: `s_1=1`, `T_23=1`. Hence the correct dimension-free quantity survives only after aggregation, exactly as in (4.3)--(4.5).

## 7. What this pays and what remains unpaid

The fleet02/B20 O0 ridge-heavy endpoint is no longer merely “one heavy ridge row plus a determinant packet.” It now has a source-valid nested form:

- one original physical singleton `i` and one disjoint original-coordinate bank `R_q` carry rank-one cross energy `s_q`;
- on four **other** disjoint original-coordinate banks, the cross block `C_{pr}` carries genuine rank-two exterior mass `e_2(C_{pr}C_{pr}^T)`;
- their scale-invariant product is bounded below by `1/995328`.

This is precisely the first algebraic implication needed by the partner's proposed singleton-row expansion. It also proves that the O0-heavy endpoint necessarily contains a second cross direction **away from the singleton bank**, at the bank/compound level, even when every individual coefficient or minor is tiny.

The full target is nevertheless still OPEN. The analytic payment still has to tolerate arbitrary self blocks, arbitrary cross-contamination among the six physical banks, and arbitrary affine terms produced by legitimate conditioning. One cannot condition on an orthogonal complement inside `R_q`, because that would destroy the original-coordinate product structure. Therefore the next unpaid theorem should be formulated directly at the physical-bank level, for example:

`QFORM-RANK1xRANK2-BANK-PAYMENT-v1` — if six disjoint original-coordinate banks satisfy

`||B[i,R_q]||_2^2 e_2(C_{pr}C_{pr}^T) >= c_0`

with `c_0=1/995328`, prove a dimension-free density bound for the full quadratic form with arbitrary self blocks/outside couplings, or route a fixed amount of this currency into an already-paid square-pivot/fractional-ridge, grouped-coordinate, or O1/O2/O3 endpoint.

A viable next attack is to calibrate a fractional-ridge scale on `C_{pr}`. In its diffuse regime the existing fractional-ridge theorem controls a half-Riesz potential below the direct density threshold; what is still missing is a dependence-safe **bank-level hyperbolic transducer** that spends the disjoint singleton-to-`R_q` energy without replacing `R_q` by a rotated scalar variable. In the heavy regime of `C_{pr}`, repeat the leverage-to-compound localization one level lower. This is now a sharply stated scale-invariant debt rather than an opaque five-bank packet.

The other overlap classes O1/O2/O3 remain separate full-target debts, exactly as in the partner report. No full-proof claim is made. Continuity is not claimed from the present structural result.

## 8. Keeper outcome and provenance scope

The account-local native inventory was checked before research. All twenty managed fleet01 slots B01--B20 were present as enabled hourly QFORM tasks with quiet notifications; no duplicate or missing authorized managed slot was found. Therefore no scheduler mutation and no mutation lease were needed. Missing worker check-ins, if any, are not treated as outages.

The active QFORM sign-in request was acknowledged by this run. Native assignment, worker check-in, and substantive mathematical completion are kept distinct.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN`. Provider usage counters: `UNKNOWN/null`, not zero. `full_brain_connected=false`; no claim of authenticated learned-memory ingestion is made.
