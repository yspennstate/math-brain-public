# Independent review of `agents/c02.md`: one Euler step at the scalar switching scale

**Verdict.** The five-coordinate convergence, the endpoint-kernel formula, and the alpha-dependent nonzero-correction claim are correct under the stated scalar iid-stable model and the joint marked-initialization lemma in `research/T384_marked_PPP.md`. I find no fatal gap. The result is genuinely one-step: it does not establish any later-grid or macroscopic discrete-training law. The only edit I recommend is to clarify which *unprefactored* sum is being compared with `C_m` in equation (4); the bound and ensuing conclusion are right.

## Exact scaling and output identity

Write `n=m^(1/alpha)` and `L=(log m)^(1/alpha)`. Then the network scale is `a=1/(nL)`, the training multiplier is `eta=L^2`, and a step of physical length `h=gamma/L` has parameter increment coefficient `h eta a r=gamma r/n`. With `z_i=W_i/n` and initial `u_i=U_i`, an active row updates **simultaneously** to

`u_i^+=u_i+gamma r_m z_i`, `W_i^+=W_i+(gamma r_m/n)u_i`.

Inactive rows remain unchanged. Since `La=1/n`, expanding `W_i^+(u_i^+)_+-W_i u_i` gives exactly equation (3) of c02, including the cross term

`gamma r_m n^(-2)sum_{u_i>0}u_i(u_i+gamma r_m z_i)_+`.

There is no missing second-order term: the cross term is that term. Define its unprefactored factor `D_m=n^(-2)sum_{u_i>0}u_i(u_i+gamma r_m z_i)_+`. The correct interpretation of c02 equation (4) is

`|D_m-C_m| <= gamma |r_m| n^(-2)sum_{u_i>0}u_i|z_i| <= (gamma |r_m|/(2n)) S_m=o_P(1)`.

Here `S_m=n^(-2)sum(W_i^2+U_i^2)` is tight and `r_m` is tight. Multiplying by the prefactor `gamma r_m` still leaves an `o_P(1)` error. I recommend naming `D_m` to avoid reading the phrase “second sum in (3)” as including its `gamma r_m` prefactor.

For the kernel, `|W_i^{+2}-W_i^2|` and `|(u_i^+)_+^2-(u_i)_+^2|` have normalized total bounded by a constant times `(2|d_m|+d_m^2)S_m`, with `d_m=gamma r_m/n=o_P(1)`. The positive-part square bound remains valid even for an overshoot to a negative `u_i^+`; it follows from `|(x_+)^2-(y_+)^2| <= |x-y|(|x|+|y|)`. Thus the post-step second-layer block is `C_m+o_P(1)`, the moved W squares may be replaced by initial W squares, and the *gate* is exactly `1_{u_i>0,u_i+gamma r_m z_i>0}`. This verifies c02 equation (5). A negative overshoot is preserved as a signed hidden coordinate, so with the specified derivative `1_{U>0}` that neuron stays inactive in subsequent scalar steps.

## Joint endpoint mapping and boundary area

For each fixed `gamma`, the marked PPP map has possible discontinuities at `u=0` and `u+gamma r z=0`. Conditional on `F`, `r=y-F` is fixed, independent of N, and the stable U mark has a density, so neither boundary carries an atom almost surely. Truncating to `epsilon<|z|<R` and `|u|<M` yields a finite continuous map. The omitted small-z first-layer kernel is bounded by `sum z_i^2`, and the omitted output term by `gamma |r_m|sum z_i^2`; the uniform truncated-square estimate is `O(epsilon^(2-alpha))`. The large-z and large-mark omissions have vanishing *probability* as `R,M` grow. These estimates justify the joint continuous-mapping step for `(F_m,H_m(0),H_m^+,L_m(f_m^+-F_m))`, even though the limiting PPP has infinitely many small atoms and its full z-square sum has infinite expectation.

The exact ReLU identity for an initially active row is

`z[(u+gamma r z)_+-u] = r z^2 int_0^gamma 1_{u+r z s>0}ds`.

Its right side is dominated by `gamma |r|z^2 1_{u>0}`, whose PPP sum is finite almost surely for `alpha<2`. Adding the `gamma r C` term from the output-weight update proves the limit `r int_0^gamma K(s)ds`. Consequently

`L_m[r_m^+-(r_m-h_m H_m(0)r_m)] => r int_0^gamma [K(0)-K(s)]ds`.

The sign is correct: the naive tangent-kernel step overstates the magnitude of the residual reduction when opposing gates cross. This is a joint expansion at order `1/L_m`; the unscaled output increment itself tends to zero.

## The alpha threshold and strict positivity

For `r!=0`, crossing atoms satisfy `u>0`, `rz<0`, and `u<gamma |r||z|`. The opposing z half-axis has intensity `alpha c v^(-1-alpha)dv`. Tonelli gives its conditional intensity

`lambda_gamma(r)=alpha c int_0^infinity v^(-1-alpha)P(0<U<gamma |r|v)dv`

`=c(gamma |r|)^alpha E[U^(-alpha)1_{U>0}]`.

The standard symmetric alpha-stable density is continuous and strictly positive at zero, so the negative moment is finite exactly for `0<alpha<1` and infinite for `1<=alpha<2`. If `alpha<1`, the crossing count is Poisson with this finite mean, and the correction is nonzero with conditional probability `1-exp[-lambda_gamma(r)]`. If `alpha>=1`, the crossing region has infinite PPP measure, hence contains infinitely many atoms almost surely and the correction is strictly nonzero almost surely. Nevertheless

`0 <= M_gamma=int_0^gamma[K(0)-K(s)]ds <= gamma sum_{N,u>0}z^2 < infinity` almost surely.

Thus “infinitely many crossings” does **not** mean a divergent kernel loss, a jump at boundary time zero, or a divergent correction. The correction has the sign of r. Since F has a continuous law, `P(r=0)=0` for every fixed label y, so these conditional conclusions imply the unconditional statement in c02.

## Held Euler interpolation and limits of the claim

For every fixed `0<s<gamma`, the zero-order-hold first-step path equals `H_m(0)`, hence tends to `K(0)`. The continuous-flow boundary process at that s is strictly below `K(0)` with positive probability for `alpha<1` and almost surely for `alpha>=1`. A deterministic s is almost surely not a jump time of K, so these distinct one-time laws preclude the claimed continuous-flow `J_1` law for the held Euler path. At the first grid endpoint, the post-step kernel does tend to `K(gamma)`, while the rescaled output increment equals the continuous boundary *area*. Both statements are consistent: Euler evaluates ReLU after an overshoot, so an atom that crosses during the step contributes only its pre-hit area to the output change.

The proof does not compare two or more GD updates, establish a held-path limit at all grid points, control a fixed positive physical time, or extend to several inputs. It also uses the exact one-step coefficient `h_m=gamma/L_m` and the explicit simultaneous update; changing the step scaling or update convention requires a separate argument.
