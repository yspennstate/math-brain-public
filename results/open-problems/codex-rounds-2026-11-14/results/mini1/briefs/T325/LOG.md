# T325 work log

Task: “push this problem forward by one checkable piece.” Started 2026-11-14 22:13 Asia/Tbilisi (18:13 UTC).

## 1. Orientation and literature check (18:13–18:16 UTC)

The session is confined to this folder. No git, external writes, subagents, or model-training jobs. The later folder-only instruction overrides the earlier requests to update the shared brain, mesh, and checklist; those services write outside this folder, so they were not run. Read the memory index and compute-state file. Compute state: status warn, mode owner_away_open, CPU saturated; no heavy computation planned.

Commands used for read-only orientation:

```
pwd && rg --files -g 'AGENTS.md' -g 'LOG.md' -g 'REPORT.md' -g '*MEMORY*' . ~/.claude ~/brain-views 2>/dev/null | head -60
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 - <<'PY'
from pathlib import Path
for name in ['~/.claude/projects/-Users-user/memory/MEMORY.md','~/.claude/compute/compute_state.json']:
 p=Path(name)
 print('\nFILE',name)
 print(p.read_text()[:13000] if p.exists() else 'MISSING')
print('\nWORKSPACE')
for p in Path('.').iterdir(): print(p.name)
PY
```

Output that matters: workspace initially contained codex.log, PROMPT.md, run.pid. The nice wrapper printed `nice: setpriority: Operation not permitted` but the short Python read completed. A subsequent priority inspection command `OMP_NUM_THREADS=1 nice -n 15 /bin/ps -o pid,ppid,ni,comm -p $$ -p $PPID` was denied (`nice: /bin/ps: Operation not permitted`, exit 126). No numerical workload was launched. Do not interpret these calls as a verified process-priority audit.

Web search tool queries:

- `transformers linear regression multi layer training convergence gradient descent 2025 2026`
- `"in-context" "multi-layer" "convergence" linear transformers training`
- `"multi-layer linear" transformer "convergence" "random" regression 2025 2026`
- `"transformers" "in-context linear regression" "training" "convergence" 2026`

Opened arXiv 2410.08292 and 2502.21212. These point to training-convergence theorems for weight-shared linear looped transformers and for chain-of-thought training, respectively. They predate the supplied November 2026 status; the status may omit substantial restricted advances. Need inspect theorem assumptions before deciding whether the instruction to stop applies. Attempted HTML `https://arxiv.org/html/2410.08292v2` returned 404.

## 2. Choice: verify the substantial-advance branch (18:14–18:16 UTC)

Choice: inspect the actual convergence statements and architectural restrictions in the two papers, then write SOLVED_ELSEWHERE.md and REPORT.md and stop, as instruction 1 requires on finding substantial progress. This is a correction to the supplied literature status, not a claim to solve the full random-initialization softmax/untied problem. The relevant papers are from 2024 and 2025, not papers published after November 2026.

Opened full HTML and PDF of 2410.08292v1 and full HTML of 2502.21212v1, plus the ICML proceedings page. Read 2410.08292 Theorems 3.2–3.4, Table 1, block parameterization, and Appendix A.11–A.12; read 2502.21212 Assumption 4.1, Theorem 4.1, Sections A.2–A.3 and Theorem A.1. The looped convergence theorem trains a single shared matrix block, with other blocks fixed. The CoT theorem uses a different supervised objective and a structured initialization.

Additional web queries: `transformer "multi-layer" "random initialization" "linear regression" convergence theorem`; `transformer "linear regression" "training convergence" "2026" multilayer`. Found a late-October 2026 CoT/heavy-ball paper; opening the primary source to check its scope. Search snippets and secondary summaries are not being treated as theorem evidence.

Audit flags already found in the primary texts: the 2024 gradient-flow comparison ODE in Appendix A.12 has a sign inconsistency and its displayed integrated prefactor needs re-derivation; do not repeat that numerical time constant. The 2025 Theorem A.1 displays a target floor without the leading d that appears in its proof immediately before the final loss estimate. Report these as textual discrepancies, not as a disproof of the qualitative restricted training result.

## 3. Audit and stopping decision

Opened the primary arXiv page for 2610.31089 and full text versions v1 and v2. Verified authors Yuxuan Cai and Yuan Cao, first submission 22 October 2026 and revision 31 October 2026. Read v2 Assumptions 3.1–3.2 and Theorem 3.3. This is a linear-attention CoT weight-prediction theorem with two-stage supervision and a prescribed sparse initialization. It cannot be substituted for a full-random-initialization final-query softmax theorem.

Checked the 2024 untied-layer Appendix A.1: Theorem A.1 is an explicit recursion formula. Its presence does not establish training convergence for untied layers. Checked the PDF text of Appendix A.12 as well as its HTML: the comparison-equation sign and prefactor issues appear in both representations.

Independent hand audit of the comparison calculation (conditional on the paper's stated gradient-dominance inequality): write p=(2L−1)/L and suppose f′ ≤ −f^p/16 while above the stated floor. Since p−1=(L−1)/L, separation gives

    f(t) ≤ [f(0)^(-(L−1)/L) + (L−1)t/(16L)]^(-L/(L−1))

until reaching the floor. A sufficient time from this inequality is

    t ≥ [16L/(L−1)] ξ^(-(L−1)/L).

Second derivation: set h=f^(-(L−1)/L). The chain rule gives h′ ≥ (L−1)/(16L); integrate this linear inequality. Direct differentiation of g(t)=[g(0)^(-(L−1)/L)+(L−1)t/(16L)]^(-L/(L−1)) yields g′=−g^p/16. For L=2 this reduces to g(t)=[g(0)^(-1/2)+t/32]^(-2), again giving g′=−g^(3/2)/16. This verifies sign and constant independently. The source's time prefactor is [16L/(L−1)]^((L−1)/(2L−1)); it does not follow from that comparison inequality. This audit does not show its theorem is false: a stronger inequality could give a better constant.

The 2025 looped theorem/proof discrepancy can also be checked algebraically: the proof estimates loss by 2d ||I−A||^(2L), and requests ||I−A||² at scale (ξ/d)^(1/L). Combining that with a squared-norm concentration cutoff at scale L²d log²(d)/n yields a target scale d[L²d log²(d)/n]^L. This agrees with the proof's explicit cutoff and differs from the statement's cutoff. No sharp dimension-dependent rate is adopted here.

Other failure cases checked: constructions alone do not imply training convergence; a global-minimizer characterization alone does not imply a training trajectory reaches it; convergence to a small-loss region does not imply exact finite-N Bayes prediction; randomizing a prescribed block is different from independently randomizing all matrices; teacher-supervised CoT is a different objective. No inspected paper establishes all requirements of the unrestricted task. The bounded literature search cannot certify that no other paper does.

Saved SOLVED_ELSEWHERE.md and REPORT.md using apply_patch. Stopped under the substantial-advance branch. No PROOF.md, simulation, or data file is claimed, because this branch ends after the literature finding and report. These artifacts report existing theorems with caveats, not a newly proved transformer convergence theorem.

Final artifact check (18:16 UTC): ran `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3` with a short standard-library script reading the three deliverables, asserting final newlines and the exact report verdict prefix, and confirming no proof/data artifact was claimed. Output: `Artifact checks passed.` The nice wrapper again printed `setpriority: Operation not permitted`; no computation beyond these file checks was performed. Search and artifact work finished within four minutes of the first clock reading.
