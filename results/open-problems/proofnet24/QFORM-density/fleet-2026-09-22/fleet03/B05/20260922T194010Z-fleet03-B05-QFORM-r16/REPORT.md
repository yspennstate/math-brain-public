SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-22T19:40:10Z.
attacking: weighted moving-critical-value coarea via an original-coordinate indefinite pair, together with the requested independent check of the arbitrary-rank pair-log extension.

# fleet03/B05 — pair-coarea repair of the near-zero scalar-pivot loss

Run: `20260922T194010Z-fleet03-B05-QFORM-r16`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Quadratic coarea bound  
Fresh owner control before publication: revision `2026-09-22.15`; brain main observed at refresh `02852d4bd7a60a888a74262ec49c3373a63ea39b` after concurrent fleet writes, with the protected README still at blob `fca13a89d221115332ce5e60d49554ee0e213efa`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Status: **SCOPED INDEPENDENT REVIEW PASS + SUPPORTING TARGET-VALID FAMILY REPAIRED / FULL QFORM OPEN**. Continuity remains open separately.

## 1. Exact target and correction discipline

The target remains the full arbitrary-dimensional statement: independent real coordinates with one-dimensional densities at most one, and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one. No Gaussian, log-concave, compact-support, moment, sign, or post-rotation-independence hypothesis is introduced.

This run does not use the refuted arbitrary-joint rank-three coarea inequality, the refuted positive conditional-projection moment, a normalized scalar worst-fiber supremum, a fiber-supremum estimate, or law-uniform pointwise van-der-Corput decay. The preceding B05 source-status addendum proved that the absolute scalar half-Riesz interface can itself lose a logarithm as a physical scalar pivot tends to zero. The first question here is whether that loss is intrinsic to the actual quadratic form or only to the scalar completion architecture.

The answer is concrete: on the exact stress family that made the scalar half-Riesz majorant diverge, completing the **two-coordinate indefinite physical pair instead** retains the moving critical translation and gives a uniform density bound below 9.514.

## 2. Sources checked in full

### 2.1 Pair-log envelope

Canonical source:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For two independent cap-one original coordinates with an invertible indefinite symmetric pair `B`, write

`D=|det B|`, `kappa=sigma_min(B)`.

After completion against arbitrary variables independent of that original pair, if the scalar remainder `R` satisfies

`sup_t P(|R-t|<rho) <= H sqrt(rho)` for all `rho>0`,

then the supplied theorem proves

`||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.                   (2.1)

The proof comes from the pointwise conditional pair envelope

`p_pair(t) <= 2 sqrt(2)/r
             + D^(-1/2) log_+(2 r^2/(kappa |t-t0|))`,                (2.2)

followed by layer-cake averaging of the moving logarithmic singularity. The pair variables remain ORIGINAL independent coordinates; the orthogonal diagonalization in the near-region calculation is only a Lebesgue change of variables and is not used to infer independence.

### 2.2 Arbitrary-rank pair extension

Canonical source:

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

It claims: if `s_3(A)>=s>0` and an ORIGINAL-coordinate principal pair `B` is invertible indefinite, then

`||p_Q||_infinity
 <= 3*400^(1/3) (D^2 kappa s)^(-1/6)`.                              (2.3)

All additional spectrum, couplings and affine terms are allowed. I independently checked the requested proof components in Sections 3--5. The result of that review is in Section 4 below.

### 2.3 Designated partner status

The assignment names `fleet04/B05`. A fresh source search found no completed current-QFORM handoff or current-QFORM math commit from that exact slot; the only searchable `fleet04 B05` commits remain superseded BT4 work. I therefore do **not** fabricate a partner theorem or approval. The present run instead performs the owner-requested independent check of the completed interactive pair theorem and applies that theorem to an actual B05 inequality. This partner-evidence deficit is operational, not mathematical evidence against the theorem.

## 3. A uniform pair-coarea repair of the exact near-zero stress family

The preceding B05 correction used, for `0<a<=1/3`,

`A_a = [[a, sqrt(1+a), 0],
        [sqrt(1+a), 0, 0],
        [0, 0, 1]].`                                                 (3.1)

Its eigenvalues are exactly `{1+a,-1,1}`, so `s_3(A_a)=1`. For cap-one independent inputs, scalar completion in `X_0` produced an absolute half-Riesz majorant diverging logarithmically as `a downarrow 0`. The actual form is nevertheless target-valid and uniformly bounded by earlier fixed-matrix results.

The correct coarea object for this family is the whole physical pair `(X_0,X_1)`.

### Theorem 3.1 — `QFORM-NEARZERO-MOVING-TRANSLATION-PAIR-REPAIR-v1`

Let `0<a<=1/3`. Let `X_0,X_1,X_2` be independent real random variables with probability densities bounded by one. More generally allow an arbitrary affine term `ell dot X+c`. Then

`Q_a = X^T A_a X + ell dot X+c`

has an essentially bounded density satisfying

`boxed(
 ||p_(Q_a)||_infinity
 <= 8*2^(1/4) (1+a)^(-1/4)
 <= 8*2^(1/4)
 < 9.514.
)`                                                                    (3.2)

No continuity claim is made.

#### Proof

Use the original-coordinate pair `I={0,1}`. Its quadratic matrix is

`B_a=[[a,sqrt(1+a)],[sqrt(1+a),0]].`                                  (3.3)

The characteristic polynomial is

`lambda^2-a lambda-(1+a)
 =(lambda-(1+a))(lambda+1)`,                                          (3.4)

so `B_a` is indefinite with eigenvalues `1+a` and `-1`. Hence

`D=|det B_a|=1+a`,                                                    (3.5)

and, because `a>0`, its singular values are `1+a` and `1`, so

`kappa=sigma_min(B_a)=1`.                                             (3.6)

There are no quadratic cross terms from this pair to `X_2`. Completing the pair absorbs the affine terms in `X_0,X_1` into a deterministic translation of the two pair coordinates. The remainder is therefore, up to an additive constant,

`R(X_2)=X_2^2+beta X_2
       =(X_2+beta/2)^2-beta^2/4`.                                    (3.7)

For every `t` and `rho>0`, the inverse image in the real line of

`| (x+beta/2)^2 - t | < rho`

has total length at most `2 sqrt(2 rho)`. Indeed, if `t<rho` it lies in one interval of length at most `2sqrt(2rho)`; if `t>=rho`, the two symmetric intervals have total length

`2( sqrt(t+rho)-sqrt(t-rho) ) <= 2sqrt(2rho)`,                        (3.8)

with the maximum attained at the transition `t=rho`. Since the density of `X_2` is at most one,

`sup_t P(|R-t|<rho) <= 2sqrt(2) sqrt(rho)`.                           (3.9)

Thus (2.1) applies with

`H=2sqrt(2)`, `D=1+a`, `kappa=1`.                                    (3.10)

Consequently

`||p_(Q_a)||_infinity
 <=4 sqrt(4sqrt(2)) (1+a)^(-1/4)
 =8*2^(1/4)(1+a)^(-1/4)`,                                            (3.11)

which is (3.2). QED.

### What the theorem proves about the missing factor

On exactly the family where the scalar-square estimate

`a^(-1/2) E|R_a-t|^(-1/2)`

loses a logarithm, the pair-coarea calculation is uniformly finite. The improvement is not a cancellation hidden in a numerical constant. The pair envelope (2.2) keeps the moving critical value as a **logarithmic singularity whose location is averaged against the remainder law before a supremum is taken**. Scalar completion instead replaced the fixed translated density by its cap one first and thereby allowed it to saturate every moving critical translate simultaneously.

Hence the near-zero scalar-pivot obstruction is not an obstruction whenever the cross coupling can be retained as a quantitatively conditioned original-coordinate indefinite pair.

## 4. Independent review of the arbitrary-rank pair extension

I checked the complete supplied argument for (2.3), not merely its statement.

### 4.1 Arbitrary-rank quarter-power small-ball lemma — PASS

Write `L=||S||` and `M=max_i |S_ii|`.

* If `M>=L/2`, conditioning on that original coordinate gives a scalar quadratic whose inverse image of an interval of length `2rho` has total length at most `2sqrt(2rho/|S_ii|) <=4sqrt(rho/L)`. For `rho<=L`, this is at most `4(rho/L)^(1/4)`; for `rho>=L`, probability one suffices.
* If `M<L/2`, then `S_0=S-diag(S)` satisfies `||S_0||>L/2`. For a random diagonal sign matrix `E`,

  `C_E=(S_0-E S_0 E)/2`

  obeys `E C_E=S_0/2`. Convexity of operator norm forces one sign cut with `||C_E||>=||S_0||/2>=L/4`. For that original-coordinate cut, `C_E=[[0,T],[T^T,0]]` and `||T||=||C_E||`.
* The completed regularized-determinant estimate then yields

  `|phi(t)| <= (2 pi e/(L|t|))^(1/4)`.                               (4.1)

  Gaussian smoothing with `v=1/8` gives the exact prefactor

  `2^(3/8) pi^(-1/4) exp(3/8) Gamma(3/8) <5`,                        (4.2)

  so

  `sup_w P(|Z^T S Z+b^T Z+d-w|<rho)
   <=min(1,5(rho/L)^(1/4))`.                                         (4.3)

The exponents, conditioning provenance and constant algebra check.

### 4.2 Rank-two approximation / Schur scale — PASS

For

`A=[[B,E],[E^T,C]]`, `S=C-E^T B^(-1)E`,

set

`A_0=[[B,E],[E^T,E^T B^(-1)E]]`.

The factorization in the source shows `rank(A_0)=2`. Hence by the singular-value min-max / best rank-two approximation inequality,

`s_3(A) <= ||A-A_0|| = ||S||`.                                       (4.4)

Thus the Schur remainder retains at least the third-singular-value scale without any assumption on the other eigenvalues or on `E`.

### 4.3 Logarithmic averaging and optimization — PASS

From the pair envelope,

`p_Q(t)<=A_1/r+B_1 sqrt(r)`,                                          (4.5)

where

`A_1=2sqrt(2)`,

`B_1=20*2^(1/4) D^(-1/2) kappa^(-1/4) s^(-1/4)`.                    (4.6)

The layer-cake identity is

`E log_+(a/|t-R|)
 = integral_0^infinity P(|t-R|<a e^(-v)) dv`,                        (4.7)

and (4.3) gives the source's factor `20 s^(-1/4) a^(1/4)`.

The exact optimizer of (4.5) is

`r=(2A_1/B_1)^(2/3)`,                                                 (4.8)

and the minimum is

`3(A_1 B_1^2/4)^(1/3)
 =3*400^(1/3) D^(-1/3) kappa^(-1/6) s^(-1/6)`,                      (4.9)

which is exactly (2.3).

### 4.4 Special physical-pair branch — PASS

If `s_3(A)>=1`, `|A_ij|>=1/2`, and both associated diagonal magnitudes are at most `1/4`, the pair is indefinite and Weyl's singular-value perturbation inequality gives `kappa>=1/4`; also `D>=kappa^2`. Taking `r=kappa` in the unoptimized envelope gives the source's monotone expression and the advertised bound below 51. I found no sign, rank, affine-term, or conditioning gap in this scoped argument.

### Review conclusion

`QFORM-ARBITRARY-RANK-QUARTER-SMALLBALL-v1` and `QFORM-FULL-MATRIX-INDEFINITE-PAIR-LOG-v1` receive a **PASS from fleet03/B05 for the stated supporting scope**. This is not an end-to-end review of full QFORM and does not convert the supporting pair theorem into an exhaustive reduction.

## 5. Full-matrix comparison on the stress family

The arbitrary-rank theorem alone already gives on (3.1)

`||p_(Q_a)||_infinity
 <=3*400^(1/3)(1+a)^(-1/3)
 <=3*400^(1/3)
 =22.1041889918...`.                                                  (5.1)

The sharper bound (3.2) uses the actual square remainder and improves this to

`8*2^(1/4)=9.5136569200...`.                                         (5.2)

Both are uniform as `a downarrow0`, while the scalar absolute-half-Riesz majorant from the preceding B05 run diverges logarithmically. This is a direct, source-valid demonstration that the missing factor is the order of operations: **retain the coupled pair / moving critical value first; average; only then take an envelope**.

## 6. First unpaid implication after this run

The stress family is cross-coupling-localized: one original coordinate `X_1` carries the whole `X_0` cross direction, so the pair has `kappa=1`. In the general exact-coloop geometry the linear cross direction can be spread over many original coordinates. Then every individual physical pair can have tiny `kappa`, and (2.3) pays a reciprocal local-pair cost.

The next B05 target is therefore

`QFORM-NEARZERO-CROSSBANK-AGGREGATE-BEFORE-PAIR-INVERSION-v1`:

> In the near-zero physical-pivot/coloop geometry, aggregate the entire original-coordinate cross bank before paying a reciprocal pair condition number, while retaining its dependence with the residual quadratic form. Prove either a dimension-free weighted coarea estimate or an exhaustive reduction to the already-paid ridge/diffuse/grouped branches.

The completed fleet01/B16 star-family result supplies a concrete model of the desired order: sum the determinant/cross-bank mass before reciprocal local-minor payment. But it does not by itself prove this general coloop reduction, because the aggregated linear innovation and residual quadratic form can remain dependent.

Thus the full conjecture remains **OPEN / NOT PROVED**. The full continuous-density conclusion also remains open separately.

## 7. Source / privacy / execution notes

Only the authorized mathematical repositories and current QFORM controls were used. The changed-file allowlist for this run is confined to this B05 immutable run directory and its source-pinned brain handoff/memory/run records. Manual fallback inspection found no credentials, unrelated private material, email addresses, machine paths, or external private transcripts. No scheduler mutation, task creation, notification change, email/Drive action, public release, paid model/API/Codex call, remote workflow, or cross-account authentication was performed.
