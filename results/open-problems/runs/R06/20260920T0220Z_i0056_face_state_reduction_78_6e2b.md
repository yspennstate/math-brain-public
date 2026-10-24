Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FROZEN I0056 METRIC NO MOVEMENT / SOURCE-CLAUSE BOUND MOVEMENT: `H_{5,5}` width `0 -> 0`; for the source-valid tetrapentagonal graph `T=r{4,5}`, the rigorous vertex upper bound improves `33178/38983 -> 113708/133611`, shrinking the secondary certified interval width `0.3429895229019940 -> 0.34293830065971065`; methods #18 SAY IT IN ANOTHER LANGUAGE, #13 FIND WHAT ONLY INCREASES, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R06 / I0056 — triangle-group face states and a sharper tetrapentagonal vertex bound

Repository: private `yspennstate/math-open-problems`, branch `master`.  
Worker: R06.  
Source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20; intake `I0056`.  
Overall source status after this run: **PARTIAL**.

## 1. Exact source, normalization, and frozen metric

The maintained source question retained by R06 is:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The normalization remains

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_VK|}{|K|},
\qquad
\partial_VK=\{x\notin K:\exists y\in K,\ x\sim y\}.
\]

The frozen regular/co-regular target is still

\[
H_{5,5}=\{5,5\},\qquad (d,f)=(5,5),
\]

with the already proved/audited/posted value

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

Thus the fixed metric cannot decrease numerically. This does **not** close the full source question, because Question 6.20 also asks for edge and vertex constants for more general transitive plane graphs.

Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain excluded prior art: their paper proves the exact vertex-isoperimetric constants for the triangular and square hyperbolic lattices and explicitly identifies these as the face/codegree `3` and `4` cases of Question 6.20. Nothing in this report relabels those cases.

## 2. Continuity recovered before research

The newest prior R06 report read before this attack was

`runs/R06/20260920T0118Z_i0056_schreier_ball_growth_77_f3a1.md`.

It left the source-valid mixed-face graph

\[
R=H_{5,4}=\{4,5\},\qquad T=M(R)=r\{4,5\}
\]

where `T` is the 4-regular vertex-transitive plane graph of cyclic face type `[4,5,4,5]` (the tetrapentagonal tiling), with rigorous interval

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(T)
\le \frac{33178}{38983}.
}
\tag{2.1}
\]

It also had an exact Coxeter/Schreier development through radius 16 and an **unproved** shell recurrence observed on finitely many generations. The previous report explicitly said that merely computing another larger ball was now lower-value than finding the finite-state mechanism behind that recurrence. This run follows that instruction: the main new work is the face-state reduction; the improved finite ball bound is a byproduct/certificate.

The current progress-first owner directive was also read. It supersedes the old repeated targetless-admission loop and explicitly asks for substantive mathematics while preserving source/ownership/history. `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the campaign index, and current R06 history were checked for material changes. `I0056/R06` remains assigned and the regular-tessellation result remains excluded from duplicate research.

## 3. Fresh literature boundary checked 20 September 2026

Primary/current items checked this run:

1. **Haslegrave--Panagiotis (2021), DOI `10.1002/rsa.20946`.** The current Wiley page still says that the paper establishes the vertex constant for all triangular and square hyperbolic lattices; the full text says these answer Lyons--Peres Question 6.20 for `d'=3,4`. This does not cover `[4,5,4,5]`.
2. **de Souza--da Silva, “Enumeration and Growth Functions for Uniform Tilings of the Hyperbolic Plane”, Ars Combinatoria 160 (2024), DOI `10.61091/ars-160-14`.** The current full-text page defines generations by graph distance, arrival/departure/fraternal edges, and the rule that a face starts at a vertex or fraternal edge and closes after a distance dictated by its parity. It develops a finite face-position method and rational generating functions. In the checked article, the explicit enumerations are for all valence-5 families and selected/general valence-6 families; I did not find the valence-4 `[4,5,4,5]` generating function printed there. Importantly, its “at most two arrival edges” lemma is stated for valence at least 6, so I do **not** import that lemma into our valence-4 graph.
3. **Floyd--Plotnick (1994), “Growth functions for semi-regular tilings of the hyperbolic plane”, DOI `10.1007/BF01264041`.** The accessible publisher/university abstract concerns growth of torsion-free surface groups with an `n`-gon fundamental domain and edge-identification generating set. It is highly relevant background for reciprocal/Salem growth functions, but the checked abstract is not a direct statement of the graph-distance sphere sequence of our tetrapentagonal 1-skeleton.
4. **da Silva--de Souza (2022), “Uniform tilings, border automata and orbifolds of the hyperbolic plane”.** Current bibliographic/search material explicitly includes `[4,5,4,5]` as a uniform-tiling construction example. I did not find in the checked material the exact outer-vertex isoperimetric constant or the shell rational function below.

Dated searches included exact strings for `[4,5,4,5]`, `tetrapentagonal growth function`, the shell prefix `1,4,10,20,38,70,130,240`, the candidate denominator polynomial, and `tetrapentagonal isoperimetric vertex boundary`. I did not recover a primary source announcing either the exact vertex-isoperimetric constant or this exact shell formula. This is **bounded negative evidence only**, not a novelty/priority certificate. The growth-function mechanism itself is plainly part of an established literature.

## 4. Idea before code and methods used

The required idea was written before the new checker in

`artifacts/R06/20260920T0220Z_i0056_cayley_face_states_idea_78_6e2b.md`.

### #18 — SAY IT IN ANOTHER LANGUAGE

The preceding exact model used the Coxeter reflections `s1,s2,s3` and the four medial moves

\[
r=s_2s_3,\quad r^{-1},\quad q=s_1rs_1,\quad q^{-1}.
\]

The new exact arithmetic check reveals the additional identity

\[
\boxed{r^5=q^5=1,\qquad (rq^{-1})^2=1.}
\tag{4.1}
\]

Thus the two pentagon cycles and the square cycle are exposed directly in the orientation-preserving triangle-group language. This is consistent with the known `[5,5]` half-symmetry of the tetrapentagonal tiling. I do **not** claim (4.1) itself as novel; its value here is that it makes the distance-frontier state equations transparent.

The finite certificate does not require a global claim that the action is a new presentation theorem: it works in the already verified exact orbit model and checks (4.1) as a matrix identity.

### #13 — FIND WHAT ONLY INCREASES

Track graph distance from the root. Every edge changes distance by `-1,0,+1`. On the exactly developed layers, every non-root vertex is one of only three coarse types:

\[
A=(1\text{ arrival},0\text{ fraternal},3\text{ departure}),
\]
\[
B=(1,1,2),\qquad C=(2,0,2).
\tag{4.2}
\]

The missing arbitrary-radius theorem is now sharply isolated: prove that no fourth frontier type ever appears.

### #30 — ONE SCALE / ONE DIRECTION AT A TIME

Separate the two faces incident to a same-generation (fraternal) edge. Exact development shows two orientations only:

- `X_n`: pentagon runs inward with relative level profile `(0,0,-1,-2,-1,0)` while the square runs outward `(0,0,+1,+1,0)`;
- `Y_n`: the reverse orientation, with pentagon outward `(0,0,+1,+2,+1,0)` and square inward `(0,0,-1,-1,0)`.

This splits square propagation from pentagon propagation and yields a small delayed state system instead of one opaque shell sequence.

Before using the pattern, I tried to falsify it in the exact development: through every fully exposed layer checked, no exotic `(arrival,fraternal,departure)` type and no third fraternal-face profile occurs.

## 5. A new rigorous source-clause bound

The exact Schreier breadth-first development now reaches radius 18:

\[
\begin{aligned}
(|S_n|)_{n=0}^{18}={}&1,4,10,20,38,70,130,240,446,824,1528,2824,\\
&5234,9680,17934,33178,61450,113708,210566.
\end{aligned}
\tag{5.1}
\]

Hence for the radius-16 graph ball,

\[
|B_{16}|=\sum_{j=0}^{16}|S_j|=133611,
\qquad
|\partial_VB_{16}|=|S_{17}|=113708.
\]

(The equality `partial_V B_16=S_17` is automatic for graph-distance balls.) Therefore

\[
\boxed{
\Phi_V(T)\le \frac{113708}{133611}
=0.8510377139606768\ldots
}
\tag{5.2}
\]

and this strictly improves the preceding certified value because

\[
33178\cdot133611-113708\cdot38983
=266794>0.
\tag{5.3}
\]

Combining (5.2) with the inherited lower bound gives

\[
\boxed{
\frac1{\sqrt3+\sqrt5-2}
\le \Phi_V(r\{4,5\})
\le \frac{113708}{133611}.
}
\tag{5.4}
\]

Numerically,

\[
0.5080994133009662\ldots
\le \Phi_V(r\{4,5\})
\le 0.8510377139606768\ldots .
\]

Thus the rigorous secondary interval width moves

\[
0.3429895229019940
\longrightarrow
\boxed{0.34293830065971065},
\]

a decrease of about `5.12222423e-5` (`0.014934%` of the preceding width).

This is a real bound on a graph in the still-open source clause. It is **PROVED PARTIAL / R06 self-check**, not a determination of `Phi_V(T)` and not closure of Question 6.20.

## 6. Exact finite frontier anatomy

For each fully exposed sphere through `n=17`, the exact checker determines the counts `(A_n,B_n,C_n)` from (4.2):

```text
n : (A_n, B_n, C_n)
1 : (4, 0, 0)
2 : (4, 4, 2)
3 : (4, 12, 4)
4 : (8, 24, 6)
5 : (16, 40, 14)
6 : (32, 72, 26)
7 : (56, 132, 52)
8 : (104, 252, 90)
9 : (188, 464, 172)
10: (356, 864, 308)
11: (652, 1584, 588)
12: (1220, 2948, 1066)
13: (2236, 5436, 2008)
14: (4168, 10104, 3662)
15: (7672, 18648, 6858)
16: (14272, 34600, 12578)
17: (26320, 63924, 23464)
```

For the fraternal edges, the exact counts are

```text
n=2..16:
X_n = 2,4,8,12,24,42,84,148,284,508,966,1752,3300,6024,11276
Y_n = 0,2,4,8,12,24,42,84,148,284,508,966,1752,3300,6024
```

so every checked layer satisfies

\[
B_n=2(X_n+Y_n),\qquad Y_n=X_{n-1}.
\tag{6.1}
\]

Splitting the two-parent vertices into `C_n^4` (closing a square between the arrival edges) and `C_n^5` (closing a pentagon) gives, on every index where the entire relevant faces are exposed,

\[
C^5_{n+2}=Y_n.
\tag{6.2}
\]

If `Q_n` is the number of square faces starting at generation `n` and `P_n` the number of pentagons starting there, the exact local counts satisfy

\[
Q_n=A_n+2Y_n+C_n^4,
\qquad
C^4_{n+2}=Q_n,
\tag{6.3}
\]

\[
P_n=A_n+2X_n+C_n^5,
\qquad
X_{n+2}=P_n.
\tag{6.4}
\]

The checker verifies (6.2)--(6.4) for every safe index `3<=n<=14`; these are finite claims only at this stage.

## 7. Conditional theorem: one frontier lemma implies the observed recurrence

The state equations make the remaining proof obligation much smaller than “guess and prove an order-six recurrence”.

### Frontier-anatomy lemma still needed

For every graph-distance generation of `T`, prove that:

1. every non-root vertex has one of the three types `A,B,C` in (4.2);
2. every fraternal edge is exactly one of the two face profiles `X,Y` above;
3. the square/pentagon start-and-close rules (6.1)--(6.4) continue with no additional face-position state.

Call this statement `FAL(4,5,4,5)`.

### Proposition (conditional on `FAL(4,5,4,5)`)

If `FAL(4,5,4,5)` holds at all generations, then the shell numbers satisfy, for every `n>=7`,

\[
\boxed{
S_n=S_{n-1}+2S_{n-2}-2S_{n-3}+2S_{n-4}+S_{n-5}-S_{n-6}.
}
\tag{7.1}
\]

Consequently the graph-distance growth series is

\[
\boxed{
V(z)=\sum_{n\ge0}S_nz^n
=\frac{1+3z+4z^2+4z^3+4z^4+3z^5+z^6}
{1-z-2z^2+2z^3-2z^4-z^5+z^6}.
}
\tag{7.2}
\]

### Algebraic reduction

Under `FAL`, (6.1)--(6.4) are identities. Since `C_n^5=Y_{n-2}=X_{n-3}`, (6.4) gives

\[
A_n=X_{n+2}-2X_n-X_{n-3}.
\tag{7.3}
\]

Also, using `C_n=C_n^4+C_n^5`, equations (6.2)--(6.3) give

\[
C_{n+2}=A_n+C_n+3X_{n-1}-X_{n-3}.
\tag{7.4}
\]

Finally double-count the edges between successive spheres. Departures from generation `n` equal arrivals into generation `n+1`, so

\[
3A_n+2B_n+2C_n
=A_{n+1}+B_{n+1}+2C_{n+1}.
\tag{7.5}
\]

Substitute `B_n=2(X_n+X_{n-1})`, (7.3), and (7.4) into (7.5). After cancellation one obtains

\[
R_{m+1}=R_m,
\]

where

\[
R_m:=X_m-X_{m-1}-2X_{m-2}+2X_{m-3}-2X_{m-4}-X_{m-5}+X_{m-6}.
\tag{7.6}
\]

The exact initial layers give `R_m=0` at one admissible base index, hence (7.6) forces `R_m=0` thereafter. Thus `X_n` satisfies the denominator recurrence in (7.1). Equations (6.1), (7.3), and (7.5) then show the same recurrence for `A_n,B_n,C_n`, after checking one finite base residual; summing gives (7.1). The initial values in (5.1) yield the numerator in (7.2).

This is a **conditional proof**, because the all-generation `FAL(4,5,4,5)` step is not yet on the page. The algebra after that lemma is complete.

The exact checker independently confirms (7.1) on every `7<=n<=18`, extending the previous finite verification from `n<=16`. That finite agreement is evidence for `FAL`, not a substitute for proving it.

## 8. Why this is a better obstruction than the old recurrence guess

The 2024 face-position paper provides exactly the language needed for the next step: arrivals, departures, fraternal edges, and deterministic face closure distances. But its general “at most two arrivals” lemma quoted in the checked text assumes valence at least 6; our tetrapentagonal graph has valence 4. So the last gap cannot be closed by citing that lemma unchanged.

The new obstruction is therefore concrete and local:

\[
\boxed{\text{prove `FAL(4,5,4,5)` for the valence-4 tetrapentagonal tiling.}}
\]

A proof can attack the first hypothetical exotic frontier vertex and use the alternating square/pentagon faces to force an earlier exotic vertex, or translate (4.1) into a finite geodesic-cone automaton. Either route is substantially narrower than deriving the shell recurrence from scratch.

The triangle-group relation also explains why a finite cone-type proof should exist, but older Cannon/Floyd--Plotnick growth theory means that the *existence* of some finite automaton/rational growth function is not in itself a novelty claim. The source-relevant objective remains the isoperimetric constant, not ownership of a growth-series technique.

## 9. Exact certificate

Idea-before-code artifact:

`artifacts/R06/20260920T0220Z_i0056_cayley_face_states_idea_78_6e2b.md`

Executed exact-arithmetic checker:

`artifacts/R06/20260920T0220Z_i0056_face_state_exact_78_6e2b.py`

Archived output:

`artifacts/R06/20260920T0220Z_i0056_face_state_exact_78_6e2b.out`

The executed output ends with

`ALL_EXACT_CHECKS_PASS`.

It certifies: Coxeter relations; the new exact relation `(r q^{-1})^2=1`; shells through radius 18; the radius-16 ball/boundary and strict rational improvement; the complete `A/B/C` anatomy through layer 17; the two fraternal face profiles through layer 16; the finite face-start/closure identities on their fully exposed index range; and the scalar recurrence through `n=18`.

This is an R06 **self-check**, not an independent outside audit.

## 10. Status and next attack

### What is proved this run

- The rigorous source-clause upper bound improves to `113708/133611`.
- The exact triangle relation (4.1) holds in the verified orbit representation.
- The stated finite frontier anatomy and face-state identities hold on the checked layers.
- Conditional on one explicit all-generation frontier lemma, the candidate order-six shell recurrence and rational growth series follow by a complete algebraic elimination.

### What is not proved

- `FAL(4,5,4,5)` is not yet proved for arbitrary radius.
- The recurrence is therefore not yet promoted to an unconditional all-generation theorem.
- `Phi_V(T)` is not determined.
- The full Lyons--Peres Question 6.20 remains **PARTIAL**.

### Next concrete attack

Do **not** spend the next run merely increasing the BFS radius. Instead prove `FAL(4,5,4,5)` by one of two routes:

1. **minimal exotic vertex / face closure:** assume the first generation containing a vertex outside `A,B,C`; use the alternating `4,5,4,5` incident faces and the deterministic start/closure profiles to push the defect to an earlier generation;
2. **geodesic cone automaton:** use `r^5=q^5=(rq^{-1})^2=1` to classify the finite set of geodesic suffix/cone states and read off exactly the same `A/B/C/X/Y` transition system.

Either proof would convert Section 7 from CONDITIONAL to PROVED and give a rigorous arbitrary-radius structural model for later isoperimetric optimization.

## 11. Model / scheduler truth

The available scheduler-control surface still exposes task identity/title, prompt, schedule/timing mode, and enabled-state controls, but **no binding model-family selector, no binding reasoning-effort selector, no guaranteed hour-long execution control, and no authenticated applied-model/applied-effort receipt**. The repository progress-first directive records the same limitation. Therefore GPT-6/maximum remains a requested prompt preference on this surface; this report truthfully records the actual model as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

The historical P26 `You cannot modify this task` event was authorization-context-specific. `RESULTS.md` records that a later authorized context successfully updated P26. The compliant remedy for a denied task is therefore the owning/authorized product/admin/API context or a platform permission/schema change, not a worker-side bypass. No scheduler or permission mutation was attempted here.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  full_source_status: PARTIAL

  frozen_target:
    graph: "H_{5,5}={5,5}"
    class: "regular co-regular plane tessellation"
    parameters: "degree 5, face degree 5"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    metric: "certified interval width U-L for Phi_V(H_{5,5})"
    before: 0
    after: 0
    exact_value: "sqrt(5)"
    unchanged_count: UNKNOWN
    status: "PROVED subclass / full source PARTIAL"

  source_clause_target:
    graph: "T=r{4,5}=M({4,5})"
    class: "4-regular vertex-transitive plane graph; face type [4,5,4,5]"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    lower_bound: "1/(sqrt(3)+sqrt(5)-2)"
    upper_before: "33178/38983"
    upper_after: "113708/133611"
    interval_width_before: 0.3429895229019940
    interval_width_after: 0.34293830065971065
    status: "PROVED PARTIAL / R06 self-check only"

  structural_progress:
    exact_relation: "r^5=q^5=(r q^{-1})^2=1 in exact Coxeter orbit representation"
    finite_anatomy: "only A=(1,0,3), B=(1,1,2), C=(2,0,2) through fully exposed layer 17"
    fraternal_profiles: "exact X/Y square-pentagon profiles through layer 16"
    recurrence_checked: "n=7..18 exact"
    all_generation_recurrence: "CONDITIONAL on FAL(4,5,4,5)"

  tried_moves: [18, 13, 30]
  remaining_obligation: "prove FAL(4,5,4,5), then return to exact isoperimetric optimization; full Question 6.20 remains open"

  evidence:
    idea_before_code: "artifacts/R06/20260920T0220Z_i0056_cayley_face_states_idea_78_6e2b.md"
    checker: "artifacts/R06/20260920T0220Z_i0056_face_state_exact_78_6e2b.py"
    checker_output: "artifacts/R06/20260920T0220Z_i0056_face_state_exact_78_6e2b.out"
    checker_verdict: "ALL_EXACT_CHECKS_PASS"
    prior_report: "runs/R06/20260920T0118Z_i0056_schreier_ball_growth_77_f3a1.md"
    prior_art_exclusion: "Haslegrave-Panagiotis DOI 10.1002/rsa.20946; triangular/quadrangular cases only"
    growth_method_prior_art:
      - "de Souza-da Silva, Ars Combinatoria 160 (2024), DOI 10.61091/ars-160-14"
      - "Floyd-Plotnick, Geometriae Dedicata 53 (1994), DOI 10.1007/BF01264041"

  audits:
    this_run: "none; R06 self-check only"
```
