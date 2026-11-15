# C0021 work log

- 2026-11-13 06:05 +04: Started task: “Open problem C0021.” Working only in this directory; no subagents, publication, pushes, or paper page images. Computation will use one process, nice 10, one numerical-library thread, with a memory cap below 4 GB.
- Read startup memory, recalled relevant brain context, and read the mesh protocol. Shared mesh digest failed with `attempt to write a readonly database`. The current task's directory-only restriction and filesystem policy prohibit updating the global mesh/checklist/brain. All task records and durable findings stay here; no substitute mesh is represented as shared coordination.
- Initial governor reading: `warn`, `owner_away_open`, CPU saturated. Use a single lightweight worker and recheck before substantial computation.
- Literature first: located the authors' book draft, Exercise VIII.5, and the 2016 Magniez–Nayak–Santha–Sherman–Tardos–Xiao manuscript. Checking uniform-average versus worst-case expected query models before transferring any bound.
- 06:10 +04: Saved the authors' book and six related full text extracts. The current author-hosted draft has the exercise on printed p. 100; numbering/pagination differ across versions. Definitions VIII.1/VIII.7, Theorems VIII.2/VIII.8/VIII.9, and Open Problem XIII.1 read.
- Literature audit found the uniform lower bound `C(f) >= I(f)^2`, stronger here than OSSS; also found Peres's 2009 lecture recording an approximately `2.46^k` uniform-average upper bound. The worst-case `2.57143^k` lower bound in the 2016 paper uses a non-product hard distribution and cannot lower-bound uniform cost. Found Göös–Jayram 2016, a subsequent worst-case lower bound, and Al-Dhalaan–Ben-David 2026, which explicitly leaves the worst-case exponential base open.
- Runtime inherits nice 15 from the launcher. Attempting to change niceness is sandbox-denied; retained this lower priority. Both AS and DATA `setrlimit` changes were rejected before computation. The exact DP uses one Python process/thread and an explicit 1.5 GB RSS guard instead.
- 06:11 +04: Exact unrestricted uniform costs obtained: `C_1=5/2`, `C_2=393/64`, `C_3=15796051/1048576`. Bellman certificate saved with 13,986 states and every query action. These yield revealments `5/6`, `131/192`, and `15796051/28311552`.
- 06:18 +04: Independent checks passed: labelled partial-assignment DP at k=1,2; an integer-arithmetic fixed-majority-tree DP at k=1,2,3 without AND/OR conversion or projection elimination; regeneration and exact checking of all 66,680 Bellman inequalities; literal 2016 algorithm checked on all 512 depth-2 inputs. Peak verification RSS was about 76 MB.
- Fixed-tree restriction counts at depths 1,2,3,4 are 6, 46, 17,206, and 849,110,490,846. Thus k=4 full optimization is not feasible by this exhaustive method under the memory budget. No exact k=4 value is claimed.
- Reanalyzed the 2016 Evaluate/Complete routines under uniform input. Exact average recurrences give the positive root of `32*x^3-47*x^2-78*x-2` as a rigorous algorithmic growth base, approximately 2.4670436373.
- Testing an explicit finite-state recursive family with 46 types and 17,206 lookahead states. At trial base 2.46 the rational certificate fails; this is not a bound. Seeking a slightly larger rational base with all inequalities exact.
- 06:23 +04: Certified the rational growth base `lambda=246003/100000=2.46003`. Trial 2.460025 failed and is retained only as a failed search result. A separate verifier, importing no search code, checked the legality of all 17,204 policy actions and all 46 exact type inequalities. Minimum nonconstant slack is `185008634992727/605174760090000000000`. The resulting all-height prefactor is less than 13.385.
- Independently converted all bounds and finite exponents with 55-digit Decimal logarithms; checked total influences both by the ancestor/Russo proofs and by truth-table flips at heights 1 and 2. Certified interval: `log_3(300000/246003) <= sigma <= log_3(4/3)`, approximately `[0.180626728576668, 0.261859507142915]`.
- Finished REPORT.md with status PARTIAL, the exact k=1,2,3 values, explicit interleaving recurrence, finite-state algorithm proof, LP/Bellman formulation, directional counterexample, Schramm–Steif consequence, and precise unresolved gap. The log-linear finite fit is descriptive only. No literature resolution was found; no claim is made that the literature search proves absence of one.
- Artifact audit checked all 11 source text hashes, all report file links, certificate hash, required first line, and absence of PDFs/page images. Largest measured mathematical-run RSS: 75,694,080 bytes. Final formatting audit corrected inline math delimiters and checked balanced math spans.

## Checklist

- [x] Retrieve text sources and audit the cited exercise, definitions, and literature through 2026.
- [x] Prove the revealment / uniform expected-cost identity and derive exponent bounds.
- [x] Compute exact optimal values at feasible small depths and test depth-first optimality.
- [x] Independently verify load-bearing values; finish REPORT.md with the required status.

Exact sigma remains undetermined. This task ends with a partial mathematical result, not a resolution of C0021. Global task/mesh/memory writes remain unavailable under this task's directory restriction.
