# Round 450 annular cut energy implies restricted SAW operator mass

Round 450 connects the annular subset-energy obstruction to the earlier SAW
operator route.

For an exterior domain \(X_u=V\setminus B_{u-1}(x)\), write
\[
  C_{\ell}^{X_u}(y,z)
  =
  \#\{\eta:y\to z,\ \eta\subset X_u\ {\rm SAW},\ |\eta|=\ell\}.
\]
Then
\[
  C_{Q,\le L}^{X_u}
  =
  \sum_{\ell=0}^L Q^\ell C_\ell^{X_u}.
\]

If an annular cut \(U,V\subseteq S_{u-1}(x)\) has large energy
\[
  E=
  Q^2\langle \nu_U,C_{Q,\le L}^{X_u}\nu_V\rangle,
\]
then some length \(0\le\ell\le L\) satisfies
\[
  \langle \nu_U,C_\ell^{X_u}\nu_V\rangle
  \ge
  \frac{E}{Q^2(L+1)Q^\ell}.
\]
Consequently
\[
  \|C_\ell^{X_u}\|_{2\to2}
  \ge
  \frac{E}{Q^2(L+1)Q^\ell\|\nu_U\|_2\|\nu_V\|_2}.
\]
Since
\[
  \|\nu_U\|_2\le \Delta |U|^{1/2},
  \qquad
  \|\nu_V\|_2\le \Delta |V|^{1/2},
\]
large annular cut energy yields a lower bound
\[
  \|C_\ell^{X_u}\|_{2\to2}
  \gtrsim
  \frac{E}{(L+1)Q^{\ell+2}\Delta^2\sqrt{|U||V|}}.
\]

Thus failure of the annular cut estimate produces a restricted exterior
SAW-operator obstruction at some length scale.  This is more precise than the
raw degree obstruction: it identifies not merely many paths, but many paths
organized coherently enough to create \(L^2\) operator mass between boundary
vectors.

The next sufficient condition is therefore clear.  If one can prove a killed
SAW operator growth bound
\[
  \|C_\ell^{X_u}\|_{2\to2}\le C e^{o(\ell)} a^\ell
\]
uniformly in \(x,u\), with \(Qa<1\), then the annular cut energies are
summable in \(L\).  This is a localized exterior-domain version of the global
SAW operator-gap route.
