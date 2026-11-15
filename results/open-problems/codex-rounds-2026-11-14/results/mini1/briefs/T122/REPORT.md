VERDICT: PARTIAL located recent cavity-formula proofs covering the Erdős–Rényi branch; regular-graph coverage not verified

The literature stopping condition was met within ten minutes. See
[SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) for references, theorem scope,
and the deduction for G(n,d/n). No new research proof is claimed.

The principal arXiv finding is Dmitry Panchenko, *The Mézard-Parisi formula*,
[arXiv:2610.39545](https://arxiv.org/abs/2610.39545), submitted October 29,
2026, with companion [arXiv:2610.39542](https://arxiv.org/abs/2610.39542).
The separate OpenAI manuscript linked in SOLVED_ELSEWHERE.md states a general
Poisson theorem whose hypotheses include deterministic antiferromagnetic
two-spin interactions. Its stated equality yields the Erdős–Rényi
zero-temperature variational value. These are recent proof manuscripts;
their full proofs were not audited here.

Checks: verified the antiferromagnetic factorization, positivity for every
integer moment, interaction-density normalization, finite-volume entropy
error log(2)/beta, Poisson-to-simple-graph coupling with expected edit count
at most d^2(n-1)/(2n), and concentration. Rechecked the energy normalization
independently through Cut=(|E|-sum sigma_u sigma_v)/2. No numerical constants
or computation results are asserted.

Commands: read-only `pwd`, `rg --files`, `rg -n`, `sed -n`, and
`date '+%Y-%m-%d %H:%M:%S %Z'`; web-tool searches and opened primary papers
and primary TeX, listed in LOG.md. A startup Python file read and a later
echo probe under `nice -n 15` both reported `setpriority: Operation not
permitted`. No research computation followed, and no script or dataset was
needed. All created files are in this folder. No git, external writes, or
subagents were used.

What stopped: the proposed quantitative subdivision reduction in LOG.md was
abandoned once the literature stopping condition was satisfied. It has not
been proved here. What remains uncertain: independent validation of the new
proof manuscripts and the fixed-degree regular ensemble. Next worker: audit
the cited general theorem and determine whether its lower-bound argument
extends to regular factor graphs; do not infer regular coverage from Poisson
coverage or symmetric-coupling examples.

Task: “push this problem forward by one checkable piece” — T122, received
2026-11-14 approximately 22:00 +04 (Asia/Tbilisi).
