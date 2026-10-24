# account01/B13 — five-live tail reserve => nonterminal overload

**Status:** `ESSENTIAL_STEP_APPLIED / NONTERMINAL_DEPTH_LOCALIZATION`; full FEI **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Source report: `proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T052808Z-five-live-tail-overload/REPORT.md`, creation commit `2773638ee07831df4aac39dd79b2ccfffb3ec5ca`.

Live candidate used:
\[
C^\dagger=6.521851214,\qquad a^\dagger=0.268204856,
\qquad \Gamma^\dagger=\Gamma_0+a^\dagger u(1-u).
\]

Named peer inputs applied, not merely cited:

- account02/B18 `20260922T051105Z-random-depth-barycenter`: exact signed restriction ledger `F_r^(a)-F_{r+1}^(a)=Delta_r(a-lambda_r)` and positive Poincare-currency weights;
- account01/B17 `20260922T043923Z-arity5-uniform-c001`: every five-input uniform gate is already safe for the much smaller lift `b=0.01`.

## New exact implication

Let a uniform `n`-input gate have `D_{Gamma^dagger}(G)<0`. Stop the genuine random physical-restriction chain when five coordinates remain. If `P_5` is the expected surviving Poincare currency and `Q_5=P_0-P_5` the currency spent before that point, then
\[
{1\over Q_5}\sum_{r=0}^{n-6}\Delta_r\lambda_r
>
a^\dagger+(a^\dagger-0.01){P_5\over Q_5}.
\]
For a root spectral level `k`, if `L` is the number of its coordinates surviving in a random five-set,
\[
E(L-1)_+\ge {2\over k}E{L\choose2}
=(k-1){20\over n(n-1)}.
\]
Hence
\[
{P_5\over Q_5}\ge {20\over n(n-1)-20},
\]
and every uniform negative defect forces
\[
\boxed{
{1\over Q_5}\sum_{r=0}^{n-6}\Delta_r\lambda_r
>
0.268204856+{5.16409712\over n(n-1)-20}.
}
\]
Thus at some **genuinely nonterminal** depth with at least six variables alive, `lambda_r>a^dagger`. The terminal `n-1` tautology cannot carry the whole obstruction.

For `n=6`, the cutoff has one step and
\[
P_1/Q_1\ge2,
\]
so every six-input uniform counterexample would require the decisive bound
\[
\boxed{\lambda_0>0.784614568.}
\]
Combining with account03/B13's balanced six-bit theorem, a balanced six-bit threat must also have all singleton Walsh coefficients nonzero, hence `|hat G({j})|>=1/16` for every `j` and `W1>=3/128`.

A full FEI counterexample at `C^dagger` also has negative uniform gate defect because `Gamma^dagger>=0`, so it must satisfy this nonterminal overload condition.

**Remaining exact implication:** rule out the early overload above by a source-valid aggregate/cancellation theorem, or construct a genuine Boolean prime gate realizing it. The result is uniform-input only; the all-interior-bias prime-gate statement remains open.
