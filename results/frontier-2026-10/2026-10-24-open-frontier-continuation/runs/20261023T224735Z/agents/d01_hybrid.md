# T384: global two-input absorbing hybrid limit in the stable coordinate model

**Result.** For two fixed orthonormal inputs in a fixed finite-dimensional space, iid symmetric `alpha`-stable hidden coordinates (`0<alpha<2`), both layers trained by continuous squared-loss gradient flow, and explicit absorption at ReLU gates, the output has a full macroscopic `C([0,T])` limit. The rate-scaled kernel has a full `L^1([0,T])` limit for every finite T. After the initial layer, its first-layer diagonal consists of the initially supporting output-weight populations. At most one of those two populations can later disappear, at the unique transverse return of its cumulative residual to zero. The second-layer matrix is frozen and may have a strictly positive off-diagonal. No kernel `J_1` claim is made at the later switch: multiple endpoint-atom deaths collapse into one macroscopic jump, creating a separate topology question.

This note proves the compactness and identification argument, rather than assuming a transverse crossing. The 45-degree rotation of `../20261023T222120Z/agents/c01.md` is an explicit instance. The result extends the coordinate-input argument in `research/T384_COORDINATE_LIMIT.md` to **any pair of orthonormal inputs** in the iid-stable coordinate basis. It does not treat three or more training inputs or nonorthogonal inputs.

## Notation and exact finite-width equations

Fix `d<infinity` and orthonormal `x_1,x_2 in R^d`. Let the initial `U_i in R^d` have iid standard symmetric alpha-stable coordinates, and let the `W_i` be independent standard symmetric alpha-stables. Put

`a_m=m^(1/alpha)`, `L_m=(log m)^(1/alpha)`, `b_m=a_m L_m`, `gamma_m=L_m/a_m`, `c=Gamma(alpha)sin(pi alpha/2)/pi`, and `beta=alpha/2`.

Write `V_ij=U_i dot x_j`, `h_i=((V_i1)_+,(V_i2)_+)`, and `f_m=b_m^(-1)sum_i W_i h_i`. Train with learning-rate multiplier `L_m^2` and loss `||y-f_m||^2/2`. The gate-selection rule is that when any `V_ij` reaches zero, it stays zero; this is consistent with the other input's gradient because the inputs are orthogonal. Let `r_m=y-f_m` and `J_j,m(t)=int_0^t r_j,m(s)ds`. Away from gate hits,

`V_ij'=gamma_m W_i r_j,m 1_{V_ij>0}`, `W_i'=gamma_m sum_{j=1}^2 r_j,m(V_ij)_+`,

`r_m'= -K_m r_m`, `K_m=diag(A_1,m,A_2,m)+C_m`,

`A_j,m=a_m^(-2)sum_i W_i(t)^2 1_{V_ij(t)>0}`, `C_m=a_m^(-2)sum_i h_i(t)h_i(t)^T`.

The first-layer block is exactly diagonal because `x_1 dot x_2=0`; `C_m` need not be diagonal. The integral equation for r holds through hits and `K_m` is positive semidefinite, so `||r_m(t)||<=||r_m(0)||`.

## Joint initialization lemma, including arbitrary orthonormal orientation

For `ell=1,...,d`, put `v_ell=(x_{1,ell},x_{2,ell})` and `h_ell^+=(v_ell)_+`, `h_ell^-=(-v_ell)_+` coordinatewise. Let all `Z_ell^sign` be independent symmetric alpha-stables with characteristic function `exp(-c|t|^alpha)`, and all `S_ell^sign` be independent positive beta-stables with Laplace transform `exp[-c Gamma(1-beta)s^beta]`. Let `N` be independent of all these variables, a Poisson measure on `(R\{0}) x R^d` with intensity `alpha c |z|^(-1-alpha) dz product_ell P_U(du_ell)` on both z half-axes. Then the joint initialization limit is

`F=sum_{ell,sign} h_ell^sign Z_ell^sign`,

`C=sum_{ell,sign} S_ell^sign h_ell^sign(h_ell^sign)^T`,

`N_m=sum_i delta_(W_i/a_m,U_i) => N`,

with `F_m=f_m(0) => F`, `C_m(0) => C`, and **all primitive** `Z,S,N` mutually independent in the joint limit. The two F marginals are nondegenerate and atomless. The matrix C is positive definite almost surely, with nonnegative entries. Indeed the signed rays h_ell^sign span R^2 because v_ell=h_ell^+-h_ell^- and the two inputs are independent; every corresponding S coefficient is strictly positive. Two independent nonparallel stable ray components also give F an everywhere-positive continuous two-dimensional density, after convolution with the other rays. See the independent detailed check in reviews/d02_general_pair_review.md.

Equivalently, for `t in R^2` and any positive semidefinite `2 x 2` matrix `Lambda`, the exact transforms are

`E exp(i t dot F)=exp[-c sum_{ell,sign}|t dot h_ell^sign|^alpha]`,

`E exp[-tr(Lambda C)]=exp[-c Gamma(1-beta)sum_{ell,sign}((h_ell^sign)^T Lambda h_ell^sign)^beta]`.

Set `r_0=y-F` and `sigma_j=sgn(r_0j)`, which is defined almost surely. The selected initial-sign first-layer populations are

`P_j=int z^2 1_{u dot x_j>0, sigma_j z>0}N(dz,du)`, `j=1,2`.

The integrals are finite almost surely. The corresponding finite-width `P_j,m=a_m^(-2)sum_i W_i(0)^2 1_{V_ij(0)>0,sigma_j,m W_i(0)>0}` converge jointly with the other initialization variables, where `sigma_j,m=sgn(y_j-F_j,m)`. The full initial kernel also converges separately to `C+diag(int z^2 1_{u dot x_j>0}N)`.

Here is a proof of the orientation-dependent assertion, needed for the dynamic theorem. Let `H(u)=((x_1 dot u)_+,(x_2 dot u)_+)` and `Psi(u)=sum_{ell,sign}(sign u_ell)_+ h_ell^sign`. If `M_2(u)` is the second-largest coordinate magnitude, choosing the largest coordinate first and using the Lipschitz property of ReLU yields `||H(u)-Psi(u)||<=C_d M_2(u)`. Independence and stable tails give `P(M_2(U)>t)=O(t^(-2alpha))`, so `E M_2(U)^alpha<infinity`. Conditional on the U array, a W-weighted sum is exactly alpha-stable; hence the normalized difference `b_m^(-1)sum_i W_i[H(U_i)-Psi(U_i)]` tends to zero in probability because its conditional alpha-power scale has expectation `O(1/log m)`. Thus F reduces to the `2d` product sums `b_m^(-1)sum W_i(sign U_iell)_+` along the ray vectors `h_ell^sign`.

For the Gram limit, `||H(u)H(u)^T-sum_{ell,sign}(sign u_ell)_+^2 h_ell^sign(h_ell^sign)^T||<=C_d sum_{ell<q}|u_ell u_q|`. Choose `alpha/2<p<min(alpha,1)`; the normalized sum of each cross product tends to zero by `P(a_m^(-2)sum_i |U_iell U_iq|>epsilon)<=C epsilon^(-p)m^(1-2p/alpha)`. Each signed coordinate-square endpoint gives a positive beta-stable S. Different coordinate/sign endpoint categories have asymptotically disjoint jumps. The product categories also have disjoint one-row jumps: opposite signs of one coordinate cannot coincide, and two different coordinates sharing W have overlap `O(1/log m)` after multiplication by m. Product jumps and W endpoints, product jumps and U-square endpoints, and W and U endpoints have `o(1/m)` one-row overlap by the split-at-`L a_m` argument in `research/T384_orthogonal_initialization.md`. The product small-jump centered variance is `O(epsilon^(2-alpha))` and square small-jump mean is `O(delta^(1-beta))`; removing cutoffs makes the axis limits mutually independent, including N. The W-square marked-Poisson integral and the U-square endpoint integrals may be added jointly, so the initial normalized energy below is tight. The selected P mapping follows by small-z square truncation, mark truncation, and atomlessness of `F_j` and the gate marks.

For the 45-degree rotation in `../20261023T222120Z/agents/c01.md`, this recovers `F=(Z_0+Z_1,Z_0+Z_2)/sqrt(2)` and `C=(1/2)[[S_0+S_1,S_0],[S_0,S_0+S_2]]`; hence `C_12=S_0/2>0` almost surely. In general `b=C_12>=0`; if there is some coordinate ell with `x_{1,ell}x_{2,ell}>0`, then `b>0` almost surely, while if no such ell exists, `b=0` almost surely.

## Explicit unique hybrid candidate

Set `Q_0=C+diag(P_1,P_2)` and `r^0(t)=exp(-Q_0 t)r_0`, `J_j^0(t)=int_0^t r_j^0(s)ds`. Define

`tau=inf{t>0: sigma_j J_j^0(t)<0 for some j}`, with `inf empty=infinity`.

If `tau=infinity`, let `r(t)=r^0(t)` and `Q(t)=Q_0` for all `t>0`. If `tau<infinity`, the returning coordinate `j_*` is unique, `J_j*^0(tau)=0`, and `sigma_j* r_j*^0(tau)<0`. Let `Q_1=C+diag(P_1 1_{1!=j_*},P_2 1_{2!=j_*})`. Define

`r(t)=r^0(t)` for `t<=tau`, and `r(t)=exp[-Q_1(t-tau)]r^0(tau)` for `t>=tau`,

`Q(t)=Q_0` for `0<t<tau`, and `Q(t)=Q_1` for `t>=tau`.

Then `f(t)=y-r(t)` is continuous. The value assigned to Q at tau is a right-continuous convention; the theorem below uses L1, for which a single time has no effect. There is no second population loss: after the first return, the two residual signs are mixed and stay mixed, so the other cumulative residual remains in its initial direction while the returned one continues beyond zero. If `b=0`, or if the initial residual signs are mixed, then `tau=infinity`.

There is a simple criterion when the initial residual signs agree. The selected PPP masses `P_1,P_2` are strictly positive almost surely, so `Q_0=[[a,b],[b,d]]` is positive definite. Put `q=(|r_01|,|r_02|)`. The cumulative vector for the common sign has limit `Q_0^(-1)q=((d q_1-b q_2),(a q_2-b q_1))/(ad-b^2)`. A finite return occurs exactly when one of these two components is negative; that component identifies `j_*`. They cannot both be negative because `ad>b^2`. If a component is zero, its cumulative coordinate approaches zero from above as `t->infinity` and has no finite return. This criterion follows from the sign-cone/unimodality proof below; it is not an extra assumption.

## Theorem and topology

For every fixed `T<infinity`, jointly with the initialization variables above,

`f_m|_[0,T] => f|_[0,T]` in `C([0,T];R^2)`,

`K_m|_[0,T] => Q|_[0,T]` in `L^1([0,T];R^(2x2))`.

Equivalently, under an asymptotically exact coupling of the joint initialization array, `sup_{t<=T}||r_m(t)-r(t)||->0` and `int_0^T||K_m(t)-Q(t)||dt->0` in probability. At t=0, the separate initial-kernel limit includes *both* W-sign populations; this does not conflict with L1 convergence to the positive-time selected Q. At `tau<infinity`, several positive-mass endpoint atoms usually hit in a shrinking window near tau. Their individual jumps need not converge to the single jump of Q in `J_1`; no such assertion follows from this theorem.

### Step 1: tightness, monotone replacement, and a limit equation

Put `S_m=a_m^(-2)sum_i[W_i(0)^2+V_i1(0)^2+V_i2(0)^2]` and `R_m=||r_m(0)||`. Both are tight by the initialization lemma and stable-square tails. On `S_m<=K, R_m<=R`, the active vector `(W_i,(V_i1)_+,(V_i2)_+)` obeys the same symmetric star-matrix motion bound as in `research/T384_orthogonal_dynamics.md`: its norm is at most `e^(gamma_m RT)` times its initial norm, and its displacement at most `gamma_m RT e^(gamma_m RT)` times that norm. Consequently, uniformly on `[0,T]`,

`a_m^(-2)sum_i|W_i(t)^2-W_i(0)^2|=o(1)`, `||C_m(t)-C_m(0)||op=o(1)`,

`||K_m(t)||op<=e^(2gamma_m RT)S_m<=2K`, and `||r_m'(t)||<=2KR` almost everywhere.

Define the *initial-square gate clock* `B_j,m(t)=a_m^(-2)sum_i W_i(0)^2 1_{V_ij(t)>0}`. Then `sup_{t<=T}|A_j,m(t)-B_j,m(t)|=o_P(1)`. Each B is nonincreasing because gates absorb, and `0<=B_j,m(t)<=S_m`. Thus on every bounded-energy event, Helly's theorem makes `(B_1,m,B_2,m)` relatively compact in L1, while Arzela-Ascoli makes `(r_m,J_m)` relatively compact in C. Join these variables with S_m, the uniformly vanishing error variables, and the tight initialization tuple (including the marked endpoint process, whose finite compact truncations avoid intensity-bearing boundaries) and take an arbitrary subsequence, then a Skorokhod coupling of a further subsequence. Its limit has `F,C,N`, continuous `r,J` with `J'=r`, and nonnegative bounded nonincreasing A_j(t) defined almost everywhere. Passing to the integral residual equation gives

`r(t)=r_0-int_0^t [C+diag(A_1(s),A_2(s))]r(s)ds`.  (H)

No gate law has yet been assumed for A.

### Step 2: a two-dimensional sign-cone lemma valid for every subsequential A

Let `b=C_12>=0`, `a(t)=C_11+A_1(t)>=0`, and `d(t)=C_22+A_2(t)>=0`. Equation (H) reads `r_1'=-a(t)r_1-br_2`, `r_2'=-br_1-d(t)r_2`. If `b=0`, each residual keeps its initial sign. If `b>0`, each mixed-sign cone is invariant: for example, writing `p=r_1`, `q=-r_2` when `r_1>0,r_2<0` gives `p'=-a p+bq`, `q'=bp-dq`, a cooperative two-dimensional system with strictly positive p,q. From equal initial signs, the trajectory can remain in that orthant or one component can first hit zero. The other component cannot be zero at the same time, because a bounded linear ODE cannot carry nonzero initial r to the zero vector at finite time. At that first boundary, the vanishing component has derivative `-b` times the nonzero same-sign component and crosses *transversely* into a mixed-sign cone. The cone is then invariant, so no component can cross again. Multiplying r by `-1` covers two negative initial signs.

Therefore each `sigma_j J_j(t)` starts strictly increasing, can change monotonicity at most once, and can return to zero at most once. Every finite positive return is transverse: at a return `sigma_j r_j(t)<0`, and immediately thereafter `sigma_j J_j(t)<0`. There are no zero plateaus or nontransverse finite returns. At most one coordinate can return because at most one residual coordinate can reverse sign.

### Step 3: identify the gate clock from the marked endpoint atoms

The integrated motion formula is uniform in the row index. While an initially active gate has not hit zero,

`V_ij(t)=V_ij(0)+gamma_m W_i(0)J_j,m(t)+e_ij,m(t)`,

`sup_{i,j,t<=T}|e_ij,m(t)|<=gamma_m R T max_i sup_{s<=T}|W_i(s)-W_i(0)|`.

The star-matrix bound and `max_i||(W_i(0),h_i(0))||<=a_m sqrt(S_m)` make the right side `O(L_m^2/a_m)=o(1)` on the bounded-energy event. For a W-endpoint atom `z_i,m=W_i(0)/a_m` converging to `z!=0` with mark `u_i,m=U_i(0)` converging to u and `v_j=u dot x_j!=0`, the main displacement is `L_m z_i,m J_j,m(t)`.

In the Skorokhod coupling, `r_m->r` and `J_m->J` uniformly. If `v_j<0`, the gate was inactive and never activates. If `v_j>0` but `sgn(z)=-sigma_j`, then at every fixed positive t the initially positive `sigma_j J_j(s)` at some `s<t` makes `z_i,m J_j,m(s)` strictly negative; survival to s would force `V_ij(s)<0` for large m, impossible. Thus every opposing endpoint gate is dead at all positive macroscopic times. If `v_j>0` and `sgn(z)=sigma_j`, then before a cumulative return `tau_j`, `sigma_j J_j(s)>0` for all `0<s<=t`. Uniform convergence of r_m near zero preserves the initial residual sign there, while uniform convergence of J_m and a positive minimum preserve it on `[delta,t]`; hence `sigma_j J_j,m(s)>0` throughout `[0,t]` for large m. The main displacement is nonnegative, and the `o(1)` error cannot kill a gate with fixed `v_j>0`. If `t>tau_j`, the sign-cone lemma gives a prior s with `sigma_j J_j(s)<0`; the same survival contradiction kills it by t. At the single return time, pointwise gate convergence is not needed.

This atomwise reasoning is first applied on a compact truncation `xi<|z|<R`, `||u||<M`, with gate-mark cutoffs `|u dot x_j|>epsilon`; there are finitely many matched atoms and no limiting atom on the cut boundaries. For fixed xi, the probability of any omitted `|z|>R` atom is `O(R^(-alpha))`, and of an atom with `|z|>xi, ||u||>M` is `O(xi^(-alpha)P(||U||>M))`. Small gate marks have probability tending to zero as epsilon decreases because each projection has a continuous density. The remaining small-W square mass has the uniform bound

`limsup_m E[a_m^(-2)sum_i W_i(0)^2 1_{|W_i(0)|<=xi a_m}] <= C xi^(2-alpha)`;

the matching PPP expectation is `2alpha c xi^(2-alpha)/(2-alpha)`. Hence, first for the matched finite atoms and then by `R,M->infinity`, `epsilon,xi->0`, the B clocks converge in L1 to

`A_j(t)=P_j 1_{t<tau_j}` for almost every `t>0`, where `tau_j=inf{t>0:sigma_j J_j(t)<0}` and `inf empty=infinity`.

The limits at the one or two exceptional times `t=0,tau_j` do not affect L1. This is the point where absorption matters: once an atom is killed, it stays out even if the sign of J later changed; the sign-cone lemma rules out such a later change in the two-input limit anyway.

### Step 4: uniqueness of the identified limit

Before the first cumulative return, Step 3 makes `A_j=P_j` for both coordinates almost everywhere, so (H) has the unique solution `r^0(t)=e^(-Q_0t)r_0` up to that return. The sign-cone lemma shows this first return, if it exists, is the unique transverse return of the explicit `J^0`. At that time only one population disappears. Thereafter the other population stays at P and the returned population stays at zero; equation (H) has the unique solution with constant matrix `Q_1` displayed above. The mixed-sign cone prevents any second return. Thus every subsequential limit equals the explicit hybrid `(r,Q)`, a measurable function of `(F,C,N)`. Tightness and uniqueness of all joint subsequential limits give the stated `C x L1` weak convergence. The same argument yields convergence in probability under a coupling where the initialization primitives converge.

## Precise limitations and an independent localized proof route

The kernel convergence is `L1` over time. A positive-time fixed-time limit holds away from the random switch. For a supporting atom with fixed mark `v_j>0` and endpoint `z`, its hit requires `sigma_j J_j,m` near `-v_j/(L_m|z|)`. Uniform convergence of `J_m` and transversality show that each such death time converges to tau; they do **not** give an absolute `O(1/L_m)` error relative to limiting tau without a rate for `J_m-J`. Distinct endpoint atoms make distinct finite-width jumps that coalesce in the limit, so a `J1` claim at the switch needs separate analysis and is generally suspect. The output limit is uniform because integrating the bounded kernel over a shrinking switch window makes its effect vanish. The theorem is finite-width-then-fixed-T; it does not interchange `T->infinity` with `m->infinity` or identify discrete-GD training.

There is also a direct localized proof through a prescribed transverse first return, useful if one wants to avoid Helly. Let `tau` be such a return of `J^0`, choose `epsilon>0`, and use the safe-clock estimate from `../20261023T222120Z/agents/c01.md` on `[0,tau-epsilon]`. In `[tau-epsilon,tau+epsilon]`, bounded derivatives imply `J_j,m(tau+epsilon)-J_j(tau+epsilon)=o_P(1)+O(epsilon^2)`, whereas transversality gives `sigma_j J_j(tau+epsilon)=-kappa epsilon+O(epsilon^2)`. For small fixed epsilon, the actual cumulative residual is negative at `tau+epsilon`. The integrated gate formula then kills all initially supporting `|W|>xi a_m` atoms in the returned coordinate, except marks of size `Omega(xi epsilon L_m)`, whose union probability is `O(1/log m)`; initially opposing atoms died near zero. After `tau+epsilon`, absorption keeps its first-layer mass negligible. The other coordinate's positive cumulative margin closes a stopping-time bootstrap and retains its P population. The rate kernel is close to `Q_0` before `tau-epsilon` and to `Q_1` after `tau+epsilon`; the intervening kernel integral is bounded by `O(epsilon)`. Letting m grow and then epsilon shrink gives the same output-uniform and kernel-L1 result. This route requires a transverse candidate return as a hypothesis; the compactness/sign-cone argument above proves that every actual two-input subsequential return has this property and yields a global theorem.
