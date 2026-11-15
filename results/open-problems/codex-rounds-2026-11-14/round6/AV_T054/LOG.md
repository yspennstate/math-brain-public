# T054 round 6 log

Task: “Verify: has open problem T054 been settled by the OpenAI math release?”
Session start: 2026-11-15, about 09:46 +04 (Asia/Tbilisi).

## 1. Orientation and scope

Read startup memory and compute state (ok, owner_away_open); listed rounds 3–5 and began reading their reports, logs, proofs, and scripts. All mutations remain in this folder, as explicitly required by this task; no shared mesh/checklist/brain mutation, git, or subagent. Only small one-thread computations are planned, under OMP_NUM_THREADS=1 and nice -n 15; actual priority and resource use will be printed by scripts. No predecessor files will be changed.

Started the bounded five-minute literature update with web searches for November 2026 fixed-degree QUE, the exact GOE title with corrections/errors, and arXiv:2610.08127. Opened arXiv:2610.08127 and current release history. The first still identifies He–Huang–Wang's known bulk result; history still begins October 29. Further opens and a source register follow.

## 2. Bounded update search complete

The update check finished within five minutes. Further web queries used “random regular graphs” / “QUE” / “November” / “2026” and the exact GOE title with error/refutation/correction. Opened Huang–Yau arXiv:2102.00963v3, its Theorem 1.4 and following unconditional probability discussion; the community GOE manuscript page (no contributed notes, automatic notes unreviewed); and Jaehun Lee's arXiv:2611.09215 abstract (mesoscopic eigenvalue CLT, not an additional spatial QUE result). No newly identified outside settlement changes rounds 3–5. The known prescribed-test QUE consequence was already established there. This is a bounded search, not a proof of absence. No SOLVED_ELSEWHERE.md is warranted. Web opens of AIProofWatch and the GitHub lean/docs directory returned cache misses; record these as failed opens, not read sources.

## 3. Earlier result re-derived; one extension selected

Independently checked the round-5 argument: for a fixed direction, centered squared mass has |z_i|<=L^2/N and mean square <=L^2/N^2; without-replacement exponential moments are bounded by replacement moments. Its scalar Bernstein exponent is N^2 t^2/[2 L^2(q+Nt/3)]. A 1/4-net costs 9^m and changes t to kr/(2N), giving exactly k^2 r^2/[8 L^2(q+kr/6)]. Summing over at most N eigenspaces yields its displayed bound. The all-direction hypothesis gives projector diagonal <=L^2/N and m<=L^2. The claimed threshold and inversion therefore hold. A rerun of its audit follows after reading the script.

Choice, before doing the extension: remove the exponential eigenspace-net factor using a proved matrix exponential inequality for sampling without replacement. Target failure bound is epsilon + 2N exp[-k^2 r^2/(2 L^2(q+kr/3))], with q=min(k,N-k), for every eigenvector including repeated eigenspaces. The sum of eigenspace dimensions is N, so the prefactor should be 2N, and k/(L^2 log N)->infinity should suffice without simple spectrum. Prove the sampling comparison by an explicit coupling and convexity, and the replacement matrix estimate by Golden–Thompson plus a scalar matrix-mgf bound. This extends only the quantitative prescribed-set result; it is not a new universality proof or a novelty claim.

## 4. Earlier audit rerun

Read all requested reports, logs, proofs and six predecessor scripts. Command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B -c 'import runpy; runpy.run_path("~/codex_op_1114r5/briefs/AV_T054/audit_bernstein.py", run_name="__main__")'
```

Exit 0. PASS 189 scalar cases / 6,132 subset instances / 595 tails / 189 exact mgf comparisons / 3,465 smoothing identities; 3,654 constant and quadratic-inversion checks; 536 compressions / 69,680 quadratic forms; block-Walsh examples. The s=128 support-miss probability is 0.36500164. Runtime 1.805 s, peak RSS 16,695,296 bytes; niceness 20, OMP_NUM_THREADS=1. The nice warning reflects inability to raise inherited priority from 20; the process already runs at lower priority than requested. Earlier result holds, both by independent derivation above and unchanged audit. No bytecode or other predecessor mutation (-B).

Fresh web opens of all three original theorem TeX sections succeeded. The displayed main theorem environments match the earlier quotations. Searched primary matrix-concentration sources for the chosen extension; opened sources are registered below when read. These methodological reads are separate from the completed five-minute settlement search.

## 5. Matrix proof and audit saved

Saved PROOF.md with the target bound and every concentration step. The without-replacement coupling is explicit: draw q indices independently, extend their distinct set to a uniform containing q-subset R, and condition on R. Conditional expected multiplicity of each i in R is exactly 1. Conditional Jensen applies to convex trace exp. For a compressed eigenspace, A_i=a_i a_i^T, sum A_i=I, ||A_i||<=L^2/N, and the centered matrix variance is <=(L^2-1)I/N^2. Golden–Thompson is applied to two matrices at a time; a scalar identity bound on each independent matrix mgf permits iteration. Summing 2 dim(V) across eigenspaces gives exactly 2N.

Opened David Gross and Vincent Nesme, arXiv:1001.2738v2 abstract and three-page PDF, especially Section C / Lemma 2 / final convex comparison; and Joel A. Tropp's author-hosted User-Friendly Tail Bounds PDF, equation (2.6) and the warning against a naive multi-factor iteration. The proof uses the valid scalar-mgf conditional iteration, not a multi-factor Golden–Thompson assertion. It imports the standard two-factor Golden–Thompson theorem explicitly.

Saved audit_matrix.py before running it. Planned checks: exact rational coupling conditional means through N=6, noncommuting rank-one tight frames, exact centered-square and finite-population matrix variance identities, direct eigenvector mass versus compressed quadratic forms, separately enumerated replacement/without-replacement trace mgfs, independent matrix exponential power series, tail constants and independent quadratic-root inversion. Resource caps: 120 s wall alarm, 100 s CPU, 256 MB data limit; standard library only, one thread.

Read-only GitHub fetch also retrieved and saved fresh original theorem sources, formalization.yaml, Apache-2.0 LICENSE, and the lean/docs filename inventory. There are 245 scope notes, 218.md present, 219.md absent. Web opened lean README, catalogue and scope 218: the latter is a different finite-graph Ising companion, not conformal universality. No matching selected main theorem was identified and no Lean compilation was run.

First audit command `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_matrix.py` stopped before mathematical checks: macOS rejected setting the data hard limit to 256 MB because the inherited hard limit is lower. Corrected the script to use the minimum of 256 MB and the inherited hard limit. No mathematical assertion failed and no resource limit was relaxed.

The second attempt had the same setup error. Correction to the preceding diagnosis: an independent resource inspection printed DATA=(9223372036854775807,9223372036854775807), AS the same, and RLIM_INFINITY=9223372036854775807. The inherited hard limit is unlimited, so “because the inherited hard limit is lower” was an unsupported inference. This environment rejects the requested DATA limit for an undetermined reason. The script now reports that guard as unavailable; CPU/wall caps remain, the finite audit stores only tiny N<=8 matrices and N<=6 coupling tables, and measured peak RSS must stay below 1 GB. No mathematical check has yet failed.

## 6. Matrix audit passed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_matrix.py`. Exit 0. Output:

```text
DATA_limit_unavailable current limit exceeds maximum limit inherited 9223372036854775807
nice 20 OMP_NUM_THREADS 1
PASS exact_coupling_cases 19 ordered_draws 52500 subset_extensions 56262 conditional_count_means 584
PASS tight_frames 12 noncommuting_populations 12 exact_subsets 1008 matrix_second_moments 78 direct_mass_forms 4032 matrix_tail_comparisons 216
PASS noncommuting_mgf_comparisons 72 independent_exponential_series 18 two_factor_Golden_Thompson_checks 38
PASS exponent_substitutions_and_root_inversions 7020 eigenspace_dimension_compositions 4095
peak_rss_bytes 15597568 elapsed_seconds 1.154
```

The coupling and second-moment identities are exact rational computations. Trace-mgf/tail checks use 65-digit Decimal arithmetic, supplemented by a separate exponential power series; they are finite audits, not proofs of the general inequalities. All 12 matrix populations genuinely contain noncommuting rank-one matrices, so the audit is not restricted to scalar/diagonal cases. The proof's independent centered-square versus ordered-product derivations agree, and both upper and lower tails and complementary sets are included. Final threshold constants were checked algebraically and against the independently solved quadratic root.

Compute state re-read at 09:54:23 +04: ok / owner_away_open. No heavy work. Next: write the verification/source register and final report, then check theorem quotations and artifact consistency.

## 7. Additional attempt to break the bound

The small tight-frame tail checks can have bounds above 1, so they do not strongly test the tail constants. Added a focused check at N=64 and 128 with four equal-sized groups of directions (two different orthonormal pairs). These frames have exactly L^2=2, rank 2, and noncommuting row matrices. Enumerate subset occupancy classes with exact multivariate hypergeometric weights, rather than all subsets. Test both the sampled set and its complement at thresholds where the matrix tail bound is below 1 and the actual tail is positive. This specifically addresses the potentially vacuous small-N checks; it does not add a second mathematical extension.

The first expanded audit passed every tail inequality, but its final test-design assertion expected all 12 selected bounds to be below 1. Two (N=64,k=16,r=1/2 and its complement) equal 1.6974914, so that assertion failed. The other 10 are below 1 and every actual probability is positive. Retained all 12 cases and corrected the expected nonvacuous count to 10. No concentration inequality failed; the failed assertion was the audit's incorrect nonvacuity expectation. Examples: at N=128,k=32,r=1/2 actual=0.000066778554, upper=0.72036925; at r=9/10 actual=1.1354732e-19, upper=0.027369637. The complementary-set values agree exactly after scaling r by one third.

Final rerun `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_matrix.py` passed (exit 0). All original counts in Step 6 unchanged. New grouped output: PASS 12 tails, 7,514 occupancy classes, 10 nonvacuous bounds, 12 positive actual tail probabilities. Runtime 1.513 s, peak RSS 17,596,416 bytes, OMP_NUM_THREADS=1, niceness 20. No mathematical failure found.

## 8. Deliverables and final review

Saved REPORT.md and VERIFY.md, including all three fresh exact theorem quotations, clause-by-clause comparison, primary-source register, bounded negative follow-up finding, Lean scope limits, and three-sentence replacement row. REPORT.md follows the later continuation verdict format, with PARTIAL-CLAIMED reserved for the release's explicit main-theorem scope. No newly discovered outside settlement warrants SOLVED_ELSEWHERE.md.

Reviewed the proof's vulnerable points: the coupling conditions on labels, not matrix values, so repeated population elements cause no problem; only trace convexity is used; matrix variance retains product order; the mgf iteration uses a scalar identity bound before the next step; dimensions sum to N; complementing changes the sampled cardinality q but leaves the relative normalization k; L=1 and the zero-variance case are safe because the proof uses positive upper bounds on b,v; k=N is handled separately. Complex vectors are controlled by the same real symmetric compression. The unconditional delocalization exception remains epsilon, and no overwhelming-probability claim is imported.

## 9. Artifact audit and handoff

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_artifacts.py`. Exit 0. PASS exact theorem quotations against fresh source plus rounds 3,4,5: GOE 385 characters, Anderson 800, Ising 1,624. PASS current Lean catalogue/scope inventory, license presence, continuation verdict, three-sentence row, Python syntax and control-character checks. Peak RSS 20,381,696 bytes. Final non-log hashes: REPORT.md `ba688bcd294103ce420d754585a1ef6d6ab9ddd28ad2ef79c007e5c8d26d97d2`; PROOF.md `4c61b3810239ebf9c33b0abf081f42ad5a2f284ab07f962cf3bad6b4c85f7017`; VERIFY.md `334a5511487d0f57bc3fdc3de18b749a10cbfa20b9907ee881d5e1556e0f383b`.

The chosen matrix-concentration extension is complete. The next worker should specify a stronger QUE observable class, or examine necessity of the logarithm with a full counterexample ensemble. No optimality, arbitrary graph-dependent QUE, or validation of the OpenAI universality proof is claimed. All writes stayed in this folder; predecessors remained read-only; no git, external mutation, subagents, GPU, MLX, torch, large computation or Lean build.

Task: “Verify: has open problem T054 been settled by the OpenAI math release?” — session start approximately 2026-11-15 09:46 +04.
