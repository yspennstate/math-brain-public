# Audit of the sensitivity/Sard argument for all finite `k`

## Verdict

**The proposed argument closes generic transversality and nonsimultaneity for every phase of the finite-`k` irreversible hybrid, conditional on the frozen random environment and an absolutely continuous initial residual.** I found no obstruction in the saltation, strict energy, Sard, or induction steps. It supplies precisely the later-phase ingredient missing from `agents/d04_transversality.md`. To promote this into a stochastic full-`k` training theorem, one must also state and prove the finite-ray joint initialization for the chosen `k` orthonormal inputs and write the finite-cutoff gate identification for `k` coordinates. The latter is a finite union of the argument in `reviews/d04_compactness.md`; the former is outlined, but not independently audited in full, in `agents/d01_hybrid.md` for two inputs.

## Fixed sign branch and a regular history chart

Condition on the environment `(C,N)` and restrict `p=r0` to an open sign orthant. All masses `P_j(sigma)` are then fixed numbers, independent of the magnitudes of `p`. For an active set `S`, set `Q_S=C+sum_(j in S) P_j e_j e_j^T`, symmetric positive definite. The candidate hybrid in the cumulative variable satisfies

`J'(t,p)=p-Q_S J(t,p)`, `J(0,p)=0`.       (1)

At a deletion of `j in S`, `J_j(tau,p)=0` and `Q_(S\{j})=Q_S-P_j e_j e_j^T`. Therefore the two vector fields agree *at the switching point*:

`p-Q_(S\{j})J(tau,p)=p-Q_S J(tau,p)`.       (2)

The identity (1) follows also from the residual formulation: initially `r=p-Q_S J`; it remains valid after deletion because the removed term is `P_jJ_j e_j=0` at the switch, then both sides solve the same next-phase equation.

Suppose the first `n` switches of a parameter `p_*` are distinct and transverse. Each switch time is locally analytic in `p` by the implicit-function theorem applied to its active clock `J_j(t,p)=0`, since `J_j'=r_j!=0`. On a compact interval before each switch, the other active clocks stay strictly on their initial sides, apart from the universal zero at `t=0` where `sigma_j J_j(t)=|p_j|t+O(t^2)` uniformly near `p_*`. Thus a sufficiently small parameter neighborhood preserves the earlier switch order, and the formulas for each completed phase are analytic there. These regular-history neighborhoods are the charts needed below. There are finitely many ordered switch histories and a countable subcover of the resulting parameter domains.

For a chart with `n` prior switches, continue its last constant matrix **virtually** to any `t>tau_n(p)`, even beyond what might become the next switch. This gives an open `(t,p)` domain and an analytic `J(t,p)` there; every actual next event in that chart lies among these virtual zeros. The sensitivity calculation below applies both before and during this virtual phase. One need not assume in advance that the next event is regular.

## Saltation and strict invertibility of the parameter sensitivity

Let `Z(t,p)=D_pJ(t,p)` on a regular-history chart, with its natural one-sided derivatives at prior switch times. Within a phase, differentiating (1) gives

`Z'=I-Q_S Z`, `Z(0)=0`.       (3)

At a previous transverse switch `tau(p)`, differentiate the identity `J^-(tau(p),p)=J^+(tau(p),p)` with respect to `p`. The terms involving `D_p tau` are the two phase vector fields at the switch, which cancel by (2). Thus `Z^+(tau,p)=Z^-(tau,p)`: the saltation matrix is exactly `I`. The piecewise solution of (3) is continuous through all earlier deletions. (The solution is also jointly `C^1` across a switching surface, since both its time derivative and parameter derivative match.)

For `v!=0`, put `z(t)=Z(t,p)v`. It solves `z'=v-Q_S z`, `z(0)=0`, and `z'(0)=v`. On a constant-matrix phase define

`E(t)=1/2 z(t)^T Q_S z(t)-v^T z(t)`.

Symmetry gives `E'=z'^T(Q_S z-v)=-||z'||^2`. At deletion of coordinate `j`, continuity of `z` and the diagonal drop of `Q` give

`E(tau+)-E(tau-)=-1/2 P_j z_j(tau)^2<=0`.       (4)

Because `z'(0)=v!=0`, the integral of `||z'||^2` is strictly positive on a short initial interval; thereafter `E` cannot increase, even at deletions. Hence `E(t)<0` for **every** `t>0`. If `Z(t,p)v=z(t)=0`, however, `E(t)=0`, a contradiction. Thus `Z(t,p)` is invertible at every positive time on every regular-history chart, including after arbitrarily many of its previous deletions. This argument does not need the phase matrices to commute or the parameter-to-switch-time derivatives to vanish.

## Sard for grazing and dimension for simultaneous zeros

For an as-yet-active coordinate `j` in a regular-history virtual phase, let `F_j(t,p)=J_j(t,p)`. Its parameter gradient is the nonzero row `e_j^T Z(t,p)`. Thus `M_j={F_j=0}` is a smooth `k`-dimensional hypersurface in the open `(t,p)` domain (`k+1` variables). Consider the projection `pi:M_j -> R^k`, `(t,p) |-> p`. At a point on `M_j`, its differential is surjective exactly when `partial_t F_j=r_j(t,p)!=0`: if that derivative is nonzero, any perturbation in `p` can be accompanied by a suitable perturbation of `t`; if it is zero, tangent parameter perturbations must lie in `ker(D_pF_j)`, a codimension-one subspace. Therefore the critical values of `pi` are precisely parameters for which the virtual phase has a grazing clock `J_j=r_j=0`. Sard's theorem makes this parameter set Lebesgue-null. `C^1` regularity suffices here because the source and target of `pi` both have dimension `k`; in fact the virtual-phase chart is analytic.

For distinct active `j,l`, the two parameter gradients `e_j^TZ` and `e_l^TZ` are independent rows of the invertible `Z`. Hence `{F_j=F_l=0}` is a smooth `(k-1)`-dimensional submanifold of `(t,p)` space. Its projection to `R^k` is null: cover it by countably many local Lipschitz charts and compact boxes. This excludes a simultaneous next event. No claim that two residual coordinates cannot vanish together is needed.

Induct on the number of previous deletions. At step zero there are no prior-chart conditions. Remove the null grazing and simultaneous parameter sets for each active coordinate/pair and each countable regular-history chart; outside their union the next event, if any, is unique and transverse. Its history extends to a regular chart for the next step. At most `k` distinct populations can be deleted. The finite induction and countable unions show that, for Lebesgue-almost-every `p` in a fixed sign orthant, **all** actual positive switching times are isolated, unique among coordinates, and transverse. They cannot accumulate in finite time because only `k` deletions are possible; zero initial coordinates are a separate null set. Finally integrate over the environment and sum the `2^k` sign orthants, using the independent density of `r0`, to obtain the almost-sure statement.

## Consequence for the network limit and remaining dependency

On this probability-one regular set, the hybrid has a unique finite sequence of at most `k` deletion times on every horizon. The compactness/gate proof can identify it inductively. Before the next candidate return, each still-active signed cumulative clock is strictly positive on compact subintervals, so its supporting endpoint gates survive and opposing gates have died in the initial layer. At a unique transverse return, that clock is strictly negative a fixed time later, so its macroscopic supporting population is absorbed in a shrinking window; all other active clocks have positive margins at the event. The uniformly bounded kernel makes the window's contribution to the residual equation vanish. Repeat after deletion. This produces uniqueness of each subsequential `L^1` kernel and uniform output limit, without the special two-dimensional mixed-sign cone. It allows multiple switches, as the deterministic example in `agents/d04_transversality.md` illustrates.

The deduction is **conditional** on a joint initialization `(F,C,N)` with `F` independent of `(C,N)`, a full-dimensional density for `F`, and positive-definite `C`, plus the finite-`k` energy and endpoint-cutoff estimates. For fixed `k<=d` orthonormal inputs, the finite-coordinate ray decomposition strongly suggests these ingredients and the energy estimate is dimension-free up to fixed constants, but this review certifies the sensitivity/Sard closure, not an unwritten `k`-ray initialization proof. The theorem should retain the `C([0,T]) × L^1([0,T])` topology; coalescing gate deaths still obstruct a general kernel `J_1` claim.
