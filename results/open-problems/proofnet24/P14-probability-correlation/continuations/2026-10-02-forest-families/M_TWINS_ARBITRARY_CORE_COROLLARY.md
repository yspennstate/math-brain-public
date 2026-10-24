# A smaller matrix formula for any number of identical terminals

This is an algebraic corollary of `FOUR_TWINS_ZERO_SPOKE_EXTENSION.md`.

Let H be a weighted core, with positive spoke weights a_v and d=sum a_v.
Attach m>=4 identical terminals to H, each terminal-v edge having conductance
a_v, and mark matching edges e,f on four of these terminals. Core and spoke
activities scale by lambda. Other terminal-to-terminal edges are absent.
Define M_m=L_H+m diag(a), W_m=det(M_m), and let mu_i be the generalized core
Laplacian eigenvalues, that is the eigenvalues of
 diag(a)^{-1/2} L_H diag(a)^{-1/2}.

The same two leading Rayleigh coefficients vanish. Its third coefficient is

\[
\begin{aligned}
 H_2
 &=\frac{4d^{2m-6}W_m^2}{m^4}
       \left(\sum_i\left(\frac{m}{m+\mu_i}\right)^2-1\right)\\
 &=\frac{4d^{2m-8}}{m^4}\sum_{u,v}a_ua_v
       \left(md\operatorname{adj}(M_m)_{uv}-W_m\right)^2.
\end{aligned}
\]

It is strictly positive if the core has at least two vertices. By continuity,
one may again allow zero spoke weights, provided every core component is
anchored; strictness then requires at least two positive a_v.

**Derivation.** Treat the m-4 extra terminals as core vertices with zero spoke
weight in the four-terminal theorem. Put k=m-4. The enlarged matrix is

\[
 \widehat M=
 \begin{pmatrix}L_H+mD_a&-a\mathbf1_k^T\\
                 -\mathbf1_k a^T&dI_k\end{pmatrix}.
\]

The Schur complement is M_m-(k/d)aa^T. Since M_m^{-1}a=1/m, where 1 is the
constant vector,

\[
 \det\widehat M=d^kW_m(1-k/m)=\frac4m d^{m-4}W_m.
\]

Put P_m=mD_a^{1/2}M_m^{-1}D_a^{1/2} and u=sqrt(a)/sqrt(d).
The supported block of the four-terminal matrix Q is, by the rank-one inverse
formula,

\[
 \widehat Q=\frac4mP_m+\frac{k}{m}uu^T.
\]

Consequently Q-uu^T=(4/m)(P_m-uu^T) on the support, and its other rows and
columns vanish. Substituting in the earlier Frobenius-norm formula gives the
first equality above. Since P_m u=u, its eigenvalues are m/(m+mu_i), and
converting its entries to adjugates proves the second equality.

For empty H-edge set and a_v=1 at s hubs, this reduces to
H_2=4(s-1)s^{2m-6}m^{2s-4}, the bipartite corollary already checked in the
zero-spoke extension. No new conjecture is solved by this reformulation.
