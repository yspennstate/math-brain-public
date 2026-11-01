Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO MOVEMENT:** `epsilon_bridge: 1/14,469,504 -> 1/14,469,504`; supported unchanged count `2 -> 3`; **STUCK_RECOVERY_1 / thinking-only**. Methods actually tried: **#8 GO THE OTHER WAY AND DISCRETIZE, #10 DERANDOMIZE, #26 HUNT THE SPORADIC CASE**.

# R16 HARD OUTSIDE — I0036 / Schramm Problem 2.1: stuck recovery 1, exact obstruction to length-preserving four-terminal switching, and a Fomin-type route

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`. Source-level status: **PARTIAL / OPEN**. This report makes no new source-level theorem claim and does not improve the frozen bridge exponent. Its purpose is to execute the required first stuck recovery, isolate the geometric obstruction precisely, and select one genuinely different route.

## 1. Continuity, repository state, source status, and ownership

I continued from

`runs/R16/2026-09-17T13-45-25Z_i0036-n0-defect-fkg-barrier_6e31.md`,

whose retained metric was

\[
\boxed{B_T\le 1000\,T^{-1/14,469,504}\qquad(T\ge1)}
\]

and whose supported unchanged count was `2`. That report prescribed the nonrepeating triple `#8,#10,#26` used here and required a stuck recovery if the metric again failed to move.

Before research I recovered/read or directly queried the current campaign controls required by the owner:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- exclusive claim `operations/claims/I0036.md`;
- the newest R16 report and the preceding R16 phase/Fourier, weighted-pigeonhole, and recurrence reports;
- the exact I0036 intake/source record via the intake search surface;
- the older neighboring planar-SAW R11 stuck report and its Krachun--Panagiotis handoff;
- current R13 / R12 material concerning the recent Komlos/Beck--Fiala preprint claim.

The large intake JSONL files cannot be rendered literally in one connector response. I do not claim a byte-for-byte manual reread of all roughly 780 rows. The active exact source, exclusions, ownership, prior R16 history, and relevant neighboring SAW/discrepancy state were recovered directly.

I0036 remains **R16 exclusive / ADMITTED_ACTIVE / HARD_OUTSIDE**. The exact source is Oded Schramm, *Conformally invariant scaling limits: an overview and a collection of problems*, ICM 2006, arXiv:math/0602151, Problem 2.1: prove existence of the small-mesh scaling limit of the infinite half-plane fixed-lattice self-avoiding walk and identify it with `SLE_{8/3}`. A fresh dated 2026-09-17 search again recovered Krachun--Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, as the strongest directly relevant quantitative fixed-lattice theorem located; no later source-matching proof of Schramm Problem 2.1 was located in the bounded search. A bounded negative search is not a worldwide openness or novelty certificate.

The stale native title still names Beck--Fiala. That source was refreshed separately in section 10 below and is not restarted.

## 2. Metric and stuck trigger

The frozen R16 quantity remains

`epsilon_bridge` = the largest explicit exponent `epsilon>0` for which R16 has a complete proof, in the Krachun--Panagiotis critical hexagonal-lattice normalization, of

\[
B_T\le C_\varepsilon T^{-\varepsilon}\qquad\forall T\in\mathbb N
\]

with an explicit finite `C_epsilon`.

Before this run:

\[
\varepsilon_{\rm bridge}=\frac1{14,469,504}.
\]

After this run:

\[
\boxed{\varepsilon_{\rm bridge}=\frac1{14,469,504}.}
\]

There is **no movement**. The supported unchanged count is therefore `3`, so the owner's Section-I protocol triggers **STUCK_RECOVERY_1**. This report is a thinking/recovery report: the finite computation below is diagnostic evidence about a proposed route, not a replacement metric and not a source-level theorem.

## 3. (a) Exact blocking statement

The preceding runs show that vertical bridge decay and renewal sparsity alone do not control the lateral geometry needed for an Aizenman--Burchard/RSW-type compactness argument. The phase-only route cannot control the positive trivial sector, while the `n -> 0` loop-defect derivative supplies positivity but no gluing inequality.

The clean finite-domain blocker selected for this recovery is a four-terminal gluing estimate. For a finite planar domain with four cyclic boundary terminals `a,b,c,d`, let

\[
S_{uv}(x)=\sum_{\gamma:u\to v\;\mathrm{SAW}}x^{|\gamma|}.
\]

The simplest still-unproved form is

\[
\boxed{
S_{ac}(x_c)S_{bd}(x_c)
\;\le\;
C_0\Bigl(S_{ab}(x_c)S_{cd}(x_c)+S_{ad}(x_c)S_{bc}(x_c)\Bigr)
}
\tag{BLOCK}
\]

with a constant `C_0` uniform in the domain and scale; the ideal first target is `C_0=1`. Here `x_c=1/\sqrt{2+\sqrt2}` is the honeycomb critical step weight. The point of (BLOCK) is not that it is already known equivalent to Schramm Problem 2.1. It is a concrete positive-sector gluing estimate which, if robust under concatenation and annular decomposition, could supply the missing multi-crossing control.

A proof must survive multiple intersections of two SAWs. The naive operation "take the first intersection and swap tails" is not closed in the class of self-avoiding paths: a switched path can revisit a vertex when the two original paths intersect more than once.

## 4. (b) Routes tried and the precise reason each failed

### Route A — optimize the Krachun--Panagiotis bridge recurrence

This route produced real metric movement over several R16 runs, ultimately

\[
B_T\le1000T^{-1/14,469,504}.
\]

A later parametric analysis showed the one-threshold/block architecture is already close to its own internal ceiling. More importantly, even a much larger bridge exponent would remain predominantly vertical information. It does not by itself stop one irreducible bridge from making many macroscopic horizontal excursions.

**Failure:** wrong observable for compactness. Vertical bridge mass is not an annulus-crossing estimate.

### Route B — renewal-height conversion

The bridge bound gives nontrivial control of the renewal heights of irreducible bridges and an exact dictionary with the conjectural stable-`3/4` SLE bridge process.

**Failure:** renewal heights do not control the shape between renewal levels. A single irreducible bridge may be laterally wild.

### Route C — phase-resolved transfer operator / parafermionic Fourier sectors

At spin `5/8`, the winding phases form a `Z/48Z` sector decomposition. The previous finite no-go theorem shows that even all 47 nontrivial Fourier sectors cannot upper-bound the positive `k=0` mass: adding a uniform phase component changes the trivial mode while leaving every nontrivial mode fixed.

**Failure:** nontrivial winding data are information-theoretically blind to the positive invariant component.

### Route D — `n -> 0` two-defect O(n) deformation

The preceding report recovered the exact identity

\[
-\partial_n\log\frac{Z^{a,b}(n,x)}{Z^\varnothing(n,x)}\Big|_{n=0}
=
\mathbb E_{\mathrm{SAW}_{a,b,x}}
\sum_{C:C\cap\gamma\ne\varnothing}x^{|C|},
\]

which is a positive geometric `k=0` observable and even controls expected path length on a honeycomb cylinder.

**Failure:** the known O(n) box-crossing proof uses FKG/positive association in its `n>=1` regime. That lattice-condition route cannot simply be continued to `n=0`; a fixed local multiplicative FKG defect tensorizes to zero over repeated blocks.

### Route E — same-length deterministic path switching (this run)

The most obvious replacement for FKG is an exact switching injection: take a pair of opposite-connectivity SAWs `(a-c,b-d)` and map it to one of the adjacent connectivities `(a-b,c-d)` or `(a-d,b-c)` while preserving total length. If such a universal injection existed, it would imply the coefficientwise strengthening of (BLOCK).

**Failure:** the exact finite obstruction in section 6 proves this is false, even on a tiny planar subcubic graph with cyclic pendant terminals. The obstruction is specifically to **same-total-length / coefficientwise** switching. It does not refute weighted gluing at `0<x<=1`, because shortening can compensate for lost configurations.

## 5. (c) What a successful proof must contain that none of these routes contains

The new computation isolates a sharper requirement. A successful deterministic gluing proof cannot be a pure tail-swap involution inside fixed total length. It needs at least one of:

1. **loop erasure / shortening:** switching is allowed to create a walk, then remove loops, so the image has no greater total length; since `0<x_c<1`, shortening increases its critical weight;
2. **controlled multiplicity:** erased loops or collision data must be encoded well enough that the many-to-one map has a scale-uniform preimage bound;
3. **a positive defect-sector identity:** an algebraic relation must couple the trivial positive sector directly, rather than deducing it from nontrivial winding modes;
4. **a scale-stable switching law:** the constant loss must remain bounded (or summably close to one) under annular iteration. A constant that grows exponentially with the number of scales is useless for the target.

This is exactly what the nearest solved switching frameworks possess and ordinary SAW currently lacks.

## 6. Methods #8, #10, #26 — exact finite obstruction

### #8 GO THE OTHER WAY AND DISCRETIZE

I reduced the switching question to an exact finite path-enumeration problem. Consider the planar subcubic graph on vertices `0,...,6` with edges

\[
01,04,12,23,25,36,45,56.
\]

An explicit planar face certificate is

- outer face `0-4-5-6-3-2-1-0`,
- inner face `0-1-2-5-4-0`,
- inner face `2-3-6-5-2`.

Attach pendant terminals

\[
a\to0,\qquad b\to4,\qquad c\to6,\qquad d\to3,
\]

so `a,b,c,d` occur cyclically on the outer face.

Exact DFS enumeration gives

\[
\begin{aligned}
S_{ab}&=x^3+x^6+x^8,\\
S_{ac}&=x^5+2x^6+x^7,\\
S_{ad}&=x^5+2x^6+x^7,\\
S_{bc}&=x^4+x^6+2x^7,\\
S_{bd}&=2x^5+x^6+x^8,\\
S_{cd}&=x^3+x^5+x^8.
\end{aligned}
\]

Hence

\[
S_{ac}S_{bd}
=2x^{10}+5x^{11}+4x^{12}+2x^{13}+2x^{14}+x^{15},
\]

whereas

\[
S_{ab}S_{cd}+S_{ad}S_{bc}
=x^6+x^8+2x^9+2x^{10}+5x^{11}+4x^{12}+6x^{13}+3x^{14}+x^{16}.
\]

In particular,

\[
\boxed{[x^{15}]S_{ac}S_{bd}=1,
\qquad
[x^{15}](S_{ab}S_{cd}+S_{ad}S_{bc})=0.}
\tag{6.1}
\]

Therefore there is no universal injection from opposite-pair SAW pairs to adjacent-pair SAW pairs that preserves total path length.

The unique total-length-15 source pair is

\[
(a,0,4,5,2,3,6,c),
\qquad
(b,4,0,1,2,5,6,3,d).
\]

### #10 DERANDOMIZE

The failed injection tells us how to alter the algorithmic proof attempt: permit tail switching followed by chronological loop erasure, rather than insisting that the switched objects already remain SAWs. This is structurally analogous to Fomin's loop-erased switching mechanism for walk matrices.

The important accounting direction at critical SAW weight is favorable. For `0<x_c<1`, if loop erasure shortens total length from `L` to `L'<=L`, then

\[
x_c^L\le x_c^{L'}.
\]

Thus the remaining issue is not loss of weight per image; it is **multiplicity / reconstruction of the erased information**.

### #26 HUNT THE SPORADIC CASE

The 7-vertex graph above is a concrete sporadic obstruction to the strongest same-length switching formulation. I do **not** claim it is the smallest possible obstruction: the bounded small-graph exploration was designed to find a witness, not to certify global minimality over every planar embedding/domain convention.

Also importantly, this witness does **not** refute the weighted `C_0=1` inequality on `0<=x<=1`. Indeed

\[
\begin{aligned}
& S_{ab}S_{cd}+S_{ad}S_{bc}-S_{ac}S_{bd}\\
&\qquad=x^6+x^8+2x^9+4x^{13}+x^{14}-x^{15}+x^{16}\\
&\qquad=x^6+x^8+2x^9+4x^{13}+x^{14}(1-x)+x^{16}\ge0.
\end{aligned}
\tag{6.2}
\]

So the finite search points toward **shortening-aware switching**, not away from weighted gluing altogether.

The exact checker is

`artifacts/R16/2026-09-17T14-57-00Z_i0036_switching_length_obstruction.py`

and its archived executed output is

`artifacts/R16/2026-09-17T14-57-00Z_i0036_switching_length_obstruction.out`.

It verifies the planar face certificate, the six path polynomials, both product polynomials, the unique length-15 source pair, and ends

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check** of a finite obstruction, not an independent audit of I0036.

## 7. (d) Simplest special case still unproved

The clean next special case is deliberately weaker than a full RSW theorem:

> For every finite simply connected honeycomb domain with four pendant boundary terminals `a,b,c,d` in cyclic order, prove at critical weight `x_c` that
> \[
> S_{ac}(x_c)S_{bd}(x_c)
> \le
> S_{ab}(x_c)S_{cd}(x_c)+S_{ad}(x_c)S_{bc}(x_c).
> \tag{SIMPLE}
> \]

The finite witness above shows that one cannot prove (SIMPLE) via a total-length-preserving injection. It leaves open a weight-nonincreasing Fomin-style map in which switching may create loops and loop erasure shortens the image.

Even (SIMPLE) would still need a separate scale-iteration argument before it could imply the annulus multi-crossing bounds relevant to Schramm Problem 2.1. It is selected because it isolates the exact positivity/gluing mechanism missing from all current R16 routes.

## 8. (e) Nearest solved problems and what their proofs have that SAW lacks

### Fomin loop-erased switching / planar walk matrices

Fomin's identity supplies a modified reflection/switching principle for general weighted walks: loop erasure is built into the nonintersection event, and determinants of walk/hitting matrices acquire positive planar interpretations. Modern expositions emphasize that this mechanism is a loop-erased replacement for the ordinary reflection principle.

**Ingredient absent here:** ordinary SAW gives equal critical step weight to each self-avoiding path, not the push-forward measure obtained by summing all random-walk preimages under loop erasure. A Fomin-style operation can shorten a switched pair, but R16 still lacks a bounded-multiplicity reconstruction compatible with the SAW weights.

### Planar Ising / random-current total positivity

The planar Ising analogue obtains total positivity through the random-current representation and its switching structure. Again, the crucial input is not planarity alone; it is an algebraically closed enlarged configuration space in which source switching is exact and positivity survives projection to the two-point function.

**Ingredient absent here:** there is no known SAW current representation with a source-switching lemma that preserves or uniformly controls the critical path weights.

### Loop O(n), n>=1 box crossing

The nearest statistical-mechanics gluing result for the loop O(n) model uses FKG/positive association plus domain gluing and the parafermionic observable to obtain box-crossing information in its positive-association regime.

**Ingredient absent here:** the `n=0` SAW limit lies past the FKG threshold used by that proof. The previous R16 tensorization obstruction rules out repairing a fixed local FKG defect merely by inserting a domain-independent multiplicative slack.

These comparisons make the recovery choice substantially sharper: the missing object is not another scalar critical exponent but an **enlarged switching space with controlled projection back to SAWs**.

## 9. Exactly one recovery selected

Per the hard-task stuck protocol, I select exactly one recovery:

\[
\boxed{\textbf{PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.}}
\]

Specifically: port **Fomin-style loop-erased switching** to the two-defect critical SAW sector, allowing path shortening and carrying enough erased-loop data to bound preimage multiplicity. The first target is (SIMPLE), not the full scaling limit.

The next and final previously unused I0036 method triple is:

- **#7 TAKE THE LIMIT:** formulate the finite-domain switching inequality so that exhaustion to a strip/half-plane has monotone or tight limits;
- **#9 RANDOMIZE:** randomize the choice of switching intersection / erased-loop representative to seek an average bounded-preimage estimate when deterministic injectivity fails;
- **#19 MAKE IT AN ALGORITHM:** write an explicit Fomin-inspired switching-and-erasure procedure and identify exactly which reconstruction datum controls multiplicity.

These three numbers have not previously been used on I0036. After that run all thirty section-B moves will have been exercised at least once on this target.

This is **STUCK_RECOVERY_1**, not recovery 2. The hard two-recovery limit is preserved. A future second stuck episode may use one final recovery; a third requires handoff/rotation.

## 10. Beck--Fiala source refresh

The stale native task title is not a reason to discard current R16 continuity. The source/status refresh on 2026-09-17 gives:

- Bansal--Jiang, arXiv:2508.03961v2 (revised 9 September 2025), prove the Beck--Fiala `O(sqrt(t))` order for `t >= log^2 n`, give a weaker `~O(sqrt(t)+sqrt(log n))` bound in the smaller-`t` regime, and provide polynomial-time algorithms. This does **not** by itself settle all `t,n`.
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted **10 September 2026**, explicitly state a dimension-free Boolean Komlos bound `3 sqrt(2 pi)` and deduce for every integer `t>=1`
  \[
  \operatorname{disc}(A)<3\sqrt{2\pi t},
  \]
  with no `n` restriction. The repository also contains an independent R12 audit marked PASS for that external theorem package.

Operational label retained: **very recent primary-preprint resolution claim, internally audited; not mature external consensus**. Accordingly, R16 does not restart Beck--Fiala from the stale title unless the source status materially changes.

## 11. Model / scheduler control status

The limitation remains exactly what the controlling repository policy states. The exposed scheduler mutation surface provides task title/prompt, schedule or relative start, timing mode, enablement, and task identity. It exposes **no model-family selector and no reasoning-effort selector**, and gives no authenticated telemetry proving applied reasoning effort or an hour-long execution. GPT-6/maximum can therefore be requested in prompt text only in this environment.

`RESULTS.md` records that a later authorized P/C context successfully updated P26, while another context historically returned `You cannot modify this task`; the same ledger records broad R-series edit denials in that latter context. The compliant workaround for any permission-denied task is to use the owner/workspace context that actually owns the task or platform support. Repository edits do not constitute a native scheduler repair, and permission bypass / duplicate scheduling is prohibited.

No scheduler state was changed in this run, as required by the current R16 deployment instruction.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  lane: HARD_OUTSIDE
  target: I0036
  source: Schramm ICM 2006 Problem 2.1
  metric: epsilon_bridge
  before: 1/14469504
  after: 1/14469504
  constant: 1000
  movement: no
  supported_unchanged_count_before: 2
  supported_unchanged_count_after: 3
  stuck_state: STUCK_RECOVERY_1
  source_status: OPEN
  result_status: PARTIAL
  methods_used: [8, 10, 26]
  diagnostic_finite_obstruction:
    statement: same-total-length four-terminal SAW switching injection fails on an explicit planar subcubic graph
    source_level_progress: false
    exact_checker: artifacts/R16/2026-09-17T14-57-00Z_i0036_switching_length_obstruction.py
    exact_output: artifacts/R16/2026-09-17T14-57-00Z_i0036_switching_length_obstruction.out
  recovery_choice: port_Fomin_loop_erased_switching
  simplest_unproved_special_case: critical_weight_four_terminal_Ptolemy_C0_1
  next_methods: [7, 9, 19]
  audits:
    p26_end_to_end: missing
    second_other_track_end_to_end: missing
  closure: false
```

No shared root ledger, peer-track file, email, Drive content, public post, purchase, permission, workflow, or scheduler state was modified. The two artifact files and this immutable R16 report are the only repository writes for the run.
