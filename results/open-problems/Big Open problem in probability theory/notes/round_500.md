# Round 500 excess-weight calibration for the packet norm

The packet norm from Round 499 needs an excess weight.  This weight is not a
free parameter: its one-particle shadow must reproduce the fresh-column
obstruction from Round 490.

Write
\[
  s=\sqrt q,\qquad
  M_q=\max\{s+1,\sqrt{1+4s}\}.
\]
For a fresh outward tree step followed by a monotone vertical run in the new
column, the endpoint-\(L^2\)-normalized block inventory is
\[
  B_q(z,w)
  =
  szw\left(
    1+\frac{zw}{1-zw}+\frac{z/w}{1-z/w}
  \right).
\]
Here \(w\) marks annular excess.  The critical equations for this one-particle
kernel give the \(\sqrt{1+4s}\) rate.  Therefore, for every
\[
  z<M_q^{-1},
\]
there should be a positive excess multiplier \(w=w(z)\) such that
\[
  B_q(z,w)<1.
\]
When \(q=2,3\), this is the active constraint.  When \(q\ge4\), the
product-shuffle scale \(s+1\) is larger, so \(z<M_q^{-1}\) is already below
the fresh-column threshold.

This suggests the following packet-state weight.  In a cone rooted at tree
depth \(r\) outside a ball of radius \(u\), define
\[
  e_r(h)=r+|h|-u
\]
for each portal height \(h\).  For an ordered packet
\[
  \Pi=((a_1,b_1),\ldots,(a_k,b_k)),
\]
set
\[
  E_r(\Pi)=\sum_{j=1}^k \bigl(e_r(a_j)+e_r(b_j)\bigr).
\]
A first weighted Fock-type norm is therefore
\[
  \|E\|_{z,\xi,w,\Phi}
  =
  \sum_{k\ge0}\frac{\xi^k}{k!}
  \sup_{\Pi:|\Pi|=k}
  \frac{E_z(\Pi)}
       {w^{E_r(\Pi)}\Phi(\Pi)}.
\]
The factorial handles time-order shuffles.  The factor \(w^{E_r(\Pi)}\)
handles excess.  The remaining gap factor \(\Phi\) must encode the ordered
portal gaps and the hard-core vertical matching from Round 498.

The depth shift in the recursion is compatible with this norm.  Passing a
\(k\)-packet from a root cone to a child cone increases the excess of each of
its \(2k\) boundary ports by one, so \(E_r(\Pi)\) increases by \(2k\).  Thus
the recursive call contributes a deterministic per-atom factor \(w^{2}\),
which can be absorbed into the atom fugacity \(\xi\).  This is exactly the
kind of bookkeeping that the exponential-generating norm was designed to
preserve.

The remaining missing ingredient is now sharply localized: choose a gap
weight \(\Phi\) for ordered portal sets such that the root transform, with
the calibrated \(w(z)\), maps the weighted packet ball into itself for every
\(z<M_q^{-1}\).  Any successful choice must reduce to the inequality
\(B_q(z,w)<1\) on fresh one-particle blocks and to the \(s+1\) shuffle bound
on stack/product behavior.
