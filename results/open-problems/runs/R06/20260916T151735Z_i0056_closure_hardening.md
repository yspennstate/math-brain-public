Model: GPT-5.6 Sol. Reasoning: UNVERIFIED by runtime metadata; GPT-6 maximum was requested, but the scheduler exposes no model or reasoning selector, so I do not claim GPT-6 maximum.
Problem: Russell Lyons and Yuval Peres, *Probability on Trees and Networks* (2016; current paperback e-version 2026-08-19), Question 6.20; intake I0056. **No movement:** frozen metric width `0 -> 0`; overall source status `PARTIAL`; regular/co-regular branch `PROVED, audit-gated`; unchanged-count since the metric first reached zero = `1`.

Run ID: `20260916T151735Z_i0056_closure_hardening`
Repository: `yspennstate/math-open-problems`, branch `master`.

# 1. Repository recovery; no restart

I read the required campaign/root controls before continuing:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`;
- root `RESULTS.md`;
- root `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`;
- `operations/RFLEET_2026-09-16.md`;
- the exact intake row in `probability_1000_intake_I_20260914/problems.jsonl`;
- the canonical ownership file `operations/claims/I0056.md`;
- newest own R06 report
  `runs/R06/20260916T144133Z_i0056_edge_vertex_closure.md`;
- newest neighboring R05 report
  `runs/R05/20260916T141505Z_i0030_edge_mnhd_n8.md`;
- newest R07 report
  `runs/R07/2026-09-16T1425Z_kpz_weighted_overlap_02.md`.

The source intake row says Question 6.20 asks first for `Phi_V(G)` for regular,
co-regular plane graphs and then asks for both edge and vertex constants for
more general transitive plane graphs. It records the Haslegrave--Panagiotis
face-codegree `3` and `4` cases. The intake line itself displays the old
`alpha_d` expression with a minus sign; the R06 theorem below does not depend
on that convention.

The old R06 two-dimensional Anderson-localization assignment remains retired;
its preserved handoff was already recorded before I0056 was claimed. I did not
reopen or edit that personal research track.

The frozen pair remains
\[
H_{5,5},
\]
the regular pentagonal tessellation with vertex degree `d=5` and face
degree/codegree `f=5`. The certified interval was already collapsed in the
previous run:
\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},
\qquad
\boxed{\text{interval width}=0}.
\]
Since width cannot improve below zero, this run is closure hardening rather
than metric movement.

# 2. Recovered result; canonical proof remains the previous immutable report

The previous run proved `R06-I0056-CLOSURE-01`:

> Let `G` be an infinite simple `d`-regular graph. If
> \[
> \Phi_E(G)\ge d-3,
> \]
> then
> \[
> \Phi_V(G)=\Phi_E(G).
> \]

The complete written proof is preserved in
`runs/R06/20260916T144133Z_i0056_edge_vertex_closure.md`.
No new theorem is substituted for it in this run.

The mechanism is the multiplicity-two closure of a finite set. If
`v notin K` has `r=|N(v) cap K|>=2`, adjoining `v` changes the edge boundary
exactly by
\[
d-2r\le d-4
\]
and changes the outer vertex boundary by at most
\[
-1+(d-r)\le d-3.
\]
The edge-expansion hypothesis forces this closure to terminate; at termination
every outer boundary vertex has exactly one neighbour in the set, so simplicity
gives equality between outer-boundary vertices and crossing edges. Backward
bookkeeping yields `|partial_V K|>=Phi_E|K|` for the original arbitrary finite
set.

Combining this theorem with Oh's exact regular-tessellation edge constant
\[
\Phi_E(d,f)
=(d-2)\sqrt{1-\frac4{(d-2)(f-2)}}
\]
gave the regular/co-regular source branch
\[
\boxed{
\Phi_V(d,f)=
(d-2)\sqrt{1-\frac4{(d-2)(f-2)}}
\qquad(f\ge5),
}
\]
because for `d>=4`, `f>=5`,
\[
\Phi_E(d,f)^2-(d-3)^2
=
2d-5-\frac{4(d-2)}{f-2}
\ge\frac{2d-7}{3}>0,
\]
and for `d=3` the threshold is the trivial `Phi_E>=0=d-3`.

This is a resolution candidate for the *first* regular/co-regular clause of
Question 6.20 after combining it with Haslegrave--Panagiotis for face degrees
3 and 4. It does **not** solve the second clause asking for general transitive
plane graphs; the overall source problem therefore remains `PARTIAL`.

# 3. Fresh adversarial self-audit of the closure proof

This self-audit does **not** count toward either required independent closure
audit.

I checked every proof dependency again.

## 3.1 The boundary update is source-correct

For a simple `d`-regular graph, if `r>=2` neighbours of `v` lie in `K`, then
exactly `r` crossing edges disappear and `d-r` new crossing edges appear:
\[
e(K\cup\{v\})-e(K)=d-2r.
\]

For the **outer** vertex boundary used by Lyons--Peres, `v` itself disappears
from the old boundary. Every old boundary vertex other than `v` remains a
boundary vertex because `K` only grows, and at most the `d-r` outside
neighbours of `v` can become newly exposed. Hence
\[
b(K\cup\{v\})
\le b(K)-1+d-r.
\]
No inner-boundary convention is being substituted.

## 3.2 Termination really uses the infinite-graph definition

If `K_0` has size `n` and `m` vertices are added, then
\[
e_m\le dn+m(d-4)
\]
whereas the infinite-graph edge expansion gives
\[
e_m\ge h(n+m)
\]
for every finite `K_m`. Thus
\[
(h-d+4)m\le(d-h)n.
\]
Under `h>=d-3`, the left coefficient is at least one, so infinitely many
closure steps are impossible.

There is no finite-graph `|K|<=|V|/2` restriction in this argument. That
distinction is essential.

## 3.3 The terminal identity uses simplicity

At termination every outer boundary vertex has exactly one neighbour in the
closed set. In a simple graph this gives a bijection between crossing edges and
outer boundary vertices:
\[
b_m=e_m.
\]
The theorem is therefore deliberately stated for simple graphs. I did not
silently extend it to multigraphs.

The regular hyperbolic/Euclidean tessellation edge graphs in the cited
Lyons--Peres / Haslegrave--Panagiotis / Oh scope are the ordinary simple
tessellation graphs; nevertheless, this source-matching point is explicitly
included in the independent audit request.

## 3.4 The quadrangular case is an adversarial non-example

At `f=4`,
\[
\Phi_E(d,4)^2-(d-3)^2=-1.
\]
Thus the closure threshold does not apply. This is necessary: the known
quadrangular outer-vertex constants from Haslegrave--Panagiotis are not equal
to the edge constants. Hence the theorem is not accidentally asserting a
false universal edge/vertex equality.

# 4. New exact certificate: exhaustive local-geometry hardening

I wrote and executed

`artifacts/R06/20260916T151735Z_i0056_closure_hardening_exact.py`.

Its archived output is

`artifacts/R06/20260916T151735Z_i0056_closure_hardening_exact.out`.

The checker is independent of the previous symbolic-only checker in one useful
respect: it exhaustively enumerates **every simple graph on at most six
vertices**, every nonempty proper set, and every admissible closure vertex.

Exact results:

- `2,331,910` multiplicity-two closure moves checked;
- `533,158` terminal multiplicity-one configurations checked;
- in every move,
  \[
  \Delta e=\deg(v)-2r
  \]
  exactly and
  \[
  \Delta b\le -1+\deg(v)-r;
  \]
- every tested terminal multiplicity-one state has `b=e`;
- exact source-threshold sweep over all admissible
  `3<=d<=500`, `5<=f<=500`: `247,007` pairs PASS;
- the only threshold-equality pair in that sweep is Euclidean `(3,6)`;
- `f=4` gives the exact squared obstruction `-1` for every `4<=d<=500`;
- frozen `H_{5,5}` again certifies `Phi_E^2=5`, threshold
  `sqrt(5)>2`, and width `0`.

Checker output SHA-256:
`132c3e371e86cf9f962848f90ce748b11a1d5ad9824032967cdc0c0b50e9e01d`.

This is a **self-check**, not an independent audit.

# 5. Current-status and prior-art check — 2026-09-16

I reran a bounded search rather than treating old `admitted=true` as current
verification.

## 5.1 Original source/status page

Checked:
- `https://rdlyons.pages.iu.edu/prbtree/`

The official page still identifies the current paperback e-version as
**19 August 2026**. The repository intake row still quotes Question 6.20 as an
open question with the Haslegrave--Panagiotis codegree 3 and 4 update.

## 5.2 Haslegrave--Panagiotis primary paper

Checked:
- DOI `10.1002/rsa.20946`;
- full text at Wiley;
- arXiv `1905.09723`.

Their paper explicitly says it establishes the vertex isoperimetric constant
for all triangular and square hyperbolic lattices and that the equality cases
answer Lyons--Peres Question 6.20 for face/codegrees `3` and `4`. I found no
`f>=5` exact outer-vertex formula there.

## 5.3 Later paper by the same author

Checked:
- Christoforos Panagiotis, *Self-avoiding walks and polygons on hyperbolic
  graphs*, J. Graph Theory 106 (2024), DOI `10.1002/jgt.23087`,
  arXiv `1908.00127`.

Its preliminaries explicitly remark that the **vertex Cheeger constant** of
the hyperbolic tessellations `H(d,k)` has been computed for `k=3` or `4`, while
it records the edge constant for general `k`. This is useful later-author
evidence that the `k>=5` outer-vertex constant was not regarded as already
computed in that line of work as of 2024.

## 5.4 Current edge-isoperimetry source

Checked:
- Byung-Geun Oh, arXiv `2009.04394`,
  *Sharp isoperimetric inequalities for infinite plane graphs with bounded
  vertex and face degrees*.

The paper's `(p,q)`-regular convention is: every vertex has degree `p`, every
face has degree `q`. Its exact quantity is the unnormalized crossing-edge
boundary divided by vertex count,
\[
\Phi(p,q)=(p-2)\sqrt{1-\frac4{(p-2)(q-2)}}.
\]
This matches the `Phi_E` normalization required by CLOSURE-01. Oh resolves
the edge-isoperimetric bounded-degree question, not the outer-vertex half of
Question 6.20.

## 5.5 Subsequent/citing work

Checked, among other searches:

- `"Question 6.20" vertex isoperimetric plane graphs`;
- `"Site percolation and isoperimetric inequalities for plane graphs" vertex
  isoperimetric pentagonal`;
- `"outer vertex boundary" regular hyperbolic tiling`;
- `"vertex isoperimetric constant" hyperbolic lattice pentagonal`;
- `"edge isoperimetric constant" "d-3" "vertex isoperimetric"`;
- `"3-regular" "vertex expansion" "edge expansion" equality infinite`.

Relevant subsequent items found:
- D'Achille--Jacquier--Ruszel (2026), regular hyperbolic-lattice perimeter
  minimization: edge/perimeter rather than the original outer-vertex constant;
- Grimmett (2025), hyperbolic site percolation: no exact `f>=5` outer-vertex
  constant located;
- Panagiotis 2026 papers located by author search concern spin systems,
  sandpiles/percolation, and do not resolve this constant.

I found no exact prior source for the threshold theorem
`Phi_E>=d-3 => Phi_V=Phi_E`, nor for the resulting `f>=5` outer-vertex
formula. This remains a **bounded negative search, not proof of novelty**.
Novelty status is therefore `UNVERIFIED`.

One generic literature source gives only the standard comparison
\[
\Phi_V\le\Phi_E\le d\Phi_V,
\]
not the high-expansion equality used here.

# 6. Closure-audit gate and audit request

Searches of the repository for `R06-I0056-CLOSURE-01`, `I0056`, and the
edge-to-vertex theorem found **no** P26 audit and **no** R05 audit of the new
closure theorem.

The existing R05 audit
`R05-AUDIT-R06-I0056-LOWER-20260916T141505Z: PASS_SCOPED`
predates the closure theorem and checked only the old Haslegrave--Panagiotis
lower-bound half. It does not count toward closure of CLOSURE-01.

Under the R-series directed audit cycle, **R05 is the directed auditor for
R06**. P26 is the second required independent audit.

I therefore created the immutable audit packet

`artifacts/R06/20260916T151735Z_i0056_closure_hardening_audit_request.md`

requesting:
1. R05 audit of the theorem, source normalization, simplicity/tessellation
   match, and `f>=5` corollary;
2. P26 independent closure audit of the same package.

No audit is claimed merely because the request exists.

# 7. R07 directed-audit obligation

The newest R07 package remains
`runs/R07/2026-09-16T1425Z_kpz_weighted_overlap_02.md`.

The previous R06 run already independently audited its concrete lemma
`R07-GH-C06` and recorded

`R06-AUDIT-R07-C06-20260916T144133Z: PASS`.

No newer R07 report/package appeared after that audit in the repository view
available to this run, so I did not fabricate or duplicate a new audit.

# 8. Status and remaining obligation

Tracked metric:
\[
\boxed{
0\longrightarrow0
}
\]
for the frozen `H_{5,5}` interval width.

This is the first unchanged run since the metric collapsed to zero.

Mathematical state:
- frozen pair `H_{5,5}`: exact value `sqrt(5)`, **PROVED, audit-gated**;
- all regular/co-regular tessellation cases with face degree `f>=5`:
  exact edge formula transferred to the outer-vertex constant by
  CLOSURE-01, **PROVED, audit-gated**;
- face degrees `3,4`: **KNOWN**, Haslegrave--Panagiotis;
- first regular/co-regular clause of Lyons--Peres Question 6.20:
  **candidate complete, audit-gated**;
- second clause for more general transitive plane graphs: **OPEN**;
- overall Question 6.20: **PARTIAL**.

No paper folder is created because the mandatory independent audits and
novelty/status clearance are not complete.

The next run should first check whether R05 and P26 have returned audits. If
both pass and the prior-art status remains clear enough for the fleet closure
protocol, package the regular/co-regular result while explicitly leaving the
general-transitive clause PARTIAL. If an audit fails, repair the first invalid
step rather than adding unrelated lemmas.

## ledger_delta

```yaml
ledger_delta:
  track: R06
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks (2016; current paperback e-version 2026-08-19), Question 6.20; intake I0056"
  target: "Frozen H_{5,5} outer vertex-isoperimetric constant; plus the regular/co-regular face-degree >=5 branch, excluding the Haslegrave-Panagiotis face-degree 3 and 4 cases"
  metric: "width of rigorously certified interval for Phi_V(H_{5,5})"
  before: "0"
  after: "0"
  movement: "no movement"
  unchanged_count: 1
  status: "PARTIAL overall; H_{5,5} and regular/co-regular f>=5 branch PROVED but audit-gated"
  exact_evidence:
    - "runs/R06/20260916T144133Z_i0056_edge_vertex_closure.md"
    - "artifacts/R06/20260916T144133Z_i0056_edge_vertex_closure_exact.py"
    - "artifacts/R06/20260916T144133Z_i0056_edge_vertex_closure_exact.out"
    - "artifacts/R06/20260916T151735Z_i0056_closure_hardening_exact.py"
    - "artifacts/R06/20260916T151735Z_i0056_closure_hardening_exact.out"
    - "artifacts/R06/20260916T151735Z_i0056_closure_hardening_audit_request.md"
  audit_ids:
    p26_closure_audit: "MISSING"
    directed_r05_closure_audit: "MISSING"
    old_r05_lower_bound_audit: "R05-AUDIT-R06-I0056-LOWER-20260916T141505Z: PASS_SCOPED (does not audit CLOSURE-01)"
    r06_to_r07: "R06-AUDIT-R07-C06-20260916T144133Z: PASS; no newer R07 package observed"
  novelty: "UNVERIFIED; bounded current search found no exact prior theorem"
  remaining_obligation: "Obtain P26 and R05 audits of CLOSURE-01/source corollary; then closure-package only the regular/co-regular clause if audits pass, leaving the general-transitive clause PARTIAL."
```
