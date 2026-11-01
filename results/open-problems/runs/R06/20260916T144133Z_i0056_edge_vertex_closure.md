Model: GPT-5.6 Sol. Reasoning: UNVERIFIED by runtime metadata; GPT-6 maximum was requested, but the scheduler exposes no model or reasoning selector, so I do not claim GPT-6 maximum.
Problem: Russell Lyons and Yuval Peres, *Probability on Trees and Networks* (2016; current paperback e-version dated 19 August 2026), Question 6.20; intake I0056.
Metric movement: certified interval width for the frozen pair `H_{5,5}` moved from `(sqrt(5)-1)/2 = 0.6180339887498948...` to **0**. Frozen-pair status: **PROVED, audit-gated**. Regular/co-regular branch: **candidate PROVED by the theorem below, audit-gated**. Question 6.20 as a whole remains **PARTIAL** because its second clause asks for more general transitive plane graphs.

# R06 immutable run — edge expansion closes the face-degree >=5 vertex constants

Run ID: `20260916T144133Z_i0056_edge_vertex_closure`
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Repository recovery and protocol state

I continued from the newest canonical R06 report

- `runs/R06/20260916T132257Z_i0056_h55_interval.md`.

That report fixed

\[
H_{5,5}=\{5,5\},\qquad
\frac{1+\sqrt5}{2}\le \Phi_V(H_{5,5})\le\sqrt5,
\]

with metric width

\[
\sqrt5-\frac{1+\sqrt5}{2}=\frac{\sqrt5-1}{2}.
\]

Before doing new mathematics I read the required repository controls:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`;
- root `RESULTS.md`;
- root `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`;
- `operations/RFLEET_2026-09-16.md`;
- canonical ownership file `operations/claims/I0056.md`;
- newest neighbouring R05 report `runs/R05/20260916T141505Z_i0030_edge_mnhd_n8.md`;
- newest R07 report `runs/R07/2026-09-16T1425Z_kpz_weighted_overlap_02.md` and its checker output.

The root intake family `probability_1000_intake_*/problems.jsonl` was re-discovered/read-attempted. These large JSONL files are connector-truncated in model-visible output, so I record the intake-family reread as **PARTIAL due connector truncation**, not as a complete row-by-row reread of all roughly 780 entries. The exact I0056 source row and canonical ownership were already recovered in the previous run and remain fixed. No old `admitted=true` value is being used as a substitute for the current-status check below.

No Gmail, Drive, email, public publication, purchase, permission change, workflow execution, or scheduler change occurred. Root shared ledgers were not edited; P26 remains the shared-ledger writer.

The prior two-dimensional Anderson-localization assignment remains retired under the preserved R06 handoff. No personal-project work was resumed.

## 2. Exact source conventions and dated status check

Lyons--Peres define, for unweighted graphs,

\[
\partial_V K
=
\{x\notin K:\exists y\in K,\ x\sim y\},
\]

and

\[
\Phi_V(G)
=
\inf_{\varnothing\ne K\subset V,\ K\text{ finite}}
\frac{|\partial_VK|}{|K|}.
\]

This is the **outer** vertex boundary. The edge analogue used here is

\[
\partial_EK
=
\{xy\in E:x\in K,\ y\notin K\},
\qquad
\Phi_E(G)
=
\inf_K\frac{|\partial_EK|}{|K|}.
\]

For a regular/co-regular plane tessellation I use

- `d` = common vertex degree;
- `f=d^dagger` = common face degree/codegree.

Current source checked 2026-09-16:

- Lyons--Peres current paperback e-version is dated **19 August 2026**. Question 6.20 still asks for `Phi_V(G)` for regular, co-regular plane graphs and then asks for both edge and vertex constants for more general transitive plane graphs.
- The current source note records Haslegrave--Panagiotis for codegrees `3` and `4`, and records Oh (2020) for the separate edge-boundary Question 6.21. It does **not** record an exact face-degree `>=5` vertex formula.
- Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, state that their equality cases answer Question 6.20 for all `f=3` and `f=4` cases. Those cases remain excluded from the present target exactly as requested.
- Byung-Geun Oh, arXiv:`2009.04394`, proves the sharp edge-isoperimetric bound

\[
\Phi(d,f)
=
(d-2)\sqrt{1-\frac{4}{(d-2)(f-2)}}
\]

for plane tessellations with degree/face-degree bounds. Setting lower and upper bounds equal to the same regular/co-regular pair gives

\[
\boxed{
\Phi_E(G)=
(d-2)\sqrt{1-\frac{4}{(d-2)(f-2)}}
}
\tag{2.1}
\]

for the source regular/co-regular class whenever `1/d+1/f<=1/2`.

Dated search queries in this run included:

- `"Question 6.20" vertex isoperimetric Haslegrave Panagiotis`;
- `"vertex isoperimetric" hyperbolic tessellation pentagonal {5,5}`;
- `"outer vertex" "hyperbolic tessellation" isoperimetric`;
- `"edge isoperimetric constant" "vertex isoperimetric constant" regular graph equality`;
- `"h_E > d-3" vertex isoperimetric`;
- `"site perimeter" hyperbolic animals pentagonal tiling`;
- later Panagiotis hyperbolic-graph papers, Roldan--Toala-Enriquez hyperbolic-animal papers, and Grimmett's 2024/2025 hyperbolic site-percolation paper.

I found no paper in this bounded search stating the threshold equality theorem proved below or an exact outer-vertex formula for the `f>=5` regular/co-regular branch. The 2023/2025 hyperbolic-animal papers optimize polygonal-animal perimeter/vertex statistics, not this outer neighboring-vertex constant. **This is not a proof of novelty. Novelty remains UNVERIFIED pending independent audit/search.**

A source erratum issue from the prior run remains: the current Lyons--Peres display for `alpha_d` has a minus-root sign inconsistent with Haslegrave--Panagiotis' primary-paper golden-ratio equality. The present proof does not use that display.

## 3. Refutation-first adversarial check

Before accepting a universal edge-to-vertex equality, I tested it against the already solved quadrangular branch.

For `f=4`, Oh's exact edge formula gives

\[
\Phi_E(d,4)^2=(d-2)(d-4).
\]

But

\[
(d-2)(d-4)-(d-3)^2=-1.
\tag{3.1}
\]

Thus the threshold in the new lemma below fails by an exact unit in squared form for **every** quadrangular case. In particular, for `H_{5,4}` the known Haslegrave--Panagiotis vertex constant is the golden ratio, whereas the edge constant is `sqrt(3)`; they are not equal. So the stronger conjecture `Phi_V=Phi_E for all regular/co-regular plane graphs` is false. The face-degree threshold is doing real work.

For the frozen `H_{5,5}`, the previous exact finite face-ball construction gives vertex-boundary ratios

\[
3,\;\frac73,\;\frac94,\;\frac{47}{21},\;\frac{123}{55},\ldots
\]

decreasing to `sqrt(5)`. Thus any new lower bound above `sqrt(5)` would immediately be refuted by an already archived exact construction. The theorem below lands exactly at `sqrt(5)`, passing this adversarial check.

## 4. R06-I0056-CLOSURE-01 — edge-to-outer-vertex equality above the degree threshold

**Label: PROVED. Full proof included. No planarity or transitivity is needed.**

### Theorem

Let `G` be an infinite simple `d`-regular graph. Define

\[
h_E:=\Phi_E(G),\qquad h_V:=\Phi_V(G)
\]

using finite nonempty vertex sets, with `Phi_V` the outer vertex boundary. If

\[
\boxed{h_E\ge d-3,}
\tag{4.1}
\]

then

\[
\boxed{h_V=h_E.}
\tag{4.2}
\]

### Proof

The easy inequality is always

\[
h_V\le h_E,
\tag{4.3}
\]

because every outside boundary vertex is incident to at least one crossing edge, so

\[
|\partial_VK|\le|\partial_EK|
\]

for every finite `K`.

It remains to prove the reverse inequality.

Fix an arbitrary finite nonempty set

\[
K_0\subset V(G),\qquad n:=|K_0|.
\]

Construct a closure sequence as follows. If there is a vertex

\[
v\notin K_j
\]

having

\[
r_j:=|N(v)\cap K_j|\ge2,
\]

set

\[
K_{j+1}:=K_j\cup\{v\}.
\]

If no such vertex exists, stop.

Write

\[
b_j:=|\partial_VK_j|,
\qquad
e_j:=|\partial_EK_j|.
\]

Because `v` had `r_j` neighbors in `K_j`, exactly `r_j` old crossing edges become internal and exactly `d-r_j` edges from `v` to the new complement become crossing. Therefore

\[
\boxed{
e_{j+1}=e_j+d-2r_j\le e_j+d-4.
}
\tag{4.4}
\]

For the outer vertex boundary, `v` itself disappears from the boundary. Every old boundary vertex different from `v` remains a boundary vertex, because its old neighbor in `K_j` is still in `K_{j+1}`. New boundary vertices can only be outside neighbors of `v` which were not boundary vertices before, and there are at most `d-r_j` of them. Hence

\[
\boxed{
b_{j+1}\le b_j-1+(d-r_j)\le b_j+d-3.
}
\tag{4.5}
\]

We first show that this process must stop after finitely many additions. After `m` additions,

\[
|K_m|=n+m
\]

and iteration of (4.4) gives

\[
e_m\le e_0+m(d-4)\le dn+m(d-4).
\tag{4.6}
\]

By the definition of the edge-isoperimetric constant,

\[
e_m\ge h_E(n+m).
\tag{4.7}
\]

Combining (4.6)--(4.7),

\[
(h_E-d+4)m\le(d-h_E)n.
\tag{4.8}
\]

Condition (4.1) gives

\[
h_E-d+4\ge1>0,
\]

while `h_E<=d` from a singleton test. Thus (4.8) bounds `m` by a finite constant depending on `K_0`; an infinite closure sequence is impossible. Let

\[
\widehat K=K_m
\]

be a terminal set.

At termination every vertex of `partial_V \widehat K` has **at most one** neighbor in `\widehat K`. It has at least one by definition of outer boundary. Therefore each boundary vertex has exactly one neighbor in `\widehat K`, and crossing edges are in bijection with boundary vertices:

\[
\boxed{
|\partial_V\widehat K|
=
|\partial_E\widehat K|.
}
\tag{4.9}
\]

Iterating (4.5) backwards gives

\[
b_0\ge b_m-(d-3)m.
\tag{4.10}
\]

Using (4.9) and edge expansion,

\[
\begin{aligned}
b_0
&\ge e_m-(d-3)m\\
&\ge h_E(n+m)-(d-3)m\\
&=h_E n+(h_E-d+3)m\\
&\ge h_E n,
\end{aligned}
\tag{4.11}
\]

where the last inequality is exactly (4.1).

Since `K_0` was arbitrary,

\[
h_V\ge h_E.
\]

Together with (4.3), this proves (4.2). QED.

### Remarks on scope

1. The argument needs **simplicity** so that distinct outside boundary vertices correspond to crossing edges once the terminal multiplicity is one. The source regular tessellations are simple.
2. No planarity, transitivity, or face structure enters the theorem.
3. Equality at the threshold `h_E=d-3` is allowed. Termination still has one unit of slack because the closure step reduces the edge-boundary comparison at threshold `d-4`.
4. The theorem is deliberately not claimed for `h_E<d-3`; the quadrangular source cases show equality can fail there.

## 5. R06-I0056-COR-F5 — all source regular/co-regular cases with face degree at least five

**Label: PROVED, conditional only on the already-known Oh edge theorem.**

Let `G` be a regular, co-regular plane tessellation in the source class, with common vertex degree `d` and face degree/codegree `f>=5`, satisfying the nonpositive-curvature admissibility

\[
\frac1d+\frac1f\le\frac12.
\]

Oh's theorem gives the exact edge constant

\[
h_E=
(d-2)\sqrt{1-\frac4{(d-2)(f-2)}}.
\tag{5.1}
\]

I claim

\[
h_E\ge d-3.
\tag{5.2}
\]

For `d>=4`, square both nonnegative sides. Exact algebra gives

\[
\begin{aligned}
h_E^2-(d-3)^2
&=(d-2)^2-\frac{4(d-2)}{f-2}-(d-3)^2\\
&=2d-5-\frac{4(d-2)}{f-2}\\
&\ge 2d-5-\frac{4(d-2)}3\\
&=\frac{2d-7}{3}>0,
\end{aligned}
\tag{5.3}
\]

because `f>=5`.

For `d=3`, admissibility forces `f>=6`. Here `d-3=0` and (5.1) is nonnegative, with equality only in the Euclidean `(3,6)` case. So (5.2) holds in every admissible `f>=5` case.

Applying CLOSURE-01 gives the exact vertex constant

\[
\boxed{
\Phi_V(G)
=
\Phi_E(G)
=
(d-2)\sqrt{1-\frac4{(d-2)(f-2)}}
\qquad(f\ge5).
}
\tag{5.4}
\]

This covers not merely `H_{5,5}` but the **entire regular/co-regular face-degree >=5 branch** of the first clause of Lyons--Peres Question 6.20, under the same source tessellation hypotheses used by Oh.

The formula also correctly gives `0` for the Euclidean `(d,f)=(3,6)` case. The remaining Euclidean regular tilings with face degrees `3` or `4` lie in the already-excluded Haslegrave--Panagiotis branch.

### Why this complements rather than replaces Haslegrave--Panagiotis

For `f=4`, exact algebra gives

\[
h_E^2-(d-3)^2=-1,
\]

so CLOSURE-01 does not apply. For `f=3` the gap is larger. Those are precisely the difficult triangular/quadrangular cases handled by Haslegrave--Panagiotis.

Thus, if CLOSURE-01 and its use of Oh's edge theorem survive independent audit, the regular/co-regular part of Question 6.20 is completed by:

- `f=3,4`: Haslegrave--Panagiotis (known);
- `f>=5`: (5.4) above.

The **second clause** of Question 6.20, asking for edge and vertex constants of more general transitive plane graphs, is not resolved here.

## 6. Frozen metric closes: `H_{5,5}`

For the frozen pair

\[
d=f=5,
\]

Oh's edge formula is

\[
\Phi_E(H_{5,5})
=3\sqrt{1-\frac49}
=\sqrt5.
\]

Since

\[
\sqrt5>2=d-3,
\]

CLOSURE-01 gives

\[
\boxed{
\Phi_V(H_{5,5})=\sqrt5.
}
\tag{6.1}
\]

Therefore the certified interval moves from

\[
\left[
\frac{1+\sqrt5}{2},\ \sqrt5
\right]
\]

to

\[
\boxed{[\sqrt5,\sqrt5]},
\]

and the required tracked width moves

\[
\boxed{
\frac{\sqrt5-1}{2}
\longrightarrow
0.
}
\tag{6.2}
\]

This exact value independently matches the previous Higuchi--Shirai face-ball construction, whose boundary ratios tend down to `sqrt(5)`.

## 7. Exact checker and self-check scope

Executed exact checker:

- `artifacts/R06/20260916T144133Z_i0056_edge_vertex_closure_exact.py`
- `artifacts/R06/20260916T144133Z_i0056_edge_vertex_closure_exact.out`

Read-back commits:

- checker create commit: `2368338cd1387ed45ecc8abebcd9ba9e9789ec7a`;
- output create commit: `b5c8b6d7cf43b70ad1bbdd8e69397f3695f21f3c`.

Local SHA-256 before upload:

- source: `63d36e2fadf5f50408584fd8036626556dd678be6ef7eee160a049aa3faae6de`;
- output: `f9f5bcdea3ebaf5744d5acf372d0bb364d968cbb3a183656b03b744ab72ba721`.

The output ends `PASS` and verifies in exact arithmetic/symbolic algebra:

1. one-step closure inequalities for every integer `2<=d<=100`, every `2<=r<=d`;
2. the symbolic iteration algebra `h=d-3+x`;
3. the exact threshold identity (5.3);
4. 9,407 admissible exact rational pair checks with `3<=d<=100`, `5<=f<=100`;
5. `H_{5,5}` has `Phi_E^2=5` and exceeds the threshold `d-3=2`;
6. the post-theorem frozen interval has width `0`;
7. the exact quadrangular obstruction `h_E^2-(d-3)^2=-1`.

The infinite-family proof is the written proof in Sections 4--5; the finite sweep is a **self-check**, not a substitute for that proof.

## 8. Independent audit of R07 package

R07 has a ready package. I independently audited the newest report's lemma

`R07-GH-C06`:

\[
q(r)
=\operatorname{Var}(\min\{X,r\})
\ge
\frac1{16e}
(1-e^{-r})(r\wedge1)^2,
\qquad X\sim\mathrm{Exp}(1).
\]

Audit ID:

`R06-AUDIT-R07-C06-20260916T144133Z: PASS`.

Independent proof:

Let `Y=min(X,r)` and `Y'` be an independent copy. Then

\[
q(r)=\frac12\mathbb E(Y-Y')^2.
\]

If `0<r<=1`, use the two disjoint events

\[
\{X\le r/2,X'\ge r\},
\qquad
\{X'\le r/2,X\ge r\}.
\]

On either, `|Y-Y'|>=r/2`. The factor `2` from the two events cancels the prefactor `1/2`, so

\[
q(r)
\ge
(1-e^{-r/2})e^{-r}\frac{r^2}{4}.
\]

Now `1-e^{-r/2}>=r/4` for `0<=r<=1` and `e^{-r}>=e^{-1}`, hence

\[
q(r)\ge\frac{r^3}{16e}
\ge
\frac1{16e}(1-e^{-r})r^2,
\]

because `1-e^{-r}<=r`.

If `r>=1`, use the two events with thresholds `1/2` and `1`. They give

\[
q(r)
\ge
(1-e^{-1/2})e^{-1}\frac14
\ge
\frac1{16e},
\]

because `1-e^{-1/2}>=1/4`. Since `1-e^{-r}<=1` and `(r wedge 1)^2=1`, the claimed bound follows. The case `r=0` is trivial.

So C06 is correct. This is deliberately a **scoped audit** of C06, not a vote on R07's full KPZ target.

R07's archived checker output also reports PASS for its finite refresh-derivative/kernel checks. I did not rely on that self-check for the analytic argument above.

## 9. Audit/closure state for R06

An earlier independent R05 audit is now present:

`R05-AUDIT-R06-I0056-LOWER-20260916T141505Z: PASS_SCOPED`.

It independently confirms the old Haslegrave--Panagiotis lower bound for `H_{5,5}`. It does **not** audit the new CLOSURE-01 theorem or the exact formula (5.4).

Current closure gate for the new theorem:

- R06 self-proof/checker: **PASS**;
- prior R05 audit of old lower half: **PASS_SCOPED**;
- independent OTHER-track audit of CLOSURE-01 / COR-F5: **PENDING**;
- P26 audit: **PENDING**;
- dedicated novelty/prior-art clearance: **PENDING / UNVERIFIED**.

Therefore I do **not** call the repository problem closed and I do **not** create a paper folder this run, despite the frozen metric reaching zero and the written argument covering the regular/co-regular branch. This follows the fleet closure rule requiring two audits by other tasks plus prior-art clearance.

## 10. Failed routes / adversarial limitations

Preserved route information:

1. The previous universal Haslegrave--Panagiotis lower bound for face degree at least four stopped at the golden ratio for `d=5`; it did not use the exact face degree `5` and left a gap to `sqrt(5)`.
2. Exact finite face-ball constructions gave the sharp-looking upper `sqrt(5)` but by themselves could not certify a universal lower bound.
3. The tempting stronger statement `Phi_V=Phi_E` for every regular/co-regular tessellation is **false**: the `f=4` branch gives the exact threshold deficit (3.1), and known vertex/edge constants differ.
4. The new closure theorem is not being extrapolated to irregular graphs; regularity is used in both update formulas.
5. The new result resolves only the first regular/co-regular clause of Question 6.20. No claim is made about the second, more-general transitive-plane-graph clause.
6. The bounded literature search did not locate this lemma, but absence from search is not novelty proof.

## 11. Next attack

Because the fixed metric has reached its mathematical minimum `0`, the next R06 obligation is **not** to invent a new stronger conjecture. The next run should:

1. recover any independent audit of CLOSURE-01 / COR-F5 from another track and any P26 ledger/audit receipt;
2. adversarially recheck the closure proof against source conventions and against known `f=3,4` constants;
3. deepen prior-art/citation search for an existing edge-to-vertex threshold lemma;
4. if both required independent audits PASS and novelty/status are cleared, package the regular/co-regular resolution according to the closure rules while explicitly leaving Question 6.20's second general-transitive clause PARTIAL;
5. if closure remains audit-gated, do not silently reformulate the target or replace the fixed metric.

## 12. `ledger_delta` for P26

```yaml
ledger_delta:
  track: R06
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks (2016; paperback e-version 2026-08-19), Question 6.20; intake I0056"
  target: "Frozen H_{5,5} outer vertex-isoperimetric constant; plus the source regular/co-regular face-degree >=5 branch, excluding HP face degrees 3 and 4"
  metric: "width of rigorously certified lower/upper interval for Phi_V(H_{5,5})"
  before: "(sqrt(5)-1)/2 = 0.6180339887498948..."
  after: "0; certified interval [sqrt(5), sqrt(5)]"
  status: "PROVED for frozen pair and candidate PROVED for entire regular/co-regular f>=5 branch; audit-gated; Q6.20 overall PARTIAL because the second general-transitive clause remains"
  unchanged_count: 0
  exact_evidence:
    prior_report: "runs/R06/20260916T132257Z_i0056_h55_interval.md"
    checker: "artifacts/R06/20260916T144133Z_i0056_edge_vertex_closure_exact.py"
    checker_output: "artifacts/R06/20260916T144133Z_i0056_edge_vertex_closure_exact.out"
    checker_result: PASS
    checker_source_sha256: "63d36e2fadf5f50408584fd8036626556dd678be6ef7eee160a049aa3faae6de"
    checker_output_sha256: "f9f5bcdea3ebaf5744d5acf372d0bb364d968cbb3a183656b03b744ab72ba721"
    theorem: "If G is infinite simple d-regular and Phi_E(G)>=d-3, then Phi_V(G)=Phi_E(G)"
    source_corollary: "For admissible regular/co-regular plane G with f>=5, Phi_V=Phi_E=(d-2)*sqrt(1-4/((d-2)(f-2)))"
  audit_ids:
    R05_prior_lower: "R05-AUDIT-R06-I0056-LOWER-20260916T141505Z: PASS_SCOPED"
    new_theorem_other_track: PENDING
    P26: PENDING
    R06_to_R07: "R06-AUDIT-R07-C06-20260916T144133Z: PASS"
  prior_art:
    status: "UNVERIFIED novelty; bounded dated search found no existing exact f>=5 outer-vertex formula or edge-to-vertex threshold lemma"
    source_current_status: "Lyons-Peres 2026-08-19 still lists Q6.20 with HP f=3,4 update and Oh edge-Q6.21 update"
```
