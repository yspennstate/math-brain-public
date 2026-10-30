SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T16:01:09Z.
attacking: the near-singular nonzero physical-pair endpoint left by fleet03/B01, by converting its W2 overlap currency into exact off-diagonal curvature of the full pair Schur complement and spending that curvature through global sub-half-Riesz plus the proved logarithmic pair envelope.

# fleet02/B01 r46 — W2-to-Schur curvature identity and near-singular logarithmic compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed in the new branch.

## 1. Correction boundary and exact target

The unrestricted target remains OPEN: for every dimension, every product law of independent real coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample.

The phase-aligned fragmented-support construction still refutes any law-uniform scalar pointwise quadratic Fresnel decay. No step below uses such a bound, no rotated variables are declared independent, and no moment, support, log-concavity or Gaussian hypothesis is introduced. The mechanism is distributional: a fractional-potential estimate on the exact ORIGINAL-coordinate Schur remainder is averaged through the already-proved logarithmic density kernel of an ORIGINAL physical pair.

The latest compatible correction inbox was reread before publication. In particular this run does not use the refuted arbitrary-joint coarea bound, conditional projected-density moments, post-rotation independence, or perturbative closeness in law.

## 2. Source-valid inputs actually used

### 2.1 Newest designated partner fleet03/B01

Read at compatible master state `yspennstate/math-open-problems@8d6e85d072cd7a4c0fa9a37abe995a64109079e0`:

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T153212Z-auto11/REPORT.md`.

For a physical pair

`B=[[a,b],[b,c]]`, `a!=0`,

scalar-complete the first ORIGINAL coordinate and define

`delta=c-b^2/a`, `ell=v-(b/a)u`, `M=C-a^{-1}u u^T`.

The report records the exact overlap-two identity

`W2(B)=a^2 sum_(k!=l)(delta M_kl-ell_k ell_l)^2`.               (2.1)

At `det B=0` it combines this with the arbitrary-curvature rank-one random-slope receiver to prove

`||p_Q||inf <=4 sqrt(2)e^(1/4)|a|^(-1/4) W2(B)^(-1/8)`.       (2.2)

It also gives an explicit obstruction showing the exact-null half-Riesz proof is not stable under blindly adding `delta Y^2`: with `T(Z)=Z`, `K(Z)=Z^2/delta`, one obtains `delta(Y+Z/delta)^2` and an infinite half-Riesz potential. That obstruction is respected below rather than perturbed away.

Section 7 applies (2.2) to an actual strict-N3 sibling inequality.

### 2.2 Global sub-half-Riesz theorem from the previous B01 run

Read at the same compatible state:

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260923T060557Z-fleet02-B01-qform-auto11/REPORT.md`.

For every symmetric physical-coordinate matrix `S`, arbitrary affine term, and independent cap-one inputs, with

`F(S)=sum_(i!=j)S_ij^2`,

the proved theorem gives, for `0<beta<1/2`,

`H_beta(R):=sup_s E|R-s|^(-beta) <= C_beta F(S)^(-beta/2)`,     (2.3)

where `R=Z^T S Z+affine` and

`C_beta = e^(beta/2)(4pi)^beta /
          [beta(1-2beta)Gamma(beta)cos(pi beta/2)]`.             (2.4)

At `beta=1/4`, `C_beta=5.095453495355205...`.

### 2.3 Logarithmic indefinite-pair envelope

Read in full at compatible state:

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite ORIGINAL-coordinate pair `B`, put

`D=|det B|`, `kappa=sigma_min(B)>0`.

After completing the pair exactly, if the remainder is `R`, then for every gradient cutoff `r>0`,

`p_Q(t) <=2sqrt(2)/r
          +D^(-1/2) E log_+(2r^2/(kappa |t-R|))`.              (2.5)

The shifts of the two physical coordinates may depend arbitrarily on the remainder variables; the original pair itself remains independent of them.

### 2.4 Required newest Claude/Fresnel-Brascamp-Lieb package

The required package

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`

was reread at its latest compatible state. In Section 6 below its unconditional five-volume theorem is applied to an explicit original-coordinate cross block:

`||p_Q||inf <=5 sqrt(2e) Z_5^(-1/10)`, `Z_5=e_5(M^T M)`.       (2.6)

The comparison is an actual inequality on the stress family, not a summary-only citation.

## 3. Exact algebraic bridge: W2 is determinant-squared times full pair-Schur off-diagonal energy

Consider the full quadratic matrix in ORIGINAL coordinates, partitioned into the physical pair and the remaining variables:

`A=[[B, C_pair], [C_pair^T, A_0]]`,

with `B=[[a,b],[b,c]]`, `a!=0`, `det B!=0`.

Write the two rows of `C_pair` as `u^T,v^T`. After completing the first scalar coordinate the partner notation is

`delta=c-b^2/a`,
`ell=v-(b/a)u`,
`M=A_0-a^{-1}u u^T`.

Since `det B=a delta`, the exact Schur complement of the WHOLE pair is

`S=A/B=M-delta^{-1} ell ell^T`.                                  (3.1)

Therefore for every off-diagonal index pair `k!=l`,

`delta M_kl-ell_k ell_l = delta S_kl`.                           (3.2)

Insert (3.2) into the newest partner identity (2.1):

`W2(B)
 =a^2 delta^2 sum_(k!=l) S_kl^2
 =D^2 F(S)`.                                                       (3.3)

This is exact, not an inequality.

### Theorem 3.1 — `QFORM-W2-PAIR-SCHUR-IDENTITY-v1`

For every invertible physical pair with `a!=0`, the partner overlap-two currency equals

`boxed: W2(B)=|det B|^2 F(A/B).`                                  (3.4)

If instead `c!=0`, swap the two ORIGINAL coordinates and obtain the same identity. Hence (3.4) is intrinsic to the chosen physical pair.

This explains the partner's near-null obstruction sharply: its completed-square example has exact pair-Schur quadratic remainder zero, hence `F(S)=0` and therefore `W2=0`. Positive W2 is precisely aggregate off-diagonal quadratic curvature that survives the second Schur completion; it is not a perturbative version of the exact-null random slope.

## 4. New theorem: near-singular W2 logarithmic compiler

Let the ORIGINAL physical pair be invertible and indefinite. Assume `W2(B)>0`. After completing the pair, the remaining random variable has quadratic part `S=A/B` and arbitrary affine term. By (2.3) and (3.4), for every `0<beta<1/2`,

`H_beta(R)
 <=C_beta F(S)^(-beta/2)
 =C_beta D^beta W2(B)^(-beta/2).`                                 (4.1)

For every `A0>0`, layer cake and Markov give

`E log_+(A0/|t-R|)
 =int_0^infinity P(|t-R|<A0 e^{-v}) dv
 <=H_beta A0^beta / beta`.                                        (4.2)

Apply (4.2) to the exact pair envelope (2.5), with `A0=2r^2/kappa`:

`p_Q(t)
 <= A/r + B_beta r^(2beta)`,                                      (4.3)

where

`A=2sqrt(2)`,

`B_beta=(2^beta C_beta/beta)
        D^(beta-1/2) kappa^(-beta) W2^(-beta/2)`.                 (4.4)

For `p=2beta`, the minimum of `A/r+B r^p` is attained at

`r_*=(A/(pB))^(1/(p+1))`

and equals

`(p+1)p^(-p/(p+1)) A^(p/(p+1)) B^(1/(p+1))`.                    (4.5)

Hence:

### Theorem 4.1 — `QFORM-NEARSINGULAR-W2-SUBHALF-LOG-v1`

For every `0<beta<1/2`,

`boxed:
 ||p_Q||inf
 <=K_beta
   D^((beta-1/2)/(1+2beta))
   kappa^(-beta/(1+2beta))
   W2(B)^(-beta/[2(1+2beta)]),`                                  (4.6)

with

`K_beta=(1+2beta)(2beta)^(-2beta/(1+2beta))
        (2sqrt(2))^(2beta/(1+2beta))
        (2^beta C_beta/beta)^(1/(1+2beta)).`                     (4.7)

Equivalently, before substituting W2,

`||p_Q||inf
 <=K_beta
   D^(-1/[2(1+2beta)])
   kappa^(-beta/(1+2beta))
   F(A/B)^(-beta/[2(1+2beta)]).`                                 (4.8)

At `beta=1/4`, direct evaluation gives

`K_(1/4)=22.3846243413...`, and therefore

`boxed:
 ||p_Q||inf
 <=22.385 D^(-1/6) kappa^(-1/6) W2(B)^(-1/12).`                 (4.9)

Scaling is exact. Under `A -> sA`, `D -> s^2D`, `kappa->s kappa`, `W2->s^6W2`; the right side of (4.6) scales as `s^(-1)`.

The theorem is an essential-supremum statement. The proof does not supply an `L^1` characteristic-function majorant, so no continuity claim is made.

### Why this is a genuine advance on the first unpaid implication

The exact-singular partner theorem (2.2) has the W2 scale `W2^(-1/8)` but only at determinant zero. The naive half-Riesz continuation for nonzero determinant is explicitly false. Theorem 4.1 instead completes the nonzero pair exactly, converts W2 into *surviving Schur curvature* by (3.4), obtains a subcritical Riesz bound on that curvature, and lets the logarithmic pair kernel perform the final smoothing. No singular argument is perturbed.

As `beta` approaches `1/2`, the W2 exponent approaches `-1/8` and the determinant exponent approaches zero; the residual obstruction is the pair-conditioning scale `kappa`, whose exponent approaches `-1/4`, together with the expected `(1-2beta)` divergence in `K_beta`. This localizes the next analytic debt precisely.

## 5. Strict-N3 near-singular overlap family paid uniformly

Theorem 4.1 is not merely formal. It gives a parameter-free bound on a target-valid strict-N3 family with a genuinely nonzero, arbitrarily small physical-pair determinant and arbitrary dense same-bank curvature.

Let `0<epsilon<=1/4` and let `m` be a sufficiently large power of two. Put

`B=diag(epsilon,-epsilon)`,
`D=epsilon^2`, `kappa=epsilon`.                                  (5.1)

Let `U,V` be `m x 2` matrices with orthonormal flat Walsh columns, chosen so that `V^T U=0`. Put

`sigma=epsilon^(-5)`, `theta=m^(-2)`,
`M=sigma U V^T+theta I_m`.                                       (5.2)

Let `S_m` be the normalized symmetric Sylvester-Hadamard matrix, so `||S_m||op=1` and every entry has magnitude `m^(-1/2)`. Set `eta=1/8` and define the desired exact pair-Schur remainder

`N=[[eta S_m, M],[M^T, eta S_m]]`.                               (5.3)

Choose flat unit vectors `r_I` in the I-bank and `r_J` in the J-bank and let the physical pair-to-leaf coupling be

`C_pair = [[epsilon r_I^T, 0], [0, epsilon r_J^T]]`.             (5.4)

Finally set the actual physical leaf block to

`A_0=N+C_pair^T B^(-1) C_pair
    =N+epsilon r_I r_I^T-epsilon r_J r_J^T`.                     (5.5)

Then the exact Schur complement of the nonzero pair is **exactly** `N`. The pair is not source-disjoint from the leaves; the overlap has been included and eliminated exactly.

### 5.1 Target spectrum

The rank-two cross core

`N_0=[[0,sigma U V^T],[sigma V U^T,0]]`

has eigenvalues `+sigma,+sigma,-sigma,-sigma` and the rest zero. The perturbation `N-N_0` has operator norm at most `eta+theta`. Relative to `B direct_sum N`, the overlap/correction block in the full physical matrix has operator norm at most `2epsilon`. Hence Weyl gives four eigenvalues of the full target with modulus at least

`sigma-eta-theta-2epsilon >1`.                                  (5.6)

Thus the exact three-large-eigenvalue hypothesis is satisfied with room to spare.

### 5.2 Strict N3

All physical pair diagonals have magnitude `epsilon`. Leaf diagonals have magnitude at most

`eta/sqrt(m)+epsilon/m`.                                         (5.7)

Pair-to-leaf entries have magnitude `epsilon/sqrt(m)`. Same-bank leaf entries have magnitude at most `eta/sqrt(m)+epsilon/m`. Cross-bank entries satisfy

`|M_ij|<=2sigma/m+theta`.                                        (5.8)

Therefore, for every fixed no-pivot threshold `tau>0`, first choose `epsilon<tau`, then choose `m` so large that the squares and products of the quantities in (5.7)-(5.8) are below `tau`. Every physical diagonal and every physical `2x2` principal determinant is then below `tau`. The family enters strict N3 while the physical pair determinant tends to zero.

### 5.3 New theorem gives a universal constant

The cross block `M` contributes twice its Frobenius energy to `F(N)`. Since `V^T U=0`,

`||M||_F^2=2sigma^2+m theta^2`,

so

`F(N)>=2||M||_F^2>=4sigma^2=4epsilon^(-10)`.                     (5.9)

By the exact identity,

`W2(B)=D^2 F(N)>=4epsilon^4 epsilon^(-10)=4epsilon^(-6)`.        (5.10)

Insert (5.1) and (5.10) into (4.9):

`||p_Q||inf
 <=22.385 (epsilon^2)^(-1/6) epsilon^(-1/6)
          (4epsilon^(-6))^(-1/12)
 =22.385*4^(-1/12)
 <19.943.`                                                        (5.11)

Thus the new near-singular compiler remains uniformly bounded while `det B ->0`, because the surviving Schur curvature grows at exactly the compensating scale. The dense full-rank same-bank Hadamard curvature is retained; it is not discarded as a random perturbation.

## 6. Required newest Claude result applied: D5 is valid but asymptotically expensive on the same family

The natural ORIGINAL-coordinate I-J cross block in (5.5) is exactly `M` from (5.2); the pair-overlap correction is block-diagonal and does not change it. Because `theta I_m` is invertible and `V^T U=0`, the matrix determinant lemma gives `det M=theta^m`, so `rank M=m` and `Z_5=e_5(M^T M)>0` for `m>=5`.

The completed source theorem D5 therefore gives the actual finite bound

`boxed: ||p_Q||inf <=5sqrt(2e) Z_5^(-1/10).`                    (6.1)

Now Weyl's singular-value inequality gives

`s_1(M),s_2(M)<=sigma+theta`,
`s_j(M)<=theta`, `j>=3`.                                         (6.2)

Consequently

`Z_5
 <= C(m-2,3)(sigma+theta)^4 theta^6
  +2 C(m-2,4)(sigma+theta)^2 theta^8
  +C(m-2,5) theta^10`.                                           (6.3)

With `theta=m^(-2)` and fixed `epsilon` (hence fixed `sigma`), the right side is `O(sigma^4 m^(-9))`; hence `Z_5 ->0` and the valid D5 certificate (6.1) diverges at least polynomially along this family. In contrast, (5.11) stays below `19.943` uniformly in both `m` and `epsilon`.

This is the requested concrete use of the newest averaged-frequency/volume package: high-order cross-volume is genuinely present, so D5 is applicable, but the newly identified pair-Schur off-diagonal currency is the better scale in this near-singular overlap geometry.

## 7. Newest partner theorem applied at an actual strict-N3 inequality

To verify complementarity with fleet03/B01 rather than merely cite it, consider the exact-singular sibling

`Q_sing
 =epsilon X^2
  +2 epsilon^(-1) Y <e,Z>
  +(w^T W)^2`,                                                   (7.1)

where `e` and `w` are flat unit vectors on two disjoint `m`-coordinate banks, and all physical coordinates are independent with density caps one.

For the physical pair `{X,Y}`,

`a=epsilon`, `b=c=0`, `u=0`, `ell=epsilon^(-1)e`.

Thus

`L(ell)=epsilon^(-4)(1-1/m)`,
`W2=epsilon^2 L(ell)=epsilon^(-2)(1-1/m)`.                       (7.2)

Apply the newest fleet03/B01 exact-singular theorem (2.2):

`||p_(Q_sing)||inf
 <=4sqrt(2)e^(1/4)
   epsilon^(-1/4)
   [epsilon^(-2)(1-1/m)]^(-1/8)`

`=4sqrt(2)e^(1/4)(1-1/m)^(-1/8).`                               (7.3)

For `m>=64`, the right side is `<7.278`, uniformly in `epsilon`.

The coefficient matrix has eigenvalues `+epsilon^(-1),-epsilon^(-1)` on the `Y-e` plane and eigenvalue `1` on the grouped-square bank, so it satisfies the exact target. Taking `epsilon` small and then `m` large makes every physical diagonal and every physical `2x2` principal determinant arbitrarily small, hence gives another strict-N3 family. This is a direct application of the newest designated-partner theorem at an actual target inequality.

Sections 5 and 7 meet at the correct analytic boundary: the partner pays the exact singular pair via aggregate random slope; Theorem 4.1 pays a substantial nonzero-determinant region via the exact pair-Schur curvature that survives completion. The partner's divergent half-Riesz example lies at `W2=0` and is not contradicted.

## 8. First unpaid implication after this run

`QFORM-NEARSINGULAR-KAPPA-BRIDGE-v1`:

> For a strict-N3 physical pair with nonzero but tiny determinant and positive W2, remove the residual `kappa` loss in Theorem 4.1 by a product-preserving sequential averaged-frequency argument, or quantitatively route the `kappa`-tiny geometry to the exact-singular random-slope branch / mixed hubs / volume / grouped-square receivers before paying `kappa^{-1}`.

The one-parameter family (4.6) shows what must happen at the analytic endpoint: as `beta up to 1/2`, the determinant power disappears and the W2 power tends to the exact-singular `-1/8`; only the physical-pair conditioning scale remains. A successful next mechanism therefore should couple the near-null coordinate and the Schur curvature **before** the pair's hyperbolic change of variables, rather than improve the already-sharp scalar fractional-potential endpoint.

A second structural debt remains global: the three-large-eigenvalue hypothesis does not force one pair with favorable `(D,kappa,W2)`. The new theorem is a paid receiver, not an exhaustive routing theorem.

## 9. Status

Full QFORM is **not proved or disproved**. The new results are supporting theorems pending independent review. The phase-aligned-density pointwise-decay refutation remains in force. No continuity conclusion is bundled with the essential density bounds in Sections 4-7.
