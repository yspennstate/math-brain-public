# FEI handoff — account04/B14 criticality-matched stopping

Status: **ESSENTIAL_STEP_APPLIED / FULL FEI OPEN / WITHOUT_VERIFIED_BRAIN**.

Scientific source: `yspennstate/math-open-problems`, report commit `af287715e4ad6faf21f0475a2bd25148692d5464`, report blob `79cf35fd1ddb48ccb9948081cc5ae6f3b13ce5b2`, path `proofnet24/P03-fei/fleet-2026-09-22/account04/B14/20260922T071120Z-criticality-matched-stopping/REPORT.md`.

Consumed source-exact account01/B18 curvature report: `account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`. Also consumed the newer account01/B18 owner-pivot correction, blob `13aacee16ac78f05d89cde2d493a115cf3579d6a`, so no old fixed-`Gamma^dagger` collar is promoted to universal evidence.

For a centered state and physical singleton `i`, write folded influence `q_i`, singleton posterior crossing `C_i`, exact folded drift `D_i=q_i+C_i=J(parent)-E J(child)`, and curvature refund `W_i=sum_{j!=i} j'(q_j)c_j({i})>=0`.

Since the spectral bit has marginal `q_i`, `B_i<=h_2(q_i)`. For any `K>2`, query original coordinate `i` only when

`h_2(q_i)-W_i < K D_i`.

The account01/B18 inequality gives `Delta_i F<=B_i-W_i`, hence the physical tree satisfies

`F(root)-E F(leaf) <= K[J(root)-E J(leaf)]`.

A stronger literal-Shannon subpolicy uses `h_2(q_i)<K D_i` and gives `sum_v pi_v B_i <= KJ(root)`.

Every terminal leaf satisfies for every original coordinate

`h_2(q_i)-W_i >= K(q_i+C_i)`.

Consequently `q_i<=sigma_K`, where `h_2(sigma_K)=K sigma_K`, and

`C_i<=delta_K=log_2(1+2^{-K})/K`.

At `K=4`, `sigma_4=0.156417354964272...` and `delta_4=(1/4)log_2(17/16)=0.02186571031258485...`.

Exact source-to-next-arrow use: on an `F/J`-critical core of ratio `rho`, account01/B18 gives `B_i>=rho(q_i+C_i)+W_i`. Together with `B_i<=h_2(q_i)`, this yields `h_2(q_i)-W_i>=rho D_i` for every physical coordinate. Thus a ratio-`rho` critical core is exactly terminal for the new rule at `K=rho`.

Compiler: if every centered terminal state satisfying `h_2(q_i)-W_i>=K(q_i+C_i)` for all `i` obeys `F<=KJ`, then the stopping telescope gives `F<=KJ` for every Boolean function, hence `H<=(K+2/ln 2)J<=(K+2/ln 2)I`.

Remaining arrow: prove that terminal-class bound by a dimension-free compatibility argument, or construct a genuine Boolean counterexample to it. Do **not** sum the per-coordinate `delta_K` bound with a factor of dimension. Preserve the addressing obstruction: this is adaptive selection, not prescribed-coordinate payment. Full FEI remains OPEN.