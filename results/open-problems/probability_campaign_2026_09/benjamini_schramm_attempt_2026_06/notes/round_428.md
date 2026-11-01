# Round 428 laminarity of exterior-return intervals

Round 428 records a deterministic structural lemma for the spread-return
profiles.  This is the first candidate mechanism for reducing the raw
binomial entropy identified in Round 427.

For a rooted path \(\gamma=(v_0,\ldots,v_\ell)\), an exterior return through
level \(u\ge1\) is witnessed by a time interval \([s,t]\) with
\[
  d(x,v_s)=d(x,v_t)=u-1,\qquad
  d(x,v_{s+1})=d(x,v_{t-1})=u,
\]
and
\[
  d(x,v_b)\ge u\qquad(s<b<t).
\]

Consider two exterior-return intervals \(I=[s,t]\) through level \(u\) and
\(J=[s',t']\) through level \(v\).  Their time intervals cannot cross:
\[
  s<s'<t<t'
  \quad\text{or}\quad
  s'<s<t'<t
\]
is impossible.

Indeed, suppose \(u\le v\).  If \(s<s'<t<t'\), then \(t\in(s',t')\), so the
interior condition for \(J\) gives
\[
  d(x,v_t)\ge v,
\]
while \(I\)'s endpoint condition gives
\[
  d(x,v_t)=u-1\le v-1,
\]
a contradiction.  If \(s'<s<t'<t\), then \(s\in(s',t')\), so the interior
condition for \(J\) gives \(d(x,v_s)\ge v\), while \(I\)'s endpoint condition
gives \(d(x,v_s)=u-1\le v-1\), again a contradiction.  The case \(v<u\)
follows by symmetry after exchanging the two intervals.

Moreover, containment has a radial orientation.  If \(u<v\), then a
level-\(v\) return may be contained inside a level-\(u\) return, but a
level-\(u\) return cannot be strictly contained inside a level-\(v\) return:
an endpoint of the level-\(u\) interval would lie in the interior of the
level-\(v\) interval and would have radius \(u-1<v\), contradicting the
level-\(v\) interior condition.

Thus any chosen family of one exterior-return interval per return level is a
laminar forest, with nesting depth increasing with the return level.  This is
stronger than a raw subset of return levels.  It does not yet prove the
fixed-density spread-return exponent, but it gives a concrete route: replace
the binomial level-selection entropy by an enumeration of laminar return
forests plus the cost of the associated nested excursions.

The next target is to quantify the laminar-forest entropy.  A useful bound
would show that a family of \(\delta L_H\) exterior returns in a slab of
height \(\beta L_H\) either has a nested chain of length comparable to
\(\delta L_H\) or splits into many disjoint lower-level returns whose
time-ordered excursions can be charged separately.  Either alternative could
produce the missing return-level cost function \(a(\delta)\).
