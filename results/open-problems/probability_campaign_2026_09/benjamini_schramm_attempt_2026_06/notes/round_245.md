# Round 245

Round 245 splits subterminal record outward-through spread into persistent
subterminal record spread and return-generating nonpersistent subterminal
record spread.

Let
\[
  \tau_x^{\rm end}(\gamma)=\min\{t:d(x,v_t)=e_x(\gamma)\}.
\]
A subterminal record level \(u\) is persistent if, after its record
\((-1,+1)\) run exits to level \(u+1\), the path stays outside \(B_u(x)\)
until the first hit of the endpoint sphere.  If not, the first return to
level \(u\) is an inward level-\(u+1\) token and hence gives
\(\mathcal X_{u+1,0}\).

Thus
\[
  U^{\rm sub}_{j,K}
  \le
  U^{\rm per}_{j,2K}
  +X^{\rm ret,spr}_{j,4K}
  +X^{\rm ret,spr}_{j+1,4K}.
\]
Applied with \(K=4M_i\), this introduces a looser spread-return threshold
\(16M_i\).  The finite ladder becomes
\[
  \mathfrak Y_{\lambda_0}
  \preceq
  \mathfrak Y_{\lambda_N}
  +P^{\rm per}
  +(4R^{\rm spr,+}_{j}+3R^{\rm spr,+}_{j+1})
  +WT^{\rm long}
  +S^{\rm ret}
  +W\widehat X^{\rm ret}.
\]

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, persistent subterminal record
outward-through spread, long tangential runs, spread exterior returns, and
ordinary exact-level exterior returns.
