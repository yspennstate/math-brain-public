# Round 293

Round 293 adds an exact-start escape to the existing prefix-record branch.

The new lemma is
```tex
\begin{lemma}[Exact-start chains with enough levels are record spread]
\label{lem:exact-start-chains-with-enough-levels-are-record-spread}
```
It observes that an exact-start chain of length \(\ell\) gives crossing runs
at \(\ell\) distinct consecutive slab levels.  If
\[
  \ell>\frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H ,
\]
then these levels already witness the prefix-record outward-spread profile.
In particular, once
\[
  K\ge \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H ,
\]
every exact-start chain of length at least \(5\) is absorbed by the existing
prefix-record profile.

The large-window consequence is
```tex
\begin{corollary}[Large-window exact starts are record spread except short children]
\label{cor:large-window-exact-starts-are-record-spread-except-short-children}
```
In the exact-start large-window branch, let
\[
  \mathcal S_r=\{h\in\{1,\ldots,B_r\}:\ell_r+h\le4\}.
\]
All children outside \(\mathcal S_r\) reduce to the prefix-record
outward-spread profile at parameter \(K_{r+1}\).  The exceptional set has at
most two increments and is empty when \(\ell_r\ge4\).  Thus the exact-start
branch is now reduced to:

- the already existing prefix-record outward-spread branch, with total
  coefficient at most \(5W_{\beta,p}^2\);
- at most two genuinely new exact-start children, of total length \(3\) or
  \(4\), with total coefficient at most \(10W_{\beta,p}\).

Both costs remain subexponential on the \(L_H\) scale.  This narrows the
large-window exact-start obstruction from all child lengths to only the very
short exact-start exceptions.
