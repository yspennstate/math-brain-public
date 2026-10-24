# R31 verification - quaternion Gaussian square base

Date: 2026-06-28.

Target: integrate the square iid quaternion Gaussian row-submatrix base
\[
  m^{-1}\log \min_{|T|=m}\sigma_{\min}(A_T)\to -h(\gamma)/4
\]
without reviving the R27-removed quaternion spherical-radial universality claim.

Five tool-managed agents were launched for independent checks:

- one-matrix lower tail (`019f0ca9-61f1-7851-89ff-26720c0edc54`): safe, with the guardrail that the negative
  second-moment identity is used in quaternionic row space, not naively on the
  realification;
- upper-side second moment (`019f0ca9-623b-7140-871a-d94c1950013c`): constants correct but the manuscript proof needed
  local quaternion lemmas, Haar normal lines rather than chosen deterministic
  vectors, and an explicit split of the divergent \(D=2\) overlap term;
- spherical/radial scope (`019f0ca9-6286-77c2-b4ec-84373a6cdeb1`): the quaternion spherical-direction transfer is a
  possible narrow corollary, but it was not promoted this round;
- master integration (`019f0ca9-62df-79c0-9eea-02a508364d4e`): add a compact Lane O theorem with a lane-prefixed
  label and no phase-retrieval or universality overclaim;
- references/scope (`019f0ca9-632a-7720-a085-ae1f71137459`): add quaternionic conventions, the \(\Sp(m)\) macro, and
  keep fixed excess separate;
- Lean: no Lean change is useful for this round because the risk is the
  quaternion Haar/Beta/Jacobian argument, not rational algebra.

Implemented guardrails in `parts/ensembles.tex`:

- theorem `thm:quaternion-gaussian-base` is restricted to iid standard
  quaternion Gaussian square row submatrices;
- standard quaternion Gaussian normalization is explicit:
  \(q_\ell\sim N(0,1/4)\), so \(p_{\mathbb H}(t)=2t^4+O(t^6)\);
- lower side uses the quaternionic negative second-moment identity and gives
  \(P\{\sigma_{\min}(G)\le t\}\le C m^3t^4\);
- upper side writes the one-row exposure second moment locally, with Haar
  normal lines in \(\mathbb HP^{D-1}\), the quaternion two-ball Jacobian
  \((1-|\rho|^2)^{-2}\), the beta moment for \(D\ge3\), and the separate
  \(D=2\) estimate
  \[
    P(D=2)/p_{\mathbb H}(t)
    \le m^{O(1)}e^{-(h(\gamma)-4s+o(1))m}\to0.
  \]
- quaternion matrix conventions now cite `Zhang1997Quaternions`.

Master integration:

- `master/chO_phase_retrieval_rmt.tex` contains the compact theorem
  `laneO:thm:quaternion-gaussian-base`;
- the master version states only the iid standard quaternion Gaussian square
  row-submatrix base and explicitly avoids quaternion phase retrieval,
  supercritical Balan--Wang, and global real/complex replacement claims.

Not promoted:

- quaternion spherical-radial transfer;
- rotationally invariant quaternion universality;
- quaternion fixed-excess exact laws;
- beta/division-algebra interpolation.

Build:

- `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  passed twice.
- Final standalone PDF: 48 pages, 679,118 bytes.
- Master PDF: 855 pages, 7,769,065 bytes, copied to
  `~/Downloads/master.pdf`.
- Targeted final log scans found no undefined citations/references, no rerun
  request, and no fatal/package/LaTeX errors; each scan reported only its
  `Output written` line.
- Lean was intentionally left unchanged.
