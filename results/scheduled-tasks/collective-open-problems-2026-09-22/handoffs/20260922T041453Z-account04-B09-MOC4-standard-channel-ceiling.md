# MOC4 handoff — account04/B09 standard-channel ceiling

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Worker/run: account04/B09 `20260922T041453Z-b09-moc4-r34`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains OPEN.  
Scientific source: `yspennstate/math-open-problems/proofnet24/collective-MOC4/account04/B09/20260922T041453Z-b09-moc4-r34/REPORT.md`, report blob `faaf77b4fcebb8fed6a6c9763251acc1042105ac`.

Consumed source-bound results:
- campaign lead account03/B07 `account03-B07-20260922T033411Z-d2a63b2a`, `MOC4-V4-PAIR-GAP-CEILING-v1`, scientific commit `dcce2e52aee9c3fb338be4dd56acb02114ebfdde`;
- required OTHER-account partner account01/B07 `MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`, scientific commit `ebf5fd79e719931fbacc23a12ce7c06a456c0019`, plus its later `MOC4-CARTAN-HESSIAN-PACKING-v1`;
- account03/B09 exact compatibility `D=(1/4)E^T P E`, report blob `06b56b516f3d36c9fa1e11601e775771fcf7e285`.

New theorem `MOC4-STANDARD-CHANNEL-CEILING-v1`: let `H_sigma` be the 24 endpoint support values, `B_rho` the six Klein-four fiber means, `Delta=M-max_rho B_rho`, and

`kappa_sigma = H_sigma - B_{rho_sigma}`, `Kstd=max_sigma kappa_sigma`.

For every true unitary `U`, its standard/oriented support component satisfies

`k(U) <= Kstd`.

Reason: `P=|U|^2` is doubly stochastic, so `P=sum lambda_sigma P_sigma`; the exact same-unitary identity `D=(1/4)E^TPE` makes the standard channel linear in that same Birkhoff decomposition, hence

`k(U)=sum lambda_sigma kappa_sigma`.

The lead already proved every support violation `h(U)=M+gamma` must satisfy `k(U)>=gamma+Delta`. Therefore every genuine violation obeys

`gamma <= Kstd-Delta`.

This is independent of stationarity, genericity, invertibility and simple spectra. In particular `Kstd=Delta` certifies the entire spectra/support-direction instance for all true unitaries.

Direct application to the lead's exact stress point `a=(-1,2,1,0)`, `b=(-1,1,-2,2)`, `eta=1`: the lead had `M=36`, `m=29/6`, `Q=15`, `Delta=21`, `G=141`, leaving its previous pair/fiber ceiling `gamma<=1/2`. Exact enumeration gives `Kstd=21=Delta`, so the new true-unitary ceiling is `gamma<=0`. Thus that previously sharp abstract relaxation witness cannot come from a true unitary.

Named-partner strengthening: on account01/B07's all-Cartan-zero-endpoints-safe branch, the Cartan curvature payments imply every `P_ij>=gamma/(4W)` for the two-channel scale `W`. Shrinking `P` about the uniform bistochastic point gives

`k(U) <= (1-gamma/W) Kstd`, hence

`gamma <= W (Kstd-Delta)/(W+Kstd)`.

Exact verifier blob `fe835da90b6d1f4bcd1f72b4cf33228926c30cb0`; captured exact output blob `da7b010f7e2879969b8be670127ed1b0a139106b` records `lead_V4_pair_ceiling=1/2`, `Kstd=21`, `standard_channel_ceiling=0`.

Surviving target-level obligation: handle the residual `Kstd>Delta` reserve by combining the symmetric quotient `R` with genuine stationarity/odd-Weyl/Pluecker or zero-face support geometry. Do not return to a universal full `(P,R)` positive lift.

Execution remained `WITHOUT_VERIFIED_BRAIN`; no benchmark material, credentials, email/Drive data, remote workflow, scheduler mutation, public posting, paid model/API/Codex use, or notification enabling occurred.
