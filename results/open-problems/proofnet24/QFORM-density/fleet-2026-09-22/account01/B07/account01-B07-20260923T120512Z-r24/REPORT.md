SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T12:05:12Z.
attacking: the near-singular fixed double-pair determinant bank — extract physical two-star currency without rotating the product law, then compile it to R1/R2/H3 and a fifth-volume payment.

# account01/B07 r24 — a near-singular double-pair core forces physical two-star currency, then R1/R2/H3

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / GEOMETRY  
Run: `account01-B07-20260923T120512Z-r24`  
Status: `ESSENTIAL_STEP_APPLIED / NEW DOUBLEPAIR SINGULAR-VALUE STAR COMPILER / COMPLETED PARTNER PAIRTAIL APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

## 1. Exact target and source boundary

The target is unchanged: for every dimension, independent real ORIGINAL-coordinate inputs `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with a universal essential-supremum bound, or give a target-valid counterexample. No Gaussianity, moments, compact/connected support, log-concavity, iid assumption, or independence after spectral rotation is used. Continuity remains a separate desired conclusion.

The final pre-publication control refresh retained OWNER CONTROL revision `2026-09-22.15`, QFORM-only, with no B07 pause. The live correction inbox was reread. In particular, this run does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, positive moments of conditional projection density, naive fiber-sup integration, deletion of a small nonzero quadratic tail, or a one-good-minor claim.

The principal sources actually used are:

1. Own preceding aggregate theorem: `yspennstate/math-open-problems@bcecea864b0c99b14a47665b87f9c9ea6fde4b41`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T110318Z-r23/REPORT.md`. It proves the fixed-double-pair extension identity and aggregate physical-edge extraction.
2. Completed designated partner account02/B07: `yspennstate/math-open-problems@3e36370502df5afeb00457b74d05cdbfd87168b0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T104812Z-account02-B07-qform-r13/REPORT.md`. Its `QFORM-PAIRTAIL-CURVATURE-RECEIVER-v1` is applied below to an actual physical principal-pair inequality.
3. Account03/B07 curvature compiler: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T104247Z-account03-B07-qform-r32/REPORT.md` on current master. Its deterministic `QFORM-TWOSTAR-CURVATURE-E2-OR-R1-v1` and anchored-H3 lift are applied after this run converts coefficient singular vectors back to actual physical stars.
4. Completed determinant-volume theorem D5: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, path `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. It gives `||p_Q||_infinity <= 5 sqrt(2e) E_5^{-1/10}` for a physical cross block, with no marginal condition.

The current account02/B07 11:38Z checkpoint independently found the same elementary-symmetric rank-four/fifth-volume ladder used in Section 6 below. It is a live checkpoint, not used as a completed premise; the derivation is reproduced here.

## 2. Input from the preceding run: exact double-pair extension bank

Let `M` be a physical ORIGINAL-coordinate cross block between disjoint row and column banks, and fix two physical row anchors and two physical column anchors. After physical permutations only,

`M = [[B,U],[V,D]],`                                                (2.1)

where `B` is `2 x 2`. Let

`H := sum_(k,l) det M[P union {k}, Q union {l}]^2`                    (2.2)

be the complete squared third-minor mass extending the fixed anchor pair by one residual physical row and one residual physical column. The preceding run proves exactly

`H = || (det B) D - V adj(B) U ||_F^2`.                              (2.3)

Put

`F=||M||_F`.                                                         (2.4)

It also proves

`||B||_F >= 2 sqrt(H)/F^2`,                                         (2.5)

hence some physical edge in `B` has magnitude at least `sqrt(H)/F^2`. No individual third-order minor has been selected or reciprocated.

The new question is what the same aggregate bank says when the fixed `2 x 2` cross anchor `B` is nearly singular. A direct Schur inversion would be exactly the wrong operation; the point is to spend the determinant bank before any division by `det B`.

## 3. Main new theorem: near-singular anchor forces two physical stars

Let

`s_1 >= s_2 >= 0`                                                   (3.1)

be the singular values of the physical `2 x 2` anchor `B`. Since `adj(B)` has the same two singular values, choose unit vectors `p,q in R^2` so that

`adj(B) = s_1 p q^T + E`,                                           (3.2)

with

`||E||_op = s_2`.                                                    (3.3)

This is only a coefficient-space singular-value decomposition. It is not a rotation of the random coordinates, and no probability assertion is made in this basis.

From (2.3),

`sqrt(H)
 <= |det B| ||D||_F + ||V adj(B) U||_F
 <= s_1 s_2 ||D||_F
    + s_1 ||V p||_2 ||q^T U||_2
    + s_2 ||V||_F ||U||_F.`                                         (3.4)

Write

`d=||D||_F, u=||U||_F, v=||V||_F`.                                 (3.5)

Since `s_1<=||B||_F`,

`s_1 d + uv
 <= (||B||_F^2+d^2)/2 + (u^2+v^2)/2
 = F^2/2`.                                                          (3.6)

Therefore

`boxed:
 s_1 ||Vp||_2 ||q^T U||_2
 >= sqrt(H) - (s_2 F^2)/2.`                                         (3.7)

This immediately gives an exhaustive aggregate alternative.

### Theorem 3.1 — `QFORM-DOUBLEPAIR-SINGULARVALUE-STAR-COMPILER-v1`

For every fixed-double-pair bank `H>0`, exactly one of the following two quantitative regimes occurs.

**NS (quantitatively nonsingular cross anchor):**

`s_2 > sqrt(H)/F^2`.                                                (3.8)

Then (2.5) and `s_1>=||B||_F/sqrt(2)` give

`boxed: s_1 >= sqrt(2H)/F^2,`                                      (3.9)
`boxed: sigma_min(B)=s_2 > sqrt(H)/F^2,`                            (3.10)
`boxed: |det B|=s_1s_2 > sqrt(2) H/F^4.`                            (3.11)

Thus the whole physical `2 x 2` cross anchor is quantitatively nonsingular on the determinant-bank scale.

**SS (near-singular cross anchor):**

`s_2 <= sqrt(H)/F^2`.                                               (3.12)

Then (3.7) yields

`s_1 ||Vp||_2 ||q^T U||_2 >= sqrt(H)/2.`                            (3.13)

Although `p,q` need not be physical coordinate vectors, there are actual physical anchor column `j` and actual physical anchor row `k` for which

`||V e_j||_2 >= ||Vp||_2/sqrt(2),`                                 (3.14)
`||e_k^T U||_2 >= ||q^T U||_2/sqrt(2)`.                            (3.15)

Indeed `||Vp||<=||V||_F<=sqrt(2) max_j||Ve_j||`, and similarly for `U`. Define the corresponding ORIGINAL-coordinate physical stars

`c := V e_j`, `r := e_k^T U`.                                      (3.16)

Then

`boxed:
 s_1 ||r||_2 ||c||_2 >= sqrt(H)/4.`                               (3.17)

Since `s_1<=F`, the star product satisfies the dimension-free lower bound

`boxed:
 P_*:=||r||_2||c||_2 >= sqrt(H)/(4F).`                             (3.18)

This is the main new coordinate-selection statement. A near-singular determinant-carrying `2 x 2` core cannot lose its third-volume bank: after the coefficient-space singular direction is converted back to one of the two actual physical rows and one of the two actual physical columns, a genuine two-star product survives at the natural scale. No independent random variables were rotated.

### Exact singular face

If `s_2=0`, (3.7) is exact enough to recover the preceding run's factorization. For rank-one `B=sab^T`,

`H=s^2 ||Vb_perp||_2^2 ||a_perp^T U||_2^2`.                         (3.19)

Theorem 3.1 is therefore a stable quantitative version of the exact singular-anchor identity.

## 4. Convert the physical two-star reserve to R1 / R2 / anchored H3

Remain in the SS branch and use the physical row `k` and physical column `j` from (3.14)-(3.16). Let their scalar intersection be

`b=B_kj`.                                                           (4.1)

Using the same residual original-coordinate banks as in (2.1), form the literal physical subblock

`N = [[b,r^T],[c,D]].`                                              (4.2)

Its row-coordinate bank and column-coordinate bank remain disjoint, so every determinant below is an actual original-coordinate cross minor. Put

`P=P_*=||r||_2||c||_2`.                                            (4.3)

The account03/B07 deterministic curvature theorem applies to this actual block. Define the incident Schur-numerator matrix

`K=bD-cr^T`.                                                        (4.4)

Then either

`||K||_F^2 >= P^2/9`,                                              (4.5)

or

`dist_F(N, rank<=1) < (1/2)||N||_F`.                               (4.6)

By (3.18), the incident second-volume branch has the explicit bank lower bound

`boxed:
 ||K||_F^2 >= H/(144 F^2).`                                       (4.7)

This is already a nontrivial determinant-weighted coordinate-minor conclusion: the third-volume bank has descended to a complete incident `2 x 2` minor bank rather than one selected pivot.

If (4.5) holds, let

`T_2(N)=dist_F(N,rank<=2)^2`.                                      (4.8)

The same account03/B07 theorem gives the next exhaustive split. If

`T_2(N)<P/9`,                                                      (4.9)

then

`dist_F(N,rank<=2)<||N||_F/3`.                                    (4.10)

Otherwise the same physical row and column anchors carry a squared third-minor packet `W` satisfying

`W >= (1/2) T_2(N) ||K||_F^2
   >= P^3/162.`                                                    (4.11)

Using (3.18),

`boxed:
 W >= H^(3/2)/(10368 F^3).`                                       (4.12)

Thus the near-singular double-pair branch has been converted, with no reciprocal determinant, into one of three explicit physical outcomes:

`R1: dist_F(N,rank<=1)<||N||_F/2`,                               (4.13)

`R2: dist_F(N,rank<=2)<||N||_F/3`,                               (4.14)

or

`H3: W >= H^(3/2)/(10368 F^3)`.                                  (4.15)

The nonzero tails in R1/R2 are retained; they are not discarded as perturbations.

## 5. Actual application of the completed designated partner account02/B07 theorem

The completed account02/B07 r13 theorem is used here as an independent paid exit for the same aggregate bank. From the preceding r23 theorem, the complete `H` bank forces an actual physical edge `beta=A_rs` with

`|beta| >= sqrt(H)/F^2`.                                          (5.1)

Consider the actual symmetric principal pair on these original coordinates,

`P_beta=[[A_rr,beta],[beta,A_ss]].`                               (5.2)

If both diagonals have magnitude `<|beta|/2`, then the pair is indefinite and

`|det P_beta| >= 3 beta^2/4`,                                    (5.3)
`sigma_min(P_beta) >= |beta|/2`.                                 (5.4)

Let `C` be any inherited disjoint physical cross block in the exact pair Schur remainder. The completed designated-partner receiver gives

`||p_Q||_infinity
 <=26.00795741955
   |det P_beta|^(-2/5)
   sigma_min(P_beta)^(-1/10)
   T_2(C)^(-1/20).`                                               (5.5)

Hence whenever

`T_2(C)>=tau beta^2`,                                             (5.6)

(5.1), (5.3), and (5.4) imply the actual inequality

`boxed:
 ||p_Q||_infinity
 <=31.274095 tau^(-1/20) F^2/sqrt(H).`                           (5.7)

This is a genuine current-run application of the designated partner's completed theorem: the input is the physical edge forced by the entire double-pair determinant bank, not an assumed or selected good minor. It retains arbitrary same-bank curvature, affine terms, outside couplings, and extra spectrum. The cited partner theorem establishes essential boundedness in this scope; continuity is not promoted here.

If (5.6) fails, the exact retained conclusion is the nonzero rank-two Schur tube

`T_2(C)<tau beta^2`.                                             (5.8)

If one of the principal-pair diagonals has magnitude at least `|beta|/2`, this branch remains a separate scalar-pivot obligation. Thus Section 5 does not falsely declare the whole `H` bank paid; it records the exact partner-paid subbranch.

## 6. Spend the H3 branch by a fifth-volume ladder or retain a rank-four tube

Now take the actual physical block `N` in the H3 outcome (4.15). Write its squared singular values as nonnegative numbers `lambda_1>=lambda_2>=...`, and set

`E_k=e_k(lambda)`,
`T_k=sum_(j>k) lambda_j=dist_F(N,rank<=k)^2`.                    (6.1)

For every `k`,

`(k+1)E_(k+1)
 = sum_(|I|=k) (prod_(i in I)lambda_i) sum_(j notin I)lambda_j.`  (6.2)

For each `I` of size `k`, the complement sum is at least `T_k`, because deleting any `k` eigenvalues removes at most the `k` largest. Therefore

`boxed: T_k E_k <= (k+1)E_(k+1).`                               (6.3)

At `k=3,4`,

`E_5 >= (T_3 T_4/20) E_3 >= (T_4^2/20) E_3`.                   (6.4)

Since the anchored packet is a subpacket of all third minors,

`E_3>=W`.                                                        (6.5)

Let `a=W^(1/6)`. If

`T_4 >= a^2/16 = W^(1/3)/16`,                                  (6.6)

then

`E_5 >= W^(5/3)/5120`.                                         (6.7)

Apply the completed D5 theorem to this actual original-coordinate cross block. It yields a continuous full-ambient density with

`||p_Q||_infinity
 <=5 sqrt(2e) E_5^(-1/10)
 <=5 sqrt(2e) 5120^(1/10) W^(-1/6)
 <27.388 W^(-1/6).`                                             (6.8)

Using the lower bound (4.12),

`boxed:
 ||p_Q||_infinity
 <127.892 F^(1/2) H^(-1/4).`                                   (6.9)

If the rank-four-tail condition (6.6) fails, no perturbative deletion is made; the exact residual statement is

`boxed:
 dist_F(N,rank<=4)<W^(1/6)/4.`                                 (6.10)

Thus the H3 currency is converted to an already-paid continuous-density D5 branch or a genuine nonzero rank-four tube at the packet's own natural volume scale.

If the inherited double-pair bank has the scale `H>=cF^6`, then (6.9) has the correct homogeneity

`||p_Q||_infinity <127.892 c^(-1/4) F^(-1).`                    (6.11)

No universal lower bound on `F` is asserted.

## 7. Combined structural conclusion

### Theorem 7.1 — `QFORM-DOUBLEPAIR-NEARSINGULAR-TO-R1-R2-H3-D5-v1`

Let a physical original-coordinate cross block `M` carry a fixed two-row/two-column anchored third-volume bank `H>0`, and put `F=||M||_F`. Let `B` be the fixed physical `2 x 2` anchor core.

Then either:

1. `sigma_min(B)>sqrt(H)/F^2` and `|det B|>sqrt(2)H/F^4`; or
2. there exist one actual physical row anchor and one actual physical column anchor such that their two residual star vectors have product at least `sqrt(H)/(4F)`, and the corresponding actual physical subblock `N` satisfies one of:
   - `dist_F(N,rank<=1)<||N||_F/2`;
   - `dist_F(N,rank<=2)<||N||_F/3`;
   - an anchored H3 packet `W>=H^(3/2)/(10368F^3)`.

In the H3 alternative, either D5 pays the full ambient form continuously by (6.9), or the same actual physical block lies in the explicit rank-four tube (6.10).

Independently, the complete bank forces a physical edge, and the completed designated-partner account02/B07 theorem pays the conditioned-indefinite / nontrivial-tail principal-pair branch by (5.7).

The theorem tracks determinant weights through conditioning and never claims that one tiny principal minor is uniformly good. Coefficient singular vectors are used only to prove a norm inequality; before probability enters, they are converted back to an actual physical row and column by (3.14)-(3.16).

## 8. What is still unpaid

Full QFORM remains OPEN, and the full continuity conclusion remains OPEN.

The first B07 debt after this run is now substantially narrower:

`QFORM-DOUBLEPAIR-LOWRANK-TUBE-RECEIVER-v1`:

spend the `R1`, `R2`, or rank-four-tube survivors above while retaining the actual nonzero tail, arbitrary same-bank curvature, and original-coordinate product provenance. On the separate physical-edge route, also pay the large-diagonal / low-`T_2` Schur branch without treating the residual quadratic tail as harmless.

A promising next exact move is to combine the scalar square-peel with the orientation-free rank-two affine half-Riesz theorem only after proving that the post-pivot quadratic remainder has a quantitative rank-two determinant currency. The current results do not yet supply that implication, so it is not claimed.

## 9. Verification

A direct random-matrix regression check of (3.7) was run on 10,000 random blocks of residual sizes 1 through 7 and found zero violations. The analytic proof is (3.4)-(3.7); the finite computation is only a regression aid. The constants used in (6.9) are

`10368^(1/6)=4.669630297356063`,
`6*10368^(1/6)=28.01778178413638`,
`27.388*10368^(1/6)=127.89183458398786`.

No Monte Carlo or histogram is used as evidence for a density theorem.
