# T384: global finite-`k` orthonormal-input absorbing hybrid limit

**PROVED (internal).** Independently audited in reviews/d02_k_input_review.md, with the sensitivity/Sard step independently audited in reviews/d04_sensitivity_review.md. Reviewer-requested presentation repairs are incorporated below.

**Theorem.** Fix `k<=d<infinity`, orthonormal inputs `x_1,...,x_k in R^d`, `0<alpha<2`, and a deterministic target `y in R^k`. Initialize all hidden coordinates and output weights independently as standard symmetric `alpha`-stables. Train both layers by continuous squared-loss gradient flow at multiplier `(log m)^(2/alpha)`, and absorb each ReLU input gate when its preactivation first reaches zero. Put `a_m=m^(1/alpha)`, `L_m=(log m)^(1/alpha)`, and `b_m=a_m L_m`. Explicitly, `f_m(t)=b_m^(-1)sum_i W_i(t) h_i(t)`, where `h_i(t)=((U_i(t) dot x_j)_+)_j`, and the loss is `||y-f_m||^2/2`; there are no biases. On every fixed finite horizon, the output converges in `C([0,T];R^k)` and the rate-scaled kernel converges in `L^1([0,T];R^(k x k))` to the finite-switch hybrid process defined below. At most `k` positive-time population deletions occur. Almost surely they are distinct and transverse. This result is restricted to **fixed finite `k,d`, orthonormal inputs, continuous time, and absorbing gates**. It makes no kernel `J_1` assertion at a deletion.

The new point beyond the two-input cone argument is an energy proof that the sensitivity `Z(t)=partial J(t)/partial r_0` is invertible along every regular deletion history. This proves that later grazing and simultaneous returns, as well as the first ones, have probability zero. The smooth-chart/Sard argument is needed: simply conditioning on a previous random switching time would be invalid.

## Joint initial primitives and their law

Let `v_ell=(x_{1,ell},...,x_{k,ell}) in R^k`, `h_ell^+=(v_ell)_+`, `h_ell^-=(-v_ell)_+`, with positive parts coordinatewise, `ell=1,...,d`. Let `c=Gamma(alpha)sin(pi alpha/2)/pi`, `beta=alpha/2`. Independently over `(ell,sign)`, take symmetric variables `Z_ell^sign` with characteristic function `exp[-c|s|^alpha]` and positive variables `S_ell^sign` with Laplace transform `exp[-c Gamma(1-beta)s^beta]`. All `Z`, `S`, and the following marked Poisson measure `N` are independent:

`N(dz,du)` has intensity `alpha c |z|^(-1-alpha) dz product_(ell=1)^d P_U(du_ell)` on both nonzero `z` half-axes.

The initial output, frozen second-layer Gram matrix, initial residual, and selected first-layer masses are

`F=sum_(ell,sign) h_ell^sign Z_ell^sign`,

`C=sum_(ell,sign) S_ell^sign h_ell^sign(h_ell^sign)^T`,

`r_0=y-F`, `sigma_j=sgn(r_0j)`,

`P_j=int z^2 1_{u dot x_j>0, sigma_j z>0} N(dz,du)`.             (1)

The joint finite-width initialization `(f_m(0),C_m(0),N_m,(P_j,m)_j)` converges to `(F,C,N,(P_j)_j)` (with vague point-process topology on `N_m=sum_i delta_(W_i(0)/a_m,U_i(0))`). In particular, `F` is independent of `(C,N)`; the selected `P` is sign-dependent and is not asserted independent of `F`. Almost surely `C` is positive definite, `0<P_j<infinity`, and each `r_0j!=0`. The exact transforms, for `t in R^k` and PSD `Lambda`, are

`E exp(i t dot F)=exp[-c sum_(ell,sign)|t dot h_ell^sign|^alpha]`,

`E exp[-tr(Lambda C)]=exp[-c Gamma(1-beta) sum_(ell,sign)((h_ell^sign)^T Lambda h_ell^sign)^beta]`.       (2)

Here is the finite-`k` extension of the initialization proof in `d01_hybrid.md` and `research/T384_orthogonal_initialization.md`. Write `H(u)=((u dot x_j)_+)_j` and `Psi(u)=sum_(ell,s in {+1,-1})(s u_ell)_+ h_ell^s`. The ReLU Lipschitz bound gives `||H(u)-Psi(u)||<=C_(d,k) M_2(u)`, where `M_2` is the second-largest `|u_ell|`, defined as zero when d=1 (the ray reduction is then exact). As `P(M_2(U)>s)=O(s^(-2alpha))`, `E[M_2(U)^alpha]<infinity`; conditioning on the U rows makes the normalized W-weighted remainder an alpha-stable sum with scale `O_P((log m)^(-1/alpha))`. The Gram remainder is bounded by `C_(d,k) sum_(ell<q)|u_ell u_q|`, and its `a_m^(-2)` sample sum vanishes using any `alpha/2<p<min(alpha,1)`. Thus the output and Gram reduce to finitely many signed coordinate-ray product/square categories. Their rare product jumps, coordinate-square endpoints, and marked W endpoints have negligible one-row overlap; truncating small product jumps by centered variance and small square jumps by their mean gives mutually independent ray limits and `N` exactly as in the cited joint initialization argument. Since `h_ell^+ - h_ell^-=v_ell` and the rows `v_ell` span `R^k`, the ray vectors span `R^k`. Every `S_ell^sign>0` almost surely, giving `C>0`. The characteristic exponent of `F` dominates `c_*||t||^alpha` by compactness of the unit sphere, so `F` has a bounded continuous full-dimensional density. Each selected `P_j` is finite by square-integrability of the PPP near zero and has infinitely many eligible small atoms; hence it is positive. Boundary atoms `u dot x_j=0` and residual sign ties have probability zero, validating selection in (1).

## The explicit hybrid, including a continuous integrated-residual field

Initially all coordinates are active. On a phase with active set `S subset {1,...,k}`, define

`A_j=P_j 1_{j in S}`, `Q_S=C+diag(A)`, `J'=r`, `r'=-Q_S r`, `J(0)=0`, `r(0)=r_0`.       (3)

Keep an active coordinate `j` so long as `sigma_j J_j>0` after the initial instant. Delete it irreversibly at its first positive return to zero followed by `sigma_j J_j<0`. In a regular history each such return has `sigma_j r_j(tau)<0`; simultaneous returns are absent. Continue (3) with the reduced active set. Thus no coordinate can be deleted twice and there are at most `k` deletions. If a phase begins at `t_s`, its explicit continuation is

`r(t)=exp[-Q_S(t-t_s)]r(t_s)`,

`J(t)=J(t_s)+Q_S^(-1)(I-exp[-Q_S(t-t_s)])r(t_s)`.       (4)

The kernel limit is `Q(t)=Q_S` at positive times between deletion times; its value at any switch is immaterial in `L^1`. The limiting output is `f=y-r`. At `t=0`, the separately convergent finite-width kernel has law `C+diag(D_j)`, `D_j=int z^2 1_{u dot x_j>0}N(dz,du)`; it includes **both** W-sign populations and need not equal `Q(0+)`.

There is a useful exact global conservation identity:

`r(t)+[C+diag(A(t))]J(t)=r_0`, hence `J'(t)=r_0-Q(t)J(t)`.       (5)

Indeed, on a phase, `d(r+CJ+diag(A)J)=0`. At a deletion of coordinate `j`, `A_j` falls by `P_j` exactly when `J_j=0`, so `diag(A)J` has no jump. This proves (5) globally. The vector fields immediately before and after the switch agree on its surface: `Q_before J-Q_after J=P_j e_j J_j=0`. Thus `J` is `C^1` across switches, while `r'=J''` and `Q` generally jump.

## Invertible sensitivity and almost-sure regularity of *all* switches

Fix a realized environment `(C,N)` and an initial-residual orthant. Its `P_j` are then fixed, independent of variation of `r_0` inside that orthant. Consider a chart on which the first `s` deletion indices are prescribed, previous times are finite, distinct, transverse, and no earlier return intervenes. The implicit function theorem applied to each preceding equation `J_(j_l)(tau_l;r_0)=0`, with time derivative `r_(j_l)(tau_l)!=0`, makes its `tau_l(r_0)` smooth (indeed real analytic). Use (4) to extend the `s`-th phase analytically to every `t>tau_s(r_0)` even if a *future* gate would be deleted; this extension is only a device for detecting the next zero. Countably many local charts cover all regular finite histories.

On such a chart let `Z(t)=D_(r_0)J(t;r_0)`. The switch saltation for `J` is the identity, since the vector fields `r_0-Q_before J` and `r_0-Q_after J` coincide at `J_j=0`. In particular, `Z` is continuous across each previous switch and satisfies

`Z(0)=0`, `Z'=I-Q(t)Z` on each open phase.       (6)

The dependence of the preceding switch times has **not** been discarded: it cancels from the saltation term because the two vector fields agree on the switching surface. To show `Z(t)` is invertible for every `t>0`, fix `v!=0`, put `z(t)=Z(t)v`, and define the phasewise energy

`E_v(t)=1/2 z(t)^T Q(t) z(t)-v^T z(t)`.       (7)

On open phases `z'=v-Qz` and `E_v'=(Qz-v)^Tz'=-||z'||^2`. At deletion of `j`, `Q` changes to `Q-P_j e_j e_j^T` while `z` stays continuous, so `E_v(tau+)-E_v(tau-)=-P_j z_j(tau)^2/2<=0`. Since `z'(0)=v`, the integral of `||z'||^2` is strictly positive on every interval beginning at zero. Hence `E_v(t)<0` for all `t>0`; if `Z(t)v=0`, (7) would instead give zero. This contradiction proves **`det Z(t)!=0` on all regular-history phase extensions**, including their switching endpoints. Positive definiteness of `Q` follows from `C>0`; the strict-energy argument itself uses its symmetry and the PSD direction of each deletion.

For each surviving `j` on a phase extension define `H_j(r_0,t)=J_j(t;r_0)`. Its spatial gradient is the nonzero row `e_j^T Z(t)`. Consequently the zero set `{H_j=0}` is a smooth `k`-dimensional hypersurface in the `(r_0,t)` chart. Project it to `r_0`. Its projection is critical exactly when `partial_t H_j=r_j=0`: to see this, tangent vectors obey `D_(r_0)H_j delta r+r_j delta t=0`, so the projection is onto all `delta r` precisely when `r_j!=0`. Sard's theorem (smooth equal-dimensional projection, covered by countably many charts) says the set of `r_0` admitting a phase grazing `J_j=r_j=0` is Lebesgue null. For `j!=l`, the spatial gradients `e_j^TZ,e_l^TZ` are independent because `Z` is invertible; `{H_j=H_l=0}` has dimension `k-1` in `(r_0,t)` and its projection is Lebesgue null. This excludes simultaneous phase returns. These arguments include any later phase, despite its switch times depending on `r_0`.

At an endpoint `t=tau_s(r_0)` of a previous phase, another surviving `j` could share a zero only on a null set. If the deleted index is `l`, implicit differentiation gives `D tau_s=-e_l^T Z(tau_s)/r_l(tau_s)`, so

`D_(r_0)[J_j(tau_s(r_0);r_0)]
 =e_j^T Z(tau_s)-[r_j(tau_s)/r_l(tau_s)]e_l^T Z(tau_s) !=0` for `j!=l`.       (8)

Thus that endpoint collision is a hypersurface in parameter space. The same argument, or the interior simultaneous-zero argument on the preceding phase, removes it. At the origin `r_0j!=0`, so `sigma_j J_j(t)>0` for small positive `t`. Inductively, outside the countable union of these null sets, every first zero of a surviving cumulative coordinate after a prior switch is isolated, unique among coordinates at that time, and has nonzero derivative. Since it was positive before its first zero, that derivative necessarily has `sigma_j r_j<0`. It therefore triggers the prescribed deletion. With at most `k` indices, the induction stops. For each fixed `T`, an event exactly at `T` is null as well: within a phase `D_(r_0)J_j(T)=e_j^TZ(T)!=0`, and for `T=tau_s(r_0)` the gradient of the transverse switching time is `-e_l^TZ/r_l!=0`.

Finally, condition on `(C,N)` and split the residual into its finitely many sign orthants. Because `F` is independent of `(C,N)` and has a density, the conditional residual law in each orthant is absolutely continuous. Every deterministic null set just proved has conditional probability zero. This proves that the hybrid is almost surely regular on each fixed finite horizon. Taking the intersection over integer horizons makes all finite-time switches regular simultaneously, without assuming generic entries of `C` or independence of the selected `Q` and `r_0`.

## Identification from the actual finite-width absorbing dynamics

For `V_ij=U_i dot x_j`, `h_i=((V_ij)_+)_j`, `gamma_m=L_m/a_m`, the exact equations away from hits are

`V_ij'=gamma_m W_i r_j,m 1_{V_ij>0}`, `W_i'=gamma_m sum_j r_j,m(V_ij)_+`,

`r_m'=-K_m r_m`, `K_m=C_m+diag(A_1,m,...,A_k,m)`,

`A_j,m=a_m^(-2)sum_i W_i(t)^2 1_{V_ij(t)>0}`,

`C_m=a_m^(-2)sum_i h_i(t)h_i(t)^T`.       (9)

The first-layer kernel is diagonal exactly because the training inputs are orthonormal. `K_m` is PSD and `||r_m(t)||<=||r_m(0)||`. Put `S_m=a_m^(-2)sum_i(W_i(0)^2+sum_j V_ij(0)^2)`, a tight sequence. On `S_m<=K,||r_m(0)||<=R`, the symmetric row-motion bound gives `sup_t||K_m(t)||<=2K` for large m and

`sup_t||C_m(t)-C_m(0)||=o(1)`,

`sup_t a_m^(-2)sum_i|W_i(t)^2-W_i(0)^2|=o(1)`.       (10)

Define the monotone initial-square clock `B_j,m(t)=a_m^(-2)sum_i W_i(0)^2 1_{V_ij(t)>0}`. Then `sup_t|A_j,m-B_j,m|=o_P(1)`. Each B is nonincreasing and bounded by `S_m`. Helly's `L^1` compactness, Arzela-Ascoli for `(r_m,J_m)`, and joint tightness of the initial primitives together with S_m, the uniformly vanishing error variables, and every finite truncated marked-endpoint configuration yield, from any subsequence, a further coupled subsequence with uniform `r_m,J_m` convergence and `L^1` convergence of B to some nonnegative nonincreasing `A_j`. The limit obeys

`J'=r`, `r(t)=r_0-int_0^t [C+diag(A(s))]r(s)ds`.       (11)

The gate formula identifies A away from zero-clock touches. Uniformly in rows, while an initially positive gate survives,

`V_ij(t)=V_ij(0)+gamma_m W_i(0)J_j,m(t)+e_ij,m(t)`,

`sup_(i,j,t<=T)|e_ij,m(t)|=O_(K,R,T)(L_m^2/a_m)=o(1)`.       (12)

For a matched W-endpoint atom `(W_i(0)/a_m,U_i(0))->(z,u)` with `z!=0` and `u dot x_j>0`, the main displacement is `L_m z J_j,m`. An initially opposing atom (`sigma_j z<0`) dies at every fixed positive time, using the initial positive excursion `sigma_j J_j>0`. An initially supporting atom (`sigma_j z>0`) remains alive up to `t` if `sigma_j J_j(s)>0` for all `0<s<=t`; uniform clock convergence, positivity near zero from `r_0j!=0`, and (12) establish this. If `sigma_j J_j(s)<0` at any prior `s<t`, the supporting atom has died by `t` and cannot reactivate. The initially inactive gate remains inactive. Truncate first to finitely many atoms `xi<|z|<R`, compact U marks away from `u dot x_j=0`. The omitted `|z|<=xi` square mass is at most `O_P(xi^(2-alpha))`, uniformly in m; the large-z and large-mark tails vanish after `R,M->infinity`. Therefore, with A represented by its monotone version and in particular for almost every time within the stated strict-sign regions,

`A_j(t)=P_j` whenever `sigma_j J_j(s)>0` for every `0<s<=t`,

`A_j(t)=0` whenever `sigma_j J_j(s)<0` for some `0<s<t`,             (13)

and (13) holds almost everywhere over open intervals of those types. It deliberately makes no assertion after a tangential zero with no negative excursion. This is the only potential obstruction to identifying a general subsequential solution.

On the almost-sure regular environment and residual established above, that obstruction cannot affect the limit. Initially the explicit hybrid has `sigma_j J_j>0` until its first transverse return. Equation (13) and uniqueness of the constant-coefficient ODE (11) force any subsequential limit to equal the first explicit phase up to that return. More formally, work on compact intervals inside the strict-positivity region and use a first-exit continuation argument; equality near zero follows from `r_0j!=0`. At the return, equality and continuity give the same `J,r`. Immediately afterward the returned coordinate has a strict negative excursion, so (13) fixes its clock to zero permanently; every other active coordinate retains a strict positive clock until its own candidate return. ODE uniqueness then forces the next explicit phase. Repeating at most `k` times gives `r,J` equal to (3)--(4) and `A_j(t)=P_j 1_{j active at t}` almost everywhere. Hence every coupled subsequential limit is the same measurable hybrid function of `(F,C,N)`; (10) identifies `K_m->Q` in `L^1`, while uniform convergence of r identifies the output in `C`. This proves the theorem jointly with the initial primitives.

For an individual matched endpoint atom, (12) locates death at a negative threshold of magnitude `|u dot x_j|/(L_m|z|)`, up to vanishing gate error. This gives convergence of its death time to a transverse macroscopic return, **not** an absolute `O(1/L_m)` error relative to that return without a rate for `J_m-J`. Distinct endpoint jumps generally coalesce at the same macroscopic deletion, so `L^1` is the warranted kernel topology here. The theorem is for each fixed T; it does not exchange training time tending to infinity with width tending to infinity.

Standard theorem citation for the critical-value step: Arthur Sard, The measure of the critical values of differentiable maps, Bull. Amer. Math. Soc. 48 (1942), 883–890; original text read at https://webhomes.maths.ed.ac.uk/~v1ranick/papers/sard.pdf . See LITERATURE.md for model scope and external priority limits.
