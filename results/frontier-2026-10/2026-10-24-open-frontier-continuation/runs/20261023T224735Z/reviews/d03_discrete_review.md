# Adversarial review of `agents/d02_discrete.md`

**Verdict:** The scalar critical-grid and macroscopic Euler theorems pass this review, conditional only on the previously established joint marked initialization law in `research/T384_marked_PPP.md`. I found no missing crossing correction or accumulated error over the `O(L_m)` steps. The fixed-grid `J_1` claim is appropriate. The proof does not silently use a continuous-time interpolation at gate crossings.

## Exact secant and sign bootstrap

For a pre-step active pair `(u,w)`, the straight update is `(u+theta d w,w+theta d u)`. Differentiating `g(theta)=(w+theta d u)(u+theta d w)_+` gives

`g'(theta)=d 1_{u+theta d w>0}(u^2+w^2+2theta d u w)`

almost everywhere, even when the final hidden coordinate is negative. Since `|2uw|<=u^2+w^2`, its bracket is at least `(1-|d|)(u^2+w^2)` for `|d|<1`. The normalization `a_m beta_m=m^(-2/alpha)` then gives the exact residual identity `r_{n+1}=r_n(1-h_m J_n)` with `J_n>=0`; there is no linearization error in this identity. The upper bound `J_n<=(1+|d_n|)S_n` is correct.

The energy inequality `S_{n+1}<=(1+|d_n|)^2S_n` also includes a crossing step: the entire active pair receives the full Euler matrix before its negative overshoot is frozen. On `|r_0|<=R,S_0<=K`, the induction is noncircular. Assuming previous residual contraction gives `sum_{j<n}|d_j|<=beta_m R(T+2h_m)=o(1)`, hence `S_n<=2K`, `h_m J_n<=1/2` for all large `m`; the exact recurrence then preserves the sign and contraction at the next step. This yields the uniform squared-weight and positive-hidden-square drift bounds (8), including crossed neurons.

## Gate clock and critical boundary grid

For `sigma=sgn(r_0)`, the transformed active update on `(U,sigma W)` is `[[1,q_n],[q_n,1]]` with `q_n=|d_n|<1`. These matrices commute. Their product is exactly `rho_n[[cosh Theta_n,sinh Theta_n],[sinh Theta_n,cosh Theta_n]]`, with `rho_n=prod(1-q_j^2)^(1/2)` and `Theta_n=sum artanh(q_j)`. A supporting initial gate cannot die. For an opposing gate, its virtual hidden coordinate changes sign at most once as `Theta_n` increases, so freezing the actual coordinate at the first nonpositive Euler value gives precisely indicator (9), even after a negative overshoot. This is the key exact ordering fact.

On a fixed boundary horizon, the number of steps `floor(S/gamma)` is fixed. The step residuals satisfy `r_j-r_0=O_P(L_m^(-1))`, and `m^(1/alpha)tanh Theta_n=n gamma |r_0|+o_P(1)` for every one of those finitely many `n`. The marked PPP and `(F_m,C_m)` convergence therefore give the joint kernel-grid vector. Initial small-`|W|` square mass is bounded by `O(epsilon^(2-alpha))`; the uniform moved-square bound removes the fact that the weights at step `n` differ from their initial values. At the output grid, expansion (12) is exact; its second sum tends to `gamma r C`, and the first sum converges atomwise to the stated ReLU increment. For an atom absorbed in an earlier step, both positive parts of the *virtual* coordinate in that later cell are zero, matching its zero actual contribution. Small initial-`|W|` atoms are controlled by the same square-mass bound, so summing cells legitimately gives the boundary-kernel area.

The held processes have jumps only at the **same fixed finite list** of deterministic times `gamma,2gamma,...` for every `m` and the limit. Joint convergence of all grid heights therefore implies uniform convergence under a finite-grid coupling, hence `J_1` convergence. This differs from a shrinking cluster of distinct random gate-hit times, where `J_1` could fail; no such merging is claimed here.

## Uniform positive-time gate loss and accumulated secant error

On `c<=|r_0|<=R,S_0<=K`, `h_m J_n<=1/2` implies the lower residual bound (14), so the common hyperbolic clock by any physical time `delta>0` is at least a fixed positive multiple of `beta_m delta`. An opposing initial extreme with `|W_{i,0}|>=epsilon m^(1/alpha)` that survives then needs `U_{i,0}>=const epsilon L_m`. Independence of initialized `W_i,U_i` makes the unconditional union probability `O(1/log m)`. The initially smaller `W` square mass costs `O(epsilon^(2-alpha))`, and (8) controls later weight motion. Because absorption is irreversible, the removal is uniform over all steps after `delta`; supporting gates remain active. Letting `m->infinity`, then `epsilon->0`, and finally removing `c,R,K` by atomlessness/tightness proves the positive-time kernel comparison (16). Intersecting these unconditional rare-event estimates with the random good event causes no conditioning gap.

The crossing correction is paid **once per neuron**. In (17), noncrossing terms differ from the pre-step kernel by at most `|d_n|S_n`, while a crossing term can additionally lose at most its current squared norm. Each neuron enters `X_n` at most once and its crossing-time norm is at most `e^(2D_m)` times its initial norm. Therefore

`h_m sum_{n<T/h_m}|J_n-H_n| <= (T+h_m)sup_n|d_n|sup_nS_n + h_m e^(2D_m)S_0=o_P(1)`.

This remains valid with `O(L_m)` steps: `sup|d_n|=O_P(m^(-1/alpha))`, `h_m=gamma/L_m->0`, and `S_0` is tight. A single critical first-step secant error may be order one, but its contribution to the macroscopic log-residual is multiplied by `h_m`. The logarithm remainder is `O_P(h_m)` because `J_n=O_P(1)` uniformly. Splitting the remaining Riemann sum at `delta`, using (16) thereafter and the crude `3K` bound before it, proves (2) without a residual-sign or early-layer gap. The floor correction is `O_P(h_m)`.

## Dependency and minor editorial point

The only probabilistic input treated as established is the joint marked initialization `(F_m,C_m,N_m)=>(F,C,N)` with the small-endpoint truncation estimates, plus the resulting `(F_m,Q_m)` law. The discrete proof itself supplies all dynamical estimates it needs; it does not assume a full continuous-time boundary-path theorem. In the boundary section, the sentence `h_m J=S/L_m+O(h_m)` uses `J=floor(S/gamma)`, while `J_n` denotes the secant kernel elsewhere. Renaming that fixed step count `N_S` would avoid a momentary notation collision, but it does not change the argument.
