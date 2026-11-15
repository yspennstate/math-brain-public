VERDICT: PROVED invariance of the conditioned environment-and-velocity law at fixed density

The fixed-density diffusion and planar recurrence problems remain open. No solution elsewhere was found in the literature update, which ended within five minutes. No SOLVED_ELSEWHERE.md was created.

New beyond round 3: PROOF.md proves the proposed stationarity lemma. Let H be the event that the origin lies in an unbounded open vacant component, theta=P(H)>0, Q=P(.|H), and sigma uniform probability measure on the velocity sphere. For the billiard started at the origin with law Q tensor sigma,

\[
(\tau_{X_t}\omega,V_t)\ \stackrel{\mathrm{law}}=\ Q\otimes\sigma
\]

at every deterministic time t. The resulting environment process is stationary. No ergodicity or uniqueness of the unbounded component is assumed. The proof uses Liouville measure and finite-speed spatial averaging, with an explicit error supported in a shell of relative volume [(1+|t|/R)^d-(1-|t|/R)^d]. It covers bounded measurable observables of the entire environment.

The well-posedness justification is included: for almost every initial phase point, the billiard has a two-sided regular trajectory with locally finite collisions, even though obstacle balls overlap. Finite singular encounters are null by dimension counting. A local collision-flux bound excludes finite-time accumulation without assuming global existence first. Translation invariance and Tonelli then transfer the spatial almost-everywhere assertion to the fixed origin under Q tensor sigma. This removes round 3's regular-trajectory caveat for this initial law, while retaining exceptional directions.

A direct consequence is the exact finite-time identity

\[
\mathbb E[X_tX_t^{\mathsf T}]
 =\frac{2I_d}{d}\int_0^t(t-s)\mathbb E[V_0\cdot V_s],ds.
\]

The infinite-time formula is stated only under an additional, unproved absolute-integrability hypothesis on the velocity correlation. Neither positive diffusivity nor a CLT follows from stationarity alone. These elementary invariant-measure arguments are new relative to the supplied folders; no literature priority is claimed.

Earlier result rechecked: the independent cell exponent is (d-ac) log R-log log R+O(1), and the net exponent is (d-bc) log R+(d-1) log log R+O(1), with b increasing to a. They confirm the earlier maximum-segment constant d/a, its dyadic almost-sure argument, and its trajectory corollary with the stated component caveat. The unmodified earlier audit was also executed in memory and passed. Its maximum sausage-volume discrepancy was 7.83e-15. The earliest logarithmic time-window witness checks as well.

Validation command from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit_stationarity.py
```

Output: PASS. Hemisphere projection and independent angular integration agree within 4.63e-14; tube Jacobians within 8.88e-16; shell formulas within 1.78e-15. The time-square, triangle, and closed-form checks confirm the covariance factors, with finite-grid error at most 2.5e-7. Runtime was 0.004 seconds and peak resident memory 12,795,904 bytes. Actual nice value was 20. LOG.md records the complete output and the in-memory earlier-audit command. All code uses bounded standard-library loops and one thread.

What failed or remains uncertain: no mathematical check failed. The nice wrapper warned when trying to raise inherited priority 20 to 15; the actual process remained at the lower priority 20. No decay, mixing, ergodicity, quenched limit, positive diffusivity, or recurrence estimate has been obtained. The literature search was bounded, and the proof has only the internal independent checks recorded here.

Next worker: derive the stationary collision Palm law from the flux construction. Normalize incoming velocity by |v dot n| on exposed boundary patches adjacent to unbounded vacancy, and express the mean collision rate through that boundary's mean area per unit volume. Establish finiteness and the normalization without assuming ergodicity. After that, the missing dynamical issue is quantitative control of velocity correlations or a suitable martingale approximation; neither follows from the geometric flight bound.

Opened primary sources confirming scope: Karsten Matthies and Raphael Winter, [arXiv:2506.18539v2](https://arxiv.org/html/2506.18539v2); Bálint Tóth, [arXiv:2501.00519v2](https://arxiv.org/abs/2501.00519v2); Yingxin Mu and Artem Sapozhnikov, [arXiv:2609.11690v1](https://arxiv.org/html/2609.11690v1). Their joint-limit and visibility results do not supply fixed-density diffusion.

Task: “Diffusion in the random Lorentz gas at fixed density” — 15 November 2026, 04:25 +04:00 (session orientation time).
