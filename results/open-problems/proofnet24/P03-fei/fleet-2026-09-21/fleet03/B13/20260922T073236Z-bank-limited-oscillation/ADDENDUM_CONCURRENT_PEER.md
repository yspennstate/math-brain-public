# Addendum — concurrent sharper peer theorem closes the entire uniform-bank repair class

**Updated run classification:** `ESSENTIAL_STEP_APPLIED / UNIFORM_BANK_REPAIR_REFUTED`; full uniform-cube FEI remains **OPEN / NOT PROVED**.

After the main report in this run was committed, a source-compatible stronger result arrived from **fleet01/B13**:

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B13/20260922T073227Z-bellman-and-bank/REPORT.md`

scientific commit `0e7f3ca7bdd6c71b1a208776f57bd51b479730c9`.

It sharpens the fleet02/B17 charged-AND constant by using the same 253-cycle plus a second exact AND bridge.  For every bounded symmetric center-zero perturbation satisfying
\[
L_{p,q}(\psi)\ge-KM(p,q),
\qquad M=pq(1-p)(1-q),
\]
it proves
\[
R_{wit}(\psi):={57\over256}\psi(3/8)-\psi(967/2048)
\le \kappa K,
\]
with exact-rational
\[
\kappa=0.0676346063971711006296130\ldots<0.067635.
\]

The guaranteed quadratic AND bank inside the refuted `Gamma^dagger` is
\[
A=0.258204856.
\]
Therefore
\[
\kappa A
=0.0174635838053982428454308\ldots
<0.017611,
\]
whereas the exact composition-prime Numaro witness needs more than `0.017611` repair.  Hence the entire **center-preserving uniform-bank repair class** considered in the main report is impossible, not merely the degree-20 polynomial subclass.

The peer further proves the non-increasing-center extension: after subtracting the quadratic center component, any bounded symmetric perturbation with `psi(1/2)<=0` financed solely by the same uniform bank is also impossible.  Its residual gap is
\[
0.017611-\kappa A>0.00014741619.
\]

## Application to this run

The main report's exact ten-constraint polynomial dual remains valid mathematics, but the concurrent theorem strictly dominates its route-specific conclusion.  Its useful independent role is now diagnostic: low-degree repairs already fail by a factor `>5.6057`, while the sharper peer theorem shows **no amount of oscillatory complexity can rescue a perturbation that uses only the uniform bank**.

Thus the replacement obligation becomes exact:

> Any viable all-gate potential repair at the current or lower center must spend the **detailed nonuniform residual slack** of the certified read-once/AND potential somewhere; a free/local dent or a uniform-bank-only dent is impossible.

This plugs directly into the prime-Bellman envelope interpretation supplied in the same fleet01/B13 report.  The next calculation should evaluate the actual certified read-once AND residual on the finite dual/bridge constraints and then test the full one-coordinate Numaro bias line.  Do not spend another run designing a uniform-bank-only correction.

**Consumed_peer_artifact (new):** fleet01/B13 `20260922T073227Z-bellman-and-bank/REPORT.md`, commit `0e7f3ca7bdd6c71b1a208776f57bd51b479730c9`.

**Applied_to_claim:** feasibility of a finite-cap replacement potential after the exact biased-prime refutation.

**Remaining_implication:** quantify and spend the actual pointwise residual AND slack of the certified read-once potential inside the prime-Bellman envelope; then prove nonnegativity of all finite gate costs or extract a genuine gate/bias obstruction.

**Next_recipient:** `fleet03/B18` primary; `fleet01/B18` and `fleet04/B18` for envelope integration.
