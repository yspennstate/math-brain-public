# Independent reconstruction

Let (q(t)=t\log_2(1/t)+2t/\ln2), let 

\[
\Phi(f)=\sum_iq(\widehat f(\{i\})^2),\qquad
L_{c,\eta}=M+(1+\eta)U-cI,
\]

and use the reviewed producer constant (c_*=29/2+4/\ln2).  The sole
imported analytic input is the independently reviewed fresh-fair activation
inequality

\[
L_{c_*,\eta}(A(f))+2\Phi(A(f))
\le \tfrac12\{L_{c_*,\eta}(f)+2\Phi(f)\},
\qquad 0<\eta\le1. \tag{1}
\]

For a physical-coordinate block (X), define

\[
\Theta_X(f)=\sum_{x\in X}q(\operatorname{Inf}_x f)
+\sum_{i\notin X}q\!\left(\sum_{A\subseteq X}
\widehat f(\{i\}\cup A)^2\right). \tag{2}
\]

The function (q) is increasing on ([0,1]), since
(q'(t)=\log_2(1/t)+1/\ln2>0).  For (x\in X), the singleton mass is at
most (operatorname{Inf}_x f).  For (i\notin X), it is the (A=\emptyset)
summand of the orbit energy.  Thus

\[
\Phi(f)\le\Theta_X(f). \tag{3}
\]

Now let (F=A(f)) with fresh fair selector (z).  At this selector node the
inherited block is empty, the opened block is (X\cup\{z\}), and the core
child inherits (X).  From the definitions,

\[
O=\Theta_{X\cup\{z\}}(F)-\Phi(F),\qquad
R=\Theta_{X\cup\{z\}}(F)-\tfrac12\Theta_X(f), \tag{4}
\]

because the constant child has zero potential.  Subtracting in the signed
order required by SOLD cancels the entire opened orbit packet:

\[
R-O=\Phi(F)-\tfrac12\Theta_X(f). \tag{5}
\]

Equations (1), (3), and (5) give

\[
\begin{aligned}
\Delta_zL_{c_*,\eta}(F)+2(R-O)
&=L(F)-\tfrac12L(f)+2\Phi(F)-\Theta_X(f)\\
&\le \Phi(f)-\Theta_X(f)\le0. \tag{6}
\end{aligned}
\]

This proves the one-node theorem for every finite-cube Boolean core, every
core block (X), and every (0<\eta\le1).  There is no dependence on
dimension, block size, depth, bias, or overlap in (6).

The complete-tree consequence is also valid, but conditional.  If a
complete adapted core tree already satisfies SOLD with inherited block
(X), prepend the selector node above.  The ordinary restriction telescope
for (L) and the signed orbit telescope then have constant leaves, so their
terminal (L) and (Theta) terms vanish.  This gives
(L_{c_*,\eta}(F)+2\Phi(F)\le0).  At (eta=1), the reviewed mismatch
reduction yields

\[
G(F)\le(c_*+2)I(F)
=\left(\frac{33}{2}+\frac4{\ln2}\right)I(F).
\]

The exact first unpaid statement is the existence of that complete
inherited-(X) core tree.  For a stopped tree, terminal (L) and terminal
orbit reserve remain and may not be discarded.

## Scope ruling

The algebra supports “open an arbitrary core block (X) at a fresh fair
outer activation and transfer it to the core child.”  It does not support
the stronger reading “pay an arbitrary pre-existing reused history at an
arbitrary internal node”: the inherited block at the audited selector node
is explicitly empty.  It also does not cover biased or nonfresh selectors,
later data-query nodes, or universal existence of a SOLD tree.
