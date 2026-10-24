SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02.
attacking: integrated Fourier estimate; independently check the new q-dependent sharp-Hausdorff--Young volume theorem, optimize it on the live perturbative physical cross block, then attack the first unpaid two-sided D' star concentration by an aggregate block compiler.

# account02/B02 — sharp-HY stability optimization and joint-star block compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
**Partner:** `account03/B02`  
**Fresh owner control at start:** `math-research-brain@a05b08f84f939248c82f5d2f91d15c2964e7ae95`, owner revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  

The target remains: independent real coordinates with probability densities at most one, symmetric `A` with at least three eigenvalues of modulus at least one, and one dimension-free essential density bound for `X^T A X`, with no moment, support, log-concavity, diagonal-basis, or post-rotation-independence hypothesis.

## 1. Sources consumed and scope

The exact requested Claude-attributed package was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, namely `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. I use its D' three-volume and D5 five-volume integrated-Fourier mechanisms, together with the reviewed sharp Hausdorff--Young refinement.

A later owner continuation additionally points B02 to the volume-stability package

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

I independently checked the **analytic** part of that note (the sharp-HY/BL multiplier, exponent and inversion constants) and record PASS for that scope. I do not claim the separate matrix/tail perturbation review assigned elsewhere.

The newest completed designated-partner result available at fresh control was `account03/B02` r17, canonical proof

`yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T230126Z-account03-B02-QFORM-r17/REPORT.md`.

It proves that if an ORIGINAL-coordinate physical cross block `M` has exact rank three and `Gamma` is the product of its three nonzero singular values, then

`||p_Q||_infinity <= 6 Gamma^(-1/3)`,

and in fact `phi_Q` is in `L1`. I apply this result below, rather than merely cite it.

The current corrections were also consumed. In particular I do not use the false near-zero-self half-Riesz inference, fixed-good-minor extraction, post-rotation independence, or law-uniform pointwise Fresnel decay.

## 2. Independent check of the q-dependent sharp-HY theorem

Let `M=A[I,J]` be a physical cross block and

`Z=e_3(M^T M)>0`.

Volume-sample row/column triples with weights `det(M[S,T])^2/Z`; write `alpha_i,beta_j` for the row and column inclusion probabilities. The volume-stability note states that for

`1 <= q < 3/2`,   `max_i alpha_i <= q/2`,

one has

`||p_Q||_infinity <= C(q) Z^(-1/6)`,
`C(q)=3e/((3-2q)sqrt(q)).`                                           (2.1)

I checked the constants as follows.

For `h_i(u)=|hat f_i(2tu)|^q`, sharp Hausdorff--Young at output exponent `q/alpha_i >= 2` uses input exponent `q/(q-alpha_i)` and, since `f_i<=1` and has mass one,

`||h_i||_(1/alpha_i)
 <= (pi/|t|)^alpha_i
    (alpha_i/q)^(alpha_i/2)
    (1-alpha_i/q)^(-(q-alpha_i)/2).`                                 (2.2)

The Gaussian BL constant contributes `alpha_i^(-alpha_i/2)`, cancelling the corresponding factor in (2.2). Since `sum alpha=sum beta=3` and `-(1-x)log(1-x)<=x`, the row and column entropy products contribute at most `e^(3/2)` each. Hence

`E F_t(D)^q <= e^3 q^(-3/2) (pi/|t|)^3 Z^(-1/2).`                    (2.3)

The decoupling inequality is `|phi_Q(t)|^2 <= E F_t(D)`, and Jensen gives

`|phi_Q(t)| <= min(1,K|t|^(-3/(2q)))`,
`K=[e^3 q^(-3/2) pi^3 Z^(-1/2)]^(1/(2q)).`                          (2.4)

Integrating the optimized envelope and dividing by `2pi` gives exactly (2.1). The endpoint bookkeeping is consistent: `alpha_i=0` is interpreted continuously; a column with `beta_j=1` is dropped using its density cap; `q=1` is valid; and `q -> 3/2` is precisely the non-integrable endpoint. Thus the analytic constants/exponents in Sections 5--6 of the new note pass this independent check.

## 3. New optimization: improve the live volume-stability constant from <23/a to <15.247/a

### Theorem 3.1 — `QFORM-VOLUME-STABILITY-OPTIMAL-Q-v1`

Assume the live physical block decomposes as

`M=M0+E`,
`rank(M0)>=3`, `s_3(M0)>=a>0`,
`max_i (P_range(M0))_ii <= 1/2`,
`||E||_op <= a/16`.                                                  (3.1)

Then the same product-input hypotheses as the target imply a continuous density and

`boxed( ||p_Q||_infinity <= C_* / a )`,

where

`C_* = 3600 e/(1035-227 sqrt(3))
     = 15.246870586040... .`                                         (3.2)

This improves the source package's convenient `q=4/3` constant `24 sqrt(3)e/5 = 22.60...` without changing a structural hypothesis.

#### Proof

Let `P=P_range(M0)`, `kappa=s_3(M)`, and let `alpha_i` be the actual third-volume row marginals of `M`. The source's proved projection inequality is

`sqrt(alpha_i) <= sqrt(l_i) + (sqrt(3)||E||_op/kappa)sqrt(1-l_i)`,
`l_i=P_ii`.                                                          (3.3)

Weyl gives `kappa>=15a/16`. Therefore

`d:=sqrt(3)||E||_op/kappa <= sqrt(3)/15=:d0`.

For `l<=1/2` and `d<=1`, the right side of (3.3) is increasing in `l`, so

`alpha_i <= h0 := (1+d0)^2/2`.                                      (3.4)

The source chose `q=4/3`. Instead choose the smallest admissible q,

`q_* := 2h0 = (1+sqrt(3)/15)^2
               =1.244273441009... <3/2`.                            (3.5)

This is optimal within (2.1), because

`d/dq log C(q)
 = 2/(3-2q) - 1/(2q)
 = (6q-3)/(2q(3-2q)) >0` for `q>=1`.                                (3.6)

Also `Z=e_3(M^T M)>=s_1^2 s_2^2 s_3^2>=kappa^6`, so (2.1) gives

`||p_Q||_infinity <= C(q_*)/kappa
                    <= (16/(15a)) C(q_*).`                           (3.7)

Since `sqrt(q_*)=1+sqrt(3)/15`, elementary simplification yields

`(16/15) C(q_*) = 3600e/(1035-227sqrt(3))`,

which is (3.2). Because the proof is through an `L1` characteristic-function envelope, this branch also has a continuous density vanishing at infinity. QED.

### Partner result applied to an actual endpoint

If the same live block has **zero tail beyond rank three**, so the actual physical cross block has exact rank three, the designated partner theorem applies without any volume-marginal gate. If `s_3(M)>=a`, then `Gamma=s_1s_2s_3>=a^3`, hence

`boxed( ||p_Q||_infinity <= 6/a ).`                                  (3.8)

Thus (3.2) is a stability extension into arbitrary extra singular directions, while the partner theorem pays the exact-rank-three endpoint with the stronger constant `6/a`. This is the required concrete use of the completed `account03/B02` result.

## 4. First unpaid implication: two-sided D' failure forces an aggregate block resource

D' closes a cross block whenever its third-volume row marginals are sufficiently diffuse. Suppose it fails in both orientations. Then there are a physical row `i` and physical column `j` with

`alpha_i >= 3/4`, `beta_j >= 3/4`.                                   (4.1)

Let `Z3=e_3(M^T M)` and let

`J_ij := sum_{|S|=|T|=3, i in S, j in T} det M[S,T]^2`.              (4.2)

Under the squared-minor probability law, (4.1) and the union bound give

`J_ij/Z3 = P(i in S and j in T)
          >= alpha_i+beta_j-1 >=1/2`,

so

`J_ij >= Z3/2`.                                                       (4.3)

The next lemma converts this abstract Pluecker-star concentration into explicit physical-coordinate resources without choosing one tiny minor.

### Lemma 4.1 — `QFORM-JOINT-STAR-BLOCK-COMPILER-v1`

Reindex the selected row and column first and write

`M = [ a    r^T ]
    [ c     N   ]`,                                                  (4.4)

where `a=M_ij`, `r` is the rest of row `i`, `c` the rest of column `j`, and `N` is the complementary physical cross block. Put

`E2(N)=e_2(N^T N)`,
`F_perp=||P_(c^perp) N P_(r^perp)||_F`,                              (4.5)

with the convention that the corresponding projection is the identity if `c=0` or `r=0`. Then

`sqrt(J_ij)
 <= |a| sqrt(E2(N)) + ||c|| ||r|| F_perp`.                           (4.6)

Consequently, under (4.3), at least one of

`boxed( a^2 E2(N) >= Z3/8 )`                                        (4.7)

or

`boxed( ||c||^2 ||r||^2 F_perp^2 >= Z3/8 )`                          (4.8)

must hold.

#### Proof

For residual row pairs `S` and residual column pairs `T`, the `3x3` minor containing the distinguished row and column is

`D_ST = a det N[S,T] - r_T^T adj(N[S,T]) c_S`.                       (4.9)

Take the Euclidean norm over all such `(S,T)`. By the triangle inequality and Cauchy--Binet,

`(sum D_ST^2)^(1/2)
 <= |a| (sum det N[S,T]^2)^(1/2)
    +(sum (r_T^T adj(N[S,T])c_S)^2)^(1/2)
 = |a| sqrt(E2(N)) + second_term.                                    (4.10)

The second term has the exact coordinate-free identity

`sum_{S,T} (r_T^T adj(N[S,T])c_S)^2
 = ||c||^2 ||r||^2 ||P_(c^perp) N P_(r^perp)||_F^2.                 (4.11)

For completeness: the left side is the squared Hilbert--Schmidt norm of the component of the third exterior-power coefficient tensor containing the distinguished row and column, and is invariant under orthogonal changes of basis in the residual row and column spaces. Rotate `c=||c|| e_1` and `r=||r|| e_1`. Only pairs containing those first residual axes survive, and each surviving cofactor is, up to sign, `||c||||r||` times one entry of the doubly projected block. Summing its square gives (4.11). These rotations are only a deterministic proof of a matrix identity; no random input is rotated.

Equations (4.10)--(4.11) prove (4.6). If both terms on its right were strictly below `sqrt(J_ij)/2`, their sum would be below `sqrt(J_ij)`. Hence one is at least `sqrt(J_ij)/2`; use (4.3) and square to obtain (4.7) or (4.8). QED.

### Why this pays a real part of the collar

This lemma is not yet a density theorem, but it removes an ambiguity in the first unpaid interface. Two-sided D' failure cannot leave only an amorphous 'heavy Pluecker star'. It yields either

1. a **single physical cross edge times aggregate residual two-volume**, `|a| sqrt(E2(N))`, or
2. **two physical cross stars times a transverse aggregate Frobenius packet**, `||c||||r||F_perp`.

No reciprocal of one selected `2x2` or `3x3` minor appears.

There are two immediate completed exits:

- If `rank(M)=3`, partner r17 gives `||p_Q||_infinity <=6 Z3^(-1/6)` regardless of the failed D' gate, because `Gamma^2=Z3`. Therefore the genuinely unpaid joint-star collar has cross rank at least four.
- If `Z5=e_5(M^T M)>0`, the reviewed D5 theorem gives the unconditional integrated-Fourier branch

  `||p_Q||_infinity <= (5e/sqrt(2)) Z5^(-1/10)`.                    (4.12)

Thus the sharp remaining use of Lemma 4.1 is the high-concentration rank-four / quantitatively weak-fifth-volume collar, exactly where D' can fail and D5 gives no useful scale.

## 5. Status of the stronger global Fourier criterion

The requested `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` contain no target-valid counterexample to a universal unweighted `int |phi_Q(t)| dt` criterion, and I found none in this run. The criterion therefore remains **open, not refuted**. This run instead strengthens two source-valid integrated-Fourier branches and narrows the first unpaid collar.

The current correction forbidding a near-zero-self half-Riesz inference is respected: Theorem 3.1 uses a physical cross-volume gate, and Lemma 4.1 is a deterministic cross-block identity. Neither assumes that a small self coefficient can be replaced by zero.

## 6. First unpaid implication after this run

The next interface is now concrete:

**`QFORM-JOINT-STAR-RESOURCE-TO-L1-v1`.** In the rank-at-least-four, D'-failed, D5-weak collar, convert either (4.7) or (4.8) into an `L1_t` estimate or a dependence-safe fractional-potential density bound while retaining all cross couplings `r,c` and arbitrary same-bank quadratic phases. Do not localize to one minor and do not rotate random inputs. In branch (4.7), the natural target is a physical-edge + aggregate-rank-two transducer; in branch (4.8), the natural target is an aggregate mixed-hub/two-star transducer.

This is strictly narrower than the preceding 'joint star' obligation and is compatible with the live corrections.

## 7. Claims and telemetry

Statuses in this report are deliberately separated:

- analytic review of the q-dependent sharp-HY theorem: **independent PASS for the analytic constants/endpoints only**;
- Theorem 3.1: **proved supporting theorem / improved constant**;
- Lemma 4.1: **proved deterministic supporting lemma**;
- partner r17: **completed external worker result, actually applied in (3.8) and the rank-three exit**;
- full QFORM target: **OPEN**;
- global target-wide unweighted `L1` characteristic-function criterion: **OPEN / no valid counterexample found**.

Model self-report: GPT-5.6 Sol. Configured reasoning effort and provider reasoning-token/thinking-time telemetry are not exposed here and must remain UNKNOWN/null. Elapsed wall work, when recorded by the run wrapper, is not pure thinking time.
