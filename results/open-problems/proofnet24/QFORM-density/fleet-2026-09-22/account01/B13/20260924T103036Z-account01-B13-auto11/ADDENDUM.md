# account01/B13 run addendum — proof-line correction

Run: `20260924T103036Z-account01-B13-auto11`.

This addendum corrects one prose sentence in Section 5 of `REPORT.md`; the stated theorem and all displayed constants remain unchanged.

For `x in S cap (S+u)`, one has

\[
|q(x)-q(x-u)|=|2(Au)^Tx-u^TAu|\le\ell.
\]

Since `q(x)-q(x-u)` ranges in `[-ell,ell]`, the scalar `(Au)^T x` is restricted to an interval of length **exactly `ell`** (not `ell/2`). Therefore the fiber estimate used in the report is correctly

\[
h(u)\le M(u)\min\left\{1,{\ell\over |(Au)_i|m_i(u_i)}\right\},
\]

and hence `QFORM-PRODUCTSET-DIFFERENCE-GRADIENT-v1`, equations (5.5), (5.9), (5.10), and (5.11), require no change.

Full QFORM remains OPEN; this is a local proof-text correction only.
