# P0117 review packet for coordinator and w389

2026-10-10. Reviewer w386. The exact individual verdicts with reproductions are in REVIEWS.jsonl. Every KEEP below is scoped to its stated lemma or counterexample; the parent problem has **no certified proof** in this packet.

| Claim | Verdict | Scope and unresolved input |
| --- | --- | --- |
| w384.S1.1; w385-S1.1 | KEEP | Dated ranking metadata; duplicate source rows, ingest once. |
| w385-S1.2 | KEEP | Shell-witness compactness; P(E_n)->0 unproved. |
| w385-S1.3 | KEEP | Coherent adaptive-selector counterexample; abstract only. |
| w385-S1.4 | KEEP | Endpoint-count arithmetic and primary midpoint theorem scope; no union decay. |
| w384.S1.2 | KEEP | Moment-free properness for iid positive finite weights. |
| w384.S1.3 | KEEP | Deleted-edge metric formula, ties separate. |
| w384.S1.4 | KEEP | Decreasing threshold and conditional identity; support collapse unproved. |
| w384.S1.5 | KEEP as gap | H_infinity<=a is the exact unproved lemma, not a result. |
| w385-S1.5 | KEEP | Potential bigeodesic arms have limiting directions under A1; random singleton directions remain. |
| w385-S1.6 | KEEP | q_n cannot be o(1/n) along all scales; no P(E_n) lower bound. |
| w385-S1.7 | KEEP | Box-witness filtration reduction; annulus contraction unproved. |
| w385-S1.8 | KEEP | Positive-probability atomless iid box/full metric-substitution control. |
| w385-S1.9 | KEEP | Ladder counterexample to planarity/nonatomicity alone; outside Z^2. |
| w384.S1.6 | KEEP | One-edge lowering and positive-probability strict pinning; pinned-path exclusion unproved. |
| w384.S1.7 | KEEP | Constant-weight capacity 3c, outside nonatomic target. |
| w384.S1.8 | KEEP | Abstract selected-index warning; duplicate of stronger w385-S1.3 control. |
| w384.S1.9 | KEEP | Public 2026-09-24 theorem statement only. |
| w384 bundle_001 | FIX | Seven entries use absent probability.fpp namespace; see below. |
| w385 bundle_001 | KEEP | Eight scoped entries and eight relations; no second-account or ingestion certification. |

## Independent reconstruction of the hardest peer claim

For w384.S1.4 I did not rely on w385's review. Fix the outside weights and vary s=t_e. The formula T_s=min(d,s+C_e) makes s<D_e(x,y) equivalent to strict e preference for one shell pair. First-hit truncation of a strictly e-preferring outer geodesic preserves strict preference; otherwise an e-free inner route would splice into an e-free outer competitor. This proves H_(n+1)<=H_n. A path through e at every radius has a centered diagonal subsequence, which is a bigeodesic because each stabilized finite segment is globally minimizing. At the random independent edge value, ties against the countable H_n and H_infinity are null. This yields P(A_e|outside)=F(H_infinity). The step supplies **no estimate** on H_infinity; support collapse is the only claim needed to conclude absence by this route.

## Source and public manuscript boundary

SOURCE_STATUS.json records the exact Damron--Hanson Conjecture 1 quote, Auffinger--Damron--Hanson Question 31, P0117 ledger rows 188/600 and attempt row 119, and the dated 2026-09-24 public claim. The source card already in the read-only store has logical ID math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp; I probed by distinctive title/body words across the nodes table before preparing any draft relation. Its current body says status unverified and carries the older intake paraphrase. The public manuscript's local label-budget and posterior-raise calculations were rederived in ATTEMPT.md; its exceptional-label transfer and no-forks proof have not been fully checked. Current openness remains UNKNOWN.

## Independent review requested

w389 is the named independent referee for any new result by w386. Please check w386.S1.2, the local label-budget derivation in ATTEMPT.md, especially the uniform o(Nl) error at random first/last marks and the bounded reverse-Fatou step. The narrow review request was sent to w389 as mesh message msg-13d17bae16. Also audit the public manuscript's Lemma 4.4 and Proposition 6.1 before any solved-status promotion. A KEEP of w386.S1.2 is a KEEP of a conditional budget lemma only.

The draft brain bundle is a concept-level review aid. Submission, second-login review, ingestion and retrieval are separate states; none of the latter three is claimed here.

## w384 bundle audit

I read all seven entries and seven relations directly, and queried the read-only live store: there are 0 existing logical IDs under `math:probability.fpp:*`; the existing P0117 card is under `probability.core`. The verified brain-growth method recommends existing namespaces. The mathematical content is scoped correctly, but the bundle needs a **FIX before ingestion**: move its entries to `probability.core`, clarify properness card wording to "changes on finitely many edges," and deduplicate its threshold and selector material against the revised w386 draft and w385's stronger dyadic selector control. Its dependency from conditional identity to properness should describe the iid application rather than implying the deterministic identity needs the iid theorem. The seven relations have matching local keys; its cross link matches the existing target logical ID. The withheld graph verifier ran 0 graph checks because the fresh governor state reported distress; I did not bypass that gate.

## w385 bundle audit and revised draft

w385/bundle_001.json (SHA256 C8D4E4EEBF32AEB74D5F0C4616B44B751C9692CFD12301ABDD7AA47DC8DF3C44) has eight entries and eight relations. I checked each statement against the separately audited w385 claim and each relation against its local or existing target key. A read-only store query found one existing node in its probability.first-passage-percolation namespace. The author-reported finite check covers 9375 equalities and 290 ties with maximum error zero; it is a control measurement, not an infinite-volume proof, and I did not rerun it while the fresh compute gate constrained graph checks. Content verdict: KEEP, scoped to draft review. Account-diverse review and integration remain pending.

My active bundle is ~/math-brain-inbox/w386/bundle_002.json, two entries and two relations, SHA256 568F09503AAB1DE5BF2E26EAF000DA3D1E11F1F3935EB3087EFF7E83944F0D74. It uses the existing probability.core namespace and links to the existing P0117 card. The overlapping max-pair card was removed because w385 already supplied it. The earlier bundle_001 was renamed to bundle_001.part to withdraw it from normal ingestion. Both remaining cards are concept-level drafts; no theorem or solved-status promotion is proposed.

Integration handoff to codex-01a12190 was sent as mesh message msg-1b9813d3f3 with exact packet paths, hashes, scoped verdicts, and remaining gap. The requested GPT-6 Sol final referee setting has no response-side served-model evidence in this packet; model identity remains unverified.
