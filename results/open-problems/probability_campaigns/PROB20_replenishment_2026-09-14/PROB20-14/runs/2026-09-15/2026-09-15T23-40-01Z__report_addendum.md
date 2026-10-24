# PROB20-14 — addendum to 2026-09-15T23:40:00Z report

**SOLUTION STATUS: PARTIAL (unchanged).**

This append-only addendum makes one notation correction and sharpens the denominator-adapted large-forest cutoff from Section 6 of the main report.

## 1. Notation correction

In the first displayed line of Section 6, the convolution mass was typeset once as `\nu^{*b}_{M-c}`. The intended quantity throughout is
\[
u^{*b}_{M-c}
\]
with `u`, i.e. the excess-total-progeny law defined in (3.1). Equations (6.4) onward already use `u`; there is no change to the argument.

## 2. Sharper slow-inflation cutoff

The main report chose
\[
t_M=\sqrt{(L_M+1)/M},\qquad L_M=-\log u_M,
\]
only for a simple explicit formula. One can get a substantially smaller cutoff, closer to the intrinsic Laplace scale, by letting the factor above the denominator cost diverge arbitrarily slowly.

Since \(L_M=o(M)\), put
\[
x_M:=\frac{M}{L_M+1}\longrightarrow\infty
\]
and choose any deterministic
\[
a_M\to\infty,\qquad a_M=o(x_M).
\tag{A.1}
\]
For example,
\[
a_M=\log(e+x_M)
\]
works. Define
\[
\boxed{
t_M:=a_M\frac{L_M+1}{M}.
}
\tag{A.2}
\]
Then
\[
t_M\downarrow0,\qquad Mt_M=a_M(L_M+1),
\qquad \frac{L_M}{Mt_M}\to0.
\tag{A.3}
\]
The same Chernoff inequality from (6.4) gives, uniformly in every shift \(c\ge0\),
\[
\frac{u^{*b}_{M-c}}{u_M}
\le
\exp\{L_M+t_MM-bK(t_M)\}.
\tag{A.4}
\]
Define
\[
\boxed{
\beta_M^{(a)}:=
\left\lceil\frac{2Mt_M}{K(t_M)}\right\rceil
=\left\lceil\frac{2M}{\psi(t_M)}\right\rceil,
\qquad \psi(t)=K(t)/t.
}
\tag{A.5}
\]
Then for \(b\ge\beta_M^{(a)}\),
\[
\boxed{
\sup_{c\ge0}
\frac{u^{*b}_{M-c}}{u_M}
\le
\exp\{L_M-Mt_M\}
\longrightarrow0.
}
\tag{A.6}
\]
There is no ceiling loss in this upper bound: \(b\ge\lceil2Mt_M/K(t_M)\rceil\) implies \(bK(t_M)\ge2Mt_M\) exactly.

Now apply the new Laplace window from the main report,
\[
K(t)/t^{1/q}\to\infty,
\qquad
K(t)/\sqrt t\to0.
\]
Equivalently,
\[
t^{(q-1)/q}\psi(t)\to\infty,
\qquad
\sqrt t\,\psi(t)\to0.
\]
Hence
\[
\boxed{
M\sqrt{t_M}\ll \beta_M^{(a)}
\ll_o M t_M^{(q-1)/q}.
}
\tag{A.7}
\]
Substituting (A.2),
\[
\boxed{
\sqrt{M a_M(L_M+1)}
\ll \beta_M^{(a)}
\ll_o
M^{1/q}\,[a_M(L_M+1)]^{(q-1)/q}.
}
\tag{A.8}
\]
In particular,
\[
\beta_M^{(a)}\to\infty,
\qquad
\beta_M^{(a)}=o(M).
\]

Because \(a_M\) may diverge as slowly as desired subject to (A.1), (A.8) is sharper than the square-root choice in the main report. It puts the large-count suppression, up to an arbitrarily slow denominator-paying factor, at the natural heavy-tail scale
\[
M^{1/q}(L_M+1)^{(q-1)/q}
\]
on the upper side, without assuming regular variation.

For a regularly varying comparison law with offspring stable index \(\alpha\in(q,2)\), one would have heuristically \(K(t)\asymp t^{1/\alpha}\), and (A.5) becomes of order
\[
M^{1/\alpha}[a_M(L_M+1)]^{(\alpha-1)/\alpha};
\]
this comparison is only explanatory and is not used in the theorem.

## 3. Revised unresolved corridor

Every conclusion of Sections 7–8 of the main report remains valid with \(\beta_M\) replaced by the smaller \(\beta_M^{(a)}\). After choosing the diagonal small-count cutoff \(\alpha_M\to\infty\) with
\[
\alpha_M<\beta_M^{(a)}/2,
\]
the only unresolved balanced-prefix contribution lies in
\[
\boxed{
\alpha_M<B_k<\beta_M^{(a)},
\qquad
0\le C\le D_k(1+B_k).
}
\tag{A.9}
\]
Thus this run narrows the large edge of the mesoscopic corridor to an arbitrarily slowly inflated Laplace/denominator scale. It still does not prove the averaged local ratio inside (A.9), so the universal every-fixed-level theorem remains open.
