SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T12:01:05Z.
attacking: the nested dominant-2x2-pivot / near-rank-one Schur collar; control the bankwise shear from aggregate E2 dominance, then use the fractional-volume perturbation theorem before the tiny transverse direction is discarded.

# Early substantive checkpoint

Let a physical cross block be

`N=[[P,R],[C,M]]`, `P` invertible `2x2`, `D=|det P|`, `S=M-CP^{-1}R`, and `E2=e2(N^T N)`.

Assume the literal pivot carries a fixed fraction of aggregate second volume,

`D^2 >= theta E2`, `0<theta<=1`.

Cauchy--Binet on the two pivot columns and on the two pivot rows gives exactly

`D^2 det(I+(CP^{-1})^T(CP^{-1})) <= E2`,

`D^2 det(I+(P^{-1}R)(P^{-1}R)^T) <= E2`.

Hence

`||CP^{-1}||op, ||P^{-1}R||op <= sqrt(theta^{-1}-1)`.

Let `S1=s1(S)uv^T` be a top singular rank-one part and define

`N0=[[P,R],[C,CP^{-1}R+S1]]`.

Then

`N0 = [[I,0],[CP^{-1},I]] diag(P,S1) [[I,P^{-1}R],[0,I]]`,

so with

`m*=min(sigma_min(P),s1(S))`, `kappa_theta=(1+sqrt(theta^{-1}-1))^2`,

one has

`s3(N0) >= m*/kappa_theta`,

while

`||N-N0||op=s2(S)`.

Thus the live nested-minor endpoint can be treated as a genuine rank-three physical cross block plus a controlled operator tail. The next step in this run is to feed this exact decomposition into the completed fractional-volume stability theorem, retaining its leverage gate, and to splice the complementary non-small-tail branch to the fresh account02/B02 bankwise-Schur grouped Fourier theorem. Full QFORM remains open.