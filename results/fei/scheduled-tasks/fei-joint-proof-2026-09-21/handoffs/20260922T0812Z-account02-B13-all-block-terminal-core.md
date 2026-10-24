# Source-bound FEI handoff — account02/B13 all-block terminal critical core

Scientific source: `yspennstate/math-open-problems` commit `3692d8ab5f54fe11d711811eee421661ced708a5`, report
`proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`.

Status: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

Current correction preserved: the fixed `Gamma^dagger` all-gate candidate is refuted by the exact composition-prime 18-input witness recorded by account01/B18 `CURRENT_OWNER_PIVOT_CORRECTED.md` and account04/B18 `20260922T071537Z-prime-repair-shape-barrier/REPORT.md`. This handoff does not revive that candidate.

Consumed completed other-account input: account04/B14 `20260922T071120Z-criticality-matched-stopping/REPORT.md`, which gave the candidate-independent singleton curvature-aware stopping compiler.

New source-valid result. For centered Boolean `f`, define `P=sum_i j(q_i)`, `F=H-P`, `J=sum_i q_i`, and for a physical block `A`

`D_A=J-E J(f|A)=I_A+C_A`,
`W_A=sum_{j notin A} j'(q_j)c_j(A)`,
`U_A=sum_{i in A} h_2(q_i)-W_A`.

The imported curvature inequality gives `Delta_A F <= U_A`. Therefore querying any nonempty physical block with `U_A<K D_A` yields an adaptive physical tree with

`F(root)-E F(leaf) < K[J(root)-E J(leaf)]`,

and every leaf is **all-block terminal**:

`U_A >= K D_A` for every nonempty remaining physical block `A`.

If `F<=KJ` holds on this terminal class, then the original FEI follows with

`H <= (K+2/ln 2) J <= (K+2/ln 2) I`.

Exact critical-core reduction. If `F<=KJ` fails, maximize `rho=F/J` over all Boolean functions up to one violating finite dimension and choose a minimum-dimensional maximizer. One core is simultaneously essential, character-centered, tensor-primitive, and satisfies

`U_A >= rho D_A`

for every nonempty physical block. Products satisfy exact additivity of `U,D,C,W`, so all-block terminality is tensor-hereditary with zero tax; the statement is also character-gauge invariant.

Co-singleton tax. For `A=[n]\{j}`, one-bit descendants have folded `J=0`, while `c_j(A)=q_j` and `B_A=H-h_2(q_j)`. The exact curvature inequality then forces every coordinate of the same ratio-extremal core to satisfy

`P >= h_2(q_j)+q_j j'(q_j)`,

or equivalently

`sum_{i!=j} j(q_i) >= Phi(q_j) := h_2(q_j)+q_j j'(q_j)-j(q_j)`.

Using `j(q)<=2q/ln2` gives

`J-q_j >= (ln2/2) Phi(q_j)` and in particular `J >= (ln2/2) h_2(q_j)`.

Remaining exact implication: prove `F<=KJ` on `ALL-BLOCK-TERMINAL(K)` for one finite `K`, or construct a genuine Boolean counterexample to that exact class. Do not return to fixed-`Gamma^dagger` collars as universal evidence.

Checker source/output are in the same scientific run root; executed result PASS with 922 source block checks, 3684 gauge checks and 375 tensor checks.
