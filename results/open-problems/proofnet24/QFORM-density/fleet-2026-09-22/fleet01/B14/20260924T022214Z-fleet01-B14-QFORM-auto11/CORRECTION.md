# Notational clarification for REPORT.md

No theorem, hypothesis, constant, spectrum check, or conclusion changes.

In Section 4.2, the displayed shorthand

`S_#sigma_k = p_{S_0} * (c_#sigma_k)`

should be read as the pushforward of the **product positive measure** `P_{S_0} tensor sigma_k` under `(s_0,u) -> s_0+c(u)`. Precisely,

`(s_0+c(u))_#(P_{S_0} tensor sigma_k)`

has density `p_{S_0}*(c_#sigma_k)` and therefore has `L^infinity` norm at most `M_0 m_k`, where `m_k=sigma_k(Omega)`. This is the positive slope measure used in the theorem and in the phase-weighted total-variation domination. The abbreviated notation in the report does not mean that `S` is a function of `U` alone.
