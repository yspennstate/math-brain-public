SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-23T15:15:55Z.
attacking: spectral-square monotone extension — absorb arbitrary additional signed eigenvalues at zero cost when they lie in the spectral complement of a carrier core, and pay general noncommuting tails only through the negative localized anticommutator.

# fleet01/B12 — spectral-square monotone extension and localized anticommutator stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260923T151555Z-fleet01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Continuity: **not claimed for this theorem as a whole**. The designated partner's D5 exit gives continuity; its physical-core/pair exits give essential boundedness only.


## 1. First essential missing implication attacked

A recurring obstruction in additional-eigenvalue control is that a matrix remainder `R` can have enormous operator norm and `X^T R X` cannot be treated as a small independent convolution error. The useful current receivers instead depend on deterministic physical-coordinate matrix certificates. The question attacked here is:

> When a baseline matrix already has a spectral-square carrier, which additional signed eigenvalues can be added without degrading that carrier, and how should a genuinely noncommuting matrix tail be charged?

The answer is stronger than ordinary Weyl stability. Orthogonal spectral additions cost **exactly zero**, regardless of their signs, ranks, multiplicities or magnitudes. A general noncommuting addition is charged only through the **negative part of a localized anticommutator**, not through its global operator norm.

## 2. Localized anticommutator carrier theorem

Let `A0=A0^T`, `R=R^T`, and

`A=A0+R`.

Let `H` be a set of ORIGINAL coordinates and `P=P_H` its coordinate projection. Define the localized anticommutator

`K_H := P(A0 R+R A0)P |_{Ran P}`

and its negative-part size

`nu_H := ||(K_H)_-||op = max(0,-lambda_min(K_H))`.

### Theorem 2.1 — QFORM-LOCALIZED-ANTICOMMUTATOR-CARRIER-STABILITY-v1

For every `j<=|H|`,

`lambda_j( A^2[H,H] ) >= lambda_j( A0^2[H,H] ) - nu_H`.       (2.1)

In particular, if

`lambda_6(A0^2[H,H]) >= g0^2 > nu_H`,

then the ACTUAL final matrix satisfies

`lambda_6(A^2[H,H]) >= g0^2-nu_H`.                            (2.2)

Hence every density receiver whose deterministic premise is a lower bound on the sixth physical spectral-square mode may be applied to the final matrix with

`g = sqrt(g0^2-nu_H)`,

provided its other hypotheses are checked on the final matrix.

### Proof

The exact identity is

`A^2 = A0^2 + (A0R+RA0) + R^2`.                              (2.3)

Because `R=R^T`, `R^2>=0`, so after physical-coordinate compression,

`P R^2 P >=0`.                                                 (2.4)

By definition of `nu_H`,

`P(A0R+RA0)P >= -nu_H P`.                                    (2.5)

Combining (2.3)-(2.5),

`P A^2 P >= P A0^2 P - nu_H P`.                              (2.6)

The min-max principle (equivalently monotonicity of ordered eigenvalues under Loewner order) gives (2.1), and `j=6` gives (2.2). QED.

The theorem is genuinely local. `||R||op` may be arbitrarily large. Only a negative localized anticommutator can erode the carrier. Positive anticommutator contribution is harmless, and the positive term `R^2` can only help.

## 3. Zero-loss corollaries for arbitrary additional spectrum

### Corollary 3.1 — orthogonal spectral remainder costs zero

If

`A0 R=0`,

then, by symmetry, also `R A0=0`; hence `nu_H=0` for every `H`, and

`A^2=A0^2+R^2 >= A0^2`.                                      (3.1)

Therefore

`lambda_j(A^2[H,H]) >= lambda_j(A0^2[H,H])`                  (3.2)

for every physical set `H` and every `j`.

This is exactly the situation obtained by splitting the **final matrix itself** into disjoint spectral packets. If

`A = sum_k lambda_k u_k u_k^T`

and `S` is any subset of eigenmodes, put

`A_S = sum_{k in S} lambda_k u_k u_k^T`,
`A_{S^c}=A-A_S`.

Then `A_S A_{S^c}=0`, and consequently

`A^2 = A_S^2 + A_{S^c}^2 >= A_S^2`.                          (3.3)

Thus **all unselected eigenvalues are free at the spectral-square-carrier level**: they may be smaller or larger, positive or negative, repeated, arbitrarily numerous, and arbitrarily large. No convolution statement appears.

### Corollary 3.2 — weighted physical footprint of a chosen spectral packet

Let `U_S` have the selected eigenvectors as columns and let

`D_S=diag(|lambda_k|: k in S)`.

For every physical set `H`,

`A_S^2[H,H]
 = (P_H U_S D_S)(P_H U_S D_S)^T`.                            (3.4)

Therefore

`lambda_6(A^2[H,H])
 >= s_6(P_H U_S D_S)^2`.                                     (3.5)

In the common special case of exactly six selected modes with `|lambda_k|>=s0`, if

`alpha_H := s_6(P_H U_S)>0`,

then

`lambda_6(A^2[H,H]) >= s0^2 alpha_H^2`.                      (3.6)

The signs of the six selected eigenvalues themselves are irrelevant to this carrier bound, and increasing any of their absolute values can only improve (3.5).

### Corollary 3.3 — anticommuting huge additions also cost zero

The orthogonal-support condition is not necessary. If instead

`A0R+RA0=0`,

then again `nu_H=0` for every `H` and

`A^2=A0^2+R^2>=A0^2`.                                        (3.7)

So even an arbitrarily large **noncommuting** signed addition is free whenever it anticommutes with the carrier core.

Example: on two equal banks take

`A0=diag(I,-I)`, `R=[[0,C],[C^T,0]]`.

Then `{A0,R}=0`, while `||C||` is arbitrary. The final eigenvalues are `+-sqrt(1+sigma_j(C)^2)`, and every spectral-square lower bound of `A0` survives.

## 4. Applying the completed fleet02/B12 theorem to an actual inequality

The designated completed partner result is:

`QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1`

at

`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T145451Z-fleet02-B12-QFORM-r36/REPORT.md`.

Its relevant statement is the following. If the ACTUAL final symmetric matrix has `s3(A)>=s>0`, an ORIGINAL-coordinate carrier `H`, `|H|=m>=6`, and a certificate `0<=G<=A^2` with

`lambda_6(G[H,H])>=g^2`,

then, writing `N=binom(m,2)`, for `0<a<b/N`, `0<b<g`, and `kappa=b/N-a`,

`||p_Q||inf <= max {`
`  2sqrt(6 pi m)/a,`
`  pi/kappa,`
`  3*400^(1/3) kappa^(-5/6) s^(-1/6),`
`  5sqrt(2e)/sqrt(g^2-b^2)`
`}.`                                                           (4.1)

I now apply (4.1) to an actual family in which **every additional eigenvalue is unrestricted**.

Take twelve original coordinates split into

`H={e_1,...,e_6}`, `F={f_1,...,f_6}`,

and define orthonormal vectors

`u_j=(e_j+f_j)/sqrt(2)`, `j=1,...,6`.

Let `U=span{u_1,...,u_6}` and

`A0=P_U`.

Now let `R=R^T` be **arbitrary subject only to `R U=0`**. Equivalently, `R` is any symmetric operator on `U^perp`. It may have arbitrary dimension after appending spectator coordinates, arbitrary rank, arbitrary eigenvectors inside `U^perp`, arbitrary positive and negative eigenvalues, and arbitrarily large norm. Put

`A=A0+R`.                                                     (4.2)

Because `R U=0` and `R` is symmetric,

`A0R=RA0=0`.                                                  (4.3)

Hence the final spectrum contains six exact eigenvalues `+1`, while every other eigenvalue is arbitrary. In particular,

`s3(A)>=1`.                                                    (4.4)

Also

`A^2=P_U+R^2>=P_U`.                                           (4.5)

The physical compression of `P_U` to `H` is exactly

`P_H P_U P_H = (1/2) I_6`.                                  (4.6)

Thus (4.5)-(4.6) give an actual partner certificate with

`G=P_U`, `g^2=1/2`, `m=6`, `N=15`, `s=1`.                   (4.7)

Choose the exact parameters

`b=7/10`, `a=23/750`, `kappa=b/15-a=2/125`.                 (4.8)

They satisfy

`0<a<b/15`, `0<b<1/sqrt(2)`.

The four terms in (4.1) become

`T1 = 9000 sqrt(pi)/23 = 693.5688981804...`,

`T2 = 125 pi/2 = 196.3495408494...`,

`T3 = 3*400^(1/3)*(125/2)^(5/6)
    = 693.4916978615...`,

and because `g^2-b^2=1/2-49/100=1/100`,

`T4 = 50 sqrt(2e) = 116.5821990799...`.                      (4.9)

Therefore the completed partner theorem gives the actual law-uniform inequality

`boxed( ||p_{X^T A X}||inf < 694 )`                           (4.10)

for **every** independent cap-one product input and **every** symmetric `R` satisfying `RU=0`, irrespective of the signs, multiplicities, or magnitudes of all the additional eigenvalues.

This is a literal use of the partner theorem at an inequality. The remainder is not treated as an independent random variable, and no rotation of the input vector is used.

## 5. General partner compiler with a noncommuting tail

Combining Theorem 2.1 with the partner theorem yields a useful general form.

Suppose the final `A=A0+R` satisfies `s3(A)>=s>0`, and an ORIGINAL-coordinate `H`, `|H|=m>=6`, obeys

`lambda_6(A0^2[H,H]) >= g0^2`.

Let `nu_H` be the negative localized anticommutator size from Section 2 and suppose

`nu_H<g0^2`.

Then set

`g=sqrt(g0^2-nu_H)`.                                         (5.1)

Taking `G=A^2` itself, Theorem 2.1 verifies the partner hypothesis

`lambda_6(G[H,H])>=g^2`.                                     (5.2)

Consequently every choice `0<a<b/N`, `0<b<g` gives the partner bound (4.1) for the full final form.

The point is that this may remain quantitative even when `||R||op` is enormous. Only the **harmful negative interaction** of `R` with the carrier core on `H` is charged. The always-positive square `R^2` is retained instead of discarded.

A crude global estimate is available,

`nu_H <= ||A0R+RA0||op <=2||A0||||R||`,

but this throws away the purpose of the theorem. The useful quantity is the actual compressed negative part, which can be zero while `||R||` tends to infinity.

## 6. Why this is not the full QFORM proof

The owner hypothesis provides only

`s3(A)>=1`,

i.e. three global large eigenmodes. A selected three-mode spectral packet has square rank at most three and cannot by itself create a six-mode carrier. Thus (3.5) does **not** manufacture the partner's six-mode premise from the bare target hypothesis.

The remaining structural implication is:

> From only three global eigenvalues of modulus at least one, force either a bounded physical six-mode spectral-square carrier (to which the zero-loss additional-spectrum theorem above applies), **or** one of the already-paid D5 / fractional-volume / ridge / grouped-bank-hub / physical-pair / rank-two-half-Riesz / scalar-Schur exits.

Known correction families prohibit replacing this by an assertion that one universally good small principal minor or one rank-three cross cut always exists.

So the result here settles a real **additional-eigenvalue bookkeeping problem** for every spectral-square-carrier branch, but it does not settle the remaining three-to-six structural extraction. Full QFORM and unrestricted continuity remain open.

## 7. Scope and correction compliance

- Original-coordinate product structure is preserved throughout.
- No input moment, centering, compact-support, connected-support, log-concavity, Gaussianity, or identical-law assumption is made.
- No eigen-coordinate independence is asserted.
- No small operator-norm matrix is converted into a law-uniformly small quadratic random variable.
- No pointwise scalar stationary-phase estimate is used.
- No arbitrary-joint coarea or positive conditional-density-moment premise is used.
- Repeated eigenvalues cause no problem.
- The result is deterministic matrix stability feeding an existing product-law receiver.

## 8. Sources and review status


Designated partner actually applied:

`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T145451Z-fleet02-B12-QFORM-r36/REPORT.md`.

Early substantive checkpoint for this run was committed before this report at math-open-problems commit `af4c24c90c90a4aecfdc281a92363f3c78b4a2ba`, same run directory.

Independent end-to-end review of this new theorem: **not supplied by this run**. A full candidate proof would still require two independent complete reviews.

Execution/memory status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval and writes are not claimed to be native learned-memory ingestion.
