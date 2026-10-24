# account01/B15 handoff — exact restriction I-projection chain

**Programme:** FEI-ALL-TEAM-20260922T095941Z  
**Control revision consumed:** 2026-09-22.3  
**Classification:** ESSENTIAL_STEP_APPLIED  
**Full FEI:** OPEN / NOT PROVED  
**Recipient:** account03/B17

## Immutable scientific source

- repository: `yspennstate/math-open-problems`
- final source commit for this run: `3a5fccff414043be05a0c7f2f219dabd9b44708b`
- report: `proofnet24/P03-fei/fleet-2026-09-22/account01/B15/b15-20260922T103236Z-restriction-iprojection-chain/REPORT.md`
- claims: same folder, `CLAIMS.json`
- checker/output: same folder, `CHECKER.py`, `CHECKER_OUTPUT.txt`
- correction: same folder, `CORRECTION.md` (only clarifies that the first child coefficient in Section 2 is Latin `u_T`; mathematics unchanged)

## Exact theorem to consume

For a genuine physical restriction of coordinate `j` at actual bias `s`, let `W` be the parent full spectral law, `U,V` the two child full spectral laws, and let

`Kcal(X) = v_X K_occ(X^+) = D(X || M(v_X,rho_X))`,

where `M(v,rho)` is the maximum-entropy full law with the same empty/nonempty mass and original-coordinate occurrence marginals. Put `E=(1-s)U+sV`, `R_b=M(v_b,rho^b)`, `bar R=M(bar v,bar rho)`, let `R^-` be the parent I-projection reference after erasing `j`, and define

- `C_marg=(1-s)D(R_0||bar R)+sD(R_1||bar R)`;
- `C_erase=D(bar R||R^-)`;
- `C_pair=sum_T E_T d_2(q_T||theta_T)` for the true/reference selector posteriors;
- `JS_s(U,V)=(1-s)D(U||E)+sD(V||E)`.

Then exactly

\[
\boxed{
Kcal(W)=(1-s)Kcal(U)+sKcal(V)+C_{marg}+C_{erase}+C_{pair}-JS_s(U,V).
}
\]

All three `C` terms are nonnegative, and the occurrence-marginal movement term is exactly

\[
C_{marg}=Hscr(\bar v,\bar\rho)-(1-s)Hscr(v_0,\rho^0)-sHscr(v_1,\rho^1)\ge0.
\]

Using account03/B15's exact physical packet theorem at commit `8793c7e49e1de7921bc76c7724c92fae03024e26`,

\[
JS_s(U,V)\le\kappa(s)\,It_j,
\]

so

\[
\boxed{
vK_{occ}(G)\ge(1-s)v_0K_0+s v_1K_1-\kappa(s)It_j.}
\]

The child dependence KL survives with coefficient exactly one. This is substantively compatible with the consumed account02/B15 no-loss theorem at commit `b5bf5c990f3597cf26c2aa0ab1eabea4ae9ea277`, which proves that any fixed multiplicative loss of `K_occ` is fatal on sparse Boolean suspensions even with an `O(J)` bank.

## Negative entropy term is essential

The universal stronger shortcut `Kcal(parent) >= weighted child Kcal` is false. The report gives a genuine four-bit Boolean witness with truth table

`(1,1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1)`

restricted on bit 0. Its parent spectrum is uniform on all 16 subsets, so parent `Kcal=0`; the two child spectra are disjoint four-atom laws, hence `JS=1` bit exactly. Numerically the child average is `0.783110158260427`, `C_marg=0.216889841739573`, and `C_erase=C_pair=0`, so the exact ledger closes at zero. Thus the `-JS` sign cannot be dropped.

## Multiscale consequence and next unpaid implication

Iteration down a physical restriction tree gives exactly

\[
Kcal(root)=E[Kcal(leaves)]+\sum_u\pi_u(C_{marg,u}+C_{erase,u}+C_{pair,u}-JS_u).
\]

This retains all scales and does not make the recursive-majority-refuted fixed/low-depth KL compression.

**Next unpaid implication:** combine this signed multiscale KL ledger with the corresponding Bellman/influence increment so that accumulated negative `JS` terms are paid by physical selector-price/branch credits, while preserving full `K_occ` to additive-influence scale and retaining high-cardinality dependence. A valid joint node inequality would telescope; otherwise seek a genuine Boolean counterexample to that joint inequality.

**Execution context:** WITHOUT_VERIFIED_BRAIN. Repository synchronization only; no native memory ingestion is claimed.
