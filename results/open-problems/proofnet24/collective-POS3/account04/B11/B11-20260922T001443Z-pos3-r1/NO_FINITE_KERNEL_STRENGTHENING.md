# Strengthening — arbitrary order with width exactly three, connected incomparability graph, and `pi<=3`

This strengthens Proposition 6.1 of `REPORT.md`, whose simpler threshold-order family had `pi<=4`.

For every `n>=4`, form intervals on the real line

- `I_1=[0,3]`,
- `I_2=[0,1]`,
- `I_3=[1/2,3/2]`,
- for `k>=4`, `I_k=[2+(3/2)(k-4), 4+(3/2)(k-4)]`.

Define an interval order `R_n` by

`i <_{R_n} j` iff the right endpoint of `I_i` is strictly smaller than the left endpoint of `I_j`.

Two elements are incomparable exactly when the corresponding intervals intersect.  The incomparability graph is therefore a triangle on `I_1,I_2,I_3` with a path tail

`I_1 -- I_4 -- I_5 -- ... -- I_n`

attached at `I_1`.  Hence it is connected and has maximum degree `3`, so

`pi(R_n)<=3`.

The triangle gives width at least three.  There is no four-element antichain: an antichain in an interval order is a pairwise-intersecting family of intervals, and intervals satisfy the one-dimensional Helly property; inspection of the construction shows no point lies in four intervals.  Thus the width is exactly three.

Since `n` is arbitrary, even

`width(P)=3`, connected incomparability graph, and `pi(P)<=3`

do **not** imply a finite order bound.

This does not assert that `R_n` is a POS3 counterexample.  It only blocks a structural shortcut: a qualitative theorem saying that hypothetical counterexamples have bounded incomparability range cannot by itself be converted into a finite census unless one proves additional counterexample-specific structure.
