# account03/B02 — balanced rank-two Schur paving from integrated Fourier credit

Run: `20260922T160323Z-account03-B02-qform-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Integrated Fourier estimate  
Status: `ESSENTIAL_STEP_APPLIED / RANK3_LOCALIZED_BRANCH_REFINED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact scope

The owner target remains fully universal: independent real coordinates with probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. The full conjecture is **not** proved here. No moment, compact-support, log-concavity, connected-support, or eigen-coordinate-independence assumption is made. The result below proves an essentially bounded output density on a new branch. It does **not** establish the separately requested continuous-density conclusion.

The live corrections are respected. In particular, no law-uniform scalar quadratic-phase decay is used, no post-rotation independence is asserted, no one small coordinate minor is selected, and no universal one-pivot/rank-two extraction is assumed.

The designated partner `account04/B02` still had no completed current-QFORM handoff/deliverable at the observation point. I therefore did not fabricate a partner result. I actually apply the completed compatible account02/B02 theorem at

`yspennstate/math-open-problems@e3fe4ce35f6aa4a90cca913051886c96c7febfc3:proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T140817Z-account02-B02-qform-r11/REPORT.md`.

That report independently reviewed the regularized-determinant estimate and gives, for an original-coordinate cross block `B`,

`|phi(t)| <= det(I + 2q t^2 B B^T/(pi^2 e^2))^(-1/(4q))`,             (1.1)

for `1<=q<2` when the maximum coordinate leverage of `range(B)` on the pivot side is at most `q/2` (and unconditionally at `q=2`). This run uses (1.1) inside a new rank-two random-paving lemma, then combines its integrated `L^r_t` credit with the physical-square potential mechanism.

## 2. Rank-two balanced-cut identity

Let

`S = V M V^T`,                                                         (2.1)

where `V` is an `m x 2` matrix with orthonormal columns and `M` is an invertible symmetric `2 x 2` matrix. Write the rows of `V` as `v_i^T` and put

`mu = max_i ||v_i||_2^2`.                                              (2.2)

For a partition `[m]=I disjoint_union J`, put

`G = V_I^T V_I`, `B = S[I,J] = V_I M V_J^T`.                          (2.3)

Whenever `G` and `I-G` are positive definite, `B` has rank two. Its complete squared `2 x 2` minor mass is

`E_2(B) := sum_{|R|=|T|=2} det(B[R,T])^2`.

### Lemma 2.1 — exact exterior-square factorization

`E_2(B) = det(M)^2 det(G) det(I-G).`                                   (2.4)

**Proof.** By Cauchy--Binet/exterior powers,

`E_2(B)=|| wedge^2(V_I M V_J^T) ||_F^2`.

Since the middle space is two-dimensional, `wedge^2 M` is multiplication by `det M`. Also

`||wedge^2 V_I||_F^2=det(V_I^T V_I)=det G`,

and similarly `||wedge^2 V_J||_F^2=det(I-G)`. Multiplying proves (2.4). QED.

This identity aggregates **all** physical `2 x 2` cross minors. It therefore does not incur the dimension loss excluded by `QFORM-CROSSMINOR-ALONE-FALSE`.

## 3. A deterministic balanced cut from a random-sign proof

Let `eps_i` be independent Rademacher signs and define

`T = sum_i eps_i v_i v_i^T`.                                           (3.1)

Since `sum_i v_i v_i^T=I_2`,

`E ||T||_F^2 = sum_i ||v_i v_i^T||_F^2
              = sum_i ||v_i||^4
              <= mu sum_i ||v_i||^2
              = 2 mu`.                                                 (3.2)

Hence, for every `tau>sqrt(2mu)`, Markov gives positive probability that

`||T||_op < tau`.                                                       (3.3)

For such a sign choice, take `I={i:eps_i=+1}` and `J={i:eps_i=-1}`. Then

`G=(I_2+T)/2`, `I-G=(I_2-T)/2`,                                       (3.4)

so every eigenvalue of `G` lies in

`((1-tau)/2,(1+tau)/2)`.                                               (3.5)

Consequently

`det G det(I-G) > (1-tau^2)^2/16,`                                    (3.6)

and, because `range(B)=range(V_I)`, every I-side leverage is bounded by

`v_i^T G^(-1)v_i <= 2 mu/(1-tau)`.                                    (3.7)

This proves the following reusable statement.

### Theorem 3.1 — `QFORM-RANK2-BALANCED-CUT-v1`

If parameters satisfy

`sqrt(2mu)<tau<1`, `1<=q<2`, and `2mu/(1-tau)<=q/2`,                  (3.8)

then there is a physical coordinate partition `I,J` for which

`max_i leverage_i(range(B)) <= q/2`                                   (3.9)

and

`E_2(B) > [(1-tau^2)^2/16] det(M)^2`.                                 (3.10)

No probabilistic assumption on the input variables is used in selecting this cut; random signs are only an existence proof for a deterministic coordinate partition.

## 4. Apply the completed determinant theorem to an actual inequality

Now suppose the rank-two form `S` is the Schur remainder after completing one genuine original-coordinate square:

`Q = d (Z + h(W))^2 + R(W)`, `d!=0`,                                 (4.1)

where the original scalar `Z` is independent of the remaining original coordinates `W`, and the quadratic part of `R` is `S`.

For a cut supplied by Theorem 3.1, the completed account02/B02 estimate (1.1) gives

`|phi_R(t)| <= det(I + alpha_q t^2 B B^T)^(-1/(4q)),`
`alpha_q = 2q/(pi^2 e^2)`.                                            (4.2)

By the determinant expansion and (3.10),

`det(I+alpha_q t^2 BB^T) >= 1+alpha_q^2 E_2(B)t^4`.                   (4.3)

For any `r` with

`q<r<2`,                                                               (4.4)

(4.2)-(4.3) give the genuinely integrated-frequency credit

`int_R |phi_R(t)|^r dt
 <= (1/2) BETA(1/4, r/(4q)-1/4)
    alpha_q^(-1/2) E_2(B)^(-1/4)`.                                   (4.5)

Hausdorff--Young therefore gives `R` an `L^p` density with `p=r/(r-1)>2`. Conditioning on `W`, the translated physical scalar `Z+h(W)` retains density cap one. The standard near/far split for the kernel `|u|^(-1/2)`, optimized in the splitting radius, then yields

`||p_Q||_infinity <= C(q,2,r)|d|^(-1/2) E_2(B)^(-1/8)`,              (4.6)

where

`C(q,2,r)
 = 4(2-r)^((r-3)/2) r^(-r/2)
   sqrt(e) 2^(-3/4) q^(-1/4)
   sqrt( (1/2) BETA(1/4, r/(4q)-1/4) )`.                             (4.7)

Substituting (3.10) produces the new sign-insensitive rank-two Schur estimate

`||p_Q||_infinity
 < C(q,2,r) sqrt(2) (1-tau^2)^(-1/4)
   |d|^(-1/2)|det M|^(-1/4).`                                        (4.8)

This is `QFORM-RANK2-SCHUR-BALANCED-PAVING-v1`.

The proof uses an integrated `L^r_t` estimate, not the refuted law-uniform pointwise scalar Fresnel bound.

## 5. Two explicit universal cutoffs

### 5.1 Cleaner cutoff `mu<1/8`

Take

`q=1`, `tau=1/2`, `r=3/2`.

Then (3.8) holds whenever `mu<1/8`, and

`E_2(B) > (9/256) det(M)^2`.                                          (5.1)

The explicit density bound is

`||p_Q||_infinity
 < 17.748474 |d|^(-1/2)|det M|^(-1/4).`                               (5.2)

### 5.2 Wider cutoff `mu<=1/6`

Take

`q=7/4`, `tau=3/5`, `r=15/8`.

For `mu<=1/6`,

`2mu/tau^2 <= (1/3)/(9/25)=25/27<1`,

and the leverage in (3.7) is at most `5/6<7/8=q/2`. Moreover

`E_2(B) > (16/625)det(M)^2`.                                          (5.3)

Thus

`||p_Q||_infinity
 < 52.591349 |d|^(-1/2)|det M|^(-1/4).`                               (5.4)

The constants are not optimized; the structural point is that an indefinite rank-two residual with no row leverage above `1/6` is now paid by an aggregate physical cut rather than one chosen minor.

More generally, (3.8) is feasible for some `q<2` whenever

`mu < (3-sqrt(5))/4 = 0.190983...`,                                   (5.5)

because one may choose `tau` strictly between `sqrt(2mu)` and `1-2mu`, then choose `q` between `4mu/(1-tau)` and `2`.

## 6. Direct refinement of the exact-rank-three localized obstruction

Let now

`A=U Lambda U^T`, `U^T U=I_3`,                                      (6.1)

have exact rank three, with all three nonzero eigenvalues of modulus at least one. Choose a physical pivot `k` with

`d=A_kk!=0`, `ell=||U_{k,*}||^2`.                                    (6.2)

The exact Schur determinant identity already established in the QFORM archive is

`|det M| = |det Lambda| ell/|d|`,                                     (6.3)

where `M` is the nonzero `2 x 2` spectral matrix of the rank-two Schur remainder. Inserting (6.3) into (4.8) yields

`||p_Q||_infinity
 < C_bal(q,r,tau)
   (|d| |det Lambda| ell)^(-1/4)`.                                   (6.4)

In particular, if a localized pivot has

`ell>1/2`, `|d|>=1/2`,                                                (6.5)

then the sign of `d` is irrelevant. If the residual rank-two frame has maximum row leverage `mu<=1/6`, (5.4) and `|det Lambda|>=1` give

`||p_Q||_infinity < 74.376`.                                          (6.6)

For the cleaner `mu<1/8` branch the corresponding number is

`||p_Q||_infinity < 25.101`.                                          (6.7)

This attacks the current localized indefinite **majority-sign** obstruction directly. Previous minority-pivot arguments made the Schur remainder definite; (6.6) does not need definiteness. A remaining exact-rank-three counterexample in the localized branch must therefore, at each such first heavy pivot, satisfy at least one of

1. `|A_kk|<1/2` (near the spectral light cone), or
2. the rank-two Schur frame has a second physical row of leverage `>1/6`.

Thus the first pure-rank-three debt is reduced from an unrestricted majority-sign residual to an explicit **near-isotropic-or-second-heavy-row** alternative.

This meshes with the existing Plucker localization chain without assuming a universal single good pivot: the cut is constructed only after a pivot has actually been supplied by that branch.

## 7. Regression

`check_balanced_rank2.py` verifies the exact exterior-square identity on a twelve-row tight frame with `mu=1/6`, exhaustively searches its `2^12` sign partitions, finds a partition satisfying the explicit `q=7/4,tau=3/5` conditions, and checks the beta-function constants. `CHECK_OUTPUT.txt` records `STATUS=PASS`.

This computation is regression evidence only; Sections 2--6 are analytic.

## 8. What remains unpaid

The full QFORM conjecture remains **OPEN**. This theorem does not solve:

- the near-isotropic localized pivot branch `|A_kk|<1/2`;
- the resulting two-level/heavy residual branch when `mu>1/6`;
- the general full-matrix interaction problem when there are additional spectral directions beyond a selected rank-three core.

The next B02-integrated-Fourier target is therefore finite and explicit: use two physical coordinates coming from the second-heavy-row alternative to obtain either a rank-two mixed-slope packet with a universal integrated budget, or a dependence-safe aggregate-bank representation. The live corrections forbid replacing this by a one-minor or conditional-independence shortcut.

Essential boundedness is proved on the branches above. Continuity is not proved by this square-potential argument.
