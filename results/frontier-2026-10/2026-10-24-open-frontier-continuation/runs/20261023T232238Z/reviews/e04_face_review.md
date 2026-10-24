# Independent audit: local attracting-face selection and Schur action

**Disposition:** `FACE_SCHUR.md` passes this deterministic audit under its explicit hypotheses: full-row-rank `X`, frozen `z,r`, strict `P,N` projection margins, nonempty `B`, `z r_B<0`, and the strictly interior solution `theta_B^* in (0,1)^B`. The proof establishes local vanishing-Euler-step selection, uniqueness of the corresponding convex inclusion, finite-time capture, and the stated output action. I found no substantive gap. It is not a self-consistent stochastic training limit or an external novelty claim.

## Filippov set and Euler selection

With `c_j=-z r_j>0`, the frozen-sign field is `a_P-sum_(j in B)c_j 1{x_j·u>0}x_j`. The function `phi(u)=sum_j c_j(x_j·u)_+-a_P·u` is convex and globally Lipschitz, and `-partial phi` is exactly the convexified field. At a point with some zero `B` projections, every binary sign combination for those projections is locally attainable: the map `X_B:R^d->R^B` is onto. Convexifying all those vertex fields therefore gives independent coefficients `theta_j in [0,1]`, matching the subgradient formula. This remains a *local* Filippov identification while `P,N` signs stay fixed.

The Euler compactness proof is valid for arbitrary selections `g_n in partial phi(u_n)`, including the actual zero-at-zero ReLU convention. The common bound `||g_n||<=M` makes polygons uniformly Lipschitz. Along a uniformly converging polygon subsequence, their piecewise constant subgradients have a weak-star `L-infinity` limit. For each fixed rational `v`, integrate the subgradient inequality over arbitrary measurable time sets. Uniform convergence of nodes and Lipschitz continuity of `phi` pass all terms except the linear subgradient term strongly; weak-star convergence passes that term. Hence the limiting inequality holds almost everywhere, first for rational `v` and then every `v` by continuity. The limiting path solves `u' in -partial phi(u)`. Monotonicity of convex subgradients gives contraction of distances between two solutions and thus uniqueness. Every vanishing-step sequence has the same limit. No loss-descent or tangent-kernel positivity claim is needed for this selection.

The proof's globally defined frozen-sign model is a device for this local conclusion. If the starting point is sufficiently close to the relative interior of the face, the strict `P,N` margins and the velocity bound `M` keep their signs fixed through the short capture interval. Equivalently, uniform Euler convergence and a positive margin exclude an earlier `P,N` crossing for small steps. The lemma correctly stops at the first later `P,N` sign change.

## Attraction and capture

Let `w=Pi_N u`, the projection onto the row space of `X_B`. Since `G_BB` is SPD, the normal projection of `a_P` is

`Pi_N a_P = z X_B^T G_BB^(-1)G_BP r_P
            = sum_(j in B)c_j theta_j^* x_j`.

This verifies (3), including its signs. On the normal space, `w'=-sum_j c_j(theta_j-theta_j^*)x_j`. For `x_j·w>0` the inclusion forces `theta_j=1`; for `x_j·w<0` it forces `theta_j=0`; at zero the product with `x_j·w` vanishes. Therefore `(theta_j-theta_j^*)(x_j·w)>=min(theta_j^*,1-theta_j^*)|x_j·w|`. Summing yields (5). Because `w` lies in the row space of `X_B`, `||X_B w||_2>=sigma_min(X_B)||w||`, and `sum_j|x_j·w|>=||X_Bw||_2`. Thus `d||w||/dt<=-delta sigma_min(X_B)` almost everywhere while `w!=0`, proving the capture bound (6).

At `w=0`, `theta^*` gives zero normal velocity and the constant tangent velocity `Pi_T a_P`. This is a valid solution; uniqueness of the convex flow proves that a captured trajectory stays on the face. The strict inequalities `0<theta^*<1` are what make attraction uniform rather than mere face feasibility. The argument does not extend as written when a coefficient is at an endpoint, `z r_j>=0`, or the face is rank-degenerate.

## Velocity and matrix-versus-action check

Tangency is `G_BB q_B+G_BP r_P=0`, with `q_B=diag(theta_B)r_B`. SPD of `G_BB` and nonzero `r_B` make `q_B=q_B^*` and `theta_B=theta_B^*` unique. Substituting `q_B^*=-G_BB^(-1)G_BP r_P` into `V'=zGq` gives all three lines of (7), including the `N` line. On the face, `V_B=0`, `V_P>0`, and `V_N<0`; hence the endpoint output derivative is exactly `z^2 E_P S E_P^T r`, with `S=G_PP-G_PB G_BB^(-1)G_BP`. This `S` is SPD for nonempty `P` by the Schur-complement theorem; the output-action representative is symmetric PSD.

The matrix distinction in the lemma is important and correct. With `G=[[1,1/2],[1/2,1]]`, `B={1}`, `P={2}`, `z=1`, and `r=(-1,1)`, one has `theta_1^*=1/2`. The output-action representative is `diag(0,3/4)`. The fractional expression `D(theta)G D(theta)=[[1/4,1/4],[1/4,1]]` is a different matrix, but both send this particular `r` to `(0,3/4)`. An average of binary tangent Grams with boundary-active fraction `1/2` would instead be `[[1/2,1/4],[1/4,1]]`, whose action on `r` is `(-1/4,3/4)`; it is not the face output derivative. The lemma carefully avoids identifying these matrices.

The captured-face result concerns one frozen endpoint and residual, and lasts only until a `P` or `N` sign changes. It supplies no uniform estimate for growing boundary time, coupled endpoints, or a changing network residual. Those limitations are explicitly respected in the statement.
