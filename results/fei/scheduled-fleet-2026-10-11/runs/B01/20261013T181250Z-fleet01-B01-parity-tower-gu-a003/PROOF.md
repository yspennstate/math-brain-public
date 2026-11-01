# Exact GU transfer through parity-balanced activation towers

All logarithms are base two.  For a Boolean sign (f), write
[
U(f)=\sum_S\widehat f(S)^2
\log_2\frac{\sum_{R\supseteq S}\widehat f(R)^2}
{\widehat f(S)^2},
\qquad
G(f)=\sum_i\left(U(f)-\mathbb E_{x_i}U(f|x_i)\right).
]

## 1. Tower and statement

For an arbitrary Boolean base (P), put (Q_0(w_0,x)=w_0P(x)).  If (q)
is balanced, define
[
A_z(q)(z,x)=
\begin{cases}
1,&z=+1,\\
q(x),&z=-1.
\end{cases}
]
Recursively set (F_k=A_{z_k}(Q_{k-1})), and, for (k<d),
(Q_k=w_kF_k), with every (z_k,w_k) fresh.  Let (T_d(P)=F_d).

Define the even continuous scalar
[
\begin{aligned}
\phi(\mu)
={}&\frac34+\frac{\mu^2}{4}
+\frac{\mu^2}{2}\log_2\frac1{\mu^2}\\
&-\frac32\left[
\frac{(1+\mu)^2}{4}\log_2\frac{2}{1+\mu}
+\frac{(1-\mu)^2}{4}\log_2\frac{2}{1-\mu}
\right],
\end{aligned}                                                    \tag{1}
]
with zero times a divergent logarithm interpreted as zero.  Then
[
\boxed{
G(T_d(P))
=2^{-d}G(P)+2^{-(d-1)}(1+\phi(\mathbb EP))
+2(1-2^{-(d-1)})(1+\phi(1/2)).
}                                                                  \tag{2}
]

Moreover,
[
\phi(1/2)=\frac78-\frac{27}{32}\log_2\frac43,
\]
and, with
[
K_*=2(1+\phi(1/2))
=\frac{15}{4}-\frac{27}{16}\log_2\frac43
=3.049624219966\ldots,                                            \tag{3}
]
the exact formula implies
[
G(T_d(P))\le2^{-d}G(P)+K_*.                                       \tag{4}
]

Consequently, for any (a\ge0) and (0\le b<1),
[
G(P)\le aI(P)+bU(P)
\quad\Longrightarrow\quad
\boxed{G(T_d(P))\le(a+K_*)I(T_d(P))+bU(T_d(P))}                   \tag{5}
]
for every (d\ge1).  The contraction coefficient (b) is preserved
exactly and the loss in (a) is independent of dimension and depth.

## 2. Character balancing preserves (G)

For a fresh sign (w), character multiplication shifts every Fourier set
by adjoining (w).  Therefore (U(wf)=U(f)).  Restrictions of any old
coordinate give the same (U)-differences as for (f), while restricting
(w) gives (f) or (-f), which have equal (U).  Hence
[
G(wf)=G(f),qquad I(wf)=I(f)+1.                                   \tag{6}
]

## 3. Exact scalar balancer charge

Let (mu=\mathbb Ef) and let (A(f)) denote the half-activation of
(f), without assuming (f) balanced.  Put
(u(\mu)=\mu^2\log_2(1/\mu^2)), and
[
E(\mu)=
\frac{(1+\mu)^2}{4}\log_2\frac{4}{(1+\mu)^2}
+\frac{(1-\mu)^2}{4}\log_2\frac{2}{1-\mu}.
]
A direct cap calculation gives
[
U(A(f))
=E(\mu)+\frac12\bigl(U(f)-u(\mu)\bigr)
+\frac14(1-\mu^2).                                               \tag{7}
]

Now activate (wf).  The selector contributes exactly one to (G).
Every original coordinate contributes half its charge for (f).  The
balancer (w) has children (A(f)) and (A(-f)), so (7) yields exactly
[
U(A(wf))-\frac{U(A(f))+U(A(-f))}{2}=\phi(\mu).
]
Thus
[
\boxed{G(A(wf))=\frac12G(f)+1+\phi(\mathbb Ef).}                \tag{8}
]
This is stronger on this structured input than paying the balancer charge
by the full influence of (f).

## 4. Solving the hierarchy

Each (Q_k) is balanced, and every (F_k=A(Q_{k-1})) has mean (1/2).
The first step of (8) therefore uses (phi(\math EP)); all subsequent
steps use the same scalar (phi(1/2)):
[
G(F_1)=\frac12G(P)+1+\phi(\math EP),qquad
G(F_k)=\frac12G(F_{k-1})+1+\phi(1/2)quad(k\ge2).
]
Solving this recurrence proves (2).

From (1), the negative bracket may be discarded and
[
\phi(\mu)\le1+\frac1{2e\ln2}.
]
Hence the non-seed part of (2) is a convex combination of
(1+\phi(\math EP)\le2+1/(2e\ln2)) and
(2(1+\phi(1/2))=K_*).  Since (e>2), (ln2>1/2), and
(log_2(4/3)<1/2), the latter is larger.  This proves (4).

## 5. GU' and FEI bookkeeping

For every balanced (q), the same cap calculation gives
(U(A(q))=1+U(q)/2), while direct pivotal counting gives
(I(A(q))=1/2+I(q)/2).  Combining these with
(U(wf)=U(f)) and (I(wf)=I(f)+1), then solving the affine recurrences,
gives
[
U(T_d(P))=2+2^{-d}(U(P)-2),qquad
I(T_d(P))=2+2^{-d}(I(P)-2).                                      \tag{9}
]
Let (arepsilon=2^{-d}).  Applying the base GU' bound in (4) and then
(9),
[
\begin{aligned}
G(T_d(P))
&\le a\varepsilon I(P)+b\varepsilon U(P)+K_*\\
&=a[I(T_d)-2(1-\varepsilon)]
 +b[U(T_d)-2(1-\varepsilon)]+K_*\\
&\le aI(T_d)+bU(T_d)+K_*.
\end{aligned}
]
Since (I(T_d)\ge2(1-2^{-d})\ge1), (5) follows.

If the base also satisfies (U(P)\le cI(P)) for (c\ge1), (9) gives
(U(T_d(P))\le cI(T_d(P))).  The standard implication
[
H(f)\le2I(f)+2U(f)
]
then yields (H(T_d(P))\le(2+2c)I(T_d(P))).

## 6. Scope

This proves a depth-uniform closure theorem for a growing hierarchy with
fresh fair selectors and fresh parity balancers.  It does not cover biased
selectors, imperfect balancing, shared variables, or arbitrary coherent
core changes.  As the independent B19 review observed, the positive-depth
tower family is not itself restriction-closed under arbitrary physical
restrictions.  Therefore (5) is a proper-class GU' transfer, not the
universal GU' inequality and not full FEI.

