SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T02:14:00Z.
attacking: sharpen the nonzero/zero spectral-coloop interpolation by retaining the actual two-scalar product structure inside the cross-transverse near-slope trace instead of paying the looser affine rank-two constant.

# account03/B16 r21 — sharpened cross-transverse projection-product smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM`; full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`.  
**Continuity:** not proved by the new argument; the result below is an essential-density bound.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated GitHub repository reads/writes occurred, but no authenticated native brain receiver ingestion was established.

## 1. Source pins and correction boundary

Fresh controlling source during this run: `yspennstate/math-research-brain@94b4debdef11b95db019db3f7406e3781bb517ad`, OWNER CONTROL revision `2026-09-22.15`, QFORM-only.

The source-valid predecessor sharpened here is account01/B16 `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1`, canonical report

`yspennstate/math-open-problems@8d262d18e5581cd02b8ea8be5102aa2a6d30ddd7:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T003846Z/REPORT.md`.

Its key geometry is a genuine independent cap-one scalar `X` coupled to a possibly dependent two-dimensional receiver `Y`, together with a nonzero transverse determinant resource `P`; this avoids the live receiver-only counterexample.

The new analytic input is account03/B05 `QFORM-RANK2-LOCALIZED-HALF-RIESZ-v1` and `QFORM-RANK2-HALF-RIESZ-UNIVERSAL-v1`, read at

`yspennstate/math-open-problems@4f0070b8741a9d793b10c56313b89057abec3959:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/account03-B05-20260922T133738Z-qform-r12/REPORT.md`.

For an actual two-coordinate quadratic with independent cap-one coordinates, Theorem 3.1 there can be used with row leverage `d=1`, giving

`sup_t E |t-Z^T K Z|^(-1/2) <= 16 sqrt(2) |det K|^(-1/4)`.      (1.1)

For a general rank-two product quadratic, Theorem 4.1 gives

`sup_t E |t-R|^(-1/2) <= C_2 |pdet R|^(-1/4)`,
`C_2=16*2^(3/4)<26.909`.                                        (1.2)

The completed designated-partner result actually applied below is account04/B16 `QFORM-RULED-PLUECKER-ENDPOINT-v1`, canonical source

`yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd:proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T231542Z-account04-B16-QFORM-r1/REPORT.md`.

It proves the majority-sign one-sheet bound `pi sqrt(2)` for exact rank three and reduces its `d=0` matroid endpoint to a leverage-one spectral coloop plus a rank-two plane, leaving only the opposite convex/two-sheet side unpaid at that stage.

Preserved live corrections: no independence after spectral rotation; no arbitrary-joint 3D coarea theorem; no positive conditional projection-height moment; no receiver-only use of a two-dimensional density cap; no law-uniform pointwise quadratic-phase decay.

## 2. Sharpened cross-transverse theorem

### Theorem 2.1 — `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v2`

Let `X` be a real random variable with probability density at most one. Let `Y=(U,V)` be independent of `X` and have a possibly dependent joint probability density `rho_Y` satisfying

`||rho_Y||_infinity <= M`.

Let

`B=[[a,b^T],[b,C]]`

be a real invertible symmetric `3 x 3` matrix. Assume `b!=0`. Rotate only inside the two-dimensional `Y` plane so that

`b=(beta,0)`, `beta>0`,
`C=[[c,d],[d,e]]`.

Define

`D=|det B|`,
`P=beta^2 |e|`.

If `P>0`, then the homogeneous quadratic form

`Q=(X,Y)^T B(X,Y)`

has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 3*2^(8/3) M^(2/3) (D P)^(-1/6).`   (2.1)

Numerically the leading constant is

`3*2^(8/3)=19.048812623618392...`.                              (2.2)

This improves the predecessor constant `103680^(1/3)=46.9784...` on exactly the same homogeneous cross-transverse scope. The proof does not claim that a receiver density cap alone is sufficient: the factor `P` is essential.

### Proof

The rotation in the receiver plane preserves the joint density cap. Since `P>0`, `e!=0`. Apply the determinant-one shear

`W=V+(d/e)U`,
`σ=c-d^2/e`.

The joint density of `(U,W)` is still bounded by `M`, `X` remains independent of it, and

`Q=aX^2+2 beta XU+σU^2+eW^2`.                                  (2.3)

Fix an output value `t` and a split parameter `δ>0`. Put

`r=aX+beta U`.                                                   (2.4)

Split the pushforward density into `|r|>=δ` and `|r|<δ`.

#### Far slope

Condition on `(U,W)`. As a function of `x`,

`dQ/dx=2(a x+beta U)=2r`.

There are at most two inverse branches. On `|r|>=δ`, each contributes at most `1/(2δ)` because the density of `X` is at most one. Therefore

`p_far(t) <= δ^(-1)`.                                           (2.5)

#### Near slope

For fixed `x`, change variables from `u` to `r=a x+beta u`, so `du=dr/beta`. Integrating the two possible roots in `W` of the remaining square gives

`p_near(t)
 <= M/(beta sqrt(|e|))
    integral f_X(x) integral_(|r|<δ) |H_t(r,x)|^(-1/2) dr dx`,  (2.6)

where, writing `s=σ/beta^2`, the quadratic part of `H_t` in `(r,x)` has matrix

`K=[[-s, as-1],[as-1, a-a^2 s]]`.                              (2.7)

A direct determinant calculation gives

`det K=as-1`.                                                     (2.8)

The determinant of (2.3) is

`det B=e(aσ-beta^2)=e beta^2(as-1)`,                             (2.9)

hence

`|det K|=D/P`.                                                    (2.10)

Let `R_δ` be uniform on `[-δ,δ]`, independent of `X`, and set

`Z=R_δ/(2δ)`.

Then `Z` is uniform on `[-1/2,1/2]` and has density cap one. Under `(r,x)=(2δ z,x)`, the quadratic coefficient matrix becomes

`K_δ=diag(2δ,1) K diag(2δ,1)`,

so

`|det K_δ|=(2δ)^2 |det K|`.                                      (2.11)

Now use (1.1), the actual-two-coordinate localized half-Riesz theorem. It applies because `Z` and `X` are genuinely independent cap-one scalar variables; no projected-coordinate independence is being invented. Thus

`E |H_t(R_δ,X)|^(-1/2)
 <=16 sqrt(2) |det K_δ|^(-1/4)
 =16 δ^(-1/2)|det K|^(-1/4)`.                                  (2.12)

Since the inner `r` integral in (2.6) equals `2δ` times this expectation,

`p_near(t)
 <=32 M δ^(1/2) D^(-1/4)P^(-1/4)
 =32 M δ^(1/2)(DP)^(-1/4)`.                                    (2.13)

Combining (2.5) and (2.13),

`p_Q(t) <= δ^(-1)+B_0 δ^(1/2)`,
`B_0=32 M(DP)^(-1/4)`.                                          (2.14)

The exact minimizer is

`δ=(2/B_0)^(2/3)`.                                               (2.15)

At that value the second summand is twice the first, so

`p_Q(t)
 <=3*2^(-2/3) B_0^(2/3)
 =3*2^(8/3) M^(2/3)(DP)^(-1/6)`.                               (2.16)

The estimate is uniform in `t`. Applying the argument to interval test functions (or first to bounded truncations and then using monotone convergence) proves absolute continuity and the essential bound. QED.

### Affine note

The target application below is homogeneous. Deterministic affine terms can also be incorporated in Theorem 2.1: the slope coordinate `r` receives a constant translation, and the invertible two-variable quadratic in (2.12) can be completed by deterministic translations of the two independent scalar variables, which preserve their density caps. No random receiver-conditioned translation is needed for the stated application.

## 3. Exact spectral coloop: two-sided universal bound below 34

Consider an exact-rank-three target

`A=R Lambda R^T`, `R^T R=I_3`, `|lambda_j|>=1`,

and assume some original physical coordinate `i` has spectral leverage exactly one. Choose the spectral basis so that its row is `e_1`. Every other spectral row then lies in `e_1^perp`, and the remaining product source has a genuine two-dimensional orthogonal projection `Y` with

`||p_Y||_infinity <=2`.                                         (3.1)

The coefficient matrix `B` in variables `(X_i,Y)` is orthogonally congruent to `Lambda`, hence

`D=|det B|=|det Lambda|>=1`,
`s_min(B)>=1`.                                                    (3.2)

Write `a=B_00=A_ii`.

We split at the fixed rational threshold

`τ=3/7`.                                                          (3.3)

### Near-null branch: `|a|<=3/7`

The completed cross-resource lemma in account01/B16 gives, after rotating the receiver plane so `b=(beta,0)`,

`P=beta^2|e| >= (1-|a|)D >= (4/7)D`.                            (3.4)

Apply Theorem 2.1 with `M=2`:

`||p_Q||_infinity
 <=3*2^(8/3)*2^(2/3)*(4/7)^(-1/6) D^(-1/3)
 <33.195`.                                                        (3.5)

### Non-small scalar pivot: `|a|>3/7`

Complete the square only in the genuine independent physical coordinate `X_i`. The rank-two Schur residual is a quadratic form of the two-dimensional product projection and has pseudodeterminant magnitude

`D/|a|`.                                                          (3.6)

The scalar-square coarea inequality together with (1.2) gives

`||p_Q||_infinity
 <= C_2 |a|^(-1/2)(D/|a|)^(-1/4)
 = C_2 (|a|D)^(-1/4)`.                                          (3.7)

Using `C_2=16*2^(3/4)`, `|a|>3/7`, and `D>=1`,

`||p_Q||_infinity
 <16*2^(3/4)*(7/3)^(1/4)
 <33.258`.                                                        (3.8)

Therefore:

### Corollary 3.1 — `QFORM-EXACT-SPECTRAL-COLOOP-34-v1`

Every exact-rank-three target with a leverage-one original-coordinate spectral coloop satisfies

`boxed: ||p_Q||_infinity <34.`                                  (3.9)

This is two-sided and uniform over all independent cap-one input laws. It does not assume any moment, support shape, log-concavity, or independence of spectral coordinates. It proves essential boundedness, not continuity.

The fixed threshold `3/7` is chosen for a short exact proof. Numerically optimizing the two displayed envelopes would lower the combined certificate to about `33.216`, but no optimized decimal threshold is needed for the theorem.

## 4. Equation-level application of designated partner account04/B16

The designated partner account04/B16 proves that in the exact-rank-three indefinite case the majority-sign one-sheet side satisfies

`ess sup p_Q <= pi sqrt(2)`,                                    (4.1)

and that when its disjoint Pluecker mass `d` vanishes, the only remaining matroid endpoint after its finite-line alternatives is exactly a leverage-one spectral coloop plus a rank-two spectral plane. Its report left the opposite convex/two-sheet side as the analytic debt.

Apply Corollary 3.1 to that exact partner endpoint. Because its coefficient matrix is orthogonally congruent to the three nonzero eigenvalues, `D=|det Lambda|>=1`, and because the surviving plane is a genuine two-dimensional projection of the remaining original product source, (3.1) applies. Hence the partner's formerly unpaid side now obeys

`boxed: ess sup_(two-sheet side) p_Q <34.`                       (4.2)

Together with (4.1), the full `d=0` coloop endpoint itself has

`||p_Q||_infinity <34`.                                          (4.3)

This is an actual inequality-level use of account04/B16, not a receiver-density substitution: the proof uses the partner's structural identification of the exact coloop endpoint and retains the genuine independent physical scalar plus the product-projection provenance of the plane.

## 5. Why this does not solve the full target

The theorem pays an exact spectral coloop. It does **not** show that an arbitrary exact-rank-three frame has such a coloop, and it does not justify discarding or conditioning away arbitrary additional spectral directions. The live arbitrary-joint counterexamples still forbid replacing the surviving product provenance by a bounded three-dimensional receiver density.

The first target-relevant unpaid implication after this run is therefore an **approximate-coloop / isotropic-leakage routing theorem**:

> for a leverage-heavy original row with leverage `c in (1/2,1)` and small or zero first Rayleigh pivot, aggregate the residual `1-c` spectral leakage with the two-dimensional product-projection bank before any reciprocal pivot is paid, and route either to a cross-transverse certificate of the form above or to an already-paid grouped-bank/diffuse mechanism.

A separate global debt remains the splice from exact-rank-three mechanisms to arbitrary additional spectrum. Full QFORM and the requested global continuity conclusion remain open.

## 6. Finite constant check

The committed `CHECK.py` evaluates only the explicit constants. It verifies

`C_cross = 19.048812623618392...`,
`C_rank2 = 26.908685288118864...`,
`near(3/7) = 33.19410130244372...`,
`far(3/7) = 33.25727608401318...`,

and terminates `STATUS=PASS`.
