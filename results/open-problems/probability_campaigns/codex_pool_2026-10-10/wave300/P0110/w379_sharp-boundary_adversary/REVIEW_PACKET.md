# Review packet for w380

Worker w379, P0110 sharp-boundary adversary, 2026-10-10. This is one task with one independently derived bridge obstruction and two direct peer verdicts.

Completed mathematical review: w380 independently KEEP C1/C2. REFEREE_VERDICTS.jsonl preserves those receipts; the review request below identifies what was checked. The final draft has four entries and six relations. Account/model provenance verification, ingestion and retrieval remain separate coordinator steps.

Primary target: [Auffinger–Damron–Hanson, arXiv:1511.03262v2](https://arxiv.org/pdf/1511.03262v2), Question 22 and equation (4.19). The target is existential in a fixed iid nearest-neighbor edge law. SOURCE_STATUS.json distinguishes this target from the conditional theorem and records present openness UNKNOWN.

The exact requested mathematical review is CLAIM C2. Let tau be iid, finite, nonnegative, nonconstant on nearest-neighbor Z^2. Let T_N be unrestricted passage from 0 to N e1 and D_N its restriction to coordinatewise nondecreasing paths (the unique axial path). Choose 0<l<h with p_l=P(tau<=l)>0 and p_h=P(tau>=h)>0, integer n>2l/(h-l), L=n+2, delta=n(h-l)-2l, q=p_h^n p_l^(n+2). Then

    liminf (D_N-T_N)/N >= delta q/L > 0 almost surely.

For finite mean m, also limsup T_N/N <= m-delta q/L. A proof is in INDEPENDENT.md. Each deterministic block event uses n axis edges and n+2 disjoint detour edges. Blocks at horizontal spacing L have disjoint edge sets; their event indicators are iid Bernoulli(q). Replacing a successful block in the direct path saves at least delta. The strong law gives the stated lower rate. This argument never assumes that edge values conditioned on a minimizing path remain independent.

Review the existence of l,h for a nonconstant finite law; edge disjointness; validity of the concatenated path for every N; the strong-law step; the absence of a mean assumption in the difference statement; and the explicit scope. These are checks of the author proof, not a source/hash or runner-success receipt. No formal proof assistant check was attempted; the probability input is the ordinary iid Bernoulli strong law.

Numerical validation is exact and limited: MEASUREMENTS.json records 320/320 shortest-path checks, one strict-detour case out of 256 at n=3, mean saving 1/256, and zero shared edges across 20 translated blocks. Its command is in that file. These checks corroborate the construction but do not replace the infinite-volume proof.

PEER_AUDIT.md and AUDIT_VERDICTS.jsonl independently KEEP w378's L1/L2. The proofs preserve the distinction between a fixed-law exponent problem and uniformity over a family of narrow laws. No gap was found in those stated lemmas.

The math-brain draft uses concept kinds for reviewed route derivations awaiting coordinator integration; proof-text fields remain null. All sources for the new mathematical derivation use the required owner-own-work license. The proposed bridge and refuting concept are both in the same bundle, with exact supporting ends. An additional semantic association targets the existing P0110 logical ID verified by a read-only exact-ID query; EDGE_EVIDENCE.jsonl quotes both ends. Submission, mathematical review, ingestion and retrieval are recorded separately.

Reviewer application: inspect the complete bundle in math-brain-inbox/w379, independently review C2, and use the coordinator's normal integrator only after the required review. The worker did not run an integrator or write to any live SQLite store.

NEXT: Coordinator checks review provenance and ingests the scoped draft; further proof work must bound centered replacement error for one fixed iid law while retaining the original exponent-existence gap.
