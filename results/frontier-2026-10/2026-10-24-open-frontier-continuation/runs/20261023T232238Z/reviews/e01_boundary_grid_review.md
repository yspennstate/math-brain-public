# Independent review of `BOUNDARY_GRID.md`

**Verdict: the fixed-finite-grid theorem is supported, conditional on the cited prior joint stable-initialization law.** I checked the exact output secant identity, its error bound, the heavy-tail tightness/localization argument, threshold continuity, and cutoff removal. I found no step that assumes monotone projected gates. This review makes no claim about `n` growing with width, a continuous-time selection, a macroscopic nonorthogonal limit, or external priority.

## Exact algebra

Write `h_i,n=(v_i,n)_+` and `Delta h_i=h_i,n+1-h_i,n`. Since `L/b=1/a`, expanding the simultaneous product update gives exactly

`L Delta f = a^(-1) sum_i [W_i,n Delta h_i+(Delta W_i)h_i,n+1]`.

Substituting `Delta W_i=(gamma/a)r_n^T h_i,n` gives equation (15), with `z_i,n=W_i,n/a`. The second term splits as

`(gamma/a^2)sum_i(r_n^T h_i,n)h_i,n+1
 =gamma C_m,n r_n+(gamma/a^2)sum_i(r_n^T h_i,n)Delta h_i`.

The ReLU Lipschitz bound and the projected step imply `||Delta h_i||<= (gamma/a)|W_i,n| ||G|| ||r_n||`, while `||h_i,n||<=||X||||U_i,n||`. These yield exactly the first inequality in (16); `sum_i |W_i,n||||U_i,n||<= (1/2)sum_i(W_i,n^2+||U_i,n||^2)` yields its `O(S_m,n/a)` conclusion. Thus the `gamma C r` part and the endpoint secant part are correctly separated. Replacing the secant by `gamma K_n r` would be wrong when a projection crosses zero during a step.

For (8), the first part of the exact increment is bounded by `gamma ||G||||r_n|| a^(-2)sum_i W_i,n^2`; the `gamma C_m,n r_n` part is bounded by `gamma ||X||^2||r_n||S_m,n`; (16) supplies the last term. The asserted constants `A_X,B_X` therefore exist.

## Tightness and finite-step localization

At initialization `S_m,0=a^(-2)sum_i(W_i,0^2+||U_i,0||^2)` is tight. One direct verification uses `p=alpha/2<1` and the stable-square tail `P(Z^2>t)<=C t^(-p)` for large `t`. With `T=R a^2`, a union bound for values above `T` plus Markov's inequality for values truncated at `T` gives

`P(S_m,0>R) <= C_(d,alpha) R^(-p)`

for large `R`, uniformly in `m`, because `a^(2p)=m`. Tightness of `r_0=y-f_0` is supplied by the cited initial-law convergence.

For each fixed step the update of `(U_i,W_i)` is a symmetric star matrix of operator norm at most `(gamma/a)||X||||r_n||`; this verifies the row norm estimate. On `||r_0||<=R,S_m,0<=B`, assume inductively `||r_n||<=R+1,S_m,n<=2B`. The row bound changes `S_m,n` by a factor `1+O(1/a)` per step, while (8) changes `r_n` by `O(1/L)` per step. Since `N_0` is fixed, both bootstrap bounds close for large `m`, giving (9). Summing row increments then gives `|| (U_i,n,W_i,n)-(U_i,0,W_i,0)||<=C R_i,0/a`; the quadratic Gram and output-weight-square comparisons in (10) follow after summing against `R_i,0/a^2`. No loss-descent premise is needed.

## Endpoint continuity and cutoff removal

For a prescribed finite gate history, `v_n=Xu+gamma zG sum_(j<n)D_jr`. Each possible coordinate tie is an affine hyperplane in `u`, since every row of full-rank `X` is nonzero. The stable mark law is absolutely continuous; conditioning on `z,r` and using the prior independence of `F` and the marked PPP makes the probability of any tie among countably many atoms and integer steps zero. This validates finite-atom induction, including reactivation, with the localized drift `W_i,n/a-W_i,0/a=o(1)` and `r_n-r_0=o(1)`.

Near `z=0`, both the kernel and the endpoint output increment are bounded by constants times `z^2`, whose Poisson intensity integral is `O(epsilon^(2-alpha))`. The finite-width counterpart in (14) has the same truncated-square expectation bound; (10) controls the changed `W_i,n^2`. At large `|z|`, the probability of any atom is `O(M^(-alpha))`; at fixed lower `|z|>epsilon`, large marks have probability at most a constant times `epsilon^(-alpha)P(||U||>B)`, tending to zero as `B` grows. These probability cutoffs avoid the generally infinite expectation of large `z^2`. They justify ordinary absolutely convergent Poisson sums, equation (6), and the common-grid held-path `J1` conclusion.

## Scope and small presentation point

The extension of the *initial* joint stable law from the cited coordinate-ray proof to fixed full-row-rank `X` is used as a dependency. Its stated ray remainder bounds and rank argument do not use orthogonality, and I see no new obstruction there, but this review does not independently rederive the entire earlier stable triangular-array theorem. The fixed-grid result is distinct from continuous-time training: no amount of finite-`N_0` tightness alone permits `N_0` of order `L_m` or selects a Filippov trajectory. The note already states that boundary clearly.
