# A finite uniformization of rational symmetric walks

Let a probability measure \(\mu\) on a group \(G\) act on functions by
\[
 P_\mu f(x)=\sum_{g\in G}\mu(g)f(xg).
\]
Write \(H^\infty(G,\mu)\) for the vector space of bounded real-valued
\(\mu\)-harmonic functions. The walk is Liouville if this space consists of
constants.

## Theorem

Let \(G\ne\{e\}\) be a finitely generated group. Let \(\mu_1,\mu_2\) be
symmetric probability measures with finite support, rational atom weights,
and supports generating \(G\). There are an integer \(r\ge1\), the finite
group \(K=(\mathbb Z/2\mathbb Z)^r\), and two finite symmetric generating
sets \(S_1,S_2\subset G\times K\) such that:

1. Neither set contains the identity, neither has repeated elements, and
   \(|S_1|=|S_2|\).
2. Both sets contain \(\{e\}\times(K\setminus\{0\})\).
3. Pullback under \(\pi:G\times K\to G\) is an isometric linear bijection
   \[
   H^\infty(G,\mu_i)\ \longrightarrow\ H^\infty(G\times K,u_{S_i}),
   \qquad i=1,2,
   \]
   where \(u_{S_i}\) is the uniform probability measure on \(S_i\).

More explicitly, remove the holding mass from each measure, obtaining
\[
 \rho_i(g)=\begin{cases}
  \mu_i(g)/(1-\mu_i(e)),&g\ne e,\\
  0,&g=e.
 \end{cases}
\]
If \(D\) is any common positive denominator of the atom weights of both
\(\rho_i\), then the construction can be made with
\[
 2\le |K|\le2D,\qquad |S_i|=D+|K|-1<3D.
\]
The two projected walks have laws
\[
 \pi_*u_{S_i}=\alpha\rho_i+(1-\alpha)\delta_e,
 \qquad \alpha=\frac{D}{D+|K|-1}>\frac13.
\]

### Proof

Since \(G\ne\{e\}\) and each support generates \(G\), we have
\(\mu_i(e)<1\). Thus \(\rho_i\) is defined, symmetric, finitely supported,
rational-valued, and generating. For any function for which the sums exist,
\[
 P_{\mu_i}f=\mu_i(e)f+(1-\mu_i(e))P_{\rho_i}f.
\]
Consequently \(P_{\mu_i}f=f\) if and only if \(P_{\rho_i}f=f\).

For each \(g\ne e\) in the support of \(\rho_i\), put
\[
 a_i(g)=D\rho_i(g)\in\mathbb N.
\]
Then
\[
 a_i(g^{-1})=a_i(g),\qquad \sum_{g\ne e}a_i(g)=D.
\]
Let \(A\) be the maximum of these positive integers over both measures, and
let \(M\) be the least power of two at least \(\max\{2,A\}\). Since
\(1\le A\le D\), we have \(2\le M\le2A\le2D\): when \(A=1\),
\(M=2=2A\); when \(A\ge2\), the preceding power of two is less than \(A\),
so \(M<2A\).

Choose \(K=(\mathbb Z/2\mathbb Z)^r\) of order \(M\). Fix a listing
\(k_0=0,k_1,\ldots,k_{M-1}\) of its elements, and set
\[
 B_{i,g}=\{k_0,\ldots,k_{a_i(g)-1}\}.
\]
Define
\[
 S_i=\bigl(\{e\}\times(K\setminus\{0\})\bigr)
     \ \cup\!
     \bigcup_{g\in\operatorname{supp}\rho_i}
               \bigl(\{g\}\times B_{i,g}\bigr).
\]
These unions are disjoint. The vertical part has \(M-1\) elements and the
remaining parts have a total of \(D\) elements. Hence both sets have size
\(N=D+M-1<3D\).

No vertical element is the identity, and every element in another part has
first coordinate different from \(e\). Thus the identity is excluded.
Every \(k\in K\) satisfies \(-k=k\), so
\((g,k)^{-1}=(g^{-1},k)\). Equality
\(a_i(g^{-1})=a_i(g)\) implies \(B_{i,g^{-1}}=B_{i,g}\), proving symmetry.
This also covers elements \(g\) of order two.

Each \(B_{i,g}\) contains \(0\). Therefore \(S_i\) contains
\((g,0)\) for every \(g\in\operatorname{supp}\rho_i\), generating
\(G\times\{0\}\). The vertical elements generate \(\{e\}\times K\).
Together they generate the full direct product.

Counting elements above each \(g\) gives
\[
 (\pi_*u_{S_i})(e)=\frac{M-1}{N},\qquad
 (\pi_*u_{S_i})(g)=\frac{a_i(g)}{N}=\frac D N\rho_i(g)\quad(g\ne e).
\]
This is the claimed lazy law, with \(\alpha=D/N>1/3\). Its harmonic
functions are exactly those of \(\rho_i\), by the same algebra used to
remove the original holding mass.

It remains to show that every bounded \(u_{S_i}\)-harmonic function is
constant on each fiber of \(\pi\). Fix \(i\), write \(a(g)=a_i(g)\),
\(B_g=B_{i,g}\), and let \(F\) be such a function. Its harmonic equation is
\[
 N F(x,k)=\sum_{\ell\in K\setminus\{0\}}F(x,k+\ell)
       +\sum_g\sum_{b\in B_g}F(xg,k+b).                       \tag{1}
\]
Define the fiber average
\[
 \overline F(x)=\frac1M\sum_{k\in K}F(x,k).
\]
Averaging (1) over \(k\) and reindexing each translation of \(K\) gives
\[
 N\overline F(x)=(M-1)\overline F(x)
                       +\sum_g a(g)\overline F(xg).
\]
As \(N-(M-1)=D\), division by \(D\) proves that \(\overline F\) is
\(\rho_i\)-harmonic. Its pullback to \(G\times K\) is therefore
\(u_{S_i}\)-harmonic. Hence
\[
 U(x,k)=F(x,k)-\overline F(x)
\]
is bounded, harmonic, and satisfies \(\sum_{k\in K}U(x,k)=0\) for every
\(x\). In particular,
\[
 \sum_{\ell\ne0}U(x,k+\ell)=-U(x,k).
\]
Substitution in (1) gives
\[
 (D+M)U(x,k)=\sum_g\sum_{b\in B_g}U(xg,k+b).
\]
There are exactly \(D\) terms on the right. Taking absolute values and
then the supremum gives
\[
 (D+M)\|U\|_\infty\le D\|U\|_\infty.
\]
Boundedness and \(M>0\) force \(\|U\|_\infty=0\). Thus \(F\) is the
pullback of \(\overline F\), which is also \(\mu_i\)-harmonic.

Conversely, if \(f\) is bounded and \(\mu_i\)-harmonic, it is
\(\rho_i\)-harmonic, and the displayed projected law shows directly that
\(F(x,k)=f(x)\) satisfies (1). Pullback preserves the supremum norm and is
injective because \(\pi\) is onto. This proves the theorem. \(\square\)

## Consequence: an equivalent restricted formulation of T057

The following universal assertions are equivalent:

(A) For every finitely generated group, the Liouville status of simple
random walk is independent of its finite symmetric generating set.

(B) For every finitely generated group, all symmetric, finitely supported,
rational-valued probability measures whose supports generate the group
have the same Liouville status.

(C) Assertion (A) holds whenever the two generating sets have equal
cardinality and, for some decomposition \(H=G\times K\) with \(K\) a
nontrivial finite elementary abelian 2-group, both contain
\(\{e\}\times(K\setminus\{0\})\).

Indeed, (A) implies (C) by restriction. If (C) holds, apply the theorem to
any pair in (B), obtaining two sets on one group of exactly the form in
(C). The isomorphisms of harmonic-function spaces then imply (B).
Finally, (B) implies (A), since uniform measures on finite generating sets
are rational-valued. These implications treat nontrivial groups; the
trivial group has only constant functions and satisfies both assertions
directly. Allowing the identity in a generating set causes no change,
since adding or removing its positive holding mass preserves harmonic
functions.

Thus a rational-weight counterexample transfers explicitly to a
generating-set counterexample on a finite central extension, with equal
degrees. This is a universal reduction: it does not identify different
weighted walks with unweighted walks on the original fixed group. No
assertion concerning irrational weights follows from it.

## Central translation lemma

Let \(H\) be a countable group and \(\eta\) a probability measure whose
support generates \(H\) as a semigroup. If \(z\) is central in \(H\),
every bounded \(\eta\)-harmonic function satisfies \(f(xz)=f(x)\) for
every \(x\in H\).

### Proof

It suffices to consider a real-valued \(f\); real and imaginary parts
give the complex-valued statement. If \(z=e\), the conclusion is
immediate. Otherwise semigroup generation gives an integer \(m\ge1\)
with \(p=\eta^{*m}(z)>0\).

Let \(Y_j\) be independent increments with law \(\eta\), write
\(Z_0=e\), \(Z_n=Y_1\cdots Y_n\), and fix \(x\in H\). The random
variables \(M_n=f(xZ_n)\) form a martingale. To check this, condition on
\(Y_1,\ldots,Y_n\) and use
\(\sum_y\eta(y)f(xZ_ny)=f(xZ_n)\). They are bounded by
\(\|f\|_\infty\).

For \(b\ge a\), the martingale identity implies
\(\mathbb E[M_bM_a]=\mathbb E[M_a^2]\), so
\[
 \mathbb E[(M_b-M_a)^2]
   =\mathbb E[M_b^2]-\mathbb E[M_a^2].                       \tag{2}
\]
Thus \(\mathbb E[M_n^2]\) is nondecreasing and bounded above by
\(\|f\|_\infty^2\), hence convergent. Applying (2) with
\(a=n,b=n+m\) gives
\[
 \mathbb E[(M_{n+m}-M_n)^2]\longrightarrow0.
\]
Independence of the next \(m\) increments also gives
\[
 \mathbb E[(M_{n+m}-M_n)^2]
  =\mathbb E\!\left[
     \sum_y\eta^{*m}(y)(f(xZ_ny)-f(xZ_n))^2\right]
  \ge p\,\mathbb E[(f(xZ_nz)-f(xZ_n))^2].                   \tag{3}
\]
Put \(d_zf(w)=f(wz)-f(w)\). Centrality gives
\[
 \begin{aligned}
 P_\eta(d_zf)(w)
   &=\sum_y\eta(y)\bigl(f(wyz)-f(wy)\bigr)\\
   &=\sum_y\eta(y)\bigl(f(wzy)-f(wy)\bigr)\\
   &=f(wz)-f(w)=d_zf(w).
 \end{aligned}
\]
Consequently \(d_zf(x)=\mathbb E[d_zf(xZ_n)]\) for every \(n\).
Cauchy–Schwarz and (3) yield
\[
 |d_zf(x)|^2
 \le\mathbb E[|d_zf(xZ_n)|^2]
 \le p^{-1}\mathbb E[(M_{n+m}-M_n)^2]\longrightarrow0.
\]
Thus \(d_zf(x)=0\). \(\square\)

For the sets in the theorem, every \((e,k)\) is central and every
nonidentity such element occurs in \(S_i\). The lemma therefore also
proves that all bounded harmonic functions of each lifted walk descend
to \(G\). Counting the projected law then gives the same isomorphism
of harmonic-function spaces without using the averaging contraction.

## A cyclic version with degree \(D+2\)

Under the hypotheses of the theorem, with the same normalized measures
\(\rho_1,\rho_2\) and common denominator \(D\), there is a nontrivial
finite odd cyclic group \(C_M\) and two identity-free finite symmetric
generating sets \(T_1,T_2\subset G\times C_M\) such that
\[
 |T_1|=|T_2|=D+2,\qquad 3\le M\le D+2.
\]
Each contains \((e,1)\) and \((e,-1)\), and pullback under projection
again gives isometric linear bijections
\[
 H^\infty(G,\mu_i)\cong H^\infty(G\times C_M,u_{T_i}).
\]
The projected laws are
\[
 \pi_*u_{T_i}=\frac D{D+2}\rho_i+\frac2{D+2}\delta_e.
\]

### Proof

As above let \(a_i(g)=D\rho_i(g)\) and let \(A\) be the maximum integer
weight over both measures. Choose \(M\) to be the least odd integer at
least \(\max\{3,A\}\). If \(A=1\), then \(M=3=A+2\); if \(A=2\),
then \(M=3=A+1\); if \(A\ge3\), then \(M\) is \(A\) or \(A+1\).
Therefore \(3\le M\le A+2\le D+2\). Put \(q=(M-1)/2\) and write
\(C_M\) additively, with representatives
\(0,1,-1,\ldots,q,-q\).

For each \(i\), partition the support of \(\rho_i\) into its inverse
orbits. For an orbit \(\{g,g^{-1}\}\) of size two, choose one of its
elements \(g\), choose any subset \(B_{i,g}\subset C_M\) of size
\(a_i(g)\), and set \(B_{i,g^{-1}}=-B_{i,g}\). Such a subset exists
because \(a_i(g)\le A\le M\), and its negative has the required equal
size.

For an orbit \(\{g\}\) of size one, \(g\ne e\) is an involution.
Choose \(B_{i,g}\) as follows:
\[
 \begin{array}{ll}
 a_i(g)=2b:& B_{i,g}=\{1,-1,\ldots,b,-b\},\\[2pt]
 a_i(g)=2b+1:& B_{i,g}=\{0,1,-1,\ldots,b,-b\}.
 \end{array}
\]
The even case has \(b\le q\), since an even integer at most the odd
integer \(M\) is at most \(M-1\). The odd case also has \(b\le q\).
The listed residues are distinct, so these are symmetric subsets of
exactly the desired sizes. For \(b=0\), the second set is \(\{0\}\).

Now define
\[
 T_i=\{(e,1),(e,-1)\}
       \ \cup\!
       \bigcup_{g\in\operatorname{supp}\rho_i}
                 \bigl(\{g\}\times B_{i,g}\bigr).
\]
Since \(M\ge3\), the two vertical elements are distinct and nonidentity.
All other elements have nonidentity first coordinate, and the displayed
union is disjoint. Thus \(T_i\) is identity-free and has size
\(2+\sum_g a_i(g)=D+2\). In a direct product,
\((g,k)^{-1}=(g^{-1},-k)\). The choices of tag sets therefore make
\(T_i\) symmetric, including above involutions.

The element \((e,1)\) generates \(\{e\}\times C_M\). For every
\(g\in\operatorname{supp}\rho_i\), choose \(b\in B_{i,g}\), which is
possible since \(a_i(g)\ge1\). The subgroup generated by \(T_i\)
contains both \((g,b)\) and \((e,-b)\), hence their product \((g,0)\).
These elements generate \(G\times\{0\}\), proving generation of the
whole product. This argument does not assume that \(0\in B_{i,g}\).

The central translation lemma applies to this symmetric generating walk,
so every bounded harmonic function is invariant under \((e,1)\), and
therefore under the whole cyclic fiber. Direct counting gives the
displayed projected law. Removing its holding mass identifies its harmonic
functions with those of \(\rho_i\), hence of \(\mu_i\). Conversely any
bounded \(\mu_i\)-harmonic function pulls back to a harmonic function of
the lifted walk by this same projected-law calculation. Pullback is
injective, onto, and preserves the supremum norm. \(\square\)

Consequently T057 is also equivalent to its restriction to pairs of
equal-degree generating sets on products \(G\times C_M\), where \(M\ge3\)
is odd and both sets contain the two standard vertical generators. The
implications are the same as for (A)–(C): the restriction follows from
T057, the cyclic construction turns the restriction into (B), and (B)
implies T057 by taking uniform measures.
