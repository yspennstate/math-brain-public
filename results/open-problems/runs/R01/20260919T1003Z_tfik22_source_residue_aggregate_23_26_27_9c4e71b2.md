Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT: frozen Aldous–Fill I0024 remains `C=1`; active successor `R_TFIK22=0 -> 0`; status `CANDIDATE COMPLETE / AUDITS PENDING`; methods #23 DO WHAT THE PROPOSER DID NOT EXPECT, #26 HUNT THE SPORADIC CASE, #27 SWAP THE QUANTIFIERS.**

# R01 — source-residue aggregation and prior-art stress test after `R_TFIK22=0`

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Run date: 2026-09-19.

## 1. Continuity: do not reopen I0024

I reread the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current follow-up implementation manifest, the active exclusive claim, the newest complete R01 report and complete-package audit handoff, and repository-wide current ownership/audit evidence before doing new work. I also searched the intake/repository corpus for the exact successor arXiv ID; it occurs only in the manually admitted successor claim/reports and neighboring admission records, not as a pre-existing intake ownership conflict.

The original R01 source, Aldous–Fill Open Problem 3.44 / I0024, remains frozen and is **not reopened**. Its retained exact characterization is

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad R_*=CB^TL^+,
\]

with fixed optimal distortion

\[
\boxed{C=1}.
\]

The existing independent audits remain:

- `R20-AUDIT-R01-I0024-03 = PASS`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

The active exclusive successor remains `KIM-MATTMAN-OH-2026-TFIK22-D34`, based on H. Kim, T. W. Mattman and S. Oh, *Four triangle-free intrinsically knotted graphs with 22 edges*, arXiv:2609.08891 (submitted 2026-09-08). Its frozen source-valid metric is

`R_TFIK22 := number of the three claimed unresolved degree profiles (11,0),(5,8),(2,12) not completely classified.`

The preceding R01 runs established

- `(11,0)`: 0 IK classes (known prior-art exhaustion),
- `(5,8)`: exactly 4 IK classes,
- `(2,12)`: exactly 3 IK classes,

while the source itself proves `(8,4)`: exactly 4 IK classes. Thus `R_TFIK22=0` remains unchanged. The package handoff at `artifacts/R01/tfik22_complete_audit_handoff_20260919.md` is already present, so I did not manufacture another audit request.

Repository-wide searches at run time found **no independent OTHER-track TFIK22 audit yet**. The newest visible P26 audit work is on R06/Romero packages, not this one. Therefore the successor remains candidate-complete rather than closed.

## 2. Fresh source and prior-art check, dated 2026-09-19

Primary source: https://arxiv.org/abs/2609.08891 . The live abstract still says that the 22-edge triangle-free IK classification remains incomplete, that the previously settled high-degree part consists of exactly eight examples with a vertex of degree at least 5, and that the only remaining source case is when every vertex has degree 3 or 4. It then settles only `(n4,n3)=(8,4)`, finding Cousins 43, 105, 109 of the `E9+e` family and `H12+e`.

I also rechecked the two predecessor classification papers that make the source's number eight exact rather than heuristic:

1. H. Kim, H. J. Lee, M. Lee, T. Mattman, S. Oh, *A new intrinsically knotted graph with 22 edges*, Topology Appl. 228 (2017), 303–317, DOI 10.1016/j.topol.2017.06.013. It proves exactly three triangle-free 22-edge IK graphs having at least two degree-5 vertices and no triangle-free 22-edge IK graph having a vertex of degree greater than 5.
2. H. Kim, T. Mattman, S. Oh, *More intrinsically knotted graphs with 22 edges and the restoring method*, J. Knot Theory Ramifications 27 (2018), 1850059, DOI 10.1142/S0218216518500591. It proves exactly five triangle-free 22-edge IK graphs having exactly one degree-5 vertex: Cousin 29 of the `K_{3,3,1,1}` family, Cousins 97 and 99 of the `E9+e` family, and two previously unknown examples.

Exact-title, exact arXiv-ID, author/follow-up, degree-profile, and `triangle-free intrinsically knotted 22 edges` searches dated 2026-09-19 found the September 8 source and these older classification papers but no later primary paper completing the three profiles claimed by R01. This remains bounded negative evidence, not a worldwide novelty/priority certificate.

Important scope qualification: the older classification machinery explicitly reduces to graphs of minimum degree at least 3; degree-1/2 non-minimal extensions/subdivisions are not silently promoted into the claimed source residue. The exclusive claim therefore remains exactly the all-degree-3/4 residue stated in `operations/claims/KIM-MATTMAN-OH-2026-TFIK22-D34.md`.

## 3. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: aggregate the whole reduced source classification

The September source is organized profile-by-profile. Once the R01 three-profile package is candidate-complete, there is a stronger and cleaner statement in the **source's standard reduced minimum-degree-3 scope**.

The prior high-degree classifications contribute exactly

\[
3+5=8
\]

triangle-free IK classes with a degree-5 vertex, and none with degree greater than 5.

The all-degree-3/4 part has the degree equation

\[
4n_4+3n_3=44,
\]

whose four nonnegative solutions are

\[
(11,0),\ (8,4),\ (5,8),\ (2,12).
\]

The exact class counts now available in those four profiles are respectively

\[
0,\quad4,\quad4,\quad3.
\]

Hence the entire all-degree-3/4 residue contains exactly

\[
\boxed{0+4+4+3=11}
\]

IK isomorphism classes, and the standard reduced triangle-free 22-edge classification (`\delta(G)\ge3`) contains exactly

\[
\boxed{8+11=19}
\]

classes.

This `19` is not a new independent enumeration and does not enlarge the exclusive claim. It is a source-level synthesis: the eight high-degree cases are published prior art, the `(8,4)` four are the September source, and R01 supplies the candidate-complete remaining 0+4+3. The new value of this formulation is that it makes explicit what closing the three R01 profiles would complete globally **within the source's reduced scope**.

I do **not** claim that this counts every non-minimal triangle-free 22-edge IK graph obtainable by inserting degree-2 vertices or other trivial extensions. The claim/source framework is the minimum-degree-3 reduced classification used by this literature.

## 4. Method #26 — HUNT THE SPORADIC CASE: no hidden high-degree branch remains

The most dangerous gap in the aggregate statement would be a sporadic degree pattern outside both the published degree-5 cases and the all-degree-3/4 equation.

The predecessor papers rule this out in the reduced scope:

- maximum degree `>=6`: no triangle-free 22-edge IK graph;
- maximum degree `=5` with at least two degree-5 vertices: exactly 3;
- maximum degree `=5` with exactly one degree-5 vertex: exactly 5;
- maximum degree `<=4` and minimum degree `>=3`: every vertex is degree 3 or 4, so `4n4+3n3=44` forces exactly the four profiles above.

Thus the aggregate count has no unclassified degree-pattern bucket hiding between the older papers and the September source.

This is the principal prior-art reconciliation gained in this run: the R01 package is not merely three isolated finite exercises. If both independent audits pass, it completes the degree-pattern partition explicitly left open by the September 2026 source.

## 5. Method #27 — SWAP THE QUANTIFIERS: replace four case statements by one theorem

The profile-by-profile output can be stated equivalently as one source-residue theorem:

> **Candidate theorem (audit pending).** Let `G` be a triangle-free intrinsically knotted simple graph with 22 edges in the source's reduced minimum-degree-3 scope. Then exactly one of the following holds:
> 1. `G` belongs to one of the eight previously classified degree-5 classes;
> 2. `deg(G)=4^8 3^4`, and `G` is one of the four Kim–Mattman–Oh classes;
> 3. `deg(G)=4^5 3^8`, and `G` is one of the four R01 classes;
> 4. `deg(G)=4^2 3^12`, and `G` is one of the three R01 classes.
>
> There is no class with `deg(G)=4^11`, and no further degree pattern occurs.

Equivalently, there are exactly 19 classes in that reduced scope, of which 11 have all degrees in `{3,4}`.

This formulation is preferable for a final paper because it says precisely what is completed by combining the new profile arguments with the already-published classification chain. It should remain labeled **candidate theorem / audit pending** until two independent OTHER-track audits pass.

## 6. What did not work / what remains

There was no mathematical obstruction left to attack inside the frozen metric: `R_TFIK22` was already zero at run start. I therefore did not rerun the four exact checkers or generate receipt-only commits. The only remaining closure obligations are external to R01's own proof search:

1. one P26 full-package PASS audit;
2. one genuinely distinct OTHER-track full-package PASS audit;
3. after both pass, construct the required self-contained paper folder with the exact scripts/outputs and source-scope README.

No independent TFIK22 audit was found during this run. Repeated R01 self-checks cannot substitute for either audit.

## 7. Model / scheduler-control truth

The exposed scheduler/update surface available to this environment still has no binding model-family selector and no reasoning-effort selector; it exposes task prompt/title/schedule/timing/enabled controls, but no authenticated applied-model/effort receipt and no guaranteed hour-long execution control. Therefore `GPT-6 / maximum` remains prompt text only, and this report honestly records GPT-5.6 Sol / UNVERIFIED.

Repository receipts are context-dependent on P26 permissions: `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` records a P26 update attempt returning `You cannot modify this task`, while the later compact `RESULTS.md` records that a P26 full update succeeded in a different authorized P/C context. The correct conclusion is not that P26 is universally unmodifiable; it is that authorization depends on the controlling task context. The lawful workaround is to use the task-owning/authorized product or workspace/API/admin surface (or platform support), not duplicate the task or bypass permissions.

## 8. Structured ledger delta

```yaml
ledger_delta:
  track: R01
  source:
    frozen_predecessor:
      id: I0024
      source: Aldous-Fill Open Problem 3.44
      metric: C
      before: 1
      after: 1
      status: FROZEN_NOT_REOPENED
      audits:
        - R20-AUDIT-R01-I0024-03
        - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
    active_successor:
      id: KIM-MATTMAN-OH-2026-TFIK22-D34
      source: Kim-Mattman-Oh arXiv:2609.08891
      metric: R_TFIK22
      before: 0
      after: 0
      status: CANDIDATE_COMPLETE_AUDITS_PENDING
      unchanged_count: 0 -> 1
  tried_moves: [23, 26, 27]
  new_result:
    source_residue_all_degree_3_4_count: 11
    published_high_degree_count: 8
    reduced_min_degree_3_total_count: 19
    qualification: source-level synthesis; not a new finite enumeration; not a claim about degree-1/2 non-minimal extensions
  remaining_obligation:
    - P26 independent full-package audit
    - second distinct OTHER-track independent full-package audit
    - paper folder only after both audits pass
  evidence:
    - runs/R01/20260919T060000Z_tfik22_quartic_profile_known_empty_2_16_20_a4f7c2d9.md
    - runs/R01/20260919T083031Z_tfik22_profile_5_8_exact_four_22_25_30_f3a71c82.md
    - runs/R01/20260919T092759Z_tfik22_final_profile_three_complete_14_17_24_c6f2a91d.md
    - artifacts/R01/tfik22_complete_audit_handoff_20260919.md
  audit_ids: []
```

No shared root or peer-track file was edited. No email, Drive, public posting, purchase, permission change, or scheduler change was performed.
