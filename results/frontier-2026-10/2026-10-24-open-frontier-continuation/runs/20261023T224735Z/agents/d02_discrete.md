# T384: scalar critical-step Euler boundary and macroscopic limit

**Status:** A full scalar discrete-GD theorem, proved below from the established joint initialization in `research/T384_marked_PPP.md`. It extends the one-step note `runs/20261023T222120Z/agents/c02.md`. The proof handles negative Euler gate overshoot exactly. It is internal and independently reviewed in reviews/d03_discrete_review.md. It does not address interacting inputs.

## Model and result

Fix `0<alpha<2`, a deterministic scalar label `y`, `gamma>0`, and one training input `x=1`. Initialize all `(W_i,U_i)` as independent standard symmetric `alpha`-stable variables. Write

`L_m=(log m)^(1/alpha)`, `a_m=(m log m)^(-1/alpha)`, `beta_m=m^(-1/alpha)L_m`, `h_m=gamma/L_m`.

At integer step `n`, use the simultaneous explicit update

`U_{i,n+1}=U_{i,n}+d_n W_{i,n}1_{U_{i,n}>0}`,

`W_{i,n+1}=W_{i,n}+d_n(U_{i,n})_+`, `d_n=h_m beta_m r_n=gamma m^(-1/alpha)r_n`,

`f_n=a_m sum_i W_{i,n}(U_{i,n})_+`, `r_n=y-f_n`,

`H_n=m^(-2/alpha)sum_i[W_{i,n}^2 1_{U_{i,n}>0}+(U_{i,n})_+^2]`.

An inactive neuron is unchanged at every later step, including when a step lands at a **negative** hidden value. Set `F_m=f_0`, `C_m=m^(-2/alpha)sum_i(U_{i,0})_+^2`, and define `A_m,B_m,Q_m` as in `research/T384_SCALAR_LIMIT.md`: `Q_m=C_m+A_m` for `r_0>0` and `Q_m=C_m+B_m` for `r_0<0`. At `r_0=0`, choose any `Q_m`, since the trajectory is stationary.

Let `(F,C,N)` be the mutually independent stable-output, positive-stable hidden-square, and marked endpoint-PPP joint limit from `research/T384_marked_PPP.md`. Put `r=y-F` and

`K(s)=C+sum_{(z,u) in N}z^2 1_{u>0,u+r z s>0}`.

The following two statements hold.

**Critical boundary grid.** For every finite `S`, define the held processes on `0<=s<=S` by

`K_m^E(s)=H_{floor(s/gamma)}` and `P_m^E(s)=L_m[f_{floor(s/gamma)}-F_m]`.

Then, in `R^2 x D([0,S])^2` with `J_1` topology on the path coordinates,

`(F_m,C_m,K_m^E,P_m^E) => (F,C,K_gamma,P_gamma)`, where

`K_gamma(s)=K(gamma floor(s/gamma))`,

`P_gamma(s)=r int_0^{gamma floor(s/gamma)} K(v)dv`. **(1)**

All jumps of these held paths are at the deterministic mesh points; equivalently, convergence holds jointly for the finite vector of all mesh values on `[0,S]`. The limiting output update over each step is the **area** of the continuous boundary kernel across that cell, whereas the held kernel waits until the end of the cell to change. The one-step law in `c02.md` is the first cell of (1).

**Macroscopic scalar GD.** For every finite physical-time `T` and every `0<delta<T`,

`sup_{0<=t<=T}|r_{floor(t/h_m)}-r_0 exp(-Q_m t)| ->_P 0`, **(2)**

`sup_{delta<=t<=T}|H_{floor(t/h_m)}-Q_m| ->_P 0`. **(3)**

Consequently the held output converges jointly with its initialization to the **same** random continuous limit as scalar gradient flow:

`f_{floor(t/h_m)} => y-(y-F)exp(-Qt)` in `D([0,T])` with `J_1`, with `Q` independent of `F` and Laplace transform `E exp(-lambda Q)=exp[-(3c_alpha/2)Gamma(1-alpha/2)lambda^(alpha/2)]`. Linear interpolation of the discrete outputs converges in `C([0,T])`. As before, `H_0=>Q+D` while (3) tends to `Q` on every positive-time interval; no usual `D([0,T])` kernel limit retaining both values is asserted.

## Step identity and a uniform good event

The pivotal exact identity is a ReLU secant formula. For one active neuron, let `u=U_{i,n}>0`, `w=W_{i,n}`, and `d=d_n`. Along the straight update segment, `g(theta)=(w+theta d u)(u+theta d w)_+`. Its derivative exists almost everywhere and is

`g'(theta)=d 1_{u+theta d w>0}(u^2+w^2+2theta d u w)`.

Since `a_m beta_m=m^(-2/alpha)`, summing its integral gives the **exact** residual recurrence

`r_{n+1}=r_n(1-h_m J_n)`, **(4)**

`J_n=m^(-2/alpha)sum_{i:U_{i,n}>0} int_0^1 1_{U_{i,n}+theta d_n W_{i,n}>0}`

`       [U_{i,n}^2+W_{i,n}^2+2theta d_n U_{i,n}W_{i,n}]dtheta`. **(5)**

Let `S_n=m^(-2/alpha)sum_i(U_{i,n}^2+W_{i,n}^2)`. For `|d_n|<1`, the integrand bracket is between `(1-|d_n|)(u^2+w^2)` and `(1+|d_n|)(u^2+w^2)`. Hence `0<=J_n<=(1+|d_n|)S_n`. Also each active pair is multiplied by the matrix `[[1,d_n],[d_n,1]]`, while each inactive pair is fixed, so

`S_{n+1}<=(1+|d_n|)^2S_n`. **(6)**

Both `F_m` and `S_0` are tight. Fix `R,K,T` and work on `G_m(R,K)={|r_0|<=R,S_0<=K}`. Write `D_{m,n}=sum_{j<n}|d_j|` and let `D_m` be its value at the last step through `T+h_m`. For all sufficiently large `m`, induction using (4)–(6) shows, uniformly through `n h_m<=T+h_m`,

`sgn(r_n)=sgn(r_0)`, `|r_n|<=|r_0|<=R`,

`D_{m,n}<=D_m<=beta_m R(T+2h_m)=o(1)`,

`S_n<=exp(2D_m)S_0<=2K`, `0<=h_m J_n<=1/2`. **(7)**

If `r_0=0`, all updates vanish and the sign assertion is read as stationarity. The induction is noncircular: assume the sign and magnitude through step `n`, use the energy bound from prior steps to get `h_mJ_n<1/2`, then (4) preserves the sign and decreases the magnitude. A coordinate's total movement before it becomes inactive, followed by no movement afterward, also gives

`|U_{i,n}-U_{i,0}| vee |W_{i,n}-W_{i,0}| <=(e^{D_m}-1)(U_{i,0}^2+W_{i,0}^2)^(1/2)`.

Consequently, with `g(D)=2(e^D-1)+(e^D-1)^2`, uniformly over `n h_m<=T`,

`m^(-2/alpha)sum_i|W_{i,n}^2-W_{i,0}^2|<=g(D_m)S_0=o_P(1)`,

`|m^(-2/alpha)sum_i(U_{i,n})_+^2-C_m|<=g(D_m)S_0=o_P(1)`. **(8)**

The second bound uses the 1-Lipschitz positive-part map. These estimates include crossing steps and their genuine negative overshoots.

## Exact gate threshold and boundary-grid proof

On the good event with `r_0 ne 0`, put `sigma=sgn(r_0)`, `V_{i,n}=sigma W_{i,n}`, and `q_n=|d_n|`. While an initially active neuron remains active, its `(U,V)` vector is multiplied by `[[1,q_n],[q_n,1]]`. These matrices commute. Since `q_n<1`, define

`Theta_n=sum_{j<n} artanh(q_j)`, `rho_n=prod_{j<n}(1-q_j^2)^(1/2)`.

The virtual unabsorbed coordinate is `rho_n[U_{i,0}cosh Theta_n+sigma W_{i,0}sinh Theta_n]`. An initially active supporting neuron (`sigma W_{i,0}>=0`) never dies. An opposing neuron can cross zero only if `|W_{i,0}|>U_{i,0}`; once its virtual coordinate becomes nonpositive, it stays nonpositive as `Theta` increases. The actual Euler neuron freezes at its first nonpositive coordinate (possibly **strictly negative**), so for every integer `n` its **exact active indicator** is

`1_{U_{i,n}>0}=1_{U_{i,0}>0}1_{U_{i,0}+sigma W_{i,0}tanh(Theta_n)>0}`. **(9)**

No fictitious restart from zero or negative overshoot is used in (9).

Fix a boundary horizon `S` and let `J=floor(S/gamma)`, a number independent of `m`. From (4), (7), and `h_m J=S/L_m+O(h_m)`, one has `max_{j<=J+1}|r_j-r_0|=O_P(L_m^(-1))`. Since `q_j=gamma m^(-1/alpha)|r_j|`, Taylor expansion at zero yields, jointly for the finite list `0<=n<=J+1`,

`m^(1/alpha)tanh(Theta_n)=gamma sum_{j<n}|r_j|+o_P(1)=n gamma |r_0|+o_P(1)`. **(10)**

By (8)–(10), simultaneously at all boundary mesh values,

`H_n=C_m+sum_i (W_{i,0}/m^(1/alpha))^2`

`       1_{U_{i,0}>0,U_{i,0}+sigma W_{i,0}tanh(Theta_n)>0}+o_P(1)`. **(11)**

The marked PPP convergence, joint with `(F_m,C_m)`, sends (11) to `(K(n gamma))_{n<=J}`. For completeness, keep `|W_{i,0}|/m^(1/alpha)>epsilon`: there are finitely many matched endpoint atoms, and their marks almost surely avoid `u=0` and each grid threshold `u+n gamma r z=0`. Large `|z|` and large marks are removed by finite-atom tightness. The discarded first-layer mass is bounded uniformly in `n` by the initial `|z|<=epsilon` square mass plus the `o_P(1)` drift in (8); its expectation is `O(epsilon^(2-alpha))`. The analogous Poisson bound vanishes as `epsilon` decreases. This proves **joint**, not merely marginal, kernel-grid convergence.

For the output-grid vector, the exact step expansion, with `z_{i,n}=W_{i,n}/m^(1/alpha)` and `b_n=gamma r_n`, is

`L_m(f_{n+1}-f_n)`

`=sum_{i:U_{i,n}>0} z_{i,n}[(U_{i,n}+b_n z_{i,n})_+-U_{i,n}]`

`  +b_n m^(-2/alpha)sum_{i:U_{i,n}>0}U_{i,n}(U_{i,n}+b_n z_{i,n})_+`. **(12)**

The second sum without `b_n` differs from `m^(-2/alpha)sum_i(U_{i,n})_+^2` by at most `|b_n|m^(-1/alpha)S_n/2`; using (8) and `r_n-r_0=o_P(1)` over the fixed grid, its contribution tends to `gamma r C`. For each fixed retained endpoint atom `(z,u)`, (9)–(10), the active hyperbolic formula, and the fact `rho_n->1` give `z_{i,n}->z` and, if still active, `U_{i,n}->u+n gamma r z`. If the neuron died earlier, it remains inactive and both adjacent positive parts of the limiting virtual coordinate are zero. Thus the first sum in (12) tends to

`sum_{(z,u) in N:u>0} z[(u+(n+1)gamma r z)_+-(u+n gamma r z)_+]`. **(13)**

The small-initial-`|z|` part of (12)'s first sum is bounded by `gamma |r_n|sum_{small}|z_{i,n}|^2`; (8) bounds this by `gamma R` times the vanishing initial small-square mass plus `o_P(1)`. The Poisson version is absolutely summable. Summing (13) across `n=0,...,j-1` telescopes, while the `C` term contributes `j gamma r C`. The ReLU fundamental theorem of calculus then identifies

`L_m(f_j-F_m) => r int_0^{j gamma}K(v)dv` jointly for all `j<=J`.

Because the held paths have the **same fixed finite set of jump times** `gamma,2gamma,...`, convergence of their joint height vector implies (1) in `J_1` (indeed under a finite-grid coupling their uniform path distance tends to zero). The actual gate overshoot only determines that a dead neuron cannot return; no continuous-time gate-hit interpolation was silently imposed.

## Positive-time kernel loss and macroscopic residual proof

We now allow `n` up to `T/h_m`, of order `L_m`. Work first on `G_m(c,R,K)={c<=|r_0|<=R,S_0<=K}` for fixed positive `c,R,K`. By (7), `J_n<=3K` for large `m`. Since `h_mJ_n<=1/2`, (4) and `1-x>=exp(-2x)` for `x<=1/2` give

`|r_n|>=c exp[-6K(T+h_m)]` for `n h_m<=T+h_m`. **(14)**

For all mesh times `n h_m>=delta>0`, (14) implies

`Theta_n>=sum_{j<n}q_j=beta_m h_m sum_{j<n}|r_j|>=beta_m c delta exp[-6K(T+h_m)]`.

Also `Theta_n<=beta_m R(T+h_m)(1+o(1))=o(1)`, so `tanh Theta_n>=Theta_n/2` for large `m`. If an opposing neuron with `|W_{i,0}|>=epsilon m^(1/alpha)` remains active at such a time, (9) forces

`U_{i,0}>|W_{i,0}|tanh Theta_n >= const(c,K,T,delta) epsilon L_m`.

Independence and stable-tail bounds give the unconditional union estimate

`P(exists i: |W_{i,0}|>=epsilon m^(1/alpha), U_{i,0}>const epsilon L_m)=O_{c,K,T,delta,epsilon}(1/log m)`. **(15)**

The normalized squared mass of opposing neurons with smaller initial `|W|` has expectation `O(epsilon^(2-alpha))`. First let `m` grow, then `epsilon` decrease. Since this opposing mass is nonincreasing in `n`, (15) removes it **uniformly** for `n h_m>=delta`. Supporting-sign neurons remain active, and (8) freezes their squared output weights and the whole second-layer kernel. Therefore, on the good event and then unconditionally by tightness and the atomlessness of the stable limit of `F_m`,

`sup_{delta<=n h_m<=T}|H_n-Q_m|->_P0`. **(16)**

The lower cutoff `c` is removable because `F_m=>F` with a continuous density, so `lim_{c downarrow 0}limsup_m P(|r_0|<c)=0`; `R,K` are removed by tightness. Equation (16) implies (3) for held time, using `delta/2` to absorb the floor at the left endpoint.

It remains to show that crossing a gate within a finite Euler step does not alter the macroscopic residual exponent. Let `X_n={i: U_{i,n}>0, U_{i,n+1}<=0}`. Comparing the secant (5) with the pre-step kernel gives the deterministic bound

`|J_n-H_n|<=|d_n|S_n+m^(-2/alpha)sum_{i in X_n}(W_{i,n}^2+U_{i,n}^2)`. **(17)**

Every neuron belongs to at most one `X_n`, including a neuron that overshoots to a negative value. Each crossing-time squared norm is at most `exp(2D_m)` times its own initial squared norm, by (6). Thus, uniformly through `T`,

`h_m sum_n|J_n-H_n|<=h_m exp(2D_m)S_0+(T+h_m) sup_n|d_n|sup_nS_n=o_P(1)`. **(18)**

This is the discrete counterpart of controlling the vanishing initial layer. The exact crossing discrepancy may be order one at the **first** step, as `c02.md` proves, but each initial neuron pays it only once, and the time integral multiplies it by `h_m`.

On `G_m(R,K)`, `h_mJ_n<=1/2`. The elementary bound `|log(1-x)+x|<=x^2` on `[0,1/2]`, (4), and (18) yield

`sup_{n h_m<=T}|log(|r_n/r_0|)+h_m sum_{j<n}H_j|=o_P(1)` whenever `r_0 ne 0`, **(19)**

because `h_m^2 sum_{j<T/h_m}J_j^2<=const(K,T)h_m->0`. With `r_0=0`, the residual conclusion is exact. By (16), splitting the sum at physical time `delta`, and using `H_j<=2K`, `Q_m<=K`,

`sup_{n h_m<=T}|h_m sum_{j<n}(H_j-Q_m)|`

`<=3K(delta+h_m)+T sup_{delta<=j h_m<=T}|H_j-Q_m|->_P0`

after `m->infinity` and then `delta->0`. Combine with (19) and `|r_0|<=R` to obtain `sup_{n h_m<=T}|r_n-r_0 exp(-Q_m n h_m)|->_P0`. Finally, `Q_m<=S_0` is tight, so replacing `n h_m` by any `t` in its holding cell costs at most `|r_0|Q_m h_m=o_P(1)`. This proves (2).

The established joint initialization law gives `(F_m,Q_m)=>(F,Q)`, with `Q` independent of `F` and the transform stated above. The continuous mapping theorem and (2) identify the macroscopic output limit. The maximum output jump on `[0,T]` is `O_P(h_m)` by (4) and (7), so polygonal output interpolation has the same uniform approximation and hence converges in `C([0,T])`.

## Scope and checks

The limit is for fixed `gamma>0`, hence `h_m=gamma/L_m->0`; no claim is made for a fixed positive physical-time step. The held boundary limit depends on `gamma` and is different from the continuous boundary path between mesh points, while the macroscopic output and positive-time kernel limits agree with continuous gradient flow. This distinction depends on retaining the actual post-step ReLU value and absorbing negative overshoot. The proof uses the scalar residual sign, one common hyperbolic clock, iid independent-coordinate stable initialization, and a single input. Multiple inputs do not share this scalar gate ordering.
