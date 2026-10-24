# B15 handoff — mesh-band arithmetic free energy

Full FEI remains OPEN.

New proved reduction: for packet masses `p_a`, normalized meshes `b_a`, `N_a=p_a/b_a^2`, and `X_a=log2(1/b_a)`, any packet partition `pi={B_j}` with `P_j=sum_{B_j}p_a`, `M_j=sum_{B_j}N_a` has

`F_pi := (1/2) sum_j P_j log2(M_j/P_j)`

and exactly

`F_pi-D = (1/2) sum_j P_j KL_2(p(.|B_j)||q(.|B_j)) >= 0`, where `q_a=N_a/sum N_a`.

Refining bins monotonically decreases `F_pi` to `D`. If bins have `X`-width at most `delta`, Hoeffding gives

`0 <= F_delta-D <= (ln 2) delta^2/4`.

For `delta_epsilon(f)=2 sqrt(epsilon I(f)/ln2)`, therefore

`D(f) <= F_epsilon(f) <= D(f)+epsilon I(f)`.

Using the inherited exact universal relation `C_H=2C_D`, the optimal full-FEI constant satisfies

`C_H = 2 lim_{epsilon->0} sup_f F_epsilon(f)/I(f)`.

At Hod's candidate `beta=6.4547837...`, a single Boolean `f` with

`F_epsilon(f) > (beta/2+epsilon) I(f)`

would rigorously force `C_H>beta`; conversely the family of bounds `F_epsilon <= (beta/2+epsilon)I` would prove sharp FEI at `beta`.

Mandatory stress tests: the punctured-subcube raw-normalizer obstruction and the valuation-misaligned tensor collision are preserved. The punctured and one-point families land in separate adaptive bins in the included calibrations, so `F_epsilon=D` there and the large negative KL credit is retained rather than discarded.

Next target: pay the one-dimensional adaptive-bin terms `(1/2)P_j log2(M_j/P_j)` by influence using Booleanity and neighboring-bin carry constraints, or construct a Boolean function crossing the finite Hod-disproof threshold above. Do not return to one-bin `log N`, `v log N_perp`, or unconditional tensor subadditivity; those routes are already refuted.
