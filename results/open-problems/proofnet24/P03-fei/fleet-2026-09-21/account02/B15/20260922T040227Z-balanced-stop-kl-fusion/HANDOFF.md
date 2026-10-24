# B15 handoff — balanced occurrence-KL target

**Source report:** `REPORT.md` in this directory.  
**Status:** full FEI remains OPEN.

Using account03/B13's constant-for-constant balanced-support-deficit equivalence and account03/B18's harmonic deletion source, this run proves two universal support-deficit payments for every balanced Boolean `f`, with `beta=I(f)-1`:

\[
T_{\rm stop}\le C_{\rm stop}\,\beta,
\qquad
J(f)\le C_J\,\beta,
\qquad
R(f)\le2C_J\,\beta.
\]

The first bound follows from `T_stop<=H(K)`, quantitative FKN stability near level one, and edge isoperimetry. The second uses the same FKN near-character reduction. Constants are finite absolute constants; no optimization is attempted.

More importantly, if

\[
\alpha_i=E[1_{i\in S}/K],\quad
\rho_i=E[(K-1)1_{i\in S}/K]/\beta,\quad
q_i=\operatorname{Inf}_i/I,
\]

then `q=(alpha+beta rho)/I`, so the root and deletion address entropies fuse exactly with the negative credit

\[
\mathcal J_{\rm mix}
=D_2(\alpha\|q)+\beta D_2(\rho\|q).
\]

Together with the prior prefix KL `K_rho`,

\[
\boxed{
H(f)=I H_2(q)+T_{\rm stop}-E\log_2(K!)-\mathcal K_\rho-\mathcal J_{\rm mix}.
}
\]

Thus the exact remaining balanced Shannon implication is

\[
\boxed{
I H_2(q)-E\log_2(K!)-\mathcal K_\rho-\mathcal J_{\rm mix}
\le C_{\rm occ}(I-1).
}
\]

A valuation-assisted sufficient form, now legal because `R=O(I-1)`, is

\[
E\log_2(K!)+\mathcal K_\rho+\mathcal J_{\rm mix}+R
\ge I H_2(q)-C_*(I-1).
\]

The new mixing credit is mandatory. For the balanced suspension of the `m`-bit one-point defect,

\[
\mathcal J_{\rm mix}/(I-1)=m-\log_2m+O(1)\to\infty,
\qquad
H/(I-1)\to4.
\]

Dropping only `-J_mix` while retaining the factorial and prefix KL credits therefore gives an unbounded false proxy. The next common proof attempt should keep all three information refunds and spend the one-time valuation reserve against the occurrence-profile entropy `I H(q)`; do not return to root/deletion-separate `O(I)` accounting.
