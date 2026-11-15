VERDICT: PROVED the abstract finite-cell local-potential lemma under its stated independent-cell hypotheses, with an explicit uniform error constant

The earlier literature verdict remains PARTIAL-CLAIMED: OpenAI's “Strict convexity and differentiability of the planar exponential first-passage limit shape” (September 24, 2026) claims strict convexity for iid exponential weights on Z², not the full T050 statement. The brief update search found no change; the selected Lean statements still omit strict convexity.

New beyond the earlier report: PROOF.md checks `found:lem-finite-cell`, an upstream step left unchecked earlier. It gives `C_H = 2 + 2 N_H B_H 2^((2H+1)^2)`, where `R=8H+20`, `N_H=(2R+1)^2 2^((4H+1)^2)` and `B_H=4R+4H+11`. This verifies the paper's abstract construction, not the strict-convexity proof or its FPP hypotheses.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 check_local_potential.py`. All exact projection and boundary checks passed, including 2,800 support-cancellation checks; runtime 4.279 seconds, peak RSS 15.09 MiB, inherited nice 20. The initial memory-limit call failed before checks; macOS rejected RLIMIT_DATA, so the corrected script reports actual peak RSS and retains a 60 CPU-second limit. The nice warning reflects the already lower inherited priority.

No counterexample to the abstract lemma was found. What remains uncertain is whether the FPP network, common-world gauges, and link estimates provide all hypotheses and uniform constants needed by the contraction. Next worker: check `found:lem-common-gauge` and its insertion of the same baseline into different completed environments, especially admissibility, same-law means, and support independence; do not infer correctness of strict convexity from the present lemma check.

Files: VERIFY.md contains the original exact theorem quotations, comparison, follow-ups and a continuation spot check; PROOF.md contains the detailed argument; LOG.md records commands, failures and outputs. No git, builds, subagents or writes outside this folder.

Task: “Verify: has open problem T050 been settled by the OpenAI math release?” — continuation received 15 November 2026, 00:51 +04.
