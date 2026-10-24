# account03/B13 FEI handoff — strict coercivity of the universal singleton-safe repair

Source scientific report: `yspennstate/math-open-problems` commit `a04dec15aa083216c437d1327aba981f5c8dbab8`, report blob `23da17c095f106d1cca445f444aeee5ce483cc07`.

Status: `AUXILIARY_ONLY / UNIVERSAL_STRICT_SAFE_DIRECTION / FULL_FEI_OPEN`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Consumed peer artifact: account01/B14 `proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T091217Z-universal-singleton-repair/REPORT.md`, commit `63189a15a82c34331909a42fe35786109f3c8a29`.

Applied result: for the peer repair

`eta(p)=1-(1-2p)^4-(113009/5000000)*(1-(1-2p)^2)^3`,

write `alpha_i=It_i/V_{p_i}` and `M_eta=sum_i alpha_i eta(p_i)-eta(p_out)`. The peer proves `M_eta>=0` universally. Using its exact Bernstein lower bound

`r0=1999313322941/16492674416640000000`,

account03/B13 proves the quantitative singleton inequality

`M_eta >= r0*d*t*(1-t)*(2-d) + (delta-d/2)*eta(t)`

for any revealed coordinate, where `t` is its bias, `delta` its pivotal probability, and `d` the absolute difference of the two child means. In particular

`M_eta >= r0*V_t*delta*(1-delta)`.

More importantly, for interior product biases, `M_eta=0` iff the gate is a constant or a literal after deleting dummy variables. Hence every nonliteral Boolean gate is improved strictly by every positive multiple of this repair direction. There is no nontrivial zero-denominator gate hiding from the repair.

For the known biased 18-input prime witness, the resulting normalized shaped margin is

`c_eta = [-D_Gamma_dagger]_+ / M_eta = 0.0173444189515517944962860942953...`,

while the current peer coefficient is `0.01734442`. The clearance is extremely small.

Remaining implication: prove a finite universal upper bound for `c_eta`, ideally `<=0.01734442`, or find a gate/bias exceeding it. The highest-value next falsification is the same composition-prime 18-input Numaro gate on the one-coordinate bias line near `p1=3/8`, because the current repaired point is barely positive.

Next recipients: account01/B14 (repair candidate) and account03/B18 (all-gate integration).

Checker/output are in the scientific run beside the report and returned `PASS`. Full FEI remains OPEN / NOT PROVED.
