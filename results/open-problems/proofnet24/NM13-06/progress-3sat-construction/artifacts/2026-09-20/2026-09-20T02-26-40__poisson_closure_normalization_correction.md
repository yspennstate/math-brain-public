# Correction to the Poisson-closure sanity calculation in the 2026-09-20 NM13-06 T04 report

This artifact corrects **only Section 9's heuristic Poisson closure** in
`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T02-26-40__t04_four_parameter_branching_index.md`.
The main first-order identities (1)--(8) in that report are unchanged.

The report defines `x_{a,b,c,d}` and `m_2,m_3` per **original** variable. Therefore, if

\[
u:=\sum_{a,b,c,d}x_{a,b,c,d}
\]

is the current unset-variable density, an independent Poisson closure conditional on an unset variable must use

\[
a,b\stackrel{\rm iid}{\sim}{\rm Poisson}(m_2/u),
\qquad
c,d\stackrel{\rm iid}{\sim}{\rm Poisson}(3m_3/(2u)),
\]

not means `m_2` and `3m_3/2` unless `u=1`.

With

\[
\mu_2=m_2/u,\qquad \mu_3=3m_3/(2u),
\]

the correct closure gives

\[
\boxed{\rho=\mu_2=\frac{m_2}{u}},
\]

\[
\boxed{g_2=\mu_3-2\mu_2=\frac{\tfrac32m_3-2m_2}{u}},
\]

\[
\boxed{g_3=-2\mu_3=-\frac{3m_3}{u}},
\]

and hence

\[
\boxed{
 g_\eta=\frac{(\tfrac32-3\eta)m_3-2m_2}{u}.
}
\]

Thus the qualitative ratio conclusion in the report survives unchanged: at `eta=0`, the sign of `g_0` changes at `m_3=(4/3)m_2`, while for `eta>=1` it is negative. What was wrong was the omitted factor `1/u` and the resulting incorrect `rho=m_2` shorthand away from `u=1`.

This correction is recorded immediately rather than silently changing the immutable run report.
