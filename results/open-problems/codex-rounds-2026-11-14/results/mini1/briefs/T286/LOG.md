# T286 work log

Task: “push this problem forward by one checkable piece.” Session started 2026-11-14, approximately 22:09 Asia/Tbilisi.

## 1. Orientation and literature check

Commands: `pwd`; `ls -la`; `cat ~/.claude/compute/compute_state.json`; read startup memory and mesh protocol. All shell programs in this session are small read-only commands or short file edits; numerical work, if any, will use one thread and `nice -n 15`.

The folder initially contained PROMPT.md, codex.log and run.pid. Compute state: status warn, mode owner_away_open, CPU saturated. No heavy computation planned.

The task-specific rule forbids writes outside this folder. Therefore brain/checklist/mesh commands that mutate their external stores are not run; orientation is read-only. No git or subagents.

Web searches (2026-11-14): `"2408.03733" general activation proof`; `"Bayes-optimal learning" "extensive-width" neural network 2026 2025`. Results include the source paper and potentially relevant follow-ups arXiv:2505.24849 and arXiv:2605.10395. Opening the primary sources next. Search window limited to ten minutes.

## 2. Primary-source follow-up (22:10 local)

Opened arXiv abstract pages 2408.03733, 2505.24849, 2605.10395, 2510.24616; the PRX publisher page DOI 10.1103/56sb-pdh6; and full HTML 2510.24616v3 and 2605.10395v1. Opening 2408.03733v2 HTML returned 404; this is a failed fetch, not evidence about the mathematics.

The 2505 paper explicitly points to superseding arXiv:2510.24616, published in PRX in July 2026. The 2605 paper explicitly describes its main decoupling argument as heuristic. Next check: the latest 2510 version and its proof-status caveats. There is already evidence of substantial progress beyond the source paper, but not yet evidence of a rigorous solution. If that is confirmed, the task's literature-stop branch applies; no new special-case theorem will be started.

## 3. Status audit and choice

Opened latest full HTML https://arxiv.org/html/2510.24616v5. Checked Remark 4, Appendix B.6, Figures 5 and 9 and their surrounding text. The general-activation theory remains conjectural; the appendix is a potential proof route. The paper treats ReLU and tanh explicitly and examines algorithmic metastability. This is substantial follow-up, not a theorem resolving T286. Its dates precede the prompt's November 2026 status date; it corrects the amount of known progress, not the statement that the rigorous general case is open.

Opened original full HTML https://arxiv.org/html/2408.03733v1. Section 4 explicitly uses Conjectures 4.1 and 4.2 plus Theorem 4.3; the original full quadratic-learning claim was not proved there. Followed the later paper's citation to https://proceedings.mlr.press/v291/xu25a.html to check subsequent rigorous quadratic progress.

Choice: follow instruction 1's substantial-advance stop branch. Write SOLVED_ELSEWHERE.md (with an explicit warning in its contents that the general problem is not solved) and REPORT.md. No new proof or numerical computation. Before finalizing, independently check the primary sources for dates, sample scaling, and the distinction between optimizer experiments and a gradient-descent theorem.

## 4. Independent scope checks and final artifacts

Additional searches: `"Fundamental Limits of Matrix Sensing" arxiv`; `"extensive-width" "rigorous" "2026" neural Bayes`. Opened arXiv:2503.14121 abstract and v2 full HTML. The guessed v3 HTML URL returned 404; the abstract identifies v2 as latest. Checked Section 2.5, Theorem 2.10, and the uniqueness condition in Theorem 2.5. Recorded the exclusions κ=1, the positive noise assumptions and the exceptional set of sample ratios instead of calling all quadratic cases solved.

Opened arXiv:2610.23779 abstract and full HTML. Independently checked Section II.1's fresh-sample update and spherical constraint, and Section IV's sample-reuse caveat. This prevents mistaking its dynamics for the fixed-dataset GD statement in T286.

Cross-check of 2510.24616: equation (4) confirms n/d²→α and extensive width directly, rather than relying on the title; Remark 4 and Appendix B.6 establish that its claimed error formulas are not a completed general proof. Checked the journal date on the publisher page independently of the arXiv history. All cited authors copied from opened primary pages. No numerical constants from plots were used or extrapolated.

Wrote SOLVED_ELSEWHERE.md and REPORT.md. No PROOF.md or computation script because the literature-stop branch applies. Findings are substantial advances since the 2024 source, all dated before the supplied November 2026 status date. No claim of a post-November solution. Search and source reading completed well within ten minutes of the 22:09 start (clock check 22:10:59 during source audit).

Final file checks:

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /usr/bin/wc -l LOG.md SOLVED_ELSEWHERE.md REPORT.md
nice: setpriority: Operation not permitted
      37 LOG.md
      27 SOLVED_ELSEWHERE.md
      15 REPORT.md
      79 total

head -n 1 REPORT.md
VERDICT: PARTIAL literature status corrected; substantial follow-ups found, general theorem still open
```

The sandbox refused the priority adjustment for the tiny line-count check; it nevertheless printed the counts. No numerical workload was launched. Counts above refer to the files before this final log append. Report first-line format verified.
