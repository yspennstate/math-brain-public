# B16 handoff — coherent signed live-low source now has a dimension-free authentic parent aggregation

**Full FEI:** OPEN / NOT PROVED.

**New proved interface-C component.** For every Boolean \(f\), every authentic retained terminal code, every authentic ordered active q-flip system, and every measurable live Borel window \(W\) of the genuine low-resolvent kernel \(w_{<2}\), define the terminal-aware signed radial feature
\[
F_W(S)=
\mathbb E_{P_0}\Phi_W(\beta(q_S+m)^2)
-
\mathbb E_{P_1}\Phi_W(\beta(q_S+m)^2),
\]
with
\[
\Phi_W(x)=\int_Ww_{<2}(s)[1-\cos(s\sqrt x)]\,ds,
\qquad
F_W^-=\tfrac12(F_W-F_W\circ\tau_M).
\]
Then the exact fleet03 square-root parent coefficients
\[
\lambda_{j,W}=4\|\partial_jL^{-1/2}F_W^-\|_2^2
\]
satisfy
\[
\boxed{\sum_j\lambda_{j,W}
=\mathbb E|D_W|^2
\le64J(f).}
\]

The proof is source-exact. For any nonnegative Borel kernel \(w\) with
\(L_w=\int s w(s)ds<\infty\),
the signed two-cell amplitude path gives
\[
\mathbb E_P|\Delta K_w|^2\le 8L_w^2J(f)/N.
\]
The terminal difference obeys exactly
\[
\partial_jF_w^-=-\tfrac14(\Delta_{P_0,j}-\Delta_{P_1,j}),
\]
hence
\[
\|\partial_jF_w^-\|_2^2\le2L_w^2J/N.
\]
There are fewer than \(N\) active q-flips, and \(L^{-1/2}\) is an \(L^2\) contraction on every nonzero active mode, giving
\[
\mathbb E|D_w|^2
=4\sum_j\|\partial_jL^{-1/2}F_w^-\|_2^2
\le8L_w^2J.
\]
For the exact low-resolvent kernel,
\[
\int_0^\infty s w_{<2}(s)ds=2\sqrt2,
\]
which yields 64.

**Why this is not the refuted positive-current estimate.** The Boolean/comparator subtraction, terminal subtraction and signed Borel integration occur **before** the square. The half-band no-go concerns an integral of positive squares. The difference is the Borel-scale variance:
\[
\int\|Z\|^2d\mu
=
M^{-1}\|\int Z\,d\mu\|^2
+
\int\|Z-\bar Z\|^2d\mu.
\]
This run pays the coherent first component; it does not pay the orthogonal scale-variance term.

**Named peer results consumed and applied.**
- fleet03/B16 `20260921T222504Z-finite-window-amplitude-transport/REPORT.md`, blob `7f15e8e4b5d14723d4e304e8a854bda847e30ebb`: supplies the signed amplitude path and explicitly left parent/multiplicity aggregation open; this handoff closes that aggregation for the coherent live-low feature.
- fleet03/B16 `20260921T211732Z-signed-square-root-resolvent/REPORT.md`: supplies the exact terminal-aware parent factorization.
- fleet04/B16 `20260921T221559Z-cell-mobius-rkhs-orientation/REPORT.md`, blob `4b4e4680852d3f0a5665c7a2a04f4bafb1d0f9e6`: its mixed cell overlap is already-spent internal cancellation; this proof does not reuse it.
- fleet03/B17 `20260921T223248Z-relation-orientation-lift/REPORT.md`, blob `ba900d4cc7cb6c7e2757b8983b3c1960577dea0e`: scalar shell compression is not losslessly orientation-identifying, so the coherent component is paid before such compression.

**Exact incompatibility / remaining ledger.** The same first-moment method cannot absorb the high-resolvent companion because
\[
w_{>2}(s)\sim4s^{-3}\quad(s\downarrow0),
\qquad
\int_0^\epsilon s\,w_{>2}(s)ds=\infty.
\]
The high/R16 term therefore remains signed and co-located. Outside-live cross terms, terminal endpoint, negative R32 credits and orientation terms also remain unspent.

**Next exact implication.** Match the authentic current to its coherent Borel projection plus orthogonal Borel-scale variance, then pay or cancel only that residual using the co-located high/outside-live/negative/terminal ledger and fleet03/B18's signed ordered flag bank. Do not return to complete-positive-current contraction or scalar-parent TV inversion.

Checker SHA-256 `8c4811d578448ca89757ec41e0e86b508db8d98b3ffeebd4d7f2025f621e8867`; output SHA-256 `ed1f04152997ea12f547ce3bd47237bee761e060fb69b1f1fb090bf7c9a91f84`; status PASS on 54 finite compiler configurations. Self-check only.

**FULL-PROBLEM CHANGE:** NONE.  
**MECHANISM CHANGE:** YES — from post-square parent/flag reconstruction to pre-square coherent signed Borel integration plus exact active-parent aggregation.
