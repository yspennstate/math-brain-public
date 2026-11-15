# T030 round 4 log

Task: Verify: has open problem T030 been settled by the OpenAI math release?
Started: 2026-11-15T04:15:09.729271+04:00

## 1. Orientation and earlier files
Read both earlier REPORT.md and LOG.md files and the round-3 PROOF.md and audit_resolvent.py; the first folder has no PROOF.md or scripts. Command: OMP_NUM_THREADS=1 nice -n 15 python3 (read-only pathlib listing and text reads). Large combined output was truncated, so targeted reads follow. Compute state: warn, owner_away_open, CPU saturated; only small single-thread text work and exact arithmetic planned. The sandbox denies a priority change, but inherited priority=20. All writes stay here. The later folder-only instruction precludes global brain/checklist/mesh logging commands, which mutate external files. No git or subagents.

## 2. Bounded literature update
Web search queries: exact hot-spots title with error/correction/November 2026; hot spots conjecture 2026 November convex proof; hot spots 2611 convex. Opened full arXiv HTML 2610.12622v1 (Krzysztof Burdzy), 2610.32920v1 (Rodrigo Bañuelos), 2610.18546v2 (Haiyun Deng, Xuyong Jiang, Xiaoping Yang), and the ai-wake follow-up index. Same conditional simple-eigenvalue non-strict extensions and strict maximum-modulus result as before; no later full strict arbitrary-convex-planar resolution found in this bounded search. Search completed within five minutes. No SOLVED_ELSEWHERE.md warranted.

## 3. Earlier recheck and chosen extension
Read round-3 PROOF.md and audit_resolvent.py fully. Independently recheck the finite resolvent identity and positivity by block Gaussian elimination, then examine the epsilon-to-zero passage in prop:interior-reciprocal, specifically the L2 Green sources and infinite diagonal. This is the next step named by round 3. The choice is to establish this one singular-limit step, rather than undertake the remaining boundary/eigenfunction proof. Fresh upstream sources are being fetched.

## 4. Fresh sources and independent recheck
Fetched and saved actual upstream introduction, boundary-kernel and reciprocal-kernel sections; MTW introduction; symmetry paper; Lean scope 369 and HotSpots target through read-only github_fetch_file. Their SHA values agree with the earlier snapshots (reciprocal bcb125482dbfe6874ffe4582625c01ea66571ca9; hot-spots introduction ca7f7f292379a95899f04a1de411eb610d1fe9ab). No change to the smooth-boundary restriction. Used apply_patch for local snapshots only.

Re-ran OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/AV_T030/audit_resolvent.py without importing or writing there. Output: all 34 elimination orders and 18 perturbation checks pass; exact same pivots, including 85695828686/91043783325; negative update inertia (2,1,0); priority 20, peak RSS 14761984 bytes. Independently re-derived the inverse update from the block factorization Qnew=L diag(Qold,s) L^T, s=1-w Hzz, and checked the perturbation estimate by adding/subtracting three inner products. Both earlier claims hold. Full derivation will be in PROOF.md.

Read startup memory and memory index directly after locating them with rg --files, without invoking logging commands outside this folder. The earlier absent path was not the actual startup path.

## 5. Singular-limit derivation
For density at most A, the explicit disk Green formula gives G(x,y)<=log(2/|x-y|)/(2*pi). Extending the integration disk to B(x,2) gives integral G^2<=1/(2*pi), integral G^4<=3/(8*pi^3). Hence every Green section is in L2(rho), including when x is in the integration support. The regularization identity yields G-Ceps<=2*pi*eps*G^2 almost everywhere, giving uniform source error <=eps*sqrt(3*A/(2*pi)) and Hilbert-Schmidt operator error <=eps*sqrt(3*A*m/(2*pi)). Both resolvents remain bounded by 1/(1-d). These estimates establish the singular limit by norm convergence, independently of monotone chain passage. Detailed proof and attempts to break the hypotheses follow.

## 6. Proof saved and hypothesis checks
Created PROOF.md with a complete source/operator-norm proof of the epsilon-to-zero passage. It includes an independent layer-set derivation of every logarithmic moment constant, the correction error bound, finite correction on the diagonal, reciprocal diagonal rate <=2*pi*epsilon, and closure of reciprocal inertia under finite limits. Re-derived the same limit by the manuscript's nonnegative chain integrals. Attempts to break it: atomic measures invalidate the source assertion but are excluded by the bounded-density assumption; d=1 makes the resolvent singular; convergence of direct kernels is not uniform across their logarithmic diagonal. No defect found in the checked passage. Saved provisional REPORT.md before these further checks.

Searched GitHub issues with repo:openai/math hot spots via read-only github_search_issues: empty result. No build, posting, or external mutations.

## 7. Independent arithmetic checks
Created check_singular_limit.py and ran OMP_NUM_THREADS=1 nice -n 15 python3 check_singular_limit.py. Output:

```text
moment coefficients: p=1..8 agree exactly by polar and level-set recurrences
L2 coefficient=1/2; L4 coefficient=3/8; source-error-squared coefficient=3/2
regularization identities: 28 high-precision off-diagonal cases; 4 diagonal cases
largest (G-C)/(2*pi*epsilon*G^2) in fixtures=0.982628220668
correction error: 18 exact-rational scalar checks
PASS (arithmetic checks only)
priority=20, peak_rss_bytes=14155776
```

The high-precision cases include h from 1e-50 to 1e30 and epsilon from 1 to 1e-12; these check the normalization and near-diagonal algebra, not the PDE. The proof has separate analytic derivations by polar coordinates, level sets, norm-resolvent convergence and nonnegative chains.

Opened actual lean/OAI/Analysis/HotSpots/Main.lean (SHA 3a4d4d6f29c7a9de7065b17f01d741df3904a1d6); it contains the noncritical theorem and imports further modules. No Lean compilation or axiom/dependency audit. Web searches of both unrelated titles with error/arxiv terms surfaced repository/catalogue pages, no directly relevant replacement or refutation in the returned results. Opened the theorem passages of Bañuelos and Deng–Jiang–Yang again to confirm non-strictness, simplicity, and maximum-modulus scope.

## 8. Verification document saved
Created VERIFY.md from the earlier verification, updating what was actually reopened in this session and the local source names. The theorem quotes remain exact source extracts. A first attempt to generate the document in a JavaScript template failed at parse time because Markdown backticks conflicted with the string delimiter; it made no filesystem changes. Used a small pathlib text operation instead. Fresh main TeX confirms OpenAI/date metadata for both hot-spots and MTW; MTW build/paper.tex failed, while build/main.tex succeeded. Opened Lean scope docs 360 and 058. The current spot check and complete opened-source inventory will be appended next.

## 9. Completed verification and report
Saved the final VERIFY.md, including all three candidate statements verbatim (both principal MTW theorems), the comparison, actual opened follow-ups and Lean artifacts, literature verdict PARTIAL-CLAIMED, and the new singular-limit spot check. Saved final REPORT.md with the requested continuation verdict PROVED for this interior proposition only, commands, exclusions, limits and next step. All load-bearing moment constants were derived twice, and both norm and chain arguments give the same limit.

One attempted delete-and-add replacement of REPORT.md was rejected by apply_patch as duplicate operations on one target; it made no changes. Corrected with an ordinary update. Final text audit command: OMP_NUM_THREADS=1 nice -n 15 python3 (small pathlib/re text audit). All four quoted theorem blocks match the fresh source snapshots exactly; report starts with the required verdict; the row update is three sentences; code fences, control characters, and local links pass. Only task-folder files were written. No git, subagents, builds, GPU, accounts, posting, or external state changes.
