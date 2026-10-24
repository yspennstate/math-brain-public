# account01/B16 FEI handoff — adaptive MUX data-boundary theorem

**Classification:** `ESSENTIAL_STEP_APPLIED`; full FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific artifact:
`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T0657Z-adaptive-mux-data-boundary/REPORT.md`, report blob `6e0c7ada7d87c05be8f57d468a2fa566fa6bd0dd`.

Exact peer consumed/applied: account04/B12 `20260922T0452Z-unequal-mux-cross-deficit`, blob `59ea7f1466e7abeff9d9756654fd6c4efa2bda98`. Its theorem says any live-candidate MUX counterexample must satisfy
\[
R_1^\dagger<-0.258204856\,Q_0,
\qquad Q_0=p(1-p)q_0(1-q_0).
\]

New theorem. Orient `q_0=x`, `q_1=y`, put
\[
Q=p(1-p)x(1-x),\qquad L=\log_2(16/Q).
\]
For every interior `p,x`, if
\[
0\le y\le {Q\over176L},
\]
then the live candidate satisfies
\[
D_{\Gamma^\dagger}(MUX;p,x,y)\ge0.
\]
The proof uses the actual physical `D_1` split. Source h96 derivative/size bounds and the exact six-mass MUX law give
\[
R_1^\dagger>-\frac{21}{88}Q>-\frac14Q,
\]
contradicting the peer cross-deficit requirement because `0.258204856>1/4`. By branch exchange/data-output complementation the same adaptive collar holds near every deterministic data face.

At `p=x=1/2`, the radius is `1/22528`, over five times the previous fixed `2^-17` compact-core radius. More importantly, there is no longer any `[1/8,7/8]` hypothesis: the radius automatically follows the exact physical currency as the other biases approach their boundaries.

Next unpaid MUX region: both data biases outside these adaptive boundary layers and outside the already-certified zero-credit/complementary/same-cell tubes. The source-exact sufficient target remains
\[
R_0^\dagger+R_1^\dagger\ge-0.258204856(Q_0+Q_1).
\]
Closing MUX is still weaker than the universal composition-prime gate implication.
