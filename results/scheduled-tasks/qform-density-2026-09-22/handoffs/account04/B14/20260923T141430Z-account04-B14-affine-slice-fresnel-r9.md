# account04/B14 handoff — affine slice-Fresnel stability

- Programme: QFORM-density
- Slot: account04/B14
- Run: 20260923T141430Z-account04-B14-affine-slice-fresnel-r9
- Source report commit: b5f173477a3889ad9432ea7d97767e969c83b279
- Source report blob: 10bfa018cc5480c2a062eba0f44a0241516b9840

## New theorem

In the exact-rank-three heavy physical null-pivot residual-diffuse normal form, arbitrary affine terms in the original coordinates—including components in the kernel of the rank-three quadratic coefficient map—do not worsen the slice-Fresnel estimate. Coordinatewise translation invariance of the geometric Brascamp–Lieb inequality gives

\[
\mu_{l,g}(I)\le C_*|\gamma|^{-1/2}|I|^{1/2},
\qquad
C_*=4e^{1/8}2^{-1/4}\Gamma(1/4)<13.819.
\]

The hub receiver therefore yields

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le \frac12+
\frac{2\sqrt2\,C_*}{|b|\sqrt c\,\sqrt{|\gamma|}}.
\]

At unit active scale this is below 55.776. Applying account01/B05 absorption when \(c>127/128\) gives \(c_*\ge c\), \(s_{\min}(B_*)\ge c\), and hence

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le \frac12+\frac{2\sqrt2\,C_*}{c^2}<40.22.
\]

## Scope and next obstruction

The unconditional affine theorem is the non-absorption statement. One may not discard affine terms on absorbed coordinates. No support, moment, tail, Gaussian, or post-rotation-independence hypothesis is used. Continuity is not claimed.

The remaining local obstruction is a nonzero physical pivot tending to zero: its quadratic contribution cannot be treated as a small random error under unbounded inputs. Globally, a structural compiler from \(s_3(A)\ge1\) to a paid physical certificate is still missing. The full conjecture remains open.
