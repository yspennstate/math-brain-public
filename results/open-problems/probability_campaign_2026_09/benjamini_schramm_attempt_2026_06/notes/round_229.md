# Round 229

Round 229 splits the heavy-slab obstruction into token types.

For a slab \(A\), define
\[
  I_x(\gamma;A)
  =
  \sum_{u\in A}\#\{t:d(x,v_{t-1})=u,\ d(x,v_t)=u-1\}
\]
and
\[
  H_x(\gamma;A)
  =
  \sum_{u\in A}\#\{t:d(x,v_{t-1})=u,\ d(x,v_t)=u\}.
\]
Since
\[
  D_x(\gamma;A)=2I_x(\gamma;A)+H_x(\gamma;A),
\]
a heavy slab with \(D_x(\gamma;A)>\theta L_H\) is either inward-heavy,
\[
  I_x(\gamma;A)>\theta L_H/4,
\]
or horizontal-heavy,
\[
  H_x(\gamma;A)>\theta L_H/2.
\]
This gives
\[
  \mathfrak V^{\rm rad}
  \le
  \mathfrak V^{\rm rad,in}
  +
  \mathfrak V^{\rm rad,hor}.
\]

The inward-heavy case is further split by a fixed integer \(K\): either the
inward tokens occur on more than \(\theta L_H/(4K)\) levels in the slab, or
some single level has more than \(K\) inward tokens.  Each inward token at a
fixed level pairs with a preceding outward crossing and hence gives an
exterior return segment through that level.  Thus the localized obstruction
has been sharpened into horizontal slab motion, spread inward motion across
many levels, or repeated exterior returns through one level.
