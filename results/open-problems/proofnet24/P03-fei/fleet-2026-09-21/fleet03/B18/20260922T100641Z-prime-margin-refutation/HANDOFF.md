# B18 handoff — `FEI-ALL-GATE-MARGIN-v1`

**Status:** `AND-DECOMPOSABLE-EXTREMALITY-v1` REFUTED; all-gate / prime-gate FEI target remains OPEN.

Fresh owner control converges FEI work on the all-gate margin. The relevant base is the committed read-once potential `Gamma_0`, with

\[
c_G(p)=-D_{\Gamma_0}(G;p)/M(G;p),\qquad
M=I/4-p_{out}(1-p_{out}).
\]

Consumed completed cross-account theorem: fleet02/B17 `20260922T004442Z-gate-composition-cocycle/REPORT.md`. It proves the exact slack and Poincare cocycles, hence every disjoint composite margin is a nonnegative weighted average of its factors and cannot exceed the worst factor margin.

The rigorous read-once certificate proves `Gamma_0+0.01 p(1-p)` pays every binary AND/OR constraint, hence every binary AND/OR read-once composition has `c_G<=0.01`.

The source-certified composition-prime 18-input Numaro gate at

\[
p_1=223/456,\quad p_2=\cdots=p_{18}=1/2,\quad p_{out}=1019/2048
\]

has exact

\[
M=62098577/239075328
\]

and certified `-0.038023735 < D_{Gamma^dagger} < -0.038023734` for `Gamma^dagger=Gamma_0+0.268204856 p(1-p)`. Therefore

\[
\boxed{c_G>0.4145936641982>0.01.}
\]

So the binary AND/read-once extremality claim is source-exactly false; the prime witness asks for more than `41.45x` the entire certified AND margin budget. This does not refute FEI. It refutes the stronger route that the read-once/AND constraint is globally extremal for the same scalar correction.

- `candidate_version`: `FEI-ALL-GATE-MARGIN-v1`.
- `failed_claim`: `AND-DECOMPOSABLE-EXTREMALITY-v1`.
- `new_proved_inference`: prime Numaro margin lower bound `>0.4145936641982`, versus certified read-once upper `0.01`; decomposable composition cannot amplify margin above factors.
- `replacement_obligation`: prove a finite-center repaired potential on every composition-prime Boolean gate and every interior product bias, or produce the next actual prime falsifier.
- `consumed_peer_artifact`: fleet02/B17 `20260922T004442Z-gate-composition-cocycle/REPORT.md`.
- `applied_to_claim`: exact reduction of normalized gate-margin extremality from composites to composition-prime factors.
- `next_recipients`: fleet02/B17 prime adversary; fleet04/B18 prime potential/Bellman integration; fleet03/B15 source-exact Gibbs/KL payment.
- `implication_to_full_FEI`: AND extremality cannot close FEI; universal prime-gate control for one finite potential remains unpaid. Full FEI OPEN / NOT PROVED.
