# T248 work log

Task: “push this problem forward by one checkable piece.” Received 2026-11-14, session first clock reading 22:08:29 +04.

## 22:08–22:11: orientation and literature search

All writes are restricted to this folder. The task-specific restriction overrides the global mesh/checklist/brain write rituals, which would mutate files elsewhere. Read the startup memory, the compute state (warn/cpu_saturated; no heavy computation planned), and the existing T248 He2-spike memory. That memory is provisional and is being treated as a lead only. No subagents, git, external writes, or background processes.

Read-only shell commands: `pwd`, `ls -la`, `rg --files` for startup memory, `cat ~/.claude/brain_startup.md`, `head ~/brain-views/BRAIN_INDEX.md`, `rg` for T248 in TOPICS.md, and `cat` of the T248 Gaussian-input He2-spike card. The directory initially contained only PROMPT.md, codex.log, and run.pid.

Web searches:
- random feature conjugate kernel Tracy Widom edge universality 2025 2026
- Benigni Péché largest eigenvalues nonlinear random matrices 2201.04753 Tracy Widom
- "random features" "edge universality"
- "conjugate kernel" "Tracy"

Opened arXiv pages 2201.04753, 2005.11879, and 2610.41416, plus full HTML of 2201.04753v1 and 2610.41416v2. Key new lead: Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form concentration*, arXiv:2610.41416v2, revised 4 November 2026. Their Assumption 1.1 requires independent centered columns with common covariance and Lp quadratic-form concentration bounded by a constant times the Hilbert–Schmidt norm. Assumption 1.2 requires bounded positive population covariance and a regular right edge; the aspect limit excludes 1. Checking whether this actually applies to a nonlinear feature subclass before deciding the required literature-stop outcome.

Commands running Python in this session use `OMP_NUM_THREADS=1 nice -n 15 python3`; all are tiny file operations or exact scalar checks.

## Literature decision and stop

The initial file-write command printed `nice: setpriority: Operation not permitted`, followed by `LOG.md written`. The sandbox denied the priority adjustment; no further Python or numerical programs were run. There were no scalar numerical checks, simulations, or data files. Later writes use the patch tool.

Additional web searches: `"2610.41416" "neural"`, `"conjugate kernel" "Tracy-Widom" 2026`, and `"random feature" "quadratic form concentration"`. These led to arXiv:2609.09440v2. Opened its arXiv page and full HTML. Also opened arXiv:2602.17960 and its full HTML as a cited predecessor; it is not needed for the reported claim. Inspected Chen–Lyu Assumptions 1.1–1.2, Theorem 1.3, Corollary 1.4, and Remark 1.5, and Ma–Misiakiewicz Theorem 2.4, Proposition 2.8, and Example 2.11. All search and full-text tool calls were completed within the ten-minute literature budget measured from 22:08:29 +04.

Decision: a substantial advance exists. Follow instruction 1: write SOLVED_ELSEWHERE.md and REPORT.md, then stop. No independent research piece is selected, so instructions 2–4 do not initiate a new project. The files distinguish a conditional regular-covariance application from the unverified full T248 statement.

Audit: checked transposition both by equality of nonzero singular-value squares and direct normalization; checked conditional mean zero from fixed input norms; checked that Gaussian Lipschitz concentration yields dimension-uniform moment concentration using the explicit quadratic-form tail inequality in the opened Ma–Misiakiewicz paper. Potential failures recorded: aspect ratio one, Gaussian-input conditional means, second Hermite coefficient, supercritical spikes, non-Lipschitz polynomials, and random-versus-deterministic edge centering. No claims of a complete solution or a new proof.

Artifacts written: SOLVED_ELSEWHERE.md, REPORT.md, LOG.md. No files outside this folder were changed by task commands.

Final read-only verification at 22:11:29 +04: `ls -l LOG.md SOLVED_ELSEWHERE.md REPORT.md; head -1 REPORT.md; tail -8 LOG.md; date '+%Y-%m-%d %H:%M:%S %Z'`. All three artifacts exist; REPORT.md begins with the required `VERDICT: PARTIAL` line. Search, documentation, and verification completed about three minutes after the first recorded clock reading.
