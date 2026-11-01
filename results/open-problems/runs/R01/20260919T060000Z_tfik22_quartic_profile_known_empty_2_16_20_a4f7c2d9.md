Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. METRIC MOVEMENT: frozen Aldous–Fill I0024 remains `C=1`; active `R_TFIK22: 3 -> 2`, unchanged streak `1 -> 0`; status `OPEN / PARTIAL`; methods #2 ATTACK THE NEGATION FIRST, #16 COMPUTE EVERY SMALL CASE, #20 FIND WHY THE ALGORITHM FAILS.**

# R01 — the quartic `(11,0)` TFIK22 profile is already known empty

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity: I0024 remains frozen and is not reopened

I first recovered the original R01 state. Aldous–Fill Open Problem 3.44 was rechecked at the maintained source page on 2026-09-19:

https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S8.html

The frozen exact right-inverse characterization remains

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with the original fixed distortion metric

\[
\boxed{C=1}.
\]

The existing independent mathematical audits remain preserved:

- `R20-AUDIT-R01-I0024-03 = PASS`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

I0024 is not reopened. The old R01 FEI assignment remains retired; P03 owns FEI.

## 2. Active target recovered exactly

The active exclusive claim is

`operations/claims/KIM-MATTMAN-OH-2026-TFIK22-D34.md`,

source Hyoungjun Kim, Thomas W. Mattman, Seungsang Oh, **Four triangle-free intrinsically knotted graphs with 22 edges**, arXiv:2609.08891 (2026-09-08).

The current arXiv abstract was rechecked on 2026-09-19. It still says the 22-edge triangle-free IK classification is incomplete, that degree at least five has been handled, and that the 2026 paper classifies the degree profile with eight degree-4 and four degree-3 vertices, obtaining exactly four graphs.

The previous R01 arithmetic split used

\[
4n_4+3n_3=44
\]

to isolate

\[
(n_4,n_3)=(11,0),(8,4),(5,8),(2,12).
\]

The 2026 paper settles `(8,4)`. The R01 claim then treated the other three arithmetic profiles as still unresolved and froze

\[
R_{\rm TFIK22}=3.
\]

That inference was too broad. The source abstract says the **all-degree-3/4 regime** remains, but does not assert that every arithmetic profile inside it was previously open. This run recovers prior art that completely eliminates `(11,0)`. This is a **KNOWN-prior-art correction**, not a new intrinsic-knotting theorem or novelty claim.

Fresh exact-title, arXiv-ID, author/follow-up and profile searches dated 2026-09-19 found no later paper superseding arXiv:2609.08891. The negative search is bounded evidence only.

## 3. Idea before code

The previous run proposed enumerating the smallest profile `(11,0)` and then attacking each candidate by either a 21-edge IK-minor certificate or a 2-apex certificate.

Before writing more enumeration code I asked a more basic question:

> **Has the abstract graph class itself already been exhaustively enumerated, and did older spatial-graph work already decide the topology of those exact graphs?**

The answer is yes on both counts.

This turns the entire `(11,0)` branch into a two-source identification argument plus a small exact checker.

## 4. Method #16 — COMPUTE EVERY SMALL CASE: exactly two quartic candidates

A graph in profile `(11,0)` is a simple triangle-free 4-regular graph on 11 vertices, hence has 22 edges.

W. D. Wallis, **Triangle-Free Graphs**, JCMCC 74 (2010), pp. 217–221, explicitly cites Meringer's exhaustive regular-graph tables and states:

> Up to isomorphism there are precisely two triangle-free `(4,11)`-graphs.

The statement appears on p. 220, together with drawings of the two graphs.

Independently, Mattman–Pierce, **The K_{n+5} and K_{3^2,1^n} families are obstructions to n-apex**, arXiv:1603.00885 / 2017, report that their size-22 MMN2A search finds exactly two graphs outside the `K_{3,3,1,1}` family, both 4-regular on 11 vertices, and they print their edge lists. I used those two printed edge lists as `E1,E2` in the exact checker.

Executed artifact:

- `artifacts/R01/tfik22_quartic_profile_exact_checker_a4f7c2d9.py`
- `artifacts/R01/tfik22_quartic_profile_exact_checker_a4f7c2d9.out`

The checker verifies exactly:

- `E1,E2` each have 11 vertices and 22 edges;
- every vertex has degree 4;
- both are connected and triangle-free;
- `E1` has 24 four-cycles and `E2` has 22, hence they are nonisomorphic;
- neither is 2-apex;
- every immediate proper minor of each is 2-apex: all `22` edge deletions, `22` edge contractions and `11` vertex deletions, i.e. `55/55` for each graph.

The executed output ends

`ALL_EXACT_TFIK22_QUARTIC_CHECKS_PASS`.

Because Wallis/Meringer give exactly two isomorphism classes and these two explicit nonisomorphic graphs are both triangle-free `(4,11)`-graphs, they exhaust the entire `(11,0)` profile.

This checker is a **self-check**, not an independent audit. NetworkX `check_planarity` is a finite combinatorial planarity algorithm; no floating-point tolerance enters these claims.

## 5. Method #2 — ATTACK THE NEGATION FIRST: both exhaustive candidates have knotless embeddings

The decisive prior-art fact is in Hyoungjun Kim and Thomas W. Mattman, **Dips at small sizes for topological graph obstruction sets**, arXiv:2205.14255v2 (2024), published in *Discrete Applied Mathematics* 360 (2025), 139–166.

In Section 3 they denote by `H_1,H_2` **the two 4-regular, 11-vertex, 22-edge graphs described in the Mattman–Pierce paper**. They state that neither is 2-apex but that both are **not intrinsically knotted**, and Figure 2 gives explicit knotless embeddings of both. Their text says, in particular, that these graphs are not IK, let alone MMIK.

This exactly answers the two graphs found above. Therefore:

### Proposition — complete `(11,0)` classification

There is **no** triangle-free intrinsically knotted simple graph with 22 edges and degree profile

\[
(n_4,n_3)=(11,0).
\]

### Proof

Let `G` be such a graph. Then `G` is a triangle-free 4-regular graph on 11 vertices. Wallis/Meringer prove that there are exactly two such graphs up to isomorphism. Mattman–Pierce list two nonisomorphic 4-regular 11-vertex size-22 graphs `H_1,H_2`; the exact checker verifies both are triangle-free, so they realize the two exhaustive Wallis classes. Kim–Mattman give knotless embeddings of `H_1,H_2`, hence both are nIK. Thus `G` is nIK. QED.

This proposition is **KNOWN from the cited prior art plus exact graph identification**. R01 does not claim it as a new mathematical result.

### Correction of the previous R01 report

The previous report said the known Schwartz graph `G_S` made `(11,0)` nonempty. That statement was wrong: it silently treated “4-regular on 11 vertices with 22 edges” as implying triangle-free. The argument above shows the opposite. Since `G_S` is IK whereas both triangle-free `(4,11)` graphs are nIK, `G_S` cannot be triangle-free. The previous nonemptiness statement is withdrawn.

## 6. Method #20 — FIND WHY THE ALGORITHM FAILS: the failure is universal, and prior art supplies the missing topology

The previous certificate architecture was:

- positive: find a known 21-edge IK minor;
- negative: find a 2-apex witness.

The exact checker shows **both channels fail for both exhaustive `(11,0)` candidates**:

1. Neither `H_1` nor `H_2` is 2-apex.
2. Every immediate proper minor is 2-apex.
3. Since the class of 2-apex graphs is minor-closed, every proper minor is 2-apex and therefore nIK.

Consequently, neither graph can have a 21-edge IK minor. If either graph had been IK, it would automatically have been a new 22-edge MMIK graph. Thus the algorithmic survivor set is exactly the full two-graph profile.

This is the precise reason the simple minor/2-apex certificate algorithm stalls. What it lacks is **direct spatial topology**. Kim–Mattman supply exactly that missing ingredient via explicit knotless embeddings, discharging both survivors negatively.

This is a useful methodological lesson for the remaining profiles: after minor and 2-apex filtering, do not keep manufacturing graph-enumeration certificates for the survivors; look immediately for knotless-embedding / restoring-method structure or a published spatial embedding.

## 7. Fixed-metric movement

The frozen successor metric was

`R_TFIK22 := number of the three claimed degree profiles whose complete triangle-free 22-edge IK classification is still unresolved by a source-valid exact proof`.

At start of run:

\[
R_{\rm TFIK22}=3.
\]

The profile `(11,0)` is now completely discharged as **KNOWN EMPTY / no IK graphs**. Therefore

\[
\boxed{R_{\rm TFIK22}:3\longrightarrow2.}
\]

The remaining exact profiles are

\[
\boxed{(n_4,n_3)=(5,8)\quad\text{and}\quad(2,12).}
\]

Because the fixed metric moved, the supported unchanged streak resets from `1` to `0`. Overall target status remains `OPEN / PARTIAL`.

This movement is primarily a **prior-art/source-scope correction**, not a claim that R01 newly solved a topology theorem.

## 8. Current prior-art map

Checked / used on 2026-09-19:

1. Aldous–Fill OP3.44 maintained source page — frozen original R01 source only.
2. Kim–Mattman–Oh, arXiv:2609.08891 (2026-09-08) — active external source; `(8,4)` classified, all-degree-3/4 residue remains in the source framing.
3. Wallis, JCMCC 74 (2010), p. 220 — exactly two triangle-free `(4,11)` graphs up to isomorphism, from Meringer's exhaustive regular-graph census.
4. Mattman–Pierce, arXiv:1603.00885 / 2017 — exact two 4-regular 11-vertex size-22 MMN2A graphs and their edge lists.
5. Kim–Mattman, arXiv:2205.14255v2 / *Discrete Applied Mathematics* 360 (2025) — identifies those two graphs as `H_1,H_2`, gives knotless embeddings, and states both are nIK.
6. Flapan–Mattman–Mellor–Naimi–Nikkuni survey (2017) — background: IK implies not 2-apex, 21-edge IK classification, and historical 22-edge MMIK census. It is not needed for the decisive nIK step once the 2025 paper is used.

Access note: Wallis was checked from the journal PDF page showing the exact two-class statement. The arXiv 2205.14255 HTML/full-text was accessible and includes the `H_1,H_2` nIK statement. A bounded 2026-09-19 current-title/author search found no later completion of the 2026 target. No negative search is promoted to a worldwide novelty certificate.

## 9. Next research route

Do **not** re-enumerate `(11,0)`. It is closed as KNOWN negative.

The next run should attack `(5,8)` first (`n=13`), because it is the smaller of the two true remaining arithmetic profiles. Fresh methods, not repeating this run:

- **#22 READ THE FAILURES, NOT THE SUCCESSES:** read the proof architecture and case failures in the 2014/2018/2026 triangle-free IK papers, especially exactly where pair-deletion/restoring arguments stop when there are five degree-4 and eight degree-3 vertices.
- **#25 COUNT THE SAME THING TWICE:** count candidate pair-deletion structures both from degree incidence and from the restored planar/nonplanar minors; seek an invariant forcing a finite short list without enumerating every labeled graph.
- **#30 ONE SCALE / ONE DIRECTION AT A TIME:** split `(5,8)` by the induced subgraph on the five degree-4 vertices (edge count and degree sequence), solve each feasible induced type separately, and identify the first type that cannot be discharged by the restoring method.

If those structural attacks produce a finite survivor set, only then build the next checker.

No independent audit is requested: the active package remains incomplete and two profiles remain.

## 10. Structured ledger_delta

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
    before: 3
    after: 2
    status: OPEN_PARTIAL
    unchanged_count_before: 1
    unchanged_count_after: 0
    movement_type: PRIOR_ART_SCOPE_CORRECTION
    profile_closed_this_run:
      profile: [11, 0]
      verdict: KNOWN_EMPTY_NO_IK
      proof_basis:
        - Wallis/Meringer exhaustive two-class theorem
        - Mattman-Pierce explicit two representatives
        - Kim-Mattman knotless embeddings of H1,H2
        - R01 exact graph/property/MMN2A self-check
    remaining_profiles:
      - [5, 8]
      - [2, 12]
    tried_moves: [2, 16, 20]
    next_moves: [22, 25, 30]
    evidence:
      - artifacts/R01/tfik22_quartic_profile_exact_checker_a4f7c2d9.py
      - artifacts/R01/tfik22_quartic_profile_exact_checker_a4f7c2d9.out
    active_audit_ids: []
    remaining_obligation: >-
      Classify all triangle-free 22-edge IK graphs in the two remaining
      profiles (5,8) and (2,12), with complete positive/negative coverage.
```

## 11. Model / scheduler-control truth

The operative repository implementation record remains `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`. It records that the exposed scheduler surface has **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed hour-long execution setting**. Therefore the prompt request `GPT-6 / maximum` is not enforceable on this surface.

This run actually identifies as **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The historical P26 `You cannot modify this task` was an authorization-context boundary; the same repository record notes later successful modification in an authorized context. A binding model/reasoning change requires an owning/authorized product/workspace/API/admin surface or a platform feature exposing those fields. No permission bypass, scheduler change, task duplication, email, Drive action, or public posting was attempted in this run.
