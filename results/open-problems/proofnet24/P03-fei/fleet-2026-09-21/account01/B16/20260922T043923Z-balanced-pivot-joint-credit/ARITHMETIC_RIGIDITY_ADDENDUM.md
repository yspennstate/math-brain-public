# Addendum — exact Boolean equality in the balanced overlap relaxation is dyadically rigid

This addendum strengthens Section 4–5 of the accompanying report on the **uniform remaining cube**. The balanced-pivot scalar relaxation is not merely strict generically: a genuine Boolean pair cannot attain it at any nontrivial disagreement density other than \(1/2\).

## Theorem

Let \(f_0,f_1:Q_m\to\{\pm1\}\) under the uniform law, let
\[
\delta=\Pr[f_0\ne f_1],\qquad 0<\delta<1,
\]
and use the report's balanced-pivot notation
\[
T_S=(a_S^2+b_S^2)/2,\quad
c_S=2a_Sb_S/(a_S^2+b_S^2),\quad
X_S=|c_S|,
\]
with \(\rho=1-2\delta=\sum_ST_Sc_S\). Then
\[
\mathbb E_T\Phi(X)\ge\Phi(|\rho|).
\]
If equality holds, necessarily
\[
\boxed{\delta=1/2.}
\]
Consequently, for every genuine Boolean pair on a uniform finite cube with
\[
0<\delta<1,\qquad \delta\ne1/2,
\]
the scalar overlap relaxation is **strict**:
\[
\boxed{\mathbb E_T\Phi(X)>\Phi(|1-2\delta|).}
\]
The endpoints \(\delta=0,1\) are the trivial pairs \(f_1=\pm f_0\).

## Proof

Equality in the strong-convex/triangle reduction forces
\[
c_S=\rho
\tag{1}
\]
for every spectral atom with \(T_S>0\). (When \(\rho=0\), equality forces \(X=0\) almost surely, which is again (1).)

Set
\[
g=(f_0+f_1)/2,\qquad d=(f_0-f_1)/2.
\]
Then \(g,d\in\{-1,0,1\}\), their physical supports are disjoint, and
\[
|\operatorname{supp}d|=k,\qquad
|\operatorname{supp}g|=N-k,
\qquad N=2^m,\qquad \delta=k/N.
\]
Writing \(G_S=\widehat g(S)\), \(D_S=\widehat d(S)\), we have
\[
a_S=G_S+D_S,\qquad b_S=G_S-D_S,
\]
so
\[
c_S=\frac{G_S^2-D_S^2}{G_S^2+D_S^2}.
\]
Substitute (1) and \(\rho=(N-2k)/N\). For every active spectral atom,
\[
\frac{G_S^2-D_S^2}{G_S^2+D_S^2}=\frac{N-2k}{N},
\]
hence
\[
\boxed{kG_S^2=(N-k)D_S^2.}
\tag{2}
\]

Under the uniform cube, \(NG_S\) and \(ND_S\) are integers: they are signed Walsh sums of the ternary functions \(g,d\). Since the pair is nontrivial, some active atom exists; (2) then implies
\[
\frac{N-k}{k}=\left(\frac{A}{B}\right)^2
\tag{3}
\]
for nonzero integers \(A,B\). Thus \((N-k)/k\) is a rational square.

Write \(A/B=a/b\) in lowest terms. Equation (3) implies
\[
N-k=s a^2,\qquad k=s b^2
\]
for some positive integer \(s\), so
\[
N=s(a^2+b^2).
\tag{4}
\]
Because \(N=2^m\), the coprime positive integer sum \(a^2+b^2\) divides a power of two and is itself a power of two. If one of \(a,b\) were even and the other odd, \(a^2+b^2\) would be an odd integer bigger than one, impossible. Hence both are odd. Then
\[
a^2+b^2\equiv2\pmod4,
\]
so the only possible power of two is \(2\). Therefore
\[
a=b=1.
\]
Equation (3) gives \(N-k=k\), i.e.
\[
k=N/2,\qquad \delta=1/2.
\]
This proves the theorem.

## Consequences for the live gate target

1. The two-angle scalar extremizer from the report is genuinely **non-Boolean** at every dyadic disagreement density except \(1/2\). So its sharpness is a sharpness statement for the scalar relaxation, not a hidden Boolean counterexample.
2. Every one-point, two-point, or more general sparse-defect restriction pair with \(0<k<N/2\) receives a strictly positive Booleanity credit beyond the scalar envelope. This applies before any candidate-potential estimate.
3. The remaining problem is quantitative: the theorem gives strictness but not yet a dimension-independent lower bound on that extra credit. Near-square rational ratios can in principle make the arithmetic separation small as dimension grows, so no uniform estimate is claimed.

This is an exact source-valid use of Booleanity, rather than an arbitrary spectral-law relaxation. Full FEI remains open.
