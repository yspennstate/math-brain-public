Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. METRIC MOVEMENT: frozen Aldous–Fill I0024 remains `C=1`; active `R_TFIK22: 1 -> 0`, unchanged streak `0 -> 0`; mathematical package `CANDIDATE COMPLETE / AUDITS PENDING`, not operationally closed; methods #14 FIND THE GROUP ACTING, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #24 FIND THE EXTREMAL OBJECT.**

# R01 — final `(n4,n3)=(2,12)` profile and completion of the claimed TFIK22 residue

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and scope recovery

I reread the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the operative implementation record, the active exclusive claim, the newest R01 report, and current neighboring ownership/status material before doing new mathematics.

The original R01 source, Aldous–Fill Open Problem 3.44 / intake I0024, remains frozen and is **not reopened**. Its retained exact characterization is

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with fixed distortion metric

\[
\boxed{C=1}.
\]

The existing independent mathematical audits remain preserved:

- `R20-AUDIT-R01-I0024-03 = PASS`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

The active exclusive successor is `KIM-MATTMAN-OH-2026-TFIK22-D34`, based on H. Kim, T. W. Mattman and S. Oh, *Four triangle-free intrinsically knotted graphs with 22 edges*, arXiv:2609.08891 (submitted 2026-09-08). The source still states that the 22-edge triangle-free IK classification is incomplete and settles the all-degree-3/4 profile `(n4,n3)=(8,4)`, finding four graphs.

The exclusive R01 claim freezes the remaining three arithmetic profiles

\[
(11,0),\qquad(5,8),\qquad(2,12)
\]

under the metric `R_TFIK22`, the number not yet completely classified. The preceding runs recovered `(11,0)` as already known empty and proved `(5,8)` has exactly four IK isomorphism classes. Thus this run starts from

\[
R_{\rm TFIK22}=1
\]

with only `(2,12)` unresolved.

## 2. Main theorem of this run

### Theorem

Up to graph isomorphism, there are exactly **three** triangle-free intrinsically knotted simple graphs with 22 edges and degree profile

\[
\boxed{(n_4,n_3)=(2,12).}
\]

Every other triangle-free simple graph with 22 edges and this degree profile is 2-apex and hence is not intrinsically knotted.

Representatives on vertices `0,...,13` are:

### Class A — `C14 + e`

```text
((0,7),(0,8),(0,9),(0,10),(1,7),(1,10),(1,11),(2,7),(2,12),(2,13),
 (3,8),(3,10),(3,12),(4,8),(4,11),(4,13),(5,9),(5,10),(5,13),
 (6,9),(6,11),(6,12))
```

Deleting edge `(0,10)` gives the 21-edge Heawood graph `C14`, hence Class A is IK.

### Class B — split of the unique order-13 pure-`Delta Y` descendant of `K7`

```text
((0,6),(0,7),(0,8),(1,6),(1,9),(1,10),(2,7),(2,9),(2,11),(3,4),
 (3,7),(3,10),(3,12),(4,8),(4,9),(4,13),(5,8),(5,10),(5,11),
 (6,12),(11,13),(12,13))
```

Contracting edge `(12,13)` gives the unique 13-vertex member of the pure-`Delta Y` `K7` family. That 21-edge graph is IK, hence Class B is IK.

### Class C — unique order-14 member of the `K_{3,3,1,1}` family

```text
((0,5),(0,8),(0,9),(1,4),(1,10),(1,11),(2,3),(2,12),(2,13),(3,8),
 (3,10),(4,9),(4,12),(5,11),(5,13),(6,7),(6,8),(6,11),(6,12),
 (7,9),(7,10),(7,13))
```

The exact family generator produces the full 58-member `Delta Y / Y Delta` family of `K_{3,3,1,1}` and finds exactly one order-14 member, isomorphic to Class C. Published work proves every member of that 58-graph family is MMIK, hence Class C is IK.

The three representatives are pairwise nonisomorphic.

## 3. Method #14 — quotient by the two degree-4 vertices

Let `a,b` be the two degree-4 vertices and put

\[
H=G-\{a,b\}.
\]

Because all other twelve vertices have degree 3, the entire problem can be quotiented by the relation of a degree-3 vertex to `a` and `b`.

There are two main cases.

### Case I: `ab` is not an edge

Put

\[
t=|N(a)\cap N(b)|.
\]

Among the twelve vertices of `H` there are then:

- `t` common neighbors of `a,b`, each of degree 1 in `H`;
- `4-t` neighbors of `a` only and `4-t` neighbors of `b` only, each of degree 2 in `H`;
- `4+t` vertices adjacent to neither `a` nor `b`, each of degree 3 in `H`.

Thus

\[
\deg_H:\qquad 1^t,\quad 2^{8-2t},\quad 3^{4+t},
\qquad |E(H)|=14.
\]

Triangle-freeness gives a crucial local restriction: a common neighbor of `a,b` can have its one `H`-neighbor only among the `4+t` vertices adjacent to neither high-degree vertex. It cannot be adjacent in `H` to any vertex sharing `a` or `b`, because that would create a triangle through that high-degree vertex.

### Case II: `ab` is an edge

Triangle-freeness forces `N(a)\setminus\{b\}` and `N(b)\setminus\{a\}` to be disjoint. Call their vertices red and blue respectively. There are three red and three blue vertices, all of degree 2 in `H`, and the remaining six vertices have degree 3 in `H`. Hence

\[
\deg_H=2^6 3^6,
\qquad |E(H)|=15.
\]

An `H`-edge cannot join two red vertices or two blue vertices, since either would make a triangle with `a` or `b`.

This quotient eliminates arbitrary 14-vertex graph generation. What remains is a small colored subdivision problem.

## 4. Method #24 — the extremal object is a subdivision of `K_{3,3}`

The key structural lemma is elementary but decisive.

### Lemma 1 — subcubic Kuratowski reduction

If a graph `H` with maximum degree at most 3 is nonplanar, then `H` contains a subdivision of `K_{3,3}`.

### Proof

By Kuratowski, `H` contains a subdivision of `K_5` or `K_{3,3}`. A subdivision of `K_5` has five branch vertices of degree at least 4 in the ambient graph, impossible when `Delta(H)<=3`. Therefore the obstruction is a subdivision of `K_{3,3}`. `□`

Moreover, every branch vertex of such a subdivision has degree exactly 3 in `H`, so all three of its incident `H`-edges are used by the subdivision. In particular branch vertices are saturated: no edge can leave the subdivision at a branch vertex.

This turns planarity of `H` into a complete structural dichotomy.

## 5. Nonadjacent high-degree vertices imply 2-apex

Assume `ab` is not an edge. If `H` is planar then `{a,b}` itself is a 2-apex certificate, so suppose `H` is nonplanar and fix a `K_{3,3}` subdivision `S` from Lemma 1.

The six branch vertices of `S` must be degree-3 vertices of `H`, hence must come from the `4+t` vertices adjacent to neither `a` nor `b`. Therefore `t>=2`.

### `t=2` is impossible

There are exactly six degree-3 vertices, so all six are saturated branch vertices of `S`. But each of the two common neighbors has degree 1 in `H` and, by triangle-freeness, can be adjacent only to one of those six degree-3 vertices. No branch vertex has a free incident edge. Contradiction.

Hence `H` is planar for `t=2`.

### `t=3`: exactly three finite orbit types, all 2-apex

There are seven degree-3 vertices. Six are saturated branch vertices of `S`; call the seventh `u`. All three common-neighbor leaves can only attach to a degree-3 vertex not saturated by `S`, hence all three attach to `u`, using all of its degree. Thus `u` together with the three common neighbors is a separate `K_{1,3}` component.

The remaining two degree-2 vertices are one `a`-only and one `b`-only vertex. Both must lie internally on edges of the `K_{3,3}` subdivision. Up to automorphisms of `K_{3,3}` and swapping `a,b`, there are exactly three possibilities:

1. both subdivisions on the same base edge;
2. subdivisions on two distinct incident base edges;
3. subdivisions on two distinct disjoint base edges.

The exact checker generates all 90 raw colored placements, quotients them to exactly three graph-isomorphism classes, and finds an explicit 2-apex pair for every one. Thus no `t=3` graph is IK.

### `t=4`: exactly two finite structural forms, both 2-apex

There are eight degree-3 vertices: six saturated branch vertices of `S` and two extra vertices `u,v`. The four common-neighbor leaves can attach only to `u,v`.

There are only two ways to use the six available degree slots of `u,v`:

1. neither lies internally on `S`; then `uv` is an edge and each receives exactly two common-neighbor leaves (a double-star component disjoint from a bare `K_{3,3}` component);
2. one, say `u`, lies internally on one edge of `S`, using two of its incident edges, and receives one common-neighbor leaf; the other `v` is outside `S` and receives the remaining three leaves.

Both forms are checked exactly and are 2-apex.

Therefore every graph in the profile with nonadjacent degree-4 vertices is 2-apex and not IK.

## 6. Adjacent high-degree vertices: exhaustive colored `K_{3,3}` subdivision

Now suppose `ab` is an edge. In `H` there are exactly six degree-3 vertices and six degree-2 vertices, three red and three blue.

If `H` is planar, `{a,b}` is again a 2-apex certificate. If `H` is nonplanar, Lemma 1 gives a `K_{3,3}` subdivision `S`. Since there are exactly six degree-3 vertices, all six are the branch vertices of `S` and are saturated.

Every red/blue degree-2 vertex is therefore either:

- an internal subdivision vertex on an edge of `S`; or
- in a separate component consisting entirely of degree-2 vertices, hence a cycle.

There are only six such vertices. Triangle-freeness forbids red-red and blue-blue edges, so any outside cycle must alternate colors and therefore has even length. A triangle-free outside cycle can consequently have only length 4 or 6; two outside cycles are impossible because each would require at least four vertices.

This gives exactly three exhaustive structural cases.

### 6.1 Connected case: all six colored vertices subdivide `K_{3,3}`

Fix the nine base edges of `K_{3,3}`. On each edge, its internal colored vertices must form an alternating word in `R,B`; globally there must be exactly three `R` and three `B` symbols.

There are exactly

\[
\boxed{22,530}
\]

such color-word placements. The exact checker constructs every one, restores the two high-degree vertices and all six high-incidence edges, and tests every vertex pair for a planar deletion.

The outcome is

\[
22,470\text{ placements are 2-apex},
\]

while

\[
60\text{ raw placements are non-2-apex}.
\]

Exact graph-isomorphism quotienting collapses those 60 placements to precisely

\[
\boxed{3\text{ non-2-apex isomorphism classes}.}
\]

### 6.2 One outside 4-cycle

The alternating 4-cycle uses two red and two blue vertices; the remaining one red and one blue vertex subdivide the `K_{3,3}` component. There are 90 raw core placements, collapsing to three isomorphism classes. Every one is 2-apex.

### 6.3 One outside 6-cycle

All six colored vertices form the alternating 6-cycle, leaving a bare `K_{3,3}` component. The resulting graph is 2-apex (and in fact the `K_{3,3}` component is disconnected from the high-degree gadget).

Thus the complete profile has at most three IK isomorphism classes, namely the three non-2-apex survivors of the connected case.

## 7. Method #17 — identify all three survivors in known IK families/minors

The finite calculation above only says that three classes survive the negative 2-apex certificate. It does not infer IK merely from non-2-apex. Positive certificates are independent.

### Survivor 1: `C14 + e`

The checker independently generates the pure `Delta Y` descendants of `K7`. There are 14, agreeing with the published 21-edge IK classification. There is a unique order-14 member, the Heawood graph `C14`.

Adding one edge to `C14` subject to triangle-freeness and target degree profile gives exactly one isomorphism class. It is Class A above. Deleting the added edge recovers `C14`, so Class A has an IK minor and is IK.

### Survivor 2: a split of the unique order-13 21-edge IK graph

The same pure-`Delta Y` generation has a unique order-13 member, with degree sequence `3^10 4^3`. Split one degree-4 vertex into two adjacent degree-3 vertices, partitioning its four old incident edges as `2+2`. Among all such splits, the triangle-free target-profile outcomes form exactly one isomorphism class. It is Class B.

In the representative above, contracting `(12,13)` recovers the 21-edge order-13 IK graph. Hence Class B is IK.

### Survivor 3: the order-14 `K_{3,3,1,1}` cousin

An independent exact `Delta Y / Y Delta` closure starting from `K_{3,3,1,1}` generates exactly 58 isomorphism classes, agreeing with the published family size. Exactly one has order 14, and it has the target profile and is triangle-free. It is Class C.

Goldberg–Mattman–Naimi prove all 58 graphs in this family are IK, in fact MMIK. Hence Class C is IK.

Finally, the exact isomorphism match matrix between the three non-2-apex survivors of Section 6.1 and these three independently generated positive certificates is the identity:

```text
((True,False,False),
 (False,True,False),
 (False,False,True))
```

So there are neither missing positive candidates nor non-2-apex false positives.

This proves the theorem.

## 8. Exact self-check and archived output

New artifacts:

- `artifacts/R01/tfik22_profile_2_12_exact_structural_checker_20260919.py`
  - creation commit `83d7df7c1f91347d586e074e9288b3bba6b7e960`;
- `artifacts/R01/tfik22_profile_2_12_exact_structural_checker_20260919.out`
  - creation commit `fcda3761990ee9c9deb50980abfd97660e5721bb`.

The executed output records:

```text
X0_T3_RAW 90 ISO_CLASSES 3 ALL_2APEX True
X0_T4_FORMS 2 ALL_2APEX True
X1_CONNECTED_WORDS 22530 TWO_APEX 22470 NON2_RAW 60 NON2_ISO 3
X1_C4_RAW 90 ISO_CLASSES 3 ALL_2APEX True
X1_C6_ALL_2APEX True
POSITIVE_MATCH_MATRIX ((True, False, False), (False, True, False), (False, False, True))
K7_PURE_DY_SIZE 14 K3311_FULL_FAMILY_SIZE 58
FINAL_PROFILE_IK_ISO_CLASSES 3
ALL_EXACT_TFIK22_2_12_CHECKS_PASS
```

The checker uses only integer/combinatorial graph operations. NetworkX planarity is used as an exact combinatorial planarity algorithm. This is explicitly a **self-check**, not an independent audit.

## 9. Completion of the three-profile R01 claim

The R01 claimed residue is now:

| Profile | Result | Evidence |
|---|---|---|
| `(11,0)` | no triangle-free IK graph | prior-art recovery plus exact two-graph check in preceding R01 run |
| `(5,8)` | exactly four IK isomorphism classes | complete exact R01 classification, preceding run |
| `(2,12)` | exactly three IK isomorphism classes | theorem and exact checker in this run |

Therefore the fixed metric moves

\[
\boxed{R_{\rm TFIK22}:1\longrightarrow0.}
\]

Combining these with Kim–Mattman–Oh's published `(8,4)` theorem yields, at the mathematical-claim level, the complete all-degree-3/4 triangle-free 22-edge classification:

\[
0+4+4+3=\boxed{11}
\]

IK isomorphism classes across the four arithmetic profiles.

This is **not yet called operationally closed**. The fleet closure rule still requires the complete package to receive two independent full-proof audits from other tasks, one normally from P26 and one from a distinct track. No self-check is counted as an audit.

## 10. Prior-art and current-status screen, dated 2026-09-19

I checked the current source and follow-up literature before promoting the metric.

Queries included:

- exact title and arXiv ID `2609.08891`;
- author/follow-up searches for Kim, Mattman and Oh;
- `triangle-free intrinsically knotted 22 edges 2 12`;
- `two vertices degree 4 intrinsically knotted`;
- `twelve vertices degree 3 intrinsically knotted`;
- `14 vertices 22 edges triangle-free intrinsically knotted`;
- `K_{3,3,1,1} family 58 MMIK`;
- the 21-edge `K7` / Heawood classification and older 22-edge papers.

Primary / near-primary sources checked include:

1. Kim–Mattman–Oh, arXiv:2609.08891 (2026), the active source; its abstract still says the 22-edge classification is incomplete and settles only `(8,4)` in the all-degree-3/4 branch.
2. Kim–Mattman–Oh, *Bipartite intrinsically knotted graphs with 22 edges* (2014), which records the complete 21-edge IK family context and the Heawood graph.
3. Kim–Lee–Lee–Mattman–Oh, *A new intrinsically knotted graph with 22 edges* (2017), for the earlier high-degree branch.
4. Kim–Mattman–Oh, *More intrinsically knotted graphs with 22 edges and the restoring method* (2018), for the single-degree-5 branch.
5. Goldberg–Mattman–Naimi, *Many, many more intrinsically knotted graphs* (2014), which proves all 58 `K_{3,3,1,1}` family graphs IK/MMIK and all 110 `E9+e` family graphs IK.

The current source was submitted only eleven days ago. I found no later primary source explicitly classifying either `(5,8)` or `(2,12)`, and no source matching the exact complete three-profile classification above. This is bounded dated negative evidence, **not** a worldwide novelty or priority certificate.

I make no claim that the seven positive graphs found in the `(5,8)` and `(2,12)` profiles are themselves newly discovered abstract graphs. Indeed the positive certificates intentionally place them in known IK families or above known 21-edge IK minors. The candidate novelty is the **complete classification proof for the previously unresolved degree profiles**, if independent audit and a stronger priority search uphold it.

## 11. Why the three fresh methods mattered

- **#14 FIND THE GROUP ACTING.** Quotienting by the two degree-4 vertices reduces twelve low-degree vertices to four adjacency types and, in the adjacent case, to three red and three blue subdivision vertices. `Aut(K_{3,3})` and the high-vertex swap collapse the problem from arbitrary 14-vertex graphs to colored subdivisions.
- **#24 FIND THE EXTREMAL OBJECT.** Kuratowski plus `Delta(H)<=3` forces every nonplanar deletion core to contain a `K_{3,3}` subdivision. Degree saturation then determines every possible nonplanar structural form; this is the theorem-producing reduction, not the checker.
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.** The three non-2-apex survivors match exactly the 14-member pure-`Delta Y` `K7` family / its 21-edge minors and the 58-member `K_{3,3,1,1}` family. This supplies positive IK certificates without inventing new spatial-embedding arguments.

## 12. Audit readiness and remaining obligation

The mathematics of the exclusive source claim is now candidate-complete. The only remaining closure obligations are external validation and packaging:

1. P26 independent end-to-end audit of the three-profile package, including rerunning the `(5,8)` and `(2,12)` finite cores and checking the structural exhaustion arguments;
2. a second independent audit by a different track;
3. reconcile any audit corrections;
4. only after two PASS audits, write the source-matching `paper_<name>/` folder and mark the claim closed.

No audit is counted in this report. No paper folder is created prematurely.

## 13. Structured `ledger_delta`

```yaml
ledger_delta:
  worker: R01
  frozen_source:
    id: I0024
    source: Aldous-Fill Open Problem 3.44
    metric: C
    before: 1
    after: 1
    status: FROZEN_NOT_REOPENED
    audits:
      - R20-AUDIT-R01-I0024-03
      - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
  active_source:
    id: KIM-MATTMAN-OH-2026-TFIK22-D34
    source: Kim-Mattman-Oh, arXiv:2609.08891
    metric: R_TFIK22
    before: 1
    after: 0
    status: CANDIDATE_COMPLETE_AUDITS_PENDING
    unchanged_count_before: 0
    unchanged_count_after: 0
    movement_type: COMPLETE_FINAL_PROFILE_CLASSIFICATION
    profile_closed_this_run:
      profile: [2, 12]
      verdict: EXACTLY_THREE_IK_ISOMORPHISM_CLASSES
    completed_profiles:
      - profile: [11, 0]
        verdict: ZERO_IK_KNOWN_PRIOR_ART
      - profile: [5, 8]
        verdict: EXACTLY_FOUR_IK_ISOMORPHISM_CLASSES
      - profile: [2, 12]
        verdict: EXACTLY_THREE_IK_ISOMORPHISM_CLASSES
    tried_moves: [14, 17, 24]
    evidence:
      - path: artifacts/R01/tfik22_profile_2_12_exact_structural_checker_20260919.py
        commit: 83d7df7c1f91347d586e074e9288b3bba6b7e960
      - path: artifacts/R01/tfik22_profile_2_12_exact_structural_checker_20260919.out
        commit: fcda3761990ee9c9deb50980abfd97660e5721bb
      - path: runs/R01/20260919T083031Z_tfik22_profile_5_8_exact_four_22_25_30_f3a71c82.md
        role: previous_complete_profile
      - path: runs/R01/20260919T060000Z_tfik22_quartic_profile_known_empty_2_16_20_a4f7c2d9.md
        role: previous_known_empty_profile
    active_audit_ids: []
    remaining_obligation: >-
      Obtain two independent full-proof audits from OTHER tasks (P26 plus one
      distinct track), reconcile corrections, and only then package and mark
      the source claim operationally closed.
```

## 14. Model / scheduler-control truth

The operative implementation record remains `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`. It states that the exposed scheduler surface has **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed hour-long execution setting**. The runtime surface available to this run likewise exposes schedule/prompt/enablement controls but no model or reasoning field.

Therefore `GPT-6 / maximum` remains a prompt request rather than an enforceable scheduler setting on this surface. This run actually identifies as **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The historical P26 `You cannot modify this task` was an authorization-context boundary. Repository evidence records later successful modification from an authorized context; the lawful workaround is an owning/authorized product/workspace/API/admin surface or platform support, not a permission bypass. No scheduler change, permission change, task duplication, email, Drive action, purchase, or public posting was attempted in this run.
