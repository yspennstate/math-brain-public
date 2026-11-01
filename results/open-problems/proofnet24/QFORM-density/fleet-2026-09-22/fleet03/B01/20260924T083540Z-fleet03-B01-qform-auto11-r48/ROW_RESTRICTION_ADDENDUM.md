# r48 addendum — pivot-free coupled-row cubic restriction

This addendum is part of the same actual run `20260924T083540Z-fleet03-B01-qform-auto11-r48`. It uses the raw ambiguity cell `F_u(s)` and difference density `m(u)` defined in `REPORT.md`, and it preserves every target hypothesis. It does **not** claim the full QFORM theorem.

## Theorem `QFORM-COUPLED-ROW-RAW-L3-v1`

Let `X=(X_1,...,X_n)` have independent densities bounded by one, let `X'` be an independent copy, and set `U_k=X_k-X'_k`. Fix an original coordinate `j` and write

\[
r_j:=\Bigl(\sum_{k\ne j}A_{jk}^2\Bigr)^{1/2}.
\]

Assume `r_j>0`. Let `m_k` be the density of `U_k`, and let `F_{j,u}(s)` be the raw ambiguity cell of coordinate `j`. Define

\[
\mathcal R_j(T)
=
\int_{-T}^T\int_{\mathbb R^n}
\left|F_{j,u_j}\bigl(t(Au)_j\bigr)\right|^3
\prod_{k\ne j}m_k(u_k)\,du\,dt.
\]

Then, for every `T>0`,

\[
\boxed{
\mathcal R_j(T)
\le
\min\left\{
2T,
\frac{2\pi\sqrt2}{r_j}
\left[1+\log_+\!\left(\frac{Tr_j}{\pi\sqrt2}\right)\right]
\right\}.
}
\tag{A.1}
\]

In particular, the estimate does not require `A_jj != 0`; it is a pivot-free averaged-frequency bound on one actual coupled row of the full quadratic form.

## Proof

Each difference variable `U_k` has density

\[
m_k(u)=\int f_k(x)f_k(x-u)\,dx\le1.
\]

Set

\[
Z_j=\sum_{k\ne j}A_{jk}U_k.
\]

The standard Ball--Rogozin one-dimensional product-projection inequality gives

\[
\|p_{Z_j}\|_\infty\le K_j:=\frac{\sqrt2}{r_j}.
\tag{A.2}
\]

For the `j`-th raw cell, the `q=3` estimate already proved in `REPORT.md` is

\[
\int_{\mathbb R}|F_{j,u}(s)|^3\,ds\le\pi m_j(u)^2,
\tag{A.3}
\]

and trivially `|F_{j,u}(s)|<=m_j(u)`.

Fix `u` and a scalar `w`. Therefore

\[
\begin{aligned}
J_T(u,w)
&:=\int_{-T}^T|F_{j,u}(tw)|^3\,dt\\
&\le
\min\left\{2T m_j(u)^3,\frac{\pi m_j(u)^2}{|w|}\right\}.
\end{aligned}
\tag{A.4}
\]

For fixed `U_j=u`,

\[
W=A_{jj}u+Z_j
\]

has a density bounded by `K_j`; translation by `A_jj u` changes no cap. For a probability density bounded by `K` and the symmetric decreasing kernel

\[
h_L(w)=\min\{L,\pi/|w|\},
\]

the bathtub principle gives

\[
\mathbb E h_L(W)
\le2K\int_0^{1/(2K)}h_L(s)\,ds.
\tag{A.5}
\]

With `L=2Tm_j(u)`, the right-hand side equals

\[
\begin{cases}
2Tm_j(u),&Tm_j(u)\le\pi K,\\
2\pi K\left[1+\log\!\left(\dfrac{Tm_j(u)}{\pi K}\right)\right],&Tm_j(u)>\pi K.
\end{cases}
\tag{A.6}
\]

Combining (A.4)-(A.6), using `m_j<=1`, and then integrating `u` gives

\[
\mathcal R_j(T)
\le
2\pi K_j\left[1+\log_+\!\left(\frac{T}{\pi K_j}\right)\right]
\int m_j(u)^2du.
\]

Since `m_j<=1` and `int m_j=1`, `int m_j^2<=1`; substituting `K_j=sqrt(2)/r_j` proves the logarithmic term in (A.1). The trivial bound `mathcal R_j(T)<=2T` follows from `|F_{j,u}|<=m_j(u)` and `int m_j^3<=1`. QED.

## Connection to the full target

The exact decoupling identity in the main report is

\[
|\phi_Q(t)|^2
=\int\prod_i F_{i,u_i}(t(Au)_i)\,du.
\]

(A.1) therefore supplies a dimension-free frequency budget for each physical row using its entire off-diagonal `ell^2` energy rather than one physical coefficient or one scalar pivot. This is potentially useful in the diffuse-entry collar, where no individual coefficient need be large.

The remaining implication is genuinely multilinear: aggregate several row budgets before taking absolute values or normalizing by the difference masses `m_i`. The main report proves that a generic absolute Brascamp--Lieb closure based only on individual unweighted phase-space norms cannot have the required scaling, so (A.1) should be used only inside a more structured/signed aggregation.

## Source used for (A.2)

The Ball--Rogozin linear-form cap is already source-pinned in the QFORM fleet; one explicit source is `yspennstate/math-open-problems@b160cb60264aea801829a91df9c8e9d51350eaff`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B14/20260924T012603Z-fleet01-B14-QFORM-auto11/REPORT.md`, equation (0.2).
