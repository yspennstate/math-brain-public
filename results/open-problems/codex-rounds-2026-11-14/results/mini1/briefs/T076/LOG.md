# T076 work log

Task received: 2026-11-14, approximately 20:52 Asia/Tbilisi (16:52 UTC).
Request: “push this problem forward by one checkable piece.”

## Initial orientation, 16:52 UTC

The folder initially contains PROMPT.md, codex.log, and run.pid. No git commands used.
The task-specific instruction to write only here overrides the global mesh, checklist,
and brain-write instructions: no external registration or memory writes will be made.
The compute governor reports `warn`, `owner_away_open`, CPU saturated; all work will
remain small and serial. No subagents.

Commands: `pwd`; `rg --files ...`; `cat ~/.claude/compute/compute_state.json`.
An attempted brain recall under `OMP_NUM_THREADS=1 nice -n 15 python3 ...` printed
`nice: setpriority: Operation not permitted` and an ONNX telemetry warning. It is
being stopped; further orientation uses direct read-only file access. The priority
restriction will be diagnosed before any computation.

Literature search begun at 16:52 UTC; budget at most ten minutes.

## Literature finding, approximately 16:52 UTC

Web search queries:
- `random band matrices delocalization two three dimensions November 2026 Lai Yang 2609.24426`
- `"random band matrices" "2026" delocalization localization`

Opened the primary arXiv pages https://arxiv.org/abs/2609.24426,
https://arxiv.org/abs/2507.20274, and https://arxiv.org/abs/2503.07606.
The first page is now titled *Localization Lengths for Two-Dimensional Random
Band Matrices: Exponential Lower Bounds*, by Xujie Lai and Fan Yang, revised
8 November 2026 (v4). Search results report a new bound
`W >= (log N)^(1+epsilon)` and localization length `exp(W^(1-epsilon))`,
substantially stronger than the supplied v2 bound `(log N)^7`.
The primary v4 paper and v2 record will be opened to confirm scope and exponents.
Under instruction 1, a confirmed substantial advance ends this session after
SOLVED_ELSEWHERE.md and REPORT.md; no independent piece should then be attempted.

The recall command completed before interruption and returned a prior note about
the one-dimensional Ghosal–Remy result, not a solution to T076. `ps` is blocked
by the sandbox. No further programs or numerical experiments are needed if the
literature advance is confirmed.

## Primary theorem checked, 16:53 UTC

Opened https://arxiv.org/abs/2609.24426v4 and
https://arxiv.org/html/2609.24426v4, Section 1.1, equations (1.5), (1.8)–(1.10),
Theorem 1.2, Remarks 1.1 and 1.3. Also opened the v4 PDF and v2 abstract.
The v2 abstract confirms the supplied seventh-power bound. The v4 abstract and
full theorem confirm a substantial advance. The model is specifically complex
Gaussian, periodic, and block structured. With `N=(W L_b)^2`, the variance is
`S_xy=(1/(5 W^2)) (1_{a=b}+1_{a~b})` for sites in blocks a,b, with four adjacent
blocks. Write `ell=10+log N`. For any fixed `A>1`, `C_bw>A+100`, and
`ell^A <= W <= ell^C_bw`, Theorem 1.2 bounds every normalized bulk eigenvector by
`||psi_k||_infinity^2 <= (log W)^10 ell^2/N`, simultaneously, with probability
at least `1-N^(-D)` for every fixed `D>0` and sufficiently large N.

The block-lattice side `L_b` is distinct from the problem's physical side length.
The full paper states that extensions to more general profiles are not pursued;
these must not be promoted to proved results. Theorem 1.2 has an upper bandwidth
restriction omitted in the abstract; Remark 1.3 explains how the previous
large-bandwidth result complements it. No local-statistics theorem at the new
threshold has been established by this inspection.

The PDF was opened as extracted text. Two attempted PDF page screenshots failed
with the web tool error “web screenshot is not enabled”; use PDF text and HTML
as the two renderings for the audit.

## Audit and stopping decision

The v4 PDF text, printed page 4, independently confirms the HTML transcription:
`A>1`, `C_bw>A+100`, `ell^A <= W <= ell^C_bw`, and squared infinity-norm
bound `(log W)^10 ell^2/N` with probability `1-N^(-D)`.
Equation (1.5) in both formats confirms the block variance and its factor 1/5.
Each row has five blocks of W^2 sites, so its variance sum is
`5 W^2/(5 W^2)=1`, a separate normalization check.

Independent exponent check, without a program:
`W >= (log N)^A` gives `log N <= W^(1/A)`; with
`A=1/(1-delta)`, this is `log N <= W^(1-delta)`.
Physical side is sqrt(N), hence its logarithm is half this value. Conversely,
at `log N = c W^(1-delta)` with fixed `0<c<1`,
`(10+log N)^A/W -> c^A<1` and
`W/(10+log N)^C -> 0` for `C>A`, so both bandwidth inequalities are compatible
with that scale. This checks the scale conversion in the presence of the
theorem's upper bound. It does not derive an infinite-volume localization theorem.

The new exponent 1+epsilon remains above the predicted 1/2; a lower bound
exp(W^(1-delta)) does not imply exp(c W^2). No d=3 fixed-bandwidth theorem or
new-threshold universality conclusion is being inferred from this result.

Created SOLVED_ELSEWHERE.md and REPORT.md with the precise restriction and
partial verdict. This ends the task under instruction 1; no additional piece,
simulation, git operation, or external write is authorized or needed.

## Final file review, 16:54 UTC

Read back REPORT.md, SOLVED_ELSEWHERE.md, and the audit log using cat and
tail. Corrected inline mathematics delimiters and removed an unverified
HTML fragment identifier. The three deliverables are saved in this folder.
Literature check completed in approximately two minutes, within the ten-minute limit.
