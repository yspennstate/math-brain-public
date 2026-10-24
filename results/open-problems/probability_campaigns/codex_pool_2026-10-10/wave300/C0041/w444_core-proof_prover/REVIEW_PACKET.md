Review packet for w446, C0041, author w444, 2026-10-10.

The author claims five conditional or special-case hand proofs and one precise open gap. The parent target is NOT claimed solved. The adversary w445 received the statement-only packet first, by mesh receipt msg-cfbb2cfcfb. Lemma boundaries were sent to w446, w447 and w450. Only the author's lane artifacts were changed.

The full proof text is [ATTEMPT.md](~/brain_workers/w444/ATTEMPT.md); structured statements and assumptions are [CLAIMS.jsonl](~/brain_workers/w444/CLAIMS.jsonl). Source recovery and bounded historical checks are in [SOURCE_STATUS.json](~/brain_workers/w444/SOURCE_STATUS.json), [REPORT_SOURCE_RECORDS.json](~/brain_workers/w444/REPORT_SOURCE_RECORDS.json), and [REPORT_STORE_CHECK.json](~/brain_workers/w444/REPORT_STORE_CHECK.json). Review byte identities are in REVIEW_HASHES.json; these are artifact identities, not proof receipts or bundle manifests.

Requested scope of KEEP/FIX/DROP decisions:

- R1: actual iid nearest-neighbor cycles with finite mean duration and positive expected directional increment imply positive limiting velocity. Check the finite-mean tail/Borel-Cantelli step and the unfinished-cycle displacement. The iid law and its finite mean are assumptions.
- L1: from every point of a closed radius-r box, <=2r+1 consecutive +e_1 steps leave; the uniform conditional chance is >=kappa^(2r+1). Check the quenched Markov iteration, mean tail sum and the geometric-to-exponential moment bound. Independence of exit attempts is never assumed.
- L2/L2b: distinct site rows are iid before any selection; the opposing sign events at a single site are disjoint for delta>0. Check the balanced half-box count, AM-GM moment-generating-function bound and Chernoff rate. Verify that the weighted series uses theta>1/2 and d>=2.
- L3: H is a genuine stopping time with the entire fixed environment included; C is measurable at H and lies in a deterministic bounded set. Check the conditional quenched moment and the union bound over centers. The Q extension merely removes a conditioning indicator at cost 1/q. It asserts no fresh environment after selection and no Markov property under Q.
- T1: even a future-dependent tau satisfies {tau>t,R<=r} subset {T_B>t}. Check the conditioning factor, fixed-box exit bound, logarithmic radius choice and the strict sufficient threshold a>2log(1/kappa). The exponential radius tail is explicitly an extra assumption.
- GAP: no one may infer E_Q[tau_1]<infinity from the inward-box estimates. The standard regeneration time is S_K, a time, rather than K, the successful-attempt index. The exact construction and unresolved integrated tail are saved in ATTEMPT.md.

Source checks: the original source is https://arxiv.org/pdf/1309.2589, Open Question 2.20, PDF page 24 (index 23), printed page 22. The 2014 Campos-Ramirez formulation is https://arxiv.org/html/1212.4020v3, Conjecture 1.1. A primary repository posted a claimed solution in September 2026: https://github.com/openai/math/blob/main/lean/docs/220.md. Its ComparatorChallenges/DirectionalBallisticity.lean ends its theorem in sorry. That file is a comparator statement, not an actual compiled-proof receipt; it does not by itself disprove the separate announcement. Current openness remains UNKNOWN in this packet.

The draft inbox bundle is ~/math-brain-inbox/w444/bundle_001.json. All entries are concepts, including clearly marked unreviewed hand calculations and the unproved input. Its one cross-bundle relation points to the exact existing C0041 logical ID captured in the read-only store report. No relation says that these calculations prove C0041.

[AUTHOR_MODEL_EVIDENCE.json](~/brain_workers/w444/AUTHOR_MODEL_EVIDENCE.json) records requested settings separately from actual served-model evidence. The latter is unavailable to this worker. Record the referee's response-side served identity if available; do not promote a theorem while the different-model review gate remains unestablished. If w446 develops a new result rather than auditing these claims, w449 is its independent referee.

Please return narrow verdicts referencing the claim IDs and the byte identities, with any changed assumptions stated explicitly. Packaging validation is not a mathematical proof audit. The worker session will finish NEEDS_REVIEW; integration contact is codex-01a12190.

NEXT: Review R1/L1/L2/L3/T1, then check a certificate for arbitrary low escape probability that does not demand this special inward-box pattern.
