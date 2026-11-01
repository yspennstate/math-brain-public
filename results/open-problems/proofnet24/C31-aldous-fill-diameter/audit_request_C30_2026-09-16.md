# C31 -> C30 directed audit request: Aldous–Fill Open Problem 4.49(ii)

Outside source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs* (2002 manuscript; 2014 recompilation), Open Problem 4.49(ii).

Claim to audit: `C31-AF449-RAMANUJAN-CONE-1` — for every finite `M`, there is a finite connected simple unweighted graph `G` with

`F(G)/(tau_rel(G) D(G)) > M`,

where `F=inf_f psi(f)` uses the exact Aldous–Fill source normalization, `tau_rel=(1-lambda_2)^{-1}` for discrete-time simple random walk, and `D` is graph diameter. This refutes the source's SOME-universal-constant diameter replacement, not merely the constant-two strengthening.

Primary author reports:

- `proofnet24/C31-kemeny-constant/runs/2026-09-16/2026-09-16_14-54-31__run-report.md` (creation commit `c1fe8bd5a64733a6c42ed082c729df7bc1fac27b`).
- strengthening/direct weak-duality report: `proofnet24/C31-aldous-fill-diameter/runs/2026-09-16/2026-09-16T12-56-04Z__report.md` (creation commit `15d120344f2151bca2fe1477ae739130021b9e37`).

Existing independent audit:

- `P26-AUDIT-C31-AF449-RAMANUJAN-CONE-01 = PASS` in `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_16-01-15__run-report.md`, creation commit `d2ec9d45f78bc19e5e7cee4ad9365790305663f7`.

Please independently check, without treating P26 as authority:

1. source scope: Open Problem 4.49(ii) asks whether (4.49) holds with diameter in place of `log n` for some universal constant;
2. source normalization of `psi` and `tau_2=(1-lambda_2)^{-1}`;
3. direct weak-duality lemma from `div f^(a)=delta_a-pi` and `sum_e c_e ell_e<=1`;
4. cone stationary law and transition spectrum, including why the large negative bipartite eigenvalue does not define `tau_2`;
5. the MSS input: infinite connected simple `d`-regular bipartite Ramanujan graphs for each fixed `d>2`, sufficient to choose order above the explicit ball bound;
6. ball-growth estimate and the quantifier order `s` first, then a sufficiently large graph in the degree-`s^2` family;
7. explicit two-length budget, shortest-path identity, and inclusion of hub-base ordered pairs in the stronger lower bound;
8. exact simplification
   `L_s=((s-1)^2(s^2+3))/(2(s+1)(s^2+2)) > (s-3)/2`, hence unboundedness;
9. scope correction that the older strongly-regular-cone formula
   `F=2(r+1)(2q-r-1)/(q(r+2))<4`
   is capped and is not the unbounded construction;
10. exact checker/output under `proofnet24/C31-aldous-fill-diameter/artifacts/2026-09-16/`, including the current reexecution output `af449_direct_duality_recheck_1355Z.out` (creation commit `a7ac3359ef32e277d6872d5853deb66fe6b385b2`).

A separate pre-existing campaign paper package is present at `probability_campaign_2026_09/paper_flow_parameter_2026_09_16/` (commit `fe58dc55b6f399d12c8f09abb07bbb7ffceffec8`). It contains additional statements beyond the minimal C31 refutation. The directed audit requested here is claim-scoped to the source-level unbounded-ratio theorem above; do not infer that every extra statement in that paper package has been audited.

Required verdict format for fleet closure evidence: `C30-AUDIT-C31-AF449-RAMANUJAN-CONE-01 = PASS` or a precise failure with the first invalid step. This file is only an audit request; it is not an independent audit and does not change C31 status by itself.
