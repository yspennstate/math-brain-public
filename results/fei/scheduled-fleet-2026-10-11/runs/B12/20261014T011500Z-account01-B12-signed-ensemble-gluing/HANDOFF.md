# A058 handoff: signed ensemble is paid, target sign is not

For pairwise disjoint physical pieces `b_j`, the complete Rademacher ensemble
obeys

`average_epsilon Eraw(sum epsilon_j b_j) <= sum_j Eraw(b_j)`,

`average_epsilon I(sum epsilon_j b_j) = sum_j I(b_j)`.

This is uniform in dimension, piece count, Fourier overlap and gluing depth.
It uses normalized spectral laws, so the raw-convolution tensor obstruction
does not apply.

For Boolean `f` and a cube isometry `tau`, the masks

`a=(f+f o tau)/2`, `b=(f-f o tau)/2`

are physically disjoint and satisfy

`H(f)<=Eraw(a)+Eraw(b)`, `I(f)=I(a)+I(b)`.

Hence any common source payment for the two masks proves FEI for `f` with the
same constant.  In particular, two affine-cylinder masks with fiber constant
`C` give `H(f)<=max(C,4)I(f)`.

Do not project the ensemble inequality to one arbitrary signing.  The exact
three-bit point-defect decomposition in `PROOF.md` violates single-sign
subadditivity by `0.515679411089406...`; the sign is certified by
`7^98>2^128*3^72`.  The companion signing is constant and carries the refund.

Next: study `D(epsilon)=Eraw(b_epsilon)-C I(b_epsilon)`.  Construct a
physical involution or posterior activation witness that pairs the target
sign with a nonpositive companion over the actual adaptive hierarchy.  Test
X007 and the signed-mask tensor family first.  No per-depth recharge is
allowed.

Independent review is pending.  Full FEI is open.

