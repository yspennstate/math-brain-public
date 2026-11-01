# P03 FEI — recovered September 19 research and delivery clarification

**Full FEI: NOT PROVED.** This handoff preserves the results of the preceding local research session. It is not a new independent mathematical audit and does not change any schedule, ownership, permission, or source-level closure status.

## Read first

[Research note with proofs and scope](../continuation-2026-09-19/RESEARCH_NOTE.md).

Principal results reported and justified in that note:

1. The nine-variable cubic phase `(-1)^(z * sum_{i<j} y_i y_j)` refutes the archived `D_cross <= 4 Delta_Q P + 2 Delta_Q L` proposal for every admissible single-coordinate quotient rule. The recorded rational certificate encloses the optimal residual in `[0.174606321218, 0.174606321219]`. This is NOT a counterexample to FEI.
2. Odd majority has `D_cross = Theta(log n)` while `R+sum j_i^2` stays bounded. Every fixed sublogarithmic marginal power beta<1 also fails as a universal budget. These are analytical proof-route obstructions, not a solution of FEI.
3. A systematic coding lift preserves entropy after physical coordinate restrictions within its distance budget and keeps small conditional spectral-block entropies zero. Sublinear redundancy and tensor amplification make the FEI-constant reduction asymptotically lossless.

The direct universal target `sup B(f)/I(f)<infinity` remains unproved. The logarithmic candidate `D_cross <= K(R+Q_log)` remains unproved and would require a separate telescoping argument even if established. Do not revive the old false pointwise shortcut `H(f)<=B(f)+(2/ln2)I(f)`.

## Exact core files delivered through the connected GitHub API

- `proofnet24/P03-fei/continuation-2026-09-19/RESEARCH_NOTE.md` — creation commit `49b58e22462cd9246d959a29547dfd4906deea2d`.
- `proofnet24/P03-fei/continuation-2026-09-19/checks/certify_nine_variable.py` — creation commit `bd2d7fabc33295381feb1983e19ac445ed9437b6`.
- `proofnet24/P03-fei/continuation-2026-09-19/checks/exact_drift_certificate.py` — creation commit `38508cdf5956ee3b98eee1c541040bba8d6ca873`.
- `proofnet24/P03-fei/continuation-2026-09-19/checks/certify_nine_variable.json` — creation commit `85bc88957893557e8245f00b50efdcfba8cafd24`.

Run the finite checker with:

    python proofnet24/P03-fei/continuation-2026-09-19/checks/certify_nine_variable.py

The checker and dependency were copied from the actual saved research ZIP; the JSON is its recorded prior-session output, not a claim of a new run or audit during delivery recovery. The research note also contains references to `raw_work/`. The larger exploratory raw-work collection and its coding/majority checkers were NOT included in this core delivery; they remain in the conversation artifact `FEI_2026-09-19_results.zip`. Do not infer those paths exist remotely from citations in the note.

## What happened to delivery

The earlier session reported it had found no GitHub write action and that its local Git connection failed. That was a failed delivery, not evidence that all scheduled workers lost write permission. In this subsequent turn, discovery exposed `create_file`, `update_file`, `create_blob`, `create_tree`, `create_commit`, and `update_ref`, and the four file-creation actions above returned real commit SHAs. We have not established the exact cause of the earlier tool-discovery/session failure.

The separate `2026-09-19__FROZEN_SESSION_RECOVERY.md` handoff correctly recorded what was recovered at its own earlier checkpoint. This handoff adds the actual later recovered research note and core certificate files; it does not delete or rewrite that historical recovery record.

Continue through the existing authorized research workflow. Reading coverage remains limited to that stated in the note: do not claim every page of the 1,506-page archive or every scheduled report was independently reviewed. No changes to automations were made in this delivery.
