# HARD8-06 — relative-discriminant index-square addendum

This append-only mathematical addendum strengthens Theorem 7.1 of `2026-09-16T09-40-33Z__report.md`.

Let
\[
Q(x)=x^D R(x+x^{-1})
\]
be a monic irreducible noncyclotomic reciprocal polynomial, let \(\alpha\) be a root, \(\beta=\alpha+\alpha^{-1}\), and put
\[
L=\mathbf Q(\alpha),\qquad F=\mathbf Q(\beta).
\]
Write
\[
I_L=[\mathcal O_L:\mathbf Z[\alpha]],\qquad
I_F=[\mathcal O_F:\mathbf Z[\beta]],
\]
and let \(\mathfrak D_{L/F}\) be the relative field discriminant ideal.

## Theorem — exact endpoint / relative-discriminant square quotient

One has
\[
\boxed{
N_{F/\mathbf Q}(\mathfrak D_{L/F})\, I_L^2
=
|Q(1)Q(-1)|\, I_F^4.
}
\tag{A.1}
\]
Consequently
\[
\boxed{
\frac{|Q(1)Q(-1)|}{N_{F/\mathbf Q}(\mathfrak D_{L/F})}
=
\left(\frac{I_L}{I_F^2}\right)^2
}
\tag{A.2}
\]
is not merely a positive integer but a **perfect square integer**. In particular,
\[
\boxed{I_F^2\mid I_L}
\tag{A.3}
\]
and for every rational prime \(p\),
\[
\boxed{
v_p(|Q(1)Q(-1)|)
\equiv
v_p(N_{F/\mathbf Q}\mathfrak D_{L/F})
\pmod 2.
}
\tag{A.4}
\]

### Proof

Let \(d_L,d_F\) be the absolute field discriminants. The polynomial/field discriminant relations are
\[
|\operatorname{Disc}Q|=|d_L|I_L^2,
\qquad
|\operatorname{Disc}R|=|d_F|I_F^2.
\tag{A.5}
\]
The tower discriminant formula for the quadratic extension \(L/F\) gives
\[
|d_L|
=
|d_F|^2 N_{F/\mathbf Q}(\mathfrak D_{L/F}).
\tag{A.6}
\]
The archived reciprocal trace identity gives
\[
|\operatorname{Disc}Q|
=
|Q(1)Q(-1)|\,|\operatorname{Disc}R|^2.
\tag{A.7}
\]
Substitute (A.5) and (A.6) into (A.7):
\[
|d_F|^2N(\mathfrak D_{L/F})I_L^2
=
|Q(1)Q(-1)|\,|d_F|^2I_F^4.
\]
Cancel \(|d_F|^2\), obtaining (A.1).

The earlier relative-order argument proves
\[
\mathfrak D_{L/F}\mid(\beta^2-4),
\]
so
\[
N(\mathfrak D_{L/F})\mid |Q(1)Q(-1)|.
\]
Therefore the left side of (A.2) is a positive integer. But (A.1) says it is the square of the rational number \(I_L/I_F^2\). A rational square which is an integer is an integer square: if \(a/b\) is reduced and \(b^2\mid a^2\), then \(b=1\). This proves (A.2)–(A.3), and taking p-adic valuations gives (A.4). ∎

## Consequences

1. **Endpoint-unit case.** If \(|Q(1)Q(-1)|=1\), then
   \[
   N(\mathfrak D_{L/F})=1,
   \qquad
   I_L=I_F^2.
   \]
   Thus the quadratic extension is unramified at every finite prime and the two monogenic indices are locked exactly.

2. **Square-class rigidity.** The endpoint product and the relative discriminant norm have the same square class in \(\mathbf Z_{>0}\). This is stronger than the support statement from the main report.

3. **Exact example with nontrivial index quotient.** For
   \[
   R(y)=y^2-4y-4,
   \]
   one has
   \[
   Q(x)=x^4-4x^3-2x^2-4x+1.
   \]
   Exact integral-basis computation gives
   \[
   d_F=8,\quad d_L=-1024,\quad I_F=2,\quad I_L=8,
   \]
   while
   \[
   |Q(1)Q(-1)|=64,
   \qquad
   N(\mathfrak D_{L/F})=16.
   \]
   Hence
   \[
   \frac{64}{16}=4
   =\left(\frac8{2^2}\right)^2,
   \]
   exactly as (A.2) predicts.

This identity is proved here as a campaign result. It may be an immediate consequence of standard discriminant/index formalism in the literature; no novelty claim is made without a dedicated literature comparison.