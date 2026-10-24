# Round 498 compressed trace words and root-interval validity

Round 497 needs one technical correction.  The heights in a root-column trace
word should be read as compressed portal heights, not as every visit to the
root column.  If every root-column vertex were listed, then a vertical segment
would only produce nearest-neighbor consecutive heights and there would be no
separate vertical-interval label.

Use the maximal decomposition instead.  A cone path alternates between:

1. maximal vertical runs in the root column; and
2. child-cone pieces that leave the root column at one height and return at
   another height.

The trace word is
\[
  \mathcal W=(h_0,\ell_0,h_1,\ell_1,\ldots,\ell_{m-1},h_m),
\]
where the \(h_i\) are portal heights, and \(\ell_i\) is either \(V\) or a
child label.  If \(\ell_i=V\), the path visits every root-column vertex in
the closed interval between \(h_i\) and \(h_{i+1}\).  If \(\ell_i\) is a child
label, the root column is touched only at the two portal heights.

This gives an exact root-column validity test.  Let
\[
  P(\mathcal W)=\{h_0,\ldots,h_m\}.
\]
Assume the child-cone pieces are themselves self-avoiding and avoid their
root column except at their endpoints.  Then the root-column part of
\(\mathcal W\) is self-avoiding if and only if:

* the portal heights \(h_0,\ldots,h_m\) are all distinct;
* no two consecutive labels are both \(V\), after maximal compression;
* every \(V\)-labeled pair \(\{h_i,h_{i+1}\}\) is an adjacent pair in the
  increasing order of \(P(\mathcal W)\); and
* the \(V\)-labeled adjacent pairs form a matching.

Indeed, if a portal height lies strictly between the endpoints of a vertical
run, that portal vertex was already visited during the run.  If two vertical
runs overlap in their interiors, some root-column vertex is visited twice.
Conversely, adjacent matched gaps have disjoint interiors and contain no
other portal height, so all root-column revisits are excluded.

Thus vertical-run entropy is not a free signed composition.  For a fixed
portal set \(P=\{x_0<\cdots<x_m\}\), the vertical labels form a hard-core
matching on the line of gaps \((x_j,x_{j+1})\).  Their metric contribution is
\[
  \prod_{\{x_j,x_{j+1}\}\in M_V} z^{x_{j+1}-x_j}.
\]
There are only Fibonacci-many possible vertical matchings on \(m\) gaps, and
large vertical moves carry their full metric cost.

The annular exterior condition adds a second local test.  If the cone root is
at tree depth \(r\) and the forbidden ball has radius \(u\), a vertical gap
\([x_j,x_{j+1}]\) is legal only when
\[
  r+|t|\ge u
  \qquad\text{for every integer }t\in[x_j,x_{j+1}].
\]
In the one-sided high-root regime this is exactly the excess-walk constraint:
upward vertical motion preserves or increases excess, while downward motion
spends it.

The next recursive norm should therefore treat the root-column contribution
as a hard-core gas on the ordered portal gaps, not as independent vertical
runs.  The remaining uncontrolled entropy is the time order of the portals
and the interleaving of the child-label subwords.
