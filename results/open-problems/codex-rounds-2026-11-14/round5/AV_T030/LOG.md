# T030 round 5 log

Task: “Verify: has open problem T030 been settled by the OpenAI math release?”
Started: 2026-11-15T07:22:32.960884+04:00

## 1. Orientation and literature search
Read file lists and REPORT.md, LOG.md, PROOF.md where present and VERIFY.md in rounds 1, 3 and 4, using OMP_NUM_THREADS=1 nice -n 15 shell reads. Combined output was truncated, so individual source reads follow. Read compute state (warn, owner_away_open); no heavy computation planned. nice reports a sandbox setpriority warning; inherited priority will be checked. The task-specific folder-only rule excludes global brain/checklist/mesh writes, so those are not run. No subagents or git.

Used web search tool with exact hot-spots title and OpenAI/2026/convex-planar variants. Leads include the already known conditional nonsmooth extension arXiv:2610.32920; no new complete strict nonsmooth result in returned results. Five-minute search continues with primary sources.

## 2. Bounded literature update and fresh sources
Web search completed within the initial five minutes: exact title with error/refutation/correction, hot spots November 2026 convex proof, plus earlier title queries. Opened arXiv HTML 2610.12622v1 (Krzysztof Burdzy), 2610.32920v1 (Rodrigo Bañuelos on the full paper; abstract metadata has a spelling error), and 2610.18546v2 (Haiyun Deng, Xuyong Jiang, Xiaoping Yang). Same non-strict conditional simple-eigenvalue results and strict maximum-modulus result as earlier; no complete strict general-convex resolution located. No SOLVED_ELSEWHERE.md warranted. Search results also contained expositions and unrelated weather results, which are not mathematical evidence.

Read round-4 PROOF.md and check_singular_limit.py and round-3 PROOF.md and audit_resolvent.py. First source fetch failed schema validation (required repository_full_name); corrected the field and fetched all sources successfully. Saved fresh introduction, boundary and reciprocal sections, MTW introduction, symmetry paper, Lean scope/target/main through read-only github_fetch_file, then local apply_patch. Reciprocal SHA bcb125482dbfe6874ffe4582625c01ea66571ca9; boundary SHA 31fde0ba6a572f90d0003a7aa91dc96ee9dfdf5e; introduction SHA ca7f7f292379a95899f04a1de411eb610d1fe9ab. Same contents as earlier snapshots. No git used.

## 3. Chosen extension
Recheck the previous uniform Green-moment and regularization estimates independently and rerun its small arithmetic script. Then prove lem:bordered: the radial boundary passage at fixed compact support, cutoff removal, and full boundary-kernel finiteness. This is exactly the next step in round 4. The main hazard is assuming a Poisson section belongs to L2(q); instead smooth it once with G and use nonnegative chain integrals. Explicit constants and a constant-density counterexample to the invalid L2 assertion will test this point.

## 4. Previous result holds
Command: OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/AV_T030/check_singular_limit.py. It passed p=1..8 moment recurrences, 28 off-diagonal regularization cases, four diagonal cases and 18 exact-rational correction checks. Largest fixture ratio 0.982628220668; inherited priority 20; peak RSS 15,204,352 bytes. No writes in the old folder. Independently, the Green majorant has level sets bounded by 4*pi*exp(-4*pi*t), yielding moment p!/(4*pi)^(p-1); the exact reciprocal identity G-C=4*pi*epsilon*f*G*C with 0<=f<=1/2 recovers the previous sqrt(3*A/(2*pi)) source-error constant. Thus the main round-4 claim holds.

## 5. Boundary estimates derived
Using P_s<=1/(pi*|y-s|), the L^(3/2) Poisson integral is bounded by 4*sqrt(2/pi); the L^3 Green integral is bounded by 3/(8*pi^2). Holder gives sup TP_s <= H=12^(1/3)*A/pi. This smooths each boundary section into L2(q). Also integral P_s dx=1/2 exactly, and for delta=|s-t|>0 the product integral is at most 2*A/(pi*delta). For n>=2, the R_n chain equals <F_s,T^(n-2)F_t> with F_s=TP_s, so its tail is at most H^2*q(D)/(1-d). This avoids pairing an unsmoothed Poisson section as an L2 vector.

Saved a provisional REPORT.md before the detailed proof and stress checks. Reopened the full theorem passages in Bañuelos and Deng-Jiang-Yang to confirm the limits and author spelling. No new settlement evidence.

## 6. Boundary lemma proof and independent arithmetic saved
Created PROOF.md with the full conditional proof of lem:bordered from the earlier interior reciprocal-inertia proposition. Fixed compact support makes radial Green sources converge uniformly and in L2; the bounded resolvent then yields the boundary pairings. A positive diagonal congruence and finite-matrix inertia closure give each compact-support bordered matrix. Nonnegative product-chain monotone convergence removes the support cutoff; explicit smoothing bounds prove the limits finite. Independently differentiated the radial Green kernel to verify both Poisson and double-boundary constants.

Created and ran OMP_NUM_THREADS=1 nice -n 15 python3 check_boundary_limits.py. Output: exact moment/Holder constants; four Poisson-square series/primitive comparisons; five increasing cutoff integrals (normalized values 6.853971, 16.034686, 34.455067, 71.296429, 135.768811); 120 one-boundary and 75 two-boundary high-precision cases; 20 exact zero-potential inertia checks and 140 independent squared-distance/sign identities. PASS. Inherited priority 20, peak RSS 14,827,520 bytes; under one second.

Stress case: q=dx satisfies the form inequality with d=1/2 by elementary square-extension estimates, yet integral over |x|<=R of P_s^2 is [-R^2-2*log(1-R^2)]/(4*pi), diverging as R tends to one. A separate local cone proves the same divergence. This is outside no manuscript hypothesis: it tests why the proof must avoid the invalid L2 step. The manuscript explicitly avoids it; no error is reported. R(s,s) may likewise be infinite; only distinct boundary pairs enter the lemma.

## 7. Source metadata and remaining scope
Freshly fetched hot-spots and MTW main TeX confirms author OpenAI and September 24/25, 2026 dates; saved source-hot-main.tex and source-mtw-main.tex. Reopened and saved lean/docs/360.md and 058.md, as well as 369.md, the actual HotSpots target and supplied Main.lean. The hot-spots target still assumes SmoothBoundary; Main.lean imports further modules and contains a proof term, but no local build or axiom/dependency audit was run. The unrelated scope documents concern optimal transport and complex domains, not Neumann extrema. Read-only GitHub issue search repo:openai/math "hot spots" returned issues=[].

Read startup memory at its actual path ~/.claude/brain_startup.md and the memory index directly, without commands that mutate brain logs. Read the remaining earlier logs separately after truncation of combined outputs. Saved sources are exact fetched text apart from final newline. All filesystem mutations still occur only here.

## 8. Verification document saved
Created VERIFY.md with four exact theorem blocks extracted directly from the fresh sources (both principal MTW theorems), full row comparison, actual follow-ups and Lean files opened, and a three-sentence row update. The literature verdict remains PARTIAL-CLAIMED for smooth convex domains. Added the current boundary-lemma spot check, its assumptions, explicit estimates, successful arithmetic checks and remaining limits. Earlier comparator/exposition records are distinguished from this session's actual source reads. No complete-proof certification is made.

## 9. Final report and proof audit
Replaced the provisional report with VERDICT: PROVED for the boundary lemma derived from the earlier interior result, retaining the separate PARTIAL-CLAIMED literature finding. Saved sources_manifest.json with the twelve opened repository sources, blob identifiers and direct URLs. Read the earlier saved conclusion section to identify the next checkable step precisely; it is not claimed checked here. Next: final bordered-form algebra, lem:hilbert and eq:sum-energy.

Audited signs, normalization, the compact-support L2 passage, product-space monotone convergence, both zero diagonals, q=0, distinctness, non-atomicity and d<1. No new defect found. Added the explicit radial error constant used by the script: for eta=1-R, 4/eta^2+32/eta^3+32/eta^4, equal to 352400 at R=0.9. One patch attempt failed to match an incomplete context line and made no changes; the corrected patch succeeded. No mathematical finding changed.

## 10. Final artifact validation
Command: OMP_NUM_THREADS=1 nice -n 15 python3 (small pathlib/re/hashlib audit). PASS: all four quoted theorem blocks occur verbatim in the fresh sources; all twelve local source snapshots match their upstream GitHub blob identities allowing a terminal newline; row update has three sentences; REPORT.md has the required continuation verdict and no provisional wording; Markdown fences, control characters and local links pass. Peak RSS 18120704 bytes; inherited priority 20. No further computation needed.

Finished: 2026-11-15T07:33:36.442783+04:00. Only the current task folder was written; no git, subagents or external mutations.
Task: “Verify: has open problem T030 been settled by the OpenAI math release?” — 15 November 2026, 07:22 Asia/Tbilisi (start).
