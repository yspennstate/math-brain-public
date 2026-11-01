# Round 243

Round 243 splits the residual outward-through tangential spread from
Round 242 into record outward-through spread and return-generating
outward-through spread.

A level \(u\) is record outward-through if it has a \((-1,+1)\) tangential run
whose first time at level \(u\) is the start of that run.  If many
outward-through levels are not record levels, then each chosen run has an
earlier visit to level \(u\).  Since the run is entered from level \(u-1\),
the path must have crossed inward from \(u\) to \(u-1\) between the earlier
visit and the run.  The inward-token lemma then gives an exterior return
through level \(u\).

Thus
\[
  U^{\rm out}_{j,K}
  \le
  U^{\rm rec}_{j,2K}
  +X^{\rm ret,spr}_{j,2K}
  \le
  U^{\rm rec}_{j,2K}
  +X^{\rm ret,spr}_{j,8K}.
\]

Substitution into the Round 242 ladder gives the record-outward finite ladder:
\[
  \mathfrak Y_{\lambda_0}
  \preceq
  \mathfrak Y_{\lambda_N}
  +P^{\rm rec}
  +(2R^{\rm spr}_{j}+R^{\rm spr}_{j+1})
  +WT^{\rm long}
  +S^{\rm ret}
  +W\widehat X^{\rm ret}.
\]

The current route to \(p_c(G)<p_{2\to2}(G)\) depends on finite-defect bins,
near-tail bins, a terminal far tail, record outward-through spread, long
tangential runs, spread exterior returns, and ordinary exact-level exterior
returns.
