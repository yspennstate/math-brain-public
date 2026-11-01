SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-24T04:38:00Z.
attacking: the multicarrier face-collapse gap by an exact three-carrier entropy dual; then test whether pair-anchored E4 promotion pays the complementary collapse on the same physical matrix.

# Early calculation — three-carrier face dual

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status at start: full unrestricted QFORM OPEN; owner control revision `2026-09-22.15`; execution `WITHOUT_VERIFIED_BRAIN`.

Let `M=A[I,J]` be a literal original-coordinate crossing and let `z_S=sum_{|T|=3} det(M[S,T])^2` be the physical row-triple Cauchy-Binet mass. Fix three physical row carriers `H={1,2,3}`. For each face `R subset H` define

`W_R = sum_{S: S cap H = R} z_S`.

After the standard conditional Gibbs optimisation over column triples and then over row triples inside a fixed carrier face, any face law `q_R` has determinant-entropy currency

`log G(q)=sum_R q_R log(W_R/q_R)`.

Imposing the exact carrier caps `P(i in S)=1/2` for all `i in H`, Lagrange duality gives

`G_* = inf_{x1,x2,x3>0} [sum_{R subset H} W_R prod_{i in R} x_i] / sqrt(x1 x2 x3)`.

Pair each face `R` with its complement `H\R`. For every positive `x`, AM-GM gives

`W_R x^R + W_{H\R} x^{H\R} >= 2 sqrt(W_R W_{H\R}) sqrt(x1 x2 x3)`.

Hence, taking one representative from each of the four complementary pairs,

`G_* >= 2 sum_{R mod complement} sqrt(W_R W_{H\R}).`

Thus failure of the pinned Theorem-D currency at scale `g` forces *every* complementary carrier-face product below `(g/2)^2`. This is a precise multicarrier collapse statement and does not select or invert any local minor.

Stress family to solve exactly: take the eight-row Walsh Parseval frame `U=H8[:,0:4]/sqrt(8)` and stack three heavy literal physical rows `L e1, L e2, L e3` above it. Right-multiply the coefficient matrix by a fixed dense orthogonal `4x4` matrix only to make all physical crossing coefficients nonzero; this does not rotate the independent variables. The Gram spectrum is

`M_L^T M_L = diag(L^2+1,L^2+1,L^2+1,1)` up to the fixed coefficient rotation.

For the three heavy carriers, aggregate row-triple face masses are predicted exactly by Cauchy-Binet:

`W_empty=4`, each singleton face `=3L^2`, each doubleton face `=2L^4`, and `W_123=L^6`.

By symmetry the dual minimiser has `x1=x2=x3=x`. Setting `y=L^2 x`, the carrier marginal equation becomes

`2 y(9+12y+3y^2)=3(4+9y+6y^2+y^3)`,

so the positive solution is `y=2`. Therefore

`G_*= (27/sqrt(2)) L^3`.

The light-row marginal under the face optimiser should be `3/16`, because conditional on a face of size `r` the Walsh light-row marginal is `(3-r)/8`, while the three carrier constraints force `E r=3/2`. Hence the pinned e5 Theorem D is genuinely admissible on this family and would give

`||p_Q||_inf <= 6 sqrt(e) (27/sqrt(2))^(-1/6) L^(-1/2)`.

Next: verify every identity exactly, apply newest fleet03/B04 pair-anchored E4 receiver to the same physical matrix, and compare with a valid direct ridge certificate without claiming post-rotation independence.