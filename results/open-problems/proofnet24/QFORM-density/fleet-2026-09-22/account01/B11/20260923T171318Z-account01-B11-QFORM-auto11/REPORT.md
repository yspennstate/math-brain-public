SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T17:13:18Z.
attacking: the true-near-coloop two-bank indefinite survivor; replace the vanishing-cross-volume limit by an exact product-provenance normal form in which the third square and the rough hidden hub translation are separated algebraically.

# account01/B11 — near-coloop graph canonicalization for indefinite exact rank three

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T171318Z-account01-B11-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / SOURCE_MATCHED_DUPLICATE_STOPPED / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not proved by the new structural theorem; the completed partner cross-volume branch cited below is continuous.

The unrestricted owner conjecture remains OPEN. Nothing below assumes moments, compact or connected support, log-concavity, Gaussianity, independence after rotation, a uniformly good physical minor, or law-uniform pointwise oscillatory decay.

## 1. Fresh sources and the mechanism switch forced by duplicate detection

Fresh control was read from `yspennstate/math-research-brain`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The current owner continuation is `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. `CURRENT_RESEARCH.md`, `CLAIMS.json`, the live correction inbox, `MEMORY_PROTOCOL.md`, and the account01/B11 assignment were reread before publication.

The following mathematical sources were consumed at their exact scopes.

1. **Newest projected-crossing theorem.**  
   `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,  
   `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.  
   In particular, one original hub plus two projected crossing directions gives an integrable Fourier envelope when the two-volume row marginals are at most `1/2`; and an exact rank-three physical crossing block is paid with no row-marginal gate.

2. **Completed designated partner account02/B11 result.**  
   `yspennstate/math-open-problems@f5996ecc005a07b4e2f0e2a728ed383f0a8e2555`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T155550Z-account02-B11-QFORM-auto11c/REPORT.md`.  
   In its exact-rank-three near-null-ruling chamber, if every essential projected cluster has all atom weights at most one third of the cluster mass, it constructs an actual original-coordinate cross cut and proves the continuous bound
   
   `||p_Q||_infinity < 133299/(s tau^2)`.
   
   Failure forces a single ORIGINAL coordinate `h` with
   
   `||r_h||^2 > tau/36`.

3. **True-near-coloop two-bank splitter.**  
   `yspennstate/math-open-problems@b467c28e31b7959bab9b858104f2b4ddcf197888`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T161353Z-account03-B11-QFORM-r36/REPORT.md`.  
   After already-paid exits, its exact-rank-three survivor has one original hub of leverage `c>63/64` and a literal partition of the remaining original coordinates into two banks `S,T` whose transverse two-dimensional Grams are uniformly positive definite (`lambda_min>1/32`).

4. **Newest Claude continuation and its correction.**  
   The continuation under `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/` was refreshed through the later commit  
   `yspennstate/math-open-problems@a1c6c5f8fff337413bd25a14e834327624ed5950`.  
   The newest `single_hub_core/REPORT.md` explicitly shows that the tempting local `(L,P)` hub maximal functional is not uniformly bounded for rough cap-one laws: comb examples make it grow. Hence the remaining rough-hub estimate must use the transverse quadratic curvature as well; a conditional-profile or local-maximal-function bound alone is not a valid completion.

### Source-matching duplicate that was stopped

At the start of this run I independently derived the identity

`|A[h,J]|^2 e_2(C^T C) = det(M)^2 det(G_J) r_h^T adj(G_I) r_h`

for the one-hub projected cross block. I saved it immediately in `EARLY_CHECKPOINT.md`. A later fresh partner refresh found account02/B11's newer actual checkpoint

`yspennstate/math-open-problems@e54396c223673fb01a571fe84048595b684eb874`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T165547Z-account02-B11-QFORM-auto11-c69c3de5/CHECKPOINT.md`,

which proves the same identity in its natural hub coordinates and already applies the exact-rank-three crossing theorem. I therefore do **not** claim that identity as new and stopped duplicating it. The partner checkpoint identifies the genuine survivor as the double-graph collar where both longitudinal Schur variances tend to zero. The rest of this report changes mechanism and attacks exactly that survivor.

## 2. Setup: a near-coloop hub and two transverse banks

Work first in exact rank three:

`A = R M R^T`, `R^T R = I_3`,                                   (2.1)

where `M` is invertible symmetric and

`s = min_j |lambda_j(M)| > 0`.                                  (2.2)

Choose an ORIGINAL hub coordinate `0` whose spectral row is

`r_0 = sqrt(c) e`, `0<c<1`,                                    (2.3)

with `e` a unit spectral vector. Split the remaining ORIGINAL coordinates into two disjoint banks `S,T`. Relative to

`R^3 = span(e) direct_sum E`, `dim E=2`,

write every light row as

`r_i = s_i e + w_i`, `w_i in E`.                               (2.4)

For `B=S,T`, define

`W_B = sum_(i in B) w_i w_i^T`,
`b_B = sum_(i in B) s_i w_i`,
`a_B = sum_(i in B) s_i^2`.                                    (2.5)

Assume `W_S,W_T` are positive definite. This is exactly the true-near-coloop two-bank state supplied by the completed r36 splitter; there the lower eigenvalue is `>1/32`.

Parseval gives the three exact block identities

`W_S + W_T = I_2`,
`b_S + b_T = 0`,
`a_S + a_T = 1-c`.                                             (2.6)

For each bank set

`q_B = W_B^(-1) b_B`,
`epsilon_i = s_i - q_B^T w_i`, `i in B`,
`tau_B = sum_(i in B) epsilon_i^2
      = a_B - b_B^T W_B^(-1)b_B >=0`.                          (2.7)

The quantities `tau_S,tau_T` are exactly the longitudinal Schur variances whose simultaneous smallness is the partner's double-graph collar.

## 3. New theorem: exact graph/residual orthonormalization

### Theorem `QFORM-NEARCOLOOP-ORTHONORMAL-HIDDEN-FRAME-v1`

Under (2.1)--(2.7), put

`d = q_S - q_T`,                                                (3.1)

and define the two-dimensional light statistics

`Z_S = sum_(i in S) w_i X_i`,
`Z_T = sum_(i in T) w_i X_i`,
`Z = Z_S + Z_T`,                                                (3.2)

`P = W_T Z_S - W_S Z_T`.                                       (3.3)

Then:

1. `W_S` and `W_T` commute, `W_SW_T` is positive definite, and

   `q_S = W_T d`, `q_T = -W_S d`.                              (3.4)

2. If

   `P_tilde = (W_SW_T)^(-1/2) P`,                              (3.5)

   then the four source coefficient columns generating `(Z,P_tilde)` are orthonormal.

3. Put

   `E_res = sum_(i in S union T) epsilon_i X_i`,
   `tau = tau_S + tau_T`.                                      (3.6)

   Its source coefficient vector is orthogonal to every coefficient column of both `Z` and `P_tilde`, and has squared norm `tau`.

   Hence, if `tau>0`,

   `U = tau^(-1/2) E_res`                                      (3.7)

   extends `(Z,P_tilde)` to a **five-dimensional orthonormal projection** of the original light product variables. If `tau=0`, the four-dimensional projection `(Z,P_tilde)` is orthonormal and the residual coordinate is absent.

4. Define

   `eta_2 = (W_SW_T)^(1/2)d`,
   `eta = (eta_2, sqrt(tau))`                                  (3.8)

   (with the last coordinate omitted when `tau=0`). Then the complete light longitudinal statistic satisfies the exact identity

   `sum_(i !=0) s_i X_i = eta_2^T P_tilde + sqrt(tau) U`,       (3.9)

   and, crucially,

   `boxed: ||eta||_2^2 = 1-c.`                                 (3.10)

Consequently the full three-dimensional spectral projection has the exact representation

`boxed:
 R^T X = (sqrt(c) X_0 + eta^T Pi)e + Z,`                        (3.11)

where `Pi=(P_tilde,U)` and `(Z,Pi)` is a five-dimensional orthonormal projection of the light ORIGINAL product coordinates (four-dimensional if `tau=0`). In particular its joint density is bounded by the standard projection cap `2^(5/2)` in the five-dimensional case. No components of `(Z,Pi)` are declared independent.

### Proof

Because `W_T=I-W_S`, the two transverse Grams commute. From `b_S+b_T=0`,

`W_S q_S + W_T q_T = 0`.                                      (3.12)

Writing `q_S=q_T+d` and using `W_S+W_T=I` gives

`q_T=-W_S d`, `q_S=W_T d`,                                    (3.13)

which proves (3.4).

Now regard every statistic as a linear form in the original light source vector. The coefficient row for `Z` is `w_i`; the coefficient row for `P` is

`W_T w_i` on `S`, `-W_S w_i` on `T`.                           (3.14)

Therefore its coefficient-column Gram identities are

`Gram(Z)=W_S+W_T=I`,                                           (3.15)

`Gram(Z,P)=W_S W_T-W_T W_S=0`,                                (3.16)

and

`Gram(P)=W_T W_S W_T+W_S W_T W_S
       =W_SW_T(W_T+W_S)=W_SW_T`.                              (3.17)

Thus (3.5) makes `(Z,P_tilde)` orthonormal.

The least-squares residuals satisfy, bank by bank,

`sum_(i in B) epsilon_i w_i
 =b_B-W_Bq_B=0`.                                               (3.18)

Hence the coefficient vector of `E_res` is orthogonal to the two `Z` columns; by (3.14) it is also orthogonal to both `P` columns. Its squared norm is exactly `tau_S+tau_T`. This proves item 3.

For the longitudinal statistic,

`sum_(i !=0)s_iX_i
 =q_S^T Z_S+q_T^T Z_T+E_res`.                                  (3.19)

Using (3.13),

`q_S^T Z_S+q_T^T Z_T
 =d^T(W_T Z_S-W_S Z_T)
 =d^T P
 =eta_2^T P_tilde`.                                            (3.20)

Finally, from (2.7),

`a_B=q_B^T W_Bq_B+tau_B`.                                      (3.21)

Thus, using (3.13), commutativity, and `W_S+W_T=I`,

`1-c=a_S+a_T`
`=d^T[W_TW_SW_T+W_SW_TW_S]d+tau`
`=d^T W_SW_T d+tau`
`=||eta_2||^2+tau`
`=||eta||^2`.                                                   (3.22)

This proves (3.10)--(3.11). QED.

### Why this is useful

No coefficient has been dropped. The apparently dangerous random longitudinal leakage in the two banks is not treated as an operator-small random perturbation. It is represented **exactly** by extra orthonormal projection coordinates. The whole double-graph collar is compressed into a deterministic coefficient vector `eta` whose length is exactly `sqrt(1-c)`.

In the r36 true-near-coloop survivor,

`c>63/64`,                                                      (3.23)

so the exact hidden coefficient obeys

`boxed: ||eta||<1/8.`                                          (3.24)

This is an algebraic coefficient statement only; because the source laws may have unbounded fragmented support, (3.24) is not used perturbatively.

## 4. Null physical hub: exact rough-hub / saddle-plus-square normal form

The sign-specific hard state is a small or zero physical hub pivot. The exact zero pivot is particularly revealing and is the endpoint that cannot be replaced by a nonzero one.

Assume

`e^T M e=0`.                                                    (4.1)

Write `M` relative to `e direct_sum E` as

`M = [[0,b^T],[b,C]]`.                                         (4.2)

Invertibility forces `b!=0`. Rotate only the deterministic two-dimensional spectral coordinate system in `E` so that

`b=(beta,0)`, `beta=||b||>0`,                                  (4.3)

and write

`C=[[gamma,delta],[delta,lambda]]`.                             (4.4)

This is only a spectral-coordinate notation change; it makes no independence assertion about the transformed light projections. Let `(L,V)` be the corresponding orthogonal coordinates of `Z`. Put

`H=sqrt(c)X_0+eta^T Pi`.                                       (4.5)

Then

`Q=2 beta H L+gamma L^2+2 delta L V+lambda V^2`.               (4.6)

Complete all terms proportional to `L` into the ORIGINAL hub variable:

`m(L,V,Pi)
 = eta^T Pi/sqrt(c)
   + gamma L/(2 beta sqrt(c))
   + delta V/(beta sqrt(c))`.                                  (4.7)

Therefore

`boxed:
 Q=2 kappa L [X_0+m(L,V,Pi)] + lambda V^2,`                    (4.8)

where

`kappa=beta sqrt(c)`.                                          (4.9)

Conditional on all original light coordinates, `X_0+m` is a translate of the original hub law and retains density cap one. It is **not** declared independent of `(L,V,Pi)`.

The third direction has an exact determinant currency. Expanding (4.2)--(4.4),

`det M=-beta^2 lambda`.                                        (4.10)

Hence

`boxed:
 kappa^2 |lambda|=c |det M| >= c s^3.`                         (4.11)

In the true-near-coloop branch (3.23),

`boxed:
 kappa^2 |lambda| > (63/64)s^3.`                               (4.12)

The sign is also exact. For signature `(2,1)`, `det M<0`, so (4.10) gives `lambda>0`; for signature `(1,2)`, `det M>0`, so `lambda<0`. Thus the forced square in (4.8) has the majority sign in both indefinite signatures. Reflection exchanges the two cases.

This proves the structural theorem

### `QFORM-NEARCOLOOP-NULLHUB-SADDLE-SQUARE-CANONICAL-v1`

Every exact-rank-three true-near-coloop two-bank state with zero physical hub pivot has, with full original-coordinate provenance retained, the canonical form (4.8), where:

- `X_0` is one ORIGINAL cap-one variable independent of all light coordinates;
- `(L,V,Pi)` is an orthogonal image of a four- or five-dimensional orthonormal projection of the remaining product input, not a vector of independent coordinates;
- `||eta||^2=1-c` exactly;
- `kappa^2|lambda|=c|det M|` exactly.

This is the precise normal form of the double-graph endpoint.

## 5. The rank-two logarithm and the exact third-direction repair

The mandatory rank-two control remains genuine. With independent centered unit uniforms,

`T=2XY`

has

`p_T(t)=log(1/(2|t|))`, `0<|t|<1/2`.                           (5.1)

The first term of (4.8), `2 kappa L(X_0+m)`, is exactly the same saddle mechanism. A general rotation does not make `L` independent of `V` or `Pi`, and bounded projection density does not justify conditioning it as though it did.

What exact rank three forces is the second term

`lambda V^2`,                                                    (5.2)

with `lambda!=0` and the scale product (4.11). If that square were absent, (4.10) would give `det M=0`, contradicting rank three. Thus in the near-coloop null-pivot endpoint the third direction removes the rank-two degeneracy **algebraically** by forcing a transverse square whose coefficient cannot vanish relative to the hub-saddle coefficient:

`kappa^2|lambda| >= c s^3`.                                    (5.3)

What remains analytically is to exploit that square for arbitrary rough product laws even though the hub translation sees the hidden projection `Pi`.

This agrees exactly with the newest Claude correction at `a1c6c5f8...`: a local maximal profile of `(L,Pi)` alone can grow for comb laws, so one must combine the `V^2` curvature with the hub incidence instead of taking a conditional supremum.

## 6. Completed designated-partner result applied to an actual case inequality

Apply the completed account02/B11 theorem at `f5996ecc...` before entering the single-hub normal form.

In its near-null-ruling chamber, if every projected essential cluster is atom-diffuse at relative scale `1/3`, the branch is already paid continuously by

`boxed:
 ||p_Q||_infinity < 133299/(s tau^2).`                          (6.1)

Therefore the only branch that needs the hub analysis satisfies the partner's actual quantitative conclusion

`boxed:
 c_h=||r_h||^2 > tau/36.`                                      (6.2)

This is not a verbal citation: (6.1) is the completed partner density inequality used to remove the entire atom-diffuse subcase, while (6.2) is the quantitative hypothesis passed to the hub branch.

When the independent r36 collision argument further identifies the true-near-coloop survivor `c>63/64`, the new theorem converts that geometric statement exactly into

`||eta||<1/8` and `kappa^2|lambda|>(63/64)s^3`,                 (6.3)

without deleting any light coordinate or treating its value as small.

For comparison, the fresh account02/B11 checkpoint `e54396c...` pays every state in which either bank has nontrivial longitudinal Schur variance through the rank-three crossing currency. Its displayed bound is

`||p_Q||_infinity < 19.099 s^(-1) tau_B^(-1/6)`                (6.4)

in the r36 bank normalization. The new normal form explains what survives as both `tau_B` tend to zero: the random leakage does not disappear; it becomes the normalized hidden projection `Pi` with deterministic coefficient budget (3.10).

## 7. Exact control example

Take

`M_*=[[0,1,1],[1,0,1],[1,1,0]]`.                               (7.1)

Its eigenvalues are

`{-1,-1,2}`,                                                    (7.2)

so it is a valid `(1,2)` indefinite target with `s=1`; reflection gives `(2,1)`. With hub direction `e=e_1`,

`e^T M_* e=0`.                                                  (7.3)

Here `||b||^2=2`; after rotating the transverse plane so `b=(sqrt(2),0)`, the orthogonal transverse coefficient is

`lambda=-1`.                                                     (7.4)

Thus, for a true-near-coloop leverage `c=63/64`,

`||eta||=1/8`,
`kappa^2|lambda|=c|det M_*|=63/32=1.96875`.                    (7.5)

The checker in this run verifies (3.4)--(3.22) on 100 independently generated finite Parseval frames and verifies (7.2)--(7.5) exactly to floating precision. It ends

`QFORM_B11_NEARCOLOOP_CANONICAL_CHECK_PASS`.

The computation is regression evidence only; the proof is the exact algebra above.

## 8. What remains genuinely unpaid

The new theorem does **not** prove a universal density bound for (4.8). The missing analytic implication is now sharper:

`QFORM-ROUGH-HUB-SEES-HIDDEN-PROJECTION-CURVATURE-v1`:

> Let `X_0` be one ORIGINAL cap-one variable, independent of the remaining product coordinates. Let `(L,V,Pi)` be an orthogonal image of a dimension-at-most-five orthonormal projection of those remaining coordinates. Prove a universal bounded-density estimate for
>
> `2 kappa L [X_0+m(L,V,Pi)] + lambda V^2`,
>
> for the affine `m` produced by (4.7), uniformly whenever `kappa^2|lambda|` has a positive lower bound. The proof must use the `V^2` curvature jointly with the hub incidence; it may not replace the law of `L` conditional on `Pi` by a marginal cap and may not use the disproved local maximal-profile bound.

This is an exact product-provenance version of the newest Claude `(SP)` issue. The theorem here shows that the true-near-coloop double-graph geometry produces no additional mysterious random perturbation: its entire difficulty is the rough hub seeing a low-dimensional orthonormal hidden projection while a nonvanishing transverse square is present.

Small **nonzero** physical hub pivots remain a separate interpolation from the exact zero-pivot normal form and may not be replaced by zero. Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate bridge to the full owner target.

## 9. Verification and status

Run files:

- `EARLY_CHECKPOINT.md`: preserved source-matched duplicate derivation; not claimed as new after partner refresh.
- `VERIFY.py`, `VERIFY_OUTPUT.txt`: regression check for the duplicated projected-crossing identity.
- `VERIFY_CANONICAL.py`, `VERIFY_CANONICAL_OUTPUT.txt`: checks the new orthonormal hidden-frame theorem and null-hub determinant currency.

The canonical checker reports maximum orthonormal-frame error `4.33e-15`, maximum energy-identity error `5.56e-17`, maximum longitudinal-reconstruction error `4.45e-16`, and the exact control currency `63/32`.

**Full QFORM:** OPEN.  
**Continuity:** not proved by the new canonicalization; partner branch (6.1) is continuous.  
**Brain/native ingestion:** `WITHOUT_VERIFIED_BRAIN`.  
**Model self-report:** `GPT-5.6 Sol`.  
**Configured reasoning effort:** `UNKNOWN`.  
**Provider reasoning-token/thinking-time usage:** `NOT_EXPOSED`.
