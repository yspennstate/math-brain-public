# T427 work log

Task: “push this problem forward by one checkable piece.” Received 14 November 2026; session clock first read at 18:14:43 UTC (22:14:43 Asia/Tbilisi).

## 2026-11-14 18:14–18:16 UTC — orientation and literature search

Read the workspace file list, startup memory, and compute governor state. The folder initially contained only PROMPT.md. The governor reported `status: warn`, `mode: owner_away_open`, and CPU saturation. No heavy computation is planned. The specific instruction to write only here takes precedence over the global mesh/checklist/brain commands, which would write elsewhere; none were run. No git or subagents are used.

Read-only shell commands: `pwd`; `rg --files -g 'AGENTS.md' -g 'LOG.md' -g 'REPORT.md' -g '*.py' -g '*.md' .`; `ls -la ~/brain-views`; `cat ~/.claude/compute/compute_state.json`; `cat ~/.claude/brain_startup.md`.

Web searches (web search tool):

- `random matching two dimensional second order constant semidiscrete 2025 2026`
- `optimal matching square second order constant Wasserstein empirical measure log n limit`

Opened https://arxiv.org/abs/2610.40509 and https://arxiv.org/html/2610.40509v1: Yunzong Xu, *Random Matching Between Distinct Distributions in Two Dimensions*, submitted 29 October 2026. Its abstract announces an additive o(1) expansion and a universal constant. This is a potentially decisive update; checking the actual square semidiscrete theorem before choosing any new mathematical subtask.

Also opened https://arxiv.org/abs/2609.08717 (Victor Armegioiu, Michael Goldman, Francesco Grotto, Dario Trevisan; first-order asymptotics for general power costs on the torus) and https://arxiv.org/abs/1810.07002 (Luigi Ambrosio, Federico Glaudo; prior finer estimates). The former abstract addresses a different asymptotic question.

## 18:15 UTC — decisive theorem located

Opened Section 5.1, Corollary 2, of Xu's HTML paper and the PDF https://arxiv.org/pdf/2610.40509. The corollary explicitly covers equal-mass semidiscrete transport and convex corners. The square specialization is therefore direct. Following instruction 1, the chosen deliverable is now a literature update in SOLVED_ELSEWHERE.md and REPORT.md; no new mathematical subtask will be started. Existence is addressed by the preprint; a numerical value is not supplied.

Audit underway: compare the HTML theorem with its PDF rendering, check the empirical normalization, and recombine the equal-mass smoothing and spectral formulas to check the coefficient and additive constant independently of simply copying Corollary 2. This is a statement/normalization audit, not a full independent verification of the 56-page proof.

## 18:15–18:16 UTC — audit and deliverables

Opened Proposition 3.1, equations (3.3)–(3.4), the equal-mass clause of Theorem 4, and the mass definition (chi_n = 1 for equal masses). Independently recombined those earlier statements, rather than using Corollary 2:

1. Set t = n^(-5/6). Then nt = n^(1/6), so t tends to zero and nt/(log n)^3 tends to infinity.
2. The smoothing contribution is log(nt)/(4 pi) + kappa_equal + o(1).
3. The spectral contribution is log(2/t)/(4 pi) + h_Q + o(1).
4. Their sum is log n/(4 pi) + kappa_equal + log 2/(4 pi) + h_Q + o(1). This agrees with beta_sd = kappa_equal + log 2/(4 pi).
5. The reduction error at this t is O(n^(-1/12)(log n)^(3/2)); the spectral error is O(n^(-5/12)). Both are bounded asymptotically by the stated O(n^(-1/120) log(en)) smoothing error. In particular the remainder tends to zero. No heat-time limit was taken with n fixed.

Checked the square spectrum separately by separation of variables: the Neumann eigenfunctions are products of cos(k pi x) and cos(l pi y), giving eigenvalues pi^2(k^2+l^2), k,l >= 0, excluding (0,0). There is one eigenfunction per ordered nonnegative pair; zero is excluded. This gives the spectral expression in SOLVED_ELSEWHERE.md without a periodic-spectrum or multiplicity substitution.

Cases checked: square corners (angle pi/2 in (0,pi)); uniform density (area 1 and log-density integral zero); Euclidean versus intrinsic distance (line segments stay in the convex square); fixed n and equal empirical weights, not Dirichlet weights or Poisson sample size; symmetry of W_2 allows reversing the measures. The claim concerns the expectation, as required.

The attempted web PDF screenshot of zero-indexed page 16 failed: `Failed to fetch https://arxiv.org/pdf/2610.40509: Cache miss`. PDF text extraction located Corollary 2 at printed page 17; HTML independently exposes the same formula. No screenshot was saved.

Wrote SOLVED_ELSEWHERE.md and REPORT.md using apply_patch. No programs performing mathematical computation were run; no computation data file is needed. All mutations remained inside this folder. No new research subtask was begun after the literature discovery.

## 18:16:31 UTC — final file validation

Exact command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B - <<'PY'
from pathlib import Path
p = Path('.')
for name in ('LOG.md', 'SOLVED_ELSEWHERE.md', 'REPORT.md'):
    f = p / name
    text = f.read_text()
    assert text.endswith('\n'), name
    print(f'{name}: {len(text.splitlines())} lines, {f.stat().st_size} bytes')
report = (p / 'REPORT.md').read_text()
assert report.splitlines()[0].startswith('VERDICT: PARTIAL ')
assert '2610.40509v1' in report.splitlines()[0]
assert not (p / 'PROOF.md').exists()
print('Checks passed: required reports exist; verdict format valid; no independent proof claimed.')
PY
```

Output before this final log append:

```text
nice: setpriority: Operation not permitted
LOG.md: 42 lines, 4919 bytes
SOLVED_ELSEWHERE.md: 26 lines, 1402 bytes
REPORT.md: 11 lines, 1223 bytes
Checks passed: required reports exist; verdict format valid; no independent proof claimed.
```

The environment rejected the requested priority change but still ran this tiny read-only validation (tool wall time below 0.1 s). No simulation or costly computation was launched. Earlier orientation reads likewise had no explicit priority wrapper. No additional shell programs are needed. Final report records this execution limitation. Search and theorem inspection finished less than two minutes after the initial clock read, within the ten-minute cap.
