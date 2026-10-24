Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: frozen I0056/H_{5,5} outer-vertex interval width `0 -> 0`; frozen target remains PROVED/audit-complete, full Lyons–Peres Question 6.20 remains PARTIAL; methods #3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #15 BREAK THE SYMMETRY ON PURPOSE.**

# R06 — I0056 prior-art hardening and a quantitative edge-to-vertex interpolation lemma

Date: 2026-09-18 UTC  
Worker: R06  
Lane: CLOSABLE OUTSIDE  
Repository: private `yspennstate/math-open-problems`, branch `master`

## 1. Continuity and controlling state

I did not reopen the frozen source metric or restart the proof from scratch. I continued from the latest R06 audit-correction/admission state and reread the current campaign controls (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`), the current operations follow-up manifest, the source theorem report, both outside audits, and the newest neighboring successor-admission screens available on master.

The exact source question remains Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20:

> What is `Phi_V(G)` for regular co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive plane graphs `G`?

The neighboring Question 6.21 is the bounded-degree / bounded-codegree **edge-boundary** inequality. The distinction matters below.

The frozen normalization is the outer vertex boundary

\[
\partial_V K=\{x\notin K:\exists y\in K,\ x\sim y\},\qquad
\Phi_V(G)=\inf_{0<|K|<\infty}\frac{|\partial_VK|}{|K|}.
\]

For the frozen regular/co-regular pair `H_{5,5}` the preserved result is

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad
[L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

The source-matching theorem already proved by R06 is stronger: if an infinite simple `d`-regular graph has edge expansion `h_E>=d-3`, then its outer vertex expansion equals its edge expansion. Combining this with the classical regular-tessellation edge constant gives the full regular/co-regular face-degree `f>=5` branch. Haslegrave–Panagiotis supply the already-known `f=3,4` branch. Thus the **first** regular/co-regular clause is mathematically accounted for, but Question 6.20 as a whole remains PARTIAL because of its second, more-general transitive-plane-graph clause.

Independent audits remain:

- `R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`;
- `P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15 = PASS_FULL_MATHEMATICAL_PROOF / REGULAR-COREGULAR-FIRST-CLAUSE / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`.

No shared root ledger or other track file was edited in this run.

## 2. Idea before code

The source metric cannot move below width zero. The highest-value research move is therefore not another certificate for `sqrt(5)`, but to stress-test the mechanism in two directions:

1. strengthen the abstract edge-to-vertex theorem quantitatively *below* its equality threshold, to see exactly what the closure algorithm still proves when equality fails;
2. search older and current hyperbolic-isoperimetry literature under the **edge** normalization and the symmetry-group language, because a numerical match to `sqrt(5)` is not enough to duplicate an outer-vertex theorem.

No code was needed: the new mathematical item is theorem-sized and is proved on the page, while the literature correction is documentary rather than finite computational evidence.

## 3. Method #3 — PROVE SOMETHING STRONGER: quantitative interpolation below `h_E=d-3`

The prior R06 theorem gives exact equality once `h_E>=d-3`. The same closure process yields a nontrivial lower bound even when `h_E` is slightly smaller.

### Proposition R06-I0056-INTERPOLATION-42

Let `G` be an infinite simple `d`-regular graph. Let

\[
h:=\Phi_E(G),\qquad v:=\Phi_V(G).
\]

Assume

\[
h>d-4,
\]

and put

\[
x:=h-d+4>0.
\]

Then:

1. if `x>=1` (equivalently `h>=d-3`),
   \[
   \boxed{v=h};
   \]
2. if `0<x<1`,
   \[
   \boxed{
   v\ge
   \max\left\{
   \frac{h}{d-(d-1)x},
   \ d+1-\frac4x
   \right\}.
   }
   \tag{3.1}
   \]

The second term may be negative away from the threshold; the first is always positive and tends to the trivial `h/d` bound as `x downarrow 0`.

### Proof

Fix a finite nonempty `K_0` of size `n`. As in the earlier closure theorem, while there is a vertex outside `K_j` having `r_j>=2` neighbors in `K_j`, add it. Write

\[
e_j:=|\partial_EK_j|,\qquad b_j:=|\partial_VK_j|.
\]

One addition gives

\[
e_{j+1}=e_j+d-2r_j\le e_j+d-4,
\tag{3.2}
\]

and

\[
b_{j+1}\le b_j-1+(d-r_j)\le b_j+d-3.
\tag{3.3}
\]

After `m` additions,

\[
e_m\le e_0+(d-4)m,
\]

whereas edge expansion gives

\[
e_m\ge h(n+m).
\]

Hence

\[
xm=(h-d+4)m\le e_0-hn.
\tag{3.4}
\]

Since `x>0`, the process terminates. At the terminal set every outer boundary vertex has exactly one neighbor inside, so

\[
b_m=e_m.
\tag{3.5}
\]

Iterating (3.3) backwards and using (3.5),

\[
\begin{aligned}
b_0
&\ge b_m-(d-3)m\\
&=e_m-(d-3)m\\
&\ge h(n+m)-(d-3)m\\
&=hn+(x-1)m.
\end{aligned}
\tag{3.6}
\]

If `x>=1`, the last term is nonnegative, so `b_0>=hn`. Since always `v<=h`, this gives `v=h`, recovering `R06-I0056-CLOSURE-01`.

Now assume `0<x<1`. First use `e_0<=dn` in (3.4):

\[
m\le \frac{(d-h)n}{x}.
\]

Because `x-1<0`, substituting this upper bound into (3.6) yields

\[
\frac{b_0}{n}
\ge h+\frac{(x-1)(d-h)}x
=d+1-\frac4x.
\tag{3.7}
\]

For a second bound, every crossing edge is incident with an outer boundary vertex and each such vertex has degree `d`, hence

\[
e_0\le d b_0.
\]

Together with (3.4),

\[
m\le \frac{db_0-hn}{x}.
\]

Again using `x-1<0` in (3.6), and writing `B=b_0/n`,

\[
B\ge h+\frac{x-1}{x}(dB-h).
\]

Since `0<x<1`, the coefficient of `B` after rearrangement is positive:

\[
\frac{d-(d-1)x}{x}>0.
\]

Therefore

\[
B\ge \frac{h}{d-(d-1)x}.
\tag{3.8}
\]

As `K_0` was arbitrary, (3.7) and (3.8) give (3.1). QED.

### Why this matters / what it does not do

This proposition does **not** move the frozen `H_{5,5}` metric; that case already lies in the equality regime. It clarifies the mechanism: the closure argument does not abruptly become useless below `d-3`; it degrades continuously down to the standard edge-to-vertex comparison as `h` approaches `d-4`.

For the quadrangular regime the bound is not sharp, which is consistent with Haslegrave–Panagiotis: their exact vertex theorem genuinely uses planar structure that the abstract closure argument discards.

Novelty of Proposition 42 is **UNVERIFIED**. A bounded exact-phrase/formula search on 2026-09-18 found standard qualitative comparisons between edge and vertex expansion, but did not surface this threshold/interpolation formula. Negative search evidence is not a novelty certificate.

## 4. Method #14 — FIND THE GROUP ACTING: older edge-constant literature is much closer than the earlier dependency log suggested

A material prior-art correction emerged from the symmetry-group language.

Yusuke Higuchi and Tomoyuki Shirai, *Isoperimetric Constants of (d,f)-Regular Planar Graphs*, Interdisciplinary Information Sciences **9** (2003), 221–228, DOI `10.4036/iis.2003.221`, work with the canonical regular Euclidean/hyperbolic tessellations. For the hyperbolic case they explicitly describe the tessellation via the Fuchsian triangle group `Gamma(2,f,d)`.

Their first constant is

\[
\alpha(G)
=
\inf_K \frac{|E(\partial_v K)|}{\operatorname{Area}(K)},
\qquad
\operatorname{Area}(K)=\sum_{x\in V(K)}\deg_G(x),
\]

where `E(partial_v K)` is the **edge cut** from `K` to its complement. In a `d`-regular graph this means `d alpha(G)=Phi_E(G)`. Their main theorem gives

\[
\alpha(G)=\frac{d-2}{d}
\sqrt{1-\frac4{(d-2)(f-2)}}.
\]

Thus the exact regular/co-regular edge formula used by R06 was already present in 2003; Higuchi–Shirai also state that Häggström–Jonasson–Lyons obtained the same main theorem independently by duality. Lyons–Peres themselves attribute the regular-tessellation edge calculations to Häggström–Jonasson–Lyons (2002) and note Higuchi–Shirai as the independent proof.

**Correction to dependency chronology:** the R06 `f>=5` corollary does not need Oh (2020) for the regular/co-regular edge value. Oh's 2020 sharp bounded-degree/bounded-face-degree theorem is the later, more general edge result aligned with Lyons–Peres Question 6.21. For the frozen regular/co-regular branch, HJL 2002 / Higuchi–Shirai 2003 are the historically correct edge dependencies.

Crucially, none of this is the outer-vertex constant of Question 6.20. The 2003 numerator is a number of crossing **edges**, not a number of distinct outside neighboring vertices.

## 5. Method #15 — BREAK THE SYMMETRY ON PURPOSE: same numerical constant, different boundary object

The most dangerous novelty error here is to identify every hyperbolic `sqrt(5)` perimeter coefficient with `Phi_V(H_{5,5})`. I explicitly broke that identification by checking the boundary object in later papers.

### 5.1 D'Achille–Jacquier–Ruszel, current 2026 publication

Matteo D'Achille, Vanessa Jacquier and Wioletta M. Ruszel, *On minimal shapes and isoperimetric constants in hyperbolic lattices*, **Discrete Mathematics 349 (2026), no. 9, 115188**, DOI `10.1016/j.disc.2026.115188`, is now a peer-reviewed September 2026 publication (preprint arXiv:2504.14080).

Their definition is explicit: for a vertex set `A`, the perimeter is the cardinality of the **external edge boundary**

\[
|\partial_e A|=|\{(v,w)\in E:v\in A,\ w\notin A\}|,
\]

and the infinite-graph Cheeger constant is `inf |partial_e A|/|A|`. Their paper characterizes fixed-size perimeter minimizers and shows convergence to the Häggström–Jonasson–Lyons isoperimetric constant. This is strong, current adjacent prior art on the **edge** problem, not a duplicate solution of the outer-vertex problem.

### 5.2 Roldán–Toalá-Enríquez 2025

Érika Roldán and Rosemberg Toalá-Enríquez, *Isoperimetric Formulas for Hyperbolic Animals*, Graphs and Combinatorics **41** (2025), article 38, DOI `10.1007/s00373-025-02900-1`, define an animal perimeter as the number of boundary edges of a tile union. This again lives on the edge/tile-perimeter side. For `{5,5}` its asymptotic coefficient numerically matches `sqrt(5)`, but the normalization is not the R06 outer vertex boundary.

### 5.3 Haslegrave–Panagiotis remains the correct vertex prior art

Haslegrave–Panagiotis, DOI `10.1002/rsa.20946`, explicitly say their equality cases answer Lyons–Peres Question 6.20 for face degrees `3` and `4`, and establish the vertex constants for triangular and quadrangular hyperbolic lattices. Those regimes remain excluded and are not relabeled as R06 work.

The f>=5 outer-vertex bridge is therefore not erased by finding older or newer edge-isoperimetry papers with the same coefficient.

## 6. Dated prior-art/source search log — 2026-09-18

Primary/current items checked in this run included:

- Lyons–Peres Question 6.20 and neighboring Question 6.21 in the book PDF;
- Haslegrave–Panagiotis, DOI `10.1002/rsa.20946`;
- Häggström–Jonasson–Lyons, *Annals of Probability* **30** (2002), 443–473, DOI `10.1214/aop/1020107775` / arXiv:math/0008191;
- Higuchi–Shirai (2003), DOI `10.4036/iis.2003.221`;
- Byung-Geun Oh, arXiv:2009.04394;
- Roldán–Toalá-Enríquez (2025), DOI `10.1007/s00373-025-02900-1`;
- D'Achille–Jacquier–Ruszel, Discrete Mathematics (Sept. 2026), DOI `10.1016/j.disc.2026.115188`.

Searches included exact combinations of `vertex isoperimetric constant`, `outer vertex boundary`, `edge isoperimetric constant`, `d-regular`, `d-3`, `hyperbolic tessellation`, `pentagonal`, and the exact Question 6.20 language. The bounded search found no primary source stating the R06 abstract threshold theorem `h_E>=d-3 => h_V=h_E` or the new interpolation bound (3.1), and no later primary source explicitly giving the f>=5 outer-vertex formula as an answer to Question 6.20.

This remains **negative search evidence only**. Priority/novelty is still `UNVERIFIED`; it must not be advertised as new until a proper citation-graph / expert-level prior-art check is complete.

## 7. Source status and fixed metric

The frozen single constant remains

\[
\Phi_V(H_{5,5})=\sqrt5,
\]

with certified interval width

\[
0\to0.
\]

Status labels:

- frozen `H_{5,5}` subtarget: **PROVED / AUDIT-COMPLETE**;
- regular/co-regular first clause of Q6.20: **mathematically accounted for** by R06 f>=5 plus the already-known Haslegrave–Panagiotis f=3,4 cases; priority/novelty of the R06 bridge remains UNVERIFIED;
- full Question 6.20: **PARTIAL**, because the more-general transitive-plane-graph clause is not solved here.

No smaller sampled interval is being represented as progress; the metric is already at its mathematical floor.

## 8. Successor admission state

I also checked current neighboring admission work rather than stealing a stale queue row. The current coordinator screen advances the common CLOSABLE cursor through `I0089` with `E_ready=0`; R02 has screened `I0090–I0099`, and R01 has screened through `I0117`, with ownership/source-status/exclusion gates blocking the apparent candidates. I did not promote any PENDING row to READY and did not overwrite an existing owner.

Accordingly R06 remains at `SUCCESSOR_ADMISSION_REQUIRED` after this source-hardening run. The successor mathematical metric remains `UNMEASURED`, not zero.

## 9. Runtime/model-control truth

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol** and exposes no authenticated reasoning-effort telemetry, so the reasoning level is **UNVERIFIED**.

The available task-control surface still exposes task title/prompt, schedule or relative start, timing mode, and enabled state. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed hour-long execution field**.

The historical P26 response `You cannot modify this task` was context/authorization-specific; repository operations records show that a later authorized context successfully updated P26. The lawful workaround is therefore to use the owning/authorized product or admin context (or platform support), not to bypass permissions or create a duplicate task. Enforcing GPT-6/maximum itself would require a product/backend scheduler surface exposing persistent model/reasoning controls plus authenticated runtime telemetry. No scheduler or permission change was attempted here.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  source: "Lyons-Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  frozen_pair: "H_{5,5}"
  graph_class: "regular co-regular plane tessellation"
  normalization: "outer vertex boundary |partial_V K|/|K|"
  metric: "certified interval width U-L"
  before: 0
  after: 0
  metric_movement: "NO MOVEMENT"
  frozen_value: "sqrt(5)"
  frozen_status: "PROVED_AUDIT_COMPLETE"
  full_source_status: "PARTIAL"
  successor_metric: "UNMEASURED"
  successor_status: "SUCCESSOR_ADMISSION_REQUIRED"
  tried_moves: [3, 14, 15]
  new_claims:
    - "R06-I0056-INTERPOLATION-42: quantitative edge-to-outer-vertex lower bound for d-regular graphs when h_E>d-4; novelty unverified"
  prior_art_corrections:
    - "regular/co-regular edge constant dependency should cite Haggstrom-Jonasson-Lyons 2002 and Higuchi-Shirai 2003, not rely on Oh 2020"
    - "D'Achille-Jacquier-Ruszel 2026 is edge-boundary Cheeger/minimal-shape work, not outer-vertex Question 6.20"
    - "Roldan-Toala-Enriquez 2025 is tile edge-perimeter work, not outer-vertex Question 6.20"
  audits:
    - "R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z"
    - "P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15"
  remaining_obligation: "No further work on the zero-width frozen constant; maintain PARTIAL label for the full source and admit a lawful free CLOSABLE successor when one is actually READY. Novelty of the abstract bridge/interpolation requires deeper prior-art review before publication."
```

No email, Drive, public posting, purchase, permission change, scheduler change, or peer-file edit occurred.
