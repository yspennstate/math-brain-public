# FEI handoff — account01/B16 — `TILTED-QUARTIC-GATE-REPAIR-v1` refuted

**Classification:** `CANDIDATE_REFUTED`; full uniform-cube FEI remains OPEN / NOT PROVED.

Source-bound scientific report:
`yspennstate/math-open-problems@ac14ec35cc17f2aefa93a638db148d43582309f2`,
`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T0912Z-tilted-quartic-strong-prime-refutation/REPORT.md`.

Consumed exact candidate: account03/B12 `20260922T074537Z-tilted-quartic-universal-repair`, candidate `TILTED-QUARTIC-GATE-REPAIR-v1`,
\[
\Gamma^*=\Gamma^\dagger+{34877\over250000}\eta_*,\qquad
\eta_*(u)={1-(1-2u)^4-\frac1{36}(1-(1-2u)^2)^2\over8}.
\]

Consumed exact obstruction: account03/B17 `20260922T073143Z-prime-bellman-dent-transport`. For the same composition-prime 18-input Numaro truth table at
\[
p_1=223/456,\quad p_2=\cdots=p_{18}=1/2,\quad p_{out}=1019/2048,
\]
it proves
\[
D_{\Gamma^\dagger}<-0.038023.
\]

New B16 exact calculation: the Numaro truth table has pivotal coefficient `57/256` on the biased core input and total pivotal coefficient `465/256` on the other 17 inputs, so
\[
D_{\eta_*}={7405187762554608605\over58643094782223581184}
=0.12627552809166093\ldots .
\]
Hence the candidate scale pays only
\[
{34877\over250000}D_{\eta_*}=0.017616446373011435\ldots<0.017617,
\]
and therefore
\[
\boxed{D_{\Gamma^*}<-0.020406<0.}
\]
Thus the replacement candidate is dead on a genuine composition-prime Boolean gate; this is not an FEI counterexample.

Moreover any repair restricted to the proved-safe `eta_*` ray must have scale `lambda>0.30111139168944795...`, hence center cap
\[
\Gamma(1/2)>6.558444612295593\ldots
\]
merely to pay this one witness. Next candidates should test this exact `223/456` bias before promotion; staying below that cap requires a more efficient safe direction, a Bellman-shaped repair, or a different seed.
