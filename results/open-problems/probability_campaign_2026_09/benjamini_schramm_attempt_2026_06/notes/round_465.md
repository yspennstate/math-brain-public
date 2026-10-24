# Round 465 half-plane transfer overcounts the two-layer product

Round 465 records the first crude upper-bound attempt for
\(T_d\square K_2\) and why it is not yet sharp enough.

If one forgets self-avoidance and remembers only the radial excess
\[
  e_t=d_T(o,v_t)+\epsilon_t-u\ge0,
\]
then from a typical state:

* outward tree moves increase \(e_t\) by \(1\) with about \(d-1\) choices;
* inward tree moves decrease \(e_t\) by \(1\) with one choice;
* layer switches change \(e_t\) by \(\pm1\) with one choice.

This gives a one-dimensional half-plane walk with upward weight roughly
\[
  d
\]
and downward weight roughly
\[
  2.
\]
The spectral radius of the corresponding unconstrained excursion transfer is
of order
\[
  2\sqrt{2d},
\]
which is much larger than the desired \(d-1\) for small \(d\).

This failure is expected.  The radial-excess process forgets the key
self-avoidance fact: an inward tree move in one layer is only safe because
the outward tree segment was traversed in the other layer, or because the
tree vertex has not appeared before in that layer.  The out-and-back lower
bound uses this constraint optimally; the radial half-plane overcount allows
unlimited incompatible switching patterns.

Therefore an upper bound for \(T_d\square K_2\) must retain at least one more
state variable, such as:

1. whether the current tree edge lies on the already used spine in the current
   layer;
2. whether switching layer would land on a previously used tree vertex;
3. the stack height of the tree projection since the last layer switch.

This suggests a pushdown/stack transfer rather than a finite Markov chain in
the radial excess alone.  The product calibration remains promising, but the
first crude half-plane bound is too coarse.
