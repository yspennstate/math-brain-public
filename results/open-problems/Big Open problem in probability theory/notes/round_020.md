# Round 020 log

Date: 2026-06-08

## Focus

Tested whether exact finite-length SAW operator bounds can close the remaining
\(T_3\square\mathbb Z\) line-factor case.

## Method

The SAW kernels are submultiplicative, so
\[
  \gamma_{\rm SAW,2}(G)\le \|C_m\|_{2\to2}^{1/m}
\]
for every fixed \(m\).  On \(T_d\square\mathbb Z\), the length-\(m\) SAW
kernel is radial in the tree coordinate and translation-invariant in the
\(\mathbb Z\)-coordinate.  If \(a_{r,h}\) is the number of length-\(m\) SAWs
from the origin to a fixed endpoint at tree distance \(r\) and height \(h\),
then
\[
  C_m=\sum_{r,h}a_{r,h}R_r\otimes S^h,
\]
where \(R_r\) is the tree sphere kernel and \(S\) is the shift on
\(\mathbb Z\).  Hence
\[
  \|C_m\|_{2\to2}
  =
  \sum_{r,h}a_{r,h}\|R_r\|_{2\to2}.
\]
The equality holds because the spherical/Fourier transform attains the
triangle bound at the tree spectral edge and at vertical frequency \(0\) or
\(\pi\): every length-\(m\) endpoint satisfies \(r+h\equiv m\pmod 2\), so all
signs align.

For \(T_3\), the sphere norms satisfy
\[
  \|R_0\|=1,\qquad \|R_1\|=2\sqrt2,\qquad
  \|R_2\|=5,\qquad
  \|R_{r+1}\|=2\sqrt2\|R_r\|-2\|R_{r-1}\|.
\]

## Results

Exact enumeration gives:
\[
  \|C_{12}\|_{2\to2}
  =
  3110764+2209048\sqrt2,
\]
and therefore
\[
  \|C_{12}\|_{2\to2}^{1/12}\le3.683286.
\]
Continuing the same computation gives:
\[
  \|C_{13}\|_{2\to2}^{1/13}\le3.669978,
  \qquad
  \|C_{14}\|_{2\to2}^{1/14}\le3.657847.
\]

The computation is reproducible via
`scripts/saw_spherical_bound.py`.  For example:

```powershell
python scripts\saw_spherical_bound.py --degree 3 --length 12
```

## Interpretation

These bounds improve the nonbacktracking exponent
\[
  \beta(5,2\sqrt2+2)\approx3.766408,
\]
so finite-length self-avoidance does help.  However, the improvement is much
too small to close \(T_3\square\mathbb Z\) with the current \(p_c\) upper
bounds.  The current target would require an operator exponent below roughly
\[
  1/0.3153\approx3.17
\]
using the two-step vertical-branching comparison.

## Status

Brute-force finite-length submultiplicativity is not the right tool by itself.
The next useful step is a structural SAW bound that captures long-range
self-avoidance, or a stronger \(p_c\) comparison for \(T_3\square\mathbb Z\).
