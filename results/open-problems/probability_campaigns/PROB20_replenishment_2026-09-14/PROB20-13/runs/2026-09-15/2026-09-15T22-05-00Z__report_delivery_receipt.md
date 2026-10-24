# PROB20-13 — delivery receipt / checking addendum

This append-only addendum records delivery information that was not knowable until after the mathematical report had been committed. It does not replace or modify the report.

## Mathematical report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/runs/2026-09-15/2026-09-15T21-55-00Z__report.md`

Creating commit:

`239362153752b4189599cdedb56374419b2f37e8`

Blob SHA from exact-commit readback:

`34218026e954900d3b3a49bb9793908d2fdb142a`

Status: **VERIFIED** by reading the file at ref `239362153752b4189599cdedb56374419b2f37e8`.

The report proves the exact wheel formula
\[
F(W_{q+1})=
\max_{1\le k\le\lfloor q/2\rfloor}
\frac{3k(4q-3k)}{2q(k+2)},
\]
shows `F(W_{q+1})->6`, and gives the exact diameter-two auxiliary counterexample
\[
F(W_{38})=\frac{744}{185}>4.
\]
It also proves that every wheel still satisfies the actual owner target `F<=2 tau_rel D`.

## Exact checker artifacts

First append-only checker:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/artifacts/2026-09-15T21-58-00Z__wheel_exact_formula_check.py`

Creating commit `884c6804134fd984c5e9a076c423355ace6b0d34`; blob `9da1bf5fc947ca9fcccb61730399dca0700a9e89`; exact-commit readback **VERIFIED**.

That first checker was not used as the canonical execution artifact because its default exhaustive range was unnecessarily large for the nested parity check. It is preserved unchanged under the append-only rule.

Canonical efficient checker:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/artifacts/2026-09-15T22-02-00Z__wheel_exact_formula_check_v2.py`

Creating commit `d11af1a41220e970001b52456d349477a8b23641`; blob `4c1c034c1e25031d3e3d911e9f0a244ca1525119`; exact-commit readback **VERIFIED**.

## Checks actually executed

The efficient exact-rational logic was executed locally through every integer
\[
4\le q\le1000.
\]
For every such `q` and every breakpoint `1<=k<=floor(q/2)`, the check verified:

1. the parity-specific wheel dual objective equals
   \[
   \frac{3k(4q-3k)}{2q(k+2)};
   \]
2. the exact difference identity
   \[
   V_q(k+1)-V_q(k)
   =\frac{3(8q-3k^2-15k-6)}{2q(k+2)(k+3)};
   \]
3. the quadratic-threshold maximizing index is an actual global maximizer;
4. every tested finite wheel value is strictly below `6`.

The exact returned stress-test values were:

- `F(W_38) = 744/185`;
- unique maximizing breakpoint for `q=37`: `k=8`;
- first wheel parameter `q>=4` with `F>4`: `q=37`;
- `F(W_5)=15/8`;
- `F(W_6)=21/10`.

These computations corroborate the exact proof; they are not used as a substitute for it.

## Status

Full owner target: **OPEN / PARTIAL**.

Auxiliary statement `D=2 => F<=4`: **REFUTED exactly** by `W_38`.

No Gmail or Google Drive action was taken. No permissions, workflows, shared indexes, or other schedules were changed.
