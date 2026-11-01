# Parity-balanced activation towers: an all-depth retained-`U` theorem

## Statement

For a Boolean function (P:\{-1,1\}^n\to\{-1,1\}), introduce a fresh sign
(w_0) and put
[
Q_0(w_0,x)=w_0P(x).
]
For a balanced Boolean (q), let its half-activation on a fresh selector (z)
be
[
A_z(q)(z,x)=
\begin{cases}
1,&z=+1,\\
q(x),&z=-1.
\end{cases}
]
For (k=1,ldots,d), put (F_k=A_{z_k}(Q_{k-1})), and, when (k<d),
put (Q_k=w_kF_k) using a fresh sign (w_k).  Define
(T_d(P)=F_d).

Let (p_f(S)=\widehat f(S)^2),
(pi_f(S)=\sum_{R\supseteq S}p_f(R)), and
[
U(f)=\sum_S p_f(S)\log_2\frac{pi_f(S)}{p_f(S)}.
]
Then, for every Boolean (P) and every (d\geq1),
[
U(T_d(P))=2+2^{-d}(U(P)-2),qquad
I(T_d(P))=2+2^{-d}(I(P)-2).                 	ag{1}
]
Consequently, if (U(P)\leq2I(P)), then (U(T_d(P))\leq2I(T_d(P))).
For every finite adaptive, possibly pruned restriction tree querying only
physical variables of (T_d(P)), with leaves (ell) of probabilities
(lambda_ell), and every common Boolean terminal core (h) on disjoint
variables,
[
U(T_d(P)h)-\sum_elllambda_ell U((T_d(P)|_ell)h)
\leq 2I(T_d(P)).                            	ag{2}
]
The constant is independent of (n,d), the dyadic terminal activation
probability (2^{-d}), the tree order and pruning, and (h).

## 1. Character balancing

If (w) is fresh, the Fourier support of (wf) is obtained from that of
(f) by adjoining (w) to every set.  Both squared coefficients and all
upper-set masses are preserved under this bijection.  Hence
[
U(wf)=U(f),qquad I(wf)=I(f)+1.              	ag{3}
]
In particular, (wf) is balanced.

## 2. Exact half-activation calculation

Let (q) be balanced.  Write (p(S)=\widehat q(S)^2) and
(pi(S)=\sum_{R\supseteq S}p(R)).  Since (widehat q(\varnothing)=0),
the spectrum of (A=A_z(q)) has mass (1/4) at each of
(\varnothing) and ({z}); for each nonempty (S), it has mass
(p(S)/4) at each of (S) and (S\cup\{z\}).

The corresponding upper-set masses are (1), (1/2),
(pi(S)/2), and (pi(S)/4), respectively.  Thus the first two atoms
contribute (1/2+1/4), while the two copies of a nonempty (S) contribute
[
\frac{p(S)}4\log_2\frac{2pi(S)}{p(S)}
+\frac{p(S)}4\log_2\frac{pi(S)}{p(S)}.
]
Because (sum_{S\ne\varnothing}p(S)=1), summation gives
[
U(A_z(q))=1+\frac12U(q).                    	ag{4}
]
The selector is pivotal exactly on the (q=-1) half of the cube, and every
old coordinate is active only on the (z=-1) half.  Therefore
[
I(A_z(q))=\frac12+\frac12I(q).             	ag{5}
]

## 3. Solving the tower

Equations (3)--(5) give, for every intermediate level,
[
U(Q_k)=1+\frac12U(Q_{k-1}),qquad
I(Q_k)=\frac32+\frac12I(Q_{k-1}),
]
whereas the last, unbalanced activation obeys (4)--(5) without the following
character.  With (U(Q_0)=U(P)) and (I(Q_0)=I(P)+1), solving these affine
recurrences proves (1).

Subtracting twice the influence identity from the `U` identity yields the
particularly transparent preservation law
[
U(T_d(P))-2I(T_d(P))
=2^{-d}\bigl(U(P)-2I(P)\bigr)-2(1-2^{-d})\leq0
]
whenever (U(P)\leq2I(P)).

## 4. Complete signed tree payment

For any finite restriction tree, the complete node charges
[
Delta_iU=U(g)-\mathbb E_{x_i}U(g|x_i)
=B_i-\Gamma_i+KL_i
]
sum exactly, by conditional expectation, to
[
U(T_d(P))-\sum_elllambda_ell U(T_d(P)|_ell).
]
No term is discarded and no node is charged separately.  Since (U\geq0),
this is at most (U(T_d(P))\leq2I(T_d(P))).

If a common (h) uses disjoint variables, Fourier tensorization gives
(U(gh)=U(g)+U(h)).  Hence (U(h)) occurs once at the root and with total
weight (sum_elllambda_ell=1) at the leaves, so it cancels exactly.
This proves (2).

## 5. Rare-event and single-use interpretation

The original core (P) is reached only when
(z_1=\cdots=z_d=-1), an event of probability (2^{-d}), and is then
multiplied by the fresh character (w_0\cdots w_{d-1}).  Each subsequent
balancer moves the preceding spectrum behind a new physical coordinate
before the next activation.  Thus the retained entropy credit is used once:
the full signed charge telescopes to root `U`, while terminal `U` is
retained rather than locally discarded.

## 6. Dense-nullity-two corollary and exact boundary

The earlier B05 dense-nullity-two shield theorem proves (U(P)\leq2I(P))
for
[
P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y),qquad
\operatorname{rank}(M)=m-2,
]
with arbitrary Boolean (D).  Therefore (1)--(2) apply to arbitrary-depth
parity-balanced towers over every such shield.  This changes the coherent
core at every level and strictly extends the fixed-shield tree class.

The proof does **not** cover biased selectors, omission of the fresh
balancing characters, reuse of selector variables, trees querying the
terminal core, or arbitrary changing coherent cores.  In particular it does
not establish a universal aggregate upper-set payment and does not prove
full FEI.

