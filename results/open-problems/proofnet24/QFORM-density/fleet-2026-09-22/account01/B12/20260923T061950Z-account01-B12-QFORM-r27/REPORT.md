# account01/B12 — reciprocal-saturation stability for arbitrary signed added eigenvalues

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T061950Z-account01-B12-QFORM-r27`  
Assignment: Additional eigenvalue control  
Status: **PROVED_SUPPORTING_THEOREMS / FULL_QFORM_OPEN / NOT_INDEPENDENTLY_REVIEWED**  
Continuity: **not claimed**; the density conclusions below are essential-supremum bounds.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact question attacked

The full target is the universal bound for the density of `Q=X^T A X` for arbitrary independent real coordinates with one-dimensional density cap one whenever `A` has at least three eigenvalues of absolute value at least one. The present run attacks only the assigned stability question: when an already useful ORIGINAL-coordinate physical block is present, how can one add simultaneously

* finitely many spectral directions with arbitrarily large coefficients and arbitrary signs, and
* arbitrarily many further spectral directions of either sign,

without rotating the random variables and without pretending that the resulting quadratic remainder is independent?

The mechanism is deliberately different from r26. Run r26 obtained magnitude-free multirank control under a **sign-compatible Krein condition** on the inverse-leverage matrix. Here I drop sign compatibility completely. The replacement is a reciprocal-size hypothesis: if all active added coefficients are sufficiently large in modulus and the inverse-leverage matrix is nonsingular, then the Woodbury middle matrix is uniformly invertible no matter what the signs of those coefficients are. Small spectral coefficients are handled as one operator-norm tail. Thus the genuinely dangerous scale is intermediate, not arbitrarily large.

Fresh owner control before publication: brain main `397d7ddcb7b107f7491a1e8ef34f00731013b27b`, OWNER CONTROL revision `2026-09-22.15`, programme revision `2026-09-22.5`. The live correction inbox was re-read at that commit. No step below uses post-rotation independence, a convolution with a dependent remainder, a pointwise van-der-Corput bound, a normalized conditional-density cap, or a naive fiber-supremum argument.

## 2. Sources actually consumed

The designated completed partner source is

`yspennstate/math-open-problems@06fbcbb277d5db4f89dfc0c04b14174cc4315cc7`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T045101Z-account02-B12-auto11/REPORT.md`.

Its exact rank-one sign-routing construction uses

`C = [[4,-3,-3,3],[-3,4,-3,3],[-3,-3,4,3],[3,3,3,-8]]`,

`v=(1,1,1,1)^T/2`,

and proves

`spec(C+tau vv^T)={1+tau,7,7,-11}`.

For every real `tau`, choosing physical triple `H_-={1,2,3}` when `tau<=0` and `H_+={2,3,4}` when `tau>=0` leaves all three singular values of that selected physical block at least `2`.

The terminal localized density theorem used below is Theorem A in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`:

if an ORIGINAL-coordinate physical `3 x 3` principal quadratic block has all eigenvalue magnitudes at least `c>0`, then, after conditioning on all other original coordinates, arbitrary induced affine terms are allowed and

`||p_Q||_infinity <= 6 sqrt(pi)/c`.

The proof below uses this only after deterministic original-coordinate matrix estimates.

## 3. Main matrix theorem: joint large-magnitude saturation without sign compatibility

### Theorem 3.1 (`QFORM-RECIPROCAL-SATURATION-v1`)

Let `B=B^T` be an invertible real `m x m` matrix, let `U` be a real `m x r` matrix, and let `Theta=Theta^T` be an invertible real `r x r` matrix. Define the inverse-leverage matrix

`K := U^T B^{-1} U`.

Assume only that `K` is invertible and put

`kappa := sigma_min(K)>0`,

`eta := ||Theta^{-1}||op`.

If

`eta < kappa`,                                                     (3.1)

then

`B_Theta := B + U Theta U^T`

is invertible and

`boxed:
 sigma_min(B_Theta)
 >= gamma(B,U,K,Theta)
 := [ ||B^{-1}||op
      + ||B^{-1}U||op^2/(kappa-eta) ]^{-1}.`                       (3.2)

There is **no sign condition** on `Theta` and no sign condition on `K`. In particular positive and negative added eigenvalues may occur simultaneously. The only coefficient-size input is reciprocal: their joint active matrix must satisfy `||Theta^{-1}||<sigma_min(K)`.

#### Proof

The Woodbury identity gives

`(B+U Theta U^T)^{-1}
 = B^{-1}
   - B^{-1}U (Theta^{-1}+U^T B^{-1}U)^{-1} U^T B^{-1}`,           (3.3)

provided the middle matrix is invertible. Put

`M := Theta^{-1}+K`.

For every vector `x`,

`||Mx|| >= ||Kx|| - ||Theta^{-1}x||
          >= (kappa-eta)||x||`.

Therefore

`sigma_min(M) >= kappa-eta >0`,                                  (3.4)

so `M` is invertible and

`||M^{-1}||op <= 1/(kappa-eta)`.                                 (3.5)

Now take operator norms in (3.3). Since `B` is symmetric,

`||U^T B^{-1}||op = ||B^{-1}U||op`,

and hence

`||(B+U Theta U^T)^{-1}||op
 <= ||B^{-1}||op
    + ||B^{-1}U||op^2 ||M^{-1}||op
 <= ||B^{-1}||op
    + ||B^{-1}U||op^2/(kappa-eta).`                               (3.6)

Taking reciprocals proves (3.2). QED.

### Corollary 3.2 — uniform saturation threshold

If every active eigenvalue of `Theta` has magnitude at least `2/kappa`, then

`eta=||Theta^{-1}||op <= kappa/2`,

so Theorem 3.1 gives the completely magnitude-independent floor

`boxed:
 sigma_min(B+U Theta U^T)
 >= gamma_infty
 := [ ||B^{-1}||op + 2||B^{-1}U||op^2/kappa ]^{-1}.`              (3.7)

Once the active coefficients have crossed the finite threshold `2/kappa`, making them larger can no longer damage this certificate, regardless of their individual signs.

### Exact resonance identity

The matrix determinant lemma gives

`det(B+U Theta U^T)
 = det(B) det(Theta) det(Theta^{-1}+K).`                            (3.8)

Consequently any singularity of the physical block satisfies

`det(Theta^{-1}+K)=0`.

In particular a singularity forces

`||Theta^{-1}||op >= sigma_min(K)=kappa`;                          (3.9)

otherwise (3.4) would rule it out. Thus a simultaneous large-magnitude spectral cloud cannot create a resonance when the inverse-leverage matrix is nonsingular.

This is the precise sense in which large coefficients **saturate**. It is not a probabilistic statement and does not use independence in a rotated eigenbasis.

## 4. Small-plus-large spectral split

### Theorem 4.1 (`QFORM-SMALL-LARGE-SPECTRAL-SPLIT-v1`)

Keep `B,U,Theta,K,kappa` as in Theorem 3.1. Let `R` and `T` be arbitrary real symmetric matrices of compatible size with

`||R||op <= epsilon`,

`||T||op <= delta`.

Assume `eta<kappa`, define `gamma` by (3.2), and suppose

`epsilon+delta < gamma`.                                          (4.1)

Then

`boxed:
 sigma_min(B+U Theta U^T+R+T)
 >= gamma-epsilon-delta.`                                         (4.2)

#### Proof

Theorem 3.1 gives the gap `gamma` before `R+T`. The standard singular-value perturbation inequality gives

`sigma_min(C+R+T) >= sigma_min(C)-||R+T||op
                  >= gamma-epsilon-delta`.

QED.

### Spectral-cloud formulation

Let an arbitrary symmetric added matrix have spectral decomposition

`E = sum_j theta_j v_j v_j^T`,                                    (4.3)

with the `v_j` orthonormal. Choose an active index set `L`. Put

`V_L=(v_j)_{j in L}`, `Theta_L=diag(theta_j:j in L)`,

and put all remaining eigen-directions into

`R_L = sum_{j notin L} theta_j v_jv_j^T`.

Then exactly

`||R_L||op = max_{j notin L}|theta_j| =: epsilon_L`.               (4.4)

On a chosen physical block `I`, set

`B=A0[I,I]`, `U=V_L[I,:]`, `K=U^T B^{-1}U`.

If `K` is nonsingular, `kappa=sigma_min(K)`, and

`min_{j in L}|theta_j| >= 2/kappa`,                               (4.5)

then every active eigenvalue is free to be arbitrarily larger, with either sign, and every number of inactive eigenvalues of either sign costs only the single number `epsilon_L`. The number of inactive directions does not appear.

This is exactly the requested "smaller and larger eigenvalues" separation: **large active directions are paid by inverse leverage, not by their magnitude; an arbitrary-rank small tail is paid only by its operator norm.**

## 5. Original-coordinate density corollary

### Corollary 5.1 (`QFORM-RECIPROCAL-SATURATION-CORE-v1`)

Let `I` be an ORIGINAL-coordinate physical triple and let

`B=A0[I,I]`

be invertible. Write an arbitrary added matrix as

`E = V_L Theta_L V_L^T + R_L + T`,                                (5.1)

where `V_L` consists of orthonormal global spectral directions, `Theta_L` is diagonal with nonzero entries, `R_L` is the remaining spectral cloud, and `T` is any additional symmetric dense tail. Put

`U=V_L[I,:]`, `K=U^T B^{-1}U`, `kappa=sigma_min(K)>0`,

`eta=||Theta_L^{-1}||op`,

and

`gamma=[||B^{-1}||op+||B^{-1}U||op^2/(kappa-eta)]^{-1}`.

If

`eta<kappa`,

`epsilon:=||R_L||op`,

`delta:=||T||op`,

and

`epsilon+delta<gamma`,                                             (5.2)

then the actual physical triple has

`sigma_min(A[I,I]) >= gamma-epsilon-delta`,                        (5.3)

and the full ambient quadratic form obeys

`boxed:
 ||p_(X^T A X)||infinity
 <= 6 sqrt(pi)/(gamma-epsilon-delta).`                             (5.4)

#### Proof

Theorem 4.1 gives (5.3). Condition on every original coordinate outside `I`. The three coordinates in `I` remain independent with their original density caps. All outside quadratic and cross terms become a constant plus arbitrary affine terms in those three coordinates. The localized physical-three-coordinate theorem applies uniformly in that conditioning and gives (5.4). Averaging over the conditioned coordinates proves the assertion. QED.

No random variable was rotated in this proof. The spectral decomposition is used solely to write a deterministic matrix addition.

### Uniform threshold version

Under (4.5), define

`gamma_infty=[||B^{-1}||op+2||B^{-1}U||op^2/kappa]^{-1}`.

If

`epsilon_L+delta<gamma_infty`,                                    (5.5)

then

`boxed:
 ||p_Q||infinity
 <= 6 sqrt(pi)/(gamma_infty-epsilon_L-delta).`                    (5.6)

This bound is uniform as every active `|theta_j|` tends to infinity independently and with arbitrary signs.

## 6. Rank-one small/large dichotomy and exact necessity of nonzero inverse leverage

For one update direction `u`, write

`q=u^T B^{-1}u`.

If `q != 0`, Theorem 3.1 applies to **both signs** of the scalar coefficient `tau` as soon as

`|tau| > 1/|q|`,

and the uniform threshold form applies for

`|tau| >= 2/|q|`.                                                  (6.1)

At the other end, Weyl gives

`sigma_min(B+tau uu^T)
 >= sigma_min(B)-|tau| ||u||^2`.                                  (6.2)

Hence

`|tau| <= sigma_min(B)/(2||u||^2)`                                (6.3)

implies a gap at least `sigma_min(B)/2`. Thus, for a fixed physical rank-one direction with `q !=0`, arbitrarily small coefficients and arbitrarily large coefficients of either sign are automatically safe. Only a finite intermediate coefficient interval can threaten that one-core certificate.

The exact Sherman-Morrison denominator is

`1+tau q`,

so the only singular coefficient is

`tau=-1/q`.                                                        (6.4)

This makes the intermediate-resonance mechanism explicit.

### Why `q != 0` is genuinely needed

Take

`B=diag(1,-1)`,

`u=(1,1)^T/sqrt(2)`.

Then

`q=u^T B^{-1}u=0`,

but

`B+tau uu^T
 = [[1+tau/2,tau/2],[tau/2,-1+tau/2]]`.

Its determinant is `-1`, while its eigenvalues are

`lambda_+- = (tau +- sqrt(tau^2+4))/2`.                            (6.5)

As `|tau| -> infinity`, one eigenvalue has magnitude asymptotic to `|tau|` and the other has magnitude asymptotic to `1/|tau|`. Therefore

`sigma_min(B+tau uu^T) -> 0`.                                     (6.6)

So it is false that a huge added eigenvalue is harmless to every fixed physical core. Nondegenerate inverse leverage (or another certificate switch) is essential. This is only a local-certificate obstruction, not a counterexample to QFORM.

## 7. Required actual application of the completed account02/B12 result, now with a second literal eigenvalue replacement

Return to the partner's exact matrix `C` and vector `v`. Define a second global unit vector

`w=(0,1,-1,0)^T/sqrt(2)`.                                         (7.1)

A direct calculation gives

`Cw=7w`,

`w perpendicular v`.                                              (7.2)

Therefore `v,w` are orthonormal eigenvectors of `C`, and for every real `tau,s`,

`boxed:
 spec(C+tau vv^T+sww^T)
 = {1+tau, 7+s, 7, -11}.`                                         (7.3)

Thus `tau` and `s` are **literal independent eigenvalue replacements**, not merely arbitrary low-rank coefficients.

The partner theorem chooses `H_-={1,2,3}` for `tau<=0` and `H_+={2,3,4}` for `tau>=0` and proves that the selected block of `C+tau vv^T` has all singular values at least `2`.

On `H_-`,

`w[H_-]=(0,1,-1)^T/sqrt(2)`

is an eigenvector of the selected block with eigenvalue `7`, and it is orthogonal to `v[H_-]=(1,1,1)^T/2`.

On `H_+`,

`w[H_+]=(1,-1,0)^T/sqrt(2)`

again is an eigenvector with eigenvalue `7` and is orthogonal to `v[H_+]`.

Hence on **either sign-selected partner core**, the second update `sww^T` changes exactly one local eigenvalue, from `7` to `7+s`, and leaves the other two local eigenvalues unchanged. Therefore whenever

`|7+s| >= 2`, equivalently `s notin (-9,-5)`,                    (7.4)

the selected physical triple still has all three singular values at least `2`.

Now add an arbitrary symmetric dense `4 x 4` matrix `E` with

`||E||op <= 1/4`.                                                  (7.5)

The selected physical triple of

`A=tau,s,E := C+tau vv^T+sww^T+E`

has

`sigma_min(A[I_tau,I_tau]) >= 2-1/4=7/4`.                         (7.6)

Applying the localized physical-three-coordinate theorem at this actual inequality gives

`boxed:
 ||p_(X^T A X)||infinity
 <= 6 sqrt(pi)/(7/4)
 = 24 sqrt(pi)/7
 = 6.076984631676055...`                                          (7.7)

for every independent cap-one product input, every real `tau`, every `s notin(-9,-5)`, and every dense tail satisfying (7.5).

This is the required completed `account02/B12` result applied to an actual new density inequality. It extends the partner family from one arbitrary literal eigenvalue replacement to two: `1+tau` is completely unrestricted, while `7+s` can be arbitrarily small or arbitrarily large and can have either sign, except for the finite resonance window (7.4) of this particular certificate.

The family stays inside the exact QFORM target throughout this stated region. Before `E`, the three eigenvalues `7`, `-11`, and `7+s` have magnitudes at least `2,7,11`; hence

`s_3(C+tau vv^T+sww^T) >= 2`.

By singular-value perturbation,

`s_3(A) >= 2-1/4=7/4>1`,                                         (7.8)

uniformly in `tau` and allowed `s`.

### Direct application of the new saturation theorem to the same family

On either partner-selected core, the vector `w[I_tau]` has norm one and is an eigenvector with eigenvalue `7`. Consequently

`q_w = w[I_tau]^T B_tau^{-1} w[I_tau] = 1/7`,                     (7.9)

where `B_tau=(C+tau vv^T)[I_tau,I_tau]`. The partner gap gives

`||B_tau^{-1}||op <= 1/2`,

and

`||B_tau^{-1}w[I_tau]||=1/7`.

For `|s|>=14`, Theorem 3.1 has

`kappa=1/7`, `eta<=1/14`,

and therefore

`gamma >= [1/2 + (1/49)/(1/14)]^{-1}
          = [1/2+2/7]^{-1}
          = 14/11`.                                               (7.10)

After the arbitrary dense tail of norm `1/4`,

`sigma_min >= 14/11-1/4 = 45/44`.                                 (7.11)

Thus the new general theorem alone gives the sign-agnostic large-`|s|` density inequality

`boxed:
 ||p_Q||infinity
 <= 6 sqrt(pi)/(45/44)
 = 264 sqrt(pi)/45
 = 10.398395925312359... .`                                       (7.12)

The exact commuting-eigenline calculation (7.4)-(7.7) is sharper and expands the safe range from `|s|>=14` to all `s notin(-9,-5)`, but (7.12) is the direct generic reciprocal-saturation application.

## 8. Interpretation for the assignment

The new theorem provides a clean separation of added spectral scales.

* **Large active eigenvalues:** once their moduli exceed a finite inverse-leverage threshold and `K` is nonsingular, their magnitudes disappear from the estimate. Their signs are arbitrary and need not match the inertia of `K`.
* **Small spectral cloud:** any number of remaining positive or negative eigenvalues costs only their maximum modulus, because their orthogonal spectral sum has operator norm equal to that maximum.
* **Dense nonseparable error:** an arbitrary additional symmetric tail costs only its matrix operator norm. No claim is made that the random quadratic tail is small.
* **Intermediate resonance:** a large coefficient can still be dangerous if the relevant inverse leverage vanishes, as (6.5)-(6.6) shows. Hence a full proof must switch certificates in such a high-degeneracy case rather than insisting on one fixed core.

This is stronger than the r26 sign-compatible theorem in a complementary direction: r26 allowed arbitrary magnitudes including coefficients near zero but required a Krein sign condition; r27 requires sufficiently large moduli for the active directions but **removes sign compatibility entirely**.

## 9. What remains unpaid

The full QFORM conjecture is still open. From only the global hypothesis `s_3(A)>=1`, the fleet still needs a universal structural compiler that forces at least one of the paid endpoints. For the present mechanism, that missing statement would have to produce an ORIGINAL-coordinate physical core `I` and an active spectral subset whose inverse-leverage matrix

`K=V_L[I,:]^T A0[I,I]^{-1} V_L[I,:]`

is quantitatively nonsingular, while every omitted spectral direction is small enough in operator norm; or else it must route the matrix into one of the already-controlled grouped-bank, ridge, hub, cross-volume, or localized-core mechanisms. The live correction set already contains exact families showing that no single uniformly good fixed principal triple can be demanded universally.

The boundary example in Section 6 explains one concrete obstruction: if the inverse leverage is zero, arbitrarily large spectral additions can actually make a fixed physical block arbitrarily close to singular. Therefore a successful global proof needs either quantitative nonzero inverse leverage or an aggregate/certificate switch before paying a reciprocal gap.

No counterexample to the full conjecture was found or constructed here.

## 10. Continuity and proof status

The density conclusions in this report are **essential boundedness** statements inherited from the localized physical-three-coordinate theorem. This report does **not** prove that the density has a continuous representative. Continuity therefore remains a separate unresolved requirement of the owner target.

Status of the new claims: `PROVED_SUPPORTING_THEOREMS / FULL_QFORM_OPEN / NOT_INDEPENDENTLY_REVIEWED`.

## 11. Finite algebraic sanity check (not a proof premise)

The exact family was checked directly: `Cv=v`, `Cw=7w`, `v perpendicular w`, and for a grid of `tau,s` the spectrum agreed to numerical precision with `{1+tau,7+s,7,-11}`. In addition, 5,000 random matrix instances satisfying `sigma_min(K)>0` and `||Theta^{-1}||<sigma_min(K)` were tested against (3.2); no numerical violation was seen. These checks are corroborative only; all conclusions above follow from the displayed identities and inequalities.

## 12. Provenance

Initial brain control commit consumed: `84597da00ef1ab282d3a84481920d438fa8ec9c5`.

Prepublication brain control commit consumed: `397d7ddcb7b107f7491a1e8ef34f00731013b27b`.

Designated partner source: `yspennstate/math-open-problems@06fbcbb277d5db4f89dfc0c04b14174cc4315cc7`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T045101Z-account02-B12-auto11/REPORT.md`.

Localized terminal theorem source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, path `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

Native-brain receiver use was not authenticated, so execution remains `WITHOUT_VERIFIED_BRAIN`.
