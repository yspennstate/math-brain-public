# T086 work log

## 2026-11-14, session start (UTC 17:33–17:37)

Task: check for a complete solution for at most ten minutes; otherwise finish one concrete mathematical piece. All output stays in this folder. No git or external writes.

Read `~\AGENTS.md` with PowerShell `Get-Content`; the current task's narrower restrictions take precedence over standing upload and memory-write instructions. Shells set `OMP_NUM_THREADS=1` and BelowNormal process priority.

Web search queries:
- `Brownian sheet small ball conjecture solved 2025 2026 dimension three`
- `small ball inequality Brownian sheet Bilyk Lacey Vagharshakyan progress 2024`

Search found arXiv:2611.09495, submitted 6 November 2026, claiming the entire conjecture. Opened the actual arXiv abstract, HTML and PDF:
- https://arxiv.org/abs/2611.09495
- https://arxiv.org/html/2611.09495v1
- https://arxiv.org/pdf/2611.09495

Authors on all three: Dmitriy Bilyk, Sebastian Neumayer, Tino Ullrich. Title: *The small ball problem for the Brownian sheet: sharp bounds via entropy numbers in L_infinity*.

Theorem 1.1, equation (1.3), states the exact two-sided order epsilon^(-2) (log(1/epsilon))^(2d-1) for the uniform small-ball exponent of the Brownian sheet in every d >= 2. Equation (1.2) gives the required covariance product_i min(s_i,t_i). Thus this appears to meet the explicit complete-solution stopping condition. Checking the PDF rendering and proof's final entropy-to-probability conversion before finalizing. No independent new proof is claimed.

Version detail: arXiv's submission history and HTML say 6 November 2026; the opened PDF's title page says 9 November 2026, while retaining arXiv:2611.09495v1, 6 Nov 2026. This discrepancy does not change the theorem statement but will be recorded rather than silently reconciled.

## 17:37–17:42 UTC: independent scope and exponent checks

Opened the version-specific PDF https://arxiv.org/pdf/2611.09495v1 as a second text path. Its PDF page 2, Theorem 1.1, matches the HTML. Opened Section 4 of the HTML and checked equation (4.1) and the proof of Theorem 1.1. Direct algebra gives 1/(r-1/2)=2 and beta/(r-1/2)=2d-1 at r=1, beta=d-1/2. In dimensions 2, 3, 4 these log powers are 3, 5, 7. No sign reversal, different covariance, different norm, or missing dimension restriction was found in this scope check. This is not an audit of the paper's full proof.

Two `web.screenshot` attempts, on unversioned and version-specific PDF page index 1, failed with `Cache miss`; extracted PDF text remained accessible.

Read the math-recall source before executing it: it opens the store read-only but normally writes a co-use log. Disabled this log, and disabled bytecode writes. Command (PowerShell):

```powershell
$env:OMP_NUM_THREADS='1'
$env:PYTHONDONTWRITEBYTECODE='1'
$env:MATH_STRENGTH_NOLOG='1'
[System.Diagnostics.Process]::GetCurrentProcess().PriorityClass='BelowNormal'
python -B '~\.claude\dreaming\math_recall.py' 'Brownian sheet small ball probabilities' --or 'Bilyk Neumayer Ullrich entropy numbers'
```

The command yielded session 99116; its completion is recorded below. No second copy was launched.

Decision: the whole stated problem is covered by the located theorem, so stop under step 1 rather than select a new piece. Wrote SOLVED_ELSEWHERE.md and REPORT.md. No PROOF.md is supplied because the proof is the cited paper's, not a new proof from this session.

## Completion checks

Math recall finished successfully (exit 0) after polling the same session, including a 45-second wait. It printed eight cards. The directly matching stored card was `claim_fad732ea73ba9c5def2dd2c82073adfd2376912b423639be892a894f93199914`; it repeats the old open status and does not contain the new paper. The unrelated entropy and Neumayer cards were not used. The store therefore supplies prior context, not independent confirmation of the November result. No memory was edited outside this folder.

The literature decision was reached by 17:41 UTC, less than ten minutes after the 17:33 start. Subsequent time was used to finish the read-only recall and save/check the deliverables.

Final readback command (PowerShell, OMP_NUM_THREADS=1, BelowNormal): `Get-Content -LiteralPath '.\REPORT.md' -Encoding UTF8; Get-Content -LiteralPath '.\SOLVED_ELSEWHERE.md' -Encoding UTF8; Get-ChildItem -File | Select-Object Name,Length`. Its output is checked for the required verdict line and the complete reference before returning.
