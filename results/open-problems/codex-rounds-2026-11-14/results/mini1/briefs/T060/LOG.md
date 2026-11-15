# T060 work log

Task: “push this problem forward by one checkable piece.” Started 2026-11-14 16:48:39 UTC (20:48:39 Asia/Tbilisi).

## 1. Orientation and bounded literature search

Work is confined to this directory. The task-specific prohibition on outside writes takes precedence over the earlier brain/mesh/checklist write requirements; those commands were not run. Read the brain navigation index and compute governor state. Governor reported `status: ok`, `mode: owner_away_open`. No subagents, git, external messages, or heavy computations.

Initial shell commands: `pwd`; `rg --files -g 'AGENTS.md' -g 'MEMORY.md' -g '*' .`. Initial files: PROMPT.md, run.pid, codex.log.

Read-only orientation command used `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3` with a small pathlib script. The sandbox printed `nice: setpriority: Operation not permitted` but executed the reads. No numerical run is planned if the literature finding is confirmed.

Web searches (2026-11-14, immediately after start):

- `spin 1 Heisenberg chain Haldane conjecture rigorous proof 2025 2026 spectral gap`
- `Haldane conjecture Heisenberg chain mathematical proof spectral gap recent advances`

Results include a September 24, 2026 manuscript, *The periodic spin-one Haldane gap*, attributed to OpenAI; Hal Tasaki's October 2026 exposition; an October 25 uniqueness manuscript (arXiv:2610.34330); and a November tensor-network verification manuscript (arXiv:2611.11049). These are search leads, not yet verified claims. Next: open the primary papers, determine exact theorem scope, and follow the user's stop rule if the reported advance is confirmed.

## 2. Primary-source metadata opened

Opened https://arxiv.org/abs/2610.34330 : author **Hal Tasaki**, v2 dated October 27, 2026. Abstract states uniqueness among translation-invariant operator-algebraic ground states, purity and a gap, and explicitly disclaims uniqueness among arbitrary nontranslation-invariant ground states.

Opened https://arxiv.org/abs/2611.11049 : author **Sirui Lu**, submitted November 8, 2026. Abstract reports verification of the periodic spin-1 proof, a bound `Delta_L > 0.0729` for every even `L >= 36`, and Lean 4 formalization of the general theorem. Full text still to be checked.

Opened https://haltasaki.github.io/writings/AI/OpenAI_Haldane.html : **Hal Tasaki** describes the analytic proof and explicitly says he has not independently checked the computer-assisted estimates. The direct GitHub directory fetch returned a cache miss. Follow the links to full texts before reporting exact scope.

Choice: apply step 1's literature-stop branch rather than start a new finite calculation. The opened primary arXiv pages already establish substantial advances beyond the supplied status; remaining work is a short check of theorem scope and citations. No claim to an original proof is intended.

## 3. Full-text scope audit

Opened Tasaki's full exposition, https://haltasaki.github.io/writings/AI/OpenAI_Haldane_CT.pdf (34 pages), and his uniqueness paper's full HTML, https://arxiv.org/html/2610.34330v2. The latter's Theorem 2.1 and final discussion agree on the translation-invariance restriction. The former's Theorem 2.2 counts energies with multiplicity, so its periodic gap includes finite-ring uniqueness.

Opened Lu's full paper, https://arxiv.org/pdf/2611.11049 (39 PDF pages including supplement). Checked the abstract against the improved-bound argument in Sec. SII.B and checked Sec. SIV/Table S6 for formalization scope. The spin-1 Lean theorem retains finite short-ring trace hypotheses. Do not describe the complete spin-1 calculation as unconditionally kernel-verified. No certificate code has been executed here.

The original OpenAI PDF's GitHub page opened, but direct PDF extraction failed: raw.githubusercontent.com returned unsupported `application/octet-stream`; the github.com raw URL returned a cache miss. A guessed `paper.tex` URL returned 404. Do not pretend these fetches read the original proof. The readable Tasaki and Lu full texts already suffice to document substantial advances.

Independent checks here concern the reported statements: (i) primary abstracts against theorem/supplement text; (ii) a second author's full exposition of the periodic result; (iii) finite periodic uniqueness versus unrestricted infinite-volume uniqueness; (iv) normalization `H_L = sum_j S_j dot S_{j+1}`, unit coupling, even periodic length; (v) analytic formalization versus finite numerical premises. No load-bearing number is newly computed in this literature-only branch.

## 4. Original paper recovered; stop condition fulfilled

The community catalogue's PDF link successfully opened the complete original 30-page manuscript at https://mathcommunity.github.io/oai-math-revised/papers/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf . Its title page confirms author **OpenAI** and date September 24, 2026; Theorem 1.1 confirms the periodic result. Thus the earlier extraction failure was resolved using a readable mirror, without a download or a git operation.

Wrote SOLVED_ELSEWHERE.md and REPORT.md. Report verdict is PARTIAL because this is a literature finding and unrestricted infinite-volume uniqueness is outside the cited uniqueness theorem. The periodic gap has been proved elsewhere according to the opened primary texts. No PROOF.md or computation/data files were needed in this stop branch. All writes remained within T060.

## 5. Artifact check and completion

At 16:51 UTC, ran:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 - <<'PY'
from pathlib import Path
for name in ('LOG.md','SOLVED_ELSEWHERE.md','REPORT.md'):
    p=Path(name)
    text=p.read_text()
    assert len(text)>100
    print(f'{name}: present, {len(text.encode())} bytes')
first=Path('REPORT.md').read_text().splitlines()[0]
assert first.startswith('VERDICT: PARTIAL ')
print(first)
print('No numerical experiment or original proof claimed.')
PY
```

All three files were present and nonempty; the verdict assertion passed. The command again emitted `nice: setpriority: Operation not permitted`. Search and documentation finished in approximately three minutes, within the ten-minute literature limit. The session stops under step 1.
