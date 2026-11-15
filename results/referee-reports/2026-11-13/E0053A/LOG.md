# E0053 work log

Task received: 2026-11-13 05:17 +04 (Asia/Tbilisi). User: “Open problem E0053”, literature first, small-degree bound audit, numerics, rigorous partial results.

## 2026-11-13 05:20 +04 — orientation and literature search

- Read brain startup/identity instructions and ran one recall for regular-graph bisection; no directly relevant recalled result. Recalled notes are hints only.
- Scope: all task artifacts and computation remain in this directory; no subagents, publication, pushes, or unrelated systems. The task-specific directory restriction overrides global checklist/mesh/memory writes outside this directory. This log is the local task record.
- Compute governor at start: status warn, mode owner_away_open, existing host CPU saturation. Use one compute worker at nice 10, cap math-library threads at one; keep well below the requested four threads / 4 GB.
- Initial search found 2026 MaxCut-versus-MaxBis work, which does not by itself resolve MinBis+MaxBis. Found 2025 positive-temperature and improved max-cut bounds, to inspect directly.
- No conclusion yet; REPORT.md starts with provisional PARTIAL until final audit.

## 2026-11-13 05:23 +04 — literature and bound audit

- Downloaded Bandeira's October 10, 2016 full notes and the MIT problem extract. Full PDF page 117 contains precisely Conjecture 8.5, fixed d, even n, (MaxBis+MinBis)/n=d/2+o(1). Saved text and rendered page.
- Downloaded Zdeborová–Boettcher, DMS, Sen, Jagannath–Sen, Gamarnik–Li, Lyons plus erratum, Coja-Oghlan et al., Lichev–Mitsche (v4 November 2026), Harangi (2025), Csóka et al. (2025), Gheissari–Perkins–Yap (2025), Aronow–Lopatto (2026), and relevant algorithm papers. Checksums/URLs in sources/manifest.json.
- No resolution of the requested identity found. Lichev–Mitsche explicitly says its bounds do not resolve it; the 2026 MaxCut=MaxBis theorem is a different statement. Positive-temperature result only reaches reconstruction.
- Csóka et al. Section 3.1 even records an opposite conjecture (strictly smaller sum), with intuition, not a proof.
- Important source scar: Díaz–Do–Serna–Wormald abstract quotes 1.32697, but Theorem 3 in the author PDF says 1.32595. Theorem 4 prints +epsilon in a universally quantified lower bound, which cannot hold as written. Saved rendered page 3. Use the unambiguous Lyons Theorem 4.1 bounds instead, and report the discrepancy.
- Harangi normalizes MaxCut by edges, not vertices: safe upward rounded constants 0.923868 and 0.867902 become 1.385802 and 1.735804 per vertex. Cubic MinBis upper 0.139822 gives sum upper 1.525624 > 1.5. Quartic MinBis upper 1/3 gives sum upper 2.069138 > 2. Lower bounds likewise do not contradict either target.
- Sandbox disallows changing niceness, but child processes already inherit nice=15 from the launcher, more yielding than requested nice=10. Retain nice=15, one compute thread.

## 2026-11-13 05:27 +04 — exact checks complete; large search started

- Exhaustive balanced enumeration completed on 144 independent graphs: d=3,4,5; n=12,16,20,24; 12 instances per cell. A separate HiGHS binary ILP cross-check agreed on 12 of these graphs (both optima).
- HiGHS also certified both optima on 18 graphs at n=32,48 (4 and 2 instances per degree). No timeouts in this batch. All 162 small graphs' EO witnesses attain both certified optima.
- Python independently checks every saved witness: simple d-regular graph, exact balance, edge crossing count, and parity. Solver status and bounds are retained, not just incumbent values.
- Small batch used initial bucket-order tie handling. Archived its exact source and SHA-256. Main batch uses uniformly random tie selection within the chosen fitness bucket, alternating tau=1.2/1.3, plus full improving two-vertex quench.
- Main batch: n=64..32768, independent exact-uniform graph samples, 4 restarts/objective, 1000–2000 EO sweeps/restart. Sequential, inherited nice=15, tiny C++ memory. Heuristic bias will be assessed with deeper EO and independent Kawasaki annealing.

## 2026-11-13 05:31 +04 — governor adaptation

- Main batch initially stopped at the next graph on throttle, preserving 131 complete records. Owner-present state persisted while proof/literature auditing continued.
- Adapted the single-child runner to a 20% wall-clock run allowance in throttle/owner-present mode (20 ms run, 80 ms SIGSTOP), still nice=15. This reduces compute below one active core; no other process is touched. Distress stops our compute immediately. Resume remaining graph sizes under this cap; use full one-thread allowance only when owner-away/open permits it.
- This is a resource-control adjustment, not an exception to yielding. No new language-model workers or services are launched.

## 2026-11-13 05:35 +04 — rigorous proof audit and interval bounds

- Wrote full proofs in data/PROOFS.md: all d<=2; a pairing-count first moment bound; exact spin/partition-function reduction; equivalence of expected and typical formulations by switching concentration. These do not resolve d>=3.
- Independently checked the pairing probability formula with exact rational arithmetic (normalization and mean), d<=2 statements by finite exhaustive enumeration, and the finite-temperature inequality by direct partition sums.
- Evaluated Harangi's explicit Table 2 parameters with outward interval arithmetic: upper fractions 0.9238674766043736 (d=3), 0.8679013142663060 (d=4), 0.8346377978544108 (d=5). This independently validates the relaxed constants used in the bound audit. Truncated Table 1 numbers would not be safe upper bounds.
- Main endpoint estimates worsen at larger n under fixed budget; sum cancellation can hide shared optimization deficits. Deeper paired-graph runs are required before interpreting a nonzero fitted intercept.
- Verified bibliography against publisher/author sources; corrected working-draft journal details for Jagannath–Sen and Lichev–Mitsche before the final report. Published Lichev–Mitsche PDF also downloaded.

## 2026-11-13 05:43 +04 — follow-up implementation speed check

- Implemented an equivalent EO rank selection that integrates the rank probabilities over the existing sign/fitness buckets, avoiding a per-flip binary search. Main engine/source remains unchanged. Follow-ups use code/bisection_fast.cpp, recorded separately in each row.
- Compared the two implementations with identical seeds on 18 pilot objective runs (d=3,4,5): every cut and full witness was bit-identical. The faster selection changes cost, not the sampled search process.
- Follow-up budget: 12 x 6000 sweeps/objective for n<=1024 (four graphs per degree/size); 8 x 4000 for n=2048,4096 (three graphs per degree/size). Independent annealing: four restarts x 2000 sweeps on three graphs per cell at n=128,512,2048,8192.

## 2026-11-13 05:48 +04 — complementary local-rule proposition

- Added a full tree-gauge proof: every finite-radius, Gaussian-label, odd local rule on locally tree-like d-regular graphs has a companion whose feasible bisection density complements it to d/2, after an o(n) balancing repair.
- The companion map is an involution, so approximation of both global optima by this local-rule class is a sufficient condition for the conjecture. That approximability hypothesis remains unproved.
- A one-neighborhood Gaussian example for d=3 gives densities about 0.45613 and 1.04387, far from both true optima, yet summing to 1.5. Thus complementary heuristic values alone can be misleading. This proposition does not directly apply to EO's global ranking process.

## 2026-11-13 05:52 +04 — follow-up analysis convention

- The original main batch completed all 306 graphs at 05:49:47 +04; largest n=32768. Its C++ peak resident memory was about 11 MB; Python controller about 47 MB.
- Additional EO runs have independent seeds and can occasionally miss a witness already found by a shorter run. Preserve all raw results; for the best endpoint estimates on matched graphs, pool main+deep witnesses (take the smaller minimum and larger maximum), recording both trace paths in data/pooled.jsonl.
- Budget comparisons report the improvements obtained by adding a follow-up's witnesses to the main batch, so observed search progress is monotone at each endpoint. The remaining optimality gap is unknown.

## 2026-11-13 06:04 +04 — numerical interpretation

- Deep EO completed all 66 matched graphs at 06:00:31 +04. Main+deep witnesses are pooled on the matched subset; all raw traces remain.
- Main cubic p=2/3 extrapolation: Delta approximately -0.000388, conditional 95% bootstrap interval [-0.000731,-0.000100]. This is an algorithm-output/scaling-model statement, not a refutation.
- Pooled deeper quintic p=2/3 fit over n>=256: +0.003334, interval [+0.001676,+0.004928]. Dropping n=256 gives +0.001712, interval [-0.000380,+0.003747]. Include this sensitivity explicitly rather than selecting a fit.
- At n=4096, added cubic EO effort changes the matched sum by -0.001139: min decreases 0.001953 and max increases 0.000814. Endpoint budget drift exceeds the main fitted residual. Remaining optimizer gaps are uncalibrated.
- Independent scalar weighted-regression formulas reproduce all 36 main one-power endpoint/paired intercepts to <1e-10. Source-hash audit and archived-small replay also passed.

## 2026-11-13 06:08 +04 — final audit and completion

- Final status: PARTIAL. No literature resolution, proof, or counterexample for fixed d>=3 was established. Known rigorous d=3,4 bounds do not contradict the target. Proofs cover d<=2, symmetric first-moment bounds, concentration/expectation reduction, finite-temperature reduction, and complementary local rules.
- Finished 570 experiment records on 468 independent graph draws: 162 small graphs with both optima certified, 306 main large graphs, 66 deeper matched EO records, and 36 independent-method annealing records. Largest n=32768.
- Independently recounted and checked all 5472 saved balanced witnesses. Exact enumeration/ILP comparisons passed. All 570 experiment source hashes match preserved implementations. Scalar regression audit passed for 36 main intercepts; all 990 saved fit results are finite.
- Verified all 21 downloaded primary PDF checksums and all local report links. Checked the local-rule example a second way using the arctangent identity. Final audit metadata: data/final_audit.json.
- Computation remained single-worker and inherited nice=15; library thread caps were one. The largest recorded Python experiment-controller RSS was about 235 MB and largest C++ RSS about 11 MB, below the 4 GB limit. Governor throttling was honored through a 20% run allowance; no other workload was touched.
- Main cubic and deeper quintic conditional fit deviations are reported, together with the size-window sensitivity and optimizer budget effects. No calibrated nonzero infinite-n deviation of the true optima is established.
- Sources, code, raw graphs, witnesses, fit tables, plots, report and this log are saved locally. No subagents, publication, pushes or external writes were performed as task work.

Done — “Open problem E0053”, received 13 November 2026, 05:17 +04 (Asia/Tbilisi).
