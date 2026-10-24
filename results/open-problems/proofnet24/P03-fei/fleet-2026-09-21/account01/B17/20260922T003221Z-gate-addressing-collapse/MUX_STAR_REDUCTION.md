# Exact MUX-to-AND star reduction

This note sharpens the addressing result in `REPORT.md`. It is an exact
identity for any symmetric potential and does not use the unavailable
`cert_vi_h96k40_f4.npz` data.

Let `Psi` be a symmetric candidate potential, write

\[
C=\Psi(1/2),\qquad V_p=4p(1-p),
\]

and let `D_G^Psi` denote the gate slack for `(G)` computed with `Psi`.
Consider the 2-input AND gate with input biases `(p,1/2)`. Its squared biased
Fourier masses are

\[
(1-p)^2,\quad p^2,\quad V_p/4,\quad V_p/4,
\]

so its spectral entropy is exactly

\[
\widetilde H_{\rm AND}(p,1/2)=2h(p).
\]

Its two biased influences are `V_p/2` and `p`, and its output bias is `p/2`.
Therefore

\[
D^{\Psi}_{\rm AND}(p,1/2)
=\frac12\bigl(\Psi(p)+h(V_p)\bigr)
 +pC-2h(p)-\Psi(p/2).
\tag{1}
\]

Now let `MUX_p,q` be the one-address-bit multiplexer with address bias `p`
and its two data bits having the same bias `q`. The addressing calculation in
`REPORT.md` gives

\[
D^{\Psi}_{\rm MUX}(p,q)
=\frac{V_q}{2}\bigl(\Psi(p)+h(V_p)-4h(p)\bigr).
\tag{2}
\]

Combining (1) and (2) yields the exact identity

\[
\boxed{
D^{\Psi}_{\rm MUX}(p,q)
=V_q\left[
D^{\Psi}_{\rm AND}(p,1/2)
+\Psi(p/2)-p\Psi(1/2)
\right].
}
\tag{3}
\]

Hence MUX needs no genuinely three-dimensional estimate if two one-dimensional
facts are known:

1. the AND inequality at `(p,1/2)`, and
2. the **star-concavity inequality**

\[
\boxed{\Psi(p/2)\ge p\Psi(1/2),\qquad 0\le p\le1/2.}
\tag{4}
\]

(The other half follows by NPN symmetry of MUX.) Concavity of `Psi` on
`[0,1/2]` with `Psi(0)=0` is sufficient for (4), but full concavity is not
needed.

For the margin-adjusted candidate

\[
\Psi_c(z)=\Gamma(z)+c z(1-z),
\]

its star defect is

\[
\Psi_c(p/2)-p\Psi_c(1/2)
=\Gamma(p/2)-p\Gamma(1/2)+\frac c4p(1-p).
\tag{5}
\]

Thus a positive gate margin `c` itself helps the star condition. Equations
(3)–(5) reduce the common-data addressing family to a **one-dimensional
interval certification problem**, not an arity-3 box problem.

For `Addr_k` with address biases `p_i` and common data bias `q`, summing (3)
coordinatewise gives

\[
\boxed{
D^{\Psi}_{\rm Addr_k}
=V_q\sum_{i=1}^k
\left[
D^{\Psi}_{\rm AND}(p_i,1/2)
+\Psi(p_i/2)-p_i\Psi(1/2)
\right].
}
\tag{6}
\]

So once (4) is certified for the immutable candidate potential, **every
common-data addressing gate in every dimension follows directly from the
already certified AND family**.

For orientation only (not a certification of the current `f4` candidate),
the older committed `cert_vi_h96k40` report records `C=6.4548` and the
representation `G(x)-2(C-4)x >= 2.22922` over its grid/tail. That crude lower
bound alone already implies (4) for `p <= 2^{-1.17541} approx 0.4426`; only a
small interval adjacent to `1/2` would remain for that older candidate. The
current `f4` binary is not present at the canonical repository path, so no
claim is made here that (4) has yet been certified for it.

**Status:** essential reduction only; full FEI remains open.
