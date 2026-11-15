# T054 round 5 log

Task: “Verify: has open problem T054 been settled by the OpenAI math release?”
Start observed: 2026-11-15T07:23:36.996674+04:00

## Step 1 — orientation and earlier work
Read startup memory and compute state, and listed the three predecessor folders. Read all predecessor REPORT.md, LOG.md, PROOF.md where present, and Python scripts. The first folder has no PROOF.md or Python scripts. No subagents, git, shared mesh/checklist/brain writes: this task explicitly confines all mutations to this directory. Compute state was warn/owner_away_open (CPU saturated); only tiny single-thread work is planned. Shell programs use OMP_NUM_THREADS=1 nice -n 15; nice reports a setpriority warning inherited from earlier runs; verify actual priority below.

## Step 2 — five-minute literature check started
Web searches: `"random regular graphs" "quantum unique ergodicity" 2026`, `"GOE bulk universality" "OpenAI"`, `"2610.08127"`. Opened arXiv:2610.08127 and github.com/openai/math. Results reproduce known bulk universality and existing older QUE qualifications; no new settlement identified. Follow-up direct opens next.

## Step 3 — bounded search complete; extension selected
The update check finished within five minutes. Opened the current release history (latest heading October 29, no family-219 update), Huang–Yau arXiv:2102.00963v3 full HTML, He–Huang–Wang arXiv:2610.08127v1 full HTML, and the family-219 community page. Targeted November QUE and GOE correction/refutation searches found no new primary result beyond those already recorded. No SOLVED_ELSEWHERE.md is warranted: the known deterministic-test interpretation is already covered in round 3, while stronger QUE remains unspecified. This is a bounded negative search, not proof of absence.

Choice, before doing the extension: replace the bounded-increment subset estimate by a variance-sensitive Bernstein estimate and use a finite net in each eigenspace. The earlier entrywise route spends powers of L both in the weight bound and in the eigenspace compression. The new route should require k much larger than L^2(M+log N), with M the largest eigenspace dimension, hence L^2(L^2+log N) in general. Preserve prescribed deterministic sets and the all-unit-eigenvector hypothesis; do not claim graph-dependent sets or validate the OpenAI proof.

## Step 4 — independent recheck of round 4
Re-derived the martingale increment from the two conditional means: (N-q)/(N-j) times (x-mu). It is bounded by 2b; q increments give exponent t^2/(8qb^2). The projection identity Q_lambda(i,i)=sup |u_i|^2 bounds each eigenspace dimension by L^2. Thus the entrywise threshold t=kr/(NL^2) yields exactly k^2 r^2/(8qL^8), including repeated eigenspaces. The earlier mathematical claim holds.
Rerun command: `OMP_NUM_THREADS=1 nice -n 15 python3 -c "import runpy; runpy.run_path(previous audit_subsets.py, run_name=__main__)"` (the complete path is in the executable tool log). No bytecode or other writes in the predecessor folder.

## Step 5 — rerun output and fresh original sources
Round-4 audit rerun passed: 189 cases, 6,132 subset instances, 7,032 conditional-prefix checks, 6,078 earlier-variance instances, 538 repeated-eigenspace compressions, and 340 coordinates in four Walsh ensembles. Runtime 0.219 s, peak RSS 17,154,048 bytes, niceness 20, OMP_NUM_THREADS=1.
Reopened all three main theorem TeX sections using web open and read-only GitHub fetch; saved fresh source files here. Fresh lean/docs listing contains 245 files, 218.md present, 219.md absent. This confirms the earlier family-219 scope observation, not proof validation.

## Step 6 — proof and independent audit saved
PROOF.md proves the variance-sensitive finite-population Bernstein bound from pair averaging of elementary symmetric polynomials, then a 1/4-net argument in each complete eigenspace. Result: failure <= epsilon + 2N 9^M exp[-k^2 r^2/(8L^2(q+kr/6))], q=min(k,N-k). Explicit inversion and simple-spectrum specialization are derived. The sufficient set-size condition is k/[L^2(M+log N)] -> infinity, M<=L^2.
Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_bernstein.py`. Output: PASS 189 scalar cases, 6,132 subset instances, 595 Bernstein tails, 189 exact rational mgf comparisons, 3,465 pair-smoothing identities; PASS 3,654 constant substitutions and independent quadratic-root inversions; PASS 536 repeated-eigenspace compressions and 69,680 direct quadratic-form comparisons. Counterexample miss-support probabilities computed independently by binomial ratio and product for s=2,4,8,16,32,64,128; at s=128 probability 0.36500164, consistent with the proved e^(-1) limit. Exact block Walsh matrices checked at s=2,4,8. All passed; elapsed 1.869 s, peak RSS 14,893,056 bytes, niceness 20, one thread.

## Step 7 — source and formalization follow-through
Opened the current lean README and scope note 218.md, fetched formalization.yaml, and reopened Latent Seminar and the community GOE page. The scope note covers a finite-graph buffered Ising companion rather than conformal universality. The exposition disclaims full proof verification; the community page (updated November 9) still has no contributed notes and labels automatic notes unreviewed. Its additional different-model literature leads are not cited as papers because they have not been opened. No newly identified matching formalization or specialist validation.

## Step 8 — verification and report saved
Wrote VERIFY.md with fresh exact theorem quotations, clause-by-clause comparisons, opened-source register, three-sentence row update and spot check; wrote REPORT.md in the later requested continuation-verdict format. The release-scope verdict remains explicitly PARTIAL-CLAIMED inside both files.
Exact runnable previous-audit command: `OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import runpy; runpy.run_path("~/codex_op_1114r4/briefs/AV_T054/audit_subsets.py", run_name="__main__")'`.

## Step 9 — final audit and completion
Reopened all three manuscript READMEs: author OpenAI, dates September 23 / October 5 / September 23, 2026 as recorded. Reopened arXiv abstracts for Jaehun Lee and Jiaoyang Huang–Horng-Tzer Yau to verify exact author lists and scopes; the latter was also read at Theorem 1.4 and its unconditional-event paragraph.
Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_artifacts.py`. PASS all three exact theorem quotations (385 / 800 / 1,624 characters) against fresh source plus round 1, round 3 and round 4 snapshots; PASS no matching selected Lean main theorem; PASS verdict prefix and three-sentence row; PASS no control characters. Peak RSS 17,661,952 bytes. No check failed.
Final self-check: the replacement-sampling moment bound is an upper bound for the without-replacement mgf, not an independence assertion; all-direction delocalization is used before taking the eigenspace net; complex vectors are covered by real symmetric operator norm; complements use q=min(k,N-k); exceptional graph probability remains epsilon. The finite audit net has 130 directions and is not presented as the analytically constructed 9^m net.
All writes remained inside this folder. No git, external mutation, subagent, heavy computation, GPU, MLX, torch or Lean compilation was used. Brain/checklist/mesh state was not changed because of the task-specific local-only restriction.
Completed 2026-11-15T07:30:49.006802+04:00.
