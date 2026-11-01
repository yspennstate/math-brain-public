# Round 239

Round 239 absorbs the adjacent-crossing profiles into exterior-return
profiles.

For a level-\(u\) crossing run of type \((\eta,\zeta)\), any exit with
\(\zeta=-1\) gives an inward level-\(u\) token.  Thus the crossing types
\[
  (-1,-1),\qquad (+1,-1)
\]
force same-level exterior returns.  The type \((-1,+1)\) is outward through
the run, but two consecutive such runs require the path to come back from
level \(u+1\) to level \(u-1\), so \(q\) such runs force at least \(q-1\)
same-level inward tokens.  Therefore, for \(R\ge1\) and \(K=R-1\), all three
types except \((+1,+1)\) are bounded by the same exact-level return profile
\(\mathfrak X_{j,K}^{\rm ret}\).

The remaining type \((+1,+1)\) begins with an inward level-\(u+1\) token, so
it is bounded by an upper-shifted exterior-return profile
\(\mathfrak X_{j,K}^{\rm ret,up}\).

The new return-absorbed ladder replaces the four adjacent-crossing profile
families by
\[
  3\mathfrak X_{j,K_i^\times}^{\rm ret}
  +
  \mathfrak X_{j,K_i^\times}^{\rm ret,up},
  \qquad
  K_i^\times=\left\lfloor\frac{\lfloor M_i/L_i\rfloor-2}{4}\right\rfloor-1.
\]
Under the standing non-profile assumptions, \(p_c(G)<p_{2\to2}(G)\) now
follows from finite-defect bins, near-tail bins, a terminal far tail,
same-sphere spread, long tangential runs, spread exterior returns,
same-level crossing-generated exterior returns, upper-shifted exterior
returns, and exact-level repeated exterior returns.
