# Round 043 log

## Goal

Rule out a tempting spectral shortcut: applying nonamenability or Kesten's
theorem directly to the normalized two-point kernel.

## Observation

On a nonamenable Cayley graph, symmetry and adaptation of a probability kernel
do not force finite-set escape with a useful uniform bound.  Take
\(\Gamma=F_2\times\mathbb Z\), let \(a,b\) generate \(F_2\), and let \(t\)
generate \(\mathbb Z\).  For \(L\ge1\), let \(u_L\) be uniform on
\(\{t^j:|j|\le L\}\), let \(\nu\) be uniform on
\(\{a,a^{-1},b,b^{-1},t,t^{-1}\}\), and set
\[
  \mu=(1-\eta)u_L+\eta\nu .
\]
For every \(\eta>0\), this is a finitely supported symmetric generating
probability measure on the nonamenable group \(\Gamma\).  But if
\[
  K_M=\{t^j:|j|\le M\},
\]
then
\[
  \frac1{|K_M|}\sum_{x,y\in K_M}\mu(x^{-1}y)
  \ge
  (1-\eta)\frac{2(M-L)+1}{2M+1}.
\]
Choosing \(\eta\) small and \(M/L\) large makes this as close to \(1\) as
desired.

## Consequence

Any proof of finite-set escape for the percolation kernel
\[
  Q_p(x,y)=\tau_p(x,y)/\bar\chi_p
\]
must use the fact that \(Q_p\) is a near-critical two-point kernel.  It cannot
be a kernel-only consequence of:

- symmetry,
- finite support or approximability by finite support,
- support generating the graph,
- row-sum normalization,
- nonamenability of the ambient graph, or
- a spectral gap for a fixed simple random walk.

This also clarifies the role of the Hutchcroft--Pan product theorem.  In
\(T\times H\), the normalized mass could a priori hide in the amenable
\(H\)-direction.  Their backscattering and nonunimodular Hammersley--Welsh
arguments are precisely the extra percolation-specific input that prevents
this hiding below \(p_u\).
