SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T22:05:51.927285Z.
attacking: the one-or-two-transverse-mode rough glue by collapsing the partner's near-rank-one branch to a two-diagonal physical core and extracting the pinned-D5 anchor/transverse obstruction.

# EARLY — rank-one three-diagonal absorption

Programme `QFORM-DENSITY-3EIG-20260922`; full unrestricted theorem remains OPEN; continuity separate. Execution `WITHOUT_VERIFIED_BRAIN`.

First unpaid implication after the calculation below:

`QFORM-TWO-DIAGONAL-OR-STAR-CORE-GLUE-v1`: pay either (a) the exact two-large-diagonal near-rank-one core forced below, together with its retained second carrier/rough mode, or (b) the near-null robust-star branch after the pinned-D5 transverse cascade, without deleting any nonzero rough quadratic tail or rotating product variables.

## Early substantive lemma

Let

`A = D + theta v v^T + F`,

where `D` is diagonal, `F=F^T`, `||F||op<=beta`, and `s_3(A)>=1`. Suppose three original diagonal coefficients satisfy `|d_i|>=d0>0`. If `beta<=d0/12`, then one of the following physical certificates exists:

1. a two-coordinate principal block of the model `D+theta vv^T` has `sigma_min>=d0/6`; hence the corresponding ACTUAL pair of `A` has `sigma_min>=d0/12` and the same inertia; or
2. a three-coordinate principal block of the model has `sigma_min>=d0/4`; hence the ACTUAL triple of `A` has `sigma_min>=d0/6`.

Proof sketch, with the full proof reserved for REPORT.md. After multiplying the form by `-1` if necessary assume `theta>=0`. If two selected `d_i` are positive, their model pair is >=d0 I. If all three are negative, write `d_i=-p_i`, `p_i>=d0`, `a_i=theta v_i^2/p_i`. A negative pair is congruent to `-(I-zz^T)` and therefore has smallest singular value at least `d0 min(1,|1-a_i-a_j|)`. Unless all three pair sums lie within `1/6` of one, a good pair exists. If all do, `S=a_1+a_2+a_3` lies in `[5/4,7/4]`, so the negative triple is congruent to `-(I-zz^T)` with smallest singular value at least `d0/4`. If exactly one diagonal is positive, either the negative pair is already good or `a_2+a_3 in [5/6,7/6]`; one of `a_2,a_3` is at most `7/12`. Pairing that negative site with the positive one gives normalized determinant at least `a_1+5/12` and operator norm at most `a_1+19/12`, hence normalized smallest singular value at least `5/19>d0*(1/6)` after restoring the diagonal scale.

For a good actual definite pair, the two-dimensional area bound gives `||p_Q||inf<=12 pi/d0`. For a good actual indefinite pair, the full-matrix physical-pair theorem gives

`||p_Q||inf <= 3*400^(1/3)*(12/d0)^(5/6)`.

For a good actual triple, the localized three-coordinate theorem gives

`||p_Q||inf <= 36 sqrt(pi)/d0`.

Thus, with

`C_rank1(d0)=max(36 sqrt(pi)/d0, 3*400^(1/3)*(12/d0)^(5/6))`,

three such diagonal sites force `||p_Q||inf<=C_rank1(d0)`.

Applied to the newest completed designated partner fleet03/B13 r35 near-rank-one branch, `beta=C1/rho`, `C1=10.321553`, and `d0=1-C1/rho`. At `rho>=184`, `beta<=d0/12` and `C_rank1(d0)<184`; hence that branch cannot contain three large diagonal sites. The partner already proves that it contains at least two. Therefore for every slab witness with `rho>=184` in that branch there are EXACTLY TWO original diagonal coefficients with `|d_i|>=1-C1/rho`.
