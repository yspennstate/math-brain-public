# Independent review: global reflection and the proposed all-mixed extension

**Verdict.** I find the existing `GLOBAL_REFLECTION.md` law sound in its stated initial double-sliding cone, subject to the cutoff and sign-invariance details already made explicit in `reviews/h03_global_review.md`. I also find no obstruction to extending the selected reflected law to **every** initial mixed residual `R_1<0<R_2` when `0<rho<1`, provided the extension states and proves the finite-decision entrance lemma and the one-sided certificate transfer below. The extension changes the selected masses: outside the double cone the survivor indicators generally depend on `R`, the original mark, and the fixed multiplier `gamma`. The constant Schur matrix `Q` remains only a local double-cone simplification.

## 1. Frozen all-mixed finite-decision lemma

Fix `r=(-p,q)` with `p,q>0`, `z>0`, and write the frozen grid in unscaled projected coordinates `(x_n,y_n)`. If `y_n<=0`, either both gates are off already or only `x` fires. In the latter case every following step subtracts `gamma*z*p` from `x` and `gamma*rho*z*p` from `y` until both gates are off. Hence support loss is an irrevocable finite-death event, including a strict negative terminal pair for generic marks.

While `y_n>0`, put `s_n=1{x_n>0}`, `c=rho*z*q>0`, `d=z(p-rho*q)` (now of either sign), and `eta_n=y_n-rho*x_n`. The exact recurrences are

\[
 x_{n+1}=\begin{cases}x_n+\gamma c,&x_n\le0,\\x_n-\gamma d,&x_n>0,\end{cases}
 \qquad
 \eta_{n+1}=\eta_n+\gamma(1-\rho^2)zq.             \tag{1}
\]

For any `D>max(d,0)`, the half-line `x> -gamma*D` is forward invariant while support is open: an off step increases `x`, and an on step ends above `-gamma*D`. If the initial `x` is below this half-line, its off steps increase it by the fixed positive `gamma*c`, so it reaches the half-line after finitely many steps unless support was lost first. If support is never lost, `eta_n` increases linearly and eventually exceeds `rho*gamma*D`. Thus the literal frozen-grid algorithm **must stop in finitely many steps** at one of two strict certificates:

* a dead state with both projections negative (after completing any remaining single-gate steps); or
* `y>0`, `x> -gamma*D`, and `eta>rho*gamma*D`.

The second certificate implies `y=eta+rho*x>0` and remains valid under *any later coefficient sequence* with `c_n=rho*z_n r_{2,n}>0`, `d_n=-z_n(r_{1,n}+rho*r_{2,n})<D`, and `z_n r_{2,n}>0`. Indeed the one-sided lower bound persists and `eta` increases. No upper strip bound or sign condition on `d_n` is needed; `x` may release to positive macroscopic size.

For `z<0`, exchange coordinates: `x` is support, `y` is normal, `c=rho*|z|*p>0`, `d=|z|*(q-rho*p)`, and `eta=x-rho*y` increases by `gamma*(1-rho^2)|z|p`. Loss of `x` is finite death; otherwise the mirrored one-sided certificate is reached. The initial finite-step threshold events are affine hyperplanes in `Xu` for fixed `(z,R)`, hence null under the marked PPP. Strict terminal certificates are stable under small perturbations. This proves a well-defined generic selector `sigma_gamma(z,u;R) in {0,1,2}` for all mixed `R`, even without a closed-form quadrant-race formula.

The test of this selector is not merely whether the initially proposed support is positive. In the upper ratio region `p>q/rho`, a positive-`z` atom can start with `y_0>0` and still die before its one-sided certificate. For example, `rho=1/2`, `r=(-3,1)`, `z=1`, and `(x_0,y_0)=(1,0.3)` die at `gamma=1` after one `++` step to `(-1.5,-0.2)`, whereas a sufficiently fine frozen grid reaches `x<=0` while `y>0` and survives. This illustrates why the all-mixed masses may retain `gamma` dependence. The double-cone selector `1{y_0>0}` (and its mirror) is recovered when `rho*q<p<q/rho`.

## 2. Noncircular transfer to actual GD

Condition on `R_m` initially mixed, then use the prior `MACRO_COMPACTNESS.md` tightness to extract any conditional subsequential limit. That limit's effective matrix is `C+int z^2 D(theta)G D(theta)N`, which has bounded entries and nonnegative off-diagonal when `rho>0`. With `s=(-r_1,r_2)`, its absolutely continuous evolution is a bounded Metzler system. Therefore both `s` coordinates stay strictly positive for each fixed finite horizon. This conclusion applies **before** endpoint selection. Under a joint subsequence representation, the actual finite-width residuals consequently remain mixed on `[0,T]` with probability tending to one, after a pathwise positive-margin localization; it does not require a selected-kernel comparison.

For a finite marked cutoff `epsilon<|z|<M`, `||u||<B`, localize the macro residual bound and choose a deterministic `D_*` larger than every possible positive part of the retained actual `d_{i,n}` through the chosen horizon. The frozen all-mixed algorithm above reaches a strict dead or one-sided live certificate in finitely many steps for each retained atom. Restrict the maximum certificate index to a deterministic `N_0` on an event of arbitrarily high probability, apply the **fixed**-`N_0` boundary-grid theorem, and then remove the index restriction. Initial fixed-step residual drift is `O_P(N_0/L)`; the strict finite histories and certificates transfer to actual rows. Actual retained weights keep their initial signs uniformly on `[0,T]` by the macro row bootstrap.

Dead rows remain exactly immobile. Live rows retain the one-sided lower normal bound and positive support throughout the mixed finite-width horizon. This is not just qualitative: for a positive-`z` survivor, in scaled coordinates `q=v/L` and after its finite boundary-step certificate,

\[
 q_{1,n}\ge-hD_*,\qquad
 q_{2,n}-\rho q_{1,n}
 =\eta_{N_0}/L+(1-\rho^2)h\sum_{j=N_0}^{n-1}z_{i,j}r_{2,j}.       \tag{2}
\]

The term `eta_{N_0}/L` tends to zero, the finite early interval has physical length `N_0*h->0`, and the mixed limit has `r_2(t)>0` with a positive minimum on every compact horizon. Thus at each fixed `t>0` the limiting support satisfies

\[
 q_2(t)\ge(1-\rho^2)z\int_0^t r_2(s)ds>0,\qquad q_1(t)\ge0. \tag{3}
\]

The mirrored negative-`z` bound is `q_1(t)>=-(1-rho^2)|z| int_0^t r_1(s)ds>0`, `q_2(t)>=0`. These estimates establish **strict limiting support before invoking the relay equation**; otherwise one might incorrectly infer gate `1` from finite-width support positivity whose margin could vanish. They also avoid a common positive lower support margin across the infinitely many atoms.

For each retained survivor, the prior macro endpoint inclusion now has support gate `1` almost everywhere on `(0,T]`. Its normal coordinate solves the monotone scalar relay with `a=z r_1<0,c=rho*z*r_2>0` (or the mirror). The collapsed initial normal coordinate is zero, and the prior reflected-integral uniqueness theorem identifies it. Tangential cancellation then identifies the full endpoint path. A dead atom has zero limiting endpoint path and zero output increment. This argument is per atom, then a countable intersection handles all PPP atoms; it never asks the finite-grid theorem to run for `O(L)` boundary steps.

Finally, the exact macro output identity and its uniform small-initial-`|z|` square-mass bound remove omitted atoms. Thus every subsequential residual solves the same selected Volterra equation. Its reflection map has a prefix Volterra Lipschitz bound, so Picard/Gronwall gives a unique continuous solution. Uniqueness identifies the full conditional path law on every fixed physical horizon. Large-`|z|` and large-original-mark cutoffs are removed by finite-atom occurrence probabilities, not an assumed finite stable second moment.

## 3. Correct proposed all-mixed statement and limits

For `R_1<0<R_2`, define the finite-grid selector just proved and

\[
 P_j^\gamma=\int z^2{\bf1}\{\sigma_\gamma(z,u;R)=j\}\,N(dz,du).
\]

These masses are finite almost surely. They may depend on `R` and `gamma`; conditional on `R`, the two sign populations are independent Poisson thinnings, but unconditional independence from `(F,C)` is generally false. Let `I=int_0^. r`, let `S(w)=w-min(0,min_{s<=.}w(s))`, and set

\[
 u=S(I_1+\rho I_2),\quad v=\rho u+(1-\rho^2)I_2,
 \quad u_-=S(-I_2-\rho I_1),\quad v_-=\rho u_--(1-\rho^2)I_1.
\]

The all-mixed candidate is the unique solution of

\[
 r=R-CI-P_2^\gamma(u,v)+P_1^\gamma(v_-,u_-).                \tag{4}
\]

The signs, factors of `z^2`, and the two mirrored reflected coordinates check against the exact simultaneous-GD endpoint update. Its almost-everywhere output action is PSD with nonnegative off-diagonal (`G` off the normal face, Schur diagonal on it), so the resulting residual remains mixed. Equation (4) agrees with the current `GLOBAL_REFLECTION.md` formula on the initial double cone, where the selector simplifies and the masses become `gamma`-independent, independent of `(F,C)`, and iid positive `alpha/2`-stable.

I do not see a need to assert convergence of finite-width pre-step tangent Grams in `L^1`, convergence of certificate times, or continuity of ratio-cone exit times. The all-mixed extension does not cover same-sign initial residuals, negative correlation, more than two inputs, deep networks, or test-input laws.
