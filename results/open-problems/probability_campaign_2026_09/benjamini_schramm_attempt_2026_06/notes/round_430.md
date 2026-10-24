# Round 430 chain-disjoint profile reduction

Round 430 packages the Round 429 dichotomy as a property-restricted profile
reduction.

For \(a\ge2\), define \(\mathcal X^{\rm chain}_{j,K,a,p}(x,\gamma)\) to be
the property that there are return levels
\[
  u_1<u_2<\cdots<u_a,\qquad u_k\in A_{j,p}\cap\mathbb N,
\]
and exterior-return intervals \(I_k=[s_k,t_k]\) through \(u_k\), such that
\[
  I_a\subset I_{a-1}\subset\cdots\subset I_1.
\]
Define \(\mathcal X^{\rm disj}_{j,K,a,p}(x,\gamma)\) to be the property that
there are at least
\[
  M_{j,K,a,p}
  =
  \left\lceil
    \frac{1}{a-1}
    \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
  \right\rceil
\]
pairwise time-disjoint exterior-return intervals through levels in
\(A_{j,p}\cap\mathbb N\).

Let
\[
  \mathfrak X^{\rm chain}_{Q,\lambda,\sigma,\beta,j,K,a}
\]
and
\[
  \mathfrak X^{\rm disj}_{Q,\lambda,\sigma,\beta,j,K,a}
\]
denote the same property-restricted radial profiles as
\(\mathfrak X^{\rm rad,ret,spr}_{Q,\lambda,\sigma,\beta,j,K}\), with
\(\mathcal X^{\rm spr}_{j,K,p}\) replaced by the corresponding chain or
disjoint property.

Then, for every \(a\ge2\),
\[
  \mathfrak X^{G\to H,{\rm rad,ret,spr}}_{Q,\lambda,\sigma,\beta,j,K}(s,p)
  \le
  \mathfrak X^{\rm chain}_{Q,\lambda,\sigma,\beta,j,K,a}(s,p)
  +
  \mathfrak X^{\rm disj}_{Q,\lambda,\sigma,\beta,j,K,a}(s,p).
\]
This follows directly from the property inclusion
\[
  \mathcal X^{\rm spr}_{j,K,p}
  \subseteq
  \mathcal X^{\rm chain}_{j,K,a,p}
  \cup
  \mathcal X^{\rm disj}_{j,K,a,p}
\]
and the union bound inside the defining radial profile.

This reduction is deterministic and introduces no coefficient depending on
\(p\).  Its value is not an immediate exponent improvement; it creates two
structured targets:

* a nested-chain profile, where one must exploit radial nesting;
* a disjoint-excursion profile, where one can try to use factorization or
  BK/Reimer-type separation over time-disjoint intervals.
