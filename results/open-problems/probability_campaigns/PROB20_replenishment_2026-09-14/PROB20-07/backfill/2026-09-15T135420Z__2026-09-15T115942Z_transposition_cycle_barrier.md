# PROB20-07 backfill — transposition-cycle barrier

**Original run provenance:** completed task response stamped `2026-09-15T115942Z` in the conversation history.

**Recovery status:** genuine authored mathematics recovered from the completed task response; it was not present in the bounded GitHub listing when this backfill was made. This file preserves that work without claiming a prior GitHub commit.

**Mathematical status at original run:** PARTIAL, self-reviewed; not independent/formal verification.

## Theorem recovered

Let `V` be a three-type quadratic stochastic operator with symmetric heredity tensor and

\[
P_{ij,k}\ge a\qquad\forall i,j,k.
\]

If `V` has a nontrivial period-two orbit `x,y` such that `y` is obtained from `x` by transposing two coordinate labels, then

\[
\boxed{a<\frac1{12}}.
\]

Thus no QSO with all coefficients at least `1/12` has a nontrivial coordinate-transposition two-cycle. The result is sharp because the exact lower-bound family from the earlier checkpoint has such cycles with minimum coefficient tending to `1/12` from below.

### Symmetrization

Treat the swap `S:(1,2,3)\mapsto(2,1,3)`. If an arbitrary QSO satisfies

\[
V(x)=Sx,\qquad V(Sx)=x,
\]

define `V^S(z)=S V(Sz)` and `\bar V=(V+V^S)/2`. The conjugate and average remain QSOs, preserve the same coefficient floor, preserve the same two-cycle, and `\bar V` is `S`-equivariant. Hence it suffices to treat the equivariant case.

### Equivariant parameterization

Write

\[
P_{11}=(p,q,r),\quad P_{22}=(q,p,r),\quad P_{12}=(s,s,1-2s),
\]

\[
P_{13}=(m,n,\ell),\quad P_{23}=(n,m,\ell),\quad P_{33}=(t,t,1-2t),
\]

with every displayed coordinate at least `a`, and

\[
p+q+r=1,\qquad m+n+\ell=1.
\]

Let

\[
x=(x_1,x_2,z),\qquad S_0=x_1+x_2=1-z,\qquad d=x_1-x_2\ne0.
\]

The second point is `(x_2,x_1,z)`.

### Antisymmetric equation

Direct expansion gives

\[
V_1(x)-V_2(x)=d\bigl((p-q)S_0+2(m-n)z\bigr).
\]

Since the output swaps the first two coordinates,

\[
(q-p)S_0+2(n-m)z=1.
\tag{A}
\]

Using

\[
q-p\le1-r-2a,\qquad n-m\le1-\ell-2a,
\]

(A) implies

\[
rS_0+2\ell z\le z-2a(1+z).
\]

But `r,\ell\ge a`, so

\[
a(1+z)\le rS_0+2\ell z.
\]

Therefore

\[
\boxed{a\le f(z):=\frac{z}{3(1+z)}}.
\tag{B}
\]

### Third-coordinate equation

The unchanged third coordinate satisfies

\[
z=r(x_1^2+x_2^2)+2(1-2s)x_1x_2+2\ell zS_0+(1-2t)z^2.
\]

Let

\[
A_1=x_1^2+x_2^2=\frac{S_0^2+d^2}{2},\qquad A_2=2x_1x_2=\frac{S_0^2-d^2}{2}.
\]

Since `s,t\ge a`,

\[
z\le rA_1+(1-2a)A_2+2\ell zS_0+(1-2a)z^2.
\tag{C}
\]

Write `R=r-a\ge0`, `L=\ell-a\ge0`. The previous inequality yields

\[
RS_0+2Lz\le z-3a(1+z).
\]

Since `A_1\le S_0^2`,

\[
RA_1+2LzS_0\le S_0\bigl(z-3a(1+z)\bigr).
\]

Substituting into (C), and using

\[
aA_1+(1-2a)A_2=\frac{(1-a)S_0^2+(3a-1)d^2}{2},
\]

we note from (B) that any possible case has `a<1/6<1/3`; since `d\ne0`, the `d^2` term is strictly negative. Dropping it strictly increases the right side, so after substituting `S_0=1-z` one obtains

\[
0<\frac{(1-z)^2-a\{3(1-z)^2+4\}}2.
\]

Hence

\[
\boxed{a<g(z):=\frac{(1-z)^2}{3(1-z)^2+4}}.
\tag{D}
\]

### Sharp endpoint optimization

On `0\le z<1`, `f` is strictly increasing and `g` strictly decreasing. Their difference factors as

\[
f(z)-g(z)=-\frac{(z-3)(3z-1)}{3(z+1)(3z^2-6z+7)}.
\]

Thus the unique intersection in `[0,1)` is `z=1/3`, and

\[
f(1/3)=g(1/3)=\frac1{12}.
\]

Because (D) is strict for a nontrivial cycle,

\[
\boxed{a<1/12}.
\]

## General midpoint identities also recovered

For an arbitrary two-cycle write

\[
x=M+d,\qquad y=M-d,\qquad d\ne0.
\]

If `B` is the symmetric bilinear form with `V(v)=B(v,v)`, then

\[
V(M+d)-V(M-d)=4B(M,d)=2DV(M)d.
\]

Since `V(x)-V(y)=y-x=-2d`, every two-cycle satisfies

\[
\boxed{DV(M)d=-d}.
\]

Averaging the cycle equations gives

\[
\boxed{M=V(M)+V(d)}.
\]

The transposition theorem solves this midpoint system when, after relabeling, one component of `d` vanishes. The all-three-components-nonzero case remained the next open obligation.
