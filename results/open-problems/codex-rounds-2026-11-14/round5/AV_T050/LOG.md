# T050 round 5 log

Task: “Verify: has open problem T050 been settled by the OpenAI math release?” — continuation started 15 November 2026, 07:22 +04.

## 1. Orientation and earlier work
Read prior folder inventories and REPORT.md, LOG.md, PROOF.md (where present), and Python scripts for rounds 1, 3, 4 using a single standard-library Python file reader. Round 1 has no PROOF.md or scripts. Large combined output was truncated; the mathematical proofs and scripts will be read again in bounded chunks before using them. Read brain navigation index and compute state; task-specific prohibition on all writes outside this folder excludes global brain, mesh and checklist mutations. No git or subagents.

Commands use OMP_NUM_THREADS=1 nice -n 15. Inherited nice is 20; nice reports permission denied trying to raise priority to 15, and the Python child retains 20. Compute status warn/owner_away_open, CPU saturated, ample RAM; only tiny reads and exact finite checks planned.

## 2. Bounded literature update (begun 07:23 +04)
Used web search for exact convexity title plus refutation/error, first-passage strict convexity 2026 OpenAI, and no-bigeodesics OpenAI; opened repository root. Results reproduce prior scope findings and known later citation, with no new solution or substantive proof review established. Search discoveries alone are not citations. Next: open current primary sources and history, finish update within five minutes.

## 3. Update check complete; next piece chosen
Within the five-minute window opened current main TeX, strict-convexity introduction and foundations, univalent introduction, repository history, lean/docs/212.md, and the arXiv:2610.42124 abstract (Scott Armstrong and Ahmed Bou-Rabee). GitHub issue search repo:openai/math "first-passage" returned no issues. Exact-title/error/referee and arXiv-domain searches found no new resolution. No SOLVED_ELSEWHERE finding. The guessed no-bigeodesics sections/introduction.tex path returned 404; correct path will be obtained from saved primary-source links.

Read round 4 common-gauge proof in full. Selected extension before doing it: audit found:lem-network, including the extra-anchor attachment and uniform local supports for inserted baselines. This is the next check named by round 4, and supplies the comparison hypothesis left conditional there. First independently rederive the common-gauge estimate; then quantify the network comparison by signed route segments and full-period defects.

## 4. Local evidence saved
Copied prior VERIFY.md and TeX/Lean/YAML/JSON evidence and scope notes here, preserving earlier folders unchanged. Saved prior proof as round4-common-gauge-proof.md and its script as recheck_common_gauge.py. Current connector sources will be saved and compared next.

## 5. Earlier result independently checked
Re-derived the common-gauge estimate without its finite toy example: the projected cost error splits into an L-period defect and J local comparisons avoiding S; the inclusion-exclusion operator has L1 norm at most 2^|S|; at most N summands give N 2^m(L+JK) beta. Conditioning an incoming-only cost on the independent world exterior leaves its incoming conditional expectation unchanged. Equal joint laws give equal calibration means at the random anchor. Linear interpolation cancels raw costs. These arguments reproduce the earlier conditional result, including C_common=5329(102+265K)2^106 for H=2.

Reran OMP_NUM_THREADS=1 nice -n 15 python3 recheck_common_gauge.py: all checks passed. Fresh primary introductions and foundations saved as fresh-*.tex through read-only GitHub fetch, with no outside writes. Correct bigeodesics introduction path is sections/01-introduction.tex. An initial apply_patch attempt combining delete/add of an identical path was rejected before changing files; separate fresh filenames fixed that tool-format error.

## 6. Network derivation and constants
Fresh foundations are byte-identical to the prior source (SHA256 2b4099ac2502613172cba97cd1cd8c842f7ffab33678fa9fee7fa1e013792ba4); all three current introductions agree with earlier saved sources, up to any terminal whitespace. The prior recheck used 0.084 seconds, peak RSS 16.45 MiB, inherited nice 20.

Read network lemma and full admissible-road definition, random-cut identity, coordinate bounds, and improvement lines 1–245. Derived a quantitative comparison for deterministic translated road labels whose marked nominal centers lie within coordinate distance D of their assigned grid index. With d=ceil(D), choose H=d+30 and K_D=20d+41. Each added anchor reaches its nearest grid intersection by two signed intervals costing at most 8 beta in expected absolute calibration error; a grid edge costs at most 5 beta; at most 4d+5 grid edges connect the two attached anchors. Hence 16+5(4d+5)=20d+41. These deliberately generous constants will be checked a second way.

The statement requires each label's road to obey the same period-defect bound; selecting one label after inspecting many labels is not covered by a pairwise bound. Inserted baselines retain spatially located private completion coordinates, so substitution preserves the local support calculation. Phase-conditioned estimates and the later envelopes/links remain unverified.

## 7. Detailed proof saved
Wrote PROOF.md: local planar crossings with loops and pauses, selected common vertex occurrences, five-period grid estimates, two-interval extra-anchor attachments, signed telescoping, and uniform support H=ceil(D)+30. Proof explicitly restricts label claims to prescribed labels and keeps phase/envelope/link hypotheses separate. No new global strict-convexity claim. Next: exact finite checks and attempted counterexamples.

## 8. Exact checks started
Saved check_network.py and ran OMP_NUM_THREADS=1 nice -n 15 python3 check_network.py. One standard-library process, inherited nice >=15 checked, 60 CPU-second limit, fixed small state spaces, peak RSS reported and checked below 768 MiB. Tests cover rounding, deterministic period containment, finite planar crossings, occurrence loops, signed telescoping, and two negative controls. Saved fresh improvement source to confirm the inserted-baseline application is unchanged.

## 9. Checks passed and attempted falsification
check_network.py exit 0: 131225 exact rounding/route checks, 243 rational endpoint/period checks, 189 paths per direction and all 35721 intersecting pairs, repeated occurrences, and 230 signed-telescoping checks passed. Two negative controls passed: physical reverse costs differ from signed reverse comparisons; uniform pairwise mean bounds do not control a maximum over many labels. Runtime 0.275 seconds, peak RSS 13.97 MiB, inherited nice 20.

Second constant count: four attachment intervals at 4 beta each, plus at most 4d+5 grid intervals at 5 beta each, gives 4*4+5*(4d+5)=20d+41. Independently, rounding gives the sharper grid count 4D+3 before relaxing to 4ceil(D)+5. Checked forward-order windows via 6delta<1 and attachment containment via 1/2+3delta<1. Checked loops, repeated visits, negative coordinates, rounding ties, same-index pairs, both directions, and that private completions are stored at original spatial locations. Fresh improvement agrees with saved prior source after terminal whitespace normalization.

No counterexample found under the stated hypotheses. Remaining uncertainty is downstream: the envelope lemma, phases and conditioned period bounds, link estimates, and locality after road improvement. No inference about the full strict-convexity proof follows.

## 10. Deliverables updated
Wrote REPORT.md with the continuation-required PROVED verdict for the conditional network lemma. Updated VERIFY.md with the current opened-source record, independent earlier-result recheck, network constants, finite checks, limits and next step. Kept its exact theorem quotations, clause-by-clause comparison and three-sentence recommended status. Fresh Lean statements, scope docs and history saved locally; older external-audit records explicitly identified as inherited. Next: final source/links/format audit.

Final audit found a missing inherited evidence link: round3-finite-cell-proof.md was not included in the initial copy list. Copied that proof from the read-only round 4 folder. Also pointed inherited round 4 PROOF.md links to the preserved round4-common-gauge-proof.md, since current PROOF.md now contains the new network check. No mathematical check failed; rerunning document audit.

The next document-audit pass reached a second missing inherited link, check_local_potential.py. Copied both historical check scripts from the read-only round 4 folder so the inherited evidence record remains self-contained. No script rerun or mathematical revision was needed.

## 11. Final audit passed
Command: OMP_NUM_THREADS=1 nice -n 15 python3 (small standard-library document audit). PASS: required files and continuation verdict; all four exact theorem quotations match freshly reopened primary sources; nine source files agree with prior evidence after terminal whitespace normalization; recommended status has exactly three sentences; 34 local links resolve; proof and report retain the conditional scope. Audit peak RSS 13.72 MiB. Corrected inherited missing evidence files/links and clarified historical provenance before this successful rerun.

Finished: REPORT.md, VERIFY.md, PROOF.md, check_network.py, recheck_common_gauge.py, fresh primary evidence and LOG.md. The new result is the conditional comparison-network check, not a proof of T050. No git, subagents, builds, messages/posts/accounts, or writes outside this folder.

Task: “Verify: has open problem T050 been settled by the OpenAI math release?” — continuation received 15 November 2026, 07:22 +04.
