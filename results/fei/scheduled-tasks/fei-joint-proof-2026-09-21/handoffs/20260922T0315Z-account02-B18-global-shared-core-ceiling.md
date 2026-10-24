# FEI handoff — account02/B18 — global signed-singleton ceiling for the exact nine-host shared-core transform

Status: **proved mechanism ceiling; full FEI remains OPEN / NOT PROVED**.

Source-bound scientific report:
`proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T030354Z-global-shared-core-ceiling/REPORT.md`
(commit `d5cd0ad0ec8150617c23362ab4f85f2f7d4e6cd5`).

Consumed other-account input:
`account04/B15/20260922T020955Z-adaptive-depth-shared-core-ceiling/REPORT.md`, which proves the exact local target `K(b)/(133/128)` is maximized on the reachable interval `[0,1/4]` below
`6.52185121301287772365150440023918196647146413881`.

New theorem: using the exact 19 `(A_s,Q_s)` Walsh classes of the account01/B18 nine-host source core, `K` is strictly increasing on `[-1,0]` and strictly decreasing on `[1/4,1]`. Hence

`sup_{-1<=b<=1} K(b)/(133/128) = sup_{0<=b<=1/4} K(b)/(133/128)`.

Combined with the exact actual-Boolean recurrence

`R'_d=(1-d0/D_d)R+(d0/D_d) K(c^d)/d0`, `d0=133/128`,

this yields for every signed singleton `c in [-1,1]` and every integer depth `d>=1`:

`R'_d <= max{R,M}`,

where `M` is the scalar source-core ceiling. After grafting, `c'=(57+c^d)/256 in [56/256,58/256]`, so the same max bound iterates for every history-dependent sequence of same-core grafts.

Therefore changing only the seed singleton sign/magnitude or the self-composition depth cannot escape the fixed nine-host core ceiling. A stronger lower-bound mechanism must start from an already stronger seed, change host/core geometry, or move to a genuinely biased gate point. Do not spend another FEI run tuning this same core/depth mechanism.

Exact checker: `CHECKER_GLOBAL.py`; output is `CHECK_OUTPUT_GLOBAL.txt`. It reduces the continuum statement analytically to exact rational-log endpoint inequalities; the finite certificate is not an FEI extrapolation.
