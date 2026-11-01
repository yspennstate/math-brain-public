# R15 verification - aspect asymptotics of the entropy base

## Scope

Round R15 filled the planned Part III.D item: endpoint asymptotics of
\[
  h(\gamma)=\gamma\log\gamma-(\gamma-1)\log(\gamma-1),
  \qquad c_\gamma=e^{h(\gamma)}.
\]
This is deterministic calculus used to interpret fixed-aspect extremal
thresholds.  It is not a new moving-aspect random-matrix theorem.

## Five-agent audit

Exactly five read-only agents were launched and then closed after reporting.

1. `019f0a3e-9e9b-7830-9afa-d713c724901e` checked the endpoint expansions and constants for \(h\) and \(c_\gamma\).
2. `019f0a3e-f2f9-7342-a7ed-0740bfd46248` adversarially checked fixed-aspect versus moving-aspect overclaims.
3. `019f0a3e-f34e-7d62-8372-d803f6825dc5` scouted standalone and Lane O insertion points.
4. `019f0a3e-f3a1-7c30-8d21-ca837a77fd18` checked the probabilistic interpretation for real/complex and fixed-excess denominators.
5. `019f0a3e-f3f2-79c3-ad5d-bc7f198abc75` checked the compact Lane O formulation.

## Result

The safe deterministic statements are:
\[
  h(1+\delta)
  =\delta\log(1/\delta)+\delta+\frac{\delta^2}{2}
   -\frac{\delta^3}{6}+O(\delta^4)
  \qquad(\delta\downarrow0),
\]
and
\[
  h(\gamma)=\log\gamma+1-\frac{1}{2\gamma}
  -\frac{1}{6\gamma^2}-\frac{1}{12\gamma^3}+O(\gamma^{-4})
  \qquad(\gamma\to\infty).
\]
Exponentiating gives \(c_\gamma\sim e\gamma\) at large fixed aspect and
\(c_{1+\delta}\to1\) at the barely overcomplete endpoint.

The manuscript states the moving-aspect caveat explicitly.  If
\(\gamma_m=N_m/m\) tends to \(1\) or infinity with \(m\), the fixed-aspect
theorems do not automatically provide a sharp law.  Uniform small-ball and,
for matching exact bases, uniform pair-correlation estimates would be needed.
When \(m h(\gamma_m)\) is only \(O(\log m)\), polynomial hard-edge factors and
Stirling constants can affect the actual scale.

## Manuscript changes

- `parts/geometric.tex`: added `sec:aspect-asymptotics`, Proposition
  `prop:h-asymptotics`, and the moving-aspect warning.
- `extremal_hard_edge.tex`: abstract now mentions endpoint aspect asymptotics.
- `master/chO_phase_retrieval_rmt.tex`: added a compact `Aspect asymptotics`
  paragraph immediately after the opening source theorem.
- `PLAN.md`, `STATE.md`, `MASTER_STATE.md`, and `master/ch_overview.tex` were
  updated.

## Build verification

After integration, the standalone manuscript compiled to
`extremal_hard_edge.pdf` with 30 pages and 531488 bytes.  The fleet master
compiled to `master.pdf` with 852 pages and 7752896 bytes, and the same file was
copied to `~/Downloads/master.pdf`.  Targeted log scans showed no
LaTeX errors, undefined references/citations, or rerun requests.
