# Round 242

Round 242 splits same-sphere spread into return-generating spread and the
residual outward-through tangential spread.

For each level \(u\) with \(H_x(\gamma;\{u\})>0\), choose a level-\(u\)
tangential run.  Except for at most two endpoint levels, this run is
two-sided and has one of four adjacent-level types.  If many such levels have
type \((-1,+1)\), the path is counted by a new outward-through tangential
spread profile.

Otherwise, many levels have one of the other three types.  These types
produce exterior returns through level \(u\) or \(u+1\).  The map from
same-sphere levels to return levels has multiplicity at most two, and the
return levels lie in the current or next slab.  This gives the deterministic
bound
\[
  \mathfrak Z_{j,K}^{\rm spr}
  \le
  \mathfrak U_{j,K}^{\rm out}
  +
  \mathfrak X_{j,8K}^{\rm ret,spr}
  +
  \mathfrak X_{j+1,8K}^{\rm ret,spr}.
\]

The resulting ladder replaces same-sphere spread by outward-through spread
and spread-return profiles.  The current route to \(p_c(G)<p_{2\to2}(G)\)
depends on finite-defect bins, near-tail bins, a terminal far tail,
outward-through tangential spread, long tangential runs, spread exterior
returns, and ordinary exact-level exterior returns.
