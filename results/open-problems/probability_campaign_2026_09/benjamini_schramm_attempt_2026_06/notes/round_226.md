# Round 226

Round 226 localizes the shifted far-tail obstruction.

For a rooted path \(\gamma\), define its maximum radius
\[
  M_x(\gamma)=\max_t d(x,v_t)
\]
and the defect contribution inside a radial interval \(A\):
\[
  D_x(\gamma;A)
  =
  \sum_{u\in A}
  \left(
    2\#\{t:d(x,v_{t-1})=u,\ d(x,v_t)=u-1\}
    +
    \#\{t:d(x,v_{t-1})=u,\ d(x,v_t)=u\}
  \right).
\]
The sum of these contributions over all radial levels is \(2I_x+H_x\).

For the far tail \(d>\lambda L_H\), fix an overshoot allowance
\(\sigma L_H\) and a slab width \(\beta L_H\).  A path is either an overshoot:
\[
  M_x(\gamma)>r+\sigma L_H,
\]
or all its visited radial levels lie in a bounded number
\[
  J_{\sigma,\beta}=O_{\sigma,\beta,\alpha_\omega,s}(1)
\]
of slabs.  In the second case, since the total defect is \(>\lambda L_H\),
one slab has defect contribution at least
\[
  \frac{\lambda}{J_{\sigma,\beta}}L_H.
\]

Thus the far-tail profile \(\mathfrak Y\) is bounded by an overshoot profile
\(\mathfrak O\) plus finitely many heavy-slab profiles \(\mathfrak V_j\).
This turns the remaining far-tail estimate into a dichotomy: control radial
overshoot, or control concentrated non-outward motion in a fixed logarithmic
annulus.
