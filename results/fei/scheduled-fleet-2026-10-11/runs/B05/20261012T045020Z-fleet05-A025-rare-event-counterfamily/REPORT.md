# A025 stage 2: the specified nested rare-flip tower has a paid outer-control face budget

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. B05 v2 assigns the nested bent/one-point-flip tower at depths 2 and 3, the four frozen orders, and exact bad-node odd-face credit divided by total influence. Bad means the strict inequality B_i>4 Inf_i, with B_i=H(S_i|S_-i) in bits. The physical charge is Q_bad,4(T)=sum_bad pi_v I(g_v h_v)/2. No spectral-conditioning probability is substituted for pi_v.

We define the tower explicitly rather than asserting a theorem about an unspecified mechanism. E0=1; Ej=Aj(Dbent(xj)+1_{xj=0} yj E(j-1)); Fj=1-2Ej. All level blocks are disjoint, each has k data bits, r controls active at zero, and one selector. The preceding tower's negative event triggers the next bent core's one-point flip. Depth one is precisely the B05 activated selector baseline. Dimension is L(k+r+1) in the frozen equal-control cases; the theorem also allows arbitrary different r_j. This construction is one concrete nested rare-flip family, not all possible rare towers.

Result: for all L>=1, all fixed even k>=2 and arbitrary r_j>=0, every complete tree querying the outermost controls first satisfies Q_bad,4/I <=1/2+5/k<=3. This includes the requested control-first and control-data-selector orders. No divergent counterfamily was found or claimed. The selector-first/data-first finite ledgers are exact evidence only; the theorem does not cover every order on every Boolean family.

## sources actually read, revisions and theorem locators

Read the 2026-10-12 04:49 UTC BOARD.md at stage start, own STATUS.md and LEARNED.md, and B05 STREAM_NOTES.md v2, 2026-10-11 23:4xZ. Read the execution protocol in full, revision 2026-10-11-execution-v2. Read B05 lead REPORT.md in 20261011T225000Z-claude-B05-odd-face-transport: Lemmas 1-2, Theorem 4 and its exact EXISTS-tree gap, and Section 6 tower assignment. Read its b05_ledger_k6.py order declaration; it makes data-first mean DATA-CONTROLS-SELECTOR, which is retained exactly here. Outer-to-inner order within each type is now explicitly frozen.

Read A021 stage-2 REPORT.md, especially Sections 4-6: every-fixed-threshold EVERY-tree failure is already established, with a paid control-first alternative. That result is not reproved or mislabeled as a failure of the existential bridge. Read A022 stage-2 REPORT.md, CLAIMS.json, ODDFACE_GAP.tex and the exact checker implementation for constant-child transfer, descendant-versus-root accounting, and the rational log conventions. REVIEW_A022.md independently accepts only the constant-child B/d<3 subclaim of A022-ODDFACE-SURGERY-GAP-LEDGER v1. It does not accept its full bundled census/descendant claim.

The previous A025 threshold-2 no-go is unchanged; this stage works at K=4. No false A021 remainder, unaccepted external theorem or numerical lead classification is a premise. The all-depth face proof is rederived from actual Boolean events. Local hashes are in out/SOURCE_RECEIPTS.json. No literature/priority assertion requires web sources; no brain or shared registry was written.

## complete derivation or exact first unsupported line

PROOF.md contains the complete derivation, face ownership counts and uniform inequalities. Here are the key quantities. With delta=2^-k, beta=2^(-k/2), a_j=2^-r_j, p_j=P(Ej=1), i_j=I(Fj), q_j=Q(Fj), and base (1,0,0), the unactivated level-j core satisfies

    c_j=(1-beta)/2+delta p_prev/2,
    J_j=k/2+delta[(k+1)p_prev+i_prev/2],
    R_j=k/4+delta/2[k(k-1)p_prev+(k+1)i_prev+q_prev].

The activated moments are exactly

    p_j=a_j c_j,
    i_j=a_j[J_j+2r_j c_j],
    q_j=a_j[R_j+r_j J_j+r_j(r_j-1)c_j].

Each unordered face pair is counted once. Data-data faces through the flipped point, data-selector, data-previous, selector-previous and previous-previous faces give R_j. Control-core and control-control pairs give the two remaining activated terms. Thus the proof keeps the cross-level faces that a naive sum of isolated root charges would miss.

For all integer r, r2^-r<=1/2 and r(r-1)2^-r<=3/4; for even k>=2, delta<=1/4, kdelta<=1/2 and k^2delta<=1. Induction gives i_j<=k+2 and q_j<=k+4 uniformly in depth and all r_j. Consequently R_L<=k/4+5/2. The lower bound i_L>=a_L k/2 is preserved.

A split with one constant child has exactly B=2d(1-d)+Psi(d^2,(1-d)^2). Its entropy bound gives B/d<=2+log2(e)/sqrt(e)<3. The outermost controls therefore incur no K=4 bad cost. They leave one active core branch of physical probability a_L. The entire remaining bad-face cost, whatever subsequent complete order is used, is at most a_L R_L by the face telescope. Therefore

    Q_bad,4(T)/I(F_L) <= a_L R_L/(a_L k/2)
                         <=1/2+5/k<=3.

This is one owned post-outer-control face reserve. It does not spend i_L anew at each nested level. For k>=4 the displayed bound is <=7/4. Terminal entropy is zero because the computed/theorem trees are complete with constant leaves. An early stop at the exposed core would retain H(core); it is not paid by declaring the controls finished.

First unsupported universal line: construct a comparable single-owned reserve after exposing overlapping control events while retaining a sufficient physical-influence lower bound, for every Boolean function. In particular the moment induction relies on disjoint blocks and a bent baseline with influence k/2. It does not transport arbitrary terminal core entropy, handle colliding outer events or prove universal FEI. The B05 existential localized bridge is still open; the specified tower no longer supplies an obstruction to it.

## executed validation with domain, arithmetic, commands and outputs

Specs were saved before computation: out/PILOT_SPEC.json, out/FULL_SPEC.json and out/REPRODUCTION_SPEC.json. The pilot is k=2,r=1,L=2 under four orders, with independent direct root checks at (k,r,L)=(2,0,1),(2,1,2),(2,0,3),(4,0,2). It passed 932 exact assertions in 0.033764 seconds. Memory was frozen at 180 MB; no job was expected above 300 MB. Caches have explicit finite limits; no GPU, automatic dimension escalation, other worker process or window was used. Actual resident memory was not instrumented, so the frozen estimate is not represented as a measurement.

Full domain: k in {2,4,6}, r in {0,1,2}, L in {1,2,3}, plus (k,r,L)=(4,8,2),(4,8,3),(6,12,2),(6,12,3). This is 31 families/124 ledgers, dimension up to 57. The compressed integer paired-Fourier histograms avoid allocating any 2^57 truth table. Remaining point-control variables contribute exact multiplicities; each nonempty lower Fourier row is multiplied by the local point coefficient, while the exceptional empty lower row receives the additive bent component. Its globally empty row is kept separate. Every histogram's cardinality and every Parseval/mismatch identity is checked.

The four orders are: selectors-controls-data; controls-selectors-data; data-controls-selectors; controls-data-selectors. Within each group levels run outer-to-inner and coordinate indices ascend. The DAG combines identical subproblems with the exact 1/2 recurrence; irrelevant queries are contracted because their physical children coincide. Node counts labeled DAG describe this contracted computation, not the number of nodes in an uncontracted full cube tree. Their reported charge and influence retain exact physical probabilities.

Full job passed 118927 assertions in 3.161137 seconds. Every B-4d decision was certified by integer linear combinations of log2 positive integers, with 100-bit outward dyadic bounds. Normalize an integer x=2^e t, 1<=t<2, and expand ln t=2 sum_j z^(2j+1)/(2j+1), z=(t-1)/(t+1). After 40 terms its positive tail is at most 2z^81/[81(1-z^2)]. Signed coefficients reverse endpoints. All 1,127 distinct signs resolved by strict intervals; 88 are positive. No floating threshold or large integer-power fallback was used. The full sign expressions and argument bounds are persisted in out/full_RESULTS.json. Each family row was flushed immediately to out/full_ROWS.jsonl and checkpoints updated.

An independent implementation, code/reproduce.py, constructs every truth-table vertex and performs direct integer Walsh transforms and edge counts. It reproduces all four orders at (2,1,2),(2,0,3),(4,0,2),(4,1,2): sixteen complete ledgers. It separately replays all 1,127 saved signs using a different 35-term exact atanh enclosure and 104-bit dyadic scale. It passed 50583 assertions in 1.96899 seconds. This is independent software reconstruction by A025, not independent agent acceptance. out/ANALYTIC_RECURRENCE_CHECK.json additionally reconstructs all 31 root moments using the closed recurrences in PROOF.md, independently of the generic restricted-state moment routine.

Exact ratios for the lead's r=2k regime:

| k | r | depth | selector-first | control-first | data-first | control-data-selector |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 8 | 2 | 56/524443 | 97/1048886 | 0 | 0 |
| 4 | 8 | 3 | 655780/8592261599 | 655667/8592261599 | 0 | 0 |
| 6 | 12 | 2 | 1603/452986798 | 1581/452986798 | 15/226493399 | 302/226493399 |
| 6 | 12 | 3 | 801118326/237495522429929 | 801117781/237495522429929 | 43/237495522429929 | 306186877/237495522429929 |

Across all frozen families/orders the maximum is 4/37 at k=4,r=0,depth=1,selector-first/control-first. The maximum over the designated depths 2,3 is 97/1126 at k=4,r=0,depth=2,selector-first/control-first. These are frozen-domain maxima only. Neither a passing finite search nor the decreasing selected sequence is used to infer the uniform theorem; PROOF.md supplies the separate finite-to-infinite bridge.

Commands from this run directory:

    python -X utf8 code/tower.py pilot
    python -X utf8 code/tower.py full
    python -X utf8 code/reproduce.py
    python -X utf8 code/save.py
    python -X utf8 code/check_artifacts.py

## proof dependencies and changed downstream conclusions

The tower theorem has no unreviewed mathematical premise: the constant-child lemma, face telescope, moment recurrences and bounds are independently reconstructed here. B05-ODDFACE-LOCALIZED-REDUCTION v1 supplies the motivation; applying its H<=(K+2/ln2)I+Q_bad corollary would give a scoped FEI bound, but that is not claimed as a new universal result or used to prove this face theorem. REVIEW_A022.md gives source-bound acceptance of only the constant-child subclaim of A022 v1; all other parts of its bundled claim retain their own review status.

Changed downstream conclusion: the lead's designated nested tower admits a paid K=4 order at every depth, even with arbitrary per-level control rarity. Repeated isolated root charges are unnecessary; all cross-level face mass is controlled by a single post-outer-control reserve. The earlier A025 threshold-2 no-go and A021 all-threshold EVERY-tree failure are unchanged. No adoption by B05, B20 or the reviewers is inferred from saving these files. This completes/validates the designated mechanism and consumes a useful review dependency, rather than opening another broad candidate while B05's pending review queue is above its cap.

## one next mathematical action and independent reviewer

Next: replace one disjoint control block by two overlapping events sharing a core, then derive the correction to the one-owned post-control face reserve while retaining exposure probabilities and terminal entropy. A023 already owns the overlap-case ledger; A025 should attack precisely the reserve/ownership correction using these recurrences, not duplicate its exact cases or increase disjoint depth. A087 should reconstruct the face categories and constant-child transfer; A094 should independently challenge the all-depth induction and exact software compression. Both reviews remain pending.

## actual persistence receipts or precise save blocker

Saved locally in this stage run: REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, PROOF.md, REVIEW_A022.md, code, all frozen specs and exact outputs. Results were flushed family by family; the proof was saved as soon as its recurrence and bounds closed. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current only in A025. out/RECEIPTS.json lists artifact sizes and SHA256s; all files are below 20 MB. out/ARTIFACT_VALIDATION.json records exact schema/hash/output checks. Independent review, supervisor repository/brain copying, mirror verification and downstream use remain pending. No shared tree, git, messaging tool or live brain store was touched.

## Universal bridge

This stage moves C019 through the B05 localized odd-face target by settling its designated nested rare-flip mechanism: every depth of the explicit tower admits Q_bad,4<=3I after querying the outer controls first, with all cross-level faces accounted for and no repeated influence reserve. Thirty-one exact families, 124 complete ledgers and a separate direct/logarithm reconstruction support the proof. The universal EXISTS-tree bridge, overlap ownership and arbitrary terminal core entropy remain open. The shortest NEXT is the one-owned reserve correction for overlapping events, because that attacks the missing nonreusing payment directly; increasing disjoint depth is now retired rather than treated as another isolated class search.
