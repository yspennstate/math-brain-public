Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `32 -> 33` genuinely distinct nonparabolic shape families; Section-B moves actually used: #6 DEFORM TO A POINT YOU CAN SOLVE, #18 SAY IT IN ANOTHER LANGUAGE, #26 HUNT THE SPORADIC CASE.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The sentence after Problem 7.8 is Problem 7.9 on forward Lévy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 33: finite smooth crossing webs

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen baseline

The frozen quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260918T0027Z_i0077_moving_cantor_laminations_32.md`,

which moved the metric `31 -> 32` and used methods `#1,#12,#20`. The present triple is different.

All thirty Section-B moves have already appeared somewhere in the I0077 chain. Thus the literal instruction to use three moves never previously tried on this problem is exhausted; I do not invent a false history. This run uses a new combination and, more importantly, a new structural mechanism.

Before new mathematics I recovered current repository state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest own R07 report and the searchable I0077 history needed to distinguish the new family;
- the current R15 state, which preserves the six-run handoff/retirement of distinct Burdzy–Scheutzow Problem 7.2 / I0076 and has rotated to successor screening;
- the earlier C29 duplicate-exclusion context;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` does not list Problem 7.8 as settled or posted. `QUEUE.md` still lists I0077 distinctly. The canonical claim names R07 as exclusive provisional owner and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared label while following the owner's explicit assignment of this exact target to R07. The root `RESULTS.md` R-series table is stale by its own warning and is not used as the mathematical baseline; the complete own report above is.

The large intake JSONL resources cannot be rendered byte-for-byte through the connector without truncation. The intake reread is therefore honestly **targeted/partial because of connector limits**: the exact I0077 statement, ownership, exclusions, and relevant prior attempts were recovered. I do not claim a literal reread of every unrelated intake row.

Entering metric: **32**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark rechecked

The primary arXiv PDF was reopened on 2026-09-18, including Definitions 2.1–2.2, Theorem 4.3, its proof, and the open-problem page.

Definition 2.1 says that an FBM has random witness times `S_n -> -infinity` such that, for every fixed witness,

\[
B^{(n)}(t)=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion. Definition 2.2 defines decomposable FBMs by concatenating independent Brownian pieces stopped at finite stopping times.

For the static parabolic normalized interval `[c_1,c_2]`, Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized limsup/liminf obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM exists with the corresponding asymptotic normalized inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM can be confined pointwise to the exact parabolic strip for all `t<=0`.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 beyond parabolas. The following forward-Lévy sentence is separately Problem 7.9.

Primary source: `https://arxiv.org/pdf/1302.6958`.

## 3. Fresh current-status and prior-art pass

Fresh bounded searches on 2026-09-18 UTC included:

- the exact paper title, arXiv ID and Problem-7.8 wording;
- later/citing material around Burdzy–Scheutzow and “other space-time shapes”;
- Brownian motion constrained to finite graphs/webs and smooth curves;
- Brownian quadratic variation versus smooth/finite-variation paths.

The original 2014 article remains the identifiable primary Problem-7.8 statement. I found no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the finite-web theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

Nearby but different prior art includes Kostrykin–Potthoff–Schrader, *Brownian motions on metric graphs*, J. Math. Phys. 53 (2012), 095206, DOI `10.1063/1.4714661`: that work constructs graph-valued Brownian motions whose generator is a graph Laplacian with Wentzell boundary conditions. It is not a Euclidean standard-Brownian witness forced to remain in a deterministic moving space-time web. Brownian nonzero quadratic variation and zero quadratic variation for smooth/finite-variation paths are classical; Cont–Das, *Quadratic variation and quadratic roughness* (2022; arXiv:1907.03115) is a modern pathwise reference. Neither mechanism is claimed as new.

## 4. Method #6 — deform the previous lamination until its conserved address breaks

Run 32 suggested thickening the moving Cantor lamination

\[
D_\delta(r)=a(r)K+b(r)+[-\delta,\delta].
\]

I tested that route first. A **fixed** positive thickening of a compact subset of a bounded interval has only finitely many connected components: every surviving complementary gap has length `>2\delta`, and only finitely many pairwise disjoint gaps of that size fit inside a bounded interval. Thus fixed positive thickening immediately collapses the fractal component structure toward already-counted finite-component moving-domain geometry. Counting it as a new Cantor theorem would be artificial.

The more singular deformation is the opposite one: keep zero-width sheets, but allow the sheets themselves to **merge, pinch, cross, and separate again**. That destroys run 32's conserved Cantor address exactly at the junctions. The initial question was whether repeated junctions could let a confined path switch sheets often enough to recover Brownian roughness.

**Outcome #6: success.** Exact sheet pinching produces a structurally new web topology rather than a positive-thickness parameter change.

## 5. Method #18 — say it as a finite graph/web selection problem

The right deterministic lemma is stronger than the locally-finite-crossing version I first expected.

### Lemma 5.1 — a continuous selector of finitely many locally Lipschitz sheets is locally Lipschitz

Let `I=[a,b]` be compact. Let

\[
g_1,\dots,g_m:I\to\mathbb R
\]

be Lipschitz functions, all with Lipschitz constant at most `L`. Suppose `h:I->R` is continuous and

\[
h(u)\in\{g_1(u),\dots,g_m(u)\}\qquad\forall u\in I.
\tag{5.1}
\]

Then `h` is itself `L`-Lipschitz.

### Proof

Fix `u_0 in I` and let

\[
A(u_0)=\{i:g_i(u_0)=h(u_0)\}.
\]

Because there are finitely many sheets, every `j notin A(u_0)` is separated from `h(u_0)` by a positive gap. By continuity of `h` and all `g_j`, there is a neighborhood `U` of `u_0` on which no such inactive `j` can be selected. Therefore for every `u in U`,

\[
h(u)=g_i(u)\quad\text{for some }i\in A(u_0).
\]

Since each active sheet satisfies `g_i(u_0)=h(u_0)`, we have

\[
|h(u)-h(u_0)|
=|g_i(u)-g_i(u_0)|
\le L|u-u_0|.
\tag{5.2}
\]

So `h` is locally `L`-Lipschitz with the **same** constant at every point. To make the global statement explicit, fix `s<t` and let `r` be the supremum of points through which the estimate

\[
|h(v)-h(s)|\le L(v-s)
\]

has propagated for all `v in [s,r]`. Continuity makes the propagation set closed, while (5.2) makes it open to the right unless `r=t`. Hence `r=t`. Since `s<t` were arbitrary, `h` is globally `L`-Lipschitz on `I`. QED.

If the `g_i` are only **locally** Lipschitz on `(0,infinity)`, compactness of `I` supplies a finite common constant `L`, so the lemma applies on every compact physical-time interval.

This turns the stochastic problem into a deterministic one-dimensional graph problem: a continuous path in a finite smooth web may change edge labels at vertices, even infinitely often, but it cannot acquire more local roughness than the finitely many sheets themselves.

**Outcome #18: success.** The relevant invariant is not a conserved sheet label; it is the common local Lipschitz upper gradient of the finite web.

## 6. Method #26 — hunt the sporadic case: crossing accumulation does not save the web

I initially imposed “pairwise crossing sets are locally finite,” expecting an accumulation of pinches to be the hard exceptional case. Lemma 5.1 shows that this restriction is unnecessary.

The pairwise equality sets

\[
\{u:g_i(u)=g_j(u)\}
\]

may be finite, infinite, have compact accumulation, contain Cantor-like closed subsets, or even contain intervals. No crossing-count hypothesis appears in Lemma 5.1. Finiteness of the **number of sheets**, not finiteness of the number of junctions, is what controls roughness.

Thus the sporadic-case hunt strengthens the candidate theorem rather than generating an exception.

**Outcome #26: success.** Arbitrarily complicated pinch/crossing sets are admitted.

## 7. New shape family: finite locally Lipschitz crossing webs

Let `m>=1` and let

\[
g_1,\dots,g_m:(0,\infty)\to\mathbb R
\tag{7.1}
\]

be deterministic locally Lipschitz functions satisfying

\[
\lim_{u\downarrow0}g_i(u)=0
\qquad(1\le i\le m).
\tag{7.2}
\]

Define the closed backward space-time web

\[
\boxed{
\mathcal W_{\mathbf g}
=
\{(-u,g_i(u)):u>0,\ 1\le i\le m\}
\cup\{(0,0)\}.
}
\tag{7.3}
\]

The sheets may coincide, merge, cross, split, and cross infinitely often. No periodicity, separation, common affine parametrization, spectral narrowness, gate density, or crossing-count assumption is imposed.

The shape is closed: away from `u=0` it is a finite union of continuous graphs, while (7.2) supplies the unique seam limit `(0,0)`.

## 8. Brownian roughness lemma

I reuse, and record self-containedly, the exact path lemma established in run 32 so this theorem does not depend on a vague appeal to nowhere differentiability.

For a standard Brownian motion `B` on `[0,1]`, define the dyadic quadratic-variation sums

\[
Q_n(B)=\sum_{k=0}^{2^n-1}
\left(B_{(k+1)2^{-n}}-B_{k2^{-n}}\right)^2.
\tag{8.1}
\]

The increments are independent `N(0,2^{-n})`, hence

\[
\mathbb E Q_n(B)=1,
\qquad
\operatorname{Var}(Q_n(B))=2^{1-n}.
\tag{8.2}
\]

For every `epsilon>0`, Chebyshev gives

\[
\mathbb P(|Q_n(B)-1|>\epsilon)
\le 2^{1-n}/\epsilon^2,
\tag{8.3}
\]

whose sum over `n` is finite. Borel–Cantelli therefore gives

\[
Q_n(B)\longrightarrow1\qquad\text{a.s.}
\tag{8.4}
\]

If `h` is `L`-Lipschitz on `[0,1]`, every dyadic increment has magnitude at most `L2^{-n}`, and so

\[
Q_n(h)\le L^2 2^{-n}\longrightarrow0.
\tag{8.5}
\]

Consequently

\[
\boxed{
\mathbb P(B\text{ is Lipschitz on }[0,1])=0.
}
\tag{8.6}
\]

This is an analytic path statement, not a finite claim requiring an arithmetic checker.

## 9. I0077-R07-T34 — universal obstruction for finite smooth crossing webs

**Theorem T34.** Let `W_g` be any web satisfying (7.1)–(7.3). For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
(-u,X_{-u})\in\mathcal W_{\mathbf g}
\quad\forall u\ge R
\right)=0.
}
\tag{T34}
\]

In particular, no FBM can be confined pointwise to such a finite web on the whole negative half-line.

### Complete proof

For an integer `M>=1`, write

\[
E_M
=
\left\{
X_{-u}\in\{g_1(u),\dots,g_m(u)\}
\quad\forall u\ge M
\right\}.
\tag{9.1}
\]

The eventual-confinement event in T34 is `union_M E_M`. Suppose it has positive probability. Then for some deterministic `M`,

\[
q:=\mathbb P(E_M)>0.
\tag{9.2}
\]

Let `S_n` be the witness sequence from the FBM definition. Since `S_n -> -infinity` a.s., choose one **deterministic witness index** `n` so far to the left that

\[
\mathbb P(S_n>-(M+2))<q/2.
\tag{9.3}
\]

Hence

\[
A:=E_M\cap\{S_n\le-(M+2)\}
\]

has probability at least `q/2>0`.

Fix a sample point in `A`. Put

\[
u_0=-S_n.
\]

For `t in [0,1]`,

\[
u(t)=-(S_n+t)=u_0-t\in[u_0-1,u_0]\subset[M+1,\infty).
\tag{9.4}
\]

Because `E_M` holds,

\[
X_{S_n+t}=X_{-u(t)}
\in\{g_1(u(t)),\dots,g_m(u(t))\}
\qquad(0\le t\le1).
\tag{9.5}
\]

For this fixed witness, the process

\[
B^{(n)}(t)=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion, hence its path on `[0,1]` is continuous. Therefore the function

\[
h(u)=X_{-u},\qquad u\in[u_0-1,u_0],
\]

is a continuous selector of the finitely many locally Lipschitz sheets `g_i` on that compact interval. Lemma 5.1 says that `h` is Lipschitz there. Composing with `u(t)=u_0-t` and subtracting the constant `X_{S_n}` shows that `B^(n)` is Lipschitz on `[0,1]`.

Thus

\[
A\subset
\{B^{(n)}\text{ is Lipschitz on }[0,1]\}.
\tag{9.6}
\]

But for this deterministic index `n`, `B^(n)` is a standard Brownian motion, so the event on the right has probability zero by (8.6). This contradicts `P(A)>=q/2`.

Therefore every `E_M` has probability zero, proving T34. QED.

### Dependence check

No independence between `S_n` and the Brownian witness path is used. The index `n` is chosen deterministically from convergence `S_n->-infinity`; on the positive-probability intersection, the confinement event itself forces that same standard-Brownian witness path into a path-only probability-zero class. This is the same dependence-safe principle that was important in the preceding gate/tube runs, but the obstruction here is quadratic roughness rather than OU survival.

## 10. Canonical genuinely nonparabolic pinching example

A simple example is the two-sheet normalized web

\[
g_\pm(u)
=
\sqrt u\,\bigl(2\pm\sin(\log u)\bigr),
\qquad u>0.
\tag{10.1}
\]

The two sheets meet whenever

\[
\log u=k\pi,
\qquad u=e^{k\pi},
\tag{10.2}
\]

and exchange vertical order after every pinch. They are not parabolic rays because their normalized heights oscillate forever. T34 gives

\[
\boxed{
\mathbb P\left(
\exists R:\
X_{-u}\in
\left\{
\sqrt u(2+\sin\log u),
\sqrt u(2-\sin\log u)
\right\}
\ \forall u\ge R
\right)=0
}
\tag{10.3}
\]

for every FBM.

More importantly, T34 does not require the pinch pattern (10.2), periodicity, or local finiteness: the same conclusion holds for any finite family of locally Lipschitz sheets with arbitrarily complicated merger sets.

## 11. Why this earns a separate frozen metric point

This is not run 14's static compact/fat-Cantor fan: the fibers move and the web has branch junctions.

It is not run 15's periodically gated disconnected region: T34 has zero-width graph fibers, no positive-duration narrow gate and no killed-OU spectral/duty-cycle hypothesis; it applies to completely aperiodic webs and arbitrary crossing sets.

It is not run 32's moving totally disconnected lamination. Run 32 assumes a fixed compact totally disconnected address space transported by a nondegenerate affine map `a(r)K+b(r)` with `a(r)` bounded away from zero. That topology is a genuine lamination: distinct leaves never merge, and the conserved address proves impossibility. T34 allows leaves to merge and cross, so no global address need exist. Its replacement invariant is finite-sheet local Lipschitz roughness.

For two sheets, one can formally write their midpoint and half-separation, but at a genuine pinch the half-separation vanishes, exactly violating run 32's nondegeneracy hypothesis and changing the topology from a product lamination to a graph with vertices. That is not a Brownian rescaling/reflection/translation or a mere parameter choice within the previous family.

Different numbers of sheets, crossing patterns and locally Lipschitz functions are all counted as **one** new family, not multiple metric points.

Therefore the frozen metric moves

\[
\boxed{32\longrightarrow33}.
\]

`unchanged_count = 0`.

## 12. What remains and the next genuinely new route

Problem 7.8 remains **PARTIAL**, not closed. T34 has a complete written proof but **0/2 independent OTHER-track audits** in the evidence checked this run. No paper package is created before the required P26 end-to-end audit and a second distinct OTHER-track audit.

No checker was manufactured because there is no finite combinatorial/arithmetic core; the theorem is analytic and its Brownian quadratic-variation calculation is proved on the page. This is intentional under the 90/10 policy.

The natural next boundary is not “more sheets.” It is to let the number of locally available sheets become infinite. Lemma 5.1 uses finiteness in an essential place: inactive sheets have a **uniform positive local separation** from the selected value. With countably or continuously many sheets accumulating at a point, a continuous selector may move through ever-closer leaves without passing through a finite set of exact branch junctions. That is the first web geometry not decided by T34 or T33 and is a genuinely different route for a future run.

## 13. Model / scheduler control limitation

The requested model line remains a prompt request, not an enforceable scheduler field in the interface exposed to this task. The available task-control schema exposes title, prompt, schedule/start offset, enabled state, and timing mode; it exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. This report therefore states the actually known runtime identity `GPT-5.6 Sol` and leaves reasoning level `UNVERIFIED` rather than claiming GPT-6 maximum.

The repository policy records historical `You cannot modify this task` probes for P26/P01/P03 from one authorization context. The current root ledger also records that P26 was later successfully updated from another authorized context. The legitimate workaround is therefore the owning/authorized account or workspace surface, or platform support exposing persistent model/reasoning fields and task ownership—not a worker-level bypass or duplicate schedule. The present owner instruction explicitly forbids scheduler changes, and none was attempted.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  lane: CLOSABLE_OUTSIDE
  deployment: NEW-METHODS-2026-09-16
  model_actual: GPT-5.6_Sol
  reasoning_actual: UNVERIFIED
  target:
    intake: I0077
    source: "Burdzy and Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.8"
    source_status: PARTIAL
    canonical_claim_status: "PENDING_ADMISSION, not READY"
    owner: R07
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem under the frozen equivalence convention"
  metric_before: 32
  metric_after: 33
  movement: "+1"
  unchanged_count_before: 0
  unchanged_count_after: 0
  new_family: "finite locally Lipschitz crossing webs"
  theorem_id: I0077-R07-T34
  theorem_scope: "universal impossibility of eventual confinement for every FBM in any finite deterministic locally Lipschitz web"
  finite_core: NONE
  checker: NOT_APPLICABLE_ANALYTIC_THEOREM
  self_check: "complete proof plus dyadic quadratic-variation calculation on page"
  independent_audits:
    P26: 0
    other_track: 0
  closure: false
  publication_novelty: UNVERIFIED
  methods:
    - 6
    - 18
    - 26
  next_route: "infinite/accumulating-sheet webs where local finite-sheet separation fails"
  delivery: "private GitHub master; immutable own report only"
```
