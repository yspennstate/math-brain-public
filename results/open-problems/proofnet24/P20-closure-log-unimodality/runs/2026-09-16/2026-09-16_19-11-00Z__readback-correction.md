# P20 immutable readback correction — 2026-09-16 19:11:00Z report

Canonical report:

`proofnet24/P20-closure-log-unimodality/runs/2026-09-16/2026-09-16_19-11-00Z__run-report.md`

Creation commit:

`4f8da53ef452c87f3ca73e0385554e335d80bf9c`

Verified canonical report blob:

`9d8828f0cd19adcdca2df6bec2066d8255753c8a`

This note preserves the immutable canonical report and clarifies one pointwise passage in Step 6 of `P20-I0081-SINGLE-INFINITE-MODE-10`. It changes **no theorem statement, metric, source status, audit count, or finite certificate**.

## Pointwise full-log-support clarification

The canonical report wrote, after obtaining only `L^1` convergence `h_n -> h_infinity`, the pointwise-looking inequality

`h_infinity(u) >= h_N(u) / prod_{n>N}(1+epsilon_n) > 0`.

The intended conclusion is correct, but the direct passage from the pointwise finite-stage inequalities to a pointwise inequality for an `L^1` limit should be made through a local almost-everywhere bound and the monotone representative, as follows.

Fix `A<infinity`. Choose `N` so large that `R_N>A`. The newly added plateau at stage `N` gives a uniform constant `m_{A,N}>0` such that

`h_N(x) >= m_{A,N}` for every `|x|<=A`.

For every `n>N`, the update satisfies pointwise

`h_{n+1}(x) >= h_n(x)/(1+epsilon_{n+1})`.

Since `sum epsilon_n<infinity`,

`P_N := prod_{n>N}(1+epsilon_n)<infinity`.

Hence, uniformly for every `n>=N` and every `|x|<=A`,

`h_n(x) >= m_{A,N}/P_N =: m_A>0`.                 (C.1)

Now `h_n -> h_infinity` in `L^1`. If the set

`E={x in [-A,A]: h_infinity(x)<m_A}`

had positive Lebesgue measure, then for some `delta>0` the subset where `h_infinity<=m_A-delta` would have positive measure, and (C.1) would force `||h_n-h_infinity||_1` to stay bounded below by a positive constant, contradicting `L^1` convergence. Thus

`h_infinity(x)>=m_A` for almost every `x in [-A,A]`.   (C.2)

In Step 4 the proof already selects the even representative of `h_infinity` that is nonincreasing on `[0,infinity)`. For such a representative, an almost-everywhere lower bound by `m_A` on `[-A,A]` implies the same pointwise lower bound at every interior point: if the monotone representative were `<m_A` at some `x_0 in (0,A)`, monotonicity would force an interval of positive measure to the right to lie below `m_A`, contradicting (C.2). The value at `0` follows from monotonicity/evenness, and endpoint representatives can be chosen by the one-sided monotone limits. Therefore the representative can be chosen with

`h_infinity(x)>0` for every finite real `x`.

Since `A` was arbitrary, the claimed full logarithmic support follows rigorously.

All other parts of the canonical proof, including the `L^1` mode-persistence diagonal argument and the infinitely many protected mode intervals, are unchanged.

END OF IMMUTABLE READBACK CORRECTION
