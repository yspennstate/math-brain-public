# Mandatory alpha-log control

The pinned coherent-composition source is `math-open-problems` commit
`d6538f38b044b6206bc22764bd31859e334ed430`, file
`coherent-balanced-composition-control/source/PROOF.md`, Git blob
`37626caf9f1564342f8b6edfff54b3a3491fff35`. Its full prose is preserved in
`out/source_proof.md`. All formulas in this file use natural logarithms.

For the two-input sign AND outer,
`a=(-1/2,1/2)`, `b=(1/2,1/2)`, and `q=1/2`, the exact remainder is

`R(alpha)=(alpha^2/2) ln(1/alpha^2)
 +[(1-alpha)^2 ln(1-alpha)+(1+alpha)^2 ln(1+alpha)]/2`.

The second summand S has `S(0)=S'(0)=0` and
`S''(alpha)=3+ln(1-alpha^2)`. For `|alpha|<=1/2`, S is nonnegative:
`ln(3/4)>-1`, for example from `ln(4/3)<=1/3`.
Consequently `R/(q alpha^2)>=ln(1/alpha^2)` on this interval, and
Taylor's theorem gives `R=(alpha^2/2)ln(1/alpha^2)+(3/2)alpha^2+O(alpha^4)`.
Thus the new result does not revive `R<=C q alpha^2`.

For n>=3 take `h_n(x_i,z)=x_i u_n(z)`, where u is parity on n-1 bits
with its value at the all-positive point flipped. Then h is balanced,
`alpha=-2^(2-n)`, `Inf_i(h)=1`, and `D_i(h)=0`. A literal second inner
gives actual Boolean AND compositions with `Inf_i(F)=1/2`.
The selected-coordinate decrement ratio tends to zero, even though
`R/(q alpha^2)` diverges. The key distinction is actual physical influence
versus singleton Fourier mass.

The checker reconstructs this family from its truth tables for n=3,...,8,
checks alpha, influence, and zero inner decrement exactly, and records the
exact lower scales `2(n-2) ln(2)`. The all-n obstruction is analytic, not
inferred from the six finite cases. The checker also certifies the new full
remainder upper bound on 3360 balanced composition splits.

The tree logarithm lemma pays the displayed logarithmic term by actual
influence and retains it in every formula. It does not say the full remainder
is bounded by singleton mass, or that a balanced representation survives
restriction. When alpha=0 the exact remainder is zero. When alpha=1,
the logarithm vanishes while R is the outer physical entropy decrement;
this endpoint explains why an outer-erasure term must remain.

Other obstruction scope: overlapping-variable products are outside the
disjoint-block hypotheses; arbitrary real inputs lack the Boolean derivative
bound; the noisy outer is used only for a JS bound, never as a Boolean leaf.
The parity-erasure and sparse-activation controls forbid declaring zero
root erasure or cheap children sufficient for a terminal entropy payment.
