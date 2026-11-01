# C0052 referee packet — w479, 2026-10-10

## Source and status

Primary source: Duminil-Copin, arXiv:1707.00520, Section 7, equations (7.1)-(7.2), Conjecture 6, and Exercise 61(1). See SOURCE_STATUS.json. The exact definition is near-critical nonvanishing of g(beta), a normalized infinite-volume sum of U4. Current 3D openness is UNKNOWN after bounded checks. Aizenman–Duminil-Copin arXiv:1912.07973 proves 4D Gaussianity, not this 3D statement. Neither peer proves C0052.

## Verdicts on peer artifacts

| Artifact | Verdict | Independent reproduction | Scope and gap |
|---|---|---|---|
| w477/LEMMA_L001.md and its CLAIMS row | KEEP, scoped | Uniform integrability of |X_n|^4 plus weak convergence gives convergence of moments 1,2,4 by truncation. The variance and fourth deficit pass to X; Gaussian N(0,1) has fourth moment 3. | Elementary conditional lemma only. It does not supply the 3D Ising deficit or compare it with g(beta). |
| w477/STATEMENT_FIRST.md | FIX | It defines critical smeared fields with finite-volume variance normalization; source equations (7.1)-(7.2) instead use beta up to beta_c, susceptibility and correlation length. | Keep as a possible auxiliary route, explicitly add the missing critical-to-near-critical comparison and field-limit assumptions. |
| w478/ATTEMPT.md L1 | KEEP, scoped | A fourth-moment upper bound C gives E[X_n^2 1(|X_n|>R)]<=C/R^2. This transfers mean and variance under weak convergence. Portmanteau gives E X^4<=liminf E X_n^4<=3-epsilon, hence non-Gaussian. | Stronger than w477 L001 for a one-sided fourth-moment bound; still conditional on the missing Ising estimate. |
| w478/ATTEMPT.md L2 | KEEP, scoped | If N_n=n^2 with probability 1/n and zero otherwise, E N_n=n while P(N_n>0)=1/n. Cauchy-Schwarz gives P(N>0)>=(EN)^2/EN^2 for any nonnegative N with finite second moment. | Correct logical obstruction to first-moment-only overlap arguments; not an Ising-current counterexample. |
| historical C0052-A001 / math-store random-current reduction node | DROP as a proved equivalence; FIX as a heuristic | Exercise 61 has two endpoint-dependent source laws and correlation factors. The exact finite-graph identity in ATTEMPT.md yields a p_f-weighted event, while g(beta) integrates U4 over all triples at beta<beta_c. No weight, scale window or localization comparison appears in the old record. | Do not inject the sentence claiming an unweighted uniform intersection probability is equivalent to C0052. The current-cluster dimension calculation is also only heuristic. |

The hardest load-bearing peer claim was w478 L1: its one-sided fourth-moment transfer is sound even without fourth-power uniform integrability, because portmanteau needs only an upper bound to exclude N(0,1). I independently checked the variance passage using the explicit C/R^2 tail estimate above. w477 L001 is also sound, with stronger hypotheses.

## Own derivation and independent review request

ATTEMPT.md derives the exact finite-graph weighted-current identity. The two-spin exact control is reproducible with `python -X utf8 two_spin_check.py`. This is a known consequence of the switching identity, with no novelty claim. **w482 must audit the source formula, repeated-endpoint convention and weighting before this own lemma receives any KEEP or theorem status.** Requested status: preliminary sketch. No response-side served-model evidence is available in this packet; a requested model name is not a receipt.

The same finite-graph identity independently appears as w477 L002 and w478 L3. My derivation is an independent reproduction of those peer claims, not a separate novelty claim. The w482 request was delivered via direct mesh as `msg-6f9c967672` after `team_comm.py` failed twice (database lock, then no-team routing).

## Later peer proof audit

All item verdicts and reproductions are in AUDIT_VERDICTS.jsonl. In particular w477 L002-L007 receive scoped KEEP. The load-bearing L007 is source-faithful: setting z=y+r in equation (3.11), stationarity and susceptibility-normalized endpoint sampling give `-g(beta)=2 xi(beta)^-3 sum_y p_y`. Restriction to a cube of `ceil(xi)^3` translated roots, single-current overlap inclusion, and Cauchy-Schwarz give `-g(beta)>=2/Q_beta`. I independently checked the factor 2, the root normalization, Tonelli's nonnegative summands, and repeated sources. The required bounded Q_beta along beta up to beta_c is wholly unproved.

w478 L1-L4 also receive scoped KEEP. L4 gives a direct block-Ursell comparison to the source coupling under explicit near-critical variance and deficit premises. Its draft edge E2 needs FIX: the finite weighted-current identity does not depend on the weak-limit moment-transfer lemma, so `weighted -> moment` must not be `depends_on`. Other reviewed concept relations are scoped KEEP.

## Unresolved parent gap

The tightest peer reduction now names the missing estimate precisely: prove a bound on `Q_beta=E[I_beta^2]/(E[I_beta])^2` along a sequence beta increasing to beta_c for w477's susceptibility-endpoint single currents and correlation-length random root. Its exact identity already handles the global U4 normalization, so a separate box-to-global comparison is unnecessary for that route. The alternative w478 L4 needs both a near-critical block deficit and variance comparability. Neither set of premises is proved. A KEEP on any row here is not a C0052 solution.
