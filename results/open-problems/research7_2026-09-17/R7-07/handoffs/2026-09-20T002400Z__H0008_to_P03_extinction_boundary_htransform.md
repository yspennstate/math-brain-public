# C06/R7-07 -> P03 shareable lemma (no objective transfer)

Source line: H0008 harmonic-boundary work; this note does not claim or alter P03's Lyons--Pemantle--Peres speed objective.

Primary proof: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T001807Z__report.md`, creation commit `48356dfe88edbdbae00a353d34979da016885335`.

For a finite-type surviving branching tree, let `s_i=P_i(survival)`, `t_i=sum_j q_j p_ij s_j`, and let the extinction Jacobian be

`J_ij = G'(1-t_i) q_j p_ij`, with `rho(J)<1`.

Introduce a backward effective conductance `a` and the harmonic function

`kappa_i(a)=E_i[a C/(a+C)]`,

where `C` is the forward effective conductance before the root edge. Under the Palm sibling law `R_i`, the positive transfer kernel

`K_ij(a,da') = M_ij E[ a/(a+R_i) 1{ F(a+R_i) in da'} ]`, `F(x)=x/(1+x)`,

satisfies exactly `kappa=K kappa`. Its Doob transform extends to the compactification `a=0`. The boundary-to-boundary subkernel is

`Q^0_ij = (s_j/s_i) G'(1-t_i) q_j p_ij = (D_s^{-1} J D_s)_ij`.

Hence `rho(Q^0)=rho(J)<1`: exact/near-pipe trapping is the boundary channel, while any genuine sibling conductance `R_i>0` injects the compactified chain into the interior. This may be useful in P03 for separating trap persistence from branch refreshment in regeneration or derivative calculations. No claim is made here that it proves speed monotonicity.