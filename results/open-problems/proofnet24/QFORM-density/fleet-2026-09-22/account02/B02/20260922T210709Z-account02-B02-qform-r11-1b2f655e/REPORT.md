SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-22T21:07:09Z.
attacking: integrated Fourier estimate via conditional Pluecker-bank whitening; aggregate exterior mass before any reciprocal coordinate-minor payment.

# account02/B02 — conditional Pluecker-bank integrated Fourier theorem

**Run:** `20260922T210709Z-account02-B02-qform-r11-1b2f655e`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, live owner revision `2026-09-22.15` at start  
**Assignment:** `Integrated Fourier estimate`, pathway `FOURIER`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source corrections

The owner target remains: independent real coordinates with probability densities at most one, and a real symmetric matrix with at least three eigenvalues of modulus at least one; prove a universal essential density bound for `Q=X^TAX`, or give a valid counterexample. This report proves a new exact-rank-three integrated-Fourier branch. It does **not** solve arbitrary extra spectrum.

Corrections respected here include: no law-uniform pointwise one-dimensional Fresnel decay; no post-rotation independence; no arbitrary-joint rank-three coarea bound; no positive conditional projection-density-moment gate; no fixed-good-minor or universal rank-three cross-cut extraction. The fresh account01/B01 rank-one-completion obstruction is also respected: arbitrary within-bank quadratic phases cannot be discarded when only a cross triangle is retained. None of those false interfaces is used below.

The analytic source is the proof-level small-coordinate Fourier part of Mark Rudelson and Roman Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, IMRN 2015, DOI `10.1093/imrn/rnu243`, arXiv `1402.4492`, specifically their Lemma 3.1 plus Proposition 5.1. The exact source was already pinned and audited in account02/B02 report `yspennstate/math-open-problems@2d79dea715c2baa9e8ef6c0ac174eee1712d2888:proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T114331Z-account02-B02-qform-r12/REPORT.md`, blob `d13acb61e2846ea2e1761acca18d5e4e0f124a34`. I retain its notation `B_RV<infinity`: whenever `V` has orthonormal columns and every row has Euclidean norm at most `1/2`, the projection characteristic function satisfies

`int_{R^d} |prod_i phi_i(<v_i,xi>)| dxi <= B_RV^d`.

This proof-level Fourier statement, not merely the projection-density theorem, is the external input.

Named partner actually consumed: account03/B02 r14, `QFORM-LOCALIZED-PRINCIPAL-3X3-REPAIRED-v1`, canonical proof `yspennstate/math-open-problems@54c9b45ccd6dd4dd686e91ff04e39e2cc5ebbbcf`. It proves that any ORIGINAL-coordinate principal `3x3` block `B` with `sigma_min(B)>=c` yields

`||p_Q||_infinity <=128*2^(1/4)/c`.

I apply this theorem quantitatively below to Pluecker atoms. I also consume the partner's r13 overlap-one theorem at `yspennstate/math-open-problems@1b8f72a4e25ef55ca4fd974007146d3971f49bf8` to identify exactly which part of its near-isotropic residual branch is paid by the new bank theorem.

## 2. Pluecker notation and the exact conditional leverage identity

Let the form have exact rank three,

`A=U Lambda U^T`, `U^T U=I_3`, `Lambda=diag(lambda_1,lambda_2,lambda_3)`, `|lambda_j|>=1`.

Write the rows of `U` as `u_i in R^3`. For every physical triple `I`, define

`w_I = det(U_I)^2 >=0`.

Cauchy--Binet gives

`sum_{|I|=3} w_I = det(U^T U)=1`.                                      (2.1)

Now choose any bank of original coordinates `L` and put

`S_L = sum_{i in L} u_i u_i^T`.

Assume `S_L` is positive definite and write

`m_L = det S_L`.

Again by Cauchy--Binet,

`m_L = sum_{I subset L, |I|=3} w_I`.                                   (2.2)

Thus `m_L` is not one chosen minor: it is the entire third-exterior mass retained inside the bank.

For `i in L`, define its conditional Pluecker star fraction

`rho_i(L) = [sum_{I subset L, |I|=3, i in I} w_I] / m_L`.               (2.3)

Then exactly

`boxed( rho_i(L) = u_i^T S_L^{-1} u_i ).`                               (2.4)

Proof: by the matrix determinant lemma,

`det(S_L-u_i u_i^T)=det(S_L)[1-u_i^T S_L^{-1}u_i]`.

By Cauchy--Binet the left side is the total weight of triples in `L` not containing `i`; subtracting from (2.2) proves (2.4).

This identity is useful because the Rudelson--Vershynin small-coordinate gate after whitening is exactly

`rho_i(L)<=1/4` for every `i in L`.                                     (2.5)

Indeed, with `v_i=S_L^{-1/2}u_i`, one has `sum_{i in L}v_i v_i^T=I_3` and `||v_i||^2=rho_i(L)`.

## 3. Main theorem: conditional Pluecker-bank Fourier smoothing

### Theorem 3.1 — `QFORM-CONDITIONAL-PLUCKER-BANK-FOURIER-v1`

Under the exact-rank-three hypotheses above, suppose there exists a bank `L` such that `S_L>0` and

`max_{i in L} rho_i(L) <=1/4`.                                         (3.1)

Then for arbitrary independent input laws with densities at most one,

`boxed( int_R |phi_Q(t)| dt <= [3 B_RV^2/(2 pi)] [m_L |det Lambda|]^(-1/3) ).`   (3.2)

Consequently `Q` has a bounded continuous density satisfying

`boxed( ||p_Q||_infinity <= [3 B_RV^2/(4 pi^2)] [m_L |det Lambda|]^(-1/3) ).`    (3.3)

In the owner normalization `|lambda_j|>=1`, the determinant factor may be dropped.

### Proof

Condition on all original coordinates outside `L`. Their contribution to the spectral variable is a fixed vector `a in R^3`. The remaining random spectral vector is

`Z=sum_{i in L}u_i X_i`.

Whiten it by `Z'=S_L^{-1/2}Z`. Its frame rows are `v_i=S_L^{-1/2}u_i`; they resolve the identity and by (3.1) have norms at most `1/2`. The proof-level Rudelson--Vershynin estimate therefore gives

`||Phi_{Z'}||_1 <= B_RV^3`.                                             (3.4)

Since `Phi_Z(xi)=Phi_{Z'}(S_L^(1/2)xi)`, change of variables yields

`||Phi_Z||_1 <= B_RV^3 m_L^(-1/2)`.                                    (3.5)

The conditional quadratic output is

`Q_L=(a+Z)^T Lambda (a+Z)`.

The Gaussian-regularized Fresnel calculation from the earlier B02 theorem is translation-uniform: inserting the absolutely convergent inverse Fourier formula for the density of `Z`, the inner quadratic kernel has modulus at most

`pi^(3/2) |t|^(-3/2)|det Lambda|^(-1/2)`.

The shift `a` changes only the linear term in that Fresnel integral and hence does not change the modulus. Therefore, for every conditioning value and every `t!=0`,

`|E[exp(itQ) | X_{L^c}]| <= K_RV [m_L |det Lambda|]^(-1/2)|t|^(-3/2)`,  (3.6)

where

`K_RV=B_RV^3/(8 pi^(3/2))`.

Averaging the conditional characteristic functions preserves (3.6). Together with `|phi_Q(t)|<=1`,

`|phi_Q(t)| <= min(1, C |t|^(-3/2))`,

`C=K_RV[m_L|det Lambda|]^(-1/2)`.                                      (3.7)

Unlike the earlier split at `|t|=1`, optimize at the exact crossover `t_0=C^(2/3)`:

`int_R min(1,C|t|^(-3/2))dt = 6 C^(2/3)`.                              (3.8)

Since `K_RV^(2/3)=B_RV^2/(4pi)`, (3.8) is exactly (3.2). Fourier inversion gives (3.3) and continuity. QED.

### What is genuinely new

The old delocalized theorem was the special case `L=all coordinates`, where `S_L=I`, `m_L=1`, and `rho_i(L)=||u_i||^2`. The present theorem allows **arbitrary large or dangerous coordinates outside L**: they are conditioned, while the retained bank is whitened and charged only through its *aggregate* exterior mass `m_L`. It therefore implements `aggregate before reciprocal minor payment` in an exact source-valid Fourier inequality.

It also improves the old integrated constant by using the optimized crossover (3.8) instead of a fixed split at frequency one.

## 4. Direct partner application: a large Pluecker atom is already paid

The same exterior-mass language gives a clean localized certificate by applying the named partner r14 theorem.

Suppose some triple `I` has

`w_I >= delta >0`.                                                      (4.1)

Let `R=U_I`. Since row restriction is a contraction, the two largest singular values of `R` are at most one. Hence

`sigma_min(R) >= |det R| >= sqrt(delta)`.                               (4.2)

The physical principal block is

`A[I,I]=R Lambda R^T`,

so

`sigma_min(A[I,I]) >= sigma_min(R)^2 sigma_min(Lambda) >= delta`.       (4.3)

Account03/B02 r14 therefore gives the actual inequality

`boxed( ||p_Q||_infinity <=128*2^(1/4) delta^(-1) ).`                   (4.4)

Thus the rank-three Pluecker measure has two rigorously paid extremes:

* one atom of mass `>=delta`: localized partner theorem (4.4);
* a bank of aggregate mass `m_L` whose conditional one-coordinate star masses are all `<=1/4`: integrated-Fourier theorem (3.3).

The missing geometry is concentration in *stars/overlaps* rather than in one atom or a diffuse bank.

## 5. Applying the theorem to the partner r13 near-isotropic branch

The partner r13 theorem identifies an exact-rank-three overlap-one alternative in which exterior mass can be concentrated on physical pivots with `|A_ii|` arbitrarily small. Its unpaid question was how to spend that mass without dividing by the small scalar pivot.

Fix such a pivot `i`, and take

`L=[n] \ {i}`.

Then

`S_L=I-u_i u_i^T`,
`m_L=det(I-u_i u_i^T)=1-c_i`, where `c_i=||u_i||^2`.                    (5.1)

For every `j!=i`, Sherman--Morrison gives the exact conditional leverage

`rho_j(L)=c_j + <u_i,u_j>^2/(1-c_i)`.                                  (5.2)

Therefore, whenever

`1-c_i >= mu >0`                                                        (5.3)

and

`c_j + <u_i,u_j>^2/(1-c_i) <=1/4` for every `j!=i`,                    (5.4)

Theorem 3.1 closes this near-zero-pivot branch **without using `A_ii` at all**:

`boxed( ||p_Q||_infinity <= [3 B_RV^2/(4 pi^2)] mu^(-1/3) ).`          (5.5)

Hence the partner's near-isotropic overlap-one debt is reduced to the explicit alternatives

1. `c_i>1-mu` (one spectral row is itself almost total in a direction), or
2. there exists a second coordinate `j` with the conditional concentration in (5.2) exceeding `1/4`.

This is a true second-coordinate/overlap concentration statement, not a vague request for a good local minor. It is precisely the regime in which overlap-two, pair-log, ridge, or recursive bank extraction should be spent next.

## 6. Greedy bank extraction as a finite concentration certificate

There is also a useful deterministic bookkeeping consequence. Start with a bank `L_0` of positive exterior mass. If (3.1) fails, choose `i_k in L_k` with `rho_{i_k}(L_k)>1/4` and set `L_{k+1}=L_k\{i_k}`. By (2.4),

`m_{L_{k+1}} = m_{L_k}(1-rho_{i_k}(L_k)) < (3/4)m_{L_k}`.              (6.1)

Thus for any prescribed `mu>0`, after at most

`ceil(log(mu/m_{L_0}) / log(3/4))`

failed balance tests, either a bank satisfying (3.1) has appeared, or the remaining third-exterior mass is below `mu`. The removed coordinates form a constant-size star-concentration certificate when `mu` is fixed. This does not itself prove the target: a small residual determinant may mean one spectral direction is concentrated on those coordinates while the other two remain diffuse. But it replaces an unstructured large-leverage obstruction by an explicit finite chain of Pluecker-star concentrations.

## 7. Regression check (not part of the proof)

`CHECK.py` verifies, on deterministic random orthonormal frames, the two algebraic identities used in Section 2:

* Cauchy--Binet `det S_L = sum_{I subset L} w_I`;
* conditional star fraction `rho_i(L)=u_i^T S_L^{-1}u_i`.

`CHECKS.txt` records exact output. Maximum observed numerical error was below `8e-16`. These computations are regression evidence only; Sections 2--6 are analytic.

## 8. First unpaid implication

For exact rank three, the next source-valid implication is now sharply localized:

`QFORM-PLUCKER-STAR-CONCENTRATION-RECURSION-v1` — when every bank retaining O(1) third-exterior mass has some conditional star fraction `>1/4`, convert the resulting finite chain of original-coordinate star concentrations into either the partner's localized principal-3x3 certificate, the already-proved overlap-one/pair/ridge certificates, or a second aggregate bank carrying an integrability credit. Do this without selecting a vanishing minor and without normalizing a conditional density fiber.

For the full owner target with arbitrary extra eigendirections, an additional dependence debt remains: the exact-rank-three component cannot simply be convolved with the rest because both spectral pieces depend on the same original coordinates.

No target-valid counterexample to the unweighted target-wide `int |phi_Q|` criterion was found in this run. The stronger Fourier criterion therefore remains open, not refuted.

## 9. Status

* `QFORM-CONDITIONAL-PLUCKER-BANK-FOURIER-v1`: **PROVED SUPPORTING THEOREM**.
* Large-Pluecker-atom inequality (4.4): **ESSENTIAL_STEP_APPLIED**, using the completed named partner account03/B02 r14.
* Partner-r13 near-isotropic diffuse-complement subbranch (5.5): **ESSENTIAL_STEP_APPLIED**.
* Full exact-rank-three theorem: **OPEN** outside the union of the completed branches.
* Full arbitrary-spectrum owner target: **OPEN**.
* Continuity: proved for the new Fourier branch only.

No novelty or publication-priority claim is made.
