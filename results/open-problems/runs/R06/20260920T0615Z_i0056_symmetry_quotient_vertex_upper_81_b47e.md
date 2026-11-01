Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FROZEN I0056 METRIC NO MOVEMENT / SOURCE-CLAUSE BOUND MOVEMENT: `H_{5,5}` width `0 -> 0`; for the source-valid tetrapentagonal graph `T=r{4,5}`, the rigorous vertex upper bound improves `116990/147339 -> 384566/484385`, shrinking the certified secondary interval width `0.2859198212533609 -> 0.28582690563954605`; methods #10 DERANDOMIZE, #4 PROVE SOMETHING WEAKER COMPLETELY, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.**

# R06 / I0056 — symmetry-quotient closure and a new exact tetrapentagonal vertex witness

Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: R06.  
Outside source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20; intake `I0056`.  
Overall source status after this run: **PARTIAL**.

## 1. Source, normalization, continuity

The current online Lyons–Peres edition still asks:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The normalization retained throughout R06 is the outer vertex boundary

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_V K|}{|K|},\qquad
\partial_VK=N[K]\setminus K.
\]

The frozen regular/co-regular pair remains

\[
H_{5,5}=\{5,5\},\qquad (d,f)=(5,5),
\]

with the already proved/audited/posted value

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

Thus the frozen metric has no numerical room to improve. Full Question 6.20 is nevertheless still PARTIAL because its second, more-general transitive-plane-graph clause remains unresolved.

I continued from the newest useful R06 checkpoint

`runs/R06/20260920T0505Z_i0056_multilayer_vertex_closure_80_71b6.md`,

which concerns the source-valid 4-regular vertex-transitive tetrapentagonal plane graph

\[
T=r\{4,5\}=M(\{4,5\}),
\]

of cyclic face type `[4,5,4,5]`. The inherited rigorous interval was

\[
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(T)
\le \frac{116990}{147339}.
\tag{1.1}
\]

The previous exact finite witness had `|K|=147339`, `|partial_V K|=116990`.

Haslegrave–Panagiotis, DOI `10.1002/rsa.20946`, remain excluded prior art. Their article explicitly establishes the vertex-isoperimetric constants for triangular and square hyperbolic lattices, equivalently the regular codegree `3` and `4` cases of Question 6.20. Nothing in this report relabels those cases.

## 2. Current source/literature check — 20 September 2026

I rechecked the current Lyons–Peres online edition and the Haslegrave–Panagiotis article, and ran bounded searches for `tetrapentagonal vertex isoperimetric constant`, `r{4,5} vertex boundary`, `[4,5,4,5] isoperimetric`, later work and citing papers. I recovered no primary source giving the exact outer-vertex constant of the mixed-face tetrapentagonal graph or the finite witness below. This is **bounded negative evidence only**; novelty/priority remains **UNVERIFIED**.

The regular triangular/quadrangular cases stay excluded. Adjacent edge/perimeter results for regular hyperbolic tilings do not by themselves answer this mixed-face outer-vertex problem.

## 3. Idea before code and the three new moves

The idea was written before the new certificate at

`artifacts/R06/20260920T0531Z_i0056_symmetry_quotient_idea_81_b47e.md`

(created at commit `01d0472c41dd7132b7bd765238c81ecc0c7363f3`).

### #10 — DERANDOMIZE

The previous max-closure solver produced a large non-round set. Rather than treat the solver output as an opaque object, use the finite root stabilizer of the exact Coxeter realization to force an equally good symmetric optimizer and encode the resulting witness by exact group words.

### #4 — PROVE SOMETHING WEAKER, COMPLETELY

Before looking for an all-radius extremal shape, prove a finite-group symmetry theorem for the exact boundary functional. This is a complete lemma and removes a factor-four amount of finite search without changing the optimum in that search problem.

### #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

Compare the symmetry-orbit layers with the already proved all-radius `A/B/C` frontier anatomy and shell recurrence, looking for a propagating boundary state rather than fitting another raw radial sequence. The finite experiments suggest a short outer transition zone, but I do **not** promote that observation to an all-radius theorem here.

## 4. New theorem: finite-group symmetry reduction is exact

For a fixed finite automorphism-invariant search region and real/rational `r`, put

\[
F_r(K)=(1+r)|K|-|N[K]|.
\tag{4.1}
\]

### Lemma R06-I0056-SYMMETRY-81

Let `H` be a finite group of graph automorphisms preserving the finite search problem. Then `F_r` has an `H`-invariant maximizer.

### Proof

The closed-neighborhood map obeys

\[
N[K\cup L]=N[K]\cup N[L],
\qquad
N[K\cap L]\subseteq N[K]\cap N[L].
\]

Therefore closed-neighborhood cardinality is submodular:

\[
|N[K\cup L]|+|N[K\cap L]|
\le |N[K]|+|N[L]|.
\tag{4.2}
\]

Since cardinality of `K` is modular, (4.1) is supermodular:

\[
F_r(K\cup L)+F_r(K\cap L)
\ge F_r(K)+F_r(L).
\tag{4.3}
\]

If `K,L` are both maximizers with value `M`, neither term on the left of (4.3) can exceed `M`, so both must equal `M`. Thus unions and intersections of maximizers are again maximizers.

Take any maximizer `K`. Every translate `hK`, `h in H`, is also a maximizer. Repeatedly taking unions gives

\[
K_H:=\bigcup_{h\in H}hK,
\]

which is again a maximizer and is `H`-invariant. QED.

For the exact `[4,5]` Coxeter model used by R06, the root midpoint is fixed by the commuting reflections `s_1,s_3`; hence

\[
H=\langle s_1,s_3\rangle\cong C_2\times C_2,
\qquad |H|=4.
\]

Consequently the maximum-closure problem can be solved exactly on `H`-orbits with orbit-cardinality weights. This is not a sampled restriction: Lemma 81 proves that the finite optimum is preserved.

## 5. Exact non-round witness

The quotient search used selectable vertices through graph distance `20` and complete coverage through graph distance `21`. At the rational test value

\[
r=\frac{497}{626},
\]

the closure objective is equivalently

\[
1123|K|-626|N[K]|
=497|K|-626|\partial_VK|.
\tag{5.1}
\]

The quotient optimum has positive surplus `1029`; an exact selected-set certificate was then reconstructed independently in the full Coxeter graph rather than trusting the cut representation.

The certified set satisfies

\[
|K|=484385,
\qquad
|N[K]|=868951,
\qquad
|\partial_VK|=384566.
\]

Indeed

\[
1123(484385)-626(868951)=1029>0.
\]

Therefore, directly from a finite set in the infinite graph,

\[
\boxed{
\Phi_V(T)\le \frac{384566}{484385}
=0.7939263189405122\ldots
}.
\tag{5.2}
\]

This is strictly better than the preceding exact upper bound because

\[
116990\cdot484385-384566\cdot147339
=6,631,276>0.
\tag{5.3}
\]

The certificate is compact but exact: it contains `121103` canonical `H`-orbit representatives as generator words of length at most `20`, front-coded and LZMA-compressed. The checker replays every word in the exact ring

\[
\mathbb Z[a,b],\qquad a^2=2,\quad b^2=b+1,
\]

verifies canonical root-stabilizer representatives, expands the full `H`-orbits, reconstructs `N[K]` by the four exact graph generators, and checks (5.2)–(5.3). No floating-point geometry is used.

Artifacts:

- checker: `artifacts/R06/20260920T0610Z_i0056_symmetry_quotient_word_exact_81_b47e.py`;
- executed output: `artifacts/R06/20260920T0610Z_i0056_symmetry_quotient_word_exact_81_b47e.out`.

The archived output ends `ALL_EXACT_CHECKS_PASS` and records the certificate SHA-256

`352c7fdcb60542e932ea0e976db8432e9f05b5d37356d2ceb22018cee14d0063`.

## 6. Quantitative movement

Combining (5.2) with the inherited rigorous lower bound gives

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(r\{4,5\})
\le \frac{384566}{484385}.
}
\tag{6.1}
\]

Numerically,

\[
0.5080994133009662\ldots
\le \Phi_V(r\{4,5\})
\le 0.7939263189405122\ldots .
\]

Thus the rigorous source-clause interval width moves

\[
0.2859198212533609
\longrightarrow
\boxed{0.28582690563954605}.
\]

This is a small numerical improvement compared with the preceding run, but it comes with a useful exact symmetry reduction and a compact fully reconstructible witness.

The **frozen requested metric remains `0 -> 0`** for `H_{5,5}`. The full source question remains **PARTIAL**.

## 7. What the finite optimizer teaches, without overclaiming

At nearby rational thresholds and successive finite radii, symmetry-quotient optimizers repeatedly contain a large full inner ball and only a short partially occupied outer transition region. This is evidence for a propagating non-round boundary profile, but it is **not** a theorem: no all-radius state rule is claimed from these finite computations.

The important change in strategy is that the optimizer is now no longer opaque. It is an exact union of root-stabilizer orbits, and the earlier R06 run already proved that every graph-distance frontier vertex has one of the three all-radius types

\[
A=(1,0,3),\qquad B=(1,1,2),\qquad C=(2,0,2).
\]

The next substantive attack should combine these two finite structures: classify selected/unselected states on `A,B,C` together with the angular/root-stabilizer state, and either derive a finite substitution/transfer rule for the non-round contour or prove that no such stationary rule can propagate. In parallel, the min-cut dual suggests a lower-bound route: construct a source-valid fractional covering/flow certificate for **all** finite sets rather than only inside a finite ball. That is the step needed to move the lower endpoint, not another larger sample.

## 8. Model/control truth

The model-control limitation is still unchanged. The exposed scheduling/task surface provides task identity/title, prompt, schedule/timing mode and enabled-state controls, but no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long runtime control, and no authenticated per-run applied-model/effort receipt. Thus `GPT-6 / maximum` remains a prompt request on this surface, not an enforceable setting.

Making it enforceable would require an owner-authorized product/backend/API schema that exposes, persists and attests the model family and reasoning effort. The historical P26 `You cannot modify this task` event was authorization-context-specific; later authorized context succeeded. The compliant workaround is the owning/authorized context or platform-side permission repair, not a permission bypass. No scheduler or permission change was attempted in this run.

```yaml
ledger_delta:
  worker: R06
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  full_source_status: PARTIAL
  frozen_target:
    graph: "H_{5,5}={5,5}"
    parameters: "degree=5, face_degree=5"
    normalization: "outer vertex boundary Phi_V"
    metric: "rigorous certified interval width U-L"
    before: 0
    after: 0
    movement: "no movement; mathematical minimum already attained"
    status: "PROVED/audited/posted subclass; full source still PARTIAL"
    stagnation: "preserve chronological zero-width history; not reset by secondary progress"
  source_clause_progress:
    graph: "T=r{4,5}, 4-regular transitive tetrapentagonal plane graph, vertex type [4,5,4,5]"
    quantity: "Phi_V(T)"
    lower_before: "1/(sqrt(3)+sqrt(5)-2)"
    lower_after: "1/(sqrt(3)+sqrt(5)-2)"
    upper_before: "116990/147339"
    upper_after: "384566/484385"
    interval_width_before: 0.2859198212533609
    interval_width_after: 0.28582690563954605
    status: "PROVED PARTIAL / exact finite self-check; no new outside audit yet"
  tried_moves: [10, 4, 17]
  remaining_obligation: "determine exact Phi_V(T) or obtain a stronger source-valid lower bound; then continue the full more-general transitive-plane-graph clause"
  evidence:
    idea: "artifacts/R06/20260920T0531Z_i0056_symmetry_quotient_idea_81_b47e.md"
    checker: "artifacts/R06/20260920T0610Z_i0056_symmetry_quotient_word_exact_81_b47e.py"
    checker_output: "artifacts/R06/20260920T0610Z_i0056_symmetry_quotient_word_exact_81_b47e.out"
    checker_verdict: "ALL_EXACT_CHECKS_PASS"
    predecessor: "runs/R06/20260920T0505Z_i0056_multilayer_vertex_closure_80_71b6.md"
  audits:
    new_symmetry_quotient_bound: "self-check only; independent audit not yet obtained"
    frozen_H55: "existing R05/P26 mathematical passes retained"
```
