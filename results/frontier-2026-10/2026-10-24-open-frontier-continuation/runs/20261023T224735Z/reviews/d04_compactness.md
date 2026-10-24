# Independent audit: compactness proof of the rotated two-input macroscopic limit

## Verdict and precise scope

The proposed compactness argument **does identify a unique two-phase macroscopic gradient-flow limit**, provided the absorbing-at-zero ReLU solution and the joint initialization lemma in `runs/20261023T222120Z/agents/c01.md` are used. There is no apparent extra random first-layer mass or delayed third phase. The essential additions to the sketch are: (i) take Helly compactness in `L^1(0,T)`, so the unavoidable initial kernel layer causes no endpoint problem; (ii) prove gate identification using *unconditional* extreme-mark and small-weight bounds on strict-sign intervals of the limiting cumulative residual; and (iii) establish the sign geometry **before** using the gate identification, so a gate cannot be incorrectly declared alive merely because the cumulative residual has become positive again. These details are supplied below.

For fixed finite `T` and deterministic labels `y`, write `a_m=m^(1/alpha)`, `L_m=(log m)^(1/alpha)`, `beta_m=L_m/a_m`, `r_m(0)=y-F_m`, and `sigma_j,m=sgn r_j,m(0)`. Define the selected initial masses

`P_j,m=a_m^(-2) sum_i W_i(0)^2 1{V_ij(0)>0, sigma_j,m W_i(0)>0}`.

The preceding joint initialization gives `(r_m(0),C_m(0),P_m) => (r0,C,P)` with `C` positive definite, `C_12>0`, `P_j>0`, and `r0_j!=0` almost surely. Here `P` is selected from the marked Poisson process using the **random** sign vector of `r0`; it should not be declared independent of `r0` without conditioning on that sign vector. The identified limit is as follows. Put `Q0=C+diag(P1,P2)` and initially `r(t)=exp(-Q0 t)r0`, `J(t)=int_0^t r(s)ds`. If one coordinate `J_j` first returns to zero at a finite positive time `t_*`, set `Q1=Q0-P_j e_j e_j^T` and continue with `r(t)=exp[-Q1(t-t_*)]exp(-Q0t_*)r0` for `t>=t_*`. The other mass stays present. If neither integral returns, use `Q0` forever. The limiting output is `f=y-r`. The first-layer diagonal equals `P` on `(0,t_*)` and `P-P_j e_j` on `(t_*,infinity)`, understood almost everywhere or as the right-continuous positive-time version.

## Compactness and passage to the ODE

Fix `R,K,T` and work first on `{||r_m(0)||<=R, S_m<=K}`, where `S_m=a_m^(-2)sum_i[W_i(0)^2+V_i1(0)^2+V_i2(0)^2]`. This event exhausts probability as `R,K` increase. The cited energy estimate yields, uniformly on `[0,T]`, bounded kernels and Lipschitz residuals, plus

`sup_t ||C_m(t)-C_m(0)|| = O_(R,K,T)(beta_m)`, and

`a_m^(-2) sum_i sup_t |W_i(t)^2-W_i(0)^2| = O_(R,K,T)(beta_m)`.

Set `B_j,m(t)=a_m^(-2)sum_i W_i(0)^2 1{V_ij(t)>0}`. Then `sup_t|A_j,m(t)-B_j,m(t)|=o(1)` on this event. Each `B_j,m` is nonnegative, bounded by `S_m`, right-continuous and nonincreasing: an initially inactive coordinate never activates, and a coordinate stays at zero after its first hit. The bounded monotone class is compact in `L^1(0,T)` by Helly and dominated convergence. Thus `(r_m(0),C_m(0),P_m,B_m,r_m,J_m)` is tight in the product of finite-dimensional spaces, `L^1(0,T)^2`, and `C([0,T])^4`. Any subsequential coupled limit has `B_m -> A` in `L^1`, `r_m -> r` and `J_m -> J` uniformly, `A_j` nonnegative and nonincreasing a.e., and

`r(t)=r0-int_0^t [C+diag(A_1(s),A_2(s))]r(s)ds`, `J(t)=int_0^t r(s)ds`.       (1)

The uniform drift estimates and `L^1` convergence justify passing through the product `A_m r_m`; no pointwise convergence at a random gate-death time is needed. The value of `B_m(0)` contains *both* signs of initially active weights and need not converge to `P`. Hence the compactness assertion is deliberately on `(0,T)`, while the residual/output start at their genuine initial values.

## Geometry of every possible subsequential limit

Equation (1) alone suffices to settle the sign issue, for **any** bounded measurable nonnegative `A_j`. Write `c=C_12>0`. If `r_1>0>r_2` at a time, then `z=(r_1,-r_2)` solves a Metzler linear system with off-diagonal entries `c`; both components remain strictly positive at all later finite times. The reverse mixed-sign cone is likewise invariant. The linear system has an invertible fundamental matrix, so `r` cannot become the zero vector at finite time.

For initially equal signs, until the first residual-coordinate zero both residuals retain their signs. At that first zero, the other component is strict and the vanishing component immediately crosses into the opposite sign: in its integral equation the diagonal term is negligible at the zero and the forcing is `-c r_k`. The mixed-sign cone is invariant thereafter. Consequently at most one residual component ever changes sign. Its integrated component initially moves in its initial direction, then moves strictly in the opposite direction forever; the other integrated component moves strictly in its initial direction forever. Thus at most one `J_j` has a positive return to zero. If it does, the return is transversal, `J_j'(t_*)=r_j(t_*)` has the strict opposite sign, and `J_j` never returns again. Neither `J_j` has a zero interval. This argument does **not** assume that `A` has already been identified, and closes the potential circularity in the sketch.

In particular, a positive value of `sigma_j J_j(t)` implies it was positive at **every** earlier `s in (0,t]`; a negative value can occur only after the single transversal return. This historical statement is what justifies survival under absorbing gates.

## Identifying the diagonal: a useful cutoff lemma

The integrated gate formula is valid only **until that coordinate's first hit**. For every initially active coordinate still alive at `t`, and also at its first hit, it reads

`V_ij(t)=V_ij(0)+beta_m W_i(0)J_j,m(t)+e_ij,m(t)`,

`max_(i,j) sup_(t<=T) |e_ij,m(t)| <= const_(R,K,T) L_m^2/a_m=o(1)`.       (2)

Indeed `max_i sup_t|W_i(t)-W_i(0)|=O_(R,K,T)(L_m)`, and integrate `beta_m(W_i(s)-W_i(0))r_j,m(s)`. Formula (2) must **not** be applied to a coordinate after absorption. Every `|W_i(0)|>=epsilon a_m` retains its sign for large `m` on the localized event.

Here is a way to make the stochastic cutoff uniform without conditioning on the random limit path. For fixed `epsilon,tau,M>0`, the unconditional probability that some row with `|W_i(0)|>=epsilon a_m` has a positive gate mark `V_ij(0)` outside `(tau,M]` is bounded in the limit by

`const epsilon^(-alpha)[Pr(0<V_j<=tau)+Pr(V_j>M)]`.       (3)

This uses independence of `W_i(0)` and `V_ij(0)` and a union bound; it makes **no** independence assertion about the event selected by `r_m` or `J_m`. The discarded small-weight square mass `Z_m,epsilon=a_m^(-2)sum_i W_i(0)^2 1{|W_i(0)|<epsilon a_m}` obeys `limsup_m E Z_m,epsilon <= const epsilon^(2-alpha)`. First fix `epsilon`, then send `tau downarrow 0`, `M uparrow infinity`, `m uparrow infinity` in the needed bound; finally send `epsilon downarrow 0`. Equivalently choose `tau,M` for each fixed `epsilon` before the `m` limit. The slight order changes are harmless as long as the bad-mark probability is removed before the small-weight cutoff.

Localize further on `min_j|r_j,m(0)|>=rho>0`. Bounded kernel and residual imply a deterministic `t0=t0(rho,R,K,T)>0` with `sigma_j,m J_j,m(t)>=rho t/2` for `0<t<=t0`. By (2), any initially active opposing row (`sigma_j,m W_i(0)<0`, `|W_i(0)|>=epsilon a_m`, `V_ij(0)<=M`) must be dead by `t0`, since survival would imply `0<V_ij(t0)<=M-epsilon L_m rho t0/2+o(1)`. The same assertion holds by any fixed earlier `delta>0` within this early interval. Thus opposing macroscopic mass disappears near time zero.

Suppose now that `sigma_j J_j` is strictly positive up to a fixed `u>0`. On a compact interval `[delta,u]` strictly before its return, uniform convergence of `J_m` and the early deterministic bound give `sigma_j,m J_j,m(s)>=0` through `u` and a fixed positive lower bound at `delta`. A supporting extreme (`sigma_j,m W_i(0)>0`, `V_ij(0)>tau`) cannot hit zero: at its hypothetical first hit the right side of (2) is at least `tau-o(1)>0`. Every opposing extreme has died by `delta` (or by a smaller fixed early time). Hence, simultaneously on this interval,

`sup_(delta<=t<=u)|B_j,m(t)-P_j,m| <= Z_m,epsilon`       (4)

outside the bad-mark event, for all large `m`. If `sigma_j J_j(v)<0` at a fixed `v` after the return, every supporting extreme with `V_ij(0)<=M` must be dead by `v`: survival and (2) would give `V_ij(v)<=M-epsilon L_m |J_j,m(v)|+o(1)<0`. The opposing extremes have already died by `t0`. Absorption then gives, uniformly for `t in [v,T]`,

`0<=B_j,m(t)<=Z_m,epsilon`.       (5)

Equations (3)–(5), Markov's inequality for `Z_m,epsilon`, and countably many rational strict-sign intervals pass these implications to every subsequential `L^1` limit. In the limit, `A_j=P_j` a.e. wherever `sigma_j J_j>0`, and `A_j=0` a.e. wherever `sigma_j J_j<0`. Geometry excludes any positive-measure zero region. The lower-mark cutoff `tau` is essential for the **survival** assertion; the upper cutoff `M` is essential for the **death** assertion. It would be incorrect to infer either assertion from the sign of `J_j(t)` alone without accounting for earlier absorption.

## Uniqueness and resulting path statement

The identification fixes `A=P` on an initial interval `(0,t0)`. Until its first positive integrated return, (1) is therefore the constant-coefficient system with `Q0`; the first return, if present, is exactly that of `e^(-Q0t)r0`, not an additional free parameter of a Helly subsequence. The transversal return changes exactly one diagonal mass to zero, while the other cumulative residual retains its original sign. The residual at the return has mixed signs, and the mixed-sign invariant cone keeps them so under `Q1`. Equations (4)–(5) then fix the remaining `A` and the second phase. This proves uniqueness of every subsequential limit and identifies the joint law with the prior joint initialization.

Explicitly, with `Q0=[[a,c],[c,b]]` and initially equal residual signs, put `u=|r01|`, `v=|r02|`. Coordinate 1 switches precisely when `v/u>b/c`; coordinate 2 switches precisely when `v/u<c/a`; otherwise there is no finite switch. Since `ab>c^2`, the two alternatives cannot both occur. Mixed initial signs never switch. At either equality threshold the relevant integral approaches zero only at infinite time. Conditional on `(C,N)` and a sign orthant, the initial residual has a density, so zero initial coordinates, either threshold equality, and a switch exactly at any specified deterministic `delta` or `T` have probability zero.

The compactness proof therefore yields joint weak convergence of `(r_m(0),C_m(0),P_m,r_m,J_m)` with `r_m,J_m` in `C([0,T])`, hence uniform-in-time convergence in law for the output `f_m=y-r_m`. On `[delta,T]`, `delta>0`, the kernel converges to the indicated one-jump `C+diag(A)` in the **scalar `M_1` topology for each varying diagonal** (and uniformly away from the random switch); the off-diagonal and frozen `C` entries converge uniformly. Endpoint switch atoms are excluded as above. Do not claim `J_1` convergence of the kernel: two distinct endpoint atoms can die at distinct times tending to `t_*`, leaving an order-one intermediate step, which cannot coalesce into one `J_1` jump. Nor can a usual cadlag limit on `[0,T]` retain both the unselected mass in `H_m(0)` and the selected right limit at `0+`. A separate boundary-time statement would be required to describe the initial kernel layer.

**Status:** The proof strategy is valid for continuous absorbing gradient flow and the stated two rotated orthogonal inputs. The existing nonfreezing note proves less, but its energy and initialization ingredients are sufficient for the argument above. This main audit does not extend the conclusion to discrete GD, smooth activations, or nonorthogonal input geometry, and it does not independently re-prove the lengthy joint initialization lemma.

## Review of the coordinator's written `TWO_INPUT_LIMIT.md`

I subsequently checked that complete candidate line by line. **Accept the stated `C([0,T]) × L^1([0,T])` theorem for the 45-degree pair.** Its finite-width equations and unscaled gate-error estimate are correct. Its endpoint-atom argument explicitly uses the formula only before a hit; it protects an initially supporting atom near time zero by the initial residual sign, then by the strictly positive cumulative margin. A returning atom is killed by the negative cumulative margin, and opposing atoms have already died. Finite truncated atoms converge at all times other than the possible switch, so dominated convergence gives their `L^1` limit; unconditional omission probabilities for very large `|z|` and marks, together with the `O(epsilon^(2-alpha))` small-square bound, remove the truncation. This is sufficient to identify every Helly limit and to pass through the residual integral equation. The one-switch classification agrees with the independent geometry calculation. The theorem wisely states only `L^1` kernel convergence, which handles both the initial layer and coalescing later atom deaths.

Two small textual improvements would make the coupling step fully explicit, without changing the result. Include `S_m` (or the uniform drift/error bounds themselves) in the joint tight tuple used for the Skorokhod representation, or state the finite-atom conclusions as probability inequalities on the observable tuple `(N_m,B_m,J_m,r_m,S_m)`. This transports the localized pre-hit bounds into the coupling without an implicit assumption that an arbitrary coupling preserves microscopic trajectories. Also state that matching a truncated atom requires `epsilon<|z|<R`, bounded marks, and gate projections bounded away from zero; the written proof says this in prose, and the mark-boundary probability vanishes because each projection has a continuous density. Neither point is a substantive gap.

I also inspected `agents/d01_hybrid.md` for its proposed extension to **any fixed pair of orthonormal inputs in fixed dimension**. Its coordinate-ray reduction has the right coefficients `h_ell^±=(±(x_{1,ell},x_{2,ell}))_+`, the second-largest original-coordinate bound has finite alpha moment, and the Gram cross products vanish with the displayed `p` choice. Different product rays have no common limiting jump; the endpoint separation argument used in `c01.md` extends to finitely many coordinate rays. The ray vectors span `R^2` because their differences give the coordinate rows of the rank-two input matrix, so the resulting `C` is positive definite almost surely; `P_j>0` almost surely. If `C_12=0`, the limit residuals decouple and no later switch occurs. Otherwise the same cone and gate proof applies. Thus this extension appears valid, subject to writing its joint-initialization lemma as a separately stated result and independently checking the finite-ray endpoint separation if it is promoted into the main theorem. The coordinator's 45-degree statement does not rely on that extension.
