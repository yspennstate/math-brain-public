# Round 244

Round 244 splits record outward-through spread into subterminal record spread
and return-generating terminal record spread.

For a rooted path \(\gamma=(v_0,\ldots,v_\ell)\), write
\[
  e_x(\gamma)=d(x,v_\ell).
\]
A record outward-through level is subterminal if \(u<e_x(\gamma)\).  If a
record outward-through level satisfies \(u\ge e_x(\gamma)\), then after the
chosen \((-1,+1)\) run exits to level \(u+1\), the path must later return to
level \(u\) before it can end.  The first such return is an inward
level-\(u+1\) token, hence gives \(\mathcal X_{u+1,0}\).

Thus
\[
  U^{\rm rec}_{j,K}
  \le
  U^{\rm sub}_{j,2K}
  +X^{\rm ret,spr}_{j,4K}
  +X^{\rm ret,spr}_{j+1,4K}.
\]
Applied with \(K=2M_i\), this exactly uses the existing
\(8M_i\)-threshold spread-return profiles.  The finite ladder becomes
\[
  \mathfrak Y_{\lambda_0}
  \preceq
  \mathfrak Y_{\lambda_N}
  +P^{\rm sub}
  +(3R^{\rm spr}_{j}+2R^{\rm spr}_{j+1})
  +WT^{\rm long}
  +S^{\rm ret}
  +W\widehat X^{\rm ret}.
\]

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, subterminal record outward-through
spread, long tangential runs, spread exterior returns, and ordinary exact-level
exterior returns.
