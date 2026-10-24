# R16 verification - finite-entropy moving-aspect lower sides

## Scope

Round R16 tested whether the lower-side union bound can be kept in finite
entropy form instead of passing through a fixed limiting aspect ratio
\(N_m/m\to\gamma>1\).  The goal was to state only lower-side estimates, not a
moving-aspect exact Gaussian law.

## Five-agent audit

Exactly five read-only agents were launched and then closed after reporting.

1. `019f0a48-4315-7d32-be79-357983173fbe` checked the square row-submatrix constants and the single power of \(K_m\).
2. `019f0a48-436b-7ec2-9c57-b16c34e56b80` adversarially checked \(N_m/m\to1\), \(N_m/m\to\infty\), fast \(K_m\), non-identical entries, and complex scalars.
3. `019f0a48-43be-7bc3-97be-a3c0a40392cc` derived the fixed-excess finite-entropy form from `rect:bd-tail`.
4. `019f0a48-4412-7220-bc7f-203c7e059681` scouted the standalone and Lane O insertion points.
5. `019f0a48-4477-7ee3-bf54-dadb068ea3d1` checked the compact Lane O formulation.

## Result

The abstract finite-budget inequality is
\[
  \PP\left\{
  \min_T Y_T\le
  \exp\left[-\frac{\log|\mathcal T_m|+\log C_m+u_m}{a_m}\right]
  \right\}
  \le e^{-u_m}
\]
whenever \(\sup_T\PP\{Y_T\le t\}\le C_m t^{a_m}\) for \(0<t\le1\).

For square row submatrices with \(L_m=\log\binom{N_m}{m}\) and scalar density
bound \(K_m\), the explicit one-minor estimate gives
\[
  \PP\left\{M_m\le
  \exp\left[-\frac{L_m+\log K_m+(d_\F+1)\log m+O_\F(1)+u_m}{d_\F}\right]\right\}
  \le e^{-u_m}.
\]
For fixed excess \(r\), \(p=r+1\), and
\(L_m^{(r)}=\log\binom{N_m}{m+r}\), the fixed-excess bound is the same with
budget \(L_m^{(r)}+p\log K_m\), exponent \(d_\F p\), and polynomial slack
\((1+d_\F p)\log m+O_{\F,r}(1)\).

## Guardrails

These are lower-side union-bound estimates only.  They do not prove a matching
upper side, an exact moving-aspect Gaussian base, a Poisson extreme process, or
phase-retrieval stability away from the exact critical reduction.  When the
entropy budget is only \(O(\log m)\), polynomial hard-edge factors and Stirling
constants can affect the actual scale.

## Manuscript changes

- `parts/principle.tex`: added `cor:finite-budget`.
- `parts/universality.tex`: added `cor:finite-entropy-square`.
- `parts/geometric.tex`: added `rect:finite-entropy` and adjusted the
  moving-aspect warning.
- `master/chO_phase_retrieval_rmt.tex`: added the compact finite-entropy lower
  side paragraph.
- `PLAN.md`, `STATE.md`, `MASTER_STATE.md`, and `master/ch_overview.tex` were
  updated.

## Build verification

After integration, the standalone manuscript compiled to
`extremal_hard_edge.pdf` with 31 pages and 539017 bytes.  The fleet master
compiled to `master.pdf` with 852 pages and 7755113 bytes, and the same file was
copied to `~/Downloads/master.pdf`.  Targeted log scans showed no
LaTeX errors, undefined references/citations, or rerun requests.
