SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B20, 2026-09-23T07:02:14Z.
attacking: the designated-partner rank-two-cross near-kernel survivor by converting small physical self-action into an exact two-bank spectral-volume identity and a quantitative near-coloop packet.

# account02/B20 auto11 — rank-two-cross near-kernel forces a 97.7% near-coloop

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Proof closure and keeper / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT BANK-VOLUME IDENTITY / NEAR-COLOOP REDUCTION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval occurred, but no native learned-memory receiver ingestion is exposed.  
**Continuity:** unchanged for the unrestricted target.

## 1. Source boundary and partner result actually consumed

Fresh protected control at the start of the mathematical pass was `yspennstate/math-research-brain@59e76ef3cee387e6d219a25f9a2189bb8892ff1e`, with OWNER CONTROL revision `2026-09-22.15`, QFORM as the sole research target, and no account02 pause.

The newest **completed** designated-partner result available before this report is account03/B20 r27,

`yspennstate/math-open-problems@949ad3211a8db6954311a0b3b8d92d99e4d3462a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T061345Z-account03-B20-QFORM-r27/REPORT.md`.

Its theorem `QFORM-RANK2-CROSS-NULL-TRANSVERSE-L3-v1` treats two disjoint original-coordinate product banks with exact-rank-two physical cross block `C`, nonzero singular values `s1>=s2>0`, and a three-dimensional source physical range `E`. In the exact-null transverse endpoint it proves

`||p_Q||_infinity < 7.5 ||P^T B r||^(-1/4)(s1 s2)^(-3/8)`,        (1.1)

where `P=range(C)` and `r` is the unit physical direction in `E cap P^perp`. Together with the preceding scalar-transverse receiver, every fixed-scale survivor in its exact-rank-three compound-energy application obeys

`|r^TBr|<1/64`, `||P^TBr||<1/64`, hence

`boxed: ||Br|| < kappa := sqrt(2)/64 = 0.0220970869... .`          (1.2)

The partner also records the compound cross threshold

`s1(C)s2(C) >= sqrt(29/3072)`,                                    (1.3)

but the deterministic theorem below turns out not to need the numerical lower bound (1.3) once (1.2) is known.

Account03/B20 r28 had a start record but no completed result at the time of the source refresh used here; it is therefore not counted as a completed partner artifact.

## 2. Exact-rank-three setup

Work in the exact-rank-three branch used by the current proof assembly. Write

`A = R Lambda R^T`,                                                (2.1)

where `R` is `n x 3`, `R^T R=I_3`, `Lambda` is real symmetric and invertible, and

`min_j |lambda_j(Lambda)| >= 1`.                                  (2.2)

Let `I union J` be a full partition of the original physical coordinates and put

`U=R_I`, `V=R_J`, `G=U^T U`, `H=V^T V=I-G`.                      (2.3)

Assume

`rank(U)=3`, `rank(C)=2`, `C:=A_IJ=U Lambda V^T`.                  (2.4)

Since `U Lambda` is injective, `rank(V)=rank(C)=2`. Let `q` be a unit vector spanning `ker V`. Then

`Hq=0`, `Gq=q`, `||Uq||=1`.                                       (2.5)

Let

`E=range(U)`, `P=range(C)`,                                       (2.6)

and let `r` be the unit vector spanning `E cap P^perp`. Put

`B=A_II=U Lambda U^T`.                                             (2.7)

Let `s1>=s2>0` denote the two nonzero singular values of `C` and set

`beta=s1 s2`, `Delta=|det Lambda|`, `k=||Br||`.                    (2.8)

## 3. New exact identity

### Theorem 3.1 — `QFORM-RANK3-RANK2CROSS-BANK-VOLUME-IDENTITY-v1`

Under (2.1)--(2.8),

`boxed: beta^2 k^2 = Delta^2 det(G) pdet(H).`                       (3.1)

Here `pdet(H)` is the product of the two nonzero eigenvalues of the rank-two positive semidefinite matrix `H`.

### Proof

Because `U` has rank three, every vector in `E` has a unique representation `Ux`; write

`r=Ux`, `x^T Gx=1`.                                                (3.2)

The condition `r perp range(C)` is equivalent to

`0=C^T r=V Lambda U^T Ux=V Lambda Gx`.                             (3.3)

Since `ker V=span{q}`, there is a nonzero scalar `alpha` with

`Lambda Gx=alpha q`.                                               (3.4)

Consequently

`Br=U Lambda Gx=alpha Uq`,                                        (3.5)

and (2.5) gives

`k=|alpha|`.                                                       (3.6)

Solving (3.4) for `x` and using (3.2),

`1=alpha^2 q^T Lambda^(-1) G^(-1) Lambda^(-1) q`,                 (3.7)

so

`q^T Lambda^(-1)G^(-1)Lambda^(-1)q = k^(-2)`.                    (3.8)

Now use exterior two-powers. Since `C` has rank two,

`beta^2 = || wedge^2 C ||_HS^2`.                                  (3.9)

The map `wedge^2 V^T` has rank one, squared Hilbert--Schmidt norm `pdet(H)`, and image `wedge^2(q^perp)=span{*q}` under the three-dimensional Hodge identification. Hence

`beta^2 = pdet(H) || wedge^2 U wedge^2 Lambda (*q) ||^2`.          (3.10)

For an invertible three-dimensional linear map,

`wedge^2 Lambda (*q)=det(Lambda) * (Lambda^(-T)q)`.                (3.11)

`Lambda` is symmetric, so `Lambda^(-T)=Lambda^(-1)`. Also, for every `v in R^3`,

`||wedge^2 U (*v)||^2 = det(G) v^T G^(-1)v`.                      (3.12)

Equation (3.12) follows immediately after diagonalising the positive matrix `G=U^TU` (equivalently from the cofactor identity for `wedge^2 U`). Combining (3.8)--(3.12) yields

`beta^2 = pdet(H) Delta^2 det(G) k^(-2)`,                          (3.13)

which is (3.1). QED.

## 4. Compression makes the identity universal at the target scale

Because `C` is a rectangular compression of `A`, singular-value monotonicity under left/right contractions gives

`s_j(C) <= s_j(A)` for `j=1,2`.                                   (4.1)

If the three nonzero singular values of `A` are `L1>=L2>=L3>=1`, then

`beta <= L1 L2 <= L1 L2 L3 = Delta`.                              (4.2)

Therefore Theorem 3.1 immediately implies the dimension-free deterministic inequality

`boxed: det(G) pdet(H) <= ||Br||^2.`                               (4.3)

This is the key synthesis improvement: the partner's near-kernel statement is not merely a small Rayleigh coefficient. It forces collapse of the product of the two complementary bank-volume factors.

## 5. Quantitative 97.7% near-coloop consequence

Since `H=I-G`, the matrices `G,H` commute. From (2.5), one eigenvalue of `G` is exactly one. Write the other two as

`gamma_1,gamma_2 in (0,1)`.                                      (5.1)

Then

`det(G) pdet(H)
 = gamma_1 gamma_2 (1-gamma_1)(1-gamma_2)`.                       (5.2)

Apply the designated-partner survivor bound (1.2) to (4.3):

`gamma_1 gamma_2 (1-gamma_1)(1-gamma_2) < 1/2048`.               (5.3)

Thus at least one `gamma=gamma_j` satisfies

`gamma(1-gamma) < 1/(32 sqrt(2))`.                                (5.4)

Solving the quadratic inequality gives

`boxed:
 min(gamma,1-gamma) < delta_* :=
 (1-sqrt(1-1/(8sqrt(2))))/2
 = 0.0226082184537... .`                                           (5.5)

Let `v` be a unit spectral vector with `Gv=gamma v`. Then the definition of `G` gives the original-coordinate mass identities

`sum_{i in I} <R_i,v>^2 = gamma`,
`sum_{j in J} <R_j,v>^2 = 1-gamma`.                               (5.6)

Hence every still-unpaid partner survivor contains a spectral unit direction with

`boxed: max{ ||U v||^2, ||V v||^2 } > 1-delta_*
       = 0.977391781546... .}`                                     (5.7)

Equivalently, one of the two physical banks carries less than `2.261%` of that direction's squared mass. This is a deterministic **near-coloop** conclusion. It is not a rotated-coordinate independence assertion: `v` is used only to describe the matrix frame.

A useful row-level corollary is that on the small-mass bank every physical row satisfies

`|<R_i,v>| < sqrt(delta_*) = 0.15036029547...`.                    (5.8)

If a physical row on that bank has total leverage `||R_i||^2>1/2`, its component in `v^perp` is therefore larger than

`sqrt(1/2-delta_*) = 0.69093543949...`.                            (5.9)

## 6. Required newest-Claude application at an exact inequality

The pinned interactive report `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` proves its Fresnel--Brascamp--Lieb Theorem F: for a rank-three form whose physical leverage scores are at most one half,

`||p_Q||_infinity <= 12 |lambda_1 lambda_2 lambda_3|^(-1/3)`.      (6.1)

Apply it directly to the exact-rank-three matrix (2.1), with zero diagonal residual. If

`max_i ||R_i||^2 <= 1/2`,                                         (6.2)

then (2.2) and (6.1) give the actual target-level payment

`boxed: ||p_Q||_infinity <= 12.`                                  (6.3)

Therefore every still-unpaid exact-rank-three survivor of Sections 1--5 has **both**:

1. a physical coordinate with leverage `>1/2`; and
2. a spectral near-coloop satisfying (5.7).

This also explains why simply invoking the pinned D5 theorem on the current cross block cannot finish this packet: the current block `C` has exact rank two, so its fifth volume is exactly zero. The D5 theorem remains a valid exit on other physical cross blocks, but not on this one.

## 7. Strongest conditional end-to-end graph after this run

The source-pinned proof graph now reads as follows.

- The owner/Claude reduction says that a proof of the fixed no-pivot `N3(tau)` core, together with its source-preserving padding/descent, would imply the full target. That global implication remains conditional.
- Scalar, physical-pair, diffuse Fresnel, physical cross-volume D/D'/D5, ruled one-sheet, grouped/ridge, and several pivot/Schur packets are already paid at their exact source scopes.
- In the exact-rank-three co-heavy branch, account01/B19 supplies a full physical partition with aggregate rank-two cross currency `e2(CC^T)>=29/3072`.
- Account03/B19 pays fixed transverse scalar self curvature; account03/B20 r27 pays the exact-null off-diagonal transverse action and reduces every fixed-scale survivor to (1.2).
- **This run converts (1.2) into the exact bank-volume collapse (4.3) and the quantitative near-coloop (5.7).**
- The pinned Theorem F simultaneously says an unpaid exact-rank-three survivor must have a physical high-leverage coordinate.

Thus the first unpaid implication in this branch is no longer the vague `near-kernel mixed-row payment`. It is the following sharpened, fully quantified statement.

### `QFORM-NEARCOLOOP-HIGHLEVERAGE-PAYMENT-v1` — OPEN

Let `A=R Lambda R^T` have exact rank three with `R^TR=I`, `min |lambda_j|>=1`, and let an original-coordinate full partition `I union J` satisfy the rank-two-cross compound-energy hypotheses used above. Assume all previously paid scalar/pair/volume/transverse exits fail. Then there exist

- a spectral unit vector `v` with at least `0.9773917815` of its squared physical mass on one bank, and
- an original physical coordinate `h` with `||R_h||^2>1/2`.

Prove a universal linear small-ball/density estimate for the full product source while retaining arbitrary same-side curvature and all ambient couplings, or reduce source-preservingly to an already-paid Theorem-H/ridge/grouped/physical-pair packet.

The exact new content is that every putative counterexample to this implication must survive a **simultaneous near-coloop plus high-leverage** geometry; a generic three-dimensional mixed-row packet no longer needs to be paid.

A natural next split is whether the high-leverage row lies on the small-mass bank. In that case (5.9) gives a fixed transverse physical component `>0.6909`. If it lies on the large-mass bank, the remaining debt is a grouped longitudinal concentration problem. Any attempted stability argument must be Fourier/product-structural; deleting the `2.26%` coefficient mass as a small quadratic perturbation is forbidden for arbitrary unbounded/fragmented inputs.

## 8. Corrections and counterexample status

This argument never uses law-uniform pointwise quadratic-phase decay, unrestricted fiber suprema, arbitrary-joint three-dimensional coarea, conditional projected-density caps, or post-rotation independence. The newest pinned counterexample-search report still records no counterexample to QFORM; this run likewise gives no full-target counterexample. It only proves the deterministic reduction above.

The unrestricted QFORM density theorem remains **OPEN**. Unrestricted continuity remains **OPEN** and is treated separately.
