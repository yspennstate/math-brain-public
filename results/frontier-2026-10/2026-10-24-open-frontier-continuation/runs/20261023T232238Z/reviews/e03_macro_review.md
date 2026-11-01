# Independent audit: `MACRO_COMPACTNESS.md`

**Verdict: the proposed partial theorem passes this audit**, conditional on the previously established joint initialization law `(f_0,C_m,0,N_m)=>(F,C,N)`. It proves subsequential compactness and the displayed inclusion, not uniqueness or convergence of the actual pre-step tangent Gram. I found no missing fixed-`gamma` secant correction in its output argument; the exact parameter integration-by-parts identity pays for repeated crossing.

## Growing-step bootstrap

The two estimates in (6) remain valid for `N=O(L)` steps. On the stopped region `S_n<=2K, ||r_n||<=R_*`, the `gamma/a` residual-squared term in the output increment is absorbed into `h const(K)||r_n||` for fixed `R_*` and sufficiently large `m`. Discrete Gronwall gives `||r_n||<=R exp[const K(T+1)]`. Choosing `R_*` above this bound leaves a strict margin. The accumulated row increment is at most `const (gamma/a)N R_*=O(L/a)`, so the squared row energy stays below `2K` for large `m`. The first-exit induction closes without finite-step loss descent. It also gives the uniform `O(L/a)` row-relative displacement, freeze bounds (9), and a physical-time Lipschitz bound on polygonal outputs. Initial energy and residual tightness remove the localization.

The error in (10) is genuinely **unscaled**: `max_i R_i,0/a<=sqrt(S_0)` and `max_{i,n}|W_i,n/a-W_i,0/a|=O_P(L/a)`; summing `O(L)` projected steps gives `O_P(L^2/a)=o_P(1)`. This does not assume that a gate crosses only once. For each matched marked atom, `q_i,m=V_i/L` has bounded physical-time slopes and initial value tending to zero.

## Atom matching and weak gate fractions

The finite-cutoff PPP matching avoids claiming a minimum threshold margin over infinitely many atoms. On each retained set, uniform path compactness and weak-star compactness of the binary gates give a diagonal subsequence. Bounded weak-star sets in `L-infinity([0,T])` are metrizable because their `L1` predual is separable, so the indicated joint extraction is valid. Uniform convergence of `r_m` and `W_i,n/a->z`, together with weak-star convergence of the gates, passes the projected integral update to `q'=zG D(theta)r`. Uniform convergence of `q_i,m` fixes each gate off its zero set, yielding the stated binary values there; the zero-set fraction remains unselected. A countable atom enumeration supplies jointly measurable time fractions after choosing measurable representatives.

The output proof does **not** pass a product of weakly converging indicators through a kernel. That would be invalid in the attracting-face chatter example. The theorem correctly keeps `Q_eff` as a representation of the limiting residual action, and explicitly disclaims convergence of the finite-width pre-step Grams to it.

## Exact output and infinite-atom interchange

Equation (11) is an exact algebraic identity: write `W_n h_n-W_0 h_0=W_0(h_n-h_0)+(W_n-W_0)h_n`, then substitute the simultaneous GD update for `W_n-W_0`. The second term is the cross-time Gram sum, and (9) turns it into `C_m,0 J_m+o_P(1)` uniformly through `T`. For a retained endpoint, the first term becomes `z(q(t))_+` because `h_n/L=(V_n/L)_+` and its initial marked projection divided by `L` vanishes.

The small-`|z_0|` estimate (12) is the important uniform truncation: its left side controls the entire first output term up to time `T`, even after repeated reactivation. Its right side is the initial small squared-output-weight mass, with expected limsup `O(epsilon^(2-alpha))`, plus `o_P(1)`. Large endpoints have vanishing occurrence probability as their cutoff grows; for `|z|>epsilon`, large original marks have vanishing occurrence probability as their mark cutoff grows. The limiting bound `sup_t|q_(z,u)(t)|<=const_T |z|` and `sum_N z^2<infinity` almost surely justify absolute **uniform** convergence of the Poisson output sum. This pays the infinite-atom interchange in (3) without assuming a finite second moment of large stable endpoints.

For each atom and coordinate, the derivative of an absolutely continuous `q_j` is zero almost everywhere on `{q_j=0}`. Thus `(q_j^+)'=theta_j q_j'` almost everywhere, regardless of the zero-set fraction. The derivative of the atom's weighted output is dominated by `const z^2||r(t)||`; summability of `z^2` and a countable full-measure intersection justify differentiation under the Poisson sum. Substituting `q'=zG D(theta)r` gives (4) as a **vector-action identity**. Since `G` and `C` are positive definite, its PSD energy inequality gives (5).

## Remaining limitation and phase

The all-zero endpoint solution in the draft verifies nonuniqueness of the collapsed-origin inclusion. Original marks can choose different entrance sectors even though every `q(0)=0`; the inclusion alone cannot produce a full limit law. Fixed `gamma` may also retain a microscopic phase in the secant matrix, as `e03_discrete.md` shows. This causes no contradiction with (4): differing phase matrices can have the same action on the realized residual, while the weak pre-step tangent Gram has a different action because it omits off-to-on secants. No kernel-topology conclusion beyond the explicitly stated output action should be inferred.
