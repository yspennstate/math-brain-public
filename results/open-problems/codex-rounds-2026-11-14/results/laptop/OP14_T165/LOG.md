# T165 work log

Session date: 2026-11-14. Work is confined to this directory; no git or external writes.

## 1. Initial reading and literature search

Read ~/AGENTS.md and the supplied task. Task-specific restrictions override its shared-memory/mesh/upload instructions: no shared registration or memory writes will be made.

Web searches (2026-11-14, beginning approximately 18:14 UTC):
- semimartingale reflecting Brownian motion positive recurrence four dimensions necessary sufficient 2024 2025 2026
- SRBM stability four dimensions Bramson positive recurrence criterion open problem
- "reflecting Brownian" "positive recurrence" "2026"
- "reflecting Brownian" "stability" "four" "2025"
- "semimartingale" "recurrence" "triangular" reflection matrix

Opened arXiv:1009.5746 and arXiv:1010.1751, and found and opened a substantial omitted advance:
Curtis Heyda, Construction of positive recurrent semimartingale reflecting Brownian motions with divergent fluid paths using predator–prey models, Queueing Systems 110, article 48 (published 11 October 2026), DOI 10.1007/s11134-026-10006-5.
https://link.springer.com/article/10.1007/s11134-026-10006-5

The paper constructs examples in dimensions four and five and proves covariance dependence already in dimension four. It does not give the general necessary-and-sufficient classification. Therefore work continues.

## 2. Concrete piece selected (before derivation)

Analyze the finite linear complementarity systems for Heyda's explicit four-dimensional reflection matrix, using exact arithmetic. Classify every constant-rate fluid solution, identify all divergent linear solutions, and test whether the covariance-dependent examples have a unique divergent support. This is a finite, checkable reduction of the still-open classification on the smallest dimension with covariance dependence; it avoids treating divergent fluid paths as a valid nonrecurrence test. A proof and an independently checked exact enumeration will be saved.

The reflection parameters stated in the paper's Section 5 are delta1=delta2=delta3=1/20, delta4=3/5, theta=(-1,-1,-1,-1). The full paper and exact hypotheses still need to be checked before using them.

## 3. Literature check closed; algebraic reduction

The literature phase ended by approximately 18:20 UTC, within ten minutes. The full text confirms the matrix and numbers above in (2.3.3)–(2.3.5) and (5.0.1). Saved SOLVED_ELSEWHERE.md; no arXiv identifier was found for Heyda's paper. Its Theorem 2.2 gives positive recurrence for beta >= 2.00046; Theorem 5.1 gives non-positive-recurrence for identity covariance with the same theta and R. Those stochastic results are cited, not reproved here.

The chosen finite calculation has a short symbolic reduction: middle-coordinate differences satisfy v_i-v_j=c(u_i-u_j), forcing equal middle regulator rates by complementarity. This reduces all 16 supports in dimension four (and all 32 in dimension five) to three scalar rates. The same calculation works for an arbitrary number m of middle coordinates. We will prove the resulting full parameter classification as part of this one linear-fluid piece, then audit it by two independent exact enumeration methods at fixed rational instances, including the threshold and both sides of it.

Provisional threshold found by subtraction: d=m(b+c), with a=delta1, b=delta2, c=delta3, d=delta4. The repeated-middle family is only an algebraic fluid family unless further stochastic hypotheses are supplied. No recurrence criterion is inferred from the calculation.
