SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T21:24:32Z.
attacking: moving-sheet weak closure for the ruled majority submeasure and the exact near-null sign asymmetry of the ruled coefficient.

# Early calculation: the ruled majority constant does not see a vanishing minority curvature

For a physical three-coordinate block of signature `(2,1)` with eigenvalue magnitudes `lambda1,lambda2,mu>0`, the completed ruled one-sheet theorem at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` gives the majority-side coefficient

`C_+(lambda1,lambda2,mu)`
`=(lambda1 lambda2 mu)^(-1/2) int_0^(2pi) [sin^2(theta)/lambda1+cos^2(theta)/lambda2+1/mu]^(-1/2) dtheta`
`=int_0^(2pi) [lambda2 mu sin^2(theta)+lambda1 mu cos^2(theta)+lambda1 lambda2]^(-1/2) dtheta.`

Therefore, with no lower bound at all on the minority magnitude `mu`,

`C_+ <= 2 pi / sqrt(lambda1 lambda2)`.

In particular if the two same-sign (majority) eigenvalues obey `lambda1,lambda2>=kappa`, then

`C_+ <= 2 pi/kappa`

uniformly for every `mu>0`, including `mu -> 0`. Hence after conditioning on all outside original coordinates and completing the square inside an invertible physical block, the majority submeasure obeys

`P(Q in I, Q>=c(W)) <= (2 pi/kappa)|I|`

and the triangular functional obeys

`E[(eps-|Q-y|)_+ 1_{Q>=c(W)}] <= (2 pi/kappa) eps^2.`

This uses the completed ruled theorem at an actual owner-scale inequality. The current audit correction that the linear term must lie in the range is satisfied automatically because the physical 3x3 block is invertible; completion of the square is an original-coordinate translation and preserves the cap-one product law.

The sign asymmetry is genuine at the level of this receiver. If instead one of the two majority magnitudes tends to zero, e.g. `(lambda1,lambda2,mu)=(1,gamma,1)`, then

`C_gamma=int_0^(2pi)[cos^2(theta)+gamma(1+sin^2(theta))]^(-1/2)dtheta.`

For `0<gamma<=1/8`, on each of the two intervals `|theta-pi/2|<=1/2`, `|theta-3pi/2|<=1/2`, use `cos^2(theta)<=u^2` and `1+sin^2(theta)<=2` to get

`C_gamma >= 4 asinh(1/(2 sqrt(2 gamma))) = 2 log(1/gamma)+O(1).`

Thus only the minority-null collar is uniformly paid by this exact one-sheet constant; a majority-null collar retains the expected rank-two indefinite logarithm.

Partner obstruction consumed: fleet03/B15 `math-open-problems@4d7b28c4737455388bd14f7bb7abeca5264dffd7` proves sharply that for `S=gamma Z^2+2rZ`, `gamma!=0`,

`||p_S||_q <= [2^(q-1)/(2-q)]^(1/q)|gamma|^(-1+1/q)`, `1<q<2`,

with equality after translating a unit uniform to the moving critical point. At `q=3/2`, this is `2|gamma|^(-1/3)` and has no gain from `r`. Comparing with the preceding `C_+<=2pi/kappa` shows that conditioning away the joint ruled geometry can manufacture a polynomial near-null loss even when the exact majority receiver is uniformly bounded. The near-null minority branch should therefore keep the physical triple jointly until the one-sheet payment is taken.

Full unrestricted QFORM remains OPEN; the minority/two-sheet term and global structural selection remain unpaid.
