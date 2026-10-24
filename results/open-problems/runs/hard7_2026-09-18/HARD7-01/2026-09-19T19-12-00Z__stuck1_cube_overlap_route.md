Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen source metric `D_MI: 2 -> 2`. Methods tried: B6 / B18 / B24.**

# HARD7-01 — STUCK1 thinking run for maximal-intersection uniqueness

**Status:** PARTIAL / source OPEN / **STUCK1**. This is the third consecutive run on the admitted maximal-intersection target with unchanged source metric. Under Section I, this run is deliberately a thinking run: it promotes **no new theorem claim**, creates no checker-only artifact, and selects exactly one recovery for the next execution.

## 1. Continuity, ownership, and required reads

I resumed the exact admitted target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T18-05-09Z__mi_cube_collar_uniqueness.md`

and the exclusive claim

`operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md`.

Before doing mathematics I reread the controlling HARD7 file, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest own checkpoints, the canonical claim, and current repository searches around `maximal intersection ellipsoid`, `maximal intersection position`, strong-`(B)` and the Artstein-Avidan--Katzin aliases. Neighboring successor/ownership reports still identify this exact source as owned by HARD7-01 and theorem-scale HARD. No competing owner was found and no alias was used to bypass the claim.

The append-only intake corpora are too large for a truthful claim of a byte-for-byte fresh visual reread of every unchanged historical `probability_1000_intake_*/problems.jsonl` row through this interface. I do not make that claim. I reopened the current intake directories, root selection ledgers, canonical ownership record, and target-specific aliases; missing rendering was not treated as novelty, release, or permission to restart a different target.

Pre-write `master` was read at `6fac842571f716f0a7f80ff948dcbee94eaae701`. I make no shared-root ledger edit in this run.

## 2. Source statement and frozen metric

The source remains Shiri Artstein-Avidan and David Katzin, *Isotropic Measures and Maximizing Ellipsoids: Between John and Loewner*, Proc. Amer. Math. Soc. 146 (2018), Section 4. For a centrally symmetric convex body `K subset R^n`, and a prescribed ellipsoid volume corresponding to an intermediate radius

`r_J < r < r_L`, 

the source asks whether the ellipsoid maximizing

`Vol_n(K cap E)`

among ellipsoids `E` of that volume is unique.

The frozen metric is

`D_MI = largest integer d such that uniqueness is proved for every centrally symmetric K and every intermediate prescribed radius in every dimension n<=d.`

The verified baseline is Bochi's theorem in dimension two:

`D_MI = 2`.

**Before this run:** `D_MI=2`.  
**After this run:** `D_MI=2`.  
**Movement:** none.  
**Unchanged streak on this admitted target:** `3`.

## 3. Fresh current-literature delta

A bounded 2026-09-19 current-status search again checked the canonical aliases and the closest equality/stability literature.

- Jairo Bochi, *On the approximation of convex bodies by ellipses with respect to the symmetric difference metric*, arXiv:1702.03808, explicitly states that MI uniqueness is open in general and proves the positive answer in dimension `2`. His mechanism is strict quasiconcavity on the fixed-area ellipse space, after smoothing/general-position reductions and uniform derivative estimates.
- Orli Herscovici, Galyna V. Livshyts, Liran Rotem and Alexander Volberg, *Stability and the equality case in the B-theorem*, arXiv:2305.17794, characterize equality/stability for the Gaussian strong `(B)` setting and explicitly discuss the maximal-intersection conjecture as a motivation for a uniform-ball no-nontrivial-equality statement. This corrects the older attribution error: this 2023 paper is **not** by Putterman.
- Eli Putterman, *Sharp stability for the (B)-theorem*, arXiv:2608.08472, submitted 2026-08-09, gives dimension-free Gaussian / `1`-log-concave stability and extensions to strong and functional `(B)`. Its abstract does not state the uniform-ball MI uniqueness theorem.
- Hoehner--Roysdon, arXiv:2401.01033, is a functional maximal-intersection analogue, not a resolution of the original convex-body uniqueness question.

I found no current source in this bounded search claiming the full `n=3` theorem or a general-dimensional resolution. This is **bounded negative evidence, not a worldwide novelty certificate**.

## 4. Section-I blocking statement

The exact source-level obstruction is now easy to state and still completely unsolved by this track:

> After an affine normalization in dimension three, assume `B_2^3` is a maximum-intersection ellipsoid of a centrally symmetric convex body `K` for an intermediate prescribed volume. Prove that for every nonzero symmetric trace-zero matrix `A`,
> 
> `Vol_3(K cap e^A B_2^3) < Vol_3(K cap B_2^3).`

Equivalently, prove that no second determinant-one ellipsoid can share the global maximum.

That universal statement, not a cube calculation, is what is required to move

`D_MI: 2 -> 3`.

The existing strong `(B)` theorem supplies global log-concavity along every one-parameter determinant-one deformation. What is missing is a **source-wide strictness/equality mechanism for the uniform-ball intersection problem at a global maximizer**.

## 5. Routes tried and the precise reason each has not closed the source

### Earlier B2 / B5: attack equality by slack coordinates

Exact product-box examples produce nontrivial flat strong-`(B)` segments, even in trace-zero directions. This successfully refuted the literal printed equality list following Artstein-Avidan--Katzin Conjecture 4.1, but it does not refute MI uniqueness.

**Failure for the current source:** the same slack-coordinate boxes are not global maximal-intersection positions.

### Earlier B11: variational/dual deformation

For `K=[-a,a] x [-M,M]^{n-1}`, an explicit determinant-one deformation narrows the inactive directions and widens the active slab, strictly increasing intersection volume.

**What it established:** the simplest flat-equality mechanism is incompatible with global maximality.

**What it did not establish:** every possible flat direction at every stationary symmetric body is killed this way.

### Earlier B12: conserved determinant / stationarity

For the cube, hyperoctahedral symmetry plus `tr A=0` forces the first variation to vanish.

**What it established:** the cube is a genuinely stationary counterexample candidate, unlike the slack box.

**What it did not establish:** source-wide rigidity for arbitrary `K`.

### Earlier B15: break symmetry in the full matrix direction

For the cube collar `a<r<sqrt(2)a`, the exact Hessian calculation retained all off-diagonal shear directions, not merely diagonal scaling. It gave a strict negative Hessian for every nonzero trace-zero symmetric `A`.

**What it established:** centered MI uniqueness for an all-dimensional cube collar.

**Failure at the next scale:** the additive disjoint-cap formula ceases at `r=sqrt(2)a`, exactly when pairs of face caps start to overlap.

### Earlier B30: one boundary scale at a time

The disjoint-cap threshold isolated the first genuinely new geometry. In `n=3`, the remaining cube window is the pair-overlap layer.

**Failure as a source proof:** even a complete cube window remains one highly symmetric body and cannot move `D_MI`.

## 6. B6 — deform continuously through the first overlap threshold

This run deformed from the solved cube collar through the first cap-overlap threshold instead of adding another collar lemma.

Normalize the prescribed ellipsoid to the unit ball and write

`K_s=[-s,s]^3`,

where the full intermediate cube window is

`1/sqrt(3) < s < 1`.

The preceding run covers `s>1/sqrt(2)`. The simplest unproved layer is therefore

`1/sqrt(3) < s <= 1/sqrt(2)`.

For a symmetric trace-zero matrix `A`, let

`F_A(t)=Vol_3(K_s cap e^{tA}B_2^3)`.

The useful deformation is radial rather than face-by-face inclusion-exclusion. For `omega in S^2`,

`rho_K(omega)=s/max_i |omega_i|`,

`rho_t(omega)=(omega^T e^{-2tA}omega)^(-1/2)`,

so

`F_A(t)=(1/3) int_{S^2} min{rho_K(omega)^3,rho_t(omega)^3} d sigma(omega)`.

At `t=0` the ball controls exactly on

`Omega_s={omega in S^2: max_i |omega_i|<s}`.

If

`a(omega)=omega^T A omega`,

`b(omega)=omega^T A^2 omega`,

then the exact Taylor coefficients of the ellipsoid radial cube are

`(rho_t^3)'|_0 = 3a`,

`(rho_t^3)''|_0 = 15a^2-6b`.

This does not yet prove a theorem because the `min` has a moving nonsmooth switching interface. The candidate distributional second-variation identity is

`F_A''(0)
 = (1/3) int_{Omega_s}(15a^2-6b) d sigma
   - (s/sqrt(1-s^2)) int_{partial Omega_s} a^2 d H^1`.      (CANDIDATE)

The sign and coefficient are consistent with the standard moving-interface differentiation: the switching contribution is a negative square divided by the spherical gradient of `rho_K^3`, whose smooth-face magnitude is `3 sqrt(1-s^2)/s`.

**Outcome of B6:** the first overlap layer does not require enumerating pairwise cap volumes. It appears to reduce to an interior quadratic form plus a strictly negative switching-boundary energy. The unresolved point is a complete proof of the candidate second-variation identity across all face-arc endpoints and the endpoint `s=1/sqrt(3)`. No theorem is promoted from this derivation in this STUCK1 run.

## 7. B18 — recast the overlap Hessian as spherical covariance geometry

The radial formulation exposes a representation-theoretic simplification.

Let

`Area=|Omega_s|`,

`p=int_{Omega_s} omega_1^4 d sigma`,

`q=int_{Omega_s} omega_1^2 omega_2^2 d sigma`.

Hyperoctahedral symmetry gives

`Area=3p+6q`.

Writing

`D=sum_i A_ii^2`,

`O=sum_{i != j}A_ij^2`,

an exact moment expansion of the **interior part** of (CANDIDATE) gives

`(1/3)int_{Omega_s}(15a^2-6b)d sigma
 = 3(p-3q)D - 2(p-3q)O`.

Since `|omega_1|<s` on `Omega_s`,

`p <= s^2 int_{Omega_s}omega_1^2 d sigma = (s^2/3)Area`.

Hence for `s^2<=1/2`,

`p-3q=(5p-Area)/2 < 0`.

So the traceless-diagonal irreducible mode is already strictly negative before the boundary term is used. The only potentially dangerous representation is the off-diagonal shear mode, where the interior quadratic form has the opposite sign and must be overcome by switching-boundary dissipation.

**Outcome of B18:** the remaining cube overlap problem collapses from a five-dimensional trace-zero matrix space to one scalar shear inequality, provided the moving-interface formula is justified. That is substantial route compression, not source-metric movement.

## 8. B24 — extremal contact pattern and a candidate scalar shear inequality

Take the representative shear

`A_12=A_21=1`, all other entries zero.

Set

`r0=sqrt(1-s^2)`,

`h=sqrt(1-2s^2)`,

`alpha=arccos(s/r0)`.

In the overlap layer `alpha in [0,pi/4)`. On a face circle, the total allowed angular measure is

`M=2pi-8alpha`,

and

`S2=int_allowed sin^2(2phi)dphi=M/2+sin(4alpha)`.

A direct boundary decomposition into the four faces carrying an `x` or `y` factor and the two `z` faces gives the candidate exact switching energy

`J_shear
 = int_{partial Omega_s}(2 omega_1 omega_2)^2 dH^1
 = 8s^2 r0^3 M + 2r0^5 S2`.

Under (CANDIDATE), the shear second derivative would therefore be

`F_shear''(0)
 = 2(Area-5p) - (s/r0)J_shear`.

The useful point is that the right sign seems to follow from a very cheap geometric bound rather than exact evaluation of `p`.

For fixed first coordinate `x`, the spherical cross-section of `Omega_s` has angular width

`M(x)=2pi-8 arccos( s/sqrt(1-x^2) )`,  `h<=x<=s`.

One computes

`M'(x)=8sx/((1-x^2)sqrt(r0^2-x^2))`,

and

`M''(x)/M'(x)
 = 1/x + 2x/(1-x^2) + x/(r0^2-x^2) > 0`.

Thus `M(x)` is convex, `M(h)=0`, and

`Area=2 int_h^s M(x)dx <= (s-h)M`.

Also `S2>=M/2`. Therefore the boundary penalty divided by two is at least

`[4s^3 r0^2 + (1/2)s r0^4]M`.

Write

`c=s/r0`,  `d=h/r0`.

Then `c^2 in [1/2,1]`, `r0^2=1/(1+c^2)`, and the sufficient scalar inequality

`4s^3 r0^2 + (1/2)s r0^4 >= s-h`

is equivalent to

`c(4c^2+1/2) >= (c-d)(1+c^2)^2`.

Since `c-d<=c` and

`4c^2+1/2-(1+c^2)^2
 =2c^2-c^4-1/2 >= 1/4`, 

the scalar inequality has slack throughout the layer. Combining this with `Area-5p<Area` strongly suggests strict negativity of the shear Hessian as well.

**Important honesty label:** this is a **candidate derivation only**, deliberately not promoted to a theorem in a Section-I thinking run. Before it can become a result, the next run must rigorously justify the nonsmooth second-variation formula, verify the boundary decomposition without double-counting at arc endpoints, and treat the limiting endpoints cleanly. A numerical sample is not being used as proof; no finite simulation is involved.

## 9. What a proof would have to contain that no route so far contains

The track now has several exact special-family strictness results, but none supplies the universal implication

`global MI stationarity in R^3 + strong (B) log-concavity => strictness in every nontrivial trace-zero direction`.

A proof of the source `n=3` case must contain at least one genuinely source-wide ingredient of that kind, or else classify every possible equality configuration for the uniform-ball strong `(B)` inequality under the additional global-maximizer constraints.

The cube route cannot substitute for this. Even if the candidate overlap calculation is completely correct, it proves only a symmetric special case and leaves `D_MI=2`.

Conversely, a counterexample route would have to produce a centrally symmetric `K` with two distinct determinant-one ellipsoids attaining the same **global** intermediate-volume maximum. Flatness without global maximality is already known to be insufficient.

## 10. Simplest special case still unproved at the start of this run

The simplest source-shaped special case not covered by the previous report was:

> `n=3`, `K=[-s,s]^3`, `1/sqrt(3)<s<=1/sqrt(2)`: prove that the centered unit ball is the unique prescribed-volume MI ellipsoid.

Together with the prior `s>1/sqrt(2)` theorem, this would cover the entire centered cube intermediate John--Loewner window in dimension three.

B6/B18/B24 produced the candidate route above. It is now sufficiently concrete to be the **single chosen Section-I recovery** for the next execution.

## 11. Nearest solved problem and the ingredient it has that this one lacks

The nearest complete source theorem is Bochi's `d=2` result. In dimension two, he proves strict quasiconcavity of the intersection area on the affine space of fixed-area ellipses, using smoothing, general position and uniform control of derivatives.

What the present `d=3` problem lacks is an analogue that controls switching surfaces and equality globally. In three dimensions, a deformation meets face/contact sets along curves; pair contacts appear before the Loewner endpoint, and general bodies have no cube symmetry reducing the Hessian to two irreducible coefficients. The strong `(B)` theorem supplies concavity, but no checked uniform-ball equality theorem currently converts that concavity to strictness under the MI stationarity constraints.

That missing equality/strictness mechanism is the real source obstruction.

## 12. Section-I decision: exactly one recovery

**Chosen recovery for the next execution:** **prove the simplest unproved special case from Section 10**.

The next run should not restart the literature survey and should not manufacture another source-metric checker. It should take the candidate radial switching formula above and either:

1. make the nonsmooth second variation completely rigorous and thereby close the full three-dimensional cube window; or
2. find the exact defect in the candidate formula/sign and record that obstruction.

Only after that recovery should the track decide whether there is a plausible source-wide extension or whether Section-I rotation pressure requires a handoff.

Next method triple, different from this run: **B4 / B14 / B25**.

- **B4:** prove the weaker special case completely, with no gap at the switching interface.
- **B14:** exploit the hyperoctahedral group to justify the complete quadratic-form decomposition.
- **B25:** obtain the same switching energy two ways (distributional differentiation and geometric boundary flux) so a sign/factor error cannot hide in the min-interface calculation.

## 13. Checker/artifact decision

No exact-arithmetic checker was created in this run because Section I required a thinking run with **no new claims**, and the only new object is an unpromoted analytic proof route. Creating a certificate for an unchanged source metric would violate the 90/10 instruction rather than strengthen the mathematics.

If the next run promotes a finite identity or theorem-sized cube result, it must put the complete written proof on the page and archive any finite symbolic core under `artifacts/hard7_2026-09-18/HARD7-01/`.

## 14. Capability honesty

The exposed scheduler/task interface still provides schedule/prompt/timing controls but **no model selector, no reasoning selector, and no guaranteed execution duration**. Therefore the requested `GPT-6 / maximum` setting remains prompt text only. The actual model visible to this run is GPT-5.6 Sol; the reasoning level is not authenticated and is reported as UNVERIFIED.

Changing that would require the platform to expose an authorized model/reasoning selection field (or an authorized execution context that does). It cannot be achieved by rewriting repository text.

The historical P26 `You cannot modify this task` event is not evidence of a permanent account-wide block: current `RESULTS.md` records that P26's full update later succeeded in an authorized context, while other context-specific denials remained. For any task that still returns that permission error, the lawful workaround is an authorized owner/workspace context or platform support/API capability; creating a duplicate task or bypassing permissions is not a valid workaround. I did not create, modify, disable, or reactivate any schedule in this run.

## 15. Ledger delta

```yaml
track: HARD7-01
target: MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS
claim: operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md
source_status: OPEN
research_status: PARTIAL / STUCK1
metric: D_MI
before: 2
after: 2
movement: false
unchanged_streak: 3
methods_this_run: [B6, B18, B24]
section_I_recovery_selected: prove_the_simplest_unproved_special_case
next_methods: [B4, B14, B25]
simplest_special_case: "3D cube, 1/sqrt(3)<s<=1/sqrt(2), centered prescribed-volume MI uniqueness"
new_claim_promoted: false
artifact_created: false
artifact_reason: "Section-I thinking run; candidate analytic route only; no finite or theorem-sized claim promoted"
```
