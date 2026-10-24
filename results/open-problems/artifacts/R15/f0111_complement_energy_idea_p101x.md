# R15 idea-before-code note — complement-energy duality for the last F0111 cells

Date: 2026-09-20 UTC.

Status: retained Talagrand F0111 `k=2` screen only; **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. Native Burdzy--Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` with no surviving frozen candidate and is not reopened. No queue item is promoted.

Methods: **#3 PROVE SOMETHING STRONGER**, **#11 DUALIZE**, **#25 COUNT THE SAME THING TWICE**. The immediately preceding complete R15 report used #6/#14/#20. The R15 history has already exhausted all thirty method numbers, so these are nonconsecutive re-entry methods on a new reduced object.

## New route

For the `k=2` hazard

\[
F(t)=\sum_i t_i-\log\!\left(\sum_i e^{t_i}-(n-1)\right)
\]

let

\[
P(t)=\sum_i A_i t_i+\sum_{i<j}B_{ij}t_it_j,\qquad A_i,B_{ij}\ge0,
\]

be a hypothetical global quadratic majorant with exact value and gradient contact at an interior point `q`.

Fix any nonempty proper coordinate set `J` and put `K=J^c`. Define the contact energies

\[
E_{JJ}=\sum_{i<j\in J}B_{ij}q_iq_j,\quad
E_{JK}=\sum_{i\in J,j\in K}B_{ij}q_iq_j,\quad
E_{KK}=\sum_{i<j\in K}B_{ij}q_iq_j,
\]

\[
W=E_{JJ}+E_{JK}+E_{KK},\qquad
D_J=\sum_{i\in J}q_i\partial_iF(q)=\sum_{i\in J}q_i(1-r_i).
\]

Exact gradient contact counted over `J` gives

\[
D_J=A_J^{(q)}+2E_{JJ}+E_{JK},\qquad
A_J^{(q)}:=\sum_{i\in J}A_iq_i.
\]

Exact full value/gradient contact gives `W=D-F(q)`. Eliminating `A_J^{(q)}` and `E_{JK}` yields

\[
A_J^{(q)}=D_J-W-E_{JJ}+E_{KK}.
\]

Now restrict the global certificate to the ray `t q_J` obtained by retaining the `J` coordinates of `q` and setting the complement to zero. Along this ray

\[
P(tq_J)=tA_J^{(q)}+t^2E_{JJ}.
\]

Therefore for every `t>0`,

\[
\boxed{E_{KK}+(t-1)E_{JJ}\ge W-D_J+\frac{F(tq_J)}t.}
\]

This is a new exact **complement-energy family**: global safety on one face forces energy into the complementary face. It is stronger to solve it by duality rather than choose one `t`.

Let

\[
g_J(t)=\frac{F(tq_J)}t,\qquad
\Phi_J(B)=\sup_{t>0}\{g_J(t)-Bt\}.
\]

The earlier all-ray theorem proves `g_J` is strictly concave (unless `J` has one active coordinate, the trivial case). Hence the complete family above is equivalent to

\[
\boxed{E_{KK}\ge W-D_J+E_{JJ}+\Phi_J(E_{JJ}).}
\]

If `B_*:=g_J'(1)` and an independent argument gives `E_{JJ}\le \bar E<B_*`, then strict concavity implies the right side is decreasing as a function of `E_{JJ}` on `[0,B_*]`, and so

\[
\boxed{E_{KK}\ge W-D_J+\bar E+\Phi_J(\bar E).}
\]

This is the desired bridge between the exact all-ray cone and the residual-Gram/null-flow machinery.

## Heterogeneity-sensitive Gram cap

For the remaining `n=30` two-level Hessian-null cells, the projective downdate has Gram vectors `w_i` with

\[
B_{ij}=\langle w_i,w_j\rangle+A_Jr_ir_j\quad(i\ne j\in J),
\qquad
\|w_i\|^2=e_i:=r_i(1-A_Jr_i),
\]

and the null relation

\[
\sum_{i\in J}w_i=\frac ba\sum_{j\in K}w_j,\qquad
T:=\left\|\sum_{j\in K}w_j\right\|^2\le T_{\rm cap}.
\]

Put `R_J=sum_{i in J} r_i q_i` and `Z_J=sum_{i in J} q_i w_i`. Then **exactly**

\[
E_{JJ}=\frac12\left(\|Z_J\|^2-\sum_{i\in J}e_iq_i^2\right)
+\frac{A_J}{2}\left(R_J^2-\sum_{i\in J}r_i^2q_i^2\right).
\]

For any real `theta`,

\[
Z_J=\theta\frac ba\sum_{j\in K}w_j+
\sum_{i\in J}(q_i-\theta)w_i,
\]

so

\[
\|Z_J\|\le \frac ba|\theta|\sqrt{T_{\rm cap}}
+\sum_{i\in J}|q_i-\theta|\sqrt{e_i}.
\]

Substitution gives a heterogeneity-sensitive upper bound on `E_JJ`; unlike the previous crude `U q_(1)q_(2)` bound, it becomes strong both when the `J` coordinates are nearly equal and when one coordinate is heavy (because its residual norm `sqrt(e_i)` is then small). The next step is to combine this cap with the complement-energy dual inequality and the tiny `K`-excess roof in the two surviving cells `N=12,13`.

No checker is warranted until this exact bridge is written and algebraically audited; the theorem-sized claims will be proved on the run report page first.
