# Bridge certificate JSON format

This directory stores exact algebra certificates for the finite-state
nonbacktracking bridge route.

The verifier is:

```powershell
python scripts\bridge_certificate_verify.py research\certificates\regular_tree_D3_bridge.json
python scripts\bridge_certificate_verify.py research\certificates\regular_tree_D3_detour.json
python scripts\bridge_certificate_verify.py research\certificates\semiregular_tree_2_3_detour.json
python scripts\bridge_certificate_verify.py --self-test
python scripts\bridge_certificate_verify.py --directory research\certificates
```

Each certificate is a JSON object with these fields:

- `criterion`: optional; either `"regular_bridge"` (default) or
  `"bounded_degree_detour"`.
- `degree`: integer \(D\ge3\).
- `pc_upper`: rational upper bound \(q\in(0,1)\) for \(p_c(G)\).
- `rho_sphere_upper_sq`: rational upper bound \(R\ge\rho_{\mathrm{sph},2}(G)^2\).
- `lambda_upper`: rational \(\lambda>0\).
- `matrix`: square nonnegative rational matrix \(M\).
- `left_vector`: nonzero nonnegative rational vector \(a\).
- `right_vector`: nonzero nonnegative rational vector \(b\).
- `positive_vector`: strictly positive rational vector \(v\).

Optional graph-specific field:

- `bridge_majorization`: currently only `"regular_tree_one_state"` is
  supported, and is only for `criterion = "regular_bridge"`.  This checks the
  exact \(D\)-regular tree bridge-probability calculation
  \[
    B_n^{\mathrm{NB}}(s)=\frac{1}{D(D-1)^{n-1}}
  \]
  against the one-state bound \(aM^nb\) for every \(n\ge1\).
- `detour_majorization`: currently only `"tree_count_one_state"` is
  supported, and is only for `criterion = "bounded_degree_detour"`.  This
  checks the exact tree detour-count calculation
  \[
    \sup_{\operatorname{dist}(x,y)=n}\sum_{k\ge0}q^kN_{n+k}(x,y)=1
  \]
  against the one-state bound \(aM^nb\) for every \(n\ge0\).
  Finite-quotient tree calibrations use this same one-state detour check after
  separate rational bounds for \(p_c\) and \(\rho_{\mathrm{sph},2}^2\) have
  been supplied.

Rationals may be JSON integers or strings accepted by Python's `Fraction`,
such as `"17/23"`.

The verifier checks:

\[
  a,b\ge0,\qquad a\ne0,\qquad b\ne0,
\]
with dimensions compatible with \(M\),
\[
  Mv\le \lambda v
\]
coordinatewise and
\[
  \bigl(q(D-1)\lambda\bigr)^2R<1.
\]
for `regular_bridge`, or
\[
  (q\lambda)^2R<1.
\]
for `bounded_degree_detour`.

Except for the supported regular-tree calibrations, it does not check the
graph-specific majorization
\[
  B_n^{\mathrm{NB}}(q(D-1))\le a^TM^nb.
\]
or its bounded-degree count-kernel analogue.  That inequality must be proved
by the radial, automaton, or transfer-matrix construction that produced the
certificate.
