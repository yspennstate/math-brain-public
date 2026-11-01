Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FROZEN I0056 METRIC NO MOVEMENT / SOURCE-CLAUSE VERTEX-INTERVAL MOVEMENT: `H_{5,5}` width `0 -> 0`; for `T=r{4,5}`, the rigorous vertex interval width improves `0.28582690563954604 -> 0.12009883937293475` via the new lower bound `2/(sqrt(3)+sqrt(5)-1)`; Section-B history check found no honest unused method number left, so the genuinely new staged-closure attack is described under reused labels #5, #26, #27 rather than falsely calling them fresh.**

# R06 / I0056 — multiplicity-three preclosure gives a substantially stronger tetrapentagonal vertex lower bound

Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: R06.  
Outside source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20; intake `I0056`.  
Overall source status after this run: **PARTIAL**.

## 1. Exact source, normalization, and repository continuity

The current Lyons--Peres edition still asks:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The frozen normalization remains

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_VK|}{|K|},
\qquad
\partial_VK=N[K]\setminus K.
\]

The frozen regular/co-regular pair is still

\[
H_{5,5}=\{5,5\},\qquad (d,f)=(5,5),
\]

with the already proved, audited, and posted exact value

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},
\qquad [L,U]=[\sqrt5,\sqrt5],
\qquad U-L=0.
\]

Thus the literal frozen metric has no numerical room to move. Full Question 6.20 remains **PARTIAL** because the second clause, concerning more general transitive plane graphs, is not settled.

At run start I reread/rechecked the required campaign surfaces on current `master`: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the I0056 ownership record, the newest R06 report, neighboring R-series state, and targeted intake/source records. I0056 remains owned by R06. I did not edit a shared root or another track.

The immediate predecessor is

`runs/R06/20260920T0820Z_i0056_edge_candidate_refutation_82_d2c8.md`.

That run refuted the old auxiliary edge candidate `Phi_E(T)=2/sqrt(5)` and left the strongest source-valid mixed-face bounds at

\[
\frac4{1+\sqrt3+\sqrt5}
\le \Phi_E(T)
\le \frac{130232}{154055}
\tag{1.1}
\]

and

\[
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(T)
\le \frac{384566}{484385},
\tag{1.2}
\]

where

\[
T=r\{4,5\}=M(H_{5,4})
\]

is the 4-regular vertex-transitive tetrapentagonal plane graph with cyclic face type `[4,5,4,5]`.

The upper endpoint in (1.2) is the exact finite witness from

`runs/R06/20260920T0615Z_i0056_symmetry_quotient_vertex_upper_81_b47e.md`.

## 2. Prior-art/source check — 20 September 2026

The official current Lyons--Peres PDF indexed on 20 September 2026 still returns the exact Question 6.20 wording above. The browser PDF renderer could not ingest the whole current PDF because of its size, so I do not claim a new page-screenshot audit; the exact text was recovered from the official indexed source and cross-checked against the repository's source record.

Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, explicitly establish the vertex-isoperimetric constants for triangular and square hyperbolic lattices, i.e. the regular codegree-3 and codegree-4 cases. Those cases remain **KNOWN prior art and excluded**. Nothing here relabels them.

Dated searches in this run included:

- `"Question 6.20" "Probability on Trees and Networks" vertex isoperimetric`;
- `"tetrapentagonal" "vertex isoperimetric"`;
- `"r{4,5}" isoperimetric`;
- `[4,5,4,5] Cheeger`;
- `"h/(2-h)" graph vertex isoperimetric edge isoperimetric`;
- `edge isoperimetric vertex isoperimetric regular graph relation`;
- Mohar / magnifying-number / outer-vertex-expansion variants;
- later Haslegrave--Panagiotis and citing-paper searches.

I found standard comparisons such as `h_out <= h_E <= d h_out` and specialized random-regular/finite-graph isoperimetry, but no primary source in the bounded search stating the exact staged-closure inequality proved below, nor an exact `Phi_V(r{4,5})`. This is **bounded negative evidence only**. The closure mechanism may be folklore; novelty/priority is **UNVERIFIED**.

Recent regular-hyperbolic-tiling work found in the search concerns regular `{p,q}` tilings, not the mixed-face tetrapentagonal graph, so it does not settle (1.2).

## 3. Idea before validation and method-history correction

Before writing the proof checker I recorded the route in

`artifacts/R06/20260920T0920Z_i0056_threeclosure_vertex_lower_idea_83_4f8c.md`

at commit `d2cd22322842077d959dda18d12a018bac0dc418`.

The mathematical idea is to split the old multiplicity-two closure into **two thresholds**. First absorb only boundary vertices having at least three selected neighbors; these vertices are favorable for *both* edge and vertex boundary. Only afterwards perform the multiplicity-two closure.

The initial idea note labeled this with #5, #26, #27. A repository-history check after writing the note found that all three labels had already appeared in earlier I0056 work: #5 and #26 in the multilayer/frontier optimization work and #27 in the earlier dual-Euler run. Wider R06/I0056 history supplies examples covering the rest of the numbered palette as well. Therefore there is no honest way to satisfy the literal “three never-before-tried numbers” requirement without inventing history.

I do **not** call #5/#26/#27 fresh. They are retained below only as descriptive lenses for a genuinely new argument, and they do not repeat the immediately preceding triple `#22/#6/#9`.

- **#5 ADD A PARAMETER:** separate multiplicity threshold 3 from threshold 2 instead of using one closure rule.
- **#26 HUNT THE SPORADIC CASE:** the exceptional multiplicity-3/4 boundary vertices are not an obstruction; they are exactly the vertices that can be swallowed without increasing outer boundary.
- **#27 SWAP THE QUANTIFIERS:** first prove an abstract edge-to-outer-vertex conversion for every finite set in every infinite graph of maximum degree 4, then substitute the tetrapentagonal edge inequality.

The work below is theorem-first; the small exact checker only validates the resulting algebra and interval movement.

## 4. New theorem — staged closure in maximum degree four

### Theorem R06-I0056-3CLOSURE-VERTEX-83

Let `G` be an infinite graph of maximum degree at most 4. Suppose there is a constant `h` with

\[
0<h<1
\]

such that every finite nonempty vertex set `S` satisfies

\[
|\partial_E S|\ge h|S|.
\tag{4.1}
\]

Then

\[
\boxed{
\Phi_V(G)\ge \frac{h}{2-h}.
}
\tag{4.2}
\]

Here `partial_V S=N[S]\setminus S` is the outer vertex boundary.

### Proof

Fix an arbitrary finite nonempty set `S`.

#### Stage I: multiplicity-three preclosure

While there is a vertex `x` outside the current set with at least three neighbors in the set, adjoin `x`. If `r>=3` is the number of its selected neighbors and `d(x)<=4`, then the edge boundary changes by

\[
\Delta |\partial_E|=d(x)-2r\le 4-2r\le-2.
\tag{4.3}
\]

Thus this first stage terminates after finitely many steps.

For the outer vertex boundary, `x` itself was in the boundary before it was added. Afterwards it can create at most `d(x)-r` new outside boundary vertices. Hence

\[
\Delta |\partial_V|
\le (d(x)-r)-1
\le 3-r
\le0.
\tag{4.4}
\]

Let `A` be the finite set at the end of Stage I, and write

\[
n:=|A|,\qquad b:=|\partial_VA|,\qquad e_0:=|\partial_EA|.
\]

Every outside vertex now has at most two neighbors in `A`. Counting each crossing edge by its outside endpoint therefore gives

\[
\boxed{e_0\le2b.}
\tag{4.5}
\]

Moreover Stage I only enlarged the set and never increased its outer boundary. Consequently, a lower bound on `b/n` also applies to the original `S`.

#### Stage II: multiplicity-two closure

Starting from `A`, repeatedly adjoin an outside vertex having at least two neighbors in the current set. For an addition of multiplicity `r>=2`,

\[
\Delta|\partial_E|=d(x)-2r\le4-2r\le0.
\tag{4.6}
\]

This second stage must also terminate. Otherwise its finite intermediate sets would have cardinalities tending to infinity while their edge boundaries stayed at most `e_0`, contradicting (4.1).

Let

- `m_2` be the number of Stage-II additions performed when the chosen vertex had exactly two selected neighbors;
- `m_{>=3}` be the number performed at multiplicity at least three.

For a multiplicity-two addition, (4.4) gives

\[
\Delta|\partial_V|\le1,
\]

whereas for multiplicity at least three it gives

\[
\Delta|\partial_V|\le0.
\]

Let `C` be the terminal set and put

\[
E:=|\partial_EC|.
\]

At termination every outside boundary vertex has exactly one selected neighbor, so

\[
|\partial_VC|=|\partial_EC|=E.
\tag{4.7}
\]

Since only the `m_2` multiplicity-two additions could increase outer boundary,

\[
E\le b+m_2,
\qquad\text{hence}\qquad
b\ge E-m_2.
\tag{4.8}
\]

The edge boundary never increased during Stage II, so by (4.5),

\[
E\le e_0\le2b,
\qquad\text{hence}\qquad
b\ge\frac E2.
\tag{4.9}
\]

Finally apply the assumed edge expansion (4.1) to the terminal set:

\[
E
\ge h|C|
=h(n+m_2+m_{\ge3})
\ge h(n+m_2).
\tag{4.10}
\]

Combining (4.8)--(4.10) yields simultaneously

\[
b\ge h(n+m_2)-m_2
\tag{4.11}
\]

and

\[
b\ge\frac h2(n+m_2).
\tag{4.12}
\]

Set `t=m_2/n>=0`. Then

\[
\frac bn
\ge
\max\left\{
 h-(1-h)t,
 \frac h2(1+t)
\right\}.
\tag{4.13}
\]

Because `0<h<1`, the first affine function decreases in `t` and the second increases. Their intersection is at

\[
t_*=rac{h}{2-h},
\]

where their common value is exactly

\[
\frac{h}{2-h}.
\]

Thus

\[
\frac{|\partial_VA|}{|A|}=\frac bn\ge\frac{h}{2-h}.
\]

Stage I never increased boundary and only increased volume, so

\[
\frac{|\partial_VS|}{|S|}
\ge
\frac{|\partial_VA|}{|A|}
\ge
\frac{h}{2-h}.
\]

Since `S` was arbitrary, (4.2) follows. QED.

## 5. Apply the theorem to the tetrapentagonal graph

The previous R06 dual-Euler argument rigorously proves for `T=r{4,5}` that every finite nonempty set satisfies

\[
|\partial_E S|
\ge
h_0|S|,
\qquad
h_0:=\frac4{1+\sqrt3+\sqrt5}.
\tag{5.1}
\]

Here `0<h_0<1`. Applying Theorem 83 with `h=h_0` gives

\[
\Phi_V(T)
\ge
\frac{h_0}{2-h_0}.
\]

A direct simplification yields

\[
\boxed{
\Phi_V(r\{4,5\})
\ge
\frac2{\sqrt3+\sqrt5-1}
=0.673827479567577446\ldots .
}
\tag{5.2}
\]

This strictly improves the previous lower endpoint

\[
\frac1{\sqrt3+\sqrt5-2}
=0.508099413300966152\ldots .
\]

Indeed, writing `s=sqrt(3)+sqrt(5)`, the inequality

\[
\frac2{s-1}>\frac1{s-2}
\]

is equivalent to `s>3`, which is immediate.

Combine (5.2) with the existing exact finite upper witness:

\[
\boxed{
\frac2{\sqrt3+\sqrt5-1}
\le
\Phi_V(r\{4,5\})
\le
\frac{384566}{484385}.
}
\tag{5.3}
\]

Numerically,

\[
0.673827479567577446\ldots
\le
\Phi_V(r\{4,5\})
\le
0.793926318940512196\ldots .
\]

The certified source-clause vertex interval width therefore moves from

\[
0.285826905639546044\ldots
\]

to

\[
\boxed{0.120098839372934750\ldots}.
\]

This is an absolute reduction of about `0.1657280662666113`, i.e. a relative reduction of

\[
\boxed{57.9819684559751\%}.
\]

The frozen requested metric remains exactly `0 -> 0` for `H_{5,5}`; this is substantive movement on the still-open second source clause, not a relabeling of the frozen metric.

## 6. Exact algebra self-check

The theorem-sized claim is proved on the page above. I nevertheless added a small exact algebra/sign checker after the idea was written:

- checker: `artifacts/R06/20260920T0927Z_i0056_threeclosure_vertex_lower_exact_83_4f8c.py`;
- archived output: `artifacts/R06/20260920T0927Z_i0056_threeclosure_vertex_lower_exact_83_4f8c.out`.

It uses rational/integer comparisons for the sign obligations and decimals only for display. In particular it certifies the radical lower estimate

\[
\sqrt3+\sqrt5>\frac{58}{15}>3,
\]

verifies that the new endpoint exceeds the old one and remains below the existing exact upper witness, and prints the two interval widths. The archived output ends

`ALL_EXACT_SIGN_CHECKS_PASS`.

This is an **R06 self-check**, not an independent audit.

## 7. Status and next mathematical obstruction

The result of this run is therefore:

- **PROVED PARTIAL** for the mixed-face source clause;
- **not a closure of Question 6.20**;
- **not yet independently audited** by P26 or a second outside track;
- **novelty/priority UNVERIFIED**, with the generic staged-closure mechanism explicitly treated as possibly folklore.

The numerical gap for the vertex constant is now much smaller:

\[
0.67382748\ldots
\le\Phi_V(T)\le
0.79392632\ldots .
\]

The next useful attack should therefore avoid another larger finite ball. There are two concrete directions:

1. improve the edge lower endpoint in (1.1) and feed it through the monotone map `h -> h/(2-h)`;
2. exploit the already proved `A/B/C` frontier anatomy to obtain a tetrapentagonal-specific vertex-boundary inequality stronger than the generic maximum-degree-four conversion.

The second route is more likely to close the remaining `~0.1201` gap because the exact upper witnesses are highly non-round and the generic conversion deliberately throws away angular/face-type information.

## 8. Model/scheduler-control truth

The implementation limitation remains unchanged. The available scheduler surface exposes task identity/title, prompt, schedule/timing and enabled-state controls, but **no binding model-family selector, no binding reasoning-effort selector, no guaranteed hour-long execution setting, and no authenticated applied-model/effort receipt**. GPT-6/maximum therefore remains a prompt request on this surface.

The historical P26 `You cannot modify this task` response was an authorization-context boundary; the repository follow-up records later successful edits from an authorized context. The compliant workaround is the owning/authorized product/admin/API context or a platform permission/schema change, not a worker-side bypass. No scheduler or permission mutation was attempted in this run.

```yaml
ledger_delta:
  worker: R06
  actual_model: "GPT-5.6 Sol"
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  full_source_status:
    before: PARTIAL
    after: PARTIAL

  frozen_target:
    graph: "H_{5,5}={5,5}"
    class: "regular co-regular plane tessellation"
    parameters: "degree=5, face_degree=5"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    metric: "rigorously certified interval width U-L for Phi_V(H_{5,5})"
    before: 0
    after: 0
    interval: "[sqrt(5),sqrt(5)]"
    exact_value: "sqrt(5)"
    unchanged_count: UNKNOWN
    status: "PROVED/audited/posted subclass; full source PARTIAL"

  source_clause_vertex_progress:
    graph: "T=r{4,5}, 4-regular vertex-transitive tetrapentagonal plane graph, face type [4,5,4,5]"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    lower_before: "1/(sqrt(3)+sqrt(5)-2)"
    lower_after: "2/(sqrt(3)+sqrt(5)-1)"
    upper_before: "384566/484385"
    upper_after: "384566/484385"
    interval_width_before: 0.28582690563954604
    interval_width_after: 0.12009883937293475
    width_reduction_fraction: 0.579819684559751
    status: "PROVED PARTIAL / R06 full proof + exact algebra self-check / independent audit pending"

  theorem:
    id: "R06-I0056-3CLOSURE-VERTEX-83"
    statement: "If G is infinite with maximum degree at most 4 and |partial_E S| >= h|S| for every finite nonempty S, where 0<h<1, then Phi_V(G) >= h/(2-h)."
    novelty: "UNVERIFIED_POSSIBLY_FOLKLORE"

  method_history:
    immediately_preceding_triple: [22, 6, 9]
    descriptive_lenses_this_run: [5, 26, 27]
    fresh_number_claim: false
    reason: "repository history shows these labels were used earlier and the R06/I0056-era 30-move palette is exhausted; no false fresh labels were invented"

  remaining_obligation: "determine exact Phi_V(r{4,5}) or further close [2/(sqrt(3)+sqrt(5)-1), 384566/484385]; continue the full more-general transitive-plane-graph clause of Question 6.20"

  evidence:
    predecessor: "runs/R06/20260920T0820Z_i0056_edge_candidate_refutation_82_d2c8.md"
    idea_before_validation: "artifacts/R06/20260920T0920Z_i0056_threeclosure_vertex_lower_idea_83_4f8c.md @ d2cd22322842077d959dda18d12a018bac0dc418"
    checker: "artifacts/R06/20260920T0927Z_i0056_threeclosure_vertex_lower_exact_83_4f8c.py @ 1654fd6909db2194dd7e3f8a91de75be19ee6764"
    checker_output: "artifacts/R06/20260920T0927Z_i0056_threeclosure_vertex_lower_exact_83_4f8c.out @ 3e8a3d736b40bfbe62f855b48fdb1753e900e98c"
    checker_verdict: "ALL_EXACT_SIGN_CHECKS_PASS"
    prior_vertex_upper: "runs/R06/20260920T0615Z_i0056_symmetry_quotient_vertex_upper_81_b47e.md"
    edge_lower_source: "runs/R06/20260916T1922Z_i0056_medial_dual_euler_02.md"

  audits:
    theorem_83_external: NONE
    note: "older R05/P26 audits concern the regular/co-regular closure theorem, not this new staged-closure theorem"
```
