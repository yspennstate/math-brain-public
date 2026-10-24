# Reused overlap blocks recharge a memoryless nonnegative ledger

All logarithms are base two.  Define

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
\psi_k(t)=q(t)+t\log_2k,
\]

\[
E_X^f(S)=\sum_{A\subseteq X}\widehat f(S\cup A)^2,
\]

and the reviewed fixed-block potential

\[
\widetilde\Lambda_X(f)=
\psi_{|X|}(E_X^f(\varnothing))+
\sum_{i\notin X}q(E_X^f(\{i\})). \tag{1}
\]

For a block path \({\cal X}=(X_0,\ldots,X_d)\), put

\[
V^+(f;{\cal X})=
\sum_{t=0}^{d-1}
\left[\widetilde\Lambda_{X_{t+1}}(f)
-\widetilde\Lambda_{X_t}(f)\right]_+. \tag{2}
\]

The frozen candidate was the existence of an absolute \(C<\infty\) such
that

\[
V^+(f;{\cal X})\le CI(f) \tag{PV}
\]

for every genuine Boolean \(f\) and every finite path of two-coordinate
blocks satisfying \(|X_t\cap X_{t+1}|=1\).  This is the natural
memoryless assembly of per-swap nonnegative fees.  If the remaining node
terms obeyed \(G\le a_0I+bU\), \(b<1\), then (PV) would add only \(CI\)
and give \(G\le(a_0+C)I+bU\) on the corresponding reused-overlap class.

We prove that (PV) is false even in fixed dimension four.

## 1. A fixed Boolean sign

Let

\[
f(y,x,z,u)=
\begin{cases}
x,&y=+1,\\
zu,&y=-1.
\end{cases}
\]

Equivalently,

\[
f=\frac{x+xy+zu-yzu}{2}. \tag{3}
\]

Put \(X=\{y,x\}\) and \(Y=\{y,z\}\).  The four Fourier coefficients
in (3) have disjoint supports and square \(1/4\).  Consequently

\[
E_X(\varnothing)=\frac12,
\qquad E_X(\{i\})=0\quad(i\notin X),
\]

and

\[
\widetilde\Lambda_X(f)=\psi_2(1/2). \tag{4}
\]

For \(Y\),

\[
E_Y(\varnothing)=0,qquad
E_Y(\{x\})=E_Y(\{u\})=\frac12,
\]

so

\[
\widetilde\Lambda_Y(f)=2q(1/2). \tag{5}
\]

Since \(q(1/2)=1/2+1/\ln2\), (4)--(5) give the exact jump

\[
\boxed{
D:=\widetilde\Lambda_Y(f)-\widetilde\Lambda_X(f)
=\frac1{\ln2}>0.} \tag{6}
\]

Parseval gives

\[
\operatorname{Inf}_x(f)=\operatorname{Inf}_y(f)
=\operatorname{Inf}_z(f)=\operatorname{Inf}_u(f)=\frac12,
\qquad I(f)=2. \tag{7}
\]

## 2. Arbitrary depth with the same physical inputs

For \(r\ge1\), take the path with \(2r-1\) swaps

\[
X,Y,X,Y,\ldots,X,Y.
\]

There are exactly \(r\) positive \(X\to Y\) jumps and \(r-1\) negative
\(Y\to X\) refunds.  Therefore

\[
\boxed{V^+(f;{\cal X}_r)=\frac r{\ln2}.} \tag{8}
\]

The right side of (PV) is always \(2C\), while (8) diverges with \(r\).
Even replacing \(I(f)\) by the union-block charge gives only

\[
C\sum_{v\in X\cup Y}\operatorname{Inf}_v(f)=\frac{3C}{2},
\]

so that variant also fails.

This is not the previous large-majority asymptotic in new notation.  The
dimension, truth table, orbit energies, and every influence are fixed; only
the number of reused overlap transitions grows.

## 3. The signed replacement does not recharge

If the refunds are retained, the same path satisfies the exact telescope

\[
\sum_{t=0}^{2r-2}
\left(\widetilde\Lambda_{X_{t+1}}(f)
-\widetilde\Lambda_{X_t}(f)\right)
=\widetilde\Lambda_Y(f)-\widetilde\Lambda_X(f)
=\frac1{\ln2}, \tag{9}
\]

independent of depth.  Thus a viable changing-core argument must either:

1. retain the negative swap refunds until the endpoint; or
2. attach persistent ownership to the transported Fourier packet so a
   return to \(Y\) is not charged as a fresh first entry.

A memoryless nonnegative per-transition fee cannot be made
depth-independent, even by charging total influence once.

## 4. Exact scope and GU relation

The path deliberately reuses the same physical blocks.  It therefore
refutes arbitrary-depth memoryless assembly under coordinate reuse.  It
does not refute a globally chosen acyclic restriction tree, in which a
revealed coordinate never reappears, nor a persistent-state ledger, nor the
exact signed \(B_i-\Gamma_i+K_i\) identity.

The source-checked reduction remains: a universal

\[
M+(1+\eta)U\le cI,qquad0<\eta\le1,
\]

would imply

\[
G\le(c+2)I+(1-\eta)U
\]

and hence FEI with constant \(2+2(c+2)/\eta\).  The theorem only rules out
one nonnegative overlap-payment mechanism for proving that estimate.  GU
and full FEI remain open.

`CHECK_DEPTH_RECHARGE.py` reconstructs (3)--(9) using exact Fraction Walsh
arithmetic.  Floating values are printed only for readability; the proof
of \(D=1/\ln2>0\) is symbolic.

