# T304 continuation log

## Step 1 — orientation and earlier work

Task: “take the NEXT checkable step on this problem, building on that work.” Session began 15 November 2026 (Asia/Tbilisi); exact first user clock time was not supplied. Read prior REPORT.md, LOG.md and VERIFY.md in ~/codex_op_1114/briefs/AV_T304. Prior PROOF.md and scripts are absent; the prior result is a scope comparison and an algebraic spot check, not a computation. Read the startup memory index and compute state read-only. The task's current folder-only rule supersedes shared brain/checklist/mesh writes; none were attempted.

Commands so far: short `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -` reads of prior files and the source inventory. `nice` reports `setpriority: Operation not permitted`, as in the earlier session; no heavy computation is being run. Compute state: warn, owner_away_open, CPU saturated. All work remains small, single-threaded, without numerical packages.

## Step 2 — bounded update search

Used web search for the exact sampling title; arXiv:2611.05813; OpenAI/math sampling error; log-concave OpenAI November 2026 correction; the proximal-sampling title with error/correction; and subpolynomial query complexity gap. Opened https://arxiv.org/html/2611.05813v1, https://arxiv.org/html/2611.03442v1 and https://arxiv.org/html/2611.15849v1. These are the same November follow-ups recorded earlier. No newly located matching minimax bound or refutation changes the picture. This is a limited search, not a universal absence claim. Update search ended within five minutes. No SOLVED_ELSEWHERE.md is warranted.

## Step 3 — independent recheck, begun

Recheck both the actual theorem quantifiers against the saved original TeX and the prior Gaussian absorption identity using an orthogonal-completion argument. Read the implementation induction before choosing the one extension; record the choice before proving anything new.

## Step 4 — recheck holds; one extension chosen

Independently read the original introduction: its epsilon is a dimension exponent; TV tolerance is 1/10, joint exact value-and-gradient oracle, C² normalized curvature class with supplied mode. Thus the earlier scope conclusion holds. Independently re-derived Lemma 7.1 via the orthogonal block matrix [[P,-a],[aᵀ,sqrt(1-||a||²)]], where a=v/(2D_s): its top block maps independent standard normals to standard normals, giving the negative restoration sign and the claimed marginal law. This is a different derivation from the earlier covariance/characteristic-function checks.

Choice before further proof: check the conditional W₂ error recurrence in Proposition 7.7 (source label prop:compiler-accuracy; printed numbering will be verified), including the uncached expression tree and its 1/4 accuracy loss. This extends the earlier exact-center identity to the actual inaccurate-center recursive use, the main remaining local independence concern identified in VERIFY.md. Prove a finite-tree inequality from explicit hypotheses in PROOF.md; check the claimed 1/12 exponent margin. Treat circuit size, coefficient, stability, and standalone lower-level accuracy estimates as hypotheses; this cannot certify the whole sampling result.

Reopened current original TeX via GitHub read connector: all three introductions, sampling implementation, history.md. The fetched text is retained in the tool session and will be saved with hashes before completion. History still ends 29 October and has no correction for these candidates. Read the saved Lean NoisyCenterSquaredError.lean and Main.lean plus scope note 139; no build attempted.

## Step 5 — sources and interim deliverables saved

Saved the five reopened source files via apply_patch; copied the remaining earlier source snapshots read-only into this folder. Retained prior VERIFY.md with an explicitly dated continuation prefix and wrote an interim REPORT.md. Current source text matches earlier text after stripping the snapshot extra trailing newline (hash comparison follows in final audit). No program or write touched the earlier folder.

## Step 6 — local proof saved and source audit

Wrote PROOF.md with: orthogonal-completion recheck; one inaccurate-center W₂ inequality; independent affine-expression coupling; finite-tree expansion; the 1/12 exponent margin; and a scalar counterexample showing that shared supplying subtrees invalidate the product coupling. All analytic circuit estimates are explicitly assumed. Also checked bias: independent errors need not be centered, so a root-sum-square improvement is unjustified.

Command: short single-threaded pathlib/re script via `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -`. Output: every retained TeX snapshot agrees with its earlier counterpart after trailing-whitespace normalization; all three main-theorem environments are exact substrings of VERIFY.md. No source theorem changed. An additional small read of current arXiv abstract pages checks revision history rather than relying only on v1 HTML; results recorded next.

## Step 7 — exact arithmetic audit and final local result

Command: `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -I -B audit_local.py`.
Output (all assertions passed):
```
Gaussian completion: U U^T = I_3; P P^T + aa^T = I_2 (exact)
Shared-center counterexample: residual=7/8; variance=33/32 by both methods
Finite-tree recurrence: bottom-up = path expansion <= bound for heights 1 through 6
Exponent margin: 1/3 - 1/4 = 1/12 (exact)
```
The process finished immediately, uses only Python's standard library, and never starts workers. `nice` again reported its sandbox priority limitation. No heavy computation, GPU, network program, package installation, git command, or outside-folder write occurred.

A second short hashlib script checked each of five reopened source snapshots against the repository blob SHA-1 from the connector (allowing only trailing-newline normalization); all five match. Ten source TeX files match the earlier worker's snapshots after trailing whitespace normalization. All three main theorem quotations remain verbatim.

Current arXiv abstract pages opened: 2611.05813 (Huanjian Zhou, Taiji Suzuki), 2611.03442 (Wei Guo, Bo Yuan, Ye He, Jiaming Liang, Molei Tao, Yongxin Chen), and 2611.15849 (Evan Dogariu). All show only v1; dates and authors agree with the earlier report. These extra revision-history reads confirm the initial bounded update search; they are not a renewed broad literature search.

Appended the new Spot check to VERIFY.md, with exact hypotheses, the counterexample and current sources. Replaced interim REPORT.md by the final continuation-format PROVED verdict for the local implication only. The original row's literature classification remains PARTIAL-CLAIMED. The next independent check is the numerical-interface coefficient/scale estimates feeding fixed-seed stability; no global proof-correctness conclusion is asserted.

## Step 8 — completion audit

A final single-threaded pathlib/re check confirmed the continuation verdict and its explicit assumptions, all three theorem quotes, retained three-sentence status recommendation, ten numbered proof displays, paired Markdown fences/display delimiters, and the six deliverables. No new failure or scope change arose. Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026; exact user request clock time was not supplied.
