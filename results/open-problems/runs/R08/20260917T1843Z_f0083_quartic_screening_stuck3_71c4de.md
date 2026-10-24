Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in active F0083: `1/2 -> 1/2`, unchanged count `2 -> 3`; I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`. New theorem-sized movement outside the frozen metric: an exact quartic screening law shows that small radius-defect modes in intact critical-lattice bulk are amplifying toward a defect, not neutral/harmonic; the transversely layered tangent has no nonzero bounded bi-infinite mode and arbitrary finite boundary data is exponentially screened. Methods actually used: B16 COMPUTE EVERY SMALL CASE, B9 RANDOMIZE, B10 DERANDOMIZE.** GPT-6 / maximum was requested in prompt text, but the exposed runtime has no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083 quartic screening: the finite-energy channel is not a neutral radius mode

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. The six-unchanged handoff continues to control: I0082 stays frozen at `2/3`, retirement count `6`. The old R08 FPP route remains retired.

The active exclusive claim is `operations/claims/F0083.md`, sourced to Hoffman--Holroyd--Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), arXiv:math/0505668, open problem (i). The frozen candidate is

\[
m_n=\lfloor(1+|n|)^{3/4}\rfloor,\qquad
H=\{(n,a,b,c)\in\mathbb Z^4:1\le a,b,c\le m_n\},\qquad
\Xi_*=\mathbb Z^4\setminus H,
\]

with appetite one. The metric remains the number of two frozen obligations proved:

1. candidate admissibility plus exact local/transient mechanism — **PROVED**;
2. prove two stable allocations of this exact `Xi_*` differ on positive Lebesgue measure — **OPEN**.

Thus the metric stays `1/2`. This is the third consecutive run without movement of that frozen metric, so `unchanged_count=3`; under the owner rule the **next** invocation must be the section-I thinking-only stuck run unless obligation 2 moves before then.

At run start I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the F0083 claim, the newest R08 report, prior F0083 attempt material, and the newest relevant R09 report. R09 is on a distinct claimed Cerf target and has no ownership overlap.

## 2. Source/current-literature and ownership refresh

The 2006 primary source was reread directly. It states that the authors did not know whether uniqueness can fail for stable allocations of **Lebesgue measure** to a deterministic set of centers in Euclidean space, and its final Open Problem (i) asks whether a discrete set can admit two stable allocations differing on a nonnull set. The source also gives the recurrent-configuration uniqueness theorem and the translation-invariant finite-intensity point-process uniqueness theorem.

Fresh bounded searches dated 2026-09-17 used the exact title/authors plus `two stable allocations`, `discrete set of centers`, `Lebesgue`, `deterministic`, `nonuniqueness`, and later stable-allocation terminology. They recovered the source, the Hoffman--Holroyd--Peres tail-bounds follow-up, Poisson-allocation papers, and a later discrete-grid algorithm paper, but no primary paper claiming to resolve this exact deterministic Lebesgue question. This is bounded negative evidence only: worldwide open status and publication novelty remain **UNVERIFIED**.

Ownership remains exclusive to R08 under `operations/claims/F0083.md`.

## 3. B16 — compute the singular local law instead of guessing a harmonic one

The admission run showed that at the critical four-dimensional lattice radius `1`, a radius decrement has no linear response: the first nonzero territory-volume change is quartic. The preceding route nevertheless treated the explicit finite-energy boundary channel as if it might carry a neutral harmonic radius mode. This run computes the coupled quartic law and shows that inference is wrong.

### 3.1 Local scaling at one critical Voronoi corner

At a corner shared by the sixteen vertices of a unit four-cube, write the radius of a center as

\[
R_s(t)=1-\frac t2 a_s,
\]

and zoom by `x=c+t z`. If `s in {+/-1}^4` labels the corner vertex, then

\[
|x-v_s|^2=1-t\,s\cdot z+t^2|z|^2,
\]

whereas

\[
R_s(t)^2=1-t a_s+\frac{t^2a_s^2}{4}.
\]

Hence, on every fixed bounded `z` set,

\[
\text{center }s\text{ is active}\quad\Longleftrightarrow\quad
s\cdot z\ge a_s+O(t).
\tag{3.1}
\]

Lebesgue volume scales by `t^4`. Since away from the sixteen old cube corners there is a fixed positive margin to the unit sphere / active-face constraints, every `O(t^4)` change is localized in these corner charts; the `O(t)` perturbation of the scaled hyperplanes contributes only `O(t^5)` to physical volume.

### 3.2 Exact transversely layered corner functional

Now impose the simplest nontrivial symmetry: all eight centers on one side of the axial interface have threshold `a`, and all eight on the other side threshold `b`. In one fixed transverse sign orthant, let `u>=0` be axial distance from the interface and let

\[
U=|z_2|+|z_3|+|z_4|.
\]

The three-dimensional slice with sum `U` has density `U^2/2`. The old territory loses the simplex

\[
\{u\ge0,\ U\ge0,\ u+U<a\},
\]

whose exact scaled volume is

\[
L(a)=\frac{a^4}{24}.
\tag{3.2}
\]

If `b>a`, the neighboring layer is inactive on a tent from which the first layer can gain. Its exact scaled volume is

\[
G(a,b)
=\int_0^{(b-a)/2}\int_{a+u}^{b-u}\frac{U^2}{2}\,dU\,du
=\frac{(b-a)^2(7b^2+10ab+7a^2)}{192};
\tag{3.3}
\]

set `G(a,b)=0` for `b<=a`.

A center has sixteen corners, eight facing each axial neighbor. Therefore the leading appetite-one equation for a layered tangent profile `(a_n)` is

\[
\boxed{
G(a_n,a_{n-1})+G(a_n,a_{n+1})=\frac{a_n^4}{12}.
}
\tag{3.4}
\]

This recovers the one-sided half-space polynomial from the previous run when only one neighboring layer has larger defect, but (3.4) is the two-sided local law needed for boundary-at-infinity tests.

### 3.3 Exact screening factor for the layered tangent

By homogeneity,

\[
\frac{G(a,ra)}{a^4}
=\frac{(r-1)^2(7r^2+10r+7)}{192}.
\]

Let `rho_layer>1` be the unique solution of

\[
2G(1,\rho_{\rm layer})=\frac1{12}.
\]

Equivalently,

\[
\boxed{
7\rho_{\rm layer}^4-4\rho_{\rm layer}^3-6\rho_{\rm layer}^2-4\rho_{\rm layer}-1=0,
}
\tag{3.5}
\]

and exact rational bracketing gives

\[
1.466<\rho_{\rm layer}<1.467,
\qquad
\rho_{\rm layer}=1.466721202180643\ldots.
\tag{3.6}
\]

Because `G(1,r)` is strictly increasing for `r>1`, (3.4) implies the following maximum principle:

> If `a_n>0`, at least one of `a_{n-1},a_{n+1}` is at least `rho_layer a_n`.

Indeed, if both were smaller, the left side of (3.4) would be less than `2G(a_n,rho_layer a_n)=a_n^4/12`.

Once the larger neighbor is chosen, the path cannot reverse: the previous site has strictly smaller amplitude. Thus on the full line a positive amplitude generates a one-directional path growing by at least `rho_layer` at every step. Consequently:

\[
\boxed{
\text{the only bounded nonnegative bi-infinite solution of (3.4) is }a_n\equiv0.
}
\tag{3.7}
\]

For a finite interval with boundary amplitudes bounded by `A`, the same path argument gives the deterministic estimate

\[
\boxed{
a_n\le A\,\rho_{\rm layer}^{-\operatorname{dist}(n,\partial I)}.}
\tag{3.8}
\]

So the layered quartic tangent has a **mass gap / screening**, not a neutral harmonic mode.

## 4. A stronger nonsymmetric local screening bound

The preceding calculation could still have been an artefact of transverse symmetry. It is not. There is a universal small-defect amplification mechanism using only the eight face neighbors of one lattice center.

Fix one old Voronoi corner of the origin, normalize the origin threshold to `a`, and suppose every incident face-neighbor threshold is at most `b`. Ignore every diagonal competitor entirely; this can only **increase** the set of sites the origin might receive, so the resulting gain is an upper bound valid without symmetry assumptions.

If exactly `k` coordinates, `k=1,2,3`, have crossed their old Voronoi faces, write `P` for their positive excursions and `N` for the sum of the remaining negative-side magnitudes. The origin score is `A=N-P`. For the origin to remain active and every crossed face neighbor to be inactive we need

\[
A\ge a,\qquad p_i<\frac{b-A}{2}.
\tag{4.1}
\]

Integrating the simplex slices exactly gives, for a fixed sign pattern,

\[
\begin{aligned}
U_1(a,b)&=\frac{(b-a)^2(7b^2+10ab+7a^2)}{192},\\
U_2(a,b)&=\frac{(b-a)^3(5b+3a)}{96},\\
U_3(a,b)&=\frac{(b-a)^4}{32}.
\end{aligned}
\tag{4.2}
\]

There are `binom(4,k)` such sign patterns. Thus the **total possible gain outside the old orthant at one corner**, even after deleting every diagonal competitor, is at most

\[
\boxed{
U_{\rm face}(a,b)
=\sum_{k=1}^3\binom4kU_k(a,b)
=\frac{(b-a)^2(7b^2-2ab+a^2)}{12}.
}
\tag{4.3}
\]

The unavoidable old-orthant loss is still `a^4/24`. Let `rho_face>1` satisfy

\[
U_{\rm face}(1,\rho_{\rm face})=\frac1{24}.
\]

Equivalently,

\[
\boxed{
14\rho_{\rm face}^4-32\rho_{\rm face}^3+24\rho_{\rm face}^2-8\rho_{\rm face}+1=0,
}
\tag{4.4}
\]

with

\[
1.233<\rho_{\rm face}<1.234,
\qquad
\rho_{\rm face}=1.2333606010903217\ldots.
\tag{4.5}
\]

The function in (4.3) is strictly increasing in `b>a`, so the root is unique.

### Theorem 2 — small-defect amplification in intact `Z^4` bulk

Fix any `rho` with

\[
1<\rho<\rho_{\rm face}.
\]

Then there exists `epsilon_0(rho)>0` with the following property. Let `Xi subset Z^4`, let `psi` be a stable appetite-one allocation, and let `x in Xi` have all eight face neighbors `x +/- e_i` present in `Xi`. Write

\[
R_y=\operatorname*{ess\,sup}_{\psi(z)=y}|z-y|,
\qquad
\epsilon_y=1-R_y.
\]

(The prior lattice-subset theorem gives `0<=epsilon_y<1` and every center is sated.) If

\[
0<\epsilon_x<\epsilon_0(\rho),
\]

then

\[
\boxed{
\max_{i,\pm}\epsilon_{x\pm e_i}>\rho\,\epsilon_x.
}
\tag{4.6}
\]

#### Proof

Assume all eight face-neighbor deficits are at most `rho epsilon_x`. Since a site closer to a face neighbor than to `x` cannot belong to `x` whenever that face neighbor is active, the territory of `x` is contained in the purely geometric upper set obtained by retaining only those eight face competitors and giving each the **smallest allowed radius** `1-rho epsilon_x`; deleting all other competitors only enlarges this upper set.

At `epsilon_x=0` this upper set is exactly the unit Voronoi cube. For small positive `epsilon_x`, its volume change is localized at the sixteen cube corners. Put `t=2 epsilon_x` and use the scaling (3.1). At each corner, the normalized unavoidable loss is `1/24`, whereas (4.3) with `a=1,b=rho` is an upper bound on every possible gain. Therefore

\[
|A_\rho(\epsilon_x)|
=1+16(2\epsilon_x)^4
\left(U_{\rm face}(1,\rho)-\frac1{24}\right)
+o(\epsilon_x^4).
\tag{4.7}
\]

Because `rho<rho_face`, the coefficient in parentheses is strictly negative. Hence `|A_rho(epsilon_x)|<1` for all sufficiently small positive `epsilon_x`. But `x` is sated and its territory has volume exactly one, contradiction. This proves (4.6). QED.

This theorem is the nonsymmetric version of the layered screening mechanism. It says that a small radius deficit in an intact critical-lattice neighborhood cannot be an isolated or slowly varying mode: moving one face step in some direction amplifies it by a fixed factor greater than one.

## 5. B9 — randomized end data do not produce a hidden phase

The previous plan proposed finite truncations of the face/tube channel with random opposite boundary data, looking for a central signal that survives as the truncation grows. The exact layered law now answers that experiment before simulation is needed.

Let the boundary amplitudes of a finite layered interval be arbitrary random variables, but assume pathwise

\[
0\le a_{\partial I}\le A.
\]

Equation (3.8) holds **for every realization**, hence

\[
a_n\le A\rho_{\rm layer}^{-\operatorname{dist}(n,\partial I)}
\quad\text{a.s.}
\]

Therefore the central amplitude converges to zero uniformly as the interval grows. Randomizing the boundary cannot uncover a persistent phase in this tangent model; the route fails for a structural reason, not because the wrong random law was sampled.

This is the B9 outcome: the random-boundary experiment is dominated by a deterministic exponential screening estimate and is therefore retired for the transversely layered mode.

## 6. B10 — derandomization gives the stronger conclusion

The same path argument is already the derandomization. No averaging or positive-probability event is needed: **every** bounded deterministic boundary condition obeys (3.8). Thus the finite-energy graph channel built at admission is not by itself a candidate for a neutral radius phase.

This corrects an important conceptual overreach in the earlier route. The abstract conductance channel has finite resistance to infinity, but the active-cell volume equation contributes a quartic geometric sink. Graph transience is necessary for HHP disagreement, not sufficient for a nontrivial stable-allocation phase.

The surviving geometric possibility is more specific:

- deep intact bulk: small radius-defect modes are screened by Theorem 2;
- periodic flat-face tangent: already proved unique;
- periodic edge tangent: already proved unique;
- triple-corner tangent: still not covered by recurrence reduction and is the first local model where missing face neighbors can defeat Theorem 2.

So the next serious object is no longer the whole side-face finite-energy channel. It is the periodic triple-corner configuration

\[
\Xi_{\rm corner}
=\mathbb Z^4\setminus
\{(n,a,b,c):a\ge1,\ b\ge1,\ c\ge1\},
\tag{6.1}
\]

and, specifically, whether its site-optimal and center-optimal allocations coincide.

## 7. Metric/status and stuck threshold

The frozen source-closing obligation has **not** moved:

\[
\boxed{1/2\to1/2.}
\]

This is now three consecutive unchanged runs, so R08 enters **STUCK1** operationally. In accordance with section I, the **next run** must be thinking-only and must write the five-part stuck report before adding another lemma. The simplest still-unproved special case to put at the center of that report is (6.1), the periodic triple-corner tangent.

The exact blocker remains

\[
\boxed{
\psi_{\rm site}^{\Xi_*}\stackrel{?}{\neq}
\psi_{\rm center}^{\Xi_*}
\quad\text{on a set of positive Lebesgue measure}.}
\tag{7.1}
\]

This run makes one route materially less plausible: a small-amplitude phase transported along the admitted flat-face conductance channel is incompatible with the exact quartic screening law.

## 8. Exact finite-core certificate

The finite algebraic core was independently executed before archival. Files:

- `artifacts/R08/20260917T1844Z_quartic_screening_exact.py`
- `artifacts/R08/20260917T1844Z_quartic_screening_exact.out`

The archived output begins `PASS exact symbolic checks` and verifies (3.2), (3.3), polynomial (3.5), the three sign-pattern integrals (4.2), the sum (4.3), polynomial (4.4), and exact rational brackets for both roots. This is a **self-check of the finite symbolic core**, not an audit of the infinite-dimensional theorem or F0083.

## 9. Model/scheduler control status

The control limitation is still exactly the one recorded in the current owner policy and root ledger. The exposed task interface offers title, prompt, schedule/timing, enablement, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run telemetry**. Therefore the string `GPT-6 / maximum` can be requested in prompt text but cannot be enforced or verified here.

The historical `You cannot modify this task` response for P26 was an authorization/context boundary, not a mathematical issue. The supported workaround is the authorized owning account/workspace, a supported ownership/admin transfer, or platform support. A duplicate task or repository edit is not a valid bypass. Actually guaranteeing GPT-6/maximum requires native model/reasoning fields plus run telemetry in the owning interface/API.

## 10. Next-run constraint

Because `unchanged_count=3`, the next invocation must perform the owner-prescribed STUCK1 thinking report. It should **not** produce another incremental local lemma first. It must inventory all F0083 routes and then choose exactly one recovery. The natural fresh B triple to evaluate there is **B2 (try to refute the admitted candidate by proving uniqueness), B18 (rewrite the triple-corner tangent as a lower-dimensional/product allocation problem), B24 (identify the extremal radius profile on that tangent)**. This triple is distinct from the present B16/B9/B10 and the previous B17/B21/B22.

```yaml
ledger_delta:
  track: R08
  original_target:
    id: I0082
    status: RETIRED_FROZEN
    metric: 2/3
    retirement_count: 6
  active_target:
    id: F0083
    owner: R08
    status: PARTIAL_OPEN_STUCK1
    candidate: Xi_* = Z^4 minus the expanding m_n^3 tube
    metric_name: frozen obligations proved for this explicit candidate
    before: 1/2
    after: 1/2
    movement: no movement
    unchanged_count_before: 2
    unchanged_count_after: 3
    source_closure: false
    new_results_outside_metric:
      - exact two-sided transversely layered quartic tangent equation
      - no nonzero bounded bi-infinite layered quartic mode
      - deterministic finite-interval screening factor rho_layer = 1.466721202180643...
      - nonsymmetric small-defect face-neighbor amplification threshold rho_face = 1.233360601090321...
    route_retired_this_run:
      - random bounded boundary data on the transversely layered flat-face tangent as a persistent phase mechanism
    next_required_mode: STUCK1_THINKING_ONLY
    next_simplest_special_case: periodic triple-corner tangent Xi_corner
  methods:
    B16: exact quartic local/tangent computation; produced G(a,b), rho_layer, rho_face
    B9: randomized bounded boundary data; pathwise screening kills the phase
    B10: derandomized to deterministic exponential screening
  exact_artifacts:
    checker: artifacts/R08/20260917T1844Z_quartic_screening_exact.py
    output: artifacts/R08/20260917T1844Z_quartic_screening_exact.out
    result: PASS exact symbolic checks
  literature_status: OPEN_CURRENT_BOUNDED; worldwide/novelty UNVERIFIED
  ownership_status: exclusive R08 claim preserved
  shared_roots_edited: false
  peer_files_edited: false
```
