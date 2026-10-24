# account04/B15 handoff — exact continuous-output extremal envelope

Programme \`QFORM-DENSITY-3EIG-20260922\`, revision \`2026-09-22.5\`. Classification: \`ESSENTIAL_STEP_APPLIED / EXACT_TARGET_LEVEL_REGULARITY_REDUCTION\`. Full QFORM remains **OPEN**. Execution: \`WITHOUT_VERIFIED_BRAIN\`.

Canonical report: \`yspennstate/math-open-problems@07672b7beb8f867c7a7b973aa3157a42ae506460\`, path \`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T152333Z-b15-qform-continuous-envelope-r3/REPORT.md\`.

Named partner actually applied: account01/B15 at \`yspennstate/math-open-problems@5e161df12dcfebf0d13eb7efeaef5c478bf09455\`, path \`proofnet24/QFORM-density/fleet-2026-09-22/account01/B15/20260922T150652Z-account01-B15-qform-r11/REPORT.md\`.

Define \(C_{\rm all}\) as the optimal interval-density constant over the full target class, \(C_{C_0}\) over target instances whose output density belongs to \(C_0(\mathbb R)\), and \(C_{\rm sm}\) over compactly supported smooth cap-one marginals. The proved target-level conclusion is
\[
\boxed{C_{\rm all}=C_{C_0}=C_{\rm sm}}
\]
including \(+\infty\). Thus failure of any proposed finite constant already has a smooth-input, continuous-output witness; for every rough target density \(p\) and \(\eta>0\), a smooth target output \(p_\eta\in C_0\) has \(\|p_\eta\|_\infty\ge\|p\|_\infty-\eta\).

Applying the partner Fresnel estimate gives: if \(r=\operatorname{rank}(A)\ge3\) and \(B=2^{-r}\pi^{-r/2}|\det\Lambda|^{-1/2}\|\widehat h\|_1\), then
\[
\|p\|_\infty\le \frac{r}{\pi(r-2)}B^{2/r},\qquad p\in C_0.
\]
This remains instance-dependent and does not resurrect uniform pointwise decay.

Continuity of every rough-input target output remains open. Total variation plus a common \(L^\infty\) cap cannot transfer continuity: \(1_{[0,1]}*\eta_\varepsilon\) are smooth cap-one probabilities converging in \(L^1\) to discontinuous \(1_{[0,1]}\). This is an inference obstruction, not a QFORM counterexample. The next step is a target-specific scale-coherence estimate or a genuine rough-input discontinuity construction.
