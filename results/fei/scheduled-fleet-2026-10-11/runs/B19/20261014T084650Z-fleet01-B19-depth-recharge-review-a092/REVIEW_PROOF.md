# Independent proof and scope audit

All logarithms are base two.  The reviewed potential is

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
\psi_k(t)=q(t)+t\log_2k,
\]

\[
E_X^f(S)=\sum_{A\subseteq X}\widehat f(S\cup A)^2,qquad
\widetilde\Lambda_X(f)=\psi_{|X|}(E_X^f(\varnothing))+
\sum_{i\notin X}q(E_X^f(\{i\})).
\]

## 1. Reconstruction from the Boolean definition

Let

\[
f(y,x,z,u)=\begin{cases}x,&y=1,\\zu,&y=-1.\end{cases}
\]

Then directly

\[
f=\frac{x+xy+zu-yzu}{2}.
\]

Thus the only nonzero Walsh coefficients are

\[
\widehat f(\{x\})=\widehat f(\{x,y\})=
\widehat f(\{z,u\})=\frac12,qquad
\widehat f(\{y,z,u\})=-\frac12.
\]

For \(X=\{y,x\}\),

\[
E_X(\varnothing)=\frac12,qquad E_X(\{z\})=E_X(\{u\})=0,
\]

so

\[
\widetilde\Lambda_X=\psi_2(1/2)=q(1/2)+\frac12
=1+\frac1{\ln2}.
\]

For \(Y=\{y,z\}\),

\[
E_Y(\varnothing)=0,qquad
E_Y(\{x\})=E_Y(\{u\})=\frac12,
\]

and therefore

\[
\widetilde\Lambda_Y=2q(1/2)=1+\frac2{\ln2}.
\]

Consequently

\[
\widetilde\Lambda_Y-\widetilde\Lambda_X=\frac1{\ln2}>0.
\]

The four Fourier supports give

\[
\operatorname{Inf}_x(f)=\operatorname{Inf}_y(f)=
\operatorname{Inf}_z(f)=\operatorname{Inf}_u(f)=\frac12,
\qquad I(f)=2.
\]

## 2. Positive variation and retained refunds

The path \(X,Y,X,Y,\ldots,X,Y\) with \(2r-1\) transitions has \(r\)
positive jumps and \(r-1\) negative jumps.  Hence

\[
V^+(f;\mathcal X_r)=\frac r{\ln2},
\]

while both \(I(f)=2\) and the distinct-union payment

\[
\sum_{v\in X\cup Y}\operatorname{Inf}_v(f)=\frac32
\]

are fixed.  No finite universal \(C\) can prove the candidate bound with
either payment made once.  The signed sum is instead

\[
\frac r{\ln2}-\frac{r-1}{\ln2}=\frac1{\ln2}.
\]

## 3. Reviewer strengthening: generic cycle lemma

Let \(P\) be any real-valued potential on states, and suppose both
transitions \(A\to B\) and \(B\to A\) are permitted.  If \(P(B)>P(A)\),
then the alternating walk with \(r\) copies of \(A\to B\) has positive
variation \(r(P(B)-P(A))\), while its signed variation is always
\(P(B)-P(A)\).  Therefore a bound on positive variation by a fixed
endpoint resource, uniformly over arbitrary walks, is possible only if
the potential is constant on every replayable communicating component
(or if revisits are otherwise bounded).

The B05 witness supplies the required nonconstant edge inside the allowed
overlap graph.  Thus the no-go is structurally stronger and simpler than a
rare-event asymptotic: arbitrary replay itself forces recharge.

## 4. Exact scope

The theorem refutes:

- arbitrary paths that may revisit the same physical blocks;
- a memoryless ledger that discards negative transitions;
- total influence or distinct-union influence paid once.

It does not refute:

- a fee paid with transition multiplicity (which already grows with depth);
- an acyclic physical reveal tree;
- persistent ownership that recognizes a previously visited packet;
- the signed aggregate \(\sum_i(B_i-\Gamma_i+K_i)\);
- universal GU or FEI.

The producer's wording is mathematically correct when “all coordinates
appearing” means the distinct union paid once.  This qualification should
remain explicit.  Two missing TeX backslashes in the producer files are
presentation-only.

The next proof target is not another nonnegative path estimate.  It is a
persistent whole-slice ownership theorem on an acyclic reveal tree, with
the retained negative transition identified with an actual
\(\Gamma_i-K_i\) credit and no repeated physical influence payment.

