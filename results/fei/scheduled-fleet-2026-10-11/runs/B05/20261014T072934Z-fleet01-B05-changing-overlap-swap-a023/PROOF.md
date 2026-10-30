# A changing-overlap swap cannot be paid locally

All logarithms are base two.  Let

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
\psi_k(t)=q(t)+t\log_2k,
\]

and, for a block (X), define the reviewed logarithmic orbit potential

\[
E_X^f(S)=\sum_{A\subseteq X}\widehat f(S\cup A)^2,
\qquad
\widetilde\Lambda_X(f)=
\psi_{|X|}(E_X^f(\varnothing))+
\sum_{i\notin X}q(E_X^f(\{i\})). \tag{1}
\]

For one fixed block, (1) contracts under physical revelation and pays the
singleton potential of products sharing (X).  We test whether changing a
two-coordinate overlap by one coordinate has a universal local price.

## 1. Frozen candidate

The candidate is that some absolute (C<\infty) satisfies

\[
\widetilde\Lambda_{\{y,z\}}(f)
\le \widetilde\Lambda_{\{y,x\}}(f)
+C\bigl(\operatorname{Inf}_x(f)+\operatorname{Inf}_z(f)\bigr) \tag{2}
\]

for every Boolean (f).  This is the smallest natural swap rule that would
let the accepted fixed-block first-revelation account follow a changing
hierarchy while charging each leaving or entering physical coordinate once.

We prove that (2) is false for every (C).

## 2. Boolean counterfamily

Let (m=2r+1) be odd and let (M_m) be odd majority on private coordinates
(u_1,\ldots,u_m).  Define the genuine Boolean multiplexer

\[
f_m(y,x,z,u)=
\begin{cases}
x,&y=+1,\\
zM_m(u),&y=-1.
\end{cases} \tag{3}
\]

Equivalently,

\[
f_m=\frac{x+xy+zM_m-yzM_m}{2}. \tag{4}
\]

Set (X=\{y,x\}) and (Y=\{y,z\}).  All three displayed coordinates are
physical and active in (3), while the overlap changes only by the swap
(x\leftrightarrow z).

Since (M_m) is balanced, (4) gives

\[
E_X^{f_m}(\varnothing)=\frac12,qquad
E_X^{f_m}(\{i\})=0\quad(i\notin X). \tag{5}
\]

Therefore

\[
\widetilde\Lambda_X(f_m)=\psi_2(1/2). \tag{6}
\]

For (Y), the empty orbit vanishes, the private (x)-orbit has energy
(1/2), and every private majority coordinate has energy

\[
E_Y^{f_m}(\{u_j\})=\frac{a_m^2}{2},qquad
a_m=\widehat M_m(\{u_j\})
=\frac{\binom{2r}{r}}{4^r}. \tag{7}
\]

Hence

\[
\widetilde\Lambda_Y(f_m)=q(1/2)+m q(a_m^2/2), \tag{8}
\]

and the exact swap deficit is

\[
\boxed{
\widetilde\Lambda_Y(f_m)-\widetilde\Lambda_X(f_m)
=m q(a_m^2/2)-\frac12.} \tag{9}
\]

## 3. Divergence with bounded local pivotal credit

Stirling's formula gives

\[
a_m^2\sim\frac{2}{\pi m}.
\]

Substitution into (9) yields

\[
\widetilde\Lambda_Y(f_m)-\widetilde\Lambda_X(f_m)
=\frac1\pi\log_2m+O(1). \tag{10}
\]

On the other hand, (4) and Parseval give exactly

\[
\operatorname{Inf}_x(f_m)=\operatorname{Inf}_z(f_m)=\frac12. \tag{11}
\]

Thus the right-side fee in (2) is exactly (C), whereas the left-side
deficit diverges.  This proves that no absolute (C) can satisfy (2).

The family does not obstruct a charge to total influence: indeed

\[
I(f_m)=\frac32+\frac12I(M_m),
\]

which grows on the order of (sqrt m).  The theorem rules out only a local
nonreusing swap fee based on the entering/leaving coordinates.  It leaves
open payment by the whole transported Fourier slice, total private-core
influence, or the signed (Gamma/KL) refund.

## 4. Relation to GU

The source-checked signed-mismatch reduction says that, for
(0<\eta\le1), a universal estimate

\[
M(f)+(1+\eta)U(f)\le cI(f)
\]

would imply

\[
G(f)\le(c+2)I(f)+(1-\eta)U(f)
\]

and hence (H(f)\le[2+2(c+2)/\eta]I(f)).  The fixed-block potential was a
candidate ownership mechanism for proving that signed estimate through rare
activation hierarchies.  The present counterfamily refutes the local swap
rule (2), not the signed estimate, GU, or FEI.

`CHECK_CHANGING_OVERLAP.py` reconstructs (5)--(11) with exact rational Walsh
arithmetic for (m=1,3,5,7,9), and evaluates the exact central-binomial
formula through (m=2001).  The proof of divergence is analytic.
