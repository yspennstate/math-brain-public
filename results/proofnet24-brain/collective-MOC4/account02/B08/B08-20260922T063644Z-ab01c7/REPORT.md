# B08 MOC4 attempt — `MOC4-COMMON-BLOCK-EXTERNAL-FACET-COLLAR-v1`

**Outcome:** `ESSENTIAL_STEP_APPLIED`.  **Full MOC4 status:** OPEN; this is not a full-proof candidate.

## Scope and source binding

This run is account02/B08 and is restricted to the repeated-spectrum/common-block boundary of the complex normal 4-by-4 Marcus–de Oliveira problem. New benchmark/brain-installation work was not performed.

Fresh control source at start: main commit `94469b947c0d4e763150447cf1a65181cdb68b44`, OWNER CONTROL revision `2026-09-22.2`, program `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact blobs read at that ref were AGENTS `94387098453b9f4a9b10179183f6f6ec780fd987`, README `3d4a9372c87802ab734141a3374d04c8823372e3`, fleet `e647d5d2479749f80ce7bb4862bee0f28513c7d9`, roles `ed17ecc94f76720c0345b3e32249b791b20ec611`, PROTOCOL `83a9268bf5287ca203e4be69a79e25382397bca7`; collective ORDER blob `a70e03208ae00795ca7c6cdf9b7dbce854347138` and TARGETS blob `a8cafa98cdb074ed15d0e214f8f54ee514c500df` were also consumed.

Campaign-lead source actually read: account03/B07 canonical report `proofnet24/collective-MOC4/account03/B07/20260922T060726Z-account03-B07-MOC4-r11/REPORT.md`, blob `3c11567e275d39376f217a9b9e3c10693efa3127`, candidate `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`. Its current residual mechanism is zero-face support plus strict Spin(4) interior safety; saturation at a genuine maximizer can be moved along a flat SU(2) orbit to a zero-entry representative.

Named OTHER-account result actually consumed and applied: account03/B09 handoff `scheduled_tasks/work/shared/collective-open-problems-2026-09-22/handoffs/account03-B09-20260922T051640Z-moc4-external-facets.md`, blob `5614c49e68dab63b0a7c5be62aeddcdd67ee260f`, status `ESSENTIAL_STEP_APPLIED`. Its exact usable statement is the Saxl external-facet bound described below. Previous B08 dependency: `MOC4-COMMON-BLOCK-EDGE-PAYMENT-v1`, shared handoff blob `73a4822805fdb2e620f8a7fed20bafa16d96fcc8`.

Work mode: `WITHOUT_VERIFIED_BRAIN`; no brain-on experiment is claimed.

## Conditional end-to-end boundary reduction entering this run

Existing B08 work gives exact MOC4 on repeated-spectrum pairs and on proper common reducing block pairs. The opposite-scalar gauge `(A,B) -> (A+tI,B-tI)` preserves `A+B` and every permutation-product vertex, so away from those solved boundaries one may reduce the unresolved core to simple spectra, individually invertible matrices, and no proper common reducing subspace. The campaign lead further reduces a support-maximizer attack to a zero-face branch and a strict Spin(4) branch.

The first boundary question left by the previous B08 run was whether a support-exposed common-block face can be paid globally rather than only along one- and two-cross-gate charts. The account03/B09 external-facet theorem supplies exactly such a global certificate when its 48 external quantities stay below the permutation endpoint maximum.

## 1. External-gap certificate: a global, not local, common-block collar

Fix spectra `a=(a_i)`, `b=(b_j)` and a real support functional `L` on the complex plane. Put

`f(sigma) = L(prod_i (a_i+b_{sigma(i)}))`,  `M=max_sigma f(sigma)`.

Let `rho:S4 -> S3` be the quotient action on the three complementary-pair matchings and let

`B_rho(f) = (1/4) sum_{sigma: rho_sigma=rho} f(sigma)`.

For each `tau in S4` and either of the two `rho' in S3` pointwise deranging `rho_tau`, account03/B09 gives the exact external Saxl functional

`e_{tau,rho'}(f) = (2/3)(B_{rho_tau}(f)+B_{rho'}(f)) - (1/3) f(tau)`

and proves, for every **true unitary** coupling `U`,

`h_L(U) := L(det(diag(a)+U diag(b) U*)) <= max(M, max_external e(f)).`      (1)

No arbitrary bistochastic or unrestricted `SO(6)` surrogate is used in (1).

Define the external gap

`g(a,b,L)=M-max_external e(f)`.

Then:

**Theorem 1 (external-gap global support certificate).** If `g>=0`, the MOC4 support inequality in direction `L` holds for every true unitary `U`. If `g>0`, this conclusion persists on an open neighborhood of `(a,b,L)`.

**Proof.** The first assertion is immediate from (1). For the second, all 24 values `f(sigma)` and all 48 values `e_{tau,rho'}` are finite polynomial/real-linear functions of `(a,b,L)`. Their finite maxima are continuous. Hence `g` is continuous. A strict positive value remains positive in some open neighborhood, and (1) applies pointwise there. QED.

This is stronger than the previous local common-block collars: once a support direction at a common-block boundary has positive external gap, no unitary anywhere in `U(4)` can cross that supporting line, and the statement is stable under small spectral and support perturbations.

Equivalently, writing endpoint deficits `delta_sigma=M-f(sigma)` and fiber-average deficits `bar_delta_rho=(1/4)sum_{rho_sigma=rho}delta_sigma`, the 48 checks are the exact scalar payments

`delta_tau <= 2(bar_delta_{rho_tau}+bar_delta_{rho'})`.                 (2)

Thus common-block boundary searches may fail closed on (2) before any Hessian or gate analysis.

## 2. Exact application: the previous mismatched-circle 2+2 boundary is globally closed in its exposed support direction

Use the exact B08 datum

`-a=(-3,-2,1-3i,1-2i)`,
` b=(-1,0,1,1+i)`,

and the support functional `L(z)=Im z`. The common-block coupling used previously is `U0=diag(H,H)` with `H` the real 2-by-2 Hadamard rotation. Its four block-preserving permutation vertices are

`-36, -32, -27, -24`,

so all have support value zero. The other twenty permutation products have strictly negative imaginary part. Exact enumeration gives

`M=0`,  `max_outside_face f=-12`.

The six Klein-fiber means are exactly

`-52, -52, -37, -38, -40, -41`.

Evaluating all 48 account03/B09 external functionals by (1) gives

`max_external e = -22`.

Therefore the exact external gap is

`g=22`.

By Theorem 1,

`Im det(diag(a)+U diag(b) U*) <= 0` for every `U in U(4)`.              (3)

So the previously exhibited exposed mismatched-circle `2+2` line is not merely safe under the two matched cross-gate tori checked last run: **its entire exposed support direction is globally MOC4-safe over all true unitary couplings**. Since `g=22>0`, (3) also has an open spectral/support collar. The separate endpoint gap `12` shows that at the base datum the four block-preserving permutations are isolated from every off-block endpoint in this support direction.

The block determinant itself is the equal average of the four displayed real vertices,

`det(A+U0 B U0*)=(-36-32-27-24)/4=-119/4`,

agreeing with the previous exact witness.

The calculation is independently reproducible from the adjacent exact Gaussian-integer/Fraction checker `CHECK.py`; its committed output is `CHECK_OUTPUT.txt`. The checker constructs the `S4 -> S3` complementary-pair quotient, verifies the six four-point fibers, evaluates exactly 48 external signatures, and asserts `M=0`, `max_outside=-12`, `max_external=-22`, `g=22`, and `det(U0)=-119/4`.

## 3. Bridge to the previous two-gate payment theorem

For a support-exposed `2+2` block base, previous B08 work proved that on either disjoint two-cross-gate torus the local safety criterion is

`C^2 <= delta_10 delta_01`,                                           (4)

with the exact true-unitary interference coefficient `C=|kappa| |L(F)|`. If (4) fails, arbitrarily small genuine unitary perturbations give `h_L(U)>M`.

Combining this with account03/B09's global inequality (1) yields a new necessary consequence:

**Theorem 2 (payment failure forces an external-facet violation).** Any true-unitary two-gate payment failure (4) at a common-block support face forces

`max_external e(f) > M`.

**Proof.** A failure of (4) produces a true unitary `U` with `h_L(U)>M`. Inequality (1) then implies `max_external e(f)>=h_L(U)>M`. QED.

Hence the prior common-block gate obstruction and the partner's Saxl obstruction are not independent. A local common-block counterexample can occur only in the external-deficient branch. Conversely, `max_external e>M` is not itself a counterexample because the external Saxl extremes need not be genuine spinor/unitary points; this is exactly where the partner's phase-exclusion/payment problem begins.

## 4. Interface with the campaign lead and named next obligation

The lead's `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1` isolates zero-entry and strict-interior mechanisms in the generic core. This run removes from boundary consideration every repeated/common-block support datum with nonnegative external gap, and gives a strict global collar whenever the gap is positive. In particular, the concrete mismatched-circle exposed `2+2` datum can no longer serve as a dangerous boundary escape: its whole supporting half-plane is certified globally with exact margin 22 against all 48 external facets.

The first unpaid boundary implication is now named

**`MOC4-COMMON-BLOCK-EXTERNAL-PAYMENT-v1`**:

> For every source-valid support-exposed `2+2` or `1+3` common-block boundary with `max_external e>M`, quantify the loss imposed by the genuine `Lambda^2 SU(4)`/spinor equations strongly enough to pay `max_external e-M`, or construct an actual normal-pair/true-unitary support violation. Arbitrary `(P,R)`, bistochastic, or unconstrained `SO(6)` witnesses do not resolve this branch.

This is aligned with account03/B09's own next obligation `MOC4-EXTERNAL-SPINOR-PAYMENT-v1`, but here it is restricted to B08's common-block boundary. The exact bridge above means a failure of the older two-gate payment already lands inside this external-deficient branch.

## 5. Failure accounting and claim limits

- No full MOC4 proof is claimed.
- No counterexample was found.
- No arbitrary bistochastic/transport relaxation was substituted for a true unitary.
- The strict external gap certificate is support-direction specific; it does not by itself control another support direction of the same spectra.
- External functional values above `M` are only a remaining obstruction to this certificate, not evidence of a genuine MOC4 violation.
- Repeated-spectrum and proper common-block exact theorems are inherited dependencies, not recounted as new target completion here.

## Outcome

`ESSENTIAL_STEP_APPLIED`: a global external-facet certificate replaces local gate analysis on the external-safe common-block branch; it globally closes the previously difficult mismatched-circle exposed `2+2` support direction with exact external margin `22`, and proves that any genuine two-gate payment failure must lie in the partner's external-deficient/spinor-payment branch.
